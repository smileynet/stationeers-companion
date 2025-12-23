"""IC10 code validator with tree-sitter parsing and rule-based checking."""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

from rich.console import Console

from . import config

console = Console()


# =============================================================================
# Data Classes
# =============================================================================


@dataclass
class ValidationIssue:
    """A single validation issue found in IC10 code."""

    severity: str  # "error", "warning", "info"
    line: int  # 1-indexed line number
    column: Optional[int]  # 1-indexed column, or None
    message: str
    rule: str  # Rule ID (e.g., "E001")


@dataclass
class ValidationStats:
    """Statistics about the validated code."""

    lines: int
    lines_of_code: int  # non-empty, non-comment lines
    bytes: int
    registers_used: list[str] = field(default_factory=list)
    devices_used: list[str] = field(default_factory=list)
    labels_defined: list[str] = field(default_factory=list)


@dataclass
class ValidationResult:
    """Complete result of validating IC10 code."""

    passed: bool
    stats: ValidationStats
    errors: list[ValidationIssue] = field(default_factory=list)
    warnings: list[ValidationIssue] = field(default_factory=list)
    info: list[ValidationIssue] = field(default_factory=list)
    parser_available: bool = True

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "passed": self.passed,
            "stats": asdict(self.stats),
            "errors": [asdict(e) for e in self.errors],
            "warnings": [asdict(w) for w in self.warnings],
            "info": [asdict(i) for i in self.info],
            "parser_available": self.parser_available,
        }


# =============================================================================
# Validator Class
# =============================================================================


class IC10Validator:
    """Validates IC10 code for Stationeers."""

    def __init__(self):
        self.parser = None
        self.language = None
        self._try_load_parser()

        # Build instruction set from config
        self.valid_instructions = set(config.ALL_INSTRUCTIONS)

        # Regex patterns for fallback parsing
        self._patterns = {
            "comment": re.compile(r"^\s*#.*$|^\s*//.*$"),
            "label": re.compile(r"^(\w+):"),
            "instruction": re.compile(r"^\s*(\w+)(?:\s+(.*))?$"),
            "register": re.compile(r"\br([0-9]+)\b|\b(ra|sp)\b"),
            "device": re.compile(r"\bd([0-9]+)\b|\b(db|dr)\b"),
            "alias": re.compile(r"^\s*alias\s+(\w+)\s+(\w+)"),
            "define": re.compile(r"^\s*define\s+(\w+)\s+(.+)"),
        }

    def _try_load_parser(self) -> None:
        """Try to load tree-sitter parser if available."""
        try:
            import tree_sitter

            if config.GRAMMAR_PATH.exists():
                self.language = tree_sitter.Language(str(config.GRAMMAR_PATH), "ic10")
                self.parser = tree_sitter.Parser()
                self.parser.set_language(self.language)
        except (ImportError, OSError, Exception):
            # tree-sitter not available or grammar not built
            self.parser = None
            self.language = None

    def validate(self, code: str) -> ValidationResult:
        """Validate IC10 code and return structured results."""
        issues: list[ValidationIssue] = []
        lines = code.split("\n")

        # Gather statistics
        stats = self._gather_stats(code, lines)

        # Run all checks
        issues.extend(self._check_constraints(code, lines))
        issues.extend(self._check_syntax(code, lines))
        issues.extend(self._check_registers(lines))
        issues.extend(self._check_devices(lines))
        issues.extend(self._check_labels(lines))
        issues.extend(self._check_loops(lines))

        # Categorize issues
        errors = [i for i in issues if i.severity == "error"]
        warnings = [i for i in issues if i.severity == "warning"]
        info = [i for i in issues if i.severity == "info"]

        # Determine pass/fail
        passed = len(errors) == 0

        return ValidationResult(
            passed=passed,
            stats=stats,
            errors=errors,
            warnings=warnings,
            info=info,
            parser_available=self.parser is not None,
        )

    def _gather_stats(self, code: str, lines: list[str]) -> ValidationStats:
        """Gather statistics about the code."""
        registers_used: set[str] = set()
        devices_used: set[str] = set()
        labels_defined: list[str] = []
        lines_of_code = 0

        for line in lines:
            stripped = line.strip()

            # Skip empty lines and comments
            if not stripped or stripped.startswith("#") or stripped.startswith("//"):
                continue

            lines_of_code += 1

            # Extract label if present
            label_match = self._patterns["label"].match(stripped)
            if label_match:
                labels_defined.append(label_match.group(1))

            # Extract registers
            for match in self._patterns["register"].finditer(line):
                if match.group(1):  # r0-r15
                    registers_used.add(f"r{match.group(1)}")
                elif match.group(2):  # ra, sp
                    registers_used.add(match.group(2))

            # Extract devices
            for match in self._patterns["device"].finditer(line):
                if match.group(1):  # d0-d5
                    devices_used.add(f"d{match.group(1)}")
                elif match.group(2):  # db, dr
                    devices_used.add(match.group(2))

        return ValidationStats(
            lines=len(lines),
            lines_of_code=lines_of_code,
            bytes=len(code.encode("utf-8")),
            registers_used=sorted(registers_used),
            devices_used=sorted(devices_used),
            labels_defined=labels_defined,
        )

    def _check_constraints(self, code: str, lines: list[str]) -> list[ValidationIssue]:
        """Check hard constraints (line count, line length, code size)."""
        issues = []

        # E002: Line count
        if len(lines) > config.MAX_LINES:
            issues.append(
                ValidationIssue(
                    severity="error",
                    line=config.MAX_LINES + 1,
                    column=None,
                    message=f"Line count ({len(lines)}) exceeds maximum ({config.MAX_LINES})",
                    rule="E002",
                )
            )

        # W001: Line length
        for i, line in enumerate(lines, 1):
            if len(line) > config.MAX_LINE_LENGTH:
                issues.append(
                    ValidationIssue(
                        severity="warning",
                        line=i,
                        column=config.MAX_LINE_LENGTH + 1,
                        message=f"Line length ({len(line)}) exceeds recommended maximum ({config.MAX_LINE_LENGTH})",
                        rule="W001",
                    )
                )

        # I001: Code size approaching limit
        code_bytes = len(code.encode("utf-8"))
        if code_bytes > config.MAX_CODE_SIZE * 0.9:
            issues.append(
                ValidationIssue(
                    severity="info" if code_bytes <= config.MAX_CODE_SIZE else "error",
                    line=1,
                    column=None,
                    message=f"Code size ({code_bytes} bytes) approaching limit ({config.MAX_CODE_SIZE} bytes)",
                    rule="I001" if code_bytes <= config.MAX_CODE_SIZE else "E007",
                )
            )

        return issues

    def _check_syntax(self, code: str, lines: list[str]) -> list[ValidationIssue]:
        """Check syntax and instruction validity."""
        issues = []

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Skip empty lines and comments
            if not stripped or stripped.startswith("#") or stripped.startswith("//"):
                continue

            # Remove inline comments
            if "#" in stripped:
                stripped = stripped[: stripped.index("#")].strip()
            if "//" in stripped:
                stripped = stripped[: stripped.index("//")].strip()

            if not stripped:
                continue

            # Check for label definition
            label_match = self._patterns["label"].match(stripped)
            if label_match:
                # Remove label prefix for instruction parsing
                stripped = stripped[label_match.end() :].strip()
                if not stripped:
                    continue  # Label-only line is valid

            # Parse instruction
            instr_match = self._patterns["instruction"].match(stripped)
            if instr_match:
                instruction = instr_match.group(1).lower()

                # E003: Unknown instruction
                if instruction not in self.valid_instructions:
                    issues.append(
                        ValidationIssue(
                            severity="error",
                            line=i,
                            column=1,
                            message=f"Unknown instruction '{instruction}'",
                            rule="E003",
                        )
                    )

        return issues

    def _check_registers(self, lines: list[str]) -> list[ValidationIssue]:
        """Check for invalid register references."""
        issues = []
        valid_register_nums = set(range(16))

        for i, line in enumerate(lines, 1):
            # Find all register references
            for match in self._patterns["register"].finditer(line):
                if match.group(1):  # Numbered register r0-r15
                    reg_num = int(match.group(1))
                    if reg_num not in valid_register_nums:
                        issues.append(
                            ValidationIssue(
                                severity="error",
                                line=i,
                                column=match.start() + 1,
                                message=f"Invalid register 'r{reg_num}' (valid: r0-r15, ra, sp)",
                                rule="E004",
                            )
                        )

        return issues

    def _check_devices(self, lines: list[str]) -> list[ValidationIssue]:
        """Check for invalid device references."""
        issues = []
        valid_device_nums = set(range(6))

        for i, line in enumerate(lines, 1):
            # Find all device references
            for match in self._patterns["device"].finditer(line):
                if match.group(1):  # Numbered device d0-d5
                    dev_num = int(match.group(1))
                    if dev_num not in valid_device_nums:
                        issues.append(
                            ValidationIssue(
                                severity="error",
                                line=i,
                                column=match.start() + 1,
                                message=f"Invalid device 'd{dev_num}' (valid: d0-d5, db, dr)",
                                rule="E005",
                            )
                        )

        return issues

    def _check_labels(self, lines: list[str]) -> list[ValidationIssue]:
        """Check for undefined branch targets."""
        issues = []

        # First pass: collect all defined labels
        defined_labels: set[str] = set()
        aliases: dict[str, str] = {}

        for line in lines:
            # Strip BOM and whitespace
            stripped = line.lstrip("\ufeff").strip()

            # Check for label definition
            label_match = self._patterns["label"].match(stripped)
            if label_match:
                defined_labels.add(label_match.group(1))

            # Check for alias (which can create label-like references)
            alias_match = self._patterns["alias"].match(stripped)
            if alias_match:
                aliases[alias_match.group(1)] = alias_match.group(2)

            # Check for define (numeric constants)
            define_match = self._patterns["define"].match(stripped)
            if define_match:
                # Defines can be used as labels in some cases
                defined_labels.add(define_match.group(1))

        # Second pass: check branch targets
        branch_pattern = re.compile(
            r"^\s*(?:\w+:)?\s*(j|jr|jal|b\w+)\s+(?:[^,]+,\s*)?(?:[^,]+,\s*)?(\w+)\s*",
            re.IGNORECASE,
        )

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith("//"):
                continue

            # Remove inline comments before parsing
            if "#" in stripped:
                stripped = stripped[: stripped.index("#")].strip()
            if "//" in stripped:
                stripped = stripped[: stripped.index("//")].strip()

            if not stripped:
                continue

            # Check for branch instructions
            branch_match = branch_pattern.match(stripped)
            if branch_match:
                instruction = branch_match.group(1).lower()
                target = branch_match.group(2)

                # Skip if target is a number (relative jump) or register
                if target.isdigit() or target.startswith("-") or target in ("ra", "sp"):
                    continue
                if re.match(r"^r\d+$", target):
                    continue

                # Skip indirect register references (rr0, rr1, rrX, etc.)
                if re.match(r"^rr\d+$", target) or re.match(r"^rr\w+$", target):
                    continue

                # Skip indirect device references (dr0, dr1, drX, etc.)
                if re.match(r"^dr\d+$", target) or re.match(r"^dr\w+$", target):
                    continue

                # For bdns/bdse/brdns/brdse, the first arg after instruction is a device, not a label
                # The pattern captures the last word, which for these is still the label
                # But if instruction is bdns/bdse and target is an alias, it's checking device
                if instruction in (
                    "bdns",
                    "bdse",
                    "brdns",
                    "brdse",
                    "bdseal",
                    "bdnsal",
                ):
                    # These instructions: bdns device label
                    # The target we captured might be the device alias, check if next word exists
                    parts = stripped.split()
                    if len(parts) >= 3:
                        # Last part should be the label, but might be captured wrong
                        # If target is a device alias, skip it
                        if target in aliases:
                            continue

                # Check if target is defined
                if target not in defined_labels and target not in aliases:
                    issues.append(
                        ValidationIssue(
                            severity="error",
                            line=i,
                            column=None,
                            message=f"Undefined branch target '{target}'",
                            rule="E006",
                        )
                    )

        return issues

    def _check_loops(self, lines: list[str]) -> list[ValidationIssue]:
        """Check for yield/sleep in loops."""
        issues = []

        # Simple heuristic: find backward jumps and check for yield between target and jump
        label_lines: dict[str, int] = {}
        jump_lines: list[tuple[int, str]] = []  # (line_num, target)

        # First pass: collect labels and jumps
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith("//"):
                continue

            # Collect labels
            label_match = self._patterns["label"].match(stripped)
            if label_match:
                label_lines[label_match.group(1)] = i

            # Collect unconditional jumps
            instr_match = self._patterns["instruction"].match(stripped)
            if instr_match:
                instr = instr_match.group(1).lower()
                args = instr_match.group(2) or ""

                if instr == "j":
                    # Simple jump - target is the first (and only) argument
                    target = args.split()[0] if args.split() else ""
                    if target and not target.isdigit() and not target.startswith("-"):
                        jump_lines.append((i, target))

        # Second pass: check for backward jumps without yield
        for jump_line, target in jump_lines:
            if target in label_lines:
                target_line = label_lines[target]
                if target_line < jump_line:
                    # This is a backward jump (potential loop)
                    has_yield = False

                    # Check lines between target and jump for yield/sleep
                    for i in range(target_line, jump_line + 1):
                        if i <= len(lines):
                            check_line = lines[i - 1].strip().lower()
                            for yield_instr in config.YIELD_INSTRUCTIONS:
                                if yield_instr in check_line:
                                    has_yield = True
                                    break
                            if has_yield:
                                break

                    if not has_yield:
                        issues.append(
                            ValidationIssue(
                                severity="warning",
                                line=jump_line,
                                column=None,
                                message=f"Loop to '{target}' (line {target_line}) may lack yield/sleep",
                                rule="W002",
                            )
                        )

        return issues


# =============================================================================
# CLI Interface
# =============================================================================


def format_pretty(result: ValidationResult) -> str:
    """Format result for human-readable console output."""
    output_lines = []

    # Status header
    if result.passed:
        status = "[green]✅ PASSED[/green]"
    else:
        status = "[red]❌ FAILED[/red]"

    output_lines.append(f"Validation: {status}")
    output_lines.append("")

    # Statistics
    stats = result.stats
    output_lines.append("[bold]Statistics:[/bold]")
    output_lines.append(f"  Lines: {stats.lines} / {config.MAX_LINES}")
    output_lines.append(f"  Lines of code: {stats.lines_of_code}")
    output_lines.append(f"  Size: {stats.bytes} / {config.MAX_CODE_SIZE} bytes")
    output_lines.append(f"  Registers: {', '.join(stats.registers_used) or 'none'}")
    output_lines.append(f"  Devices: {', '.join(stats.devices_used) or 'none'}")
    output_lines.append(f"  Labels: {', '.join(stats.labels_defined) or 'none'}")
    output_lines.append("")

    # Issues by category
    if result.errors:
        output_lines.append("[red bold]Errors:[/red bold]")
        for issue in result.errors:
            loc = f"Line {issue.line}"
            if issue.column:
                loc += f":{issue.column}"
            output_lines.append(f"  [{issue.rule}] {loc}: {issue.message}")
        output_lines.append("")

    if result.warnings:
        output_lines.append("[yellow bold]Warnings:[/yellow bold]")
        for issue in result.warnings:
            loc = f"Line {issue.line}"
            if issue.column:
                loc += f":{issue.column}"
            output_lines.append(f"  [{issue.rule}] {loc}: {issue.message}")
        output_lines.append("")

    if result.info:
        output_lines.append("[blue bold]Info:[/blue bold]")
        for issue in result.info:
            loc = f"Line {issue.line}"
            if issue.column:
                loc += f":{issue.column}"
            output_lines.append(f"  [{issue.rule}] {loc}: {issue.message}")
        output_lines.append("")

    if not result.parser_available:
        output_lines.append(
            "[dim]Note: tree-sitter grammar not available, using fallback parser[/dim]"
        )

    return "\n".join(output_lines)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Validate IC10 code for Stationeers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run -m tools.ic10_validator --file code.ic10
  cat code.ic10 | uv run -m tools.ic10_validator --stdin
  uv run -m tools.ic10_validator --file code.ic10 --format json
        """,
    )

    # Input source (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--file", "-f", type=Path, help="Path to IC10 file to validate"
    )
    input_group.add_argument(
        "--stdin", action="store_true", help="Read IC10 code from stdin"
    )
    input_group.add_argument(
        "--code", "-c", type=str, help="IC10 code string to validate"
    )
    input_group.add_argument(
        "--check", action="store_true", help="Check if validator is available"
    )

    # Output format
    parser.add_argument(
        "--format",
        choices=["json", "pretty"],
        default="pretty",
        help="Output format (default: pretty)",
    )

    args = parser.parse_args()

    # Handle --check
    if args.check:
        validator = IC10Validator()
        if validator.parser is not None:
            console.print("[green]tree-sitter parser available[/green]")
            console.print(f"Grammar: {config.GRAMMAR_PATH}")
        else:
            console.print("[yellow]tree-sitter parser not available[/yellow]")
            console.print("Using fallback regex-based validation")
            console.print(
                f"To enable full parsing, build grammar at: {config.GRAMMAR_PATH}"
            )
        return

    # Get code to validate
    if args.file:
        if not args.file.exists():
            console.print(f"[red]Error: File not found: {args.file}[/red]")
            sys.exit(1)
        code = args.file.read_text()
    elif args.stdin:
        code = sys.stdin.read()
    else:
        code = args.code

    # Validate
    validator = IC10Validator()
    result = validator.validate(code)

    # Output
    if args.format == "json":
        print(json.dumps(result.to_dict(), indent=2))
    else:
        console.print(format_pretty(result))

    # Exit code
    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()

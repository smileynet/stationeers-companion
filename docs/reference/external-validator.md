---
title: External IC10 Validator
---

# External IC10 Validator

A deterministic Python-based validator for IC10 code that provides consistent, repeatable results.

## Installation

### Python Dependencies

The validator requires the `tree-sitter` package (already in pyproject.toml):

```bash
uv sync
```

### Optional: Tree-sitter Grammar

For enhanced parsing, build the tree-sitter-ic10 grammar:

```bash
# Install tree-sitter CLI
cargo install tree-sitter-cli

# Clone and build grammar
git clone https://github.com/Xandaros/tree-sitter-ic10.git
cd tree-sitter-ic10
tree-sitter generate

# Build shared library (Linux)
cc -shared -fPIC -o tree-sitter-ic10.so -I./src src/parser.c

# Copy to project
cp tree-sitter-ic10.so /path/to/stationeers_companion/tools/grammars/
```

Without the grammar, the validator uses a fallback regex-based parser that covers most validation rules.

## Usage

### Command Line

```bash
# Validate from file
uv run -m tools.ic10_validator --file code.ic10

# Validate from stdin
cat code.ic10 | uv run -m tools.ic10_validator --stdin

# Validate inline code
uv run -m tools.ic10_validator --code "move r0 1\nyield"

# JSON output (for programmatic use)
uv run -m tools.ic10_validator --file code.ic10 --format json

# Check if validator is available
uv run -m tools.ic10_validator --check
```

### Python API

```python
from tools.ic10_validator import IC10Validator

validator = IC10Validator()

code = """
alias sensor d0
alias output d1
main:
l r0 sensor Temperature
sgt r1 r0 300
s output On r1
yield
j main
"""

result = validator.validate(code)

if result.passed:
    print("Code is valid!")
else:
    for error in result.errors:
        print(f"[{error.rule}] Line {error.line}: {error.message}")
```

## Validation Rules

### Errors (Code Won't Work)

| Code | Description | Example |
|------|-------------|---------|
| E002 | Line count exceeds 128 | Code has 150 lines |
| E003 | Unknown instruction | `moev r0 1` (typo) |
| E004 | Invalid register | `r16`, `r99` |
| E005 | Invalid device | `d6`, `d10` |
| E006 | Undefined branch target | `j nonexistent` |
| E007 | Code size exceeds 4096 bytes | Very large code file |

### Warnings (May Cause Issues)

| Code | Description | Example |
|------|-------------|---------|
| W001 | Line length exceeds 90 chars | Very long comment |
| W002 | Loop may lack yield/sleep | Infinite loop without yield |
| W003 | Register read before write | Using uninitialized register |

### Info (Recommendations)

| Code | Description | Example |
|------|-------------|---------|
| I001 | Code size approaching limit | Over 3600 bytes |

## Output Format

### JSON Output

```json
{
  "passed": false,
  "stats": {
    "lines": 45,
    "lines_of_code": 32,
    "bytes": 1024,
    "registers_used": ["r0", "r1", "r2"],
    "devices_used": ["d0", "db"],
    "labels_defined": ["main", "loop"]
  },
  "errors": [
    {
      "severity": "error",
      "line": 12,
      "column": 5,
      "message": "Unknown instruction 'moev'",
      "rule": "E003"
    }
  ],
  "warnings": [],
  "info": [],
  "parser_available": true
}
```

### Pretty Output

```
Validation: ❌ FAILED

Statistics:
  Lines: 45 / 128
  Lines of code: 32
  Size: 1024 / 4096 bytes
  Registers: r0, r1, r2
  Devices: d0, db
  Labels: main, loop

Errors:
  [E003] Line 12: Unknown instruction 'moev'
```

## Integration with Agents

The `code-validator` agent uses this tool for deterministic validation:

```bash
echo "$CODE" | uv run -m tools.ic10_validator --stdin --format json
```

The agent then supplements the tool's output with:
- Device logic type verification (is Temperature readable?)
- Game-specific semantic checks
- Style recommendations
- Context-aware suggestions

## Hard Limits

From the Stationeers game:

| Limit | Value |
|-------|-------|
| Maximum lines | 128 |
| Maximum line length | 90 characters |
| Maximum code size | 4096 bytes |
| Valid registers | r0-r15, ra, sp |
| Valid devices | d0-d5, db, dr |

## Valid Instructions

See `tools/config.py` for the complete list, organized by category:

- **Math**: add, sub, mul, div, mod, abs, sqrt, etc.
- **Logic**: l, s, ls, ss, lr, sr, ld, sd
- **Batch**: lb, sb, lbn, sbn, lbs, sbs, lbns
- **Comparison**: seq, sne, sgt, slt, sge, sle, select, etc.
- **Branching**: j, jr, jal, beq, bne, bgt, blt, bdns, etc.
- **Bitwise**: and, or, xor, nor, not, sll, srl, sra
- **Stack**: push, pop, peek, poke, get, put
- **Utility**: alias, define, move, yield, sleep, hcf

## Troubleshooting

### "tree-sitter parser not available"

This is normal - the validator uses a fallback regex-based parser. For full parsing support, build the tree-sitter-ic10 grammar (see Installation).

### False positives

The regex-based parser may have edge cases. If you encounter false positives:
1. Check the code manually
2. Report issues at the project repository
3. Consider building the tree-sitter grammar for more accurate parsing

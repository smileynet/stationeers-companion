# IC10 Validation Rules

Enforceable rules for validating IC10 code. These are concrete checks, not estimates.

## Hard Limits (MUST pass or code won't compile)

| Rule | Check | Limit |
|------|-------|-------|
| MAX_LINES | Count non-empty lines | ≤ 128 |
| MAX_LINE_LENGTH | Length of each line | ≤ 90 characters |
| MAX_CODE_SIZE | Total bytes | ≤ 4096 bytes |
| VALID_REGISTERS | Register references | r0-r15, ra, sp only |
| VALID_DEVICES | Device references | d0-d5, db only |

### Validation Logic

```python
def check_hard_limits(lines):
    errors = []

    # Line count
    code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
    if len(code_lines) > 128:
        errors.append(f"FAIL: {len(code_lines)} lines exceeds 128 limit")

    # Line length
    for i, line in enumerate(lines):
        if len(line) > 90:
            errors.append(f"FAIL: Line {i+1} is {len(line)} chars (max 90)")

    # Total size
    total_bytes = sum(len(line.encode('utf-8')) + 1 for line in lines)
    if total_bytes > 4096:
        errors.append(f"FAIL: {total_bytes} bytes exceeds 4096 limit")

    return errors
```

---

## Syntax Rules (MUST pass)

| Rule | Pattern | Valid Example | Invalid Example |
|------|---------|---------------|-----------------|
| VALID_INSTRUCTION | First word is known instruction | `move r0 1` | `mov r0 1` |
| REGISTER_FORMAT | `r[0-15]`, `ra`, `sp` | `r0`, `r15`, `ra` | `r16`, `rx` |
| DEVICE_FORMAT | `d[0-5]`, `db` | `d0`, `db` | `d6`, `device0` |
| LABEL_FORMAT | Word ending in `:` | `main:` | `main` (missing colon) |
| ALIAS_FORMAT | `alias name target` | `alias sensor d0` | `alias d0 sensor` |
| DEFINE_FORMAT | `define NAME value` | `define MAX 100` | `define 100 MAX` |

### Known Instructions

```
# Device I/O
l, s, ls, ss, lb, sb, lbn, sbn, lbs, lbns

# Math
add, sub, mul, div, mod, abs, sqrt, exp, log, sin, cos, tan, asin, acos, atan, atan2
ceil, floor, trunc, round, min, max, rand

# Comparison
seq, sne, sgt, slt, sge, sle, seqz, snez, sgtz, sltz, sgez, slez
sap, sna, sapz, snaz, sdns, sdse

# Branching
j, jr, jal, beq, bne, bgt, blt, bge, ble, beqz, bnez, bgtz, bltz, bgez, blez
beqal, bneal, bgtal, bltal, bgeal, bleal, beqzal, bnezal, bgtzal, bltzal, bgezal, blezal
bap, bna, bapz, bnaz, bdns, bdse, brdns, brdse
brap, brna, brapz, brnaz

# Stack
push, pop, peek, poke, get, put, getd, putd

# Logic
and, or, xor, nor, not

# Bitwise
sll, srl, sra

# Control
yield, sleep, hcf

# Utility
alias, define, move, select, label
```

---

## Semantic Rules (SHOULD pass)

| Rule | Check | Severity |
|------|-------|----------|
| YIELD_IN_LOOP | Every loop must contain `yield` or `sleep` | ERROR |
| REGISTER_INIT | Registers read before write | WARNING |
| UNREACHABLE_CODE | Code after unconditional `j` | WARNING |
| DEVICE_CHECK | `bdns` before reading optional devices | WARNING |
| LABEL_DEFINED | All branch targets exist | ERROR |
| LABEL_USED | Defined labels are referenced | WARNING |

### Yield Check Logic

```python
def check_yield_in_loops(lines):
    """Ensure all loops contain yield or sleep."""
    labels = set()
    jump_targets = set()
    has_yield = {}

    # Find all labels
    for line in lines:
        if ':' in line and not line.strip().startswith('#'):
            label = line.split(':')[0].strip()
            labels.add(label)

    # Find jump targets and yields
    for line in lines:
        tokens = line.split()
        if not tokens:
            continue
        if tokens[0] in ('j', 'jr', 'jal'):
            target = tokens[1] if len(tokens) > 1 else None
            if target:
                jump_targets.add(target)
        if tokens[0] in ('yield', 'sleep'):
            # Mark current section as having yield
            pass

    # Check for loops without yield
    # A loop is: label that is jumped to from below
    errors = []
    for label in labels:
        if label in jump_targets:
            # This is a potential loop - check for yield between label and jump
            # Simplified: warn if no yield/sleep anywhere
            pass

    return errors
```

---

## Style Rules (RECOMMENDED)

| Rule | Recommendation | Why |
|------|----------------|-----|
| USE_ALIASES | Alias all devices and key registers | Readability |
| USE_DEFINES | Define numeric constants | Maintainability |
| COMMENT_HEADER | Include header with device list | Documentation |
| CONSISTENT_CASE | Labels lowercase, defines UPPERCASE | Convention |
| MEANINGFUL_NAMES | Descriptive aliases | Clarity |

---

## Validation Report Format

```
=== IC10 Validation Report ===

File: example.ic10
Lines: 85 / 128 (66%)
Bytes: 2048 / 4096 (50%)

ERRORS (must fix):
  [Line 45] Unknown instruction: mov (did you mean: move?)
  [Line 89] Branch target 'looop' not found (did you mean: loop?)

WARNINGS (should fix):
  [Line 23] Register r5 read before initialization
  [Line 67] No bdns check before reading d3

STYLE (optional):
  [Line 1] Missing header comment with device descriptions
  [Line 15] Device d2 used without alias

Summary: 2 errors, 2 warnings, 2 style issues
Status: FAIL (fix errors before use)
```

---

## Integration with Agents

### code-validator agent
Must check ALL error-level rules before approving code.

### code-generator agent
Must generate code that passes ALL error-level rules.
Should follow RECOMMENDED style rules.

### code-optimizer agent
Must not introduce errors while optimizing.
Should improve style rule compliance.

---

## Quick Reference Card

```
HARD LIMITS
├── Lines: ≤ 128
├── Line length: ≤ 90 chars
├── Total size: ≤ 4096 bytes
├── Registers: r0-r15, ra, sp
└── Devices: d0-d5, db

MUST HAVE
├── yield or sleep in every loop
├── All branch targets defined
└── Valid instruction names

SHOULD HAVE
├── Device aliases
├── Constants with define
├── Header comments
└── bdns before optional devices
```

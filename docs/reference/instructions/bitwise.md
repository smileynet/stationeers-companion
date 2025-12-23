---
title: Bitwise Instructions
category: bitwise
description: Logical operations and bit manipulation
---

# Bitwise Instructions

Logical operations for combining boolean conditions and bit manipulation.

## Logical Operations

Most commonly used for combining conditions (treating non-zero as true, zero as false).

### and
Bitwise AND. Result is 1 only if both inputs are non-zero.

**Syntax**: `and r? a b` → `r? = a & b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | First operand |
| b | reg/num | Second operand |

```ic10
# Check if BOTH conditions are true
sgt r0 pressure 100    # r0 = 1 if pressure > 100
slt r1 temp 300        # r1 = 1 if temp < 300
and r2 r0 r1           # r2 = 1 if BOTH true
```

**Truth table**:
| a | b | a AND b |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

### or
Bitwise OR. Result is 1 if either input is non-zero.

**Syntax**: `or r? a b` → `r? = a | b`

```ic10
# Check if EITHER condition is true
sgt r0 pressure 150    # Overpressure?
slt r1 temp 273        # Freezing?
or r2 r0 r1            # r2 = 1 if EITHER is a problem
s alarm On r2          # Sound alarm if any issue
```

**Truth table**:
| a | b | a OR b |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

---

### xor
Bitwise XOR (exclusive or). Result is 1 if inputs differ.

**Syntax**: `xor r? a b` → `r? = a ^ b`

```ic10
# Toggle state
xor r0 r0 1            # If r0 was 0, now 1. If 1, now 0.
```

```ic10
# Check if exactly one condition is true
xor r2 r0 r1           # r2 = 1 if r0 and r1 differ
```

**Truth table**:
| a | b | a XOR b |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

### nor
Bitwise NOR (not or). Result is 1 only if both inputs are zero.

**Syntax**: `nor r? a b` → `r? = ~(a | b)`

```ic10
# True only when NEITHER condition is met
nor r2 r0 r1           # r2 = 1 if both r0 AND r1 are 0
```

**Truth table**:
| a | b | a NOR b |
|---|---|---------|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

---

### not
Bitwise NOT. Inverts all bits.

**Syntax**: `not r? a` → `r? = ~a`

```ic10
# Invert a boolean
l r0 device On
not r1 r0              # r1 = inverted state
```

**Note**: For simple boolean inversion, `seqz r1 r0` is often clearer.

---

## Bit Shift Operations

Shift bits left or right. Useful for packing/unpacking values.

### sll (Shift Left Logical)
Shifts bits left, filling with zeros.

**Syntax**: `sll r? a b` → `r? = a << b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value to shift |
| b | reg/num | Number of positions |

```ic10
sll r0 1 3             # r0 = 1 << 3 = 8 (binary: 1000)
sll r0 r1 4            # r0 = r1 * 16
```

**Equivalent**: `r0 = a * 2^b`

---

### srl (Shift Right Logical)
Shifts bits right, filling with zeros.

**Syntax**: `srl r? a b` → `r? = a >> b`

```ic10
srl r0 16 2            # r0 = 16 >> 2 = 4 (binary: 100)
srl r0 r1 4            # r0 = r1 / 16 (integer)
```

**Equivalent**: `r0 = floor(a / 2^b)`

---

### sla (Shift Left Arithmetic)
Same as sll for positive numbers.

**Syntax**: `sla r? a b`

---

### sra (Shift Right Arithmetic)
Shifts right, preserving sign bit (for signed numbers).

**Syntax**: `sra r? a b`

---

## Common Patterns

### Combine Multiple Conditions
```ic10
# Breathable atmosphere check
l r0 sensor RatioOxygen
l r1 sensor RatioCarbonDioxide
l r2 sensor Pressure

sgt r3 r0 0.16         # O2 > 16%?
slt r4 r1 0.01         # CO2 < 1%?
sgt r5 r2 20           # Pressure > 20 kPa?

and r6 r3 r4           # O2 good AND CO2 good?
and r6 r6 r5           # AND pressure good?

s indicator On r6      # Green if all good
```

### Toggle Switch
```ic10
l r0 button Activate
bnez r0 toggle         # If button pressed
j skip

toggle:
l r1 light On
xor r1 r1 1            # Flip state
s light On r1

skip:
yield
```

### Any/All Check
```ic10
# ANY problem = alarm
or r0 r1 r2            # Combine first two
or r0 r0 r3            # Add third
s alarm On r0          # Alarm if any issue

# ALL conditions = proceed
and r0 r1 r2
and r0 r0 r3
s proceed On r0        # Only if all conditions met
```

---

## See Also

- [bitwise-extended.md](bitwise-extended.md) - Bit packing and advanced patterns
- [comparison.md](comparison.md) - Generate boolean conditions
- [branching.md](branching.md) - Branch on conditions

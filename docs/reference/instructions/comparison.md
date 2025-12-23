---
title: Comparison Instructions
category: comparison
description: Compare values and set registers based on conditions
---

# Comparison Instructions

Set a register to 1 (true) or 0 (false) based on comparing values. Use with branching instructions for conditional logic.

## Two-Value Comparisons

### seq (Set Equal)
Sets register to 1 if values are equal.

**Syntax**: `seq r? a b` → `r? = (a == b) ? 1 : 0`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | First value |
| b | reg/num | Second value |

```ic10
seq r0 r1 100      # r0 = 1 if r1 equals 100
seq r0 r1 r2       # r0 = 1 if r1 equals r2
```

---

### sne (Set Not Equal)
Sets register to 1 if values are not equal.

**Syntax**: `sne r? a b` → `r? = (a != b) ? 1 : 0`

```ic10
sne r0 r1 0        # r0 = 1 if r1 is not zero
```

---

### sgt (Set Greater Than)
Sets register to 1 if first value is greater.

**Syntax**: `sgt r? a b` → `r? = (a > b) ? 1 : 0`

```ic10
alias sensor d0
alias vent d1
define TARGET 101.325

l r0 sensor Pressure
sgt r1 r0 TARGET    # r1 = 1 if pressure > target
s vent On r1        # Turn on vent if overpressure
```

---

### slt (Set Less Than)
Sets register to 1 if first value is less.

**Syntax**: `slt r? a b` → `r? = (a < b) ? 1 : 0`

```ic10
l r0 sensor Temperature
slt r1 r0 283       # r1 = 1 if temp < 10°C (too cold)
```

---

### sge (Set Greater or Equal)
Sets register to 1 if first value is greater or equal.

**Syntax**: `sge r? a b` → `r? = (a >= b) ? 1 : 0`

```ic10
sge r0 r1 0        # r0 = 1 if r1 >= 0 (non-negative)
```

---

### sle (Set Less or Equal)
Sets register to 1 if first value is less or equal.

**Syntax**: `sle r? a b` → `r? = (a <= b) ? 1 : 0`

```ic10
sle r0 r1 100      # r0 = 1 if r1 <= 100
```

---

## Zero Comparisons

Simplified versions that compare against zero.

### seqz (Set Equal Zero)
Sets register to 1 if value equals zero.

**Syntax**: `seqz r? a` → `r? = (a == 0) ? 1 : 0`

```ic10
seqz r0 r1         # r0 = 1 if r1 is zero
```

---

### snez (Set Not Equal Zero)
Sets register to 1 if value is not zero.

**Syntax**: `snez r? a` → `r? = (a != 0) ? 1 : 0`

```ic10
l r0 device On
snez r1 r0         # r1 = 1 if device is on
```

---

### sgtz (Set Greater Than Zero)
Sets register to 1 if value is positive.

**Syntax**: `sgtz r? a` → `r? = (a > 0) ? 1 : 0`

```ic10
sgtz r0 r1         # r0 = 1 if r1 is positive
```

---

### sltz (Set Less Than Zero)
Sets register to 1 if value is negative.

**Syntax**: `sltz r? a` → `r? = (a < 0) ? 1 : 0`

```ic10
sltz r0 r1         # r0 = 1 if r1 is negative
```

---

### sgez (Set Greater or Equal Zero)
Sets register to 1 if value is non-negative.

**Syntax**: `sgez r? a` → `r? = (a >= 0) ? 1 : 0`

---

### slez (Set Less or Equal Zero)
Sets register to 1 if value is non-positive.

**Syntax**: `slez r? a` → `r? = (a <= 0) ? 1 : 0`

---

## Approximate Comparisons

Compare with tolerance (useful for floating-point values).

### sap (Set Approximately Equal)
Sets register to 1 if values are approximately equal within tolerance.

**Syntax**: `sap r? a b c` → `r? = (|a - b| <= max(c * max(|a|,|b|), epsilon)) ? 1 : 0`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | First value |
| b | reg/num | Second value |
| c | reg/num | Relative tolerance |

```ic10
sap r0 r1 100 0.01  # r0 = 1 if r1 is within 1% of 100
```

---

### sna (Set Not Approximately Equal)
Sets register to 1 if values are not approximately equal.

**Syntax**: `sna r? a b c` → `r? = (|a - b| > tolerance) ? 1 : 0`

---

### sapz (Set Approximately Zero)
Sets register to 1 if value is approximately zero.

**Syntax**: `sapz r? a b` → `r? = (|a| <= epsilon) ? 1 : 0`

---

### snaz (Set Not Approximately Zero)
Sets register to 1 if value is not approximately zero.

**Syntax**: `snaz r? a b` → `r? = (|a| > epsilon) ? 1 : 0`

---

## Device State Checks

### sdse (Set Device Set)
Sets register to 1 if device port is connected.

**Syntax**: `sdse r? device`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| device | d0-d5 | Device port to check |

```ic10
sdse r0 d0         # r0 = 1 if d0 is connected
bdns d0 skip       # Alternative: branch if not set
```

---

### sdns (Set Device Not Set)
Sets register to 1 if device port is not connected.

**Syntax**: `sdns r? device`

```ic10
sdns r0 d0         # r0 = 1 if d0 is NOT connected
```

---

## Conditional Selection

### select
Chooses between two values based on a condition (ternary operator).

**Syntax**: `select r? condition a b` → `r? = condition ? a : b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| condition | reg/num | Selector (0 = false, non-zero = true) |
| a | reg/num | Value if true |
| b | reg/num | Value if false |

```ic10
sgt r0 r1 100      # r0 = 1 if r1 > 100
select r2 r0 50 0  # r2 = 50 if r0 is true, else 0
```

```ic10
# Set vent power based on pressure
l r0 sensor Pressure
sgt r1 r0 100
select r2 r1 100 0  # Full power if pressure > 100, else off
s vent Setting r2
```

---

## Common Patterns

### Threshold Check
```ic10
define MIN_O2 0.16
l r0 sensor RatioOxygen
sgt r1 r0 MIN_O2    # r1 = 1 if oxygen is sufficient
```

### Range Check
```ic10
define MIN_TEMP 283
define MAX_TEMP 303
l r0 sensor Temperature

sge r1 r0 MIN_TEMP  # r1 = 1 if temp >= min
sle r2 r0 MAX_TEMP  # r2 = 1 if temp <= max
and r3 r1 r2        # r3 = 1 if in range
```

### Boolean Inversion
```ic10
l r0 device On
seqz r1 r0          # r1 = NOT r0 (invert on/off)
```

---

## See Also

- [comparison-extended.md](comparison-extended.md) - Edge cases and advanced patterns
- [branching.md](branching.md) - Branch based on conditions
- [bitwise.md](bitwise.md) - Combine conditions with and/or

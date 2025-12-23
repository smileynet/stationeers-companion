---
title: Math Instructions
category: math
description: Arithmetic, trigonometry, and value manipulation
---

# Math Instructions

Mathematical operations for calculations in IC10 programs.

## Arithmetic

### add
Adds two values and stores the result.

**Syntax**: `add r? a b` → `r? = a + b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination (r0-r15) |
| a | reg/num | First operand |
| b | reg/num | Second operand |

```ic10
add r0 r1 10       # r0 = r1 + 10
add r0 r0 1        # Increment r0 by 1
```

---

### sub
Subtracts the second value from the first.

**Syntax**: `sub r? a b` → `r? = a - b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value to subtract from |
| b | reg/num | Value to subtract |

```ic10
sub r0 r1 273.15   # Convert Kelvin to Celsius
sub r0 100 r1      # r0 = 100 - r1
```

---

### mul
Multiplies two values.

**Syntax**: `mul r? a b` → `r? = a × b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | First factor |
| b | reg/num | Second factor |

```ic10
mul r0 r1 100      # Convert ratio to percentage
mul r0 r1 r2       # r0 = r1 * r2
```

---

### div
Divides the first value by the second.

**Syntax**: `div r? a b` → `r? = a ÷ b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Dividend |
| b | reg/num | Divisor |

```ic10
div r0 r1 r2       # r0 = r1 / r2
div r0 r1 100      # Convert percentage to ratio
```

**Note**: Division by zero returns `NaN` (not a number).

---

### mod
Returns the remainder of division (modulo).

**Syntax**: `mod r? a b` → `r? = a mod b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Dividend |
| b | reg/num | Divisor |

```ic10
mod r0 r1 360      # Wrap angle to 0-359
mod r0 r1 10       # Get last digit
```

---

## Value Manipulation

### abs
Returns the absolute (non-negative) value.

**Syntax**: `abs r? a` → `r? = |a|`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Input value |

```ic10
sub r0 r1 r2       # r0 = difference (may be negative)
abs r0 r0          # r0 = absolute difference
```

---

### ceil
Rounds up to the nearest integer.

**Syntax**: `ceil r? a` → `r? = ⌈a⌉`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value to round up |

```ic10
ceil r0 3.2        # r0 = 4
ceil r0 -3.2       # r0 = -3
```

---

### floor
Rounds down to the nearest integer.

**Syntax**: `floor r? a` → `r? = ⌊a⌋`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value to round down |

```ic10
floor r0 3.8       # r0 = 3
floor r0 -3.2      # r0 = -4
```

---

### round
Rounds to the nearest integer (0.5 rounds up).

**Syntax**: `round r? a` → `r? = round(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value to round |

```ic10
round r0 3.4       # r0 = 3
round r0 3.5       # r0 = 4
```

---

### trunc
Truncates toward zero (removes decimal part).

**Syntax**: `trunc r? a` → `r? = trunc(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value to truncate |

```ic10
trunc r0 3.9       # r0 = 3
trunc r0 -3.9      # r0 = -3 (toward zero, not down)
```

---

### min
Returns the smaller of two values.

**Syntax**: `min r? a b` → `r? = min(a, b)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | First value |
| b | reg/num | Second value |

```ic10
min r0 r1 100      # Clamp r1 to max of 100
min r0 r1 r2       # r0 = smaller of r1 and r2
```

---

### max
Returns the larger of two values.

**Syntax**: `max r? a b` → `r? = max(a, b)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | First value |
| b | reg/num | Second value |

```ic10
max r0 r1 0        # Clamp r1 to min of 0
max r0 r1 r2       # r0 = larger of r1 and r2
```

---

## Exponents & Logarithms

### sqrt
Returns the square root.

**Syntax**: `sqrt r? a` → `r? = √a`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value (must be ≥ 0) |

```ic10
sqrt r0 16         # r0 = 4
sqrt r0 r1         # r0 = square root of r1
```

---

### exp
Returns e raised to the power (e^a).

**Syntax**: `exp r? a` → `r? = e^a`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Exponent |

```ic10
exp r0 1           # r0 = 2.718... (e)
exp r0 0           # r0 = 1
```

---

### log
Returns the natural logarithm (ln).

**Syntax**: `log r? a` → `r? = ln(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value (must be > 0) |

```ic10
log r0 2.718       # r0 ≈ 1
log r0 1           # r0 = 0
```

---

### pow
Raises a value to a power.

**Syntax**: `pow r? a b` → `r? = a^b`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Base |
| b | reg/num | Exponent |

```ic10
pow r0 2 8         # r0 = 256 (2^8)
pow r0 r1 2        # r0 = r1 squared
```

---

## Trigonometry

All trig functions use **radians** (not degrees). Full circle = 2π ≈ 6.283.

### sin
Returns the sine.

**Syntax**: `sin r? a` → `r? = sin(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Angle in radians |

```ic10
sin r0 0           # r0 = 0
sin r0 1.5708      # r0 ≈ 1 (sin 90°)
```

---

### cos
Returns the cosine.

**Syntax**: `cos r? a` → `r? = cos(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Angle in radians |

```ic10
cos r0 0           # r0 = 1
cos r0 3.1416      # r0 ≈ -1 (cos 180°)
```

---

### tan
Returns the tangent.

**Syntax**: `tan r? a` → `r? = tan(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Angle in radians |

```ic10
tan r0 0           # r0 = 0
tan r0 0.7854      # r0 ≈ 1 (tan 45°)
```

---

### asin
Returns the arc sine (inverse sine).

**Syntax**: `asin r? a` → `r? = asin(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value (-1 to 1) |

```ic10
asin r0 1          # r0 ≈ 1.5708 (90° in radians)
asin r0 0          # r0 = 0
```

---

### acos
Returns the arc cosine (inverse cosine).

**Syntax**: `acos r? a` → `r? = acos(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value (-1 to 1) |

```ic10
acos r0 1          # r0 = 0
acos r0 0          # r0 ≈ 1.5708 (90° in radians)
```

---

### atan
Returns the arc tangent (inverse tangent).

**Syntax**: `atan r? a` → `r? = atan(a)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| a | reg/num | Value |

```ic10
atan r0 1          # r0 ≈ 0.7854 (45° in radians)
atan r0 0          # r0 = 0
```

---

### atan2
Returns the angle from coordinates (handles quadrants correctly).

**Syntax**: `atan2 r? y x` → `r? = atan2(y, x)`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| y | reg/num | Y coordinate |
| x | reg/num | X coordinate |

```ic10
atan2 r0 1 1       # r0 ≈ 0.7854 (45° in radians)
atan2 r0 1 0       # r0 ≈ 1.5708 (90° in radians)
```

**Tip**: Use `atan2` for solar tracking - it correctly handles all quadrants.

---

## Random

### rand
Returns a random value in range.

**Syntax**: `rand r?` → `r? = random 0.0 to 1.0`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |

```ic10
rand r0            # r0 = random value 0.0 to 1.0
mul r0 r0 100      # Scale to 0-100
```

---

## See Also

- [math-extended.md](math-extended.md) - Edge cases, patterns, and advanced examples
- [comparison.md](comparison.md) - Compare values with sgt, slt, seq, etc.

---
title: Math Instructions - Extended
category: math
description: Edge cases, advanced patterns, and detailed examples
---

# Math Instructions - Extended Reference

Advanced patterns and edge cases for mathematical operations.

## Edge Cases

### Division by Zero
```ic10
div r0 100 0           # r0 = NaN (Not a Number)
```
NaN propagates through subsequent operations. Always validate divisors.

### Overflow Behavior
IC10 uses 64-bit floating point. Values wrap on overflow:
```ic10
add r0 1.7976931348623157e+308 1e+308  # Overflow
```

### Negative Zero
```ic10
div r0 -1 1e+308       # May produce -0
# -0 equals 0 in comparisons
```

## Common Patterns

### Clamping Values
```ic10
# Clamp r0 to range [MIN, MAX]
define MIN 0
define MAX 100
max r0 r0 MIN          # Ensure >= MIN
min r0 r0 MAX          # Ensure <= MAX
```

### Mapping Ranges
```ic10
# Map value from [0-100] to [0-1]
div r0 r1 100

# Map [0-1] to [MIN-MAX]
define MIN 283
define MAX 303
sub r1 MAX MIN         # Range size
mul r0 r0 r1           # Scale
add r0 r0 MIN          # Offset
```

### Running Average
```ic10
define SAMPLES 10
alias rSum r10
alias rCount r11

l r0 sensor Temperature
add rSum rSum r0
add rCount rCount 1

blt rCount SAMPLES skip
div r1 rSum rCount     # Calculate average
move rSum 0            # Reset
move rCount 0
skip:
```

### PID Controller Delta
```ic10
# Calculate error derivative
alias rError r0
alias rLastError r1
alias rDerivative r2

l r3 sensor Temperature
sub rError r3 TARGET   # Current error
sub rDerivative rError rLastError  # Delta
move rLastError rError
```

## Trigonometry Applications

### Degrees to Radians
```ic10
define DEG_TO_RAD 0.0174533  # π/180
mul r0 degrees DEG_TO_RAD
```

### Radians to Degrees
```ic10
define RAD_TO_DEG 57.2957795  # 180/π
mul r0 radians RAD_TO_DEG
```

### Solar Angle Calculation
```ic10
# Calculate optimal solar panel angle
alias daylight d0
l r0 daylight SolarAngle    # Horizontal sun position
l r1 daylight Vertical      # Vertical sun angle

# For tracking panels:
# Horizontal = sun horizontal angle
# Vertical = 90 - sun elevation
sub r2 90 r1
```

### Circular Motion
```ic10
# Generate circular coordinates
alias rAngle r10
define RADIUS 50

cos r0 rAngle
mul r0 r0 RADIUS       # X position

sin r1 rAngle
mul r1 r1 RADIUS       # Y position

add rAngle rAngle 0.1  # Increment angle
mod rAngle rAngle 6.283  # Wrap at 2π
```

## Numeric Precision

### Float Comparison
Never use exact equality for floats:
```ic10
# BAD
seq r0 r1 0.1          # May fail due to precision

# GOOD
sap r0 r1 0.1 0.0001   # Use approximate comparison
```

### Small Number Handling
```ic10
# Avoid division by very small numbers
abs r1 r0
blt r1 0.0001 useDefault
div r2 100 r0
j continue
useDefault:
move r2 0
continue:
```

## Optimization Tips

### Multiply vs Divide
Multiplication is faster than division:
```ic10
# Instead of:
div r0 r1 4

# Use:
mul r0 r1 0.25
```

### Power of 2 Operations
Use bit shifts for powers of 2:
```ic10
# Instead of:
mul r0 r1 8

# Use:
sll r0 r1 3            # Shift left 3 = multiply by 8
```

### Precalculate Constants
```ic10
# Instead of calculating π/180 each time:
define PI_OVER_180 0.0174533

# Use the constant:
mul r0 degrees PI_OVER_180
```

## Useful Constants

| Constant | Value | Use |
|----------|-------|-----|
| π | 3.14159265359 | Circle calculations |
| e | 2.71828182846 | Exponential growth |
| Kelvin offset | 273.15 | C↔K conversion |
| Deg→Rad | 0.0174533 | Angle conversion |
| Rad→Deg | 57.2957795 | Angle conversion |

---
title: Comparison Instructions - Extended
category: comparison
description: Advanced comparison patterns and edge cases
---

# Comparison Instructions - Extended Reference

## Edge Cases

### NaN Comparisons
```ic10
div r0 0 0             # r0 = NaN
seq r1 r0 r0           # r1 = 0 (NaN != NaN)
sne r1 r0 r0           # r1 = 1 (NaN is never equal to anything)
```

### Floating Point Precision
```ic10
# Avoid exact comparisons with floats
move r0 0.1
add r0 r0 0.1
add r0 r0 0.1
seq r1 r0 0.3          # May be 0 due to precision!

# Use approximate comparison instead
sap r1 r0 0.3 0.0001   # r1 = 1 (within tolerance)
```

## Multi-Condition Patterns

### Complex Range Check
```ic10
# Check: MIN <= value <= MAX
define MIN 283
define MAX 303

l r0 sensor Temperature
sge r1 r0 MIN          # >= MIN
sle r2 r0 MAX          # <= MAX
and r3 r1 r2           # Both conditions

# Alternative using subtraction
sub r1 r0 MIN
sub r2 MAX r0
sgez r3 r1             # >= 0 means >= MIN
sgez r4 r2             # >= 0 means <= MAX
and r5 r3 r4
```

### Deadband / Hysteresis
```ic10
alias rState r10
define LOW 95
define HIGH 105

l r0 sensor Pressure
bgt r0 HIGH turnOn
blt r0 LOW turnOff
j keepState            # In deadband, keep current state

turnOn:
move rState 1
j keepState

turnOff:
move rState 0

keepState:
s vent On rState
```

### Priority Comparison
```ic10
# Execute highest priority matching condition
l r0 sensor Pressure

bgt r0 200 emergency   # Priority 1: Emergency
bgt r0 150 high        # Priority 2: High
bgt r0 100 medium      # Priority 3: Medium
j normal               # Priority 4: Normal
```

## Select Optimization

### Nested Select (Ternary Chain)
```ic10
# r0 = (a > 100) ? 3 : (a > 50) ? 2 : (a > 0) ? 1 : 0
sgt r1 a 100
select r0 r1 3 0       # Start with highest priority
sgt r1 a 50
select r2 r1 2 r0      # Override if medium
sgt r1 a 0
select r0 r1 1 r2      # Override if low
```

### Clamped Ternary
```ic10
# Output 100 if over threshold, 0 otherwise
sgt r0 r1 threshold
mul r0 r0 100          # r0 = 0 or 100 (faster than select)
```

## Device Existence Patterns

### Optional Sensor
```ic10
sdse r0 d0             # Is sensor connected?
beqz r0 useDefault

l r1 d0 Temperature    # Use real reading
j continue

useDefault:
move r1 293            # Default temperature

continue:
# r1 now has temperature (real or default)
```

### Multi-Device Fallback
```ic10
# Try d0, fallback to d1, then d2
sdse r0 d0
bnez r0 useD0
sdse r0 d1
bnez r0 useD1
j useD2

useD0:
l r1 d0 Pressure
j done
useD1:
l r1 d1 Pressure
j done
useD2:
l r1 d2 Pressure
done:
```

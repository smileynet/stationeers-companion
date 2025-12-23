---
title: Bitwise Instructions - Extended
category: bitwise
description: Advanced bit manipulation patterns
---

# Bitwise Instructions - Extended Reference

## Bit Packing

### Pack Multiple Values
Store multiple small values in one register:
```ic10
# Pack 4 flags into one value
# Flag layout: [unused][flag3][flag2][flag1][flag0]
move r10 0             # Storage register

# Set flag 1 (bit 1)
or r10 r10 2           # 2 = 0b0010

# Set flag 3 (bit 3)
or r10 r10 8           # 8 = 0b1000

# Clear flag 1
and r10 r10 -3         # -3 = ~2 = 0b...11111101
```

### Unpack Values
```ic10
# Check if flag 2 is set (bit 2)
and r0 r10 4           # 4 = 0b0100
snez r1 r0             # r1 = 1 if flag 2 set
```

### Pack Two Bytes
```ic10
# Pack r0 (low) and r1 (high) into r2
and r0 r0 255          # Ensure 8 bits
and r1 r1 255
sll r1 r1 8            # Shift high byte
or r2 r0 r1            # Combine

# Unpack
and r0 r2 255          # Low byte
srl r1 r2 8            # High byte
and r1 r1 255
```

## Flag Management

### Set/Clear/Toggle Individual Bit
```ic10
define FLAG_ACTIVE 1    # Bit 0
define FLAG_ERROR 2     # Bit 1
define FLAG_READY 4     # Bit 2
alias rFlags r15

# Set flag
or rFlags rFlags FLAG_ERROR

# Clear flag
not r0 FLAG_ERROR      # Invert mask
and rFlags rFlags r0   # Clear bit

# Toggle flag
xor rFlags rFlags FLAG_ACTIVE

# Check flag
and r0 rFlags FLAG_READY
snez r1 r0             # r1 = 1 if ready
```

### Multiple Flags at Once
```ic10
# Set multiple flags
or rFlags rFlags 7     # Set bits 0, 1, 2

# Clear multiple flags
and rFlags rFlags -8   # Clear bits 0, 1, 2

# Check if ANY flag set
and r0 rFlags 7
snez r1 r0             # r1 = 1 if any of bits 0-2 set

# Check if ALL flags set
and r0 rFlags 7
seq r1 r0 7            # r1 = 1 if all of bits 0-2 set
```

## Power of 2 Math

### Multiply by Power of 2
```ic10
sll r0 r1 1            # r0 = r1 * 2
sll r0 r1 2            # r0 = r1 * 4
sll r0 r1 3            # r0 = r1 * 8
sll r0 r1 4            # r0 = r1 * 16
```

### Divide by Power of 2
```ic10
srl r0 r1 1            # r0 = r1 / 2
srl r0 r1 2            # r0 = r1 / 4
srl r0 r1 3            # r0 = r1 / 8
```

### Check if Power of 2
```ic10
# n is power of 2 if (n & (n-1)) == 0 and n > 0
sub r1 r0 1            # r1 = n - 1
and r2 r0 r1           # r2 = n & (n-1)
seqz r3 r2             # r3 = 1 if result is 0
sgtz r4 r0             # r4 = 1 if n > 0
and r5 r3 r4           # r5 = 1 if power of 2
```

## Boolean Logic Optimization

### DeMorgan's Laws
```ic10
# NOT (A AND B) = (NOT A) OR (NOT B)
# Implemented with NOR:
nor r0 a b             # Same as: not(a or b) = not(a) and not(b)

# For NOT (A AND B):
and r0 a b
seqz r0 r0             # Invert result
```

### Consensus
```ic10
# At least 2 of 3 conditions true
and r3 r0 r1           # 0 AND 1
and r4 r1 r2           # 1 AND 2
and r5 r0 r2           # 0 AND 2
or r6 r3 r4
or r6 r6 r5            # Any pair true = majority
```

### Odd Parity
```ic10
# XOR all bits for odd parity
xor r0 r1 r2
xor r0 r0 r3
xor r0 r0 r4           # r0 = 1 if odd number of 1s
```

## Practical Applications

### Cyclic Counter
```ic10
# Count 0-7 then wrap
add r0 r0 1
and r0 r0 7            # Mask to 3 bits (0-7)
```

### Quick Modulo (Power of 2)
```ic10
# r0 mod 8 (same as r0 % 8)
and r0 r0 7            # 7 = 0b111
```

### Extract Bits
```ic10
# Get bits 4-7 of a value
srl r0 r1 4            # Shift right 4
and r0 r0 15           # Mask to 4 bits
```

---
title: Indirect Addressing
category: addressing
description: Dynamic register and device access using indirect addressing
---

# Indirect Addressing

IC10 supports indirect addressing for both registers and devices, allowing dynamic access based on computed values.

## Indirect Register Access (`rr<N>`)

Use the value in register N as the register index. This is essential for array-like patterns and reducing code size.

### Syntax

`rr<N>` where N is a register number (0-15) containing the index.

The value in register N becomes the register index.

### Examples

```ic10
# Direct vs Indirect
move r5 100            # Direct: put 100 in r5

move r0 5              # r0 = 5 (the index)
move rr0 100           # Indirect: put 100 in register[r0] = r5

# Reading indirectly
move r1 rr0            # r1 = value of register[r0] = r5 = 100
```

### Array-Like Storage Pattern

Store values in r0-r3 as an array:

```ic10
alias idx r10
alias val r11

# Store values at indices 0-3
move idx 0
move rridx 100         # r0 = 100

move idx 1
move rridx 200         # r1 = 200

move idx 2
move rridx 300         # r2 = 300

# Read value at index
move idx 1
move val rridx         # val = r1 = 200
```

### Dynamic Register Selection

Useful for state machines or computed lookups:

```ic10
# Store signal IDs in r0-r3
alias count r4
alias sigID r5
alias temp r10

# Store new signal at current count
move temp count
move rrtemp sigID       # r[count] = sigID
add count count 1

# Read signal at selected index
alias selected r6
move temp selected
move sigID rrtemp       # sigID = r[selected]
```

---

## Indirect Device Access (`dr<N>`)

Use the value in register N as the device port index. Useful for iterating over multiple devices.

### Syntax

`dr<N>` where N is a register number containing device index (0-5).

### Examples

```ic10
alias idx r10

# Read from device at index
move idx 0             # Start with d0
l r0 dr10 Temperature  # Read from d[r10] = d0

move idx 1
l r1 dr10 Temperature  # Read from d[r10] = d1
```

### Device Loop Pattern

Read temperature from all devices d0-d5:

```ic10
alias idx r10
alias maxDevices r11
alias total r12

move maxDevices 6
move idx 0
move total 0

readLoop:
bdns dr10 skipDevice   # Skip if device not connected
l r0 dr10 Temperature
add total total r0
skipDevice:
add idx idx 1
blt idx maxDevices readLoop

# total now has sum of all temperatures
```

### Multi-Device Average

```ic10
alias idx r10
alias count r11
alias sum r12
alias avg r13

move idx 0
move count 0
move sum 0

avgLoop:
bge idx 4 calcAvg      # Only check d0-d3
bdns dr10 skipDev
l r0 dr10 Pressure
add sum sum r0
add count count 1
skipDev:
add idx idx 1
j avgLoop

calcAvg:
div avg sum count      # Calculate average
```

---

## Common Patterns

### Replace Branch Tables with Indirect Access

**Before (21 lines for 4-element array):**
```ic10
beq cnt 0 st0
beq cnt 1 st1
beq cnt 2 st2
beq cnt 3 st3
j done
st0:
move r0 sig
j done
st1:
move r1 sig
j done
st2:
move r2 sig
j done
st3:
move r3 sig
done:
```

**After (3 lines):**
```ic10
move r14 cnt           # Use r14 as index holder
move rr14 sig          # Store sig in r[cnt]
```

### Savings: 18 lines!

---

## Line Count Optimization Guide

Indirect addressing is the #1 technique for keeping code under 128 lines.

| Pattern | Lines Saved |
|---------|-------------|
| 4-element array store | 18 lines |
| 4-element array read | 18 lines |
| 4-element array clear | 18 lines |
| Device iteration loop | 10+ lines |

### When to Use

- Storing/reading indexed data (signal IDs, temperatures, states)
- Iterating over multiple devices
- Any "switch" pattern with sequential indices
- Lookup tables with computed indices

### When NOT to Use

- Only 2-3 branches (overhead not worth it)
- Non-sequential indices
- When clarity matters more than brevity

---

## Gotchas

1. **Valid Range**: Register indices 0-15, device indices 0-5
2. **Alias Compatibility**: Can use `rralias` if alias points to a register
3. **Performance**: Same execution speed as direct access
4. **Debugging**: Harder to trace - add comments explaining intent

---

## See Also

- [stack.md](stack.md) - Alternative storage using IC stack
- [utility.md](utility.md) - Subroutines and control flow

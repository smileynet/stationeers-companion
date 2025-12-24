---
title: Stack Instructions
category: stack
description: Stack operations and external device memory access
---

# Stack Instructions

Operations for the internal stack and reading/writing to external device stacks.

## Internal Stack

IC Housing has a 512-value internal stack. Use for temporary storage or passing data between subroutines.

### push
Pushes a value onto the internal stack.

**Syntax**: `push value`

| Param | Type | Description |
|-------|------|-------------|
| value | reg/num | Value to push |

```ic10
push r0                # Save r0 to stack
push 100               # Push literal value
```

---

### pop
Removes and retrieves the top value from stack.

**Syntax**: `pop r?`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination for popped value |

```ic10
pop r0                 # Get top value into r0
```

**Note**: Stack is LIFO (Last In, First Out).

---

### clr
Clears stack memory for a device. Resets all stack values to zero.

**Syntax**: `clr device`

| Param | Type | Description |
|-------|------|-------------|
| device | db/d0-d5 | Target device to clear |

```ic10
clr db                  # Clear internal stack (all values = 0)
clr d0                  # Clear d0's external stack
```

**Use Cases**:
- Reset data structures before starting fresh
- Clear accumulated data
- Initialize stack to known state

---

### clrd
Clears stack memory for a device specified by device ID (prefab hash).

**Syntax**: `clrd id`

| Param | Type | Description |
|-------|------|-------------|
| id | reg/num | Device prefab hash or device ID |

```ic10
define MEMORY_HASH 1234567890
clrd MEMORY_HASH        # Clear memory device with this hash
```

**Use Cases**:
- Clear memory on devices identified by hash
- Batch memory reset
- When device port unknown but hash is known

---

### peek
Reads the top value without removing it.

**Syntax**: `peek r?`

```ic10
peek r0                # Look at top value (doesn't remove)
```

---

### poke
Writes a value to the top of the stack without changing stack size.

**Syntax**: `poke value`

```ic10
poke 50                # Replace top value with 50
```

---

## Stack Example: Subroutine with Saved State
```ic10
# Save registers before subroutine
push r0
push r1

jal mySubroutine       # Call subroutine (may use r0, r1)

# Restore registers after
pop r1                 # Pop in reverse order!
pop r0

j continue

mySubroutine:
  move r0 100          # Use r0 freely
  move r1 200
  j ra                 # Return
```

---

## External Device Stack (Memory)

Read/write to external devices that have stack memory (like Logic Memory or other ICs).

### get
Reads a value at a specific index from internal stack.

**Syntax**: `get r? device index`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| device | db | Self reference |
| index | reg/num | Stack index (0-based) |

```ic10
get r0 db 5            # Read stack position 5
```

---

### put
Writes a value at a specific index to internal stack.

**Syntax**: `put device index value`

| Param | Type | Description |
|-------|------|-------------|
| device | db | Self reference |
| index | reg/num | Stack index |
| value | reg/num | Value to write |

```ic10
put db 5 r0            # Write r0 to stack position 5
```

---

### getd
Reads from an external device's stack/memory.

**Syntax**: `getd r? device index`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| device | d0-d5 | External device |
| index | reg/num | Memory index |

```ic10
alias memory d0
getd r0 memory 0       # Read memory slot 0
getd r1 memory 1       # Read memory slot 1
```

---

### putd
Writes to an external device's stack/memory.

**Syntax**: `putd device index value`

| Param | Type | Description |
|-------|------|-------------|
| device | d0-d5 | External device |
| index | reg/num | Memory index |
| value | reg/num | Value to write |

```ic10
alias memory d0
putd memory 0 r0       # Write r0 to memory slot 0
putd memory 1 100      # Write 100 to slot 1
```

---

## Common Patterns

### Data Logging
```ic10
alias memory d0
alias rIndex r10

# Log temperature readings
l r0 sensor Temperature
putd memory rIndex r0  # Store to current index
add rIndex rIndex 1    # Next index
mod rIndex rIndex 16   # Wrap at 16 entries (circular buffer)
```

### Inter-IC Communication
```ic10
# IC 1: Write data to shared memory
alias sharedMem d0
l r0 sensor Temperature
putd sharedMem 0 r0    # Temperature in slot 0
l r1 sensor Pressure
putd sharedMem 1 r1    # Pressure in slot 1

# IC 2: Read from shared memory
alias sharedMem d0
getd r0 sharedMem 0    # Get temperature
getd r1 sharedMem 1    # Get pressure
```

### Lookup Table
```ic10
# Store calibration values in stack
put db 0 100           # Level 0 = 100
put db 1 150           # Level 1 = 150
put db 2 200           # Level 2 = 200

# Look up value based on level
l r0 dial Setting      # Get level 0-2
get r1 db r0           # r1 = calibration value for that level
s device Setting r1
```

### Save/Restore Context
```ic10
# Save all working registers
push r0
push r1
push r2
push r3

# ... subroutine work ...

# Restore in reverse order
pop r3
pop r2
pop r1
pop r0
```

---

## Stack Size Limits

- Internal stack: 512 values
- Logic Memory: varies by device
- Stack overflow causes errors

---

## See Also

- [stack-extended.md](stack-extended.md) - Advanced patterns
- [utility.md](utility.md) - Subroutines with jal/ra

---
title: Branching Instructions
category: branching
description: Control program flow with jumps and conditional branches
---

# Branching Instructions

Control program flow based on conditions. Essential for loops, conditionals, and state machines.

## Unconditional Jumps

### j (Jump)
Jumps to a label unconditionally.

**Syntax**: `j label`

```ic10
main:
  # ... do work ...
  yield
  j main               # Loop forever
```

---

### jr (Jump Relative)
Jumps by a relative line offset.

**Syntax**: `jr offset`

| Param | Type | Description |
|-------|------|-------------|
| offset | reg/num | Lines to jump (positive=forward, negative=back) |

```ic10
jr 2                   # Skip next 2 lines
s device On 0          # Skipped
s device On 1          # Skipped
# Execution continues here
```

**Note**: Harder to maintain than labels. Use sparingly.

---

### jal (Jump and Link)
Jumps to label and saves return address in `ra` register. Used for subroutines.

**Syntax**: `jal label`

```ic10
jal readSensors        # Call subroutine
# ... continues after subroutine returns ...

readSensors:
  l r0 sensor Temperature
  l r1 sensor Pressure
  j ra                 # Return to caller
```

---

## Conditional Branches

Branch if condition is true. Format: `b<condition> args label`

### beq (Branch if Equal)
**Syntax**: `beq a b label` - Branch if `a == b`

```ic10
l r0 sensor Mode
beq r0 1 handleMode1   # If mode == 1, go to handleMode1
beq r0 2 handleMode2   # If mode == 2, go to handleMode2
j defaultMode          # Otherwise, default
```

---

### bne (Branch if Not Equal)
**Syntax**: `bne a b label` - Branch if `a != b`

```ic10
l r0 device On
bne r0 0 alreadyOn     # Skip if already on
s device On 1          # Turn on
alreadyOn:
```

---

### bgt (Branch if Greater Than)
**Syntax**: `bgt a b label` - Branch if `a > b`

```ic10
l r0 sensor Pressure
bgt r0 150 overpressure   # If pressure > 150, handle
j normal
```

---

### blt (Branch if Less Than)
**Syntax**: `blt a b label` - Branch if `a < b`

```ic10
l r0 sensor Temperature
blt r0 273 tooFreezing    # If temp < 273K (0°C), too cold
```

---

### bge (Branch if Greater or Equal)
**Syntax**: `bge a b label` - Branch if `a >= b`

---

### ble (Branch if Less or Equal)
**Syntax**: `ble a b label` - Branch if `a <= b`

---

## Zero Branches

Compare against zero (shorter syntax).

### beqz (Branch if Equal Zero)
**Syntax**: `beqz a label` - Branch if `a == 0`

```ic10
l r0 device On
beqz r0 turnOn         # If off, turn on
j skip
turnOn:
s device On 1
skip:
```

---

### bnez (Branch if Not Equal Zero)
**Syntax**: `bnez a label` - Branch if `a != 0`

```ic10
l r0 button Activate
bnez r0 handlePress    # If button pressed
```

---

### bgtz (Branch if Greater Than Zero)
**Syntax**: `bgtz a label` - Branch if `a > 0`

---

### bltz (Branch if Less Than Zero)
**Syntax**: `bltz a label` - Branch if `a < 0`

---

### bgez (Branch if Greater or Equal Zero)
**Syntax**: `bgez a label` - Branch if `a >= 0`

---

### blez (Branch if Less or Equal Zero)
**Syntax**: `blez a label` - Branch if `a <= 0`

---

## Branch and Link Variants

Branch AND save return address in `ra`. For conditional subroutine calls.

### beqal, bneal, bgtal, bltal, bgeal, bleal

**Syntax**: `b<cond>al a b label`

```ic10
bgtال r0 100 handleHigh   # If > 100, call handleHigh as subroutine
# ... continues after handleHigh returns with `j ra` ...
```

---

## Device State Branches

### bdse (Branch if Device Set)
Branch if a device is connected to the port.

**Syntax**: `bdse device label`

```ic10
bdse d0 deviceOk       # If d0 connected, continue
j noDevice             # Otherwise handle missing device

deviceOk:
l r0 d0 Temperature
```

---

### bdns (Branch if Device Not Set)
Branch if a device is NOT connected.

**Syntax**: `bdns device label`

```ic10
bdns d0 skipRead       # Skip if no device
l r0 d0 Temperature
skipRead:
```

---

### bdseal / bdnsal
Branch if device set/not set, and link.

---

### bdnvl (Branch if Device Not Valid for Load)
Branch if a device cannot be read from (logic type invalid or device unavailable).

**Syntax**: `bdnvl device logicType label`

| Param | Type | Description |
|-------|------|-------------|
| device | d0-d5 | Device to check |
| logicType | name | Logic type to verify |
| label | name | Label to jump if not valid |

```ic10
alias tank d0
bdnvl tank Quantity noItem    # Skip if Quantity not readable
l r0 tank Quantity            # Safe to read now
noItem:
move r0 0                  # Default value
```

**Use Cases**:
- Checking if device supports a specific logic type
- Graceful degradation when device not available
- Preventing read errors

---

### bdnvs (Branch if Device Not Valid for Store)
Branch if a device cannot be written to (logic type invalid or device unavailable).

**Syntax**: `bdnvs device logicType label`

| Param | Type | Description |
|-------|------|-------------|
| device | d0-d5 | Device to check |
| logicType | name | Logic type to verify |
| label | name | Label to jump if not valid |

```ic10
bdnvs vent Setting skipVent   # Skip if Setting not writable
s vent Setting 50              # Safe to write now
skipVent:
```

**Use Cases**:
- Checking if write operation is valid before executing
- Preventing write errors
- Handling device incompatibility

---

### bnan (Branch if NaN)
Branch if value is NaN (Not a Number).

**Syntax**: `bnan value label`

| Param | Type | Description |
|-------|------|-------------|
| value | reg/num | Value to check |
| label | name | Label to jump if NaN |

```ic10
l r0 calculationResult
bnan r0 handleNaN        # Handle invalid result
# ... continue with valid value ...
handleNaN:
move r0 0                  # Reset to default
```

**Use Cases**:
- Division by zero protection
- Invalid calculation results
- Sensor reading errors

---

### brnan (Branch if NaN - Relative)
Relative branch if value is NaN.

**Syntax**: `brnan value offset`

| Param | Type | Description |
|-------|------|-------------|
| value | reg/num | Value to check |
| offset | reg/num | Lines to jump (can be negative) |

```ic10
brnan r0 -3               # Skip 3 lines if NaN
```

---

## Approximate Branches

Branch based on approximate equality (for floating-point tolerance).

### bap (Branch if Approximately Equal)
**Syntax**: `bap a b c label` - Branch if `a ≈ b` within tolerance `c`

```ic10
l r0 sensor Pressure
bap r0 101.325 0.01 stable   # If within 1% of target
```

---

### bna (Branch if Not Approximately Equal)
**Syntax**: `bna a b c label` - Branch if `a ≉ b`

---

### bapz / bnaz
Approximately zero / not approximately zero.

---

## Relative Branches (br* variants)

Like regular branches but jump by relative offset instead of label.

### breq, brne, brgt, brlt, brge, brle

**Syntax**: `br<cond> a b offset`

```ic10
brgt r0 100 3          # If r0 > 100, skip 3 lines
```

---

### brap, brna
Relative approximate branches.

---

## Common Patterns

### If-Else
```ic10
l r0 sensor Pressure
bgt r0 100 highPressure
# Low pressure path
s vent Mode 0          # Inward
j continue
highPressure:
s vent Mode 1          # Outward
continue:
```

### Loop with Counter
```ic10
move r0 0              # Counter
loop:
  # ... do work ...
  add r0 r0 1          # Increment
  blt r0 10 loop       # Repeat 10 times
```

### State Machine
```ic10
alias state r15
define STATE_IDLE 0
define STATE_RUNNING 1
define STATE_ERROR 2

beq state STATE_IDLE stateIdle
beq state STATE_RUNNING stateRunning
beq state STATE_ERROR stateError
j stateIdle            # Default

stateIdle:
  # ... handle idle ...
  j main

stateRunning:
  # ... handle running ...
  j main

stateError:
  # ... handle error ...
  j main
```

### Safe Device Read
```ic10
bdns d0 noSensor
l r0 d0 Temperature
j continue
noSensor:
move r0 0              # Default value
continue:
```

---

## See Also

- [branching-extended.md](branching-extended.md) - Advanced patterns
- [comparison.md](comparison.md) - Set comparison results
- [utility.md](utility.md) - Labels and control flow

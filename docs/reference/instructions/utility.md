---
title: Utility Instructions
category: utility
description: Aliases, constants, register operations, and execution control
---

# Utility Instructions

Helper instructions for organizing code and controlling execution.

## Code Organization

### alias
Creates a named reference to a register or device port. Makes code more readable.

**Syntax**: `alias name target`

| Param | Type | Description |
|-------|------|-------------|
| name | identifier | Your chosen name |
| target | register/device | What to alias (r0-r15, d0-d5, db) |

```ic10
# Device aliases
alias sensor d0
alias vent d1
alias heater d2

# Register aliases
alias rTemp r0
alias rPressure r1
alias rTarget r2

# Now use names instead of r0, d0, etc.
l rTemp sensor Temperature
s vent On 1
```

**Best practice**: Always alias devices and commonly-used registers at the top of your code.

---

### define
Creates a named constant. Value is substituted at compile time.

**Syntax**: `define name value`

| Param | Type | Description |
|-------|------|-------------|
| name | identifier | Your chosen name |
| value | number | Constant value |

```ic10
define TARGET_PRESSURE 101.325
define TARGET_TEMP 293.15
define MIN_O2 0.16
define MAX_CO2 0.01

# Device hashes
define SOLAR_PANEL -539224550
define LARGE_BATTERY 683671518

l r0 sensor Pressure
sgt r1 r0 TARGET_PRESSURE    # Use constant
```

**Best practice**: Use UPPER_CASE for constants to distinguish from aliases.

---

### label
Marks a line as a jump target. Not an instruction itself - it's a line marker.

**Syntax**: `labelname:`

```ic10
main:                    # Label for main loop
  l r0 sensor Temperature
  yield
  j main                 # Jump back to main

error:                   # Error handler label
  s display Color 2      # Red
  hcf                    # Halt
```

**Note**: Labels must be unique within the program.

---

## Register Operations

### move
Copies a value into a register.

**Syntax**: `move r? value` → `r? = value`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| value | reg/num | Value to copy |

```ic10
move r0 0              # Initialize r0 to 0
move r0 100            # Set r0 to 100
move r0 r1             # Copy r1 to r0
```

---

## Execution Control

### yield
Pauses execution for one game tick. **Required in loops**.

**Syntax**: `yield`

```ic10
main:
  l r0 sensor Temperature
  # ... process data ...
  yield                  # REQUIRED: prevents CPU overrun
  j main
```

**CRITICAL**: Always include `yield` in any loop. Without it, the IC will error with "CPU overrun" after 128 instructions per tick.

---

### sleep
Pauses execution for a specified number of seconds.

**Syntax**: `sleep seconds`

| Param | Type | Description |
|-------|------|-------------|
| seconds | reg/num | Duration to sleep |

```ic10
s actuator On 1        # Turn on
sleep 5                # Wait 5 seconds
s actuator On 0        # Turn off
```

**Use cases**:
- Airlock cycling (wait for pressure equalization)
- Debouncing button presses
- Rate-limiting operations

---

### hcf (Halt and Catch Fire)
Stops execution completely. Program must be restarted manually.

**Syntax**: `hcf`

```ic10
# Emergency stop on critical error
l r0 sensor Pressure
bgt r0 500 emergency   # Over 500 kPa = danger!
# ... normal operation ...
j main

emergency:
  sb VENT On 0         # Shut everything down
  hcf                  # Stop program
```

**Use cases**:
- Critical error handling
- One-time initialization scripts
- Debugging breakpoints

---

## Code Structure Template

```ic10
# ================================================
# Program Name
# ================================================
# Description: What this code does
# Author: Your name
# Devices:
#   d0 = Gas Sensor
#   d1 = Active Vent
# ================================================

# === ALIASES ===
alias sensor d0
alias vent d1
alias rTemp r0
alias rPressure r1

# === CONSTANTS ===
define TARGET_PRESSURE 101.325
define MIN_TEMP 283.15
define MAX_TEMP 303.15

# === INITIALIZATION ===
move rTemp 0
s vent On 0

# === MAIN LOOP ===
main:
  l rTemp sensor Temperature
  l rPressure sensor Pressure

  # ... control logic ...

  yield
  j main

# === ERROR HANDLERS ===
error:
  s vent On 0
  hcf
```

---

## See Also

- [utility-extended.md](utility-extended.md) - Advanced patterns and edge cases
- [branching.md](branching.md) - Control flow with jumps and branches

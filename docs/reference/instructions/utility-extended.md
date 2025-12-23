---
title: Utility Instructions - Extended
category: utility
description: Advanced organization and execution patterns
---

# Utility Instructions - Extended Reference

## Alias Best Practices

### Naming Conventions
```ic10
# Devices: lowercase descriptive names
alias sensor d0
alias vent d1
alias mainPump d2

# Registers: prefix with 'r' + purpose
alias rTemp r0
alias rPressure r1
alias rTarget r2
alias rState r10      # Use higher registers for state
alias rCounter r11
alias rIndex r12
```

### Grouped Aliases
```ic10
# Group related aliases together

# --- Input Devices ---
alias tempSensor d0
alias pressureSensor d1

# --- Output Devices ---
alias vent d2
alias heater d3
alias display d4

# --- Working Registers ---
alias rTemp r0
alias rPressure r1

# --- State Registers ---
alias rState r10
alias rLastState r11
```

## Define Patterns

### Configuration Block
```ic10
# === CONFIGURATION ===
# Modify these values to tune behavior

define TARGET_TEMP 293.15      # Target temperature (K)
define TEMP_TOLERANCE 5        # Acceptable deviation
define TARGET_PRESSURE 101.325 # Target pressure (kPa)
define PRESSURE_TOLERANCE 10   # Acceptable deviation

define UPDATE_INTERVAL 10      # Ticks between updates
define TIMEOUT 100             # Error timeout (ticks)
```

### Device Hashes
```ic10
# === DEVICE HASHES ===
# For batch operations

define ACTIVE_VENT -842048328
define GAS_SENSOR 546126601
define SOLAR_PANEL -539224550
define LARGE_BATTERY 683671518
```

### State Enums
```ic10
# === STATES ===
define STATE_IDLE 0
define STATE_STARTING 1
define STATE_RUNNING 2
define STATE_STOPPING 3
define STATE_ERROR 4
```

## Sleep Patterns

### Timed Actions
```ic10
# Open door, wait, close
s door Open 1
sleep 5                # 5 seconds
s door Open 0
```

### Airlock Cycle
```ic10
# Pressurize -> Open -> Wait -> Close -> Depressurize
s innerDoor Open 0
s outerDoor Open 0
s vent Mode 0          # Inward
s vent On 1
sleep 10               # Wait for pressurization
s vent On 0
s innerDoor Open 1
sleep 5                # Transit time
s innerDoor Open 0
s vent Mode 1          # Outward
s vent On 1
sleep 10               # Wait for depressurization
s vent On 0
```

### Debounce
```ic10
l r0 button Activate
beqz r0 notPressed

sleep 0.1              # Debounce delay
l r0 button Activate   # Confirm still pressed
beqz r0 notPressed

# Handle confirmed press
s light On 1
sleep 0.5              # Minimum action time
notPressed:
```

## Yield Strategies

### Every Tick
```ic10
main:
  # ... fast operations ...
  yield                # Required
  j main
```

### Periodic Processing
```ic10
alias rCounter r15

main:
  add rCounter rCounter 1
  mod r0 rCounter 10   # Every 10 ticks
  bnez r0 skipHeavy

  # Heavy processing here
  jal expensiveCalculation

skipHeavy:
  # Light processing every tick
  l r0 sensor Temperature
  yield
  j main
```

## Error Handling

### Safe Halt
```ic10
error:
  # Disable all outputs
  s device1 On 0
  s device2 On 0
  s device3 On 0
  sb ALL_VENTS On 0    # Batch disable

  # Visual indicator
  s alarm On 1
  s display Color 2    # Red

  hcf                  # Stop program
```

### Error Recovery Loop
```ic10
errorLoop:
  s alarm On 1
  sleep 1
  s alarm On 0
  sleep 1

  # Check if error cleared
  l r0 sensor Pressure
  bgt r0 10 errorLoop  # Still bad

  # Error cleared
  move state STATE_IDLE
  j main
```

## Code Organization Template

```ic10
# ================================================
# [Program Title]
# ================================================
# Description: [What this program does]
# Version: 1.0
#
# Devices:
#   d0 = [Device 1 description]
#   d1 = [Device 2 description]
# ================================================

# === DEVICE ALIASES ===
alias input1 d0
alias output1 d1

# === REGISTER ALIASES ===
alias rValue r0
alias rState r10

# === CONSTANTS ===
define TARGET 100
define TOLERANCE 5

# === INITIALIZATION ===
move rState 0
s output1 On 0

# === MAIN LOOP ===
main:
  jal readInputs
  jal processLogic
  jal updateOutputs
  yield
  j main

# === SUBROUTINES ===
readInputs:
  l rValue input1 Setting
  j ra

processLogic:
  # ... logic here ...
  j ra

updateOutputs:
  s output1 Setting rValue
  j ra

# === ERROR HANDLER ===
error:
  s output1 On 0
  hcf
```

---
title: Branching Instructions - Extended
category: branching
description: Advanced control flow patterns
---

# Branching Instructions - Extended Reference

## Subroutine Patterns

### Basic Subroutine
```ic10
jal readSensors
jal processData
jal updateOutputs
yield
j main

readSensors:
  l r0 d0 Temperature
  l r1 d0 Pressure
  j ra

processData:
  # Process r0, r1...
  j ra

updateOutputs:
  s d1 Setting r0
  j ra
```

### Nested Subroutines
```ic10
jal outerSub
j continue

outerSub:
  push ra              # Save return address
  jal innerSub         # Call nested sub
  pop ra               # Restore return address
  j ra

innerSub:
  # ... work ...
  j ra
```

## State Machine Patterns

### Enum-Style States
```ic10
define STATE_IDLE 0
define STATE_PRESSURIZE 1
define STATE_OPEN 2
define STATE_DEPRESSURIZE 3
alias state r15

main:
beq state STATE_IDLE stateIdle
beq state STATE_PRESSURIZE statePressurize
beq state STATE_OPEN stateOpen
beq state STATE_DEPRESSURIZE stateDepressurize
move state STATE_IDLE      # Reset on invalid state
j stateIdle

stateIdle:
  # Wait for activation
  l r0 button Activate
  bnez r0 startCycle
  j endTick

startCycle:
  move state STATE_PRESSURIZE
  j endTick

statePressurize:
  s vent On 1
  l r0 sensor Pressure
  blt r0 100 endTick       # Wait for pressure
  move state STATE_OPEN
  j endTick

stateOpen:
  s vent On 0
  s door Open 1
  sleep 5                  # Door open time
  move state STATE_DEPRESSURIZE
  j endTick

stateDepressurize:
  s door Open 0
  s vent Mode 1            # Outward
  s vent On 1
  l r0 sensor Pressure
  bgt r0 5 endTick         # Wait for vacuum
  s vent On 0
  move state STATE_IDLE
  j endTick

endTick:
yield
j main
```

### Timeout Pattern
```ic10
alias rTimer r14
define TIMEOUT 100

# In state that needs timeout:
add rTimer rTimer 1
bgt rTimer TIMEOUT handleTimeout
# Normal state logic...
j endTick

handleTimeout:
move rTimer 0
move state STATE_ERROR
j endTick
```

## Loop Patterns

### For Loop
```ic10
move r0 0              # i = 0
forLoop:
  # ... body using r0 as index ...
  add r0 r0 1          # i++
  blt r0 10 forLoop    # while i < 10
```

### While Loop
```ic10
whileLoop:
  l r0 sensor Pressure
  bge r0 100 exitWhile # Exit when pressure >= 100
  s vent On 1
  yield
  j whileLoop
exitWhile:
s vent On 0
```

### Do-While Loop
```ic10
doWhile:
  # Body always executes at least once
  s device On 1
  yield
  l r0 sensor Temperature
  blt r0 300 doWhile   # Continue while temp < 300
```

## Jump Table
```ic10
# Dispatch based on numeric value
l r0 dial Setting      # 0-5
mul r0 r0 2            # Each case is 2 lines
jr r0                  # Jump relative

# Case 0
j handleCase0
# Case 1
j handleCase1
# Case 2
j handleCase2
# ... etc
```

## Error Recovery

### Graceful Degradation
```ic10
bdns d0 noSensor1
l r0 d0 Temperature
j haveSensor

noSensor1:
bdns d1 noSensor2
l r0 d1 Temperature    # Fallback sensor
j haveSensor

noSensor2:
move r0 293            # Default value

haveSensor:
# Continue with r0
```

### Watchdog Pattern
```ic10
alias rWatchdog r15
define WD_LIMIT 50

main:
  l r0 sensor Temperature
  sna r1 r0 rLastTemp 0.01  # Changed significantly?
  bnez r1 resetWatchdog

  add rWatchdog rWatchdog 1
  bgt rWatchdog WD_LIMIT stuckSensor
  j continue

resetWatchdog:
  move rWatchdog 0
  move rLastTemp r0

stuckSensor:
  # Handle stuck/broken sensor
  s alarm On 1

continue:
yield
j main
```

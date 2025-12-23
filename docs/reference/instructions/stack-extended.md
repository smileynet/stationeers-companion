---
title: Stack Instructions - Extended
category: stack
description: Advanced stack patterns and memory operations
---

# Stack Instructions - Extended Reference

## Circular Buffer

### Data Logger
```ic10
alias memory d0
alias rIndex r15
define BUFFER_SIZE 16

l r0 sensor Temperature
putd memory rIndex r0

add rIndex rIndex 1
mod rIndex rIndex BUFFER_SIZE  # Wrap around
```

### Read History
```ic10
# Get value N samples ago
sub r1 rIndex r0       # Current - offset
add r1 r1 BUFFER_SIZE  # Handle negative
mod r1 r1 BUFFER_SIZE  # Wrap
getd r2 memory r1      # Get historical value
```

## Inter-IC Communication

### Shared Memory Protocol
```ic10
# Memory layout:
# 0: Sender ID
# 1: Message type
# 2-15: Data

define MSG_TEMPERATURE 1
define MSG_PRESSURE 2
define MY_ID 1

alias sharedMem d0

# Send temperature
putd sharedMem 0 MY_ID
putd sharedMem 1 MSG_TEMPERATURE
l r0 sensor Temperature
putd sharedMem 2 r0
```

### Handshake Pattern
```ic10
# Memory slot 0 = ready flag
# Sender sets to 1 when data ready
# Receiver clears to 0 when processed

# Sender:
putd memory 1 r0       # Write data
putd memory 0 1        # Signal ready

# Receiver:
getd r0 memory 0       # Check ready
beqz r0 noData         # Not ready
getd r1 memory 1       # Get data
putd memory 0 0        # Clear ready
noData:
```

## Lookup Tables

### Calibration Curve
```ic10
# Store calibration points in stack
put db 0 0             # Input 0 -> Output 0
put db 1 25            # Input 1 -> Output 25
put db 2 50            # Input 2 -> Output 50
put db 3 75            # Input 3 -> Output 75
put db 4 100           # Input 4 -> Output 100

# Lookup
l r0 dial Setting      # Get input (0-4)
get r1 db r0           # Get calibrated output
```

### State Transition Table
```ic10
# Store next state for each current state
# Index = current state, value = next state
put db 0 1             # State 0 -> State 1
put db 1 2             # State 1 -> State 2
put db 2 3             # State 2 -> State 3
put db 3 0             # State 3 -> State 0 (loop)

# Transition
get r0 db state        # Get next state
move state r0          # Update state
```

## Array Operations

### Find Maximum
```ic10
alias memory d0
define SIZE 10

move r10 0             # Index
move r11 -999999       # Max value

findMax:
  getd r0 memory r10
  max r11 r11 r0       # Update max
  add r10 r10 1
  blt r10 SIZE findMax
# r11 = maximum value
```

### Sum Array
```ic10
move r10 0             # Index
move r11 0             # Sum

sumArray:
  getd r0 memory r10
  add r11 r11 r0
  add r10 r10 1
  blt r10 SIZE sumArray
# r11 = sum
```

## Stack-Based Calculator

### RPN Calculator Pattern
```ic10
# Reverse Polish Notation: 3 4 + 5 *

push 3
push 4
pop r0                 # 4
pop r1                 # 3
add r0 r1 r0           # 3 + 4 = 7
push r0

push 5
pop r0                 # 5
pop r1                 # 7
mul r0 r1 r0           # 7 * 5 = 35
push r0

pop r0                 # Result = 35
```

## Memory-Mapped I/O

### Configuration Storage
```ic10
# Store settings in first 5 slots
define CFG_TARGET_TEMP 0
define CFG_MIN_PRESSURE 1
define CFG_MAX_PRESSURE 2
define CFG_MODE 3
define CFG_ENABLED 4

# Read config at startup
get r0 db CFG_TARGET_TEMP
get r1 db CFG_MIN_PRESSURE
get r2 db CFG_MAX_PRESSURE
get r3 db CFG_MODE
get r4 db CFG_ENABLED

# Use configuration...
```

### Persistent State
```ic10
# Save state to survive power loss
# (Values persist in IC stack)

# Save on state change
put db 0 state
put db 1 counter
put db 2 lastValue

# Restore on startup (line 0-5)
get state db 0
get counter db 1
get lastValue db 2
```

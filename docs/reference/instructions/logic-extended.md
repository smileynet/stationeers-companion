---
title: Logic Instructions - Extended
category: logic
description: Advanced device I/O patterns and edge cases
---

# Logic Instructions - Extended Reference

Advanced patterns for device communication.

## Device Connection Checks

### Safe Device Access
Always check if device is connected before reading:
```ic10
bdns d0 noDevice       # Branch if not connected
l r0 d0 Temperature
j continue
noDevice:
move r0 0              # Default value
continue:
```

### Using sdse/sdns
```ic10
sdse r0 d0             # r0 = 1 if d0 connected
beqz r0 handleMissing
l r1 d0 Pressure
```

## Dynamic Device Access

### Looping Through Devices
```ic10
move r0 0              # Device index
loop:
  ld r1 r0 Temperature # Read from device[r0]
  # ... process r1 ...
  add r0 r0 1
  blt r0 6 loop        # Check all 6 ports
```

### Conditional Device Selection
```ic10
# Select device based on mode
l r0 db Setting        # Read mode from IC's setting
ld r1 r0 Pressure      # Read from device[mode]
```

## Slot Operations Deep Dive

### Checking Slot Contents
```ic10
alias device d0

ls r0 device 0 OccupantHash    # What's in slot 0?
ls r1 device 0 Quantity        # How many?
ls r2 device 0 MaxQuantity     # Stack size?
```

### Item Type Detection
```ic10
define IRON_HASH -666742878
define GOLD_HASH -409226641

alias device d0
ls r0 device 0 OccupantHash

seq r1 r0 IRON_HASH
bnez r1 handleIron

seq r1 r0 GOLD_HASH
bnez r1 handleGold

j handleOther
```

### Iterating Slots
```ic10
alias device d0
move r10 0             # Slot index

slotLoop:
  ls r0 device r10 Quantity
  # ... process slot ...
  add r10 r10 1
  blt r10 10 slotLoop  # 10 slots
```

## Reading Self (db)

### IC Housing Properties
```ic10
l r0 db Setting        # Dial setting on housing
l r1 db On             # Power state
l r2 db Error          # Error state (1 if error)
```

### Using Setting for Mode Selection
```ic10
l r0 db Setting        # User-adjustable dial
beq r0 0 mode0
beq r0 1 mode1
beq r0 2 mode2
j defaultMode
```

### Self-Referencing for Stack
```ic10
# Store values in IC's internal stack
put db 0 r0            # Write r0 to position 0
get r1 db 0            # Read back from position 0
```

## Reagent Operations

### Reading Reagent Contents
```ic10
alias mixer d0
define WATER 123456    # Reagent hash

# Reagent modes:
# 0 = Contents (current amount)
# 1 = Required (recipe requirement)
# 2 = Recipe (output amount)

lr r0 mixer 0 WATER    # Current water in mixer
```

### Checking Multiple Reagents
```ic10
define IRON 111111
define CARBON 222222
define STEEL 333333

lr r0 furnace 0 IRON   # Iron contents
lr r1 furnace 0 CARBON # Carbon contents

# Check if ready for steel
sgt r2 r0 0
sgt r3 r1 0
and r4 r2 r3           # Both present?
```

## Common Patterns

### Sensor Caching
Read once, use multiple times:
```ic10
alias sensor d0
alias rTemp r0
alias rPressure r1
alias rO2 r2

# Read all at start of tick
l rTemp sensor Temperature
l rPressure sensor Pressure
l rO2 sensor RatioOxygen

# Use cached values in logic
sgt r3 rTemp 300
sgt r4 rPressure 150
# ... etc
```

### Value Smoothing
```ic10
alias sensor d0
alias rSmoothed r10
define ALPHA 0.1       # Smoothing factor (0-1)

l r0 sensor Temperature
sub r1 r0 rSmoothed    # Difference from smoothed
mul r1 r1 ALPHA        # Scale by alpha
add rSmoothed rSmoothed r1  # Update smoothed value
```

### Debounced Button
```ic10
alias button d0
alias rLastState r10
alias rPressed r11

l r0 button Activate
sgt r1 r0 rLastState   # Rising edge?
move rLastState r0
move rPressed r1       # rPressed = 1 only on press
```

### Toggle with Button
```ic10
alias button d0
alias light d1
alias rLastBtn r10
alias rLightState r11

l r0 button Activate
sgt r1 r0 rLastBtn     # Rising edge
move rLastBtn r0

beqz r1 noPress
xor rLightState rLightState 1  # Toggle
s light On rLightState
noPress:
```

## Error Handling

### Device Errors
```ic10
l r0 device Error      # 1 if device has error
bnez r0 handleError
```

### Power Loss
```ic10
l r0 device Power      # Current power draw
l r1 device RequiredPower  # Required power
slt r2 r0 r1           # Underpowered?
bnez r2 handlePowerIssue
```

## Tips

1. **Cache reads** - Device reads are expensive, read once per tick
2. **Check connections** - Use bdns/sdse before reading
3. **Use aliases** - Always alias devices for readability
4. **Document ports** - Comment which physical device connects where
5. **Default values** - Provide sensible defaults for missing devices

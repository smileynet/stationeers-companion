---
title: Batch Instructions - Extended
category: batch
description: Advanced batch patterns, network considerations, and complex examples
---

# Batch Instructions - Extended Reference

Advanced patterns for network-wide device control.

## Network Considerations

### Device Discovery
Batch operations find devices on the same data network. Devices must:
- Be connected via data cables (not power cables)
- Have power
- Be on the same network (not isolated by logic I/O)

### No Devices Found
When no matching devices exist:
```ic10
lb r0 NONEXISTENT_HASH Temperature 0
# r0 = 0 (no devices to average)
```

### Performance
Batch operations process all devices in one tick. No performance penalty for large networks.

## Advanced Patterns

### Counting Devices
Count devices by summing a constant:
```ic10
define SOLAR_PANEL -539224550
lb r0 SOLAR_PANEL On 1         # Sum of On values
# If all panels are on, r0 = panel count
# If some off, r0 = count of panels that are on

# Count ALL panels (regardless of state):
# Use a property that's always non-zero or count differently
lb r0 SOLAR_PANEL Maximum 1    # Sum of maximum values
# Divide by typical maximum to estimate count
```

### Threshold Detection
Find if any device exceeds threshold:
```ic10
define GAS_SENSOR 546126601
define PRESSURE_LIMIT 150

lb r0 GAS_SENSOR Pressure 3    # Maximum pressure
bgt r0 PRESSURE_LIMIT alarm    # Any sensor over limit?
```

### Minimum Charge Alert
```ic10
define BATTERY 683671518
define LOW_CHARGE 0.1

lb r0 BATTERY Ratio 2          # Minimum charge ratio
blt r0 LOW_CHARGE lowBattery
```

### Weighted Operations
Control devices based on their individual readings:
```ic10
# Turn on only vents in high-pressure rooms
define ACTIVE_VENT -842048328
define THRESHOLD 110

# This requires per-device logic, not batch
# Batch sets ALL devices to same value
sb ACTIVE_VENT On 1            # All on, or
sb ACTIVE_VENT On 0            # All off

# For per-device control, use named batches or direct connections
```

## Named Batch Strategies

### Zone-Based Control
Label devices with zone names:
```ic10
# Devices labeled "Zone1", "Zone2", etc.
define LIGHT -1407015904
define ZONE1 HASH("Zone1")     # Calculate in-game
define ZONE2 HASH("Zone2")

l r0 motionZone1 Activate
sbn LIGHT ZONE1 On r0

l r1 motionZone2 Activate
sbn LIGHT ZONE2 On r1
```

### Priority Groups
Label devices with priority:
```ic10
# Batteries labeled "Critical", "Normal", "Low"
define BATTERY 683671518
define CRITICAL_HASH 12345     # HASH("Critical")

# Monitor critical batteries specifically
lbn r0 BATTERY CRITICAL_HASH Ratio 2
```

## Slot Batch Applications

### Inventory Monitoring
```ic10
define LOCKER 1886693770

# Total items across all lockers, slot 0
lbs r0 LOCKER 0 Quantity 1     # Sum

# Check if any locker has specific item
define TARGET_HASH -666742878   # Iron
lbs r0 LOCKER 0 OccupantHash 0 # This gets average - not useful

# For item searching, need different approach
```

### Centrifuge Status
```ic10
define CENTRIFUGE 1915566057

# Check if all centrifuges have input
lbs r0 CENTRIFUGE 0 Quantity 2  # Minimum quantity in input slot
beqz r0 needsInput              # If any empty, need input
```

## Hash Calculation

### In-Game Method
1. Place a Logic Writer
2. Connect to target device
3. Writer displays the prefab hash

### Common Device Hashes
```ic10
# Atmospheric
define ACTIVE_VENT -842048328
define PASSIVE_VENT 238631271
define GAS_SENSOR 546126601
define PIPE_ANALYZER 435685051

# Power
define SOLAR_TRACKING -539224550
define LARGE_BATTERY 683671518
define SMALL_BATTERY -1900335881
define APC -1093957350

# Logic
define IC_HOUSING 1512322581
define LOGIC_MEMORY -130638386

# Fabrication
define FURNACE 545937711
define ARC_FURNACE -721824809
define CENTRIFUGE 1915566057
```

## Batch Mode Deep Dive

### Mode 0: Average
```ic10
lb r0 SENSOR Pressure 0
# Sum of all values / count of devices
# Useful for: Overall system state
```

### Mode 1: Sum
```ic10
lb r0 BATTERY Charge 1
# Total of all values
# Useful for: Total power, total inventory
```

### Mode 2: Minimum
```ic10
lb r0 BATTERY Ratio 2
# Smallest value across all devices
# Useful for: Worst-case detection
```

### Mode 3: Maximum
```ic10
lb r0 SENSOR Temperature 3
# Largest value across all devices
# Useful for: Peak detection, any-over-threshold
```

## Complex Example: Power Grid Monitor

```ic10
# Complete power grid monitoring
define SOLAR -539224550
define BATTERY 683671518
define APC -1093957350
alias display d0

# Solar production
lb r0 SOLAR Ratio 0            # Average efficiency
mul r0 r0 100                  # To percentage

# Battery status
lb r1 BATTERY Charge 1         # Total charge
lb r2 BATTERY Maximum 1        # Total capacity
div r3 r1 r2                   # Overall percentage
mul r3 r3 100

# Lowest battery
lb r4 BATTERY Ratio 2          # Minimum charge
mul r4 r4 100

# Display based on state
slt r5 r4 20                   # Any battery below 20%?
select r6 r5 2 1               # Red if low, green if ok
s display Color r6
s display Setting r3           # Show overall percentage
```

## Limitations

1. **No conditional batch** - Can't set only devices meeting criteria
2. **No device enumeration** - Can't iterate through individual devices
3. **Same value to all** - `sb` sets identical value to every matching device
4. **Name hash required** - Must know hash, can't search by name string

### Workarounds
- Use named batches with intentional naming conventions
- Use multiple networks to segment device groups
- Use direct connections (d0-d5) for devices needing individual control

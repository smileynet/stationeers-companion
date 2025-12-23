---
title: Occupancy Sensor
category: sensors
prefab_hash: 1363084076
---

# Occupancy Sensor

Detects player presence in an area. Useful for automation based on room occupancy.

**Prefab Hash**: `1363084076`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| Activate | Player detected | Boolean |
| On | Power state | Boolean |
| Power | Has power connection | Boolean |
| Error | Error state | Boolean |
| Mode | Detection mode | Integer |
| Setting | Sensitivity | Float |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Mode | Set detection mode | Integer |
| Setting | Set sensitivity | Float |

## Common Use Cases

### Occupancy-Based Lighting
```ic10
alias sensor d0
alias light d1

main:
l r0 sensor Activate     # Someone in room?
s light On r0            # Light on if occupied
yield
j main
```

### Auto-Lock When Unoccupied
```ic10
alias sensor d0
alias door d1
define DELAY 5           # Seconds before locking

alias rTimer r1

main:
l r0 sensor Activate
bnez r0 resetTimer       # Reset if occupied

# No one present - count down
sub rTimer rTimer 1
bgtz rTimer endTick      # Still counting
s door Lock 1            # Lock after delay
j endTick

resetTimer:
move rTimer DELAY
s door Lock 0            # Unlock while occupied

endTick:
sleep 1
j main
```

### Multi-Zone Occupancy
```ic10
# Track if ANY zone is occupied
alias zone1 d0
alias zone2 d1
alias zone3 d2
alias display d3

main:
l r0 zone1 Activate
l r1 zone2 Activate
l r2 zone3 Activate

# OR all zones together
or r3 r0 r1
or r3 r3 r2

s display Setting r3     # 1 if any occupied
yield
j main
```

## IC10 Example

```ic10
# HVAC activation based on occupancy
alias occupancy d0
alias vent d1
alias heater d2
alias sensor d3          # Temperature sensor

define COMFORT_TEMP 293  # 20C

main:
l r0 occupancy Activate

# If unoccupied, turn off HVAC
beqz r0 hvacOff

# Occupied: regulate temperature
l r1 sensor Temperature
slt r2 r1 COMFORT_TEMP   # Below comfort?
s heater On r2
s vent On 1
j endTick

hvacOff:
s heater On 0
s vent On 0

endTick:
yield
j main
```

## Notes

- Detects players within sensor range
- Does not detect NPCs or items
- Use Motion Sensor for movement detection
- Combine with timer for delayed actions
- Power required for operation

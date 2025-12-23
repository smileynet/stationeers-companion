---
title: Motion Sensor
category: sensors
prefab_hash: -1677616158
---

# Motion Sensor

Detects movement within its detection cone. Triggers on any movement, not just players.

**Prefab Hash**: `-1677616158`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| Activate | Motion detected | Boolean |
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

## Differences from Occupancy Sensor

| Aspect | Motion Sensor | Occupancy Sensor |
|--------|---------------|------------------|
| Triggers on | Movement | Presence |
| Stays active | Only during motion | While player present |
| Use case | Door openers | Room automation |
| Detection | Directional cone | Area-based |

## Common Use Cases

### Motion-Activated Door
```ic10
alias motion d0
alias door d1

main:
l r0 motion Activate
s door Open r0           # Open while motion detected
yield
j main
```

### Motion-Triggered Alarm
```ic10
alias motion d0
alias alarm d1
alias light d2

main:
l r0 motion Activate
s alarm On r0
s light On r0            # Flash light with alarm
yield
j main
```

### Delayed Auto-Close
```ic10
alias motion d0
alias door d1
define HOLD_TIME 3       # Seconds to stay open

alias rTimer r1

main:
l r0 motion Activate
bnez r0 motionDetected

# No motion - count down
ble rTimer 0 closeDoor
sub rTimer rTimer 1
j endTick

motionDetected:
s door Open 1
move rTimer HOLD_TIME
j endTick

closeDoor:
s door Open 0

endTick:
sleep 1
j main
```

## IC10 Example

```ic10
# Security system with motion detection
alias motion1 d0
alias motion2 d1
alias alarm d2
alias display d3
alias switch d4          # Arm/disarm switch

main:
l r4 switch On           # System armed?
beqz r4 disarmed

# Check both motion sensors
l r0 motion1 Activate
l r1 motion2 Activate
or r2 r0 r1              # Any motion?

s alarm On r2
s display Setting r2
j endTick

disarmed:
s alarm On 0
s display Setting 0

endTick:
yield
j main
```

## Notes

- Directional sensor - must face detection area
- Brief activation - only active during movement
- Good for automatic doors
- Use Occupancy Sensor for continuous presence detection
- Sensitivity affects detection range

---
title: Logic Switch
category: logic
prefab_hash: 124499454
---

# Logic Switch

A manual toggle switch that can be flipped on/off by players and controlled via IC10.

**Prefab Hash**: `124499454`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Current switch state | Boolean |
| Open | Same as On (legacy) | Boolean |
| Activate | Momentary activation state | Boolean |
| Lock | Locked state (prevents manual toggle) | Boolean |
| Power | Power connection state | Boolean |
| Error | Error state | Boolean |
| Setting | Current setting value | Float (0-100) |
| Mode | Operating mode | Integer |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Set switch state | Boolean |
| Open | Same as On (legacy) | Boolean |
| Lock | Lock/unlock manual control | Boolean |
| Setting | Set value | Float (0-100) |
| Mode | Set operating mode | Integer |

## Common Use Cases

### Read Switch State
```ic10
alias switch d0
l r0 switch On           # Read current state
beqz r0 switchOff
# Switch is ON
j continue
switchOff:
# Switch is OFF
continue:
```

### Toggle with Lock
```ic10
alias switch d0
s switch Lock 1          # Lock to prevent manual changes
l r0 switch On
xor r0 r0 1              # Toggle state
s switch On r0
s switch Lock 0          # Unlock
```

## IC10 Example

```ic10
# Use switch to control a device
alias switch d0
alias device d1

main:
l r0 switch On
s device On r0           # Mirror switch state to device
yield
j main
```

## Notes

- Setting range depends on switch type (dial switches have 0-100)
- Lock prevents players from manually flipping the switch
- Mode is typically unused for basic switches

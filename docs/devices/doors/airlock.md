---
title: Airlock
category: doors
prefab_hash: -821339274
---

# Airlock

Airtight door that maintains atmosphere separation. Essential for base pressurization.

**Prefab Hash**: `-821339274`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Open | Door is open | Boolean |
| Lock | Locked state | Boolean |
| Power | Has power connection | Boolean |
| Error | Error state | Boolean |
| Mode | Operating mode | Integer |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Open | Open/close door | Boolean |
| Lock | Lock/unlock | Boolean |
| Mode | Set operating mode | Integer |

## Common Use Cases

### Pressure-Safe Airlock
```ic10
alias door d0
alias sensor d1          # Inside atmosphere sensor
alias sensorOut d2       # Outside sensor
define SAFE_DIFF 10      # Max kPa difference

main:
l r0 sensor Pressure
l r1 sensorOut Pressure
sub r2 r0 r1
abs r2 r2                # Absolute difference

sgt r3 r2 SAFE_DIFF      # Too much difference?
s door Lock r3           # Lock if unsafe
yield
j main
```

### Airlock Cycling
```ic10
alias doorIn d0
alias doorOut d1
alias vent d2
alias sensor d3
define TARGET 101

# Close outer, pump to pressure, open inner
s doorOut Open 0
s doorOut Lock 1
s vent On 1

cycle:
l r0 sensor Pressure
slt r1 r0 TARGET
bnez r1 cycle            # Wait for pressure

s vent On 0
s doorIn Open 1
```

## IC10 Example

```ic10
# Simple airlock with pressure interlock
alias airlock d0
alias sensor d1
define MIN_PRESSURE 80
define MAX_PRESSURE 120

main:
l r0 sensor Pressure

# Only allow opening in safe pressure range
sgt r1 r0 MIN_PRESSURE
slt r2 r0 MAX_PRESSURE
and r3 r1 r2             # Both conditions met?

# Invert for lock (lock if unsafe)
seqz r4 r3
s airlock Lock r4

yield
j main
```

## Notes

- Airtight seal when closed - maintains pressure differential
- Can be damaged by extreme pressure differences
- Lock prevents both manual and IC10 operation
- Consider pressure equalization before opening

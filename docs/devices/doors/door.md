---
title: Door
category: doors
prefab_hash: 168615924
---

# Door

Standard door for interior use. Not airtight - allows gas flow when closed.

**Prefab Hash**: `168615924`

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

### Motion-Activated Door
```ic10
alias door d0
alias motion d1

main:
l r0 motion Activate     # Motion detected?
s door Open r0           # Open if motion
yield
j main
```

### Timed Auto-Close
```ic10
alias door d0
alias motion d1
define DELAY 3           # Seconds to stay open

main:
l r0 motion Activate
beqz r0 checkClose

# Motion detected - open and reset timer
s door Open 1
move r1 DELAY
j main

checkClose:
ble r1 0 main           # Already closed
sub r1 r1 1             # Decrement timer
sleep 1
bgtz r1 main            # Still counting
s door Open 0           # Close door
j main
```

## IC10 Example

```ic10
# Security door with switch control
alias door d0
alias switch d1
alias light d2

main:
l r0 switch On
s door Open r0
s door Lock 0            # Allow manual operation

# Status light (green=unlocked, red=locked)
l r1 door Lock
select r2 r1 4 2         # 4=red, 2=green
s light Color r2

yield
j main
```

## Notes

- Not airtight - gases pass through even when closed
- Use Airlock for pressure-critical areas
- Less power consumption than airlocks
- Faster open/close cycle than airlocks

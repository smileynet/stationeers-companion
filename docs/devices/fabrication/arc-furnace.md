---
title: Arc Furnace
category: fabrication
prefab_hash: -721824809
---

# Arc Furnace

Advanced electric smelting device. Uses power instead of combustion for cleaner operation.

**Prefab Hash**: `-721824809`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Power | Has power connection | Boolean |
| Activate | Currently smelting | Boolean |
| Idle | Not actively smelting | Boolean |
| Error | Error state | Boolean |
| Lock | Locked state | Boolean |
| Reagents | Has reagents to smelt | Boolean |
| RecipeHash | Current recipe hash | Integer |
| ImportCount | Items imported | Integer |
| ExportCount | Items exported | Integer |
| PrefabHash | Device type identifier | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Activate | Start/stop smelting | Boolean |
| Lock | Lock/unlock | Boolean |

## Common Use Cases

### Auto-Smelt Array
```ic10
# Control multiple arc furnaces via batch
define ARC_FURNACE -721824809

main:
lb r0 ARC_FURNACE Reagents 3  # Max of all (any has ore?)
sb ARC_FURNACE Activate r0    # Activate all with ore
yield
j main
```

### Power-Aware Operation
```ic10
alias furnace d0
alias battery d1
define MIN_CHARGE 0.3

main:
l r0 battery Ratio
sgt r1 r0 MIN_CHARGE     # Enough power?
l r2 furnace Reagents    # Has ore?
and r3 r1 r2
s furnace Activate r3    # Only smelt if power ok
yield
j main
```

## IC10 Example

```ic10
# Arc furnace array controller
alias furnace1 d0
alias furnace2 d1
alias furnace3 d2

main:
# Check each furnace for ore and activate
l r0 furnace1 Reagents
s furnace1 Activate r0

l r0 furnace2 Reagents
s furnace2 Activate r0

l r0 furnace3 Reagents
s furnace3 Activate r0

yield
j main
```

## Notes

- No combustion needed - pure electric operation
- Cleaner than regular furnace (no exhaust gases)
- Higher power consumption than regular furnace
- Faster smelting than combustion furnace
- Idle state indicates furnace is ready but no work

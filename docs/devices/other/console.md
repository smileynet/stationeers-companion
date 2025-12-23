---
title: Console
category: other
prefab_hash: -413111258
---

# Console

Computer interface for displaying information and receiving player input.

**Prefab Hash**: `-413111258`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Power | Has power connection | Boolean |
| Open | Interface is open | Boolean |
| Error | Error state | Boolean |
| Mode | Display mode | Integer |
| Setting | Current display value | Float |
| Color | Display color index | Integer |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Mode | Set display mode | Integer |
| Setting | Set display value | Float |
| Color | Set display color | Integer (0-11) |

## Color Values

| Value | Color |
|-------|-------|
| 0 | Blue |
| 1 | Gray |
| 2 | Green |
| 3 | Orange |
| 4 | Red |
| 5 | Yellow |
| 6 | White |
| 7 | Black |
| 8 | Brown |
| 9 | Khaki |
| 10 | Pink |
| 11 | Purple |

## Common Use Cases

### Display Sensor Value
```ic10
alias sensor d0
alias console d1

main:
l r0 sensor Pressure
s console Setting r0     # Display pressure value
yield
j main
```

### Status Indicator with Color
```ic10
alias sensor d0
alias console d1
define SAFE_PRESSURE 101

main:
l r0 sensor Pressure
s console Setting r0

# Green if safe, red if not
sgt r1 r0 SAFE_PRESSURE
select r2 r1 4 2         # 4=red, 2=green
s console Color r2
yield
j main
```

## IC10 Example

```ic10
# Display battery percentage with color coding
alias battery d0
alias console d1

main:
l r0 battery Ratio
mul r0 r0 100            # Convert to percentage
s console Setting r0

# Color based on charge level
slt r1 r0 20             # Below 20%?
select r2 r1 4 2         # Red if low, green if ok
s console Color r2
yield
j main
```

## Notes

- Color changes the display backlight/text color
- Mode may affect display formatting (device-specific)
- Setting accepts any float value for display

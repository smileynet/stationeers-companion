---
title: LED Display
category: other
prefab_hash: -815193061
variants:
  - name: LED Display (Small)
    hash: -815193061
  - name: LED Display (Medium)
    hash: -289015349
---

# LED Display

Numeric display for showing values. Available in small and medium sizes.

**Prefab Hashes**:
- Small: `-815193061`
- Medium: `-289015349`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Power | Has power connection | Boolean |
| Error | Error state | Boolean |
| Setting | Currently displayed value | Float |
| Color | Display color index | Integer |
| Mode | Display mode | Integer |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Setting | Value to display | Float |
| Color | Display color | Integer (0-11) |
| Mode | Display mode | Integer |

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
alias display d1

main:
l r0 sensor Pressure
s display Setting r0
yield
j main
```

### Color-Coded Display
```ic10
alias sensor d0
alias display d1
define WARN_LEVEL 80
define CRIT_LEVEL 50

main:
l r0 sensor Ratio
mul r0 r0 100            # Convert to percentage
s display Setting r0

# Color based on level
slt r1 r0 CRIT_LEVEL     # Below critical?
slt r2 r0 WARN_LEVEL     # Below warning?

select r3 r1 4 3         # Red if critical, else orange
select r3 r2 r3 2        # Keep red/orange if warning, else green
s display Color r3

yield
j main
```

### Multiple Display Dashboard
```ic10
# Display different values on multiple displays
alias pressure d0
alias temp d1
alias dispP d2
alias dispT d3

main:
l r0 pressure Pressure
l r1 temp Temperature
sub r1 r1 273            # Convert K to C

s dispP Setting r0
s dispT Setting r1

yield
j main
```

## IC10 Example

```ic10
# Battery monitor with color-coded display
alias battery d0
alias display d1

define LOW 20
define MED 50

main:
l r0 battery Ratio
mul r0 r0 100
s display Setting r0

# Color: Red < 20%, Orange < 50%, Green >= 50%
slt r1 r0 LOW
slt r2 r0 MED

select r3 r1 4 0         # Red if low
select r3 r2 r3 3        # Orange if medium (and not low)
select r3 r2 r3 2        # Green if high

# Apply color only if not red
beq r1 1 setColor        # Keep red
beq r2 1 setOrange
move r3 2                # Green
j setColor
setOrange:
move r3 3
setColor:
s display Color r3

yield
j main
```

## Notes

- Setting accepts any float value
- Large numbers may not display fully
- Color affects digit color on display
- Mode may affect decimal places (device-specific)
- Medium display is easier to read at distance

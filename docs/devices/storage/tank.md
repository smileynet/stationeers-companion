---
title: Tank
category: storage
prefab_hash: -483278802
variants:
  - name: Tank (Small)
    hash: -483278802
    capacity: 1000L
  - name: Tank (Medium)
    hash: -1334068458
    capacity: 16000L
  - name: Tank (Large)
    hash: 1520698177
    capacity: 64000L
---

# Tank

Gas storage container. Available in small, medium, and large sizes.

**Prefab Hashes**:
- Small (1000L): `-483278802`
- Medium (16000L): `-1334068458`
- Large (64000L): `1520698177`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Valve state | Boolean |
| Pressure | Internal pressure | kPa |
| Temperature | Internal temperature | Kelvin |
| Volume | Container volume | Liters |
| TotalMoles | Total gas moles | mol |
| RatioOxygen | O2 concentration | 0-1 |
| RatioNitrogen | N2 concentration | 0-1 |
| RatioCarbonDioxide | CO2 concentration | 0-1 |
| RatioVolatiles | H2 concentration | 0-1 |
| RatioPollutant | X concentration | 0-1 |
| RatioWater | H2O concentration | 0-1 |
| RatioNitrousOxide | N2O concentration | 0-1 |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Open/close valve | Boolean |

## Common Use Cases

### Monitor Tank Pressure
```ic10
alias tank d0
alias display d1
define MAX_PRESSURE 50000  # 50 MPa

main:
l r0 tank Pressure
s display Setting r0

# Warning if approaching max
div r1 r0 MAX_PRESSURE
mul r1 r1 100            # Percentage
yield
j main
```

### Auto-Fill System
```ic10
alias tank d0
alias pump d1
define TARGET_PRESSURE 10000

main:
l r0 tank Pressure
slt r1 r0 TARGET_PRESSURE  # Below target?
s pump On r1               # Fill if needed
yield
j main
```

### Gas Purity Check
```ic10
alias tank d0
alias display d1
define MIN_O2 0.95        # 95% pure O2

main:
l r0 tank RatioOxygen
sge r1 r0 MIN_O2         # Pure enough?
mul r2 r0 100
s display Setting r2

# Color: green if pure, red if not
select r3 r1 2 4
s display Color r3
yield
j main
```

## IC10 Example

```ic10
# Tank farm pressure balancing
alias tank1 d0
alias tank2 d1
alias pump d2             # Between tanks
define DIFF_THRESHOLD 100 # kPa difference

main:
l r0 tank1 Pressure
l r1 tank2 Pressure
sub r2 r0 r1             # Difference
abs r3 r2                # Absolute difference

# Only pump if significant difference
sgt r4 r3 DIFF_THRESHOLD
s pump On r4

# Direction based on which is higher
sgt r5 r0 r1             # Tank1 higher?
s pump Mode r5           # 0=reverse, 1=forward
yield
j main
```

## Batch Operations

```ic10
# Monitor all large tanks on network
define TANK_LARGE 1520698177

lb r0 TANK_LARGE Pressure 0    # Average pressure
lb r1 TANK_LARGE Pressure 1    # Sum of pressures
lb r2 TANK_LARGE Pressure 2    # Minimum pressure
lb r3 TANK_LARGE Pressure 3    # Maximum pressure
```

## Notes

- Tanks have no power requirement
- On controls valve (for pipe connections)
- Pressure can be very high - monitor carefully
- Temperature affects pressure (ideal gas law)
- Different sizes share same logic types

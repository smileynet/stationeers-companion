---
title: Solid Fuel Generator
category: power
prefab_hash: -2016970735
---

# Solid Fuel Generator

Power generator that burns solid fuels (coal, biomass) to produce electricity.

**Prefab Hash**: `-2016970735`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Activate | Currently generating | Boolean |
| Power | Power output | Watts |
| PowerActual | Current power output | Watts |
| PowerPotential | Maximum possible output | Watts |
| Combustion | Active combustion | Boolean |
| Fuel | Has fuel loaded | Boolean |
| Error | Error state | Boolean |
| Lock | Locked state | Boolean |
| Temperature | Internal temperature | Kelvin |
| Pressure | Internal pressure | kPa |
| TotalMoles | Gas moles inside | mol |
| RatioOxygen | O2 concentration | 0-1 |
| RatioCarbonDioxide | CO2 concentration | 0-1 |
| RatioVolatiles | H2 concentration | 0-1 |
| RatioPollutant | X concentration | 0-1 |
| PrefabHash | Device type identifier | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Activate | Start/stop generation | Boolean |
| Lock | Lock/unlock | Boolean |

## Common Use Cases

### Auto-Start on Low Battery
```ic10
alias generator d0
alias battery d1
define LOW_CHARGE 0.2
define HIGH_CHARGE 0.8

main:
l r0 battery Ratio
l r1 generator Fuel      # Has fuel?

slt r2 r0 LOW_CHARGE     # Below 20%?
and r3 r2 r1             # Low AND has fuel
s generator Activate r3

# Stop when batteries full
sgt r4 r0 HIGH_CHARGE
s generator Activate 0   # Stop generating
yield
j main
```

### Backup Power Controller
```ic10
alias generator d0
alias battery d1
alias solar d2
define MIN_CHARGE 0.3

main:
l r0 battery Ratio
l r1 solar PowerActual   # Solar output

# Run generator if low battery AND no solar
slt r2 r0 MIN_CHARGE
seqz r3 r1               # No solar power?
and r4 r2 r3
s generator Activate r4

yield
j main
```

## IC10 Example

```ic10
# Solid fuel generator with display
alias generator d0
alias battery d1
alias display d2
define THRESHOLD 0.25

main:
# Read states
l r0 battery Ratio
l r1 generator Combustion
l r2 generator PowerActual

# Display current output
s display Setting r2

# Auto-control based on battery
slt r3 r0 THRESHOLD
l r4 generator Fuel
and r5 r3 r4             # Low charge AND has fuel
s generator Activate r5

yield
j main
```

## Notes

- Requires O2 for combustion (connect to atmosphere or pipe)
- Produces CO2 and heat as byproducts
- Must be vented to prevent pressure buildup
- Coal is most common fuel source
- Fuel slot accepts: Coal, Charcoal, Biomass

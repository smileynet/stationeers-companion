---
title: Furnace
category: fabrication
prefab_hash: 545937711
---

# Furnace

Basic smelting device for processing ores into ingots. Requires fuel and proper atmosphere.

**Prefab Hash**: `545937711`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Activate | Currently smelting | Boolean |
| Combustion | Active combustion | Boolean |
| Temperature | Internal temperature | Kelvin |
| Pressure | Internal pressure | kPa |
| Lock | Locked state | Boolean |
| Open | Door open state | Boolean |
| Error | Error state | Boolean |
| Mode | Operating mode | Integer |
| TotalMoles | Gas moles inside | mol |
| Reagents | Has reagents to smelt | Boolean |
| ImportCount | Items imported | Integer |
| ExportCount | Items exported | Integer |
| Maximum | Maximum capacity | Integer |
| RatioOxygen | O2 concentration | 0-1 |
| RatioNitrogen | N2 concentration | 0-1 |
| RatioCarbonDioxide | CO2 concentration | 0-1 |
| RatioVolatiles | H2 concentration | 0-1 |
| RatioPollutant | X concentration | 0-1 |
| RatioWater | H2O concentration | 0-1 |
| RatioNitrousOxide | N2O concentration | 0-1 |
| PrefabHash | Device type identifier | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| Activate | Start/stop smelting | Boolean |
| Open | Open/close door | Boolean |
| Lock | Lock/unlock | Boolean |
| Setting | Target temperature | Kelvin |
| RecipeHash | Recipe to use | Hash |
| ClearMemory | Clear recipe memory | Boolean |

## Common Use Cases

### Auto-Start When Loaded
```ic10
alias furnace d0

main:
l r0 furnace Reagents    # Has ore?
s furnace Activate r0    # Start if has ore
yield
j main
```

### Temperature-Controlled Smelting
```ic10
alias furnace d0
alias sensor d1          # Pipe analyzer on output
define TARGET_TEMP 800

main:
l r0 sensor Temperature
slt r1 r0 TARGET_TEMP    # Below target?
s furnace Activate r1    # Run if cold
yield
j main
```

## IC10 Example

```ic10
# Automated furnace with temperature monitoring
alias furnace d0
alias display d1
define SMELT_TEMP 480    # Iron smelting temp

main:
# Read furnace state
l r0 furnace Temperature
l r1 furnace Reagents
l r2 furnace Combustion

# Display temperature
s display Setting r0

# Start if has ore and temp is adequate
and r3 r1 r2             # Has fuel AND ore
s furnace Activate r3
yield
j main
```

## Notes

- Combustion requires O2 + fuel (Volatiles or coal)
- Temperature must reach ore melting point to smelt
- Door must be closed for combustion
- Different ores require different temperatures

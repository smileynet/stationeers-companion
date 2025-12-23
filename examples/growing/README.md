# Growing & Hydroponics Examples

IC10 scripts for plant cultivation and greenhouse management.

## When You Need This

- Growing food sustainably
- Managing greenhouse atmosphere
- Automating harvesting
- Controlling grow lights

## Difficulty

| Script | Lines | Complexity |
|--------|-------|------------|
| `harvie.ic10` | Simple | Auto-harvest |
| `greenhouse_fill.ic10` | Medium | Atmosphere setup |
| `greenhouse_air_quality.ic10` | Medium | Ongoing monitoring |

## Plant Requirements

Different plants need:
- **Temperature**: Usually 293-313K (20-40°C)
- **Pressure**: 20-200 kPa typically
- **Light**: Some need day/night cycles
- **CO₂**: Some plants consume CO₂
- **Water**: Via hydroponics tray piping

## Key Patterns

**Environment Monitoring:**
```ic10
# Check temperature, pressure, gas ratios
# Adjust vents, AC, or lights as needed
```

**Harvesting:**
```ic10
# Check plant maturity
# Activate harvie when ready
# Sort output
```

## Common Devices

- Hydroponics Tray
- Harvie (automated harvester)
- Grow Light
- Gas Sensor (for CO₂/O₂)
- Pipe Analyzer (for water)

## Start Here

1. `harvie.ic10` - Automated harvesting
2. `greenhouse_fill.ic10` - Initial atmosphere setup
3. `greenhouse_air_quality.ic10` - Ongoing management

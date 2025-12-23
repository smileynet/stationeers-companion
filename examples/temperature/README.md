# Temperature Control Examples

IC10 scripts for heating, cooling, and climate control.

## When You Need This

- Growing plants (specific temperature ranges)
- Preventing equipment from overheating
- Keeping habitats comfortable
- Managing heat exchangers

## Difficulty

| Script | Lines | Complexity |
|--------|-------|------------|
| `water-cooler.ic10` | Simple | Basic on/off |
| `temperature-controlled-room.ic10` | Medium | Hysteresis |
| `temperaturecontroller.ic10` | Medium | Multi-zone |
| `vulcan_ac.ic10` | Advanced | Planet-specific |

## Key Patterns

**Hysteresis (prevent oscillation):**
```ic10
# Turn on cooling if temp > 300K
# Turn off cooling if temp < 295K
# 5K deadband prevents rapid switching
```

**PID Control (precise targeting):**
See `../patterns/pid-controller-template.ic10`

## Common Devices

- Air Conditioner
- Wall Cooler / Heater
- Heat Exchanger
- Radiator
- Active Vent (for gas exchange)

## Start Here

1. `temperature-controlled-room.ic10` - Basic room control
2. `room-cooler-via-exchange.ic10` - Using heat exchangers
3. `paired-ac-units.ic10` - Coordinated cooling

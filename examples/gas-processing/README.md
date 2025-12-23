# Gas Processing Examples

IC10 scripts for filtration, mixing, and gas handling.

## When You Need This

- Separating atmospheric gases
- Creating fuel mixtures (H₂ + O₂)
- Filling tanks with specific gases
- Managing waste gases

## Difficulty

| Script | Lines | Complexity |
|--------|-------|------------|
| `filtercontroller.ic10` | Medium | Basic filtering |
| `gas-mixer-fuel-regulator.ic10` | Advanced | Ratio control |
| `nitrogen-condensation-regulator.ic10` | Advanced | Phase change |

## Key Concepts

**Filtration:**
- Use filtration units to separate mixed gases
- Control pump activation based on tank levels
- Monitor pressure to prevent over-filling

**Mixing:**
- Calculate ratios based on moles, not pressure
- Temperature affects gas behavior
- Common ratios: 2:1 H₂:O₂ for fuel cells

**Condensation:**
- Gases condense at specific temperatures
- Use for liquid nitrogen, water production
- Requires precise temperature control

## Common Devices

- Filtration Unit
- Gas Mixer (deprecated, use pumps)
- Volume Pump / Turbo Pump
- Tank (various sizes)
- Pipe Analyzer

## Start Here

1. `filtercontroller.ic10` - Basic filtration setup
2. `filterpumps.ic10` - Pump-based filtering
3. `gas-mixer-fuel-regulator.ic10` - Fuel production

# Gas Mixing Resources Guide

> Last updated: 2025-12-22
> Search terms: gas mixer, fuel mixer, air ratio

## Summary

Gas mixing automation controls the blend of gases for breathable atmosphere or fuel production. Scripts manage gas ratios, pressure, and flow rates through mixers.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [Gas Mixer](https://steamcommunity.com/sharedfiles/filedetails/?id=3289986151) | Bunstructors | Clean gas mixing implementation. |
| [Gas Mixer Program](https://steamcommunity.com/sharedfiles/filedetails/?id=3057999410) | nomial | Programmable mixer control. |
| [Gas Mixer Safety Control](https://steamcommunity.com/sharedfiles/filedetails/?id=2837310506) | Murk | Includes safety interlocks. |
| [Gas Mixer Fixer](https://steamcommunity.com/sharedfiles/filedetails/?id=1883313543) | Preston | Fixes common mixing issues. |
| [Gas Mixer](https://steamcommunity.com/sharedfiles/filedetails/?id=1669121935) | CagoBHuK | Basic mixer control. |

## Key Concepts

- Gas Mixer has two inputs, blends to output
- Control `Setting` (0-100) for mix ratio
- Read `RatioOxygen`, `RatioNitrogen`, etc. for current mix
- Target atmosphere: ~21% O2, ~78% N2

## Common Mix Targets

| Use Case | O2 | N2 | Other |
|----------|----|----|-------|
| Breathable air | 21% | 79% | - |
| H2 Fuel | 66% H2 | - | 33% O2 |
| Welding gas | - | - | 100% specific |

## Logic Types

**Gas Mixer**:
- `Setting` - Mix ratio (0-100%)
- `On` - Enable mixing
- `Pressure` - Output pressure

**Pipe Analyzer** (for monitoring):
- `RatioOxygen`, `RatioNitrogen`, etc.
- `TotalMoles` - Amount of gas
- `Temperature`

## Related Local Examples

See `examples/gas-processing/gas-mixer-*.ic10` for mixing examples.

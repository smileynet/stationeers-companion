# Filtration Systems Resources Guide

> Last updated: 2025-12-22
> Search terms: filtration, gas filter, atmosphere filter

## Summary

Filtration automation manages gas separation and purification. Scripts control filter units to extract specific gases from mixed atmospheres or process waste gases.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [Internal Filtration Controller](https://steamcommunity.com/sharedfiles/filedetails/?id=2854737532) | CowsAreEvil | Internal atmosphere filtration. |
| [Osarus's Filtration Control](https://steamcommunity.com/sharedfiles/filedetails/?id=2966410020) | Osarus | Comprehensive filtration system. |
| [Filtration Pilot (OnBoard)](https://steamcommunity.com/sharedfiles/filedetails/?id=2978782048) | Sharidan | Portable/vehicle filtration. |
| [Compact Filtration](https://steamcommunity.com/sharedfiles/filedetails/?id=3603064996) | TrippleTrip | Space-efficient design. |
| [Autom. Filtration + Filter status](https://steamcommunity.com/sharedfiles/filedetails/?id=1559164765) | Gameagle | Automated with status display. |

## Key Concepts

- Filtration units separate one gas type from mixture
- Control `On` to run filtration
- Monitor output tanks to prevent overpressure
- Use batch operations for multiple filter banks
- Consider power consumption of pumps

## Logic Types

**Filtration Unit**:
- `On` - Enable filtration
- `Mode` - Select gas to filter (by gas type index)
- `Setting` - Filter intensity/speed

**Pipe Analyzer** (monitoring):
- `RatioOxygen`, `RatioNitrogen`, `RatioCarbonDioxide`, etc.
- `Pressure` - Current pressure
- `TotalMoles` - Gas quantity

## Common Filtration Tasks

1. **Atmosphere cleanup**: Remove pollutants (CO2, volatiles)
2. **Gas separation**: Extract specific gases for storage
3. **Fuel processing**: Separate H2 and O2 from water electrolysis
4. **Mars atmosphere**: Extract CO2 for processing

## Related Local Examples

See `examples/gas-processing/filtration*.ic10` and `examples/atmosphere/filtration.ic10`.

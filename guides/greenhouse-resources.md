# Greenhouse/Farming Resources Guide

> Last updated: 2025-12-22
> Search terms: greenhouse, hydroponics, farming, harvie

## Summary

Greenhouse automation manages plant growth conditions including atmosphere, temperature, lighting, and harvesting. Scripts monitor CO2/O2 levels and control environmental systems.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [Greenhouse Monitor](https://steamcommunity.com/sharedfiles/filedetails/?id=2378338576) | CowsAreEvil | Comprehensive greenhouse monitoring. |
| [Greenhouse Atmo Balancer](https://steamcommunity.com/sharedfiles/filedetails/?id=3292736448) | Bunstructors | Automatic atmosphere balancing. |
| [Greenhouse Temp](https://steamcommunity.com/sharedfiles/filedetails/?id=2352916713) | ArrowStrat | Temperature-focused control. |
| [Greenhouse CO2 and Temperature Regulator](https://steamcommunity.com/sharedfiles/filedetails/?id=1674422103) | Maireen | Combined CO2/temp management. |
| [Greenhouse Gas Control](https://steamcommunity.com/sharedfiles/filedetails/?id=2337295385) | MemoJoking | Gas ratio control for plants. |

## Key Concepts

- Plants consume CO2 and produce O2 during growth
- Monitor `RatioCarbonDioxide` - plants need ~2% CO2
- Control lighting with `On` based on growth stage
- Harvie automates plant harvesting when mature
- Temperature affects growth rate

## Plant Requirements

| Factor | Target |
|--------|--------|
| CO2 | 1-5% |
| O2 | Present |
| Temperature | 293-303K |
| Light | Required during growth |

## Logic Types

**Harvie**:
- `Activate` - Trigger harvest
- `SolarAngle` - Light level

**Plants (slot reads)**:
- `Growth` - Current growth stage
- `Mature` - Ready for harvest

## Automation Patterns

1. **CO2 injection**: Add CO2 when ratio drops
2. **O2 extraction**: Remove excess O2 to maintain CO2 ratio
3. **Auto-harvest**: Trigger Harvie when plants mature
4. **Light control**: Match day/night or force constant light

## Related Local Examples

See `examples/growing/` for greenhouse scripts including `harvie.ic10` and `greenhouse_master.ic10`.

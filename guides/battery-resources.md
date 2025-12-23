# Battery Management Resources Guide

> Last updated: 2025-12-22
> Search terms: battery, power management, APC, charge controller

## Summary

Battery management scripts monitor charge levels, display power status, and control charging/discharging to maintain stable power grids.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [Station Battery Display (2023)](https://steamcommunity.com/sharedfiles/filedetails/?id=3117351595) | Kassfaru | Updated 2023, visual status display. |
| [Battery Power Display](https://steamcommunity.com/sharedfiles/filedetails/?id=3315050989) | Bunstructors | Clean power monitoring display. |
| [Battery Backup Light](https://steamcommunity.com/sharedfiles/filedetails/?id=3569109044) | alliephante | Simple backup power indicator. |
| [3.6 Megawatt Battery](https://steamcommunity.com/sharedfiles/filedetails/?id=3004087671) | walkin_here | Large-scale battery management. |

### Mods (Not IC10)

| Item | Notes |
|------|-------|
| [Mod: Jigawatt Battery](https://steamcommunity.com/sharedfiles/filedetails/?id=1785747072) | Game mod, not IC10 script |

## Key Concepts

- Read `Charge` for current energy stored
- Read `Maximum` for battery capacity
- Calculate percentage: `div rRatio rCharge rMax`
- Use batch operations (`lb`) to sum across battery network
- Control `On` to enable/disable battery output

## Common Logic Types

**Readable**:
- `Charge` - Current energy (joules)
- `Maximum` - Maximum capacity
- `Ratio` - Charge ratio (0-1)
- `PowerActual` - Current power draw/supply

## Display Techniques

Use LEDs or console to show:
- Charge percentage via color (green=full, red=low)
- Numeric display on console screens
- Warning lights for low battery

## Related Local Examples

See `examples/power/` for power-related scripts.

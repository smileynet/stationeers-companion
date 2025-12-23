# Temperature Control Resources Guide

> Last updated: 2025-12-22
> Search terms: temperature, heating, cooling, AC, air conditioner

## Summary

Temperature control is essential for survival and equipment operation. Scripts manage air conditioners, heat exchangers, and wall heaters/coolers to maintain livable conditions.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [[F&S] Room Temperature Control](https://steamcommunity.com/sharedfiles/filedetails/?id=1693735692) | 123 | Complete room temperature management. |
| [Gas Fuel Generator Temperature Regulator](https://steamcommunity.com/sharedfiles/filedetails/?id=2423199247) | CowsAreEvil | Specialized for generator cooling. |
| [Temperature Regulator](https://steamcommunity.com/sharedfiles/filedetails/?id=1565347264) | Maireen | Simple temperature control. |
| [Room Temperature Regulator](https://steamcommunity.com/sharedfiles/filedetails/?id=1519446078) | Dr_Nerdrage | Basic room control. |

## Key Concepts

- Read `Temperature` from Gas Sensor or Pipe Analyzer
- Target range typically 290-300K (17-27°C) for comfort
- Use hysteresis to prevent rapid on/off cycling
- Control `On` for AC units, wall heaters/coolers
- Consider pressure effects on temperature

## Temperature Targets

| Condition | Kelvin | Celsius |
|-----------|--------|---------|
| Freezing | 273 | 0 |
| Comfortable | 293 | 20 |
| Hot | 313 | 40 |
| Suit overheat | 318+ | 45+ |

## Control Techniques

1. **Simple threshold**: Turn on below/above target
2. **Hysteresis**: Use deadband to prevent oscillation
3. **PID**: Proportional control for smooth regulation
4. **Heat exchanger**: Transfer heat to external environment

## Related Local Examples

See `examples/temperature/` for temperature control scripts.

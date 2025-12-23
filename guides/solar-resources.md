# Solar Tracking Resources Guide

> Last updated: 2025-12-22
> Search terms: solar tracking, solar panel, daylight sensor

## Summary

Solar tracking is essential for maximizing power generation. Scripts typically use daylight sensors to calculate sun position and adjust panel orientation for optimal angle throughout the day.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [Solar Tracking 2 Axes Universal](https://steamcommunity.com/sharedfiles/filedetails/?id=2888919844) | Hierøs | 2-axis tracking with 99-100% efficiency claim. Universal design. |
| [Solar Tracking](https://steamcommunity.com/sharedfiles/filedetails/?id=3291077326) | Bunstructors | Clean implementation, well-documented. |
| [Solar Tracking Mars - S05](https://steamcommunity.com/sharedfiles/filedetails/?id=3598079752) | Dan S. | Mars-specific with seasonal adjustments. |
| [Solar Tracking - 24H Clock](https://steamcommunity.com/sharedfiles/filedetails/?id=2301758237) | ItalianBadBoy | Includes day/night cycle detection. |
| [Solar Tracking](https://steamcommunity.com/sharedfiles/filedetails/?id=2371726794) | elru | Basic implementation. |

## Key Concepts

- Use `Daylight Sensor` to read sun position
- Logic types: `SolarAngle`, `Horizontal`, `Vertical`
- Panels should face the sun directly for maximum power
- 2-axis tracking (horizontal + vertical) is more efficient than 1-axis

## Related Local Examples

See `examples/power/` for power-related scripts.

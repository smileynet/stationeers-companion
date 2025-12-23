# Airlock Resources Guide

> Last updated: 2025-12-22
> Search terms: airlock, door cycle, depressurize

## Summary

Airlock automation is critical for maintaining base atmosphere. Scripts typically manage door states, pressure equalization, and safety interlocks to prevent accidental decompression.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [3 Way Airlock](https://steamcommunity.com/sharedfiles/filedetails/?id=3464199348) | CowsAreEvil | Handles 3-door junction airlock. |
| [Auto Bypass Airlock](https://steamcommunity.com/sharedfiles/filedetails/?id=2928534875) | CowsAreEvil | Smart bypass when pressure matches. |
| [Custom Airlock V2](https://steamcommunity.com/sharedfiles/filedetails/?id=2978749569) | CowsAreEvil | Highly configurable airlock controller. |
| [[F&S] Full Auto Airlock](https://steamcommunity.com/sharedfiles/filedetails/?id=2961762121) | 123 | Fully automated cycle with status LEDs. |
| [Adaptive Airlock](https://steamcommunity.com/sharedfiles/filedetails/?id=2194510353) | TryCatch | Adapts to different pressure scenarios. |

## Key Concepts

- Read `Pressure` from sensors inside/outside airlock
- Control `Open` and `Lock` on doors
- Use Active Vents with `Mode` for pressurize/depressurize
- Implement interlocks: never open both doors simultaneously
- State machine pattern is ideal for multi-step cycles

## Typical Cycle

1. Close all doors
2. Pump down (vacuum) or pump up (pressurize)
3. Wait for target pressure
4. Open appropriate door
5. Wait for occupancy change
6. Repeat

## Related Local Examples

See `examples/airlocks/` and `examples/patterns/state-machine-template.ic10`.

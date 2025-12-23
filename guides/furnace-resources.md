# Furnace/Smelting Resources Guide

> Last updated: 2025-12-22
> Search terms: furnace, arc furnace, smelting, auto smelt

## Summary

Furnace automation handles ore smelting, temperature control, and output management. Advanced scripts manage multiple furnaces, stack operations, and recipe selection.

## Steam Workshop Resources

> **Note**: Download with `uv run python -m tools.steam_scraper --id <ID>`

### Recommended

| Item | Author | Description |
|------|--------|-------------|
| [Furnace IC (2023)](https://steamcommunity.com/sharedfiles/filedetails/?id=3046529429) | Barsiel | Updated 2023, modern implementation. |
| [Automatic Advanced Furnace Controller](https://steamcommunity.com/sharedfiles/filedetails/?id=2520700872) | CowsAreEvil | Full automation with input/output management. |
| [Automatic Advanced Furnace Stack Writer](https://steamcommunity.com/sharedfiles/filedetails/?id=2520701196) | CowsAreEvil | Companion script for stack-based data. |
| [FurnaceLibrary v4](https://steamcommunity.com/sharedfiles/filedetails/?id=2849136097) | Elmo | Library approach, latest version. |
| [FurnaceLibrary v3](https://steamcommunity.com/sharedfiles/filedetails/?id=2432832457) | Elmo | Older but widely used version. |

## Key Concepts

- Monitor `Temperature` for smelting thresholds
- Control `Activate` to start/stop smelting
- Use slot operations (`ls`/`ss`) for ore input management
- Read `Setting` for current recipe selection
- Arc Furnace requires specific temperature ranges per alloy

## Common Logic Types

**Readable**:
- `Temperature` - Current furnace temperature
- `Pressure` - Internal pressure (for gas-based)
- `Activate` - Current activation state

**Slot Operations**:
- `ls r0 device slot Quantity` - Items in slot
- `ls r0 device slot PrefabHash` - Item type in slot

## Related Local Examples

See `examples/manufacturing/furnace.ic10` and `examples/manufacturing/arc-furnace-array.ic10`.

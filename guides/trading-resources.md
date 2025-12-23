# Trading Resources Guide

> Last updated: 2025-12-22 (Steam Workshop resources added)
> Search terms: stationeers trading, satellite dish IC10, trader automation

## Summary

Trading in Stationeers requires a Satellite Dish to scan for trader signals, a Landing Pad for shuttles to land, and a Computer with Communications Motherboard. The wiki has the most complete IC10 examples for automated trading, including cargo inspection and dish control scripts.

## Version Compatibility Warning

The trading system has undergone **two major overhauls**. Many older scripts are broken.

### Timeline of Breaking Changes

| Update | Date | Breaking Changes |
|--------|------|------------------|
| **Trading Update III** | Dec 22, 2022 | Added Small/Large dishes, tier system (Close/Medium/Far), interrogation mechanic |
| **Trading Update V** | Mar 5, 2023 | Final refinements to tier system |
| **"Big Changes Coming"** | Mar 17, 2025 | Medium Dish gets 256-byte internal stack, `TraderInstruction` enum, cargo inspection |

### Script Compatibility

| Resource | Status | Notes |
|----------|--------|-------|
| [Wiki Kit (Satellite Dish)](https://stationeers-wiki.com/Kit_(Satellite_Dish)) | **Current** | Updated March 2025, uses stack features |
| [Pastebin RKtQw3Vd](https://pastebin.com/RKtQw3Vd) | **Outdated** | Pre-2022, no tier system or interrogation |
| Steam Workshop Satellite Tracker V2 | **Broken** | Feb 2021, removed from Workshop |
| GitHub repos | **Mixed** | Check for tier/interrogation handling |

### How to Identify Current Scripts

Scripts should handle these features (added Dec 2022):
- **Tier system** - Close/Medium/Far traders with different power needs
- **Interrogation** - `InterrogationProgress` logic type, energy-based contact
- **Power management** - Higher power = faster interrogation for distant tiers

Scripts using these features are post-March 2025:
- Stack operations (`peek`/`poke`) on Medium Satellite Dish
- `TraderInstruction` enum
- Cargo data filtering before landing

## Required Devices

| Device | Purpose | Notes |
|--------|---------|-------|
| Satellite Dish (Small/Medium/Large) | Scans sky for trader signals | Medium has internal stack for cargo data |
| Landing Pad (3x3/5x5/7x7) | Where traders land | Size determines trader tier |
| Landing Pad Data | Control piece for the pad | The IC10 interface point |
| Computer + Communications Motherboard | Required for communication | Connects dish to network |
| Vending Machine (optional) | Automated item trading | For buy/sell automation |

## Best Resources

### 1. Stationeers Wiki - Kit (Satellite Dish) (Best Match)

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Kit_(Satellite_Dish)
**Quality**: 9/10
**Last Updated**: Current with game updates

**What it does**: Complete documentation with 4 IC10 code examples for trading automation.

**IC10 Scripts included**:
1. **Shuttle Cargoes Looking Glasses IC Stack Initializer** - Configures memory addresses for displaying cargo data
2. **Shuttle Cargoes Looking Glasses Runtime** - Reads and displays trader cargo info via LEDs
3. **Trader Filtration IC Housing Code** - Filters cargo by prefab or gas type
4. **Dish Control IC Housing Code** - Autonomous scanning, locking, and interrogation

**Key techniques**:
- Uses Medium Satellite Dish's internal 256-byte stack
- Edge detection for efficient shuttle tracking
- Prefab hash matching for cargo filtering

**Devices required**: Medium Satellite Dish, IC Housing, LEDs for display

---

### 2. Stationeers Wiki - Satellite Tracking (Outdated)

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Satellite_Tracking
**Quality**: 5/10 (code is pre-December 2022)

**What it does**: Explains basic sky scanning concepts. The referenced code is **outdated**.

**Still useful for**:
- Understanding scanning patterns (horizontal sweep with vertical increment)
- Signal strength monitoring concepts (lock at >94%)

**Referenced code**: [Pastebin - Satellite Tracking 5.0](https://pastebin.com/RKtQw3Vd) - **DO NOT USE** (pre-tier system, pre-interrogation mechanic)

**Use instead**: Wiki's [Kit (Satellite Dish)](https://stationeers-wiki.com/Kit_(Satellite_Dish)) page has current, working code.

---

### 3. Stationeers Wiki - Trader Overview

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Trader
**Quality**: 8/10

**What it does**: Explains the complete trading workflow and trader types.

**Key information**:
- Trader tiers (Close/Medium/Far) require different dish sizes
- Basic automation possible with 2 logic readers + 2 logic writers + 2 dials
- Signal strength must reach >94% for communication
- 500W minimum power for Far tier scanning

---

## Alternative Approaches

**Simple (no IC10)**: Use 2 logic reader/writer pairs with dials to manually control horizontal (0-360) and vertical (0-90) dish positioning.

**Full automation**: Use the wiki's Dish Control IC Housing Code for autonomous scanning + the Cargo Looking Glasses scripts for cargo inspection. This is the only current, maintained solution.

**Do NOT use**: Pastebin scripts or pre-2023 Workshop items - they lack tier/interrogation support and will not work correctly.

## Tutorials & Guides

| Title | Source | Description |
|-------|--------|-------------|
| [How to Program IC10 for Novices](https://steamcommunity.com/sharedfiles/filedetails/?id=3288129161) | Steam | Complete IC10 tutorial from basics |
| [Advanced IC10 Programming](https://stationeers-wiki.com/Advanced_IC10_Programming) | Wiki | State machines, indirect registers |
| [IC10 Simulator](https://ic10.dev/) | ic10.dev | Test scripts before deploying |

## GitHub Repositories

These repositories have general IC10 scripts (not trading-specific):

| Repository | Description |
|------------|-------------|
| [jhillacre/stationeers-scripts](https://github.com/jhillacre/stationeers-scripts) | 39 scripts for industrial automation |
| [Zappes/Stationeers](https://github.com/Zappes/Stationeers) | Collection of IC10 scripts |
| [exca/Stationeers-IC10-Automation](https://github.com/exca/Stationeers-IC10-Automation) | Printer/vending automation + Basic compiler |
| [Stationeers-ic/ic10](https://github.com/Stationeers-ic/ic10) | IC10 emulator and development toolkit |

## Steam Workshop Resources

IC10 scripts available on Steam Workshop for satellite dish control and trading automation.

> **Note**: Workshop scripts require SteamCMD to download. Run:
> `uv run python -m tools.steam_scraper --id <ID>`

### Recommended (Current)

| Item | Author | Status | Description |
|------|--------|--------|-------------|
| [Satellite Dish Controller](https://steamcommunity.com/sharedfiles/filedetails/?id=3575668781) | Xyuzhg | **Current** | Uses `TraderInstruction` enum, gradient descent algorithm. Automatically tracks and interrogates traders of all sizes. Works with Medium Satellite Dish stack features. |
| [Satellite Dish Controller](https://steamcommunity.com/sharedfiles/filedetails/?id=2960497565) | CowsAreEvil | **Usable** | Uses `InterrogationProgress` and stack operations (`push`/`peek`). Scans sky for traders and handles interrogation. Includes trader type filtering via dial. |

### Partially Compatible

| Item | Author | Status | Description |
|------|--------|--------|-------------|
| [Trading / Satellite Search v2](https://steamcommunity.com/sharedfiles/filedetails/?id=2876157383) | silentdeth | **Partial** | Basic signal homing script. May need updates for tier system. Good for learning tracking concepts. |

### Outdated (Pre-December 2022)

These scripts predate the Trading Update III and lack tier/interrogation support:

| Item | Author | Notes |
|------|--------|-------|
| [Reliable Satellite Dish Tracker](https://steamcommunity.com/sharedfiles/filedetails/?id=2798776645) | HydrO | Dated 2022, basic signal tracking only |
| [6 Dish Auto Track Trader V2.0](https://steamcommunity.com/sharedfiles/filedetails/?id=1972456301) | Ruges | Multi-dish setup, no tier/interrogation |
| [Satellite Tracker V2](https://steamcommunity.com/sharedfiles/filedetails/?id=2385803105) | CowsAreEvil | Earlier version, superseded by ID 2960497565 |

## Key Logic Types

**Satellite Dish (readable)**:
- `Horizontal` - Current azimuth (0-360°)
- `Vertical` - Current elevation (0-90°)
- `SignalStrength` - -1 (none/moving), 0-1 (signal)
- `SignalID` - ID of detected signal
- `InterrogationProgress` - 0-1 progress of interrogation

**Satellite Dish (writable)**:
- `Horizontal` - Target azimuth
- `Vertical` - Target elevation
- `Activate` - Interrogate or call trader
- `BestContactId` - Select which contact to interact with
- `TargetPadIndex` - Which landing pad to direct trader to

**Landing Pad (writable)**:
- `Activate` - Accept incoming / release landed shuttle

## Notes

- Medium Satellite Dish has a 256-byte internal stack (added in "Big Changes Coming" update) that can be read via IC10 to inspect trader cargo before landing
- Larger dishes can detect further trader tiers but all can interrogate any tier (just takes longer)
- Trading is considered endgame content - recommend mastering state machines first
- See `examples/patterns/state-machine-template.ic10` for state machine basics

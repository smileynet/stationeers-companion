# Plant Growing Reference

Complete guide to growing plants in Stationeers: ideal conditions, compatibility groups, and special areas.

## Quick Reference Table

| Plant | Temp Range | Ideal | Light | Gas In | Gas Out | Growth Time | Yield |
|-------|------------|-------|-------|--------|---------|-------------|-------|
| Wheat | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 5 + seed |
| Corn | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 2 + seed |
| Potato | 0-50°C | 20-30°C | Yes | CO2 | O2 | ~51min | 3 + seed |
| Soybean | 0-50°C | 20-30°C | Yes | CO2 | O2 | ~54min | 2 + seed |
| Rice | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 2 + seed |
| Tomato | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 2 + seed |
| Pumpkin | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 2 + seed |
| Sugarcane | 0-50°C | 20-30°C | Yes | CO2 | O2 | ~53min | 2 + seed |
| **Cocoa** | 0-50°C | **30-40°C** | Yes | CO2 | O2 | Tree+fruit | 2 + seed |
| Fern | 0-50°C | 20-30°C | Yes | CO2 | O2 | ~54min | 2 + seed |
| Switch Grass | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 2 + seed |
| Flower | 0-50°C | 20-30°C | Yes | CO2 | O2 | 1h | 2 + seed |
| **Darga Fern** | 0-50°C | 20-30°C | Yes | CO2 (7x) | O2 (7x) | 12min | 2 |
| **Tropical Lily** | 0-50°C | 20-30°C | Yes | CO2 (1.66x) | O2 (1.66x) | 12min | 2 |
| **Peace Lily** | 0-50°C | 20-30°C | Yes | CO2 (1.66x) | O2 (1.66x) | 12min | 2 |
| **Mushroom** | 0-50°C | 20-30°C | **NO** | O2 | CO2 | 1h | 3 + seed |
| **Alien Mushroom** | 0-50°C | 20-30°C | Optional | N2O | N2, O2 | 3min | 2 |
| **Winterspawn** | -26-65°C | 14-24°C | Yes | N2, H2O | O2, Volatiles | - | Cooling |
| **Hades Flower** | 0-65°C | 4-20°C | Yes | Volatiles, O2 | Pollutant | - | Heating |

## Universal Requirements

All plants require:

| Parameter | Minimum | Ideal | Maximum | Notes |
|-----------|---------|-------|---------|-------|
| Pressure | 25 kPa | 50-100 kPa | 200 kPa | Plants die outside range |
| Temperature | 0°C (273K) | 20-30°C | 50°C (323K) | 5 min death timer outside |
| Water Temp | 5°C | 15-45°C | 60°C | Via hydroponics piping |
| Pollutants | - | 0 | <1 kPa | Partial pressure limit |
| Volatiles | - | 0 | <1 kPa | Partial pressure limit |

### Standard Gas Exchange
- Common plants: 0.072 mol/min CO2 consumed, O2 produced
- Water consumption: ~0.043 mol/hour

## Compatibility Groups

### Group 1: Standard Greenhouse (11 plants)

**Plants:** Wheat, Corn, Potato, Soybean, Rice, Tomato, Pumpkin, Sugarcane, Fern, Switch Grass, Flower

**All can grow together with:**
- Temperature: 20-30°C
- Pressure: 50-100 kPa
- Atmosphere: CO2 present (1-5%), produces O2
- Light: Sunlight or Grow Lights required
- Darkness: Most need some darkness per day (check Plant Genetic Analyzer)

**Recommended setup:**
- Sealed room with windows OR grow lights
- CO2 injection system (plants consume CO2)
- O2 extraction (or vent to base)
- Temperature control (heater/cooler)
- Water piping at 20-40°C

### Group 1b: Cocoa (Higher Temperature)

**Plant:** Cocoa

**Requires warmer conditions:**
- Optimal: **30-40°C** (10°C higher than standard crops)
- Below 30°C: Grows very slowly
- Below 20°C: Dies

**Growing with other plants:**
- Set greenhouse to exactly **30°C** - this is the max optimal for standard plants AND the min optimal for cocoa
- All plants will grow at maximum speed at 30°C
- Alternatively, dedicate a warmer section for cocoa

**Note:** Cocoa grows as a tree first, then produces fruit periodically (unlike single-harvest crops).

### Group 2: High-Exchange Plants (3 plants)

**Plants:** Darga Fern, Tropical Lily, Peace Lily

**Can be added to standard greenhouse but:**
- Darga Fern exchanges gas **7x faster** (0.51 mol/min)
- Lilies exchange **66% more** (0.24 mol/min)
- Will rapidly deplete CO2 and flood O2
- Need enhanced CO2 supply system

**Tip:** Use 1-2 Darga Ferns to balance a mushroom room's CO2 output.

### Group 3: Mushroom Room (SEPARATE AREA)

**Plant:** Mushroom

**Requires dedicated dark room because:**
- **Damaged by sunlight and grow lights**
- Safe with: suit lights, wall lights, portable lights
- Consumes O2, produces CO2 (opposite of other plants)
- Same temp/pressure as standard (20-30°C, 50-100 kPa)

**Recommended setup:**
- Sealed room with NO windows
- No grow lights (use wall lights for visibility)
- O2 injection system (mushrooms consume O2)
- CO2 extraction (or vent to standard greenhouse)
- Can balance with standard plants via connected atmosphere

### Group 4: Alien Mushroom Chamber (SPECIAL ATMOSPHERE)

**Plant:** Alien Mushroom

**Requires N2O (nitrous oxide) atmosphere:**
- Consumes: N2O
- Produces: N2 + O2
- Can grow without light
- Very fast: 3 minutes to harvest

**Recommended setup:**
- Sealed room with N2O atmosphere
- Light optional (doesn't need, doesn't hurt)
- Extract N2/O2 output gases

### Group 5: Thermogenic Plants (SPECIAL PURPOSE)

These plants generate heating or cooling effects.

#### Winterspawn (Cooling Plant)

**Two strains:**
- Alpha: 90W cooling, works 0-40°C
- Beta: 150W cooling, optimal 14-24°C (narrower range)

**Requirements:**
- Temperature: -26°C to 65°C
- Consumes: N2 (nitrogen) + H2O (0.4 mol/hour)
- Produces: O2 + Volatiles + Cooling effect
- Stops cooling if N2 removed (but doesn't die)

**Use for:** Passive cooling in hot environments

#### Hades Flower (Heating Plant)

**Two strains:**
- Alpha: Less efficient
- Beta: More efficient heating

**Requirements:**
- Temperature: 0°C to 65°C (optimal 4-20°C)
- Consumes: Volatiles + O2
- Produces: Pollutant + Heat

**Use for:** Passive heating, but produces pollutant waste

## Special Area Setups

### Optimal Multi-Greenhouse Layout

```
┌─────────────────────────┐
│   MAIN GREENHOUSE       │
│   (11 standard + cocoa) │
│   30°C, CO2 in, O2 out  │
│   Grow lights + windows │
└───────────┬─────────────┘
            │ CO2 vent
┌───────────▼─────────────┐
│   MUSHROOM ROOM         │
│   (Dark, wall lights)   │
│   O2 in, CO2 out        │
│   No windows/grow lights│
└─────────────────────────┘
```

### Symbiotic Balance
- Mushrooms produce CO2 → pipes to greenhouse
- Standard plants produce O2 → pipes to mushroom room
- Net result: self-sustaining atmosphere

### Atmosphere Targets by Room

| Room | O2 | CO2 | N2 | Temperature |
|------|-----|-----|-----|-------------|
| Main Greenhouse | ~20% | 2-5% | Balance | 30°C* |
| Mushroom Room | 10-20% | Any | Balance | 20-30°C |
| Alien Chamber | Product | - | Product | 20-30°C |

*30°C is the sweet spot: max optimal for standard plants AND min optimal for cocoa.

## IC10 Automation

See `examples/growing/` for automation scripts:
- `harvie.ic10` - Auto-harvest controller
- `greenhouse_master.ic10` - Full atmosphere control
- `greenhouse_fill.ic10` - Initial atmosphere setup

Key logic types for plants:
- `Growth` (slot read) - Current growth percentage
- `Mature` (slot read) - Ready for harvest (0/1)
- `Seeding` - Needs seed planted

## Sources

- [Stationeers Wiki - Farming Guide](https://stationeers-wiki.com/Guide_(Farming))
- [Stationeers Wiki - Hydroponics](https://stationeers-wiki.com/Template:Hydroponics)
- [Stationeers Wiki - Thermogenic Plants](https://stationeers-wiki.com/Thermogenic_plants)
- [Stationeers Wiki - Cocoa](https://stationeers-wiki.com/Cocoa)
- [Steam Discussion - Greenhouse Requirements](https://steamcommunity.com/app/544550/discussions/0/1700542332338217080/)
- [Steam Discussion - Cocoa Plants](https://steamcommunity.com/app/544550/discussions/0/4334229587334553273/)
- Individual plant wiki pages (Wheat, Corn, Potato, Soybean, Tomato, Mushroom, etc.)

# Farming Hab Layout Guide

> Plan your greenhouse rooms, manage plant compatibility, and adapt to different planets.

## Overview

Farming in Stationeers requires dedicated sealed rooms with controlled atmospheres. Different plants have different needs, so planning your layout in advance saves major reconstruction later.

**Key Principles:**
- Room-based design - separate incompatible plants
- Input/output planning - gas flows, logistics
- Modular expansion - plan for growth
- Planet adaptation - each world has unique challenges

---

## Plant Compatibility Groups

Not all plants can share the same room. Plan your layout around these groups:

### Group 1: Standard Greenhouse (11 plants)

**Plants:** Wheat, Corn, Potato, Soybean, Rice, Tomato, Pumpkin, Sugarcane, Fern, Switch Grass, Flower

| Requirement | Value |
|-------------|-------|
| Temperature | 20-30°C |
| Pressure | 50-100 kPa |
| Gas | CO2 in → O2 out |
| Light | Required (sun or grow lights) |
| Darkness | ~20 min/day (check analyzer) |

All these plants can grow together in one room.

### Group 1b: Cocoa (Higher Temperature)

**Plant:** Cocoa

| Requirement | Value |
|-------------|-------|
| Temperature | **30-40°C** (warmer than standard) |
| Other | Same as Group 1 |

**Compatibility:** Set greenhouse to exactly **30°C** - this is the max optimal for standard plants AND min optimal for cocoa. All plants grow at max speed.

### Group 2: High-Exchange Plants

**Plants:** Darga Fern, Tropical Lily, Peace Lily

| Plant | Gas Exchange Rate |
|-------|-------------------|
| Darga Fern | **7x standard** (0.51 mol/min) |
| Lilies | **1.66x standard** (0.24 mol/min) |

**Warning:** These rapidly deplete CO2. Need enhanced supply system or grow separately.

**Tip:** 1-2 Darga Ferns can balance a mushroom room's CO2 output.

### Group 3: Mushrooms (SEPARATE DARK ROOM)

**Plant:** Mushroom

| Requirement | Value |
|-------------|-------|
| Temperature | 20-30°C |
| Pressure | 50-100 kPa |
| Gas | **O2 in → CO2 out** (opposite!) |
| Light | **NONE** (damaged by sun/grow lights) |

**Safe lighting:** Wall lights, suit lights, portable lights only.

### Group 4: Alien Mushroom (SPECIAL ATMOSPHERE)

**Plant:** Alien Mushroom

| Requirement | Value |
|-------------|-------|
| Atmosphere | **N2O (nitrous oxide)** |
| Gas | N2O in → N2 + O2 out |
| Light | Optional |
| Growth Time | **3 minutes** (very fast) |

Requires completely separate sealed room with N2O atmosphere.

### Group 5: Thermogenic Plants (UTILITY)

**Plants:** Winterspawn (cooling), Hades Flower (heating)

| Plant | Function | Consumes | Produces |
|-------|----------|----------|----------|
| Winterspawn | 90-150W cooling | N2 + H2O | O2 + Volatiles |
| Hades Flower | Heating | Volatiles + O2 | Pollutant |

Special purpose - use for passive temperature control.

---

## Room Types Reference

| Room | Plants | Key Requirements | Notes |
|------|--------|------------------|-------|
| Main Greenhouse | Standard (11) | CO2, 20-30°C, light | Windows or grow lights |
| Cocoa Section | Cocoa | 30-40°C | Can be subsection at 30°C |
| Mushroom Room | Mushrooms | O2, dark, 20-30°C | Wall lights only |
| Alien Chamber | Alien Mushroom | N2O atmosphere | Completely sealed |
| Thermogenic | Winterspawn/Hades | Per plant | Utility purpose |
| Genetics Lab | Any (testing) | Standard | Near greenhouses |

---

## Starter Layout (Early Game)

A simple 3x3 greenhouse gets you growing quickly.

```
┌─────────────────────────────────┐
│         STARTER GREENHOUSE      │
│                                 │
│   ┌─────┐ ┌─────┐ ┌─────┐      │
│   │Tray │ │Tray │ │Tray │      │
│   │+H   │ │+H   │ │+H   │      │  3-9 trays with Harvies
│   └─────┘ └─────┘ └─────┘      │
│                                 │
│   [Gas Sensor] [Temp Display]   │  Basic monitoring
│   [Heater] or [Cooler]          │  Temperature control
│                                 │
│ ← Airlock                       │
└─────────────────────────────────┘
        │
   [Water pipe]
```

**Build checklist:**
- [ ] Sealed room (welded frames, no leaks)
- [ ] Glass windows or grow lights
- [ ] Water pipe connection
- [ ] Heater and/or cooler
- [ ] Gas sensor for monitoring
- [ ] Some CO2 in atmosphere

**Early CO2 sources:**
- Breathe in room (slow)
- Burn organics
- Mars: use outside atmosphere
- Import from tank

---

## Mid-Game Expansion

Add specialized rooms connected by gas piping.

```
┌─────────────────────────┬────────────────────┐
│    MAIN GREENHOUSE      │   MUSHROOM ROOM    │
│                         │                    │
│  [T][T][T]  [T][T][T]   │   [T][T]  [T][T]   │
│  [H][H][H]  [H][H][H]   │   [H][H]  [H][H]   │
│                         │                    │
│  CO2 in ←───────────────┼───── CO2 out ──┐   │
│  O2 out ────────────────┼───→ O2 in      │   │
│                         │                    │
│  30°C                   │   25°C (dark)      │
│  Grow lights            │   Wall lights      │
├─────────────────────────┴────────────────────┤
│            PROCESSING AREA                   │
│                                              │
│   [Composter] ─→ [Chute] ─→ [Storage]       │
│                                              │
│   [Fertilizer Storage]  [Seed Storage]       │
└──────────────────────────────────────────────┘
```

**Symbiotic gas exchange:**
- Standard plants: consume CO2, produce O2
- Mushrooms: consume O2, produce CO2
- Connect rooms with vents/pipes for self-sustaining atmosphere

**Atmosphere targets:**

| Room | O2 | CO2 | N2 | Temp |
|------|-----|-----|-----|------|
| Main Greenhouse | ~20% | 2-5% | Balance | 30°C |
| Mushroom Room | 10-20% | Any | Balance | 25°C |

---

## Advanced Layout (Late Game)

Separate production from breeding, add full logistics.

```
┌──────────────────┬──────────────────┬──────────────────┐
│   PRODUCTION     │    BREEDING      │   GENETICS LAB   │
│   GREENHOUSE     │   GREENHOUSE     │                  │
│                  │                  │  [Analyzer]      │
│  [T][T][T][T]    │  [T][T][T]       │  [Stabilizer]    │
│  [T][T][T][T]    │  [H][H][H]       │  [Splicer]       │
│  [H][H][H][H]    │                  │                  │
│  [H][H][H][H]    │  Experimental    │  [Sample Store]  │
│                  │  varieties       │                  │
│  Batch harvie    │  Semi-auto       │  Manual ops      │
│  Full auto       │                  │                  │
├──────────────────┴──────────────────┴──────────────────┤
│              SPECIALIZED ROOMS                          │
│                                                         │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌────────────────┐ │
│ │MUSHROOM │ │ COCOA   │ │ ALIEN   │ │  THERMOGENIC   │ │
│ │ (dark)  │ │ (warm)  │ │ (N2O)   │ │  (utility)     │ │
│ └─────────┘ └─────────┘ └─────────┘ └────────────────┘ │
├─────────────────────────────────────────────────────────┤
│              LOGISTICS HUB                              │
│                                                         │
│  [Chutes]  [Sorters]  [Food Storage]  [Seed Storage]   │
│                                                         │
│   Output sorting by crop type                           │
│   Seed recirculation to harvies                         │
└─────────────────────────────────────────────────────────┘
```

**Production vs Breeding:**
- **Production**: Mass output, full automation, stable varieties
- **Breeding**: Experimentation, gene manipulation, new varieties

---

## Planet-Specific Layouts

### Moon

**Challenges:**
- No atmosphere - all gas must be created/imported
- Good sunlight - solar power works well
- No free CO2

```
┌──────────────────────────────────────────┐
│          MOON GREENHOUSE                  │
│                                           │
│    ══════════════════════════            │  ← Glass ceiling
│         (sunlight through)                │
│                                           │
│    [T][T][T]  [T][T][T]                  │
│    [H][H][H]  [H][H][H]                  │
│                                           │
│    [Arc Furnace] ──→ CO2 capture         │  Burn organics for CO2
│    [Coal storage]                         │
│                                           │
│  ← Simple airlock (no Mars storms)        │
└──────────────────────────────────────────┘
```

**Tips:**
- Burn coal/organics to generate CO2
- Glass ceiling for free lighting
- Simpler airlock (no storms)
- Conserve all gases carefully

### Mars

**Challenges:**
- Cold nights (need heating)
- Free CO2 daytime (20°C Martian air)
- Storms after day 7 can damage solar panels
- Requires advanced airlock

```
┌──────────────────────────────────────────┐
│          MARS GREENHOUSE                  │
│                                           │
│    [T][T][T]  [T][T][T]                  │
│    [H][H][H]  [H][H][H]                  │
│                                           │
│    [Heater]  [Gas Sensor]  [Temp Sensor] │
│                                           │
│  ← Advanced Airlock ──┐                   │
│                       │                   │
│                  Day cycle:               │
│                  Open → fill warm air     │
│                  Night → seal             │
└──────────────────────────────────────────┘
```

**Day/Night Cycle Automation:**
```ic10
# Simple Mars greenhouse fill
l r0 db SolarAngle    # Check sun position
sgt r1 r0 0           # Day if > 0
s Vent On r1          # Open vent during day
```

**Tips:**
- Open airlock during day to fill with ~20°C Mars atmosphere
- Seal at night, maintain heat
- CO2 is free - just use outside air
- Watch for storms (day 7+)

### Europa

**Challenges:**
- **Extremely cold** (-150°C)
- Very weak sunlight
- Batteries drain fast
- Solar panels nearly useless

```
┌────────────────────────────────────────────────┐
│            EUROPA GREENHOUSE                    │
│                                                 │
│    ████████████████████████████                │  ← Heavy insulation
│    █                          █                │    (no windows!)
│    █  [T][T][T]  [T][T][T]    █                │
│    █  [H][H][H]  [H][H][H]    █                │
│    █                          █                │
│    █  [Grow Light][Grow Light]█                │  Artificial light only
│    █  [Grow Light][Grow Light]█                │
│    █                          █                │
│    █  [Heater][Heater][Heater]█                │  MASSIVE heating
│    █  [Battery Bank]          █                │
│    █                          █                │
│    ████████████████████████████                │
└────────────────────────────────────────────────┘
```

**Power Priority:**
1. Heating (survival)
2. Grow lights (food)
3. Harvies (automation)

**Tips:**
- NO windows - insulation is critical
- Grow lights required (sun too weak)
- Multiple heaters needed
- Alternative power (Stirling, fuel gen) - solar insufficient
- Breed cold-tolerant plants

### Vulcan

**Challenges:**
- **Extremely hot** - need cooling
- **No ice** - water is precious
- **No starting seeds** - must trade or scavenge
- No starting farming kit

```
┌────────────────────────────────────────────────┐
│            VULCAN GREENHOUSE                    │
│                                                 │
│    [Water Reclaimer] ←──── Priority #1         │
│                                                 │
│    [T][T][T]  [T][T][T]                        │
│    [H][H][H]  [H][H][H]                        │
│                                                 │
│    [AC Unit] [AC Unit] [Cooler]                │  Cooling system
│                                                 │
│    [Trader Landing Pad] ←── Seeds from here    │
│                                                 │
│    [Organics Printer] ←── Food until farm      │
│                          is operational         │
└────────────────────────────────────────────────┘
```

**Progression:**
1. Set up power (solar works great here)
2. Build Organics Printer for initial food
3. Trade for seeds OR scavenge ruins
4. Build water reclamation system
5. THEN build greenhouse with cooling

**Tips:**
- Water is your limiting factor
- Breed water-efficient plants
- Cooling more important than heating
- Organics Printer bridges the gap until farm

---

## Automation Integration

### Environmental Control

Link to `examples/growing/greenhouse_master.ic10` for full atmosphere control:
- CO2/O2 monitoring
- Temperature regulation
- Pressure maintenance
- Alarm systems

### Harvie Systems

See `guides/harvie-seed-fertilizer-automation.md` for:
- Basic 3-harvie controllers
- Batch operations (500+ harvies)
- Chute networks and sorting
- Seed recirculation

### Suggested Progression

| Stage | Automation Level |
|-------|------------------|
| Early | Manual + gas sensor display |
| Mid | IC10 environmental control |
| Late | Batch harvies + full logistics |

---

## Common Mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Unsealed room | Atmosphere leaks | Check every frame is welded |
| Mixing mushrooms with other plants | Either mushrooms or others die | Separate dark room |
| No CO2 supply | Plants starve | Burn organics, pipe from mushrooms, use outside air |
| Constant light | Plants die (no darkness) | Day/night cycle or check tolerance |
| Mars: no storm prep | Panels blown away | Bolt everything, plan for day 7+ |
| Europa: windows | Freezing, inefficient | Full insulation, grow lights |
| Vulcan: no water plan | Farm fails | Water reclamation first |

---

## Sources

**Local References:**
- `knowledge/farming/plants.md` - Plant requirements
- `guides/harvie-seed-fertilizer-automation.md` - Harvie guide
- `examples/growing/` - Automation scripts

**External:**
- [Stationeers Wiki - Farming Guide](https://stationeers-wiki.com/Guide_(Farming))
- [Stationeers Wiki - Worlds](https://stationeers-wiki.com/Worlds)
- [Steam - Greenhouse Requirements](https://steamcommunity.com/app/544550/discussions/0/1700542332338217080/)
- [Steam - Surviving Every Planet](https://steamcommunity.com/sharedfiles/filedetails/?id=3394899504)

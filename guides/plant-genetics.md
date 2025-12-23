# Plant Genetics Guide

> Breed better plants through stress adaptation, directed mutation, and gene splicing.

## Overview

Every plant in Stationeers has genes that control its growth, resource needs, and environmental tolerances. Through breeding and genetic manipulation, you can create plants adapted to your specific conditions.

**Key Concepts:**
- Genes pass from parent plant to offspring (seeds/fruit)
- Environmental stress causes adaptive mutations
- Stability controls mutation rate
- Splicing transfers specific genes between plants

---

## Equipment Reference

Four devices for genetic work:

| Device | Function | Power | Time | Notes |
|--------|----------|-------|------|-------|
| **Plant Sampler** | Collect genetic samples | None | Instant | Use on growing plant |
| **Plant Genetic Analyzer** | View gene values | Low | Processing | Reveals all 18 genes |
| **Plant Genetic Stabilizer** | Control mutation rate | 100W | 1-2 min | Stabilize or destabilize |
| **Plant Genetic Splicer** | Transfer genes | 100W | ~1 min | Destroys source plant |

### Using the Analyzer

1. Sample a plant with the Plant Sampler
2. Insert sample into Analyzer
3. Click the search button to view genetics
4. Gene display shows:
   - Orange bar: current value
   - Blue range: ideal growth values
   - White: maximum possible values

---

## Plant Genes

Plants have **18 genes** controlling their behavior:

### Growth Genes

| Gene | Effect | Notes |
|------|--------|-------|
| **Growth Speed Multiplier** | Time to mature | Higher = faster growth |

### Light/Dark Cycle

| Gene | Effect | Default |
|------|--------|---------|
| **Light Per Day** | Required light time | ~20 minutes |
| **Dark Per Day** | Required darkness time | ~20 minutes |
| **Light Tolerance** | Time before light damage | Hours |
| **Darkness Tolerance** | Time before dark damage | Hours |

Plants left in permanent light or darkness eventually die.

### Resource Usage

| Gene | Effect | Notes |
|------|--------|-------|
| **Water Usage** | Water consumption rate | Lower = more efficient |
| **Drought Tolerance** | Time surviving without water | Higher = hardier |
| **Gas Production** | CO2/O2 exchange rate | Varies by plant type |

### Pressure Tolerance

| Gene | Effect |
|------|--------|
| **Low Pressure Resistance** | Min survivable pressure |
| **Low Pressure Tolerance** | Time at low pressure before damage |
| **High Pressure Resistance** | Max survivable pressure |
| **High Pressure Tolerance** | Time at high pressure before damage |

### Temperature Tolerance

| Gene | Effect |
|------|--------|
| **Low Temp Resistance** | Min survivable temperature |
| **Low Temp Tolerance** | Time at low temp before damage |
| **High Temp Resistance** | Max survivable temperature |
| **High Temp Tolerance** | Time at high temp before damage |

### Atmosphere Tolerance

| Gene | Effect |
|------|--------|
| **Suffocation Tolerance** | Time surviving gas deprivation |
| **Undesired Gas Resistance** | Max pollutant/volatile level |
| **Undesired Gas Tolerance** | Time surviving toxic atmosphere |

---

## Genetics Lab Setup

Place genetics equipment near your breeding area:

```
┌───────────────────────────────────────────────┐
│               GENETICS LAB                     │
│                                                │
│   ┌──────────┐    ┌─────────────┐             │
│   │ Analyzer │    │ Stabilizer  │             │
│   │          │    │             │             │
│   └──────────┘    │ [Stabilize] │             │
│        │          │[Destabilize]│             │
│        │          └─────────────┘             │
│        │                 │                     │
│   ┌────▼────┐      ┌─────▼─────┐              │
│   │ Sample  │      │  Splicer  │              │
│   │ Storage │      │ [L]  [R]  │              │
│   └─────────┘      └───────────┘              │
│                                                │
│   ┌────────────────────────────────────────┐  │
│   │          BREEDING TRAYS                 │  │
│   │                                         │  │
│   │  [Tray+Harvie] [Tray+Harvie] [Tray+H]  │  │
│   │                                         │  │
│   │  Separate from production farm          │  │
│   │  For experimentation and selection      │  │
│   └────────────────────────────────────────┘  │
└───────────────────────────────────────────────┘
```

**Keep breeding separate from production:**
- Experimental plants in dedicated trays
- Production farm uses stable, proven varieties
- Transfer improved seeds after verification

---

## Stability System

Each gene has a **stability value** from -1 to +1:

| Stability | Mutation Rate | Description |
|-----------|---------------|-------------|
| +1.0 | Very low | Gene rarely changes |
| 0 | Normal | Standard mutation rate |
| -1.0 | Very high | Gene changes frequently |

**Key behaviors:**
- Growing a generation moves stability toward 0
- Stabilizer "Stabilize" mode: all genes +50% toward +1
- Stabilizer "Destabilize" mode: all genes -10%, target gene -50%

---

## Breeding Methods

### Method 1: Stress Adaptation (Natural)

Plants adapt to their environment. Stressed plants pass adaptive genes to offspring.

**Workflow:**
1. Grow plant under target stress (low water, temp extremes, etc.)
2. Plant survives but grows slowly
3. Harvest seeds (offspring have adapted genes)
4. Repeat for multiple generations
5. Each generation adapts further

**Example: Breeding drought-tolerant wheat**
1. Grow wheat with minimal water
2. Plant survives, produces seeds
3. Grow those seeds with minimal water
4. Repeat 3-5 generations
5. Result: wheat with lower water usage gene

**Pros:** Simple, no equipment needed
**Cons:** Slow, affects all genes, unpredictable

### Method 2: Directed Mutation (Stabilizer)

Target specific genes for rapid mutation while keeping others stable.

**Workflow:**
1. Use Stabilizer "Destabilize" mode, select target gene
   - All genes: -10% stability
   - Target gene: -50% stability
2. Grow multiple generations (target mutates fast)
3. Use Analyzer to check results each generation
4. When target reaches desired value:
5. Use Stabilizer "Stabilize" mode to lock all genes (+50%)
6. Grow one generation to verify stability

**Example: Breeding fast-growing tomatoes**
1. Destabilize "Growth Speed Multiplier" gene
2. Grow 3-5 generations, check each with Analyzer
3. Select best offspring each generation
4. When speed is high enough, stabilize all genes
5. Final variety grows faster than baseline

**Pros:** Targeted, faster than natural
**Cons:** Requires equipment, some trial and error

### Method 3: Gene Splicing (Splicer)

Transfer a specific gene from one plant to another.

**Workflow:**
1. Identify donor plant with excellent target gene
2. Identify recipient plant you want to improve
3. Place donor in Splicer **left slot** (source)
4. Place recipient in **right slot** (target)
5. Use arrows to select gene to transfer
6. Close door, press activate
7. **Donor is destroyed**, recipient gains gene

**Example: Transfer growth speed to wheat**
1. Find tomato with high Growth Speed (or breed one)
2. Place tomato in left slot
3. Place wheat in right slot
4. Select "Growth Speed Multiplier"
5. Activate - tomato destroyed, wheat now has fast growth

**Pros:** Instant, precise
**Cons:** Destroys donor, need good source plant first

---

## Breeding Workflow Summary

```
┌─────────────────────────────────────────────────────────┐
│                    BREEDING PROCESS                      │
│                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │ SAMPLE   │───▶│ ANALYZE  │───▶│ DECIDE   │          │
│  │ Plant    │    │ Genes    │    │ Method   │          │
│  └──────────┘    └──────────┘    └────┬─────┘          │
│                                       │                  │
│         ┌───────────────────────────────┼──────────┐     │
│         │                    │          │          │     │
│         ▼                    ▼          ▼          ▼     │
│  ┌──────────┐    ┌──────────────┐  ┌─────────┐         │
│  │  STRESS  │    │ DESTABILIZE  │  │ SPLICE  │         │
│  │ Natural  │    │  + Breed     │  │  Gene   │         │
│  └────┬─────┘    └──────┬───────┘  └────┬────┘         │
│       │                 │               │               │
│       ▼                 ▼               ▼               │
│  ┌──────────────────────────────────────────┐          │
│  │              GROW GENERATION              │          │
│  └──────────────────────┬───────────────────┘          │
│                         │                               │
│                         ▼                               │
│  ┌──────────────────────────────────────────┐          │
│  │   ANALYZE OFFSPRING - Keep best seeds    │──┐       │
│  └──────────────────────────────────────────┘  │       │
│                         │                       │       │
│                         ▼                       │       │
│                  Target reached?                │       │
│                    │      │                     │       │
│                   YES     NO ───────────────────┘       │
│                    │                                    │
│                    ▼                                    │
│  ┌──────────────────────────────────────────┐          │
│  │          STABILIZE FINAL VARIETY          │          │
│  └──────────────────────────────────────────┘          │
│                         │                               │
│                         ▼                               │
│  ┌──────────────────────────────────────────┐          │
│  │      TRANSFER TO PRODUCTION FARM          │          │
│  └──────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────┘
```

---

## Planet-Specific Breeding Goals

Different planets demand different adaptations:

### Moon

| Priority Gene | Why |
|---------------|-----|
| Gas Production ↓ | Conserve precious CO2 |
| Water Usage ↓ | Water is valuable |
| Growth Speed ↑ | Faster harvest = less resource use |

CO2 is scarce on the Moon - breed plants that use less.

### Mars

| Priority Gene | Why |
|---------------|-----|
| Low Temp Resistance | Survive cold nights (-60°C) |
| Low Temp Tolerance | More time before damage |
| Drought Tolerance | Survive water system issues |

Night temperatures are the killer - breed cold-hardy plants.

### Europa

| Priority Gene | Why |
|---------------|-----|
| Low Temp Resistance | Extreme cold (-150°C) |
| Low Temp Tolerance | Extended cold survival |
| Light Tolerance ↑ | Grow lights may run 24/7 |
| Darkness Tolerance ↑ | Power outages = darkness |

Everything is about surviving the cold and power limitations.

### Vulcan

| Priority Gene | Why |
|---------------|-----|
| Water Usage ↓ | No ice, water is precious |
| High Temp Resistance | Hot environment |
| Drought Tolerance ↑ | Water system failures |

Water efficiency is survival on Vulcan.

### Summary Table

| Planet | Primary Goal | Secondary |
|--------|--------------|-----------|
| Moon | Low gas production | Low water usage |
| Mars | Cold resistance | Cold tolerance |
| Europa | Extreme cold resistance | Light tolerance |
| Vulcan | Low water usage | Heat resistance |

---

## Tips & Best Practices

### Organization
- Label seed bags: "Wheat G3 FastGrow" (generation 3, fast growth)
- Keep breeding log (which plants, what conditions)
- Separate test batches by generation

### Efficiency
- Check Stationpedia (F1) for baseline plant stats
- Start breeding early - takes multiple generations
- Keep "backup" seeds of good varieties
- Don't over-breed - mutations can go backward

### Stabilizer Use
- Stabilize (1 min) moves all genes toward +1
- Destabilize (2 min) selectively targets one gene
- Use destabilize first, stabilize when satisfied

### Splicing
- Source plant is destroyed - make seeds first
- Can only splice same plant types
- Good for transferring single excellent gene
- Build up a "gene library" of donor plants

### General
- Genetics is trial and error - expect failures
- Small improvements compound over generations
- Not everything can be IC10 automated (manual process)
- Check analyzer regularly during breeding

---

## Limitations

Current game mechanics mean:
- **No IC10 automation** of genetics devices
- All genetic work is manual
- Multiple generations needed for significant changes
- Trial and error required

---

## Quick Reference

### Stabilizer Modes

| Mode | Effect | Time |
|------|--------|------|
| Stabilize | All genes +50% stability | 1 min |
| Destabilize | All genes -10%, target -50% | 2 min |

### Stability Values

| Value | Meaning |
|-------|---------|
| +1.0 | Nearly frozen (rare mutation) |
| 0 | Normal mutation rate |
| -1.0 | Rapidly mutating |

### Gene Categories

| Category | Genes |
|----------|-------|
| Growth | Growth Speed Multiplier |
| Cycles | Light/Dark Per Day, Light/Darkness Tolerance |
| Resources | Water Usage, Drought Tolerance, Gas Production |
| Pressure | Low/High Resistance + Tolerance |
| Temperature | Low/High Resistance + Tolerance |
| Atmosphere | Suffocation, Undesired Gas Resistance/Tolerance |

---

## Sources

**External:**
- [Stationeers Wiki - Genetics](https://stationeers-wiki.com/Genetics)
- [Stationeers Wiki - Plant Genetic Analyzer](https://stationeers-wiki.com/Plant_Genetic_Analyzer)
- [Stationeers Wiki - Plant Genetic Stabilizer](https://stationeers-wiki.com/Plant_Genetic_Stabilizer)
- [Stationeers Wiki - Plant Genetic Splicer](https://stationeers-wiki.com/Plant_Genetic_Splicer)
- [Steam - Farming Update III: Genetic Manipulation](https://steamcommunity.com/games/544550/announcements/detail/3531414035623977144)
- [Steam - Reliable Genetic Engineering Methods](https://steamcommunity.com/app/544550/discussions/0/4334229775335391081/)

**Local:**
- `knowledge/farming/plants.md` - Plant baseline stats
- `guides/farming-hab-layout.md` - Where to put your genetics lab

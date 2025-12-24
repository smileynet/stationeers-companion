# Mining Processing Chains

Complete reference for ore processing, smelting recipes, and material yields in Stationeers.

---

## Table of Contents

1. [Overview](#overview)
2. [Basic Smelting](#basic-smelting)
3. [Alloy Recipes](#alloy-recipes)
4. [Processing Yields](#processing-yields)
5. [Processing Strategies](#processing-strategies)
6. [Advanced Processing](#advanced-processing)

---

## Overview

### Processing Chain

```
Ore → Sorting → Smelting → Ingot → Crafting
```

**Stages:**
1. **Extraction:** Mining drills, excavators, deep miners
2. **Sorting:** Hash-based sorters, stackers
3. **Smelting:** Arc furnace, regular furnace
4. **Storage:** Ingot stackers, organized storage
5. **Usage:** Crafting, trading, construction

### Equipment

| Device | Purpose | Notes |
|--------|---------|-------|
| **Mining Drill** | Extract ore | Place on deposit |
| **Sorter** | Separate ores by type | Hash-based |
| **Arc Furnace** | Fast smelting | Requires power |
| **Furnace** | Slow smelting | No power required |
| **Centrifuge** | Separate mixtures | Advanced processing |

---

## Basic Smelting

### Pure Metal Smelting

**Recipe:** 1 Ore → 1 Ingot

| Ore | Ingot | Smelting Time | Power |
|-----|-------|---------------|-------|
| Iron Ore | Iron Ingot | 5s (arc) / 20s (furnace) | 800W (arc) |
| Gold Ore | Gold Ingot | 5s | 800W |
| Copper Ore | Copper Ingot | 5s | 800W |
| Silver Ore | Silver Ingot | 5s | 800W |
| Lead Ore | Lead Ingot | 5s | 800W |
| Nickel Ore | Nickel Ingot | 5s | 800W |
| Cobalt Ore | Cobalt Ingot | 5s | 800W |
| Silicon Ore | Silicon Ingot | 5s | 800W |

**Arc Furnace Advantages:**
- 4x faster than regular furnace
- Higher throughput
- Requires IC10 automation

### IC10 Control

**Basic Smelter Automation:**
```ic10
# Smelt when ore present
alias furnace d0
alias oreStacker d1

main:
ls rOreQty oreStacker 0 Quantity
l rIdle furnace Idle

blez rOreQty deactivate  # No ore
blez rIdle main          # Furnace busy

# Ore present and furnace idle
s furnace On 1
s furnace Activate 1
j main

deactivate:
s furnace On 0
j main
```

---

## Alloy Recipes

### Steel

**Recipe:** Iron + Carbon
- 4 Iron Ingots
- 1 Carbon (or coal)
- **Yield:** 1 Steel Ingot

**Usage:**
- Construction (heavy plates)
- Reinforced structures
- Advanced crafting

**Hash Values:**
```ic10
define IRON_HASH -666742878
define CARBON_HASH 1582746610
```

### Electrum

**Recipe:** Gold + Silver
- 1 Gold Ingot
- 1 Silver Ingot
- **Yield:** 1 Electrum Ingot

**Usage:**
- Electronics
- High-value components

### Invar

**Recipe:** Iron + Nickel
- 2 Iron Ingots
- 1 Nickel Ingot
- **Yield:** 1 Invar Ingot

**Usage:**
- Temperature-resistant construction
- Advanced structures

### Constantan

**Recipe:** Copper + Nickel
- 1 Copper Ingot
- 1 Nickel Ingot
- **Yield:** 1 Constantan Ingot

**Usage:**
- Thermoelectric devices
- Temperature sensors

### Super Alloys

**Waspaloy, Stellite, Inconel, Hastelloy, Astroloy**

**Complex Recipes:**
- Multiple components
- Advanced processing
- High-end applications

**Reference:** See [Furnace Resources Guide](../../guides/furnace-resources.md) for complete alloy recipes.

---

## Processing Yields

### Material Efficiency

**Basic Smelting:**
- 1 Ore → 1 Ingot (100% yield)

**Alloys:**
- Multiple ingots → 1 alloy ingot
- Material loss for alloying
- Trade efficiency for properties

**Typical Efficiency:**
- Steel: 5 ingots → 1 steel (20% material efficiency)
- Electrum: 2 ingots → 1 electrum (50%)
- Invar: 3 ingots → 1 invar (33%)

### Production Rates

**Single Arc Furnace:**
- Throughput: ~12 ingots/minute (5s per smelt)
- Power: 800W continuous
- With automation: Continuous operation

**Furnace Array (4 furnaces):**
- Throughput: ~48 ingots/minute
- Power: 3200W
- Recommended for industrial operations

### Yield Calculations

**Iron Production Example:**
```
1 drill @ 5 ore/min = 300 ore/hour
1 furnace @ 12 ingot/min = 720 ingots/hour

Bottleneck: Drill production (limited by ore)
Furnace capacity underutilized

Solution: Add more drills
4 drills @ 20 ore/min = 1200 ore/hour
Now furnace is bottleneck
```

**Scale Planning:**
```
Target: 1000 iron ingots/hour

Furnaces needed: 1000 / 720 = 2 furnaces
Drills needed: 1000 / 300 = 4 drills

Ratio: 2 drills per furnace for balanced flow
```

---

## Processing Strategies

### Strategy 1: Single-Ore Focus

**Concept:** Specialize in one ore type

**Example: Iron Operation**
```
[4 Iron Drills] → [Sorter (Iron)] → [2 Arc Furnaces] → [Iron Ingots]
```

**Advantages:**
- Simple setup
- Optimized for single material
- Easy automation

**Disadvantages:**
- Limited material variety
- Must trade for other materials

### Strategy 2: Multi-Ore Processing

**Concept:** Process multiple ores in parallel

**Example: Diversified Operation**
```
[Iron Drills] → [Sorters] → [Iron Furnaces] → [Iron Storage]
[Gold Drills] → [Sorters] → [Gold Furnaces] → [Gold Storage]
[Copper Drills] → [Sorters] → [Copper Furnaces] → [Copper Storage]
```

**Advantages:**
- Material self-sufficiency
- Trading surplus
- Risk diversification

**Disadvantages:**
- Complex setup
- Higher infrastructure cost
- More automation complexity

### Strategy 3: Alloy Production

**Concept:** Process components for alloys

**Example: Steel Production**
```
[Iron Drills] → [Iron Furnaces] → [Iron Ingots] ─┐
                                                ├→ [Steel Furnace] → [Steel]
[Carbon Drills] → [Carbon Storage] ─────────────┘
```

**Advantages:**
- High-value output
- Material independence
- Advanced applications

**Disadvantages:**
- Complex ratios
- Component synchronization
- Higher skill requirement

---

## Advanced Processing

### Centrifuge Operations

**Purpose:** Separate mixed materials

**Applications:**
- Ore mixtures
- Atmospheric gases
- Impure materials

**IC10 Control:**
```ic10
# Centrifuge automation
alias centrifuge d0
alias inputStacker d1
alias output1 d2  # Output slot 0
alias output2 d3  # Output slot 1

# Check if input available
ls rQty inputStacker 0 Quantity
l rIdle centrifuge Idle

blez rQty noInput
blez rIdle main

# Activate centrifuge
s centrifuge On 1
s centrifuge Activate 1
j main

noInput:
s centrifuge On 0
j main
```

### Quality Control

**Automated Sorting by Quality:**

*Note: Stationeers doesn't have ore quality tiers, but hash-based sorting achieves similar organization.*

### Batch Processing

**Load Multiple Furnaces:**

```ic10
# Batch load multiple furnaces
define FURNACE_COUNT 4

init:
move rIndex 0

main:
beq rIndex 0 check0
beq rIndex 1 check1
beq rIndex 2 check2
beq rIndex 3 check3
j endTick

check0:
# Check furnace 0
l rIdle furnace0 Idle
ls rOre oreStacker 0 Quantity
blez rOre next0
blez rIdle next0
s furnace0 On 1
s furnace0 Activate 1
next0:
add rIndex rIndex 1
j main

# ... repeat for furnace 1, 2, 3

endTick:
move rIndex 0  # Reset for next tick
yield
j main
```

---

## Processing Flow Examples

### Simple Iron Processing

```
[Iron Drill] → [Iron Stacker] → [Arc Furnace] → [Iron Ingot Stacker]
```

**IC10:** See [single-drill-controller.ic10](../../examples/mining/single-drill-controller.ic10) and [auto-smelter-array.ic10](../../examples/mining/auto-smelter-array.ic10)

### Multi-Ore Processing

```
         [Drill Array]
              ↓
         [Sorter Network]
         ↓      ↓      ↓
    [Iron]  [Gold]  [Copper]
       ↓       ↓       ↓
  [Furnace] [Furnace] [Furnace]
       ↓       ↓       ↓
  [Iron Storage] [Gold Storage] [Copper Storage]
```

**IC10:** See [mining-complex-controller.ic10](../../examples/mining/mining-complex-controller.ic10)

### Alloy Processing

```
[Iron Furnaces] → [Iron Ingots] ─┐
                                   ├→ [Steel Furnace] → [Steel]
[Carbon Supply] → [Carbon] ────────┘
```

---

## Optimization Tips

### Furnace Utilization

**Problem:** Furnaces idle while ore waits

**Solution:** Balance drill-to-furnace ratio

```
Target: Furnace always smelting

Drill Rate: 5 ore/min per drill
Furnace Rate: 12 ingot/min

Optimal Ratio: 2-3 drills per furnace
```

### Power Efficiency

**Problem:** Power spikes with multiple furnaces

**Solution:** Stagger furnace activation

```ic10
# Activate furnaces in sequence
l rTick r0
add rTick rTick 1

# Furnace 1: ticks 0, 4, 8, ...
# Furnace 2: ticks 1, 5, 9, ...
# Furnace 3: ticks 2, 6, 10, ...
# Furnace 4: ticks 3, 7, 11, ...

and rTemp rTick 3
beq rTemp 0 activate1
beq rTemp 1 activate2
beq rTemp 2 activate3
beq rTemp 3 activate4
```

### Storage Optimization

**Problem:** Mixed ingots, hard to use

**Solution:** Hash-based sorting to stackers

```ic10
# Sort ingots by type
ls rHash sorter 0 OccupantHash

# Route to appropriate stacker
seq rTemp rHash IRON_HASH
s ironStacker On rTemp

seq rTemp rHash GOLD_HASH
s goldStacker On rTemp
```

---

## Resources

### Related Guides
- [Beginner Automation Guide](../../guides/mining-automation-beginner.md) - Smelter setup
- [Advanced Automation Guide](../../guides/mining-automation-advanced.md) - Array coordination
- [Furnace Resources Guide](../../guides/furnace-resources.md) - Complete furnace reference

### Local Examples
- [auto-smelter-array.ic10](../../examples/mining/auto-smelter-array.ic10) - Array automation
- [arc-furnace-array.ic10](../../examples/manufacturing/arc-furnace-array.ic10) - Furnace coordination
- [ore-stacker.ic10](../../examples/manufacturing/ore-stacker.ic10) - Sorting

### Knowledge Base
- [Ore Hash Reference](../hashes/reagent-hashes.md) - Hash values for automation
- [Equipment Reference](../mining/equipment.md) - Device specifications

---

## Summary

Efficient processing chains transform raw ore into useful materials. Understand your recipes, balance your equipment, and automate for continuous operation.

**Key Takeaways:**
1. Basic smelting: 1 ore → 1 ingot
2. Alloys require multiple components
3. Balance drill-to-furnace ratio (2-3:1)
4. Automate with IC10 for efficiency
5. Use hash-based sorting for organization

**Next Steps:**
- Plan your processing strategy
- Size your furnace array
- Implement automation
- Optimize for throughput

Happy smelting!

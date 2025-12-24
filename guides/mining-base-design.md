# Mining Base Design Guide

Strategic planning and layout design for efficient mining operations.

## Difficulty: All Levels | Prerequisites: None

This guide covers base layout, power systems, life support, storage, and expansion planning for mining outposts.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Location Selection](#location-selection)
3. [Layout Principles](#layout-principles)
4. [Power Systems](#power-systems)
5. [Life Support](#life-support)
6. [Storage Design](#storage-design)
7. [Environment-Specific Bases](#environment-specific-bases)
8. [Expansion Planning](#expansion-planning)

---

## Introduction

### Why Base Design Matters

A well-designed mining base:
- Maximizes efficiency and throughput
- Minimizes travel time and logistics
- Scales easily for expansion
- Provides safe working conditions
- Manages power effectively

### Design Phases

**Phase 1: Site Selection** - Find optimal location
**Phase 2: Core Infrastructure** - Power, life support, storage
**Phase 3: Mining Operations** - Drills, processing, transport
**Phase 4: Expansion** - Scale up as needed

---

## Location Selection

### Ore Proximity

**Primary Factor:** Distance to ore deposits

**Ideal:**
- Base directly on rich iron deposit
- 2-3 other ore types within 50m
- At least one deep ore accessible (gold, silver, etc.)

**Acceptable:**
- Within 20m of good deposit
- Conveyor distance to other ores
- Short jetpack ride to deep deposits

**Avoid:**
- >100m from primary deposit (too much travel)
- No nearby ore variety
- Difficult terrain (cliffs, deep valleys)

### Terrain Considerations

**Flat Terrain:**
- Pros: Easy construction, ample space
- Cons: May need to dig for deep ores

**Hills/Cliffs:**
- Pros: Exposed ore veins, vertical access
- Cons: Difficult construction, requires jetpack

**Underground:**
- Pros: Stable temperature, protection
- Cons: Requires excavation, lighting, atmosphere

### Accessibility

**Consider:**
- Landing zone for supply drops
- Path for rover (if available)
- Expansion space
- Secondary escape routes

---

## Layout Principles

### Zone-Based Design

**Divide base into functional zones:**

```
┌──────────────────────────────────┐
│  Zone 1: Living & Command         │
│  - Airlock entry                  │
│  - Atmosphere pressurization     │
│  - Command seat                   │
│  - Basic storage                  │
├──────────────────────────────────┤
│  Zone 2: Power Generation         │
│  - Battery bank                   │
│  - Solar panels / generators      │
│  - Power distribution             │
├──────────────────────────────────┤
│  Zone 3: Processing              │
│  - Arc furnaces                   │
│  - Ingot storage                  │
│  - Workbench                      │
├──────────────────────────────────┤
│  Zone 4: Mining Operations        │
│  - Drills                         │
│  - Ore collection                 │
│  - Sorters                        │
│  - Transport systems              │
└──────────────────────────────────┘
         │
    [Ore Deposits]
```

### Flow Optimization

**Ore Flow:**
```
Ore Deposit → Drill → Conveyor → Sorter → Furnace → Ingot Storage
```

**Player Flow:**
```
Airlock → Command → Processing → Mining → Maintenance
```

**Principles:**
- Minimize backtracking
- Direct paths for high-frequency routes
- Separate ore flow from player movement
- Access for maintenance without disrupting flow

### Modular Construction

**Build in modules for easy expansion:**

```
[Core Module]
    │
    ├── [Mining Module 1]
    ├── [Mining Module 2]  (future)
    └── [Mining Module 3]  (future)
```

**Benefits:**
- Add capacity without redesign
- Isolate failures
- Parallel operations
- Flexible expansion

---

## Power Systems

### Power Budgeting

**Calculate Your Needs:**

| Device | Idle Power | Active Power | Quantity | Total |
|--------|------------|--------------|----------|-------|
| Mining Drill | 10W | 500W | 1-4 | 500-2000W |
| Arc Furnace | 20W | 800W | 1-4 | 800-3200W |
| Conveyor | 5W | 50W | 2-8 | 100-400W |
| Sorter | 5W | 20W | 2-4 | 40-80W |
| Life Support | 100W | 200W | 1 | 200W |
| Lighting | 50W | 50W | 10 | 500W |
| **Total (Small)** | | | | ~2000W |
| **Total (Large)** | | | | ~6000W |

### Solar Array Sizing

**Mars/Moon:**
```
Power Needed: 2000W
Solar Panel Output: ~150W (average)
Safety Margin: 2x

Panels Needed = (2000W * 2) / 150W = ~27 panels
```

**Guidelines:**
- **Small base (1 drill, 1 furnace):** 10-15 panels
- **Medium base (2-3 drills, 2 furnaces):** 20-30 panels
- **Large base (4+ drills, 4+ furnaces):** 40+ panels

### Battery Sizing

**Calculate Storage:**

**Night Duration:**
- Mars: ~500 seconds (8 minutes)
- Moon: Very long (need large bank)

**Example Calculation:**
```
Power Draw: 2000W
Night Duration: 500s
Energy Needed: 2000W * 500s = 1,000,000 J

Large Battery: ~10,000 J
Batteries Needed: 1,000,000 / 10,000 = 100 batteries
```

**Practical Sizing:**
- **Minimum:** 10-20 large batteries (short operation)
- **Recommended:** 30-50 large batteries (overnight)
- **Industrial:** 100+ large batteries (continuous)

### Generator Backup

**When to Use:**
- Venus (limited solar)
- Underground (no solar)
- High power demand
- Redundancy needed

**Setup:**
```
[Fuel Tank] → [Generator] → [Battery Bank]
```

**Auto-Start Control:**
```ic10
# Start generator when battery < 20%
l rCharge battery Charge
blt rCharge 20 startGen
j endTick

startGen:
s generator On 1
j endTick
```

---

## Life Support

### Atmosphere Systems

**Pressurized Living Area:**

**Components:**
- Air pump (pressurization)
- Vent (distribution)
- Scrubber (CO2 removal)
- Heater/cooler (temperature)
- Pressure regulator

**IC10 Control:**
See [Atmosphere Examples](../examples/atmosphere/) for complete implementations.

### Temperature Control

**Mars:**
- **Challenge:** Cold nights (-60°C)
- **Solution:** Heater in living area
- **Power:** ~200-500W

**Moon:**
- **Challenge:** Extreme cold (-150°C)
- **Solution:** Heavy heating, insulated walls
- **Power:** ~500-1000W

**Venus:**
- **Challenge:** Extreme heat (400°C+)
- **Solution:** Active cooling, insulated walls
- **Power:** ~500-1000W

### Airlock Design

**Basic Airlock:**
```
[External] → [Airlock Chamber] → [Internal]
           [Door1]        [Door2]
```

**Safety:**
- Only one door open at a time
- Pressure equalization
- Emergency override

**IC10 Airlock Control:**
See [Airlock Resources Guide](airlock-resources.md) for implementations.

---

## Storage Design

### Ore Storage

**Stacker-Based Storage:**

**Design:**
```
[Conveyor] → [Sorter Network] → [Ore Stackers]
                                   ↓
                             [Iron] [Gold] [Copper] [Other]
```

**Capacity Planning:**
- **Small operation:** 2-4 stackers
- **Medium operation:** 6-10 stackers
- **Large operation:** 15+ stackers

**Organization:**
- One stacker per ore type (ideal)
- Multi-ore stacker with sorters (acceptable)
- General ore storage (fallback)

### Ingot Storage

**Priority:** Organized by material type

**Layout:**
```
[Arc Furnaces] → [Ingot Stackers]
                      ↓
              [Iron] [Steel] [Gold] [Copper] [Other]
```

**Access:**
- Near workbench for crafting
- Near trading port (if applicable)
- Clear labeling

### Bulk Storage

**Large Silos (Advanced):**

For massive operations:
- **Volume:** 1000+ units
- **Access:** Chute or conveyor
- **Automation:** Level monitoring

---

## Environment-Specific Bases

### Mars Surface Base

**Characteristics:**
- Thin CO2 atmosphere (can't breathe)
- Moderate temperature range
- Good solar availability

**Design Priorities:**
1. Pressurized living area (oxygen generation)
2. Solar array with overnight battery
3. Heater for cold nights
4. Dust protection (sealed structure)

**Layout:**
```
┌────────────────────────┐
│  Living (Pressurized)   │
│  - Airlock entry        │
│  - Life support         │
│  - Command station      │
├────────────────────────┤
│  Processing (Unpress.)  │
│  - Furnaces             │
│  - Storage              │
└────────────────────────┘
         │
    [Solar Array]
    [Battery Bank]
         │
    [Mining Operations]
```

### Moon/Asteroid Base

**Characteristics:**
- Vacuum (full suit always)
- Extreme temperature swings
- Rich in metals, poor in organics

**Design Priorities:**
1. Radiation protection (underground preferred)
2. Massive battery bank (long nights)
3. Heavy heating requirements
4. Bring organics from elsewhere

**Layout:**
```
[Underground Habitat]
         │
    [Solar Surface]
    [Battery Bank]
         │
    [Shaft to Mine]
```

**Challenges:**
- Extreme cold requires constant heating
- Long lunar nights need huge battery banks
- Limited surface resources

### Venus/Underground Base

**Characteristics:**
- High pressure atmosphere
- Extreme heat
- Corrosive gases

**Design Priorities:**
1. Pressure-resistant structures
2. Active cooling systems
3. Corrosion-resistant materials
4. Generator power preferred

**Layout:**
```
[Pressure Vessel Habitat]
         │
    [Cooling System]
    [Generator Room]
         │
    [Drilled Shafts]
```

**Challenges:**
- Equipment degrades from atmosphere
- Limited solar (overcast/hazy)
- Heat management critical

---

## Expansion Planning

### Phase 1: Initial Base (Days 1-7)

**Goals:**
- Establish shelter
- Basic life support
- Hand mining operations
- Stockpile key resources

**Components:**
- Small pressurized habitat
- Hand scanner and drill
- Basic solar (2-3 panels)
- Small battery (5-10)
- Temporary ore storage (lockers)

### Phase 2: Basic Automation (Days 7-21)

**Goals:**
- First automated drill
- Smelting capability
- Organized storage
- Reliable power

**Components:**
- 1-2 automated drills
- 1 arc furnace
- Solar array (10-15 panels)
- Battery bank (20-30)
- Sorter system
- Ingot storage stackers

### Phase 3: Industrial Scale (Days 21-42)

**Goals:**
- Multi-drill operation
- Processing pipeline
- Extended storage
- Power self-sufficiency

**Components:**
- 4+ automated drills
- 2-4 arc furnaces
- Solar array (30+ panels)
- Battery bank (50+)
- Conveyor transport
- Complete ore sorting
- Integrated control system

### Phase 4: Advanced Operations (Days 42+)

**Goals:**
- Deep mining or excavator
- Complex state machine control
- Industrial production
- Multi-site coordination

**Components:**
- Excavator or deep miner
- Advanced automation
- Secondary mining sites
- Trading infrastructure
- Research facilities

### Modular Expansion

**Add Mining Modules:**
```
[Core Base] ──→ [Module 1: Iron]
              ├─→ [Module 2: Gold]
              ├─→ [Module 3: Copper]
              └─→ [Module 4: Deep Mining]
```

**Each Module Includes:**
- Dedicated drills
- Local power tap
- Transport link to core
- Independent automation (optional)

---

## Resources

### Related Guides
- [Manual Mining Techniques](mining-manual-techniques.md) - Early game strategies
- [Beginner Automation](mining-automation-beginner.md) - First automated setup
- [Environment Guide](mining-environment-guide.md) - Environment-specific details

### Examples
- [single-drill-controller.ic10](../examples/mining/single-drill-controller.ic10) - Basic power management
- [multi-drill-coordinator.ic10](../examples/mining/multi-drill-coordinator.ic10) - Advanced power budgeting
- [mining-complex-controller.ic10](../examples/mining/mining-complex-controller.ic10) - System integration

### Knowledge Base
- [Ore Deposits](../knowledge/mining/ore-deposits.md) - Site selection reference
- [Equipment](../knowledge/mining/equipment.md) - Device specifications

---

## Summary

Well-designed mining bases are efficient, scalable, and safe. Plan for expansion from the start, zone your operations, and size your power systems appropriately.

**Key Takeaways:**
1. Build near ore deposits (proximity is efficiency)
2. Zone your base (living, power, processing, mining)
3. Oversize power systems (2x safety margin)
4. Plan for modular expansion
5. Adapt to environment-specific challenges

**Next Steps:**
- Survey area with hand scanner
- Select optimal base location
- Design initial layout
- Build in phases
- Expand as needed

Happy building!

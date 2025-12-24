# Beginner Mining Automation Guide

Learn to automate mining operations with IC10 for players familiar with basic concepts (Days 7-21).

## Difficulty: Beginner-Intermediate | Prerequisites

- Basic IC10 knowledge (device I/O, loops, conditionals)
- Familiarity with hand mining ([Manual Techniques Guide](mining-manual-techniques.md))
- Power system basics
- Access to Mining Drill device

---

## Table of Contents

1. [Introduction](#introduction)
2. [Single Drill Automation](#single-drill-automation)
3. [Simple Ore Sorting](#simple-ore-sorting)
4. [Power Management](#power-management)
5. [Base Layout Basics](#base-layout-basics)
6. [Common Patterns](#common-patterns)
7. [Troubleshooting](#troubleshooting)
8. [Next Steps](#next-steps)

---

## Introduction

### Why Automate Mining?

**Benefits:**
- Continuous ore production while you do other tasks
- Consistent material supply for manufacturing
- Reduce repetitive manual labor
- Scale up operations efficiently

**When to Automate:**
- Making 3+ trips to same ore deposit
- Furnace running constantly
- Need >500 units of any ore regularly
- Comfortable with IC10 basics

### Automation Levels

**Level 1: Basic Drill Control**
- Single drill on/off
- Power awareness
- No ore routing

**Level 2: Drill + Sorting**
- Automated drill
- Ore type sorting
- Basic storage management

**Level 3: Integrated Processing**
- Drill to smelter pipeline
- Automated processing
- Ingot storage

This guide covers Levels 1-2. Level 3 is covered in [Advanced Automation Guide](mining-automation-advanced.md).

---

## Single Drill Automation

### Understanding the Mining Drill

**Logic Types:**

| Logic Type | Read/Write | Description |
|------------|------------|-------------|
| `On` | Both | Turn drill on/off (0=off, 1=on) |
| `Power` | Read-only | Current power state |
| `Setting` | Both | Operation mode |

**Power Consumption:**
- Active: High power draw
- Idle: Low standby power
- Consider battery sizing

### Basic Drill Control (On/Off)

The simplest automation: turn drill on when conditions are met.

**Hardware Setup:**
```
[Battery] → [Mining Drill] → [Ore Output]
     ↑
[Solar Panel]
```

**IC10 Script:** [single-drill-controller.ic10](../examples/mining/single-drill-controller.ic10)

```ic10
# Auto-activate mining drill with power management
# Turns ON when battery > 40%
# Turns OFF when battery < 30%

alias drill d0
alias battery d1
alias rCharge r0
alias rState r1
alias rNewState r2

define POWER_HIGH 40  # Turn on above this
define POWER_LOW 30   # Turn off below this

main:
l rCharge battery Charge  # Read battery charge
l rState drill On          # Read drill state

# Hysteresis logic
bgt rCharge POWER_HIGH turnOn
blt rCharge POWER_LOW turnOff
j updateDisplay  # Within deadband

turnOn:
move rNewState 1
j applyState

turnOff:
move rNewState 0
j applyState

applyState:
beq rState rNewState updateDisplay
s drill On rNewState

updateDisplay:
yield
j main
```

**How It Works:**
1. Read battery charge percentage
2. If charge > 40%, turn drill on
3. If charge < 30%, turn drill off
4. If 30-40%, do nothing (hysteresis deadband)
5. Loop continuously

**Why Hysteresis?**
- Prevents rapid on/off cycling
- Protects drill from power fluctuation
- Maintains battery buffer for other needs

### Setup Steps

**1. Device Placement:**
```
Place mining drill directly on ore deposit
└─ Use hand scanner to find high-density area
└─ Verify drill placement (outline should be on ore)
```

**2. Power Connection:**
```
Connect battery to drill
└─ Use network cable (cable reel)
└─ Or place adjacent (auto-connects)
```

**3. IC10 Setup:**
```
Place IC10 chip
└─ Connect to battery (d1)
└─ Connect to drill (d0)
└─ Load script
└─ Write code or copy from example
└─ Enable with lever
```

**4. Testing:**
```
Manual test first
└─ Disable IC10 (lever off)
└─ Turn drill on manually
└─ Verify ore production
└─ Check power consumption
└─ Then enable IC10
```

### Expected Results

**Production Rate:**
- 5-10 iron ore per minute (varies by deposit)
- Battery drain during operation
- Battery recharge when drill off

**Power Budget:**
- 1 large battery ≈ 20-30 minutes operation
- Solar panel offsets drain during daytime
- Size battery bank for overnight operation

---

## Simple Ore Sorting

### Why Sort Ores?

**Manual vs. Automated:**
- **Manual**: Pick up each ore, place in correct locker
- **Automated**: Sorter routes by type, hands-free

**Benefits:**
- Organized storage
- Easier smelting setup
- Reduced manual sorting labor

### Understanding Sorters

**Sorter Device:**

| Property | Description |
|----------|-------------|
| **Slots** | Logic slots for item detection |
| **Hash** | Each item type has unique ID |
| **Routing** | Can direct items based on hash |

**Hash-Based Detection:**
```ic10
# Read item hash from slot
ls r0 sorter 0 OccupantHash

# Compare to target
define IRON_HASH -666742878
seq r1 r0 IRON_HASH  # r1 = 1 if iron, 0 if not
```

### Single Ore Sorting

Route one specific ore type to dedicated storage.

**Hardware Setup:**
```
[Drill] → [Sorter] → [Iron Storage]
                   → [Other Storage]
```

**IC10 Script:** [simple-ore-sorter.ic10](../examples/mining/simple-ore-sorter.ic10)

```ic10
# Route specific ore type to storage
define TARGET_HASH -666742878  # Iron

alias sorter d0
alias stacker d1
alias rItemHash r0
alias rMatch r1

main:
ls rItemHash sorter 0 OccupantHash
seq rMatch rItemHash 0
beqz rMatch noItem

seq rMatch rItemHash TARGET_HASH
s stacker On rMatch
beqz rMatch endTick

yield
s stacker On 0

noItem:
s stacker On 0

endTick:
yield
j main
```

**How It Works:**
1. Read item hash from sorter slot 0
2. Check if slot is occupied (hash ≠ 0)
3. Compare item hash to target (iron)
4. Activate stacker if match
5. Wait for item to process
6. Reset and repeat

**Common Ore Hashes:**
```ic10
define IRON_HASH    -666742878  # Most common
define GOLD_HASH    -409226641  # Precious
define COPPER_HASH  -1172078909 # Electronics
define SILVER_HASH   687283565  # Precious
```

See [Ore Hash Reference](../knowledge/hashes/reagent-hashes.md) for complete list.

### Multi-Ore Sorting

Sort multiple ore types to different storage locations.

**Concept:**
```
[Drill] → [Sorter 1: Iron] → [Iron Stacker]
        → [Sorter 2: Gold] → [Gold Stacker]
        → [Other]          → [General Stacker]
```

**Advanced Example:**
For multi-ore sorting, see [ore-stacker.ic10](../examples/manufacturing/ore-stacker.ic10) in the manufacturing examples.

---

## Power Management

### Understanding Drill Power Needs

**Power Consumption:**

| Device | Idle | Active | Notes |
|--------|------|--------|-------|
| Mining Drill | Low | High | Variable by ore hardness |
| Battery | Charging | Discharging | Net flow matters |
| Solar Panel | 0 | Variable | Day/night cycle |

**Power Budgeting:**
```
Drill active: 500-1000 W (approximate)
Solar panel output: Up to 200 W (full sun)
Large battery capacity: 10,000 J (approximate)

Runtime: 10-20 minutes per battery (no solar)
With solar: Extended operation, depends on sunlight
```

### Battery Sizing

**Minimum Viable:**
- 1 large battery
- ~20 minutes operation
- Good for testing

**Recommended:**
- 2-3 large batteries
- 1-2 hours operation
- Overnight coverage

**Industrial:**
- 4+ large batteries
- Multi-drill support
- Continuous operation

### Solar Integration

**Mars/Moon:**
```
[Solar Array] → [Batteries] → [Drill]
```

**Guidelines:**
- 1 solar panel offsets ~20-40% of drill usage
- 3 panels ≈ net neutral during daylight
- Battery bank for nighttime operation

**IC10 Solar Tracking:**
For optimal solar output, see [Solar Resources Guide](solar-resources.md) and examples in [power/](../examples/power/) directory.

### Generator Backup

**When to Use:**
- Venus (limited solar)
- Underground (no solar)
- High power demand

**Setup:**
```
[Generator] → [Batteries] → [Drill]
     ↑
[Fuel Tank]
```

**IC10 Generator Control:**
Monitor battery charge, start generator when low:

```ic10
# Generator backup control
alias battery d0
alias generator d1
alias rCharge r0

define GEN_START 20  # Start below 20%
define GEN_STOP 50   # Stop above 50%

main:
l rCharge battery Charge
blt rCharge GEN_START startGen
bgt rCharge GEN_STOP stopGen
yield
j main

startGen:
s generator On 1
yield
j main

stopGen:
s generator On 0
yield
j main
```

---

## Base Layout Basics

### Compact Mining Base

**Principles:**
- Proximity to ore deposit
- Efficient space usage
- Room for expansion
- Accessible logistics

**Example Layout (Top-Down):**
```
┌─────────────────────┐
│  [Living Quarters]  │
├─────────────────────┤
│ [Airlock] │ [Power] │
├─────────────────────┤
│  [Processing] Area  │
│                     │
│ [Furnace] [Stacker] │
└─────────────────────┘
         │
    [Mining Drill]
         │
    [Ore Deposit]
```

### Zone Planning

**Zone 1: Living**
- Airlock entry
- Atmosphere pressurization
- Basic life support
- Command seat/computer

**Zone 2: Power**
- Battery bank
- Solar panels or generator
- Power distribution (cables)
- IC10 control

**Zone 3: Processing**
- Arc furnace
- Ingot storage
- Workbench area
- Access to mine

**Zone 4: Mining**
- Drill(s)
- Ore collection
- Sorter systems
- Transport to processing

### Expansion Considerations

**Phase 1 (Current):**
- 1 drill
- 1 furnace
- Basic storage

**Phase 2 (Future):**
- +2 drills
- +1 furnace
- Conveyor transport
- Automated sorting

**Layout for Expansion:**
- Leave space for additional drills
- Plan cable routing
- Reserve area for conveyors
- Modular construction

---

## Common Patterns

### Hysteresis Control

**Used In:** Drill control, furnace control, battery management

**Pattern:**
```ic10
# Two thresholds prevent oscillation
define HIGH_THRESHOLD 60
define LOW_THRESHOLD 40

# Above high? Turn OFF
# Below low? Turn ON
# In between? No change (deadband)
```

**Benefits:**
- Prevents rapid cycling
- Stable operation
- Better for equipment lifespan

### Hash-Based Detection

**Used In:** Ore sorting, inventory management

**Pattern:**
```ic10
# Read item hash
ls r0 device 0 OccupantHash

# Compare to target
define TARGET_HASH -666742878
seq r1 r0 TARGET_HASH

# Route based on match
beqz r1 notMatch
# Handle matched item
```

**Benefits:**
- Type-specific operations
- Automated sorting
- Inventory tracking

### State Machine (Basic)

**Used In:** Multi-phase operations

**Pattern:**
```ic10
# States: IDLE, ACTIVE, ERROR
beq rState STATE_IDLE doIdle
beq rState STATE_ACTIVE doActive
beq rState STATE_ERROR doError

doIdle:
# Check conditions to transition
# ...

doActive:
# Normal operation
# ...

doError:
# Handle error condition
# ...
```

**Benefits:**
- Clear operation phases
- Easier debugging
- Handles complex logic

See [State Machine Template](../examples/patterns/state-machine-template.ic10) for full pattern.

---

## Troubleshooting

### Drill Not Activating

**Symptoms:**
- Drill stays off despite script running
- No ore production
- Battery full

**Diagnosis:**
```ic10
# Add debug display
alias drill d0
alias battery d1
alias display d2

l r0 battery Charge
s display Setting r0  # Show battery charge
l r1 drill On
s display Setting r1  # Show drill state
```

**Common Causes:**
1. **Not on ore deposit** - Move drill to visible ore
2. **No power connection** - Check cables
3. **Threshold too high** - Lower POWER_HIGH define
4. **Device slots wrong** - Verify d0=drill, d1=battery

**Fix:**
1. Use hand scanner, verify drill on ore
2. Check network with screwdriver (show network)
3. Adjust thresholds in code
4. Reconnect devices to correct slots

### Power Drain Too Fast

**Symptoms:**
- Battery depletes in <5 minutes
- Drill stops frequently
- No net power gain

**Causes:**
1. **Insufficient solar** - Add more panels
2. **Battery too small** - Add more batteries
3. **Drill on wrong deposit** - Verify ore present
4. **Daytime only** - Need overnight storage

**Fix:**
1. Add solar panels (2-3 minimum)
2. Increase battery bank (2-3 large batteries)
3. Verify drill placement on ore
4. Size for 2x operation time

### Ore Not Sorting

**Symptoms:**
- Sorter not routing correctly
- All ores go to same place
- Stacker not activating

**Diagnosis:**
```ic10
# Debug hash reading
alias sorter d0
alias display d1

ls r0 sorter 0 OccupantHash
s display Setting r0  # Show item hash
```

**Common Causes:**
1. **Wrong hash value** - Verify define constant
2. **Slot empty** - Item not in slot 0
3. **Sorter mode wrong** - Check device settings
4. **Stacker full** - No storage space

**Fix:**
1. Verify hash from [reagent-hashes.md](../knowledge/hashes/reagent-hashes.md)
2. Check item position in sorter
3. Configure sorter mode with screwdriver
4. Empty stacker or add more storage

### IC10 Script Errors

**Symptoms:**
- Script won't load
- Immediate crash
- "Syntax error"

**Common Issues:**
1. **Line too long** - Max 90 characters
2. **Too many lines** - Max 128 lines
3. **Invalid instruction** - Typo in opcode
4. **Undefined alias** - Using undefined alias

**Fix:**
1. Split long lines with multiple instructions
2. Optimize or reduce functionality
3. Check spelling, compare to reference
4. Define all aliases before use

---

## Next Steps

### Your First Automated Mining Setup

**Checklist:**
- [ ] Locate rich iron deposit with hand scanner
- [ ] Place mining drill on deposit
- [ ] Setup battery (2-3 large)
- [ ] Add solar panels (2-3 minimum)
- [ ] Load single-drill-controller.ic10
- [ ] Connect devices correctly
- [ ] Test and verify operation
- [ ] Add ore sorter for automation
- [ ] Setup storage stackers
- [ ] Connect to arc furnace

**Expected Timeline:**
- Day 7-10: Setup first drill
- Day 10-14: Add sorting
- Day 14-21: Integrate with furnace

### From Beginner to Intermediate

**After mastering single drill:**

1. **Add second drill** (different ore type)
   - Multi-drill coordinator script
   - Shared power infrastructure
   - Separate storage

2. **Implement conveyor transport**
   - Move ore automatically
   - Reduce manual handling
   - Connect mine to furnace

3. **Automate furnace feeding**
   - Ore → furnace pipeline
   - Monitor output
   - Ingot storage management

See [Advanced Automation Guide](mining-automation-advanced.md) for these topics.

### Learning Path

**Beginner (You are here):**
- Single drill control ✅
- Basic ore sorting ✅
- Power management ✅

**Intermediate (Next):**
- Multi-drill coordination
- Conveyor systems
- Furnace array automation
- Storage management

**Advanced:**
- Mining complex state machine
- Deep miner or excavator
- Full processing pipeline
- Industrial scale operations

---

## Resources

### Local Examples
- [single-drill-controller.ic10](../examples/mining/single-drill-controller.ic10) - Basic automation
- [simple-ore-sorter.ic10](../examples/mining/simple-ore-sorter.ic10) - Ore routing
- [ore-scanner.ic10](../examples/mining/ore-scanner.ic10) - Data display

### Related Guides
- [Manual Mining Techniques](mining-manual-techniques.md) - Before automation
- [Advanced Automation Guide](mining-automation-advanced.md) - Next steps
- [Base Design Guide](mining-base-design.md) - Layout strategies

### Knowledge Base
- [Ore Deposits](../knowledge/mining/ore-deposits.md) - Where to find ores
- [Equipment Reference](../knowledge/mining/equipment.md) - Device specifications
- [Ore Hash Reference](../knowledge/hashes/reagent-hashes.md) - Hash values

### Patterns
- [Hysteresis Template](../examples/patterns/hysteresis-template.ic10) - On/off control
- [State Machine Template](../examples/patterns/state-machine-template.ic10) - Multi-phase operations

---

## Summary

You now have the knowledge to automate your first mining operation! Start with a single iron drill, get it running reliably, then expand from there.

**Key Takeaways:**
1. Use hysteresis control for stable operation
2. Size power system for 2x expected runtime
3. Sort ores using hash-based detection
4. Plan for expansion from the start
5. Debug with display output

**Remember:**
- Test manually before automating
- Start simple, add complexity gradually
- Monitor and adjust as needed
- Don't be afraid to experiment

Happy automating!

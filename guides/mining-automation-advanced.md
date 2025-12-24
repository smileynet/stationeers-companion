# Advanced Mining Automation Guide

Complex mining automation systems for experienced IC10 programmers (Days 21+).

## Difficulty: Advanced | Prerequisites

- Comfortable with IC10 (state machines, batch operations)
- Completed [Beginner Automation Guide](mining-automation-beginner.md)
- Understanding of power budgets and resource management
- Familiar with hash-based operations

---

## Table of Contents

1. [Introduction](#introduction)
2. [Multi-Drill Arrays](#multi-drill-arrays)
3. [Conveyor Systems](#conveyor-systems)
4. [Automated Sorting](#automated-sorting)
5. [Processing Integration](#processing-integration)
6. [Full Mining Complex](#full-mining-complex)
7. [Performance Optimization](#performance-optimization)
8. [Advanced Patterns](#advanced-patterns)

---

## Introduction

### Beyond Single Drill Automation

You've mastered single drill automation. Now what?

**Advanced Automation Enables:**
- Industrial-scale ore production (1000+ units per hour)
- Hands-off operation for extended periods
- Integrated processing pipelines
- Complex resource allocation
- Multi-site coordination

**Scope:**
This guide covers complete mining systems from extraction to processing. You'll learn to coordinate multiple devices, manage power budgets, and implement state machines for complex workflows.

---

## Multi-Drill Arrays

### Why Multiple Drills?

**Single Drill:**
- 5-10 ore per minute
- Limited by deposit size
- Single point of failure

**Multi-Drill Array (4 drills):**
- 20-40 ore per minute
- Spreads across multiple deposits
- Redundancy (if one fails)
- Power scheduling flexibility

### Power-Aware Drill Coordination

**Challenge:** Multiple drills drain batteries quickly.

**Solution:** Activate drills based on available power.

**IC10 Script:** [multi-drill-coordinator.ic10](../examples/mining/multi-drill-coordinator.ic10)

```ic10
# Power-aware multi-drill coordination
# Charge > 60%: 4 drills active
# Charge 40-60%: 2 drills active
# Charge < 40%: 0 drills active

main:
l rCharge battery Charge

bgt rCharge POWER_HIGH allActive
sgt rActiveCount rCharge POWER_MED
sub rActiveCount rActiveCount 1
bgt rActiveCount 0 twoActive
j allOff
```

**How It Works:**
1. Monitor battery charge
2. Scale active drill count
3. Prevent deep battery drain
4. Maintain operation during low solar

### Batch Operations with Hash

**Challenge:** Controlling 4+ drills individually requires lots of code.

**Solution:** Use batch operations (`lb`, `sb`) with device hash.

**Hash-Based Control:**
```ic10
# Control all drills at once
define DRILL_HASH HASH("StructureMiningDrill")

# Read average power from all drills
lb rAvgPower DRILL_HASH Power 0  # mode 0 = average

# Turn on all drills
sb DRILL_HASH On 1

# Turn off all drills
sb DRILL_HASH On 0
```

**Batch Modes:**
- `0` = Average
- `1` = Sum
- `2` = Minimum
- `3` = Maximum

**Example: Total Power Monitoring**
```ic10
# Monitor total power consumption
lb rTotalPower DRILL_HASH Power 1  # Sum mode
bgt rTotalPower POWER_LIMIT reduceDrills
```

### Drill Placement Strategies

**Linear Array:**
```
[Drill1] [Drill2] [Drill3] [Drill4]
   ↓        ↓        ↓        ↓
[Shared Conveyor Transport]
```
- Pros: Simple transport, easy to expand
- Cons: Long cable runs, spacing issues

**Cluster Layout:**
```
   [Drill1] [Drill2]
      ↘      ↙
     [Conveyor]
      ↙      ↘
   [Drill3] [Drill4]
```
- Pros: Compact, shared infrastructure
- Cons: Complex routing, potential bottlenecks

**Parallel Rows:**
```
[Drill1] → [Conveyor1] ──┐
[Drill2] → [Conveyor2] ──┤
                           ├→ [Processing]
[Drill3] → [Conveyor3] ──┤
[Drill4] → [Conveyor4] ──┘
```
- Pros: Scalable, redundant
- Cons: More complex, expensive

---

## Conveyor Systems

### Conveyor Basics

**Device:** Conveyor Belt

| Logic Type | Description |
|------------|-------------|
| `On` | Turn conveyor on/off |
| `Mode` | Operation mode |
| `Setting` | Speed setting |

**Purpose:** Move items from mining to processing without manual handling.

### Flow Control

**Challenge:** Prevent overflow at destination.

**Solution:** Monitor destination level, control conveyor flow.

**IC10 Script:** [conveyor-belt-controller.ic10](../examples/mining/conveyor-belt-controller.ic10)

```ic10
# Flow control based on destination level
main:
l rStackLevel stacker Setting
blt rStackLevel STACK_MAX startConveyor
j stopConveyor

startConveyor:
s conveyor On 1
j endTick

stopConveyor:
s conveyor On 0
j endTick
```

**Advanced: Rate Limiting**
```ic10
# Throttle conveyor speed based on backlog
l rBacklog detector Setting  # Items waiting

# Adjust conveyor speed
bgt rBacklog 100 fullSpeed
bgt rBacklog 50 halfSpeed
j stopConveyor

fullSpeed:
s conveyor Setting 100
s conveyor On 1
j endTick

halfSpeed:
s conveyor Setting 50
s conveyor On 1
j endTick
```

### Conveyor Network Design

**Simple Linear:**
```
[Drills] → [Conveyor] → [Sorter] → [Storage]
```

**Branching:**
```
          → [Sorter Iron] → [Iron Storage]
[Drills] → [Conveyor] → [Sorter Gold] → [Gold Storage]
          → [Sorter Other] → [Other Storage]
```

**Merging:**
```
[Drill1] → [Conv1] ─┐
[Drill2] → [Conv2] ─┼→ [Main Conveyor] → [Processing]
[Drill3] → [Conv3] ─┘
```

---

## Automated Sorting

### Hash-Based Multi-Ore Sorting

**Challenge:** Separate multiple ore types automatically.

**Solution:** Digital flip-flop splitters with hash detection.

**Example:** 3-Ore Sorter
```
[Input] → [FF Splitter 1: Iron] → [Iron Stacker]
         → [FF Splitter 2: Gold] → [Gold Stacker]
         → [Other] → [General Stacker]
```

**Reference:** See [ore-stacker.ic10](../examples/manufacturing/ore-stacker.ic10) for complete implementation.

### Sorting Network Architecture

**Single-Stage Sorting:**
```
[Mixed Ore] → [Sorter Array] → [Sorted Storage]
                        → [Overflow]
```

**Two-Stage Sorting:**
```
[Mixed Ore] → [Coarse Sort] → [Metal / Non-Metal]
                           → [Fine Sort] → [Individual Ores]
```

### Stacker Integration

**Stacker Modes:**
- `On`: Enable/disable stacker
- `Mode`: Operation mode (IC mode vs auto)
- `Setting`: Stack size limit

**IC Mode Control:**
```ic10
# Manual activation (IC mode)
s stacker Mode 1  # IC mode
s stacker Activate 1  # Trigger one operation

# Continuous mode
s stacker Mode 0  # Auto mode
s stacker On 1  # Always on
```

---

## Processing Integration

### Mine-to-Smelter Pipeline

**Concept:** Automated flow from mining to ingot storage.

```
[Drills] → [Conveyors] → [Sorters] → [Arc Furnaces] → [Ingot Storage]
   ↑            ↓             ↓            ↓              ↓
[Power]    [Flow Ctrl]   [Hash Detect] [Idle Detect]  [Level Monitor]
```

### Smelter Array Automation

**Challenge:** Coordinate multiple furnaces efficiently.

**IC10 Script:** [auto-smelter-array.ic10](../examples/mining/auto-smelter-array.ic10)

**Key Features:**
1. Monitor each furnace's `Idle` state
2. Check ore availability (`Quantity` in slot 0)
3. Activate idle furnaces with ore
4. Deactivate empty furnaces
5. Kill switch for emergency stop

**Loop Through Furnaces:**
```ic10
# Iterate through 4 furnaces
beq rIndex 0 checkFurnace0
beq rIndex 1 checkFurnace1
beq rIndex 2 checkFurnace2
beq rIndex 3 checkFurnace3

checkFurnace0:
l rIdle furnace0 Idle
ls rOreQty oreStacker 0 Quantity
blez rOreQty deactivate0
blez rIdle main  # Furnace busy or idle with no ore
s furnace0 On 1
s furnace0 Activate 1
add rIndex rIndex 1
j main
```

### Recipe Management

**Alloy Smelting:**
```ic10
# Steel requires iron + carbon in specific ratio
# Iron:Slot0, Carbon:Slot1

define IRON_HASH -666742878
define CARBON_HASH 1582746610

# Check slots before smelting
ls r0 furnace 0 OccupantHash
seq r1 r0 IRON_HASH
ls r0 furnace 1 OccupantHash
seq r2 r0 CARBON_HASH

# Only activate if both present
and r3 r1 r2
s furnace On r3
```

---

## Full Mining Complex

### System Architecture

**Complete Mining Operation:**

```
┌─────────────────────────────────────────┐
│          MINING COMPLEX                  │
├─────────────────────────────────────────┤
│                                          │
│  [Power Generation]                      │
│       Solar/Battery                      │
│                                          │
│  [Extraction]      [Processing]          │
│  4x Mining Drill →  Sorters → Furnaces  │
│       ↓               ↓          ↓       │
│  [Transport]     [Storage]   [Ingot]     │
│  Conveyors      Ore Stackers  Stackers   │
│                                          │
│  [Control System]                        │
│  IC10 State Machine                      │
│  Status Display                          │
└─────────────────────────────────────────┘
```

### State Machine Control

**States:**
1. **IDLE** - Waiting for power/resources
2. **MINING** - Drill operation
3. **TRANSPORT** - Conveyor moving ore
4. **PROCESSING** - Smelting active
5. **EMERGENCY** - Low power shutdown

**IC10 Script:** [mining-complex-controller.ic10](../examples/mining/mining-complex-controller.ic10)

```ic10
# State machine for full mining complex
main:
l rPower battery Charge
blt rPower POWER_LOW emergencyState

beq rState STATE_IDLE stateIdle
beq rState STATE_MINING stateMining
beq rState STATE_TRANSPORT stateTransport
beq rState STATE_PROCESSING stateProcessing

stateIdle:
bge rPower POWER_HIGH startMining
j endTick

stateMining:
# Drill operation active
blt rPower POWER_MED backToIdle
# Check for transport trigger
j endTick

# ... (see full example for all states)
```

### State Transitions

```
           [Power > 70%]
    IDLE ──────────────→ MINING
       ↑                  ↓
       │             [Ore ready]
       │                  ↓
       │             TRANSPORT
       │                  ↓
       │            [Smelter ready]
       │                  ↓
       │──────────── PROCESSING
              [Power < 50% or Complete]

    [Power < 25%] → EMERGENCY (all off)
              ↑         ↓
              └─────────┘
          [Power > 50%]
```

---

## Performance Optimization

### Line Count Reduction

**Challenge:** IC10 max 128 lines.

**Techniques:**

**1. Use Batch Operations:**
```ic10
# Instead of:
s drill1 On 0
s drill2 On 0
s drill3 On 0
s drill4 On 0

# Use:
sb DRILL_HASH On 0  # 4 lines → 1 line
```

**2. Combine Conditions:**
```ic10
# Instead of:
bgt r0 r1 label
beq r0 r1 label

# Use:
sgt r2 r0 r1
sge r3 r0 r1
or r4 r2 r3
bnez r4 label
```

**3. Remove Redundant Checks:**
```ic10
# Before:
l r0 device On
beq r0 1 turnOn
beq r0 0 turnOff

# After:
beq r0 1 turnOn
j turnOff  # Implicitly 0
```

### Register Optimization

**Guidelines:**
- Use `r0-r9` for frequent access
- Use `r10-r15` for state/less frequent
- Reuse registers across operations
- Avoid unnecessary moves

**Example:**
```ic10
# Before:
l r0 battery Charge
move rPowerLevel r0

# After:
l rPowerLevel battery Charge  # Direct to target
```

### Yield Placement

**Challenge:** Max 128 instructions per tick.

**Strategy:** Place `yield` strategically to balance throughput and compliance.

**Common Patterns:**

**1. End of Loop:**
```ic10
main:
# ... up to 128 instructions ...
yield
j main
```

**2. After Each Major Operation:**
```ic10
main:
l r0 drill1 On
yield
l r1 drill2 On
yield
j main
```

**3. Conditional Yield:**
```ic10
# Count operations
add rOpCount rOpCount 1
bgt rOpCount 50 doYield
j continue

doYield:
move rOpCount 0
yield
j continue
```

---

## Advanced Patterns

### Template-Based Design

**Concept:** Create reusable templates for common operations.

**Example:** Mining State Machine Template
- [mining-state-machine.ic10](../examples/mining/mining-state-machine.ic10)

**Usage:**
1. Copy template
2. Define your states
3. Set thresholds
4. Implement state logic
5. Test and refine

### Error Handling

**Pattern:** Watchdog timer
```ic10
# Reset if no progress for N ticks
add rWatchdog rWatchdog 1
bgt rWatchdog MAX_WATCHDOG errorReset

# On successful operation
move rWatchdog 0

errorReset:
# Log error, reset state
move rState STATE_IDLE
move rWatchdog 0
```

### Multi-Mode Operation

**Pattern:** Configurable operation modes
```ic10
# Mode switch via display or lever
l rMode display Setting

beq rMode MODE_ECO ecoMode
beq rMode MODE_NORMAL normalMode
beq rMode MODE_MAX maxMode

ecoMode:
# Reduced power operation
j endTick

normalMode:
# Standard operation
j endTick

maxMode:
# Maximum throughput
j endTick
```

---

## Resources

### Local Examples
- [multi-drill-coordinator.ic10](../examples/mining/multi-drill-coordinator.ic10) - Power-aware coordination
- [conveyor-belt-controller.ic10](../examples/mining/conveyor-belt-controller.ic10) - Flow control
- [auto-smelter-array.ic10](../examples/mining/auto-smelter-array.ic10) - Smelter automation
- [mining-complex-controller.ic10](../examples/mining/mining-complex-controller.ic10) - Full system
- [mining-state-machine.ic10](../examples/mining/mining-state-machine.ic10) - Reusable template

### Related Guides
- [Beginner Automation Guide](mining-automation-beginner.md) - Foundation concepts
- [Base Design Guide](mining-base-design.md) - Physical layout
- [Equipment Reference](../knowledge/mining/equipment.md) - Device specs

### Patterns
- [State Machine Template](../examples/patterns/state-machine-template.ic10)
- [Hysteresis Template](../examples/patterns/hysteresis-template.ic10)
- [ore-stacker.ic10](../examples/manufacturing/ore-stacker.ic10)

---

## Summary

Advanced mining automation enables industrial-scale operations with minimal manual intervention. Master these techniques and you'll have ore flowing from mine to smelter while you focus on other aspects of your Stationeers base.

**Key Takeaways:**
1. Use batch operations to control multiple devices efficiently
2. Implement state machines for complex workflows
3. Monitor power and scale operation accordingly
4. Integrate extraction, transport, and processing
5. Optimize for line count and register usage

**Next Steps:**
- Design your mining complex layout
- Implement state machine control
- Test and refine each subsystem
- Expand to industrial scale

Happy automating!

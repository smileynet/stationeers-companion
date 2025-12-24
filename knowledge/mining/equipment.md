# Mining Equipment Reference

Complete guide to mining equipment in Stationeers.

## Overview

Mining equipment ranges from simple hand tools to automated industrial systems. This guide covers all player equipment and stationary devices for resource extraction.

## Hand Equipment (Player Tools)

### Hand Scanner

| Property | Value |
|----------|-------|
| **Type** | Passive scanner |
| **Slot** | Hand slot |
| **Power** | None (passive) |
| **Range** | ~20 meters |
| **Function** | Detects nearby ore deposits |

**Description:**
Essential tool for locating ore deposits. When equipped, displays nearby ore concentrations through visual indicators.

**Usage Tips:**
- Keep equipped while exploring
- Walk in grid patterns for coverage
- Higher density = richer deposit
- Note locations for base placement

**Prerequisites:**
- Crafted at workbench
- Low cost, high priority

---

### Mining Drill (Hand)

| Property | Value |
|----------|-------|
| **Type** | Active tool |
| **Slot** | Hand slot |
| **Power** | Battery operated |
| **Function** | Manually extract ore |

**Description:**
Portable drill for manual ore extraction. Faster than hand collection but requires player operation.

**Usage Tips:**
- Aim at ore vein
- Hold to drill
- Watch battery charge
- Drop ores into nearby storage

**Prerequisites:**
- Crafted at workbench
- Requires iron, electronics

**Best For:**
- Early game mining
- Small scale operations
- Precise extraction

---

### Jetpack

| Property | Value |
|----------|-------|
| **Type** | Movement equipment |
| **Slot** | Back slot |
| **Power** | Battery operated |
| **Function** | Vertical mobility |

**Description:**
While not mining equipment per se, jetpacks are essential for accessing ore deposits on cliffs, in pits, or underground.

**Usage Tips:**
- Essential for vertical mining
- Watch fuel/battery
- Combine with pressure suit

---

## Stationary Devices (IC10 Compatible)

### Mining Drill (Device)

| Property | Value |
|----------|-------|
| **Type** | Mining device |
| **Power** | High (passive) |
| **Automation** | IC10 compatible |
| **Logic Types** | On, Power, Setting |

**Description:**
Stationary drill that automatically extracts ore when placed on a deposit. Can be controlled via IC10.

**Logic Types:**
- `On` - Toggle drill on/off (0/1)
- `Power` - Current power state (read-only)
- `Setting` - Operation mode

**Automation Example:**
```ic10
# Basic drill control
alias drill d0
alias battery d1

l r0 battery Charge
bgt r0 40 activate
blt r0 30 deactivate
yield
j activate

activate:
s drill On 1
yield
j main

deactivate:
s drill On 0
yield
j main
```

**Setup Requirements:**
- Placed directly on ore deposit
- Connected to power network
- Storage nearby for output
- Optional IC10 control

**Best For:**
- Semi-automated mining
- Mid-game operations
- Reliable ore supply

---

### Large Mining Drill

| Property | Value |
|----------|-------|
| **Type** | Advanced mining device |
| **Power** | Very High |
| **Automation** | IC10 compatible |
| **Speed** | 2x standard drill |

**Description:**
Upgraded mining drill with faster extraction rate. Requires more power but produces ore more quickly.

**Logic Types:**
- Same as standard drill
- Additional efficiency modes

**Best For:**
- High volume production
- Established power grids
- Industrial operations

---

### Excavator

| Property | Value |
|----------|-------|
| **Type** | Industrial mining device |
| **Power** | Extreme |
| **Automation** | IC10 compatible |
| **Depth** | Deep mining capable |

**Description:**
Large-scale mining machine for deep ore extraction. Can access deep deposits that surface drills cannot reach.

**Logic Types:**
- `On` - Toggle operation
- `Power` - Power state
- `Setting` - Depth/target mode
- `Status` - Operation state

**Setup Requirements:**
- Substantial power infrastructure
- Deep mine shaft
- Heavy transport systems
- Advanced automation recommended

**Best For:**
- Deep ore access (50m+)
- Industrial scale operations
- Rare ore mining (uranium, cobalt)

**Automation Considerations:**
- Requires power management
- Conveyor systems for output
- State machine control recommended
- Safety interlocks critical

---

### Deep Miner

| Property | Value |
|----------|-------|
| **Type** | Automated endless mining |
| **Power** | Self-powering possible |
| **Automation** | IC10 recommended |
| **Complexity** | High |

**Description:**
Advanced mining system that continuously generates ore when properly configured. The ultimate in mining automation.

**Components:**
- Deep Miner Head
- Centrifuge (processing)
- Power generation
- Sorting system

**Logic Types:**
- Complex device with multiple modes
- Requires initialization sequence
- Batch operation support

**Setup Requirements:**
- Advanced IC10 knowledge
- Network configuration
- Device discovery (hash-based)
- Power management system

**Best For:**
- Endgame automation
- Passive ore generation
- Industrial complexes

**Community Resources:**
- [Fully Automated Deep Mining on One IC10](https://www.reddit.com/r/Stationeers/comments/1cuiubr/fully_automated_lowconfiguration_deep_mining_on/)
- [Automatic Deep Miner Control (Steam Workshop)](https://steamcommunity.com/sharedfiles/filedetails/?id=2886352385)

---

## Transport Equipment

### Conveyor Belt

| Property | Value |
|----------|-------|
| **Type** | Item transport |
| **Power** | Low |
| **Automation** | IC10 compatible |
| **Logic Types** | On, Mode |

**Description:**
Moves items from point A to point B. Essential for automated mining operations.

**Automation Tips:**
- Detect items with sensors
- Control flow rate with IC10
- Link to storage levels

**Example:**
```ic10
# Flow control based on storage
alias conveyor d0
alias stacker d1

l r0 stacker Setting
blt r0 90 stopConveyor
s conveyor On 1
yield
j main

stopConveyor:
s conveyor On 0
yield
j main
```

---

### Chute

| Property | Value |
|----------|-------|
| **Type** | Gravity transport |
| **Power** | None |
| **Automation** | Limited |
| **Function** | Vertical drop |

**Description:**
Simple vertical transport using gravity. No power required but limited direction.

**Best For:**
- Moving items downward
- Manual sorting systems
- Low-tech solutions

---

### Sorter / Digital Flip Flop

| Property | Value |
|----------|-------|
| **Type** | Item routing |
| **Power** | Low |
| **Automation** | IC10 essential |
| **Logic Types** | On, Mode, Setting |

**Description:**
Routes items based on hash (item type). Critical for automated ore sorting.

**Hash-Based Sorting:**
```ic10
define IRON_HASH -666742878
alias sorter d0

ls r0 sorter 0 OccupantHash
seq r1 r0 IRON_HASH
s sorter Mode r1
```

**Best For:**
- Ore classification
- Automated routing
- Multi-type storage

---

## Storage Equipment

### Stacker

| Property | Value |
|----------|-------|
| **Type** | Item storage |
| **Power** | Low |
| **Automation** | IC10 compatible |
| **Logic Types** | On, Setting, Mode |

**Description:**
Stores items in stacks. Essential for ore and ingot storage in mining operations.

**Automation Tips:**
- Monitor stack levels
- Route ores by hash
- Link to smelter input

**Example:**
```ic10
# Monitor and report level
alias stacker d0
alias display d1

l r0 stacker Setting
s display Setting r0
yield
j main
```

---

### Vending Machine

| Property | Value |
|----------|-------|
| **Type** | Configurable storage |
| **Power** | Low |
| **Automation** | IC10 compatible |
| **Function** | Access control |

**Description:**
Stores items with player access control. Useful for centralized mining depots.

---

## Power Equipment

### Battery (Large)

| Property | Value |
|----------|-------|
| **Type** | Power storage |
| **Capacity** | High |
| **Logic Types** | Charge, Power |

**Description:**
Essential for mining operations. Drills require substantial power.

**Sizing Guidelines:**
- Single drill: 1-2 large batteries
- Multi-drill: 4+ batteries or direct grid
- Deep miner: Dedicated power system

---

### Solar Panel

| Property | Value |
|----------|-------|
| **Type** | Power generation |
| **Output** | Varies by sun |
| **Best For** | Mars, Moon |

**Description:**
Renewable power for mining operations. Best on Mars and Moon.

---

### Generator

| Property | Value |
|----------|-------|
| **Type** | Fuel power |
| **Output** | Consistent |
| **Best For** | Venus, underground |

**Description:**
Reliable power regardless of conditions. Requires fuel (hydrocarbon, hydrogen, etc.)

---

## Equipment Progression

### Stage 1: Manual (Day 1-7)
- [ ] Hand Scanner
- [ ] Hand Mining Drill
- [ ] Pressure Suit
- [ ] Jetpack

### Stage 2: Basic Automation (Day 7-21)
- [ ] Stationary Mining Drill
- [ ] Battery Bank
- [ ] Solar Panels
- [ ] Sorter / Chute
- [ ] Stacker

### Stage 3: Industrial (Day 21+)
- [ ] Large Mining Drills (multiple)
- [ ] Conveyor System
- [ ] Excavator (optional)
- [ ] Advanced IC10 automation
- [ ] Arc Furnace Array

### Stage 4: Endgame
- [ ] Deep Miner System
- [ ] Self-Powering Operation
- [ ] Complex State Machine Control
- [ ] Full Processing Pipeline

## Related Resources

- [Ore Deposits Guide](ore-deposits.md) - Where to find ores
- [Manual Mining Techniques Guide](../../guides/mining-manual-techniques.md) - How to mine
- [Beginner Automation Guide](../../guides/mining-automation-beginner.md) - IC10 control
- [Mining Examples](../../examples/mining/) - Code examples

## Version Notes

Equipment specifications may change with game updates. This guide reflects Stationeers 1.0+.

- Last updated: Current game version
- Verify with [Stationeers Wiki](https://stationeers-wiki.com) for changes

# Harvie Automation Guide: Seeds & Fertilizer

> Complete guide to automating seed and fertilizer delivery for Stationeers harvesting systems, from beginner setups to advanced logistics networks.

## Overview

The **Harvie** automates planting and harvesting for Hydroponics Trays. It sits on top of a tray and handles:
- Planting seeds from its input slot
- Harvesting mature plants
- Outputting harvested items to chutes

### Critical Limitations

**Harvies cannot apply fertilizer.** Fertilizer must be placed in the Hydroponics Tray manually BEFORE the Harvie plants seeds. This is a fundamental game limitation that affects all automation strategies.

**Seed timing matters.** Plants reach maturity before generating seeds. If you harvest immediately when `Mature=1`, you lose seeds. Scripts must check `Seeding` state to wait for seed generation.

---

## Level 1: Manual/Semi-Automated (Early Game)

**Requirements**: No IC10, just basic construction

### Physical Setup

```
        [Power]
           │
    ┌──────┴──────┐
    │   HARVIE    │  ← Input slot: seeds
    │  ┌──────┐   │  ← Output slot: harvested items
    └──┤      ├───┘
       │ TRAY │      ← Fertilizer goes here before planting
       │      │      ← Water pipe connection
       └──────┘
           │
       [Chute]       ← Collects output
```

### Setup Steps

1. Build Hydroponics Tray (use the variant with data port)
2. Connect water piping (5-60°C water temperature)
3. Place Harvie on top of the tray
4. Connect power to Harvie (10W)
5. Optional: Connect chute to Harvie output

### Manual Workflow

1. Place fertilizer in Hydroponics Tray (optional but increases yield)
2. Load seeds into Harvie input slot (Slot 0)
3. Harvie automatically plants the seed
4. Wait for plant to grow and mature
5. Harvie automatically harvests when plant is ready
6. Collect output from chute or Harvie output slot
7. Repeat

### Tips for Early Game

- Start with fast-growing crops: Potato (~51 min), Soybean (~54 min)
- Ensure greenhouse has: 1-5% CO2, 25-200 kPa pressure, 20-30°C
- Grow lights or sunlight required (except mushrooms)
- One Harvie per tray - they don't share

---

## Level 2: Basic IC10 Automation (Mid Game)

**Requirements**: IC Housing, IC Chip, basic wiring

### What This Adds

- Automatic monitoring of plant growth states
- Proper seed collection timing
- Configurable behavior
- Control of 3 harvie/tray pairs per chip

### Device Wiring

```
IC Housing (with chip)
    │
    ├── d0: Hydroponics Tray 1
    ├── d1: Hydroponics Tray 2
    ├── d2: Hydroponics Tray 3
    ├── d3: Harvie 1
    ├── d4: Harvie 2
    └── d5: Harvie 3
```

### The Code

From [drclaw1188/stationeers_ic10](https://github.com/drclaw1188/stationeers_ic10):

```ic10
# Harvie Controller - Controls 3 harvie/tray pairs
# Author: Cows Are Evil

# === CONFIGURATION ===
# How many seeds to collect before harvesting fruit
# Set to 0 to skip seed collection entirely
define HARVESTSEEDS 5

# === CONSTANTS ===
define PLANTSLOT 0   # Plant slot in hydroponics
define INPUTSLOT 0   # Seed input slot in harvie

# Initialize
s db Setting 1       # Enable via Setting
move r10 HARVESTSEEDS
move r11 HARVESTSEEDS
move r12 HARVESTSEEDS

# === MAIN LOOP ===
start:
# Check each hydroponics/harvie pair
alias hydroponics d0
alias harvie d3
alias seeds r10
jal checkHydroponics

alias hydroponics d1
alias harvie d4
alias seeds r11
jal checkHydroponics

alias hydroponics d2
alias harvie d5
alias seeds r12
jal checkHydroponics

sleep 8              # Check every 8 seconds
j start

# === CHECK HYDROPONICS SUBROUTINE ===
checkHydroponics:
bdns hydroponics ra  # Skip if device not connected
bdns harvie ra

# Check if plant needs seeds (Seeding > 0)
ls r0 hydroponics PLANTSLOT Seeding
bgtz r0 getSeeds     # Plant is seeding, collect seeds

# Check if plant is mature
ls r0 hydroponics PLANTSLOT Mature
beq r0 -1 plant      # -1 means empty, try to plant
beqz r0 ra           # 0 means growing, do nothing
s harvie Harvest 1   # 1 means mature, harvest
j ra

# === PLANT SUBROUTINE ===
plant:
ls r0 harvie INPUTSLOT Quantity
beqz r0 ra           # No seeds available
l r0 hydroponics TotalMoles
beqz r0 ra           # No atmosphere in tray
l r0 db Setting
beqz r0 ra           # System disabled
s harvie Plant 1     # Plant the seed
move seeds HARVESTSEEDS  # Reset seed counter
j ra

# === SEED COLLECTION SUBROUTINE ===
getSeeds:
beqz seeds ra        # Collected enough seeds
s harvie Harvest 1   # Harvest seed
sub seeds seeds 1    # Decrement counter
j ra
```

### How It Works

1. **Seeding Check**: When `Seeding > 0`, plant has seeds ready - harvests them first
2. **Mature Check**: When `Mature = 1`, fruit is ready - harvests it
3. **Empty Check**: When `Mature = -1`, slot is empty - plants new seed
4. **Growing**: When `Mature = 0`, plant is growing - does nothing

The `HARVESTSEEDS` define controls how many seeds are collected per cycle. Set to 5 means it collects 5 seeds, then lets the plant fully mature for fruit.

### Seed Delivery Options

**Manual**: Load seeds into each Harvie input slot

**Basic Chute Network**:
```
[Seed Storage] → [Chute] → [Harvie Input]
```

---

## Level 3: Batch Operations (Mid-Late Game)

**Requirements**: Named devices, understanding of batch operations

### What This Adds

- Control 500+ harvies with ONE chip
- Organized naming system
- Fertilizer wait option
- Scalable design

### Naming Convention

Name your Harvies and matching Trays in sets:
- "Harvie Set 1" / "Tray Set 1" (or same name for both)
- "Harvie Set 2" / "Tray Set 2"
- etc.

### Device Setup

```
          [IC Housing]
              │
      ┌───────┴───────┐
      │  Data Network │
      └───────────────┘
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 Set 1     Set 2     Set 3
[H][H][H] [H][H][H] [H][H][H]
[T][T][T] [T][T][T] [T][T][T]
```

All devices connect to same data network - no direct d0-d5 wiring needed.

### The Code

From [Xon/stationeers-ic-scripts](https://github.com/Xon/stationeers-ic-scripts):

```ic10
# Harvie 500 Controller - CowsAreEvil 11/Apr/2023
# Control up to 511 harvies on separate cycles

# === CONFIGURATION ===
# Collect seeds? -1 = No, 0 = Yes
define GETSEEDS -1

# Wait for fertilizer before planting? 0 = No, 1 = Yes
define USEPOOP 1

# === SET NAMES ===
# Add your harvie set names here
# End list with "push 0"
push HASH("Harvie Set 1")
push HASH("Harvie Set 2")
push HASH("Harvie Set 3")
push HASH("Harvie Set 4")
push HASH("Harvie Set 5")
push HASH("Harvie Set 6")
push HASH("Harvie Set 7")
push HASH("Harvie Set 8")
push HASH("Harvie Set 9")
push HASH("Harvie Set 10")
push HASH("Harvie Set 11")
push HASH("Harvie Set 12")
push 0

# === CONSTANTS ===
alias setname r10
define HARVIE 958056199      # Harvie prefab hash
define TRAY -1841632400      # Hydroponics Tray hash

s db Setting 1

# === MAIN LOOP ===
reset:
move sp 0                    # Reset stack pointer

start:
yield
add sp sp 1
peek setname                 # Get current set name from stack
beqz setname reset           # If 0, restart from beginning

checkdevice:
# Check if any harvie in set is busy
lbn r0 HARVIE setname Activate Minimum
bnez r0 start                # Skip if busy

# Check plant status
lbns r0 TRAY setname 0 Mature Minimum
beq r0 -1 plant              # Empty? Try to plant
bne r0 1 start               # Not mature? Wait

# Check seeds before harvesting
lbns r0 TRAY setname 0 Seeding Minimum
blt r0 GETSEEDS start        # Wait for seeds if configured
sbn HARVIE setname Harvest 1 # Harvest!
j start

plant:
l r0 db Setting
beqz r0 start                # Disabled? Skip

# Check for seeds in harvie
lbns r0 HARVIE setname 0 Quantity Minimum
beqz r0 start                # No seeds? Skip

# Check for fertilizer if configured
lbns r0 TRAY setname 1 Quantity Minimum
blt r0 USEPOOP start         # No fertilizer? Skip if required

sbn HARVIE setname Plant 1   # Plant!
j start
```

### Key Features Explained

**`GETSEEDS`**: Controls seed harvesting
- `-1`: Never harvest seeds (just fruit)
- `0`: Wait for seeds before harvesting

**`USEPOOP`**: Fertilizer requirement
- `0`: Plant immediately when seeds available
- `1`: Wait for fertilizer in tray slot 1 before planting

**Batch Operations**:
- `lbn` / `sbn`: Read/write to all devices matching name hash
- `lbns`: Read from specific slot of matching devices
- Uses `Minimum` mode to check if ANY device in set needs attention

### Seed Delivery Network

```
                    [Seed Sorter]
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
  [Chute Set 1]    [Chute Set 2]    [Chute Set 3]
       │                 │                 │
   [Harvies]         [Harvies]         [Harvies]
```

Configure sorters to route seeds by hash to appropriate chute networks.

---

## Level 4: Advanced Chute Integration (Late Game)

**Requirements**: Full logistics understanding, multiple IC chips

### What This Adds

- Automatic output sorting by crop type
- Seed recirculation
- Hash-based item routing
- Centralized collection

### Full Logistics Layout

```
                         ┌─────────────────┐
                         │  SEED STORAGE   │
                         │ [Wheat][Corn].. │
                         └────────┬────────┘
                                  │
                         [Seed Distribution]
                                  │
       ┌──────────────────────────┼──────────────────────────┐
       ▼                          ▼                          ▼
   ┌───────┐                  ┌───────┐                  ┌───────┐
   │Harvie1│─┐                │Harvie2│─┐                │Harvie3│─┐
   │ Tray1 │ │                │ Tray2 │ │                │ Tray3 │ │
   └───────┘ │                └───────┘ │                └───────┘ │
             │                          │                          │
             └──────────────────────────┼──────────────────────────┘
                                        │
                              ┌─────────▼─────────┐
                              │   OUTPUT CHUTE    │
                              └─────────┬─────────┘
                                        │
                         ┌──────────────┼──────────────┐
                         ▼              ▼              ▼
                    [Seed Sort]   [Food Sort]    [Other]
                         │              │
                         ▼              ▼
                   ┌─────────┐    ┌─────────┐
                   │ Return  │    │ Kitchen │
                   │ to Farm │    │ Storage │
                   └─────────┘    └─────────┘
```

### The Code

From [drclaw1188/stationeers_ic10](https://github.com/drclaw1188/stationeers_ic10):

```ic10
# Harvie Automator 3 - With Chute Integration
# Automatic sorting and type detection

alias Chute d2

# === CROP HASHES ===
define HARVIE 958056199
define CORN 258339687
define CORNSEEDS -1290755415
define FERN 892110467
define FERNSEEDS -1990600883
define POTATO 1929046963
define POTATOSEEDS 1005571172
define PUMPKIN 1277828144
define PUMPKINSEEDS 1423199840
define RICE 658916791
define RICESEEEDS -1691151239
define SOYBEAN 1924673028
define SOYBEANSEEDS 1783004244
define TOMATO -998592080
define TOMATOSEEDS -1922066841
define WHEAT -1057658015
define WHEATSEEDS -654756733

alias ChuteHash r15

# === INITIALIZATION ===
reset:
move r8 -1

s Chute On 0
s Chute Setting 0
s Chute SettingOutput 0
ls ChuteHash Chute 0 OccupantHash
bnezal ChuteHash SetChute

# === MAIN LOOP ===
start:
yield

add r8 r8 1                  # Increment device index
add r9 r8 3                  # Harvie is 3 slots after tray
bgt r8 1 reset               # Cycle through d0, d1

# Check seeding or mature
ls r0 dr8 0 Seeding          # dr8 = dynamic register (d0 or d1)
sgtz r0 r0
ls r1 dr8 0 Mature
sgtz r1 r1
or r0 r0 r1
breqz r0 2
s dr9 Harvest 1              # dr9 = matching harvie

# Check empty and has seeds
ls r0 dr8 0 Occupied
seqz r0 r0                   # Not occupied = 1
ls r1 dr9 0 Quantity
and r0 r0 r1                 # Empty AND has seeds
breqz r0 2
s dr9 Plant 1

j start

# === CHUTE CONFIGURATION ===
SetChute:
s db Setting ChuteHash       # Display current hash

# Check if output is a known crop (not seeds)
seq r0 ChuteHash CORN
seq r1 ChuteHash FERN
or r0 r0 r1
seq r1 ChuteHash POTATO
or r0 r0 r1
seq r1 ChuteHash PUMPKIN
or r0 r0 r1
seq r1 ChuteHash RICE
or r0 r0 r1
seq r1 ChuteHash SOYBEAN
or r0 r0 r1
seq r1 ChuteHash TOMATO
or r0 r0 r1
seq r1 ChuteHash WHEAT
or r0 r0 r1

s Chute Mode r0              # Mode 0 = seeds route, Mode 1 = food route
yield
s Chute On 1
j ra
```

### Sorter Configuration

Sorters can be configured via IC10 or manually:

**For Seed Return**:
- Set sorter to Mode 0 (filter out)
- Configure hash filter for each seed type
- Seeds pass through, food diverts

**For Food Collection**:
- Set sorter to Mode 1 (filter in)
- Configure hash filter for each crop type
- Food diverts to storage, seeds pass through

---

## Level 5: Fertilizer Automation (Most Complex)

### The Challenge

**Harvies cannot apply fertilizer.** The fertilizer must be in the Hydroponics Tray's slot BEFORE the Harvie plants. This requires either:
1. Manual fertilizer application
2. Semi-automated workflow with `USEPOOP` wait

### Option 1: Composter Automation

Automate fertilizer production, then manually distribute.

From [Zappes/Stationeers](https://github.com/Zappes/Stationeers):

```ic10
# Composter Controller
# Devices:
#   d0 = Advanced Composter
#   d1 = Passive Vent (for waste gases)
#   d2 = Door (for gas management)

alias composter d0
alias vent d1
alias door d2

loop:
    jal checkDoor
    jal checkComposter
    yield
    j loop

# Close vent when door is open
checkDoor:
    l r0 door Open
    beqz r0 cdVentOn
    s vent On 0
    j cdDone
cdVentOn:
    s vent On 1
cdDone:
    j ra

# Activate when materials present
checkComposter:
    ls r0 composter 0 Occupied
    beqz r0 ccProcess
    s composter Activate 1
ccProcess:
    l r0 composter Quantity
    beqz r0 ccDone
    s composter Activate 1
ccDone:
    j ra
```

### Composter Room Setup

```
┌─────────────────────────────┐
│     COMPOSTER ROOM          │
│   (Separate atmosphere!)    │
│                             │
│  [Composter] → [Output Chute]
│       │                     │
│   [Materials ← [Input Chute]│
│    Input]                   │
│                             │
│  [Passive Vent]             │
│       │                     │
└───────┼─────────────────────┘
        ▼
    [Outside]
    (vents N2 + Volatiles)
```

**Warning**: Composters release nitrogen and volatiles. Must be in sealed room with exhaust!

### Option 2: USEPOOP Wait Pattern

Use the batch controller's fertilizer wait feature:

```ic10
define USEPOOP 1   # Wait for fertilizer
```

**Workflow**:
1. Composter produces fertilizer automatically
2. Player collects fertilizer from composter output
3. Player places fertilizer in each hydroponics tray
4. Harvie detects fertilizer and plants seed

This is semi-automated: the harvie won't plant until fertilizer is present.

### Fertilizer Effects

Fertilizer quality depends on composter input:

| Input Type | Effect |
|------------|--------|
| Biomass | +Uses (2 + biomass_ratio × 5) |
| Food | +Harvest Yield (1 + food_ratio × 1.5) |
| Decayed Food | +Growth Speed (1 + decay_ratio × 0.25) |

**Optimal mix**: Balance food for yield boost with some biomass for durability.

### Future-Proofing

The ability for Harvies to apply fertilizer is a commonly requested feature. Check patch notes for updates!

---

## Quick Reference

### Harvie Slots

| Slot | Name | Usage |
|------|------|-------|
| 0 | Import | Receives seeds for planting |
| 1 | Export | Receives harvested items |
| 2 | Hand | Internal harvester hand |

### Hydroponics Tray Slots

| Slot | Name | Usage |
|------|------|-------|
| 0 | Plant | The growing plant |
| 1 | Fertilizer | Fertilizer (apply before planting) |

### Key Logic Types

**Harvie (device reads/writes)**:
| Type | Read/Write | Values |
|------|------------|--------|
| Activate | R/W | Trigger action |
| Plant | W | 1 = plant seed |
| Harvest | W | 1 = harvest plant |
| On | R/W | Power state |

**Hydroponics Tray - Slot 0 (plant)**:
| Type | Read | Values |
|------|------|--------|
| Mature | R | -1=empty, 0=growing, 1=mature |
| Seeding | R | 0=no seeds, 1=has seeds |
| Growth | R | 0.0 to 1.0 |
| Occupied | R | 0/1 |

### Crop/Seed Hashes

| Crop | Crop Hash | Seed Hash |
|------|-----------|-----------|
| Wheat | -1057658015 | -654756733 |
| Corn | 258339687 | -1290755415 |
| Potato | 1929046963 | 1005571172 |
| Soybean | 1924673028 | 1783004244 |
| Rice | 658916791 | -1691151239 |
| Tomato | -998592080 | -1922066841 |
| Pumpkin | 1277828144 | 1423199840 |
| Fern | 892110467 | -1990600883 |

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Harvie not planting | No seeds in input | Load seeds into Slot 0 |
| Harvie not planting | USEPOOP=1, no fertilizer | Add fertilizer to tray |
| Losing seeds | Harvesting at Mature=1 | Wait for Seeding=1 |
| Plants dying | Wrong atmosphere | Check CO2, temp, pressure |
| Slow growth | No fertilizer | Optional: add fertilizer |
| Output backing up | Chute full | Add more storage/sorters |

---

## Sources

### Local Examples
- `examples/growing/harvie.ic10` - Batch controller (Xon)
- `examples/patterns/harvie_automator.ic10` - Simple 3-pair controller (drclaw1188)
- `examples/atmosphere/harvie_automator_3.ic10` - Advanced with sorting (drclaw1188)
- `examples/patterns/compostercontroller.ic10` - Composter automation (Zappes)
- `knowledge/farming/plants.md` - Plant requirements

### GitHub Repositories
- [Xon/stationeers-ic-scripts](https://github.com/Xon/stationeers-ic-scripts)
- [drclaw1188/stationeers_ic10](https://github.com/drclaw1188/stationeers_ic10)
- [Zappes/Stationeers](https://github.com/Zappes/Stationeers)

### Wiki & Community
- [Stationeers Wiki - Farming Guide](https://stationeers-wiki.com/Guide_(Farming))
- [Stationeers Wiki - Harvie](https://stationeers-wiki.com/Kit_(Harvie))
- [Stationeers Wiki - Advanced Composter](https://stationeers-wiki.com/Kit_(Advanced_Composter))
- [Steam Workshop - Harvie Controller](https://steamcommunity.com/sharedfiles/filedetails/?id=2378338405)
- [Steam Discussions - Harvie Tutorial](https://steamcommunity.com/app/544550/discussions/0/3114770913756213075/)

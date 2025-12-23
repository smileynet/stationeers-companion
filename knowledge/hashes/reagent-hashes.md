# Reagent & Item Hashes

Hashes for items and reagents, useful for slot operations and filtering.

## Usage with Slots

```ic10
# Read item hash from a slot
ls r0 device slotIndex OccupantHash

# Check if slot contains specific item
define TARGET_HASH -666742878  # Iron
ls r0 device 0 OccupantHash
seq r1 r0 TARGET_HASH          # r1 = 1 if iron
```

## Ores & Ingots

| Item | Hash | Notes |
|------|------|-------|
| Iron (Ore/Ingot) | -666742878 | Common metal |
| Gold | -409226641 | Precious metal |
| Copper | -1172078909 | Electrical |
| Silver | 687283565 | Precious metal |
| Nickel | 556601662 | Alloy component |
| Lead | -2002530571 | Heavy metal |
| Silicon | -1195893171 | Electronics |
| Cobalt | 1702246124 | Alloy component |
| Uranium | -208860272 | Nuclear fuel |
| Carbon | 1582746610 | Steel component |

## Alloys

| Item | Hash | Notes |
|------|------|-------|
| Steel | 1331613335 | Iron + Carbon |
| Electrum | 478264742 | Gold + Silver |
| Invar | -626453759 | Iron + Nickel |
| Constantan | 1731241392 | Copper + Nickel |
| Solder | -1206542381 | Lead + Tin |
| Waspaloy | 1787814293 | Super alloy |
| Stellite | -500544800 | Super alloy |
| Inconel | -586072179 | Super alloy |
| Hastelloy | 2019732679 | Super alloy |
| Astroloy | -1493155787 | Super alloy |

## Food & Organics

| Item | Hash | Notes |
|------|------|-------|
| Potato | -1657266385 | Crop |
| Tomato | 733496620 | Crop |
| Corn | 1550709753 | Crop |
| Wheat | -686695134 | Crop |
| Rice | 1951286569 | Crop |
| Soy | 1510471435 | Crop |
| Pumpkin | -1250164309 | Crop |
| Egg | 1887084450 | Animal product |
| Milk | 471085864 | Animal product |
| Flour | -811006991 | Processed |
| Biomass | 925270362 | Organic matter |

## Chemicals & Gases

| Item | Hash | Notes |
|------|------|-------|
| Oil | 1958538866 | Hydrocarbon source |
| Hydrocarbon | 2003628602 | Fuel/plastic base |
| Fenoxitone | -865687737 | Medical |

## Dyes & Colors

| Item | Hash | Notes |
|------|------|-------|
| Color Red | 667001276 | Spray paint |
| Color Green | 2129955242 | Spray paint |
| Color Blue | 557517660 | Spray paint |
| Color Yellow | -1430202288 | Spray paint |
| Color Orange | 1728153015 | Spray paint |

---

## Example: Ore Sorter

```ic10
# Check if centrifuge output is iron ore
define IRON_HASH -666742878
alias centrifuge d0
alias sorter d1

ls r0 centrifuge 0 OccupantHash
seq r1 r0 IRON_HASH
s sorter Output r1  # Route to iron storage if match
```

# Prefab & Item Hashes

Hash values for IC10 batch operations and slot operations in Stationeers.

## Overview

Hashes are numeric identifiers used to:
- **Batch operations** (`lb`, `sb`): Target all devices of a type on the network
- **Slot operations** (`ls`, `ss`): Identify items in device slots

## Reference Files

### [Device Hashes](device-hashes.md)

Prefab hashes for network devices, organized by category:
- Atmospheric devices (vents, pumps, sensors)
- Power devices (solar, batteries, generators)
- Logic devices (IC housing, memory, switches)
- Fabrication devices (furnaces, printers)
- Doors & airlocks
- Sensors
- Storage
- Displays

### [Reagent & Item Hashes](reagent-hashes.md)

Item hashes for slot operations:
- Ores & ingots
- Alloys
- Food & organics
- Chemicals & gases
- Dyes & colors

## Quick Usage

### Batch Operations (Devices)

```ic10
# Read from all devices of a type on network
lb r0 DEVICE_HASH LogicType BatchMode

# BatchMode: 0=Average, 1=Sum, 2=Minimum, 3=Maximum

# Write to all devices of a type
sb DEVICE_HASH LogicType value
```

**Example - Solar Panel Control:**
```ic10
define SOLAR_TRACKING -539224550
lb r0 SOLAR_TRACKING Ratio 0      # Average ratio
sb SOLAR_TRACKING Vertical 45     # Set all vertical angles
```

### Slot Operations (Items)

```ic10
# Read item hash from device slot
ls r0 device slotIndex OccupantHash

# Check if slot contains specific item
seq r1 r0 ITEM_HASH    # r1 = 1 if match
```

**Example - Ore Sorting:**
```ic10
define IRON_HASH -666742878
ls r0 centrifuge 0 OccupantHash
seq r1 r0 IRON_HASH
s sorter Output r1     # Route iron to specific output
```

## Finding Hashes

1. **In-game**: Use a Logic Writer connected to the device
2. **Wiki**: [Stationeers Wiki - Prefab Hashes](https://stationeers-wiki.com/Prefab_Hash)
3. **This reference**: Pre-compiled common hashes above

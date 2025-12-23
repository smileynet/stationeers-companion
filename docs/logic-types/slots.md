# Slot Logic Types

Properties accessed via `ls` (load slot) and `ss` (store slot) instructions for items in device slots.

## Syntax

```ic10
ls r0 device slotIndex LogicType   # Read from slot
ss device slotIndex LogicType r0   # Write to slot
```

## Common Slot Logic Types

### Item Identification

| Logic Type | Description | Unit |
|------------|-------------|------|
| OccupantHash | Prefab hash of item | Hash |
| Quantity | Stack count | Integer |
| MaxQuantity | Max stack size | Integer |
| PrefabHash | Same as OccupantHash | Hash |

### Item Condition

| Logic Type | Description | Range |
|------------|-------------|-------|
| Damage | Item damage | 0-1 (0=perfect) |
| Charge | Item charge (batteries) | J |
| Growth | Plant growth | 0-1 |
| Mature | Plant mature | Boolean |

### Suit/Helmet Slots (Worn Equipment)

| Logic Type | Description | Unit |
|------------|-------------|------|
| Pressure | Internal suit pressure | kPa |
| Temperature | Internal temperature | K |
| RatioOxygen | Suit O2 level | 0-1 |
| RatioCarbonDioxide | Suit CO2 level | 0-1 |
| Filtration | Filter efficiency | 0-1 |

### Manufacturing Slots

| Logic Type | Description | Unit |
|------------|-------------|------|
| Quantity | Items in slot | Integer |
| OccupantHash | Item type in slot | Hash |

## Slot Indices

Slot numbering varies by device:

### Storage Devices
| Slot | Description |
|------|-------------|
| 0-n | Storage slots (varies by size) |

### Furnaces
| Slot | Description |
|------|-------------|
| 0 | Input slot |
| 1 | Output slot |
| 2 | Fuel slot (some models) |

### Fabricators
| Slot | Description |
|------|-------------|
| 0 | Output slot |
| 1+ | Material slots |

### Character (via suit slot reader)
| Slot | Description |
|------|-------------|
| 0 | Back (jetpack, tank) |
| 1 | Suit |
| 2 | Helmet |
| 3 | Lungs (gas filter) |

## Examples

### Check if Slot is Empty
```ic10
alias storage d0
ls r0 storage 0 OccupantHash
beqz r0 slotEmpty          # Hash = 0 means empty
# Slot has item
j continue
slotEmpty:
# Handle empty slot
continue:
```

### Check Item Quantity
```ic10
alias chest d0
ls r0 chest 0 Quantity     # How many items in slot 0
ls r1 chest 0 MaxQuantity  # Max stack size
sub r2 r1 r0               # Space remaining
```

### Monitor Suit Status
```ic10
alias suitReader d0
ls r0 suitReader 1 Pressure         # Suit pressure
ls r1 suitReader 1 RatioOxygen      # Suit O2
ls r2 suitReader 2 RatioCarbonDioxide # Helmet CO2
```

### Check Plant Growth
```ic10
alias tray d0
ls r0 tray 0 Growth        # Growth progress (0-1)
ls r1 tray 0 Mature        # Is mature? (0/1)
bne r1 1 notReady
# Plant is ready to harvest
j harvest
notReady:
# Still growing
```

### Monitor Ore in Furnace
```ic10
alias furnace d0
ls r0 furnace 0 OccupantHash  # What ore is loaded
ls r1 furnace 0 Quantity      # How much ore
beqz r1 needOre               # Empty, need more
# Has ore, check output
ls r2 furnace 1 Quantity      # Output slot quantity
```

### Item Damage Check
```ic10
alias storage d0
ls r0 storage 0 Damage     # 0 = perfect, 1 = broken
sgt r1 r0 0.5              # Badly damaged?
bnez r1 needsRepair
```

## Batch Slot Operations

```ic10
lbs r0 hash slotIndex LogicType mode  # Batch slot read
sbs hash slotIndex LogicType value    # Batch slot write
```

### Example: Count Total Items
```ic10
define LOCKER_HASH 123456
lbs r0 LOCKER_HASH 0 Quantity 1   # Sum quantities in slot 0 of all lockers
```

## Notes

- Slot indices are 0-based
- OccupantHash = 0 means slot is empty
- Not all slot types support all logic types
- Character slots only accessible via Suit Slot Reader device
- Some slots are read-only (can't ss to them)

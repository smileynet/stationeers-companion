---
title: Logic Instructions
category: logic
description: Device I/O operations for reading and writing device values
---

# Logic Instructions

Read and write values to connected devices. These are the core instructions for interacting with the game world.

## Device Ports

IC Housing has 6 external device ports (d0-d5) and a self-reference (db):

| Port | Description |
|------|-------------|
| d0-d5 | External connected devices |
| db | Self (the IC Housing itself) |

## Basic Device I/O

### l (Load)
Reads a value from a device into a register.

**Syntax**: `l r? device logicType`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination register |
| device | d0-d5, db | Device port to read |
| logicType | name | Property to read (e.g., Temperature, Pressure) |

```ic10
alias sensor d0
l r0 sensor Temperature    # Read temperature from sensor
l r1 sensor Pressure       # Read pressure from sensor
l r2 db Setting            # Read this IC's Setting value
```

**Common readable properties**: Temperature, Pressure, RatioOxygen, RatioNitrogen, Power, On, Open, Charge

---

### s (Store)
Writes a value to a device property.

**Syntax**: `s device logicType value`

| Param | Type | Description |
|-------|------|-------------|
| device | d0-d5, db | Device port to write |
| logicType | name | Property to write |
| value | reg/num | Value to set |

```ic10
alias vent d1
s vent On 1               # Turn vent on
s vent On 0               # Turn vent off
s vent Setting 50         # Set target to 50
s vent Mode 1             # Set operating mode
```

**Common writable properties**: On, Open, Lock, Setting, Mode

---

## Slot Operations

Devices with inventory slots (centrifuges, lockers, etc.) can be read/written per-slot.

### ls (Load Slot)
Reads a value from a specific slot in a device.

**Syntax**: `ls r? device slotIndex logicType`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination register |
| device | d0-d5 | Device with slots |
| slotIndex | reg/num | Slot number (0-based) |
| logicType | name | Slot property to read |

```ic10
alias centrifuge d0
ls r0 centrifuge 0 OccupantHash    # Get item hash in slot 0
ls r1 centrifuge 0 Quantity        # Get item quantity
ls r2 centrifuge 0 MaxQuantity     # Get max stack size
```

**Common slot properties**: OccupantHash, Quantity, MaxQuantity, Damage, Charge

---

### ss (Store Slot)
Writes a value to a specific slot in a device.

**Syntax**: `ss device slotIndex logicType value`

| Param | Type | Description |
|-------|------|-------------|
| device | d0-d5 | Device with slots |
| slotIndex | reg/num | Slot number (0-based) |
| logicType | name | Slot property to write |
| value | reg/num | Value to set |

```ic10
alias locker d0
ss locker 0 Lock 1        # Lock slot 0
ss locker 0 Lock 0        # Unlock slot 0
```

---

## Reagent Operations

Read reagent contents from devices (used for things like mixing, filtering).

### lr (Load Reagent)
Reads a reagent value from a device.

**Syntax**: `lr r? device reagentMode reagentHash`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination register |
| device | d0-d5 | Device to read |
| reagentMode | reg/num | What to read (0=Contents, 1=Required, 2=Recipe) |
| reagentHash | reg/num | Hash of the reagent type |

```ic10
alias mixer d0
define WATER_HASH 123456
lr r0 mixer 0 WATER_HASH   # Read water contents in mixer
```

---

### sr (Store Reagent)
Writes a reagent value to a device.

**Syntax**: `sr device reagentMode reagentHash value`

| Param | Type | Description |
|-------|------|-------------|
| device | d0-d5 | Device to write |
| reagentMode | reg/num | What to write (0=Contents, 1=Required, 2=Recipe) |
| reagentHash | reg/num | Hash of the reagent type |
| value | reg/num | Value to set |

---

### rmap (Reagent Map)
Maps a reagent hash to its corresponding prefab hash. Used for looking up device prefabs from reagent types.

**Syntax**: `rmap destination device reagentHash`

| Param | Type | Description |
|-------|------|-------------|
| destination | register | Result register (receives prefab hash) |
| device | d0-d5 | Device to query |
| reagentHash | reg/num | Hash of the reagent type to look up |

```ic10
# Map water reagent to its prefab hash
define WATER_REAGENT_HASH 1234567890

alias reagentStorage d0
move rWaterHash WATER_REAGENT_HASH

# Get prefab hash for water
rmap rPrefabHash reagentStorage rWaterHash

# rPrefabHash now contains the device prefab hash for water
```

**Use Cases**:
- Finding device prefabs for reagent-based filtering
- Looking up stacker/pipe types from reagent types
- Converting between reagent and device identification systems

---

## Direct Register Operations

### ld (Load Device)
Reads from a device port specified by register value.

**Syntax**: `ld r? r? logicType`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination register |
| r? | register | Device index (0-5 for d0-d5) |
| logicType | name | Property to read |

```ic10
move r0 2                  # Device index 2 (d2)
ld r1 r0 Temperature       # Read Temperature from d2
```

**Use case**: Loop through multiple devices dynamically.

---

### sd (Store Device)
Writes to a device port specified by register value.

**Syntax**: `sd r? logicType value`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Device index (0-5) |
| logicType | name | Property to write |
| value | reg/num | Value to set |

```ic10
move r0 1                  # Device index 1 (d1)
sd r0 On 1                 # Turn on d1
```

---

## Common Patterns

### Read and React
```ic10
alias sensor d0
alias vent d1
define TARGET 101.325

l r0 sensor Pressure       # Read current pressure
sgt r1 r0 TARGET           # Is pressure > target?
s vent On r1               # Turn on if pressure too high
```

### Loop Through Devices
```ic10
move r0 0                  # Start at d0
loop:
ld r1 r0 Temperature       # Read from device[r0]
# ... process r1 ...
add r0 r0 1                # Next device
blt r0 6 loop              # Continue while r0 < 6
```

---

## See Also

- [logic-extended.md](logic-extended.md) - Advanced patterns and edge cases
- [batch.md](batch.md) - Network-wide device operations
- [../logic-types/readable.md](../logic-types/readable.md) - All readable logic types
- [../logic-types/writable.md](../logic-types/writable.md) - All writable logic types

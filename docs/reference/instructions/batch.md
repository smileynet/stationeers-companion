---
title: Batch Instructions
category: batch
description: Network-wide device operations using prefab hashes
---

# Batch Instructions

Operate on all devices of a type across the entire data network. Uses prefab hashes to identify device types.

## Key Concepts

### Prefab Hash
Each device type has a unique hash. Use these with batch operations:

| Device | Hash | Category |
|--------|------|----------|
| Active Vent | -842048328 | Atmospheric |
| Gas Sensor | 546126601 | Atmospheric |
| Solar Panel (Tracking) | -539224550 | Power |
| Battery (Large) | 683671518 | Power |

See [knowledge/hashes/device-hashes.md](../../../knowledge/hashes/device-hashes.md) for complete list.

### Batch Modes

When reading from multiple devices, you must specify how to aggregate:

| Mode | Value | Description |
|------|-------|-------------|
| Average | 0 | Mean of all values |
| Sum | 1 | Total of all values |
| Minimum | 2 | Smallest value |
| Maximum | 3 | Largest value |

---

## Basic Batch Operations

### lb (Load Batch)
Reads a value from all matching devices on the network.

**Syntax**: `lb r? hash logicType batchMode`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination register |
| hash | number | Device prefab hash |
| logicType | name | Property to read |
| batchMode | 0-3 | Aggregation mode |

```ic10
define SOLAR_PANEL -539224550

lb r0 SOLAR_PANEL Ratio 0      # Average efficiency of all panels
lb r1 SOLAR_PANEL Ratio 2      # Lowest panel efficiency
lb r2 SOLAR_PANEL Ratio 3      # Highest panel efficiency
```

```ic10
define LARGE_BATTERY 683671518

lb r0 LARGE_BATTERY Charge 1   # Total charge across all batteries
lb r1 LARGE_BATTERY Maximum 1  # Total capacity
div r2 r0 r1                   # Calculate overall percentage
mul r2 r2 100
```

---

### sb (Store Batch)
Writes a value to all matching devices on the network.

**Syntax**: `sb hash logicType value`

| Param | Type | Description |
|-------|------|-------------|
| hash | number | Device prefab hash |
| logicType | name | Property to write |
| value | reg/num | Value to set |

```ic10
define SOLAR_PANEL -539224550

sb SOLAR_PANEL Vertical 45     # Set all panels to 45° vertical
sb SOLAR_PANEL Horizontal 90   # Set all panels to 90° horizontal
sb SOLAR_PANEL On 1            # Turn on all panels
```

```ic10
define ACTIVE_VENT -842048328

sb ACTIVE_VENT On 0            # Turn off all active vents
sb ACTIVE_VENT Mode 1          # Set all vents to outward mode
```

---

## Named Batch Operations

Target devices by both hash AND name. The name is set on the device's label.

### lbn (Load Batch Named)
Reads from devices matching hash AND name hash.

**Syntax**: `lbn r? hash nameHash logicType batchMode`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination register |
| hash | number | Device prefab hash |
| nameHash | number | Hash of device name |
| logicType | name | Property to read |
| batchMode | 0-3 | Aggregation mode |

```ic10
define ACTIVE_VENT -842048328
define AIRLOCK_VENTS 12345     # Hash of "Airlock" label

lbn r0 ACTIVE_VENT AIRLOCK_VENTS Pressure 0   # Avg pressure from vents named "Airlock"
```

**Tip**: Use `HASH("name")` in-game to get name hashes.

---

### sbn (Store Batch Named)
Writes to devices matching hash AND name hash.

**Syntax**: `sbn hash nameHash logicType value`

| Param | Type | Description |
|-------|------|-------------|
| hash | number | Device prefab hash |
| nameHash | number | Hash of device name |
| logicType | name | Property to write |
| value | reg/num | Value to set |

```ic10
define LIGHT -1407015904
define ROOM_A 11111

sbn LIGHT ROOM_A On 1          # Turn on lights named "Room A"
```

---

## Slot Batch Operations

Operate on slots across all matching devices.

### lbs (Load Batch Slot)
Reads from a slot on all matching devices.

**Syntax**: `lbs r? hash slotIndex logicType batchMode`

| Param | Type | Description |
|-------|------|-------------|
| r? | register | Destination |
| hash | number | Device prefab hash |
| slotIndex | reg/num | Slot number |
| logicType | name | Slot property |
| batchMode | 0-3 | Aggregation mode |

```ic10
define CENTRIFUGE 1915566057

lbs r0 CENTRIFUGE 0 Quantity 1    # Total items in slot 0 across all centrifuges
```

---

### sbs (Store Batch Slot)
Writes to a slot on all matching devices.

**Syntax**: `sbs hash slotIndex logicType value`

```ic10
define LOCKER 1886693770

sbs LOCKER 0 Lock 1               # Lock slot 0 on all lockers
```

---

### lbns (Load Batch Named Slot)
Reads from slot on named devices.

**Syntax**: `lbns r? hash nameHash slotIndex logicType batchMode`

---

### sbns (Store Batch Named Slot)
Writes to slot on named devices.

**Syntax**: `sbns hash nameHash slotIndex logicType value`

---

## Common Patterns

### Solar Array Control
```ic10
define SOLAR_TRACKING -539224550
alias daylightSensor d0

l r0 daylightSensor Horizontal
l r1 daylightSensor Vertical

sb SOLAR_TRACKING Horizontal r0
sb SOLAR_TRACKING Vertical r1
```

### Battery Bank Monitoring
```ic10
define LARGE_BATTERY 683671518
alias display d0

lb r0 LARGE_BATTERY Charge 1      # Sum all charge
lb r1 LARGE_BATTERY Maximum 1     # Sum all capacity
div r2 r0 r1
mul r2 r2 100                     # Percentage

s display Setting r2
```

### Zone-Based Lighting
```ic10
define LIGHT -1407015904
define ZONE_A 12345
define ZONE_B 67890
alias motionA d0
alias motionB d1

l r0 motionA Activate
l r1 motionB Activate

sbn LIGHT ZONE_A On r0            # Zone A lights follow motion sensor A
sbn LIGHT ZONE_B On r1            # Zone B lights follow motion sensor B
```

---

## See Also

- [batch-extended.md](batch-extended.md) - Advanced patterns and edge cases
- [logic.md](logic.md) - Single device operations
- [knowledge/hashes/device-hashes.md](../../../knowledge/hashes/device-hashes.md) - Device hash reference

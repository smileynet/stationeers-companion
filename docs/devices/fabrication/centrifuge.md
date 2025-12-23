---
title: Centrifuge
category: fabrication
---

# Centrifuge

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Logic | Power |
| Logic | Error |
| Logic | Reagents |
| Logic | On |
| Logic | ImportCount |
| Logic | ExportCount |
| Logic | RequiredPower |
| Slot | Occupied |
| Slot | OccupantHash |
| Slot | Quantity |
| Slot | Damage |
| Slot | Class |
| Slot | MaxQuantity |
| Slot | PrefabHash |
| Slot | SortingClass |
| Slot | ReferenceId |

### Writable

| Logic Type | Description |
|------------|-------------|
| On | Boolean |
| Open | Boolean |
| Logic | ClearMemory |

## IC10 Example

```ic10
alias device d0  # Centrifuge
l r0 device Logic
s device On 1
```

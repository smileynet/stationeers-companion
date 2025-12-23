---
title: Locker
category: storage
prefab_hash: 1886693770
---

# Locker

Standard storage container for items. Accessible via IC10 for inventory automation.

**Prefab Hash**: `1886693770`

## Logic Types

### Readable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power state | Boolean |
| Open | Door is open | Boolean |
| Lock | Locked state | Boolean |
| Power | Has power connection | Boolean |
| Error | Error state | Boolean |
| PrefabHash | Device type identifier | Integer |
| ReferenceId | Unique device ID | Integer |
| RequiredPower | Power consumption | Watts |

### Writable

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| On | Power on/off | Boolean |
| Open | Open/close door | Boolean |
| Lock | Lock/unlock | Boolean |

## Slot Logic Types

Access items via `ls` (load slot) and `ss` (store slot):

| Logic Type | Description | Unit/Range |
|------------|-------------|------------|
| OccupantHash | Item prefab hash in slot | Integer |
| Quantity | Stack count in slot | Integer |
| MaxQuantity | Max stack size | Integer |
| Damage | Item damage (0=perfect) | 0-1 |

## Common Use Cases

### Check If Slot Has Items
```ic10
alias locker d0
ls r0 locker 0 Quantity  # Items in slot 0
bnez r0 hasItems
# Slot is empty
j continue
hasItems:
# Slot has items
continue:
```

### Count Total Items (All Slots)
```ic10
alias locker d0
alias rTotal r0
alias rSlot r1

move rTotal 0
move rSlot 0

countLoop:
ls r2 locker rSlot Quantity
add rTotal rTotal r2
add rSlot rSlot 1
blt rSlot 10 countLoop   # Locker has 10 slots
```

### Check For Specific Item
```ic10
alias locker d0
define TARGET_HASH 12345  # Replace with actual item hash

move r1 0                # Slot counter
searchLoop:
ls r0 locker r1 OccupantHash
beq r0 TARGET_HASH found
add r1 r1 1
blt r1 10 searchLoop     # Check all 10 slots
j notFound

found:
# Item found in slot r1
j end
notFound:
# Item not in locker
end:
```

## IC10 Example

```ic10
# Auto-lock locker when player is away
alias locker d0
alias motion d1          # Motion sensor

main:
l r0 motion Activate     # Someone nearby?
seqz r1 r0               # Invert: lock if no one
s locker Lock r1
yield
j main
```

## Notes

- Standard locker has 10 slots (0-9)
- Slot indices are 0-based
- OccupantHash = 0 means slot is empty
- Cannot directly move items via IC10 (use chutes/stackers)

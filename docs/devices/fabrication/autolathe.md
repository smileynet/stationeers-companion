---
title: Autolathe
category: fabrication
prefab_hash: -1753893214
---

# Autolathe

**Prefab Hash**: `-1753893214`

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| On | Boolean |
| 1 | Turns the device on. Also toggles the switch accordingly. |
| 1 | Starts purging of stored materials in the structure. Also pulls the lever accordingly. Without powering the structure it won't purge anything. |
| Activate | Boolean |
| 1 | Writing a 1 to the device starts the construction of the chosen item. If there are not enough materials inside the structure it will starts to fabricate the item anyway, but won't actually produce the item and won't consume any stored resources. |
| Lock | Boolean |
| 1 | Completely blocks any manual interaction with the structure. This doesn't inculdes interaction by logic. |
| ClearMemory | Boolean |
| On | Boolean |
| 1 | TheAutolatheis powered. This is the same as the physical red powerswitch located on the structure. |
| Open | Boolean |
| 1 | Output of theAutolatheis opened. This is the same as the physical lever located on the structure. |
| Activate | Boolean |
| 1 | The structure is currently producing something. |
| Power | Boolean |
| 1 | Can be read to return if the device is correctly powered or not, set via the power system, return 1 if powered and O if not. |
| Error | Boolean |
| 1 | 1 if device is in error state, otherwise 0. |
| Reagents | Integer |
| RequiredPower | Integer |
| CompletionRatio | Integer |
| ExportCount | Integer |
| ImportCount | Integer |
| PrefabHash | Integer |
| Referenceld | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| Open | Boolean |
| 1 | Clears the counter memory. Will set itself back to 0 when actioned. |
| RecipeHash | Integer |
| Lock | Boolean |
| 1 | 1 if device is locked, otherwise 0, can be set in most devices and prevents the user from access the values. |
| Power | Boolean |
| 1 | Can be read to return if the device is correctly powered or not, set via the power system, return 1 if powered and O if not. |
| RecipeHash | Integer |

## IC10 Example

```ic10
alias device d0  # Autolathe
l r0 device On
s device Open 1
```

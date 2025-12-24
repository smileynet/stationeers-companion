---
title: Autolathe
category: fabrication
prefab_hash: -1753893214
---

# Autolathe

**Prefab Hash**: `-1753893214`

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Device is powered on | Boolean |
| Open | Output hatch is open | Boolean |
| Activate | Device is currently producing something | Boolean |
| Power | Device is correctly powered | Boolean (1=powered, 0=not) |
| Error | Device is in error state | Boolean (1=error, 0=ok) |
| Lock | Device is locked (blocks manual interaction) | Boolean |
| ClearMemory | Clears counter memory | Boolean |
| Reagents | Number of stored reagents | Integer |
| RequiredPower | Power required for current operation | Watts |
| CompletionRatio | Fabrication completion progress | Float (0.0-1.0) |
| ExportCount | Number of items exported | Integer |
| ImportCount | Number of items imported | Integer |
| PrefabHash | Prefab hash of current recipe | Integer |
| ReferenceId | Reference ID for tracking | Integer |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| Open | Opens/closes output hatch | Boolean (1=open, 0=closed) |
| ClearMemory | Clears counter memory (sets to 0) | Boolean |
| RecipeHash | Set recipe to fabricate via prefab hash | Integer |
| Lock | Lock/unlock device (blocks manual interaction) | Boolean (1=locked, 0=unlocked) |
| Power | Turn device on/off | Boolean (1=on, 0=off) |
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

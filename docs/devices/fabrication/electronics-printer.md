---
title: Electronics Printer
category: fabrication
---

# Electronics Printer

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Power | Boolean |
| 1 | Powered |
| Open | Boolean |
| 1 | Opened |
| Error | Boolean |
| 1 | Error |
| Activate | Boolean |
| 1 | Active |
| Lock | Boolean |
| 1 | Locked |
| Reagents | Float |
| On | Boolean |
| 1 | On |
| RequiredPower | Integer |
| RecipeHash | Integer |
| CompletionRatio | Integer |
| ExportCount | Integer |
| ImportCount | Integer |
| PrefabHash | Integer |
| ReferenceId | Integer |
| NameHash | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| Open | Boolean |
| Activate | Boolean |
| Lock | Boolean |
| On | Boolean |
| RecipeHash | Integer |
| ClearMemory | Integer |

## IC10 Example

```ic10
alias device d0  # Electronics Printer
l r0 device Power
s device Open 1
```

---
title: Solar Panel
category: power
prefab_hash: 844961456
---

# Solar Panel

**Prefab Hash**: `844961456`

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| On | Boolean |
| Charge | W |
| Horizontal | degrees |
| Vertical | % |
| Maximum | W |
| Ratio |  |
| On | Boolean |

### Writable

| Logic Type | Description |
|------------|-------------|
| Horizontal | Degrees |
| Vertical | Degrees |

## IC10 Example

```ic10
alias device d0  # Solar Panel
l r0 device On
s device Horizontal 1
```

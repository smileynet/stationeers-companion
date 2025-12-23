---
title: Airlock Gate
category: doors
---

# Airlock Gate

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Lock | Boolean |
| Mode | Boolean |
| On | Boolean |
| Open | Boolean |
| Lock | Boolean |
| Mode | Boolean |
| On | Boolean |
| Open | Boolean |
| PrefabHash | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| Setting | Boolean |
| Setting | Boolean |

## IC10 Example

```ic10
alias device d0  # Airlock Gate
l r0 device Lock
s device Setting 1
```

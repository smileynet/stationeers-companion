---
title: Landing Pad
category: trading
description: Landing pad for trader shuttles
---

# Landing Pad

Platform for trader shuttle landings. Comes in different sizes for different shuttle tiers.

## Variants

| Size | Grid | Shuttle Tier | Notes |
|------|------|--------------|-------|
| 3x3 | 9 pieces | Small/Close | Basic traders |
| 5x5 | 25 pieces | Medium | More variety |
| 7x7 | 49 pieces | Large/Far | All traders |

## Components

| Piece | Purpose |
|-------|---------|
| Landing Pad Center | Central piece, required |
| Landing Pad Edge | Border pieces |
| Landing Pad Corner | Corner pieces |
| Landing Pad Data | Network connection, IC10 control point |

**Important**: The Landing Pad Data piece is where you connect cables and read/write logic types.

## Logic Types (via Landing Pad Data)

### Readable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Power` | 0/1 | Power state |
| `On` | 0/1 | Operating state |
| `Activate` | 0/1 | Activation state of center |

### Writable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `On` | 0/1 | Turn on/off |
| `Activate` | 1 | Accept incoming shuttle / release landed shuttle |
| `Vertical` | float | Adjust landing waypoint height (for underground pads) |

## IC10 Examples

### Basic Landing Trigger

```ic10
alias pad d0       # Landing Pad Data piece

# Activate landing
s pad Activate 1
```

### Automated Landing with Dish

```ic10
alias dish d0
alias pad d1

waitSignal:
l r0 dish SignalStrength
blt r0 0.94 waitSignal

# Signal locked, interrogate
s dish Activate 1

waitInterrog:
l r1 dish InterrogationProgress
blt r1 1 waitInterrog

# Ready to land
s dish TargetPadIndex 0    # This pad
s dish Activate 1          # Call trader
s pad Activate 1           # Accept landing

yield
j waitSignal
```

### Underground Pad Height Adjustment

```ic10
alias pad d0
define PAD_HEIGHT 10       # 10m above pad level

# Set vertical waypoint for underground base
s pad Vertical PAD_HEIGHT
```

## Network Requirements

All on same data network:
- Landing Pad Data piece
- Satellite Dish (any size)
- Computer with Communications Motherboard
- (Optional) Vending Machine

## Trader Behavior

1. **One trader per pad** at a time
2. **Trader waits** at orbital hold point until `Activate` received
3. **No new traders** until current one is released
4. **Release** landed trader with `Activate` again

## Prefab Hashes

| Device | Hash |
|--------|------|
| Kit (Landing Pad Small) | *Check Stationpedia* |
| Kit (Landing Pad Medium) | *Check Stationpedia* |
| Kit (Landing Pad Large) | *Check Stationpedia* |

*Note: Use in-game Labeler tool or Stationpedia for exact hashes*

## See Also

- [satellite-dish.md](satellite-dish.md) - Signal tracking
- Trader system wiki pages

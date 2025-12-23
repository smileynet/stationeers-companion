---
title: Satellite Dish
category: trading
description: Satellite dish for trader communication and signal tracking
---

# Satellite Dish

Used for detecting, tracking, and interrogating trader contacts in orbit.

## Variants

| Size | Power | Best For | Notes |
|------|-------|----------|-------|
| Small | Low | Fast scanning | Quick movement, lower interrogation power |
| Medium | Medium | Balanced | 256-byte internal stack memory |
| Large | High | Far contacts | Required for distant traders |

## Logic Types

### Readable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Power` | 0/1 | Power state |
| `On` | 0/1 | Operating state |
| `Error` | 0/1 | Error state |
| `Horizontal` | 0-360 | Current horizontal angle (degrees) |
| `Vertical` | 0-90 | Current vertical angle (degrees) |
| `SignalStrength` | -1 to 1 | Signal strength (-1 = no signal/moving, 0-1 = strength) |
| `SignalID` | int | Unique ID of detected contact (0 = none) |
| `InterrogationProgress` | 0-1 | Progress of current interrogation |
| `MinimumWattsToContact` | float | Minimum watts needed (-1 if not resolved) |
| `WattsReachingContact` | float | Actual watts reaching contact (-1 if not resolved) |

### Writable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `On` | 0/1 | Turn on/off |
| `Horizontal` | 0-360 | Set horizontal angle |
| `Vertical` | 0-90 | Set vertical angle |
| `Activate` | 1 | Trigger interrogation OR call trader to land |
| `TargetPadIndex` | 0+ | Select landing pad on network |
| `BestContactId` | int | Lock onto specific SignalID |

## Critical Notes

1. **SignalStrength returns -1** when:
   - No signal detected
   - Dish is still moving
   - Signal still resolving

2. **Activate has two functions**:
   - First call: Interrogate the current/locked contact
   - After interrogation: Call trader to landing pad

3. **Communication requires >94% signal strength** (~0.94)

4. **Line of sight required** - obstructions block signals

## Basic IC10 Examples

### Manual Dish Control

```ic10
alias dish d0
alias dialH d1     # Horizontal dial (0-360)
alias dialV d2     # Vertical dial (0-90)

main:
l r0 dialH Setting
s dish Horizontal r0

l r1 dialV Setting
s dish Vertical r1

l r2 dish SignalStrength
s db Setting r2    # Display signal strength

yield
j main
```

### Auto-Scan for Signals

```ic10
alias dish d0
define INC 15      # Scan increment (degrees)

alias sH r0
alias sV r1
move sH 0
move sV 0

scan:
s dish Horizontal sH
s dish Vertical sV
sleep 0.5

l r2 dish SignalStrength
bgt r2 0.5 found   # Signal detected!

add sH sH INC
blt sH 360 scan
move sH 0
add sV sV INC
blt sV 90 scan
move sV 0          # Full scan complete, restart
j scan

found:
l r3 dish SignalID
s db Setting r3    # Display signal ID
yield
j scan
```

### Lock and Interrogate

```ic10
alias dish d0
alias sigID r5

# Lock onto specific signal
s dish BestContactId sigID
s dish Activate 1  # Start interrogation

# Wait for completion
waitLoop:
l r0 dish InterrogationProgress
blt r0 1 waitLoop
yield

# Interrogation complete - can now call to land
s dish TargetPadIndex 0    # Land on pad 0
s dish Activate 1          # Call trader
```

## Prefab Hashes

| Device | Hash |
|--------|------|
| Kit (Satellite Dish Small) | *Check Stationpedia* |
| Kit (Satellite Dish Medium) | *Check Stationpedia* |
| Kit (Satellite Dish Large) | *Check Stationpedia* |

*Note: Use in-game Labeler tool or Stationpedia for exact hashes*

## Setup Requirements

1. Satellite dish on a data network
2. Same network as: Landing Pad, Communications Computer
3. Communications Motherboard in computer to view contacts
4. Clear sky visibility (no roof obstructions)

## See Also

- [landing-pad.md](landing-pad.md) - Landing pad control
- Trader system wiki pages

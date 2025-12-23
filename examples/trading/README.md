# Trading & Communications Examples

IC10 scripts for satellite dishes, traders, and landing pads.

## When You Need This

- Contacting traders for supplies
- Tracking satellite signals
- Automating landing procedures

## Difficulty

These are **advanced** scripts requiring:
- State machines
- Indirect register addressing (`rr<N>`)
- Multiple device coordination

| Script | Lines | Complexity |
|--------|-------|------------|
| `sky-scan.ic10` | High | Signal scanning |
| `stat-tracking.ic10` | High | Signal optimization |

## Key Concepts

**Satellite Dish Control:**
- Horizontal: 0-360° rotation
- Vertical: 0-90° elevation
- SignalStrength: -1 (none), 0-1 (signal)
- Must reach ~94% signal for communication

**Trader Workflow:**
1. Scan sky for signals
2. Lock onto signal (BestContactId)
3. Interrogate (Activate)
4. Wait for InterrogationProgress = 1
5. Call to landing pad (TargetPadIndex + Activate)

## Common Devices

- Satellite Dish (Small/Medium/Large)
- Landing Pad (3x3, 5x5, 7x7)
- Landing Pad Data piece
- Communications Motherboard (in computer)

## Start Here

1. Read `../../docs/devices/trading/satellite-dish.md` first
2. Try `sky-scan.ic10` for automated scanning
3. Build full trader controller for selection

## Prerequisites

Before attempting trading automation:
- Understand state machines (`../patterns/state-machine-template.ic10`)
- Know indirect registers (`../patterns/indirect-register.ic10`)
- Have landing pad properly networked

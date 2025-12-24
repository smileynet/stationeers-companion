# Orbital Flight Enhanced - Optimization Plan

## Problem

Original file `orbital-flight-enhanced.ic10` is 271 lines, exceeding 128-line limit by 143 lines.

## Recommended Solution: Multi-Chip Architecture

Given the complexity (7 modes, multiple destinations, cargo management), split into 3 IC10 chips:

### IC10 #1: Flight Controller (~80 lines)

**Purpose**: Main flight state machine

**Devices**:
- d0 = Automation (Rocket Controller)
- d1 = DisplayStatus (Status display)
- d6 = DestinationSelector (Dial - theoretical)

**Responsibilities**:
- Mode state machine (Landed, Launching, Traveling, InSpace, Returning, Returned)
- Destination selection
- Display coordination

**Communication**:
- Writes fuel commands to shared memory
- Writes module commands to shared memory
- Reads status from other chips

---

### IC10 #2: Fuel & Power Manager (~50 lines)

**Purpose**: Fuel monitoring and power management

**Devices**:
- d2 = FuelController (Fuel management)

**Responsibilities**:
- Fuel level monitoring
- Reserve calculation
- Return trip fuel tracking

**Communication**:
- Writes fuel status to shared memory
- Receives commands from Flight Controller

---

### IC10 #3: Cargo & Module Manager (~60 lines)

**Purpose**: Module and cargo coordination

**Devices**:
- d3 = ModuleOre (Ore mining)
- d4 = ModuleIce (Ice harvesting)
- d5 = ModuleSilo (Cargo storage)

**Responsibilities**:
- Module status monitoring
- Silo quantity tracking
- Import/export coordination

**Communication**:
- Writes cargo status to shared memory
- Receives commands from Flight Controller

---

## Shared Memory Layout

| Address | Purpose | Read By | Written By |
|---------|----------|-----------|-------------|
| 0 | Current Mode | All | Flight Controller |
| 1 | Fuel Status | Flight Controller | Fuel Manager |
| 2 | Ore Module Status | Flight Controller | Cargo Manager |
| 3 | Ice Module Status | Flight Controller | Cargo Manager |
| 4 | Silo Quantity | Flight Controller | Cargo Manager |
| 5 | Import/Export Status | Flight Controller | Cargo Manager |
| 6-7 | Destination (theoretical) | Flight Controller | Flight Controller |

---

## Implementation Benefits

1. **Fits within limits**: Each chip < 100 lines
2. **Clear separation**: Each chip manages specific subsystem
3. **Easier to debug**: Isolated concerns
4. **Reusable**: Sub-chips can be used independently

---

## Implementation Notes

### Theoretical / Unverified Features

The original file notes several theoretical/unverified features:
- `Destination` property on Automation (unverified)
- Dial functionality for destination selection
- Extended cargo management beyond standard silo operations

**Recommendation**: Verify these features in-game before implementing multi-chip solution.

### Version Compatibility

File notes deprecation of Automated Rocket Automation module.

**Recommendation**: Test all logic types in current game version before deployment.

---

## Files to Create

1. `examples/rockets/orbital-flight-main.ic10` - Flight Controller
2. `examples/rockets/orbital-fuel-manager.ic10` - Fuel & Power
3. `examples/rockets/orbital-cargo-manager.ic10` - Cargo & Modules

Original file preserved as: `orbital-flight-enhanced-original.ic10`

---

## Status

**Action Required**: Verify game features before implementation

This file has extensive theoretical content that needs in-game verification before splitting into multi-chip architecture.

**Recommendation**: Mark file as "THEORETICAL" in examples index and create working implementation once features are verified.

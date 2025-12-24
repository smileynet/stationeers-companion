# Launch Orchestrator - Multi-Chip Architecture

This document describes how to split the 250-line launch orchestrator into multiple IC10 chips that coordinate via batch operations.

## Problem

The original `launch-orchestrator.ic10` is 250 lines, exceeding the 128-line limit by 122 lines.

## Solution: Multi-Chip Architecture

Split into 3 IC10 chips communicating via batch operations (`sb` writes to shared prefab hashes):

### IC10 #1: Launch Orchestrator (~80 lines)

**Purpose**: Main state machine, countdown, abort handling

**Devices**:
- d0 = Automation (Rocket Controller)
- d5 = LaunchDisplay (Countdown display)
- d6 = StatusLED (Launch status indicator)
- d7 = AbortButton (Emergency abort)

**Responsibilities**:
- State machine (IDLE, PREFLIGHT, COUNTDOWN, LAUNCH, ABORTED)
- Countdown display
- Abort sequence
- LED status indication

**Communication**:
- Writes to `FUEL_CONTROLLER_HASH` Mode to trigger fuel operations
- Writes to `MODULE_HASH` Activate to control modules
- Reads from shared status variables via `lb`

---

### IC10 #2: Fuel Manager (~50 lines)

**Purpose**: Fuel level monitoring and coordination

**Devices**:
- d0 = FuelController (Fuel management IC)

**Responsibilities**:
- Monitor fuel levels
- Report fuel readiness to Orchestrator
- Handle refueling operations

**Communication**:
- Writes fuel status to shared memory address
- Receives commands from Orchestrator via batch reads

---

### IC10 #3: Module Manager (~60 lines)

**Purpose**: Module status monitoring and coordination

**Devices**:
- d2 = ModuleOre (Ore mining module)
- d3 = ModuleIce (Ice harvesting module)
- d4 = ModuleSilo (Cargo silo module)

**Responsibilities**:
- Monitor module states (Activate, Open)
- Report status to Orchestrator
- Handle module operations

**Communication**:
- Writes module status to shared memory
- Receives commands from Orchestrator via batch reads

---

## Communication Protocol

### Shared Memory Addresses

| Address | Purpose | Read By | Written By |
|---------|----------|-----------|-------------|
| 0 | Fuel Ready Status | Orchestrator | Fuel Manager |
| 1 | Ore Module Status | Orchestrator | Module Manager |
| 2 | Ice Module Status | Orchestrator | Module Manager |
| 3 | Silo Status | Orchestrator | Module Manager |

### Batch Operations

**Orchestrator writes**:
```ic10
# Tell fuel manager to prepare
sb FUEL_CONTROLLER_HASH Mode 1

# Tell modules to close
sb ORE_MODULE_HASH Activate 0
sb ICE_MODULE_HASH Activate 0
sb SILO_MODULE_HASH Open 0
```

**Fuel Manager writes**:
```ic10
# Report fuel ready (1=ready, 0=not ready)
# Use IC Housing's Setting as shared register
s db Setting 1
```

**Module Manager writes**:
```ic10
# Report module status
# Each module's Activate status
sb STATUS_HASH ModuleOreStatus r0
sb STATUS_HASH ModuleIceStatus r1
sb STATUS_HASH SiloStatus r2
```

---

## Implementation Benefits

1. **Fits within line limits**: Each chip < 100 lines
2. **Clear separation**: Each chip has single responsibility
3. **Reusable**: Fuel/Module managers can be used independently
4. **Easier to debug**: Smaller code, isolated concerns
5. **Parallel development**: Different chips can be developed independently

---

## Implementation Order

1. Create IC10 #3 (Module Manager) - Test independently
2. Create IC10 #2 (Fuel Manager) - Test independently
3. Create IC10 #1 (Launch Orchestrator) - Test with communication
4. Integration testing - All chips working together

---

## Files to Create

- `examples/rockets/launch-orchestrator-main.ic10` - Main orchestrator
- `examples/rockets/fuel-manager.ic10` - Fuel management
- `examples/rockets/module-manager.ic10` - Module coordination

Original file preserved as: `launch-orchestrator-original.ic10`

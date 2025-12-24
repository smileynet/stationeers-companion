---
title: Orbital Rocket
category: rockets
description: Orbital trading vessel for space mining and trading
---

# Orbital Rocket

Orbital rockets are used for automated trading, mining, and resource collection in space. They consist of a main automation controller housing (the "Rocket") with module slots for ore mining, ice harvesting, and cargo storage.

## Variants

| Size | Capacity | Module Slots | Notes |
|-------|-----------|---------------|-------|
| Small | Limited | 2-3 modules | Basic trading |
| Medium | Moderate | 4-5 modules | Standard operations |
| Large | High | 6+ modules | Full automation |

## Components

| Component | Purpose |
|-----------|---------|
| Rocket Housing | Main automation controller, contains Mode logic type |
| Ore Module | Auto-mines ore in orbit |
| Ice Module | Produces water/ice in orbit |
| Cargo Silo Module | Stores mined resources, configurable capacity |
| Thrusters | Propulsion for launch/orbit maneuvering |
| Fuel Tanks | Stores fuel for launch and return trips |

**Important**: The main Rocket Housing provides the network connection point for IC10 control.

## Logic Types

**Important**: The Automated Rocket Automation module is marked as **deprecated** on the [Stationeers Wiki](https://stationeers-wiki.com/Kit_(Automated_Rocket_Automation)). Verify logic types in-game before implementing.

### Readable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Mode` | Integer (0-7) | Current flight state (0=Idle on Pad, 1=Launching, 2=Traveling, 3=Arriving, 4=In Space, 5=Returning, 6=Returned, 7=Out of Fuel) |
| `Fuel` | Float | Current fuel amount in moles |
| `ReturnFuelCost` | Integer | Fuel required for return trip in moles |
| `CollectableGoods` | Boolean | Cargo available in orbit (1 = yes, 0 = no) |
| `ImportCount` | Integer | Number of imports to silo (internal counter) |
| `ExportCount` | Integer | Number of exports from silo (internal counter) |
| `Maximum` | Integer | Unknown purpose |
| `Setting` | Integer | Unknown purpose |
| `Ratio` | Float | Unknown purpose |
| `PrefabHash` | Integer | Structure hash identifier |
| `Open` | Boolean | Unknown purpose (possibly silo control) |

### Writable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Activate` | Integer | Trigger mode change: 1=Launch to Space, 2=Travel in Space, 4=Stop Traveling, 5=Return to Pad |
| `ClearMemory` | Boolean | Reset internal counters (ImportCount, ExportCount) when set to 1 |
| `Setting` | Float | Unknown purpose |
| `Open` | Boolean | Unknown purpose |

**Critical Note**: Setting `Activate` to the same value multiple times will not register changes. To avoid this, set to a "safe" value (0 or 1) first before triggering a new action.

## Flight Modes

| Mode | Value | Description |
|-------|--------|-------------|
| Landed | 0 | Rocket on launch pad, ready for operations |
| Launching | 1 | Launch sequence in progress |
| Traveling | 2 | En route to orbital destination |
| Arriving | 3 | Orbital insertion, preparing for operations |
| In Space | 4 | Main orbital operations (mining, trading) |
| Returning | 5 | Return trip initiated |
| Returned | 6 | Back on pad, mission complete |
| No Fuel | 7 | Emergency state, insufficient fuel |

## IC10 Examples

### Basic Mode Reading

```ic10
alias rocket d0

loop:
    l r0 rocket Mode
    # r0 now contains current flight mode
    # 0 = Landed, 4 = In Space, etc.
    yield
    j loop
```

### Launch Command

```ic10
alias rocket d0

# Initiate launch sequence
# Mode is READ-ONLY - use Activate to trigger launch
s rocket Activate 1  # Launch to space
```

### Return Fuel Check

```ic10
alias rocket d0

define FUEL_RESERVE 1.1  # 10% safety margin

checkReturnFuel:
    l r0 rocket ReturnFuelCost
    mul r0 r0 FUEL_RESERVE
    l r1 rocket Fuel
    ble r1 r0 initiateReturn

    # Sufficient fuel - continue operations
    j done

initiateReturn:
    # Not enough fuel - return now
    # Use Activate to trigger return (not Mode)
    s rocket Activate 5  # Return to launch pad

done:
    yield
    j checkReturnFuel
```

### Orbital Operation Check

```ic10
alias rocket d0

loop:
    l r0 rocket Mode
    beq r0 4 inSpace
    j main

inSpace:
    # Check for collectable goods
    l r0 rocket CollectableGoods
    beqz r0 main

    # Goods available - activate mining
    s oreModule Activate 1
    s iceModule Activate 1

main:
    yield
    j loop
```

## Network Requirements

Same data network:
- Rocket Housing (main controller)
- IC Housing(s) for flight/fuel control
- Module connections (Ore, Ice, Silo)
- (Optional) Status displays

## Module Integration

### Ore Module

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Activate` | 0/1 | Start/stop ore mining |
| `On` | 0/1 | Module operating state |

### Ice Module

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Activate` | 0/1 | Start/stop ice harvesting |
| `On` | 0/1 | Module operating state |

### Cargo Silo Module

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Activate` | 0/1 | Silo operations |
| `Open` | 0/1 | Open silo for access (1) or close for collection (0) |
| `Quantity` | float | Current silo contents |
| `ImportCount` | int | Number of imports to silo |
| `ClearMemory` | 0/1 | Reset silo memory (1 = reset) |

## Launch Sequence

A typical automated launch sequence:

1. **Pre-flight Check**
   - Verify `Mode` = 0 (on pad)
   - Verify `Fuel` > `ReturnFuelCost` * safety_margin
   - Ensure modules are inactive

2. **Countdown**
   - Display countdown (e.g., 10 seconds)
   - Use `sleep 1` between decrements

3. **Launch**
   - Set `Activate` = 1 (launch to space)
   - Set silo `ClearMemory` = 1
   - Activate modules on orbital insertion

## Return Sequence

Automated return requires:

1. **Fuel Check**
   - Read `ReturnFuelCost`
   - Apply safety margin (1.1x recommended)
   - Compare to current `Fuel`

2. **Initiate Return**
   - Set `Activate` = 5 (return to pad)
   - Deactivate all modules
   - Wait for landing

3. **Post-landing**
   - Rocket will be in `Mode` = 0 (idle on pad)
   - Open silo for unloading

## Prefab Hashes

| Device | Hash |
|--------|------|
| Kit (Rocket Orbital Small) | *Check Stationpedia* |
| Kit (Rocket Orbital Medium) | *Check Stationpedia* |
| Kit (Rocket Orbital Large) | *Check Stationpedia* |

*Note: Use in-game Labeler tool or Stationpedia for exact hashes*

## Best Practices

1. **Always include fuel reserves** - Use 1.1x to 1.2x safety margin for return fuel
2. **Mode-based dispatching** - Use `beq` to handle different flight states cleanly
3. **Module coordination** - Activate/deactivate modules based on `CollectableGoods` and silo capacity
4. **Countdown display** - Provide visual feedback during launch sequence
5. **Import tracking** - Monitor `ImportCount` for silo activity

## See Also

- [guides/rocketry-orbital-resources.md](../../../guides/rocketry-orbital-resources.md) - Orbital rocket automation guide
- [examples/patterns/flightcontroller.ic10](../../../examples/patterns/flightcontroller.ic10) - Complete flight controller
- [examples/patterns/fuelcontroller.ic10](../../../examples/patterns/fuelcontroller.ic10) - Fuel management
- [docs/devices/trading/landing-pad.md](../trading/landing-pad.md) - Landing pad infrastructure
- [docs/devices/trading/satellite-dish.md](../trading/satellite-dish.md) - Trading communications

## Notes

**Note**: Wiki documentation for "Rocket" does not exist. This documentation is based on IC10 code analysis and may be incomplete or inaccurate. Verify logic types and values in-game before implementing.

Orbital rocketry is endgame content. Recommend mastering:
- Basic IC10 programming
- State machine patterns
- Fuel management
- Trading system (satellite dish, landing pad)

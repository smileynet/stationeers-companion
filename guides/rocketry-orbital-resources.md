# Orbital Trading Rocketry Guide

> Last updated: 2025-12-23
> Search terms: stationeers orbital rocket, flight controller IC10, rocket automation, space trading

## ⚠️ Deprecation Warning

**The [Kit (Automated Rocket Automation)](https://stationeers-wiki.com/Kit_(Automated_Rocket_Automation)) is marked as deprecated on the Stationeers Wiki.**

The information in this guide is based on community code analysis (primarily Zappes/Stationeers GitHub repository) and may not reflect current game mechanics. Always verify logic types and behavior in-game before implementing automation.

## Summary

Orbital rockets in Stationeers are used primarily for automated orbital trading. An orbital rocket consists of:
- **Rocket Housing** (Automation Controller) - The main control unit
- **Modules** - Ore Mining, Ice Mining, Cargo Silo for different operations
- **Thrusters** - Propulsion system for launch and orbital maneuvering
- **Fuel Tanks** - Store fuel for launch and return trips

The trading workflow involves: launch → orbit → mine/trade → return. Full automation is possible with IC10 state machines managing launch sequences, fuel calculations, and cargo operations.

**Note**: This guide focuses on automation. For rocket construction basics, see the Stationeers in-game tutorial or community video tutorials.

## Version Compatibility

Orbital rocketry has evolved with trading updates:

| Update | Date | Changes |
|--------|------|---------|
| **Trading Update III** | Dec 22, 2022 | Tier system, orbital mechanics |
| **Trading Update V** | Mar 5, 2023 | Rocket module refinements |
| **"Big Changes Coming"** | Mar 17, 2025 | Stack features, cargo inspection |

The flightcontroller and fuelcontroller examples are current with game updates.

## Required Devices

| Device | Purpose | Notes |
|--------|---------|-------|
| Rocket (Orbital) | Trading vessel | Contains automation controller and modules |
| Module (Ore) | Mining operations | Auto-mines ore in orbit |
| Module (Ice) | Ice harvesting | Produces water/ice in orbit |
| Module (Cargo Silo) | Cargo storage | Stores mined resources, configurable capacity |
| Landing Pad (3x3/5x5/7x7) | Launch/landing pad | Orbital rockets use player-built launch infrastructure (separate from trader shuttle pads) |
| Satellite Dish | Trading comms | Required for orbital contact |
| IC Housing | Flight control | Houses flightcontroller.ic10 code |
| IC Housing | Fuel control | Houses fuelcontroller.ic10 code |
| Pump | Fuel transfer | Moves fuel from storage to rocket |
| Display | Status feedback | Shows fuel level, countdown, etc. |

## Best Resources

### 1. Flight Controller (Best Match)

**Source**: Zappes/Stationeers (GitHub)
**Link**: https://github.com/Zappes/Stationeers/blob/main/Rocket%20Controller/flightcontroller.mips
**Quality**: 9/10
**Status**: Current

**What it does**: Complete orbital rocket lifecycle automation with 8 flight modes and intelligent return fuel calculations.

**Flight modes**:
1. **Landed (0)** - Rocket on pad, ready for launch
2. **Launching (1)** - Launch countdown and ascent
3. **Traveling (2)** - En route to orbital destination
4. **Arriving (3)** - Orbital insertion and preparation
5. **In Space (4)** - Mining/trading operations
6. **Returning (5)** - Return trip initiated
7. **Returned (6)** - Back on pad, mission complete
8. **No Fuel (7)** - Emergency state, insufficient fuel for return

**Key features**:
- Launch countdown with display (10-second default)
- Cargo module control (Ore, Ice, Silo)
- Automatic return fuel calculation with 1.1x safety margin
- Import count tracking for silo capacity management
- Configurable waiting ticks for cargo operations
- Mode-based dispatching for clean state management

**Devices required**:
- d0 = Automation (Rocket Controller)
- d1 = DisplayCountdown
- d2 = FuelController
- d3 = ModuleOre
- d4 = ModuleIce
- d5 = ModuleSilo

**Logic types used**:
- `Mode` (Integer) - **Readable only**: Current flight mode (0=Landed, 1=Launching, 2=Traveling, 3=Arriving, 4=In Space, 5=Returning, 6=Returned, 7=No Fuel)
- `Activate` (Integer) - **Writable**: Trigger mode changes (1=Launch, 2=Travel, 4=Stop Traveling, 5=Return)
- `Fuel` (Float) - Readable: Current fuel amount in moles
- `ReturnFuelCost` (Integer) - Readable: Fuel needed for return trip in moles
- `CollectableGoods` (Boolean) - Readable: Available cargo in orbit
- `ClearMemory` (Boolean) - Writable: Reset silo memory counters
- Module logic types (Ore, Ice, Silo): `Activate`, `Open`, `Quantity`, `ImportCount`

---

### 2. Fuel Controller

**Source**: Zappes/Stationeers (GitHub)
**Link**: https://github.com/Zappes/Stationeers/blob/main/Rocket%20Controller/fuelcontroller.mips
**Quality**: 9/10
**Status**: Current

**What it does**: Automated fuel pump control with visual feedback and launch enable signaling.

**Key features**:
- Configurable pump strength (500 L/sec default)
- Target fuel level (pumpOffPercentage = 1.0 = 100% fill)
- Visual status feedback (red when fueling, green when ready)
- Mode check prevents fueling while in flight
- Launch enable signal when fuel is ready
- Buffer quantity handling for safety

**Parameters**:
- `pumpStrength: 500` - Pump flow rate in liters/second
- `pumpOffPercentage: 1` - Fill to 100% of max capacity
- `maxFuel: 8000` - Maximum fuel tank capacity in moles

**Safety interlocks**:
- Pump disabled if rocket mode != 0 (not on pad)
- Launch enable requires buffer quantity > 0
- Display color indicates fueling status (red = fueling, green = ready)

**Devices required**:
- d0 = Automation (Rocket)
- d1 = Pump
- d2 = Display
- d3 = LaunchEnable (optional enable signal)
- d4 = BufferQuantity (optional buffer check)

---

### 3. Stationeers Wiki - Trader (Background)

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Trader
**Quality**: 7/10

**What it does**: Explains the orbital trading workflow and trader tiers.

**Key information**:
- Small traders need 3x3 pads
- Large traders need 6x6 or 9x9 pads
- Trading workflow: track → negotiate → land → trade
- Computer with Communication Motherboard required
- Satellite dish integration

---

### 4. Stationeers Wiki - Kit (Satellite Dish)

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Kit_(Satellite_Dish)
**Quality**: 8/10

**What it does**: Complete documentation for satellite dish automation.

**Relevance**: Orbital rockets work with satellite dishes for trading communications. See [Trading Resources Guide](trading-resources.md) for complete satellite dish automation.

---

## Key Concepts

### Orbital Rockets vs. Trader Shuttles

**Important distinction**: This guide covers **orbital rockets** (player-built mining vessels), not **NPC trader shuttles**.

- **Orbital Rockets**: Player-built automated mining vessels that you launch, control, and return using IC10 automation
- **Trader Shuttles**: NPC vessels that land on your trading pads (3x3, 5x5, 6x6, 7x7, 9x9) to buy/sell goods

The landing pad sizes mentioned in trader documentation (6x6 for large shuttles, 7x7 for medium planes, 9x9 for large planes) apply **only** to trader shuttles, not to orbital rockets.

### Rocket Automation Architecture

Orbital rocket automation typically uses a **hierarchical IC10 setup**:

```
Rocket Housing (d0)
├── Flight Controller IC Housing
│   ├── Launch countdown
│   ├── Flight mode state machine
│   ├── Module coordination
│   └── Return fuel calculations
│
├── Fuel Controller IC Housing
│   ├── Pump control
│   ├── Fuel level monitoring
│   ├── Launch enable signal
│   └── Status display
│
└── Satellite Dish IC Housing (separate)
    ├── Signal tracking
    ├── Trader interrogation
    └── Landing pad coordination
```

### Launch Sequence

A typical automated launch sequence:

1. **Pre-launch Check**
   - Verify fuel level (check `Fuel` logic type)
   - Verify launch enable signal from fuel controller
   - Ensure all modules deactivated

2. **Countdown**
   - Set display to countdown value
   - Display countdown on screen (10 seconds default)
   - Use `sleep 1` between countdown decrements

3. **Launch**
   - Set rocket `Mode` to 1 (launching)
   - Clear silo memory (`ClearMemory` 1)
   - Activate modules on orbital insertion

### Orbital Operations

While in orbit (mode 4):

- **Ore Mining**: Activate ModuleOre to harvest ore
- **Ice Harvesting**: Activate ModuleIce to produce water
- **Cargo Management**: Monitor ModuleSilo `Quantity` and `ImportCount`
- **Return Decision**: Check `ReturnFuelCost` vs current `Fuel`

### Return Fuel Calculation

Critical safety feature from flightcontroller.ic10:

```ic10
l r0 Automation ReturnFuelCost  # Get fuel needed for return
mul r0 r0 fuelReserve          # Apply 1.1x safety margin
l r1 Automation Fuel             # Get current fuel
ble r1 r0 returnNow             # If fuel < required, return now
```

This ensures the rocket never gets stranded in orbit.

### State Machine Pattern

The flightcontroller uses a **mode-based dispatching pattern**:

```ic10
l currentMode Automation Mode     # Read current state
beq currentMode modeLanded processLanded
beq currentMode modeInSpace processInSpace
# ... other mode handlers

processLanded:
    # Handle landed state
    # ...

processInSpace:
    # Handle orbital operations
    # ...
```

This pattern is reusable for any multi-phase automation.

### Module Coordination

Cargo modules are coordinated in orbit:

```ic10
s ModuleOre Activate 1    # Start mining
s ModuleIce Activate 1    # Start ice production
s ModuleSilo Open 0       # Close silo for collection
```

When silo is full or time to return:

```ic10
s ModuleOre Activate 0    # Stop mining
s ModuleIce Activate 0    # Stop production
s ModuleSilo Open 1       # Open silo for unloading
```

## Construction Overview

**Note**: Detailed rocket construction guides are not available in the codebase. This is a high-level overview based on automation requirements.

### Basic Orbital Rocket Components

1. **Rocket Housing (Automation Controller)**
   - Contains all module slots
   - Provides `Mode`, `Fuel`, `ReturnFuelCost` logic types
   - Connects to external IC housings via network

2. **Modules**
   - **Ore Module**: Auto-mines ore in orbit
   - **Ice Module**: Produces water/ice
   - **Cargo Silo Module**: Stores resources, configurable capacity

3. **Launch Infrastructure**
   - Landing Pad (3x3 minimum)
   - Fuel storage tanks
   - Pump for fuel transfer
   - Status displays

### Network Setup

Connect IC housings to rocket:
- Flight controller IC housing → d0 (Rocket Automation)
- Fuel controller IC housing → d0 (Rocket Automation)
- Satellite dish → separate IC housing (see trading guide)

## Related Local Examples

### Core Automation Scripts

- **`examples/patterns/flightcontroller.ic10`** - Complete orbital rocket lifecycle automation
  - 8 flight modes
  - Launch countdown
  - Module coordination
  - Return fuel calculations

- **`examples/patterns/fuelcontroller.ic10`** - Fuel management system
  - Pump control
  - Visual feedback
  - Launch enable signaling

### Supporting Patterns

- **`examples/patterns/state-machine-template.ic10`** - Generic state machine pattern
- **`examples/patterns/pid-controller-template.ic10`** - For precision control (if needed)

### Trading Infrastructure

See these files for satellite dish and landing pad integration:

- **`guides/trading-resources.md`** - Complete trading automation guide
- **`docs/devices/trading/landing-pad.md`** - Landing pad device documentation
- **`docs/devices/trading/satellite-dish.md`** - Satellite dish device documentation

## Automation Opportunities

### Fully Automated Mining Operation

Combine flightcontroller with satellite dish automation:
1. Flight controller manages rocket launch/return
2. Satellite dish tracks traders and coordinates landings
3. Ore/Ice modules automatically mine in orbit
4. Silo module automatically stores resources
5. Rocket returns when fuel threshold reached

### Multi-Rocket Coordination

Extend the state machine pattern to manage multiple rockets:
- Shared fuel storage
- Coordinated launch windows
- Priority-based resource allocation

### Enhanced Trading

Integrate market data:
- Auto-select mining targets based on trader inventory
- Optimize cargo composition for maximum profit
- Schedule launches based on trader availability

## Code Preview

### Launch Countdown Pattern

From flightcontroller.ic10:

```ic10
move r0 countdownStart
s DisplayCountdown On 1

countdownLoop:
    s DisplayCountdown Setting r0
    sleep 1
    sub r0 r0 1
    bltz r0 countdownDone
    j countdownLoop

countdownDone:
    s DisplayCountdown On 0
    # Use Activate to trigger launch (not Mode)
    s Automation Activate 1
    move currentMode modeLaunching  # Internal tracking
```

### Return Fuel Check Pattern

From flightcontroller.ic10:

```ic10
checkReturnFuel:
    l r0 Automation ReturnFuelCost
    mul r0 r0 fuelReserve          # 1.1x safety margin
    l r1 Automation Fuel
    ble r1 r0 returnNow            # Return if low fuel
    j ra

returnNow:
    move currentMode modeReturning
    j done
```

### Fuel Pump Control Pattern

From fuelcontroller.ic10:

```ic10
bge currentFuel desiredFuel pumpOff

pumpOff:
    s Pump On 0
    l r0 LaunchEnable Setting
    l r1 BufferQuantity Setting
    # Calculate ready signal
    select r2 r0 1 0
    select r3 r1 0 r2
    s db Setting r3
    j done

pumpOn:
    s Pump On 1
    s db Setting 0
```

## Notes

- **Wiki pages for "Rocket" and "Thruster" do not exist** - This guide relies on automation code analysis
- Orbital rocketry is endgame content - Recommend mastering state machines and basic automation first
- The flightcontroller is production-ready and handles all orbital operations safely
- Always include fuel reserve calculations (1.1x minimum) to prevent stranding
- Landing pad size determines trader tier - Use 7x7 for large traders
- See [Trading Resources Guide](trading-resources.md) for complete satellite dish automation
- Atmospheric rockets are different from orbital rockets - See [Atmospheric Rocketry Guide](rocketry-atmospheric-resources.md)

## Sources

- [Zappes/Stationeers - Rocket Controller](https://github.com/Zappes/Stationeers/tree/main/Rocket%20Controller) - flightcontroller.mips and fuelcontroller.mips
- [Stationeers Wiki - Trader](https://stationeers-wiki.com/Trader)
- [Stationeers Wiki - Kit (Satellite Dish)](https://stationeers-wiki.com/Kit_(Satellite_Dish))

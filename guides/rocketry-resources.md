# Rocketry Resources Guide

> Last updated: 2025-12-24
> Search terms: rocket, fuel, engine, launch, countdown, orbital, atmospheric, IC10 automation

## ⚠️ Deprecation Warning

**The [Kit (Automated Rocket Automation)](https://stationeers-wiki.com/Kit_(Automated_Rocket_Automation)) is marked as deprecated on the Stationeers Wiki.**

The information in this guide is based on community code analysis and may not reflect current game mechanics. Always verify logic types and behavior in-game before implementing automation.

## Summary

Rocketry automation in Stationeers is primarily focused on **orbital trading rockets** for automated mining and resource collection. Community resources include production-ready flight controllers, fuel management systems, and launch sequencers. **Atmospheric rocketry** has minimal documentation and requires community development.

**Two distinct rocket types:**
1. **Orbital Rockets** - Player-built automated mining/trading vessels
2. **Atmospheric Rockets** - Surface transport (minimal documentation)
3. **Trader Shuttles** - NPC trading vessels (separate system - see [Trader page](https://stationeers-wiki.com/Trader))

## Best Resources

### 1. Rocket Controller (Orbital Flight Automation)

**Source**: Zappes/Stationeers (GitHub)
**Link**: https://github.com/Zappes/Stationeers/tree/main/Rocket%20Controller
**Quality**: 9/10
**Last Updated**: 2024
**Status**: Current

**What it does**: Complete orbital rocket lifecycle automation with 8 flight modes, launch countdown, module coordination, and intelligent return fuel calculations.

**Key features**:
- Launch countdown with display (10-second default)
- 8 flight modes (Landed, Launching, Traveling, Arriving, In Space, Returning, Returned, No Fuel)
- Automatic return fuel calculation with 1.1x safety margin
- Cargo module control (Ore, Ice, Silo)
- Import count tracking for silo capacity management
- Configurable waiting ticks for cargo operations

**Devices required**:
- d0 = Automation (Rocket Controller)
- d1 = DisplayCountdown
- d2 = FuelController
- d3 = ModuleOre
- d4 = ModuleIce
- d5 = ModuleSilo

**Logic types used**:
- `Mode` (Integer) - **Readable only**: Current flight mode (0-7)
- `Activate` (Integer) - **Writable**: Trigger mode changes (1=Launch, 2=Travel, 4=Stop, 5=Return)
- `Fuel` (Float) - Readable: Current fuel in moles
- `ReturnFuelCost` (Integer) - Readable: Fuel needed for return
- `CollectableGoods` (Boolean) - Readable: Cargo available in orbit
- Module logic types: `Activate`, `Open`, `Quantity`, `ImportCount`, `ClearMemory`

---

### 2. Fuel Controller (Orbital Rocket)

**Source**: Zappes/Stationeers (GitHub)
**Link**: https://github.com/Zappes/Stationeers/tree/main/Rocket%20Controller
**Quality**: 9/10
**Last Updated**: 2024
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

### 3. ARM Rocket (Atmospheric/Surface)

**Source**: exca/Stationeers-IC10-Automation (GitHub)
**Link**: https://github.com/exca/Stationeers-IC10-Automation/tree/main/ARM%20Rocket
**Quality**: Unknown (needs review)
**Last Updated**: Unknown
**Status**: Needs verification

**What it does**: Likely an atmospheric rocket or surface-to-orbit launch vehicle automation. The "ARM" designation suggests Autonomous Rocket Management.

**Note**: This was found in the repository directory listing but requires deeper investigation to verify functionality and version compatibility.

---

### 4. Stationeers Wiki - Trader (Orbital Trading)

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Trader
**Quality**: 7/10
**Status**: Current

**What it does**: Explains the orbital trading workflow and trader tiers.

**Key information**:
- Small traders need 3x3 pads
- Large traders need 6x6 or 9x9 pads
- Trading workflow: track → negotiate → land → trade
- Computer with Communication Motherboard required
- Satellite dish integration

---

### 5. Stationeers Wiki - Kit (Satellite Dish)

**Source**: Stationeers Wiki
**Link**: https://stationeers-wiki.com/Kit_(Satellite_Dish)
**Quality**: 8/10
**Status**: Current

**What it does**: Complete documentation for satellite dish automation.

**Relevance**: Orbital rockets work with satellite dishes for trading communications. See [Trading Resources Guide](trading-resources.md) for complete satellite dish automation.

---

### 6. Guide: How to Program Anything with an IC10 for the Novice

**Source**: Steam Community
**Link**: https://steamcommunity.com/sharedfiles/filedetails/?id=3288129161
**Quality**: 8/10
**Published**: July 14, 2024
**Status**: Current

**What it does**: Comprehensive IC10 programming tutorial covering fundamentals applicable to rocket automation.

**Relevance**: Found while searching for rocket scripts, this guide provides foundational IC10 knowledge for building custom rocket controllers.

---

## Local Examples (Based on Zappes/Stationeers)

The following examples are adapted from the Zappes/Stationeers repository and included in this codebase:

### Orbital Rocketry Examples

| Example | Description | Path |
|---------|-------------|------|
| **orbital-flight-enhanced** | Enhanced orbital flight controller with destination selection and advanced cargo management | `examples/rockets/orbital-flight-enhanced.ic10` |
| **launch-orchestrator** | Complete launch sequence with pre-flight checks, countdown, and abort handling | `examples/rockets/dispatch-orchestrator.ic10` |
| **rocket-state-machine** | Generic 8-mode state machine template for custom rocket operations | `examples/patterns/rocket-state-machine.ic10` |
| **launch-countdown** | Reusable launch countdown timer with display integration | `examples/patterns/launch-countdown.ic10` |
| **fuel-manager** | Automated fuel pump control with visual feedback | `examples/patterns/fuel-manager.ic10` |

### Key Features in Local Examples

**orbital-flight-enhanced.ic10**:
- Multiple destination support (Luna, Mars, Deep Space orbits)
- Extended cargo management with silo capacity tracking
- Advanced state tracking with import change detection
- Color-coded status display (Green/Red/Blue/Orange)

**launch-orchestrator.ic10**:
- Pre-flight check system (5 safety checks)
- Emergency abort sequence
- LED status indicators (Off/Yellow/Green/Red)
- Error code display (99 for preflight failure)

---

## Version Compatibility

| Resource | Last Updated | Status |
|----------|--------------|--------|
| Zappes/Stationeers Rocket Controller | 2024 | Current |
| Zappes/Stationeers Fuel Controller | 2024 | Current |
| exca/Stationeers-IC10-Automation ARM Rocket | Unknown | Needs Verification |
| Stationeers Wiki - Trader | 2024 | Current |
| Stationeers Wiki - Satellite Dish | 2024 | Current |
| Steam Workshop - IC10 Guide | 2024 | Current |

**Note**: Orbital rocketry scripts from before December 2022 may not support the tier system introduced in Trading Update III. Always verify scripts use `ReturnFuelCost` logic type.

---

## Key Concepts

### Orbital Rockets vs. Trader Shuttles

**Important distinction**: Rocketry in Stationeers includes three separate systems:

1. **Orbital Rockets**: Player-built automated mining vessels
   - You build and launch these
   - Controlled via IC10 automation
   - Use your own launch infrastructure
   - For mining ore/ice in orbit

2. **Trader Shuttles**: NPC trading vessels
   - **NOT** player-built or player-controlled
   - Land on your trading pads
   - Use landing pad sizes: 3x3 (small), 5x5 (medium), 6x6 (large VTOL), 7x7 (medium plane), 9x9 (large plane)
   - Controlled via satellite dish + computer
   - For buying/selling goods with NPC traders

**The landing pad sizes (6x6, 7x7, 9x9) mentioned in some documentation apply to TRADER SHUTTLES, not orbital rockets.**

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

Critical safety feature:

```ic10
l r0 Automation ReturnFuelCost  # Get fuel needed for return
mul r0 r0 1.1                   # Apply 1.1x safety margin
l r1 Automation Fuel            # Get current fuel
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

---

## Required Devices (Orbital)

| Device | Purpose | Notes |
|--------|---------|-------|
| Rocket (Orbital) | Trading vessel | Contains automation controller and modules |
| Module (Ore) | Mining operations | Auto-mines ore in orbit |
| Module (Ice) | Ice harvesting | Produces water/ice in orbit |
| Module (Cargo Silo) | Cargo storage | Stores mined resources, configurable capacity |
| Landing Pad (3x3/5x5/7x7) | Launch/landing pad | Size determines trader tier |
| Satellite Dish | Trading comms | Required for orbital contact |
| IC Housing | Flight control | Houses flightcontroller.ic10 code |
| IC Housing | Fuel control | Houses fuelcontroller.ic10 code |
| Pump | Fuel transfer | Moves fuel from storage to rocket |
| Display | Status feedback | Shows fuel level, countdown, etc. |

---

## Alternative Approaches

### Single IC Housing (Simplified)

Combine flight and fuel control into one IC housing:
- **Pros**: Fewer devices, simpler setup
- **Cons**: More complex code, harder to debug

### Manual Launch with Automated Return

- Use manual launch commands
- Automate only orbital operations and return
- **Pros**: Launch on demand, automatic return when ready
- **Cons**: Not fully autonomous

### Scheduled Launch System

Add time-based launch scheduling:
- Launch at regular intervals (e.g., every 30 minutes)
- Coordinate with trader availability
- Requires real-time clock or tick counter

---

## Tutorials & Guides

| Title | Source | Description |
|-------|--------|-------------|
| [How to Program Anything with an IC10 for the Novice](https://steamcommunity.com/sharedfiles/filedetails/?id=3288129161) | Steam Workshop | Comprehensive IC10 programming tutorial (July 2024) |
| [Trader](https://stationeers-wiki.com/Trader) | Stationeers Wiki | Orbital trading workflow and tier system |
| [Kit (Satellite Dish)](https://stationeers-wiki.com/Kit_(Satellite_Dish)) | Stationeers Wiki | Satellite dish automation documentation |

---

## Community Discussions

No specific rocketry discussions were found in recent Reddit r/stationeers searches. Most discussion appears to be on GitHub repositories and Steam Workshop guides.

---

## Atmospheric Rocketry (Limited Resources)

**Warning: Minimal Community Resources**

Atmospheric rocketry in Stationeers has minimal community documentation. No dedicated wiki pages, IC10 examples, or comprehensive guides exist.

### Current Status

| Resource | Status | Notes |
|-----------|--------|-------|
| Stationeers Wiki - Rocket | **Missing** | No page exists |
| Stationeers Wiki - Thruster | **Missing** | No page exists |
| Steam Workshop | **Limited** | Few atmospheric rocket scripts |
| GitHub repositories | **Minimal** | Only exca/ARM Rocket found (unverified) |
| Reddit r/stationeers | **Minimal** | Limited discussions |

### Theoretical Approach

Based on general Stationeers flight mechanics, atmospheric rocket automation would require:
- Altitude hold using PID control
- Flight stabilization with gyroscopes
- Landing controller for safe descent
- State machine for flight phases (Takeoff, Climb, Cruise, Descent, Landing)

**See also**: [`guides/rocketry-atmospheric-resources.md`](rocketry-atmospheric-resources.md) for theoretical patterns and untested code examples.

---

## Code Previews

### Launch Countdown Pattern

From Zappes/Stationeers flightcontroller:

```ic10
# Launch countdown with display
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

From Zappes/Stationeers flightcontroller:

```ic10
# Check if enough fuel to return
checkReturnFuel:
    l r0 Automation ReturnFuelCost
    mul r0 r0 1.1  # 10% safety margin
    l r1 Automation Fuel
    ble r1 r0 initiateReturn  # Return if low fuel
    j ra

initiateReturn:
    move currentMode modeReturning
    j done
```

### Fuel Pump Control Pattern

From Zappes/Stationeers fuelcontroller:

```ic10
# Pump control with safety interlocks
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

---

## Notes

### Orbital Rocketry
- **Production-ready code exists** in Zappes/Stationeers repository
- Always include fuel reserve calculations (1.1x minimum) to prevent stranding
- Landing pad size determines trader tier - Use 7x7 for large traders
- The flightcontroller handles all orbital operations safely
- See [Trading Resources Guide](trading-resources.md) for satellite dish integration

### Atmospheric Rocketry
- **No working automation currently verified** in community
- Device logic types and control mechanisms are unverified
- All code examples in atmospheric guide are **theoretical and untested**
- Community contributions needed for development

### General
- Orbital rocketry is endgame content - Master state machines and basic automation first
- Wiki pages for "Rocket" and "Thruster" do not exist
- Steam Workshop has limited rocket-specific scripts (most are general automation)
- GitHub repositories are the primary source for rocket automation code

---

## Sources

### GitHub Repositories
- [Zappes/Stationeers - Rocket Controller](https://github.com/Zappes/Stationeers/tree/main/Rocket%20Controller) - Production-ready orbital rocket automation
- [exca/Stationeers-IC10-Automation - ARM Rocket](https://github.com/exca/Stationeers-IC10-Automation/tree/main/ARM%20Rocket) - Atmospheric rocket (unverified)

### Official Documentation
- [Stationeers Wiki - Trader](https://stationeers-wiki.com/Trader) - Orbital trading workflow
- [Stationeers Wiki - Kit (Satellite Dish)](https://stationeers-wiki.com/Kit_(Satellite_Dish)) - Satellite dish automation

### Steam Workshop
- [Guide: How to Program Anything with an IC10 for the Novice](https://steamcommunity.com/sharedfiles/filedetails/?id=3288129161) - IC10 programming tutorial

### Other Repositories Found
- [jhillacre/stationeers-scripts](https://github.com/jhillacre/stationeers-scripts) - General IC10 scripts (no rocket-specific code found)
- [PaulSchulze1337/Stationeers](https://github.com/PaulSchulze1337/Stationeers) - IC10 programs (includes IC10 Code Minimizer Tool)
- [drclaw1188/stationeers_ic10](https://github.com/drclaw1188/stationeers_ic10) - IC10 scripts collection
- [Stationeers-ic/ic10](https://github.com/Stationeers-ic/ic10) - IC10 emulator and development toolkit

---

## Contributing

To help improve this guide:

1. **Test and document** the exca/ARM Rocket code
2. **Develop working atmospheric rocket** automation
3. **Verify device logic types** for atmospheric rockets
4. **Submit to Steam Workshop** or GitHub with clear documentation
5. **Report issues** with existing scripts to repository maintainers

For atmospheric rocketry specifically:
1. Test atmospheric rocket devices and document logic types
2. Develop and test basic altitude hold controller
3. Document thruster control behavior
4. Develop proven landing automation

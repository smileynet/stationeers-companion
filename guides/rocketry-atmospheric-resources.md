# Atmospheric Rocketry Guide

> Last updated: 2025-12-23
> Search terms: stationeers atmospheric rocket, flight control, altitude hold, atmospheric transport

## ⚠️⚠️ CRITICAL WARNING ⚠️⚠️

**ALL information in this guide is THEORETICAL and UNTESTED.**

- No official wiki documentation exists for atmospheric rockets
- No verified IC10 examples exist in the community
- All device logic types (Altimeter, Gyroscope, etc.) are unverified
- All code examples are untested and may not work

**DO NOT use this guide for actual gameplay without thorough testing.**

## Summary

**Warning: Limited Community Resources**

Atmospheric rocketry in Stationeers has minimal community documentation. Unlike orbital trading rockets, there are no dedicated wiki pages, IC10 examples, or comprehensive guides available.

This guide focuses on **theoretical automation patterns** based on general Stationeers flight mechanics and adaptation of existing control patterns. All code examples are **untested** and should be validated before deployment.

**Use cases for atmospheric rockets:**
- Surface transport between bases
- Rapid exploration
- Atmospheric science missions
- High-altitude resource collection

## Current Status

| Resource | Status | Notes |
|-----------|--------|-------|
| Stationeers Wiki - Rocket | **Missing** | No page exists |
| Stationeers Wiki - Thruster | **Missing** | No page exists |
| Steam Workshop | **Limited** | Few atmospheric rocket scripts |
| GitHub repositories | **None found** | No atmospheric rocket IC10 |
| Reddit r/stationeers | **Minimal** | Limited discussions |

## Theoretical Automation Approach

Based on general Stationeers flight mechanics, atmospheric rocket automation would require:

### 1. Altitude Control

Altitude hold using PID control:

```ic10
# Theoretical PID altitude controller
# Devices:
#   d0 = Altimeter (altitude sensor)
#   d1 = Thruster (main engine)

alias targetAltitude r10
define TARGET 5000  # Desired altitude in meters

# PID constants (tuning required)
define Kp 0.5
define Ki 0.01
define Kd 0.2

alias kp r0
alias ki r1
alias kd r2
alias error r3
alias lastError r4
alias integral r5
alias derivative r6
alias output r7
alias currentAlt r8

move kp Kp
move ki Ki
move kd Kd
move integral 0
move lastError 0

loop:
    l currentAlt d0 Altitude
    sub error targetAltitude currentAlt

    # Integral
    add integral integral error

    # Derivative
    sub derivative error lastError
    move lastError error

    # PID output
    mul output error kp
    add r9 integral ki
    add output output r9
    mul r9 derivative kd
    add output output r9

    # Clamp output
    max output output 0
    min output output 100

    s d1 On output
    yield
    j loop
```

**Caveats:**
- Altitude sensor logic type needs verification
- PID constants require extensive tuning
- Thruster control behavior may differ from expected

### 2. Flight Stabilization

Use gyroscopes with thruster balancing:

```ic10
# Theoretical stabilization controller
# Devices:
#   d0 = Gyroscope
#   d1-d4 = RCS thrusters

alias pitch r0
alias roll r1
alias yaw r2

loop:
    l pitch d0 Pitch
    l roll d0 Roll
    l yaw d0 Yaw

    # Simple proportional control
    # Forward/Back thrusters for pitch
    s d1 On pitch
    s d2 On 0  # Would use abs(pitch)

    # Side thrusters for roll
    s d3 On roll
    s d4 On 0

    yield
    j loop
```

### 3. Landing Controller

Descend at safe rate:

```ic10
# Theoretical landing controller
# Devices:
#   d0 = Altimeter
#   d1 = Thruster
#   d2 = SurfaceDetector (if exists)

alias altitude r0
alias descentRate r1
define SAFE_DESCENT 10  # meters/second
define MIN_ALT 50       # Cutoff altitude

loop:
    l altitude d0 Altitude

    blt altitude MIN_ALT cutoff

    # Simple descent control
    s d1 On 50  # Reduced thrust for descent
    yield
    j loop

cutoff:
    s d1 On 100  # Full thrust to arrest
    sleep 1
    s d1 On 0     # Cutoff
    j loop
```

## Adapted Patterns from Orbital Rocketry

### State Machine for Flight Phases

From `flightcontroller.ic10` (orbital), adapted for atmospheric flight:

```ic10
# Theoretical atmospheric flight state machine
# Flight modes:
#   0 = Grounded
#   1 = Takeoff
#   2 = Climb
#   3 = Cruise
#   4 = Descent
#   5 = Landing
#   6 = Emergency

define modeGrounded 0
define modeTakeoff 1
define modeClimb 2
define modeCruise 3
define modeDescent 4
define modeLanding 5
define modeEmergency 6

alias currentMode r6
alias altitude r7

init:
    move currentMode modeGrounded

loop:
    l currentMode Automation Mode
    beq currentMode modeGrounded processGrounded
    beq currentMode modeClimb processClimb
    # ... other modes
    yield
    j loop

processGrounded:
    l altitude d0 Altitude
    bgt altitude 0 takeoff
    j done

takeoff:
    move currentMode modeTakeoff
    j done

processClimb:
    # Climb to cruise altitude
    # ...
    j done
```

## Key Concepts

### Atmospheric Flight Mechanics

**What we know from Stationeers:**
- Thrusters provide forward thrust
- Gravity affects rockets in atmosphere
- Drag increases with speed
- Altitude affects atmosphere density (and drag)

**What needs verification:**
- Available sensor types (altimeter, gyroscope, etc.)
- Thruster control mechanisms
- Landing gear logic
- Flight state feedback from rocket

### Automation Challenges

1. **Sensor Availability**: Unknown which logic types are readable from atmospheric rockets
2. **Control Response**: Thrusters may not have fine-grained control
3. **Stability**: Atmospheric turbulence may require advanced control
4. **Landing**: Surface detection mechanisms unclear

### Potential Devices (To Be Verified)

| Device | Purpose | Status |
|---------|---------|--------|
| Gyroscope | Orientation sensing | Theoretical |
| Altimeter | Altitude measurement | Theoretical |
| Thruster | Propulsion | Confirmed exists |
| Landing Gear | Surface contact detection | Theoretical |
| Accelerometer | Velocity measurement | Theoretical |

## Required Devices (Theoretical)

Based on automation needs:

| Device | Purpose | Notes |
|--------|---------|-------|
| Rocket (Atmospheric) | Flight vehicle | Mode, Fuel logic types likely |
| Thrusters | Propulsion | Multiple for control |
| Gyroscope | Orientation | Pitch, Roll, Yaw feedback |
| Altimeter | Altitude sensing | Critical for flight control |
| IC Housing | Flight computer | Houses automation code |
| Display | Status readout | Altitude, mode indicators |

## Related Local Examples

### Core Patterns (Adaptable)

- **`examples/patterns/flightcontroller.ic10`** - State machine pattern
  - 8-mode dispatching structure
  - Mode-based control flow
  - Can be adapted for atmospheric flight modes

- **`examples/patterns/pid-controller-template.ic10`** - Precision control
  - PID implementation with anti-windup
  - Applicable to altitude/attitude control

- **`examples/patterns/hysteresis-template.ic10`** - Threshold control
  - Useful for on/off thrust control
  - Simpler than PID for basic operation

- **`examples/patterns/state-machine-template.ic10`** - Generic state machine
  - Ready to customize for flight phases

### None Directly Applicable

No existing atmospheric rocket examples exist in the codebase.

## Research Needed

**Community contributions welcome:**

1. **Device Documentation**
   - What logic types are available on atmospheric rockets?
   - How do thrusters respond to IC10 control?
   - What sensors can be attached?

2. **Code Examples**
   - Working altitude hold scripts
   - Stabilization systems
   - Landing automation
   - Takeoff sequences

3. **Mechanics Verification**
   - Flight physics (drag, gravity effects)
   - Control response times
   - Fuel consumption rates

## Notes

**Critical Warnings:**
- All code examples in this guide are **theoretical and untested**
- No working atmospheric rocket automation currently exists in the codebase
- Device logic types and control mechanisms are unverified
- Proceed with caution and test thoroughly before use

**Next Steps for Community:**
1. Verify atmospheric rocket device logic types via in-game testing
2. Create and test basic altitude hold controller
3. Document thruster control behavior
4. Develop proven landing automation

**For reference, see:**
- [`rocketry-orbital-resources.md`](rocketry-orbital-resources.md) - Orbital rocket automation (proven)
- [`examples/patterns/pid-controller-template.ic10`](../examples/patterns/pid-controller-template.ic10) - PID control pattern
- [`examples/patterns/state-machine-template.ic10`](../examples/patterns/state-machine-template.ic10) - State machine pattern

## Sources

- Stationeers Wiki (Rocket page does not exist)
- Stationeers Wiki (Thruster page does not exist)
- GitHub repositories (no atmospheric rocket scripts found)
- Steam Workshop (limited results)

**This guide is a placeholder awaiting community content.** If you have working atmospheric rocket automation, please consider contributing.

## Contributing

To help build this guide:

1. Test atmospheric rocket devices and document logic types
2. Develop and test IC10 scripts
3. Submit to: Stationeers Wiki, Steam Workshop, or GitHub
4. Contact to update this guide with verified resources


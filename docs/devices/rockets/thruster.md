---
title: Thruster
category: rockets
description: Rocket propulsion device for thrust generation
---

# Thruster

## ⚠️⚠️ WARNING: UNVERIFIED INFORMATION ⚠️⚠️

**Wiki documentation for "Thruster" does not exist.**

The logic types, values, and behaviors described in this document are **theoretical and unverified**. Always verify in-game before implementing automation.

Thrusters provide propulsion for rockets and spacecraft. They consume fuel to generate thrust, enabling launch, orbital maneuvers, and return trips. Multiple thrusters can be used for vector control.

## Variants

| Type | Thrust | Fuel Type | Notes |
|-------|---------|------------|-------|
| Small Thruster | Low | Volatiles | Fine control, RCS |
| Medium Thruster | Medium | Volatiles | Standard propulsion |
| Large Thruster | High | Volatiles | Main propulsion |
| Ion Thruster | Very Low | Electricity | Space-only, efficient |

## Components

| Component | Purpose |
|-----------|---------|
| Thruster Body | Main thruster unit |
| Nozzle Mount | Direction/orientation |
| Fuel Connection | Volatiles input |

## Logic Types

### Readable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Power` | 0/1 | Power state |
| `On` | 0/1 | Operating state |
| `Thrust` | 0-100 | Current thrust level (%) |

### Writable

| Logic Type | Value | Description |
|------------|-------|-------------|
| `On` | 0/1 | Turn thruster on/off |
| `Setting` | 0-100 | Set thrust level (%) |

**Note**: The above logic types are theoretical. Verify actual logic types in-game.

## IC10 Examples

### Basic Thruster Control

```ic10
alias thruster d0

# Turn on thruster at 50% thrust
s thruster On 1
s thruster Setting 50

# Full thrust
s thruster Setting 100

# Turn off
s thruster On 0
```

### Variable Thrust Control

```ic10
alias thruster d0
alias thrustLevel r0

loop:
    # Vary thrust based on input or condition
    # Example: ramp up thrust
    add thrustLevel thrustLevel 1
    bgt thrustLevel 100 reset

    s thruster Setting thrustLevel
    yield
    j loop

reset:
    move thrustLevel 0
    j loop
```

### Multi-Thruster Coordination

```ic10
alias thrusterMain d0
alias thrusterRCS1 d1
alias thrusterRCS2 d2

# Launch sequence - main thruster
s thrusterMain On 1
s thrusterMain Setting 100

# RCS thrusters for stability
s thrusterRCS1 Setting 50
s thrusterRCS2 Setting 50
```

## Placement Guidelines

### Main Thrusters
- Place at bottom of rocket (opposite direction of travel)
- Centered for straight ascent
- Multiple thrusters can be used for more thrust

### RCS (Reaction Control System)
- Place on sides for roll control
- Place at top/bottom for pitch/yaw
- Used for fine orbital adjustments

### Ion Thrusters
- Space-only (no thrust in atmosphere)
- High efficiency, very low thrust
- For orbital station-keeping and long burns

## Fuel Consumption

Thrusters consume volatiles (stored in fuel tanks):

| Thruster Type | Consumption | Notes |
|---------------|--------------|---------|
| Small | Low | Minimal fuel use |
| Medium | Medium | Standard use |
| Large | High | Significant fuel draw |
| Ion | Electricity | No volatiles consumed |

**Fuel efficiency**:
- Lower thrust generally = lower fuel consumption
- Longer burns = more fuel
- Efficient trajectories minimize fuel use

## Batch Operations

For multi-thruster control, use device hashing:

```ic10
# Use hash to control all main thrusters at once
# (Requires hash values from Stationpedia/Labeler)

define MAIN_THRUSTER_HASH 0x12345678  # Example hash

alias thrust r0

# Set all main thrusters to 50%
move thrust 50
sb MAIN_THRUSTER_HASH Setting thrust

# Turn off all main thrusters
sb MAIN_THRUSTER_HASH On 0
```

## Control Patterns

### PID Thrust Control

For altitude or velocity control:

```ic10
alias thruster d0
alias target r1
alias current r2
alias error r3

# PID constants (tuning required)
define Kp 0.5
define Ki 0.01

loop:
    l current sensorValue
    sub error target current

    # P-term
    mul r0 error Kp
    s thruster Setting r0

    yield
    j loop
```

### Hysteresis Control

Simple on/off with deadband:

```ic10
alias thruster d0
alias sensor d1

define TARGET 100
define DEADBAND 5

loop:
    l r0 sensor Value
    blt r0 TARGET_minus checkLow

    # Above target - thrust off
    s thruster On 0
    j loop

checkLow:
    move r0 TARGET
    sub r0 r0 DEADBAND
    bgt r0 sensor loop

    # Below threshold - thrust on
    s thruster On 1
    s thruster Setting 100

    j loop
```

## Prefab Hashes

| Device | Hash |
|--------|------|
| Kit (Thruster Small) | *Check Stationpedia* |
| Kit (Thruster Medium) | *Check Stationpedia* |
| Kit (Thruster Large) | *Check Stationpedia* |
| Kit (Thruster Ion) | *Check Stationpedia* |

*Note: Use in-game Labeler tool or Stationpedia for exact hashes*

## Network Requirements

Same data network:
- Thruster(s)
- IC Housing (flight controller)
- Fuel tanks
- (Optional) Sensors, gyroscope

## Best Practices

1. **Balance thrust** - Ensure center of thrust aligns with center of mass
2. **Redundancy** - Multiple thrusters provide backup if one fails
3. **Batch control** - Use `sb` for multi-thruster coordination
4. **RCS optimization** - Small thrusters for fine control save fuel
5. **Fuel monitoring** - Always track fuel levels for return trip
6. **Ion thrusters** - Use in space for long-duration efficiency

## See Also

- [docs/devices/rockets/orbital-rocket.md](orbital-rocket.md) - Orbital rocket overview
- [examples/patterns/pid-controller-template.ic10](../../../examples/patterns/pid-controller-template.ic10) - PID control for thrust
- [examples/patterns/hysteresis-template.ic10](../../../examples/patterns/hysteresis-template.ic10) - On/off thrust control

## Notes

**Critical Note**: Wiki documentation for "Thruster" does not exist. The logic types, values, and behaviors described here are **theoretical**. Always verify in-game before implementing automation.

Fuel consumption rates, thrust values, and specific logic types require in-game testing for accuracy.

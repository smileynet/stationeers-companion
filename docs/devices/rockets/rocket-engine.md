---
title: Rocket Engine
category: rockets
description: Advanced rocket propulsion system
---

# Rocket Engine

Rocket engines provide advanced propulsion capabilities beyond basic thrusters. They may offer features like gimballing, variable specific impulse, or specialized fuel types.

**Note**: This device type may not exist in Stationeers as a separate entity from thrusters. This documentation is provided as a placeholder until confirmed information is available.

## Status

| Aspect | Status |
|---------|--------|
| Existence in game | **Unverified** |
| Wiki documentation | **Missing** (404) |
| Community resources | **None found** |
| IC10 examples | **None found** |

## Theoretical Implementation

If rocket engines exist as a separate device class, they would likely feature:

### Enhanced Features (Theoretical)

| Feature | Description |
|----------|-------------|
| Gimballing | Vector thrust direction control |
| Variable Isp | Adjust fuel efficiency based on throttle |
| Multi-fuel | Accept multiple fuel types |
| Staging | Multi-stage rocket capability |
| Restart capability | Engine can be stopped and restarted |

### Potential Logic Types (Theoretical)

| Logic Type | Value | Description |
|------------|-------|-------------|
| `Thrust` | 0-100 | Thrust level (%) |
| `GimbalX` | float | Horizontal gimbal angle |
| `GimbalY` | float | Vertical gimbal angle |
| `FuelType` | enum | Selected fuel (if multi-fuel) |
| `RestartReady` | 0/1 | Engine ready for restart |
| `StageNumber` | int | Current active stage |

## Comparison: Engine vs Thruster

| Characteristic | Thruster | Rocket Engine |
|---------------|-----------|---------------|
| Basic thrust | Yes | Yes |
| Gimballing | No | Possibly |
| Restart capability | No | Possibly |
| Fuel efficiency | Fixed | Possibly variable |
| Staging | No | Possibly |

## IC10 Examples (Theoretical)

### Gimbal Control

```ic10
alias engine d0

# Center gimbal
s engine GimbalX 0
s engine GimbalY 0

# Pitch up
s engine GimbalY 10

# Roll right
s engine GimbalX 10
```

### Staging Control

```ic10
alias engineStage1 d0
alias engineStage2 d1
alias separator d2

# Check current stage
l r0 engineStage1 StageNumber
beq r0 1 activeStage1

# Stage 2 active
j done

activeStage1:
    # Launch with stage 1
    s engineStage1 Thrust 100

    # Check fuel for stage separation
    l r0 engineStage1 Fuel
    blt r0 FUEL_THRESHOLD separate

    j done

separate:
    # Stage separation sequence
    s engineStage1 Thrust 0
    s separator Activate 1
    sleep 1

    # Activate stage 2
    s engineStage2 Thrust 100
    j done
```

## Research Needed

The following information is **missing** and requires community contribution:

1. **Existence verification** - Do rocket engines exist as separate devices?
2. **Logic types** - What can be read/written?
3. **Gimballing** - Is vector control available?
4. **Staging** - Can engines be staged?
5. **Restart** - Can engines be stopped and restarted?
6. **Fuel types** - What fuels can be used?

## Contributing

If you have experience with rocket engines in Stationeers:

1. Verify existence of rocket engine devices
2. Test logic types and document values
3. Create working IC10 examples
4. Submit to: Stationeers Wiki, Steam Workshop, or GitHub
5. Contact to update this documentation

## See Also

- [docs/devices/rockets/thruster.md](thruster.md) - Standard thruster documentation
- [docs/devices/rockets/orbital-rocket.md](orbital-rocket.md) - Orbital rocket overview
- [guides/rocketry-orbital-resources.md](../../../guides/rocketry-orbital-resources.md) - Orbital rocket automation

## Notes

**This documentation is a placeholder.** Rocket engines may not exist as a separate device type in Stationeers. If you are looking for basic rocket propulsion, see [thruster.md](thruster.md).

If rocket engines are confirmed to exist, this documentation will be updated with verified information.

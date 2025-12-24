---
title: Volume Pump
category: atmospheric
prefab_hash: -321403609
---

# Volume Pump

**Prefab Hash**: `-321403609`
**Power**: 10W (base), up to 1000W depending on setting

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Device is powered on | Boolean |
| Pressure | Output pressure | kPa |
| RequiredPower | Power required at current setting | Watts |
| FlowRate | Gas flow rate | L/s |
| MaxFlowRate | Maximum possible flow | L/s |
| Temperature | Device temperature | Kelvin |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Turn device on/off | Boolean (1=on, 0=off) |
| Pressure | Set target pressure | kPa |
| MaxPressure | Maximum output pressure limit | kPa |

## IC10 Example

```ic10
# Volume pump pressure control
alias pump d0
alias sensor d1

alias rPressure r0
alias rTarget r1

define TARGET_PRESSURE 101.325  # 1 atm

main:
# Read current pressure
l rPressure sensor Pressure

# Compare to target
sgt r2 rPressure TARGET_PRESSURE  # r2 = 1 if pressure too high

# If pressure too high, pump out (reverse direction)
s pump On r2
s pump Pressure TARGET_PRESSURE

yield
j main
```

## Usage Notes

1. **Direction Control**: Pressure below ambient = pump out (vacuum), Pressure above ambient = pump in (pressurize)
2. **Flow Rate**: Automatically adjusts based on pressure difference
3. **Power Scaling**: Higher settings require more power
4. **Volume Capacity**: Moves large volumes quickly compared to passive vents

## Common Patterns

### Rapid Depressurization

```ic10
# Pump down to vacuum quickly
alias pump d0

s pump On 1        # Turn on
s pump Pressure 0      # Target vacuum (or low pressure)
```

### High-Throughput Pressurization

```ic10
# Pump in quickly
alias pump d0
define TARGET 150  # Higher pressure for faster fill

s pump On 1
s pump Pressure TARGET
```

### Emergency Venting

```ic10
# Full-power venting (outward pumping)
alias pump d0

s pump On 1
s pump Pressure 0  # Max outward flow
s pump MaxPressure 1000  # Ensure high capacity
```

## Related Devices

- **Passive Vent**: Lower power, slower venting
- **Active Vent**: Has direction setting, similar to volume pump
- **Atmosphere Pipe**: Required for gas supply/return

## See Also

- [active-vent.md](../atmospheric/active-vent.md) - Directional venting
- [passive-vent.md](../atmospheric/passive-vent.md) - Passive venting
- [gas-sensor.md](../atmospheric/gas-sensor.md) - Pressure sensing

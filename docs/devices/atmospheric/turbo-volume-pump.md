---
title: Turbo Volume Pump
category: atmospheric
prefab_hash: 561323117
---

# Turbo Volume Pump

**Prefab Hash**: `561323117`
**Power**: 20W (base), up to 5000W depending on setting

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
| RatioOxygen | O₂ ratio in gas | Float (0-1) |
| RatioCarbonDioxide | CO₂ ratio in gas | Float (0-1) |
| RatioNitrogen | N₂ ratio in gas | Float (0-1) |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Turn device on/off | Boolean (1=on, 0=off) |
| Pressure | Set target pressure | kPa |
| MaxPressure | Maximum output pressure limit | kPa |

## IC10 Example

```ic10
# High-throughput turbo pump control
alias turbo d0
alias sensor d1

alias rPressure r0
alias rTarget r1
alias rHighPower r2

define TARGET_PRESSURE 200  # Pressurization target
define HIGH_POWER_THRESHOLD 100  # kPa

main:
l rPressure sensor Pressure
sgt rHighPower rPressure HIGH_POWER_THRESHOLD

# High pressure = low power (sucking out)
s turbo On 1
beq rHighPower setHighPower

# Low pressure = high power (pumping in)
setHighPower:
s turbo MaxPressure 5000  # Full turbo power

setLowPower:
s turbo MaxPressure 500    # Low power mode

s turbo Pressure TARGET_PRESSURE

yield
j main
```

## Usage Notes

1. **Power Scaling**: Unlike standard Volume Pump, Turbo Pump has much higher power draw
2. **Flow Rate**: Significantly higher throughput than standard Volume Pump
3. **Direction**: Pressure relative to ambient determines in/out flow
4. **Gas Ratios**: Can read gas composition (unlike standard pump)

## Advantages vs Volume Pump

| Feature | Volume Pump | Turbo Volume Pump |
|---------|--------------|------------------|
| Base Power | 10W | 20W |
| Max Power | 1000W | 5000W |
| Flow Rate | Low | High |
| Gas Ratio Readout | No | Yes |
| Use Case | Basic venting | Rapid pressurization/depressurization |

## Common Patterns

### Rapid Pressurization

```ic10
# Quick fill with turbo pump
define TARGET 100  # kPa target

s turbo On 1
s turbo MaxPressure 5000  # Maximum power
s turbo Pressure TARGET

# Wait until target reached
main:
l r0 sensor Pressure
blt r0 TARGET main
```

### Gas Ratio Monitoring

```ic10
# Monitor air composition while pumping
l r0 turbo RatioOxygen
l r1 turbo RatioCarbonDioxide
l r2 turbo RatioNitrogen

# Check ratios (approximate Earth-like)
sgt r3 r0 0.20      # O2 > 20%
sgt r4 r1 0.01      # CO2 < 1%
sgt r5 r2 0.78      # N2 > 78%

and r6 r3 r4             # Good O2 AND good CO2
and r6 r6 r5            # AND good N2

# Only pump if gas composition is good
s turbo On r6
```

## Related Devices

- **Volume Pump**: Lower power alternative
- **Passive Vent**: For passive venting
- **Atmosphere Pipe**: Gas supply network
- **Gas Sensor**: Pressure and composition monitoring

## See Also

- [volume-pump.md](volume-pump.md) - Standard volume pump
- [gas-sensor.md](../atmospheric/gas-sensor.md) - Gas composition sensing
- [knowledge/gases/](../../../knowledge/gases/) - Gas properties reference

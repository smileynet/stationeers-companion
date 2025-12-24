---
title: Wall Cooler
category: atmospheric
prefab_hash: 1469396920
---

# Wall Cooler

**Prefab Hash**: `1469396920`
**Power**: 20W (base), up to 200W depending on setting

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Device is powered on | Boolean |
| Temperature | Cooler temperature | Kelvin |
| Pressure | Current pressure in pipe | kPa |
| RequiredPower | Power required at current setting | Watts |
| RatioOxygen | O₂ ratio in pipe | Float |
| RatioCarbonDioxide | CO₂ ratio in pipe | Float |
| RatioNitrogen | N₂ ratio in pipe | Float |
| RatioVolatiles | Other gases ratio | Float |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Turn device on/off | Boolean (1=on, 0=off) |
| Temperature | Set target temperature | Kelvin |
| Pressure | Set target pressure | kPa |
| MaxPressure | Maximum output pressure limit | kPa |

## IC10 Example

```ic10
# Temperature control with wall cooler
alias cooler d0
alias sensor d1

alias rTemp r0
alias rTarget r1

define TARGET_TEMP 280.15  # 7°C

main:
# Read temperature
l rTemp sensor Temperature

# If too hot, turn on cooler
sgt r2 rTemp TARGET_TEMP
s cooler On r2

# Set target temperature
s cooler Temperature TARGET_TEMP

yield
j main
```

## Usage Notes

1. **Mounting**: Installed on wall like a window
2. **Direction**: Cools pipe network on both sides
3. **Power Scaling**: Higher temperature difference = more power draw
4. **Temperature Range**: Can cool below ambient (down to ~80K)
5. **Pipe Network**: Requires gas pipe on both sides
6. **Ice Warning**: Can cause ice formation if pipe pressure too low

## Common Patterns

### Thermostat Control

```ic10
# Maintain target temperature
define HYSTERESIS 1.0  # ±1K deadband
define TARGET 293.15       # 20°C
define LOWER (TARGET - HYSTERESIS)
define UPPER (TARGET + HYSTERESIS)

main:
l r0 sensor Temperature
sgt r1 r0 UPPER           # Above upper limit?
slt r2 r0 LOWER           # Below lower limit?

or r3 r1 r2               # Outside deadband?
s cooler On r3
```

### Freeze Protection

```ic10
# Prevent pipe from freezing
define MIN_PRESSURE 50       # Minimum safe pressure
define MIN_TEMP 200           # Don't cool below -73°C

main:
l r0 sensor Temperature
l r1 cooler Pressure
slt r2 r0 MIN_TEMP         # Too cold?
blt r3 r1 MIN_PRESSURE      # Pressure too low?

or r4 r2 r3               # Freeze danger?
s cooler On 0               # Turn off if dangerous
```

### Power Management

```ic10
# Adjust cooling based on available power
alias cooler d0
alias battery d1

alias rPowerLevel r0
alias rHighPower r1

main:
# Read battery power
l rPowerLevel battery Charge

# Battery above 50% = high power mode
sgt rHighPower rPowerLevel 500000  # 500 kJ
beq rHighPower highPowerMode

lowPowerMode:
s cooler MaxPressure 101       # Limited cooling
j checkTemp

highPowerMode:
s cooler MaxPressure 200       # Maximum cooling

checkTemp:
# Normal temperature control loop
...
```

## Related Devices

- **Wall Heater**: Similar device for heating
- **Active Vent**: Alternative for temperature control
- **Atmosphere Pipe**: Required for gas network
- **Gas Sensor**: Temperature monitoring

## Differences from Active Vent

| Feature | Wall Cooler | Active Vent |
|---------|------------|-------------|
| Mounting | Wall-mounted | Atmos pipe-mounted |
| Direction | Both sides | Configurable (inward/outward) |
| Temperature Control | Yes | No |
| Use Case | Temperature regulation | Pressure regulation |

## See Also

- [wall-heater.md](wall-heater.md) - Heating counterpart
- [active-vent.md](active-vent.md) - Alternative cooling
- [gas-sensor.md](../atmospheric/gas-sensor.md) - Temperature sensing
- [knowledge/temperature.md](../../../knowledge/temperature.md) - Temperature management

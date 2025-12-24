---
title: Wall Heater
category: atmospheric
prefab_hash: 1389046652
---

# Wall Heater

**Prefab Hash**: `1389046652`
**Power**: 20W (base), up to 200W depending on setting

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Device is powered on | Boolean |
| Temperature | Heater temperature | Kelvin |
| Pressure | Current pressure in pipe | kPa |
| RequiredPower | Power required at current setting | Watts |
| RatioOxygen | O₂ ratio in gas | Float |
| RatioCarbonDioxide | CO₂ ratio in gas | Float |
| RatioNitrogen | N₂ ratio in gas | Float |
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
# Temperature control with wall heater
alias heater d0
alias sensor d1

alias rTemp r0
alias rTarget r1
alias rHeat r2

define TARGET_TEMP 313.15  # 40°C

main:
# Read temperature
l rTemp sensor Temperature

# If too cold, turn on heater
slt r2 rTemp TARGET_TEMP
s heater On r2

# Set target temperature
s heater Temperature TARGET_TEMP

yield
j main
```

## Usage Notes

1. **Mounting**: Installed on wall like a window
2. **Direction**: Heats pipe network on both sides
3. **Power Scaling**: Higher temperature difference = more power draw
4. **Temperature Range**: Can heat up to very high temperatures (600K+)
5. **Pipe Network**: Requires gas pipe on both sides
6. **Overheat Protection**: Can cause burns if used on low pressure

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
slt r1 r0 LOWER
slt r2 r0 UPPER

or r3 r1 r2               # Outside deadband?
s heater On r3
s heater Temperature TARGET

yield
j main
```

### Rapid Heating

```ic10
# Maximum heat for quick warmup
alias heater d0

s heater On 1
s heater Temperature 350       # ~77°C (max comfortable)
s heater MaxPressure 1000     # Full power
```

### Freeze Prevention

```ic10
# Prevent pipe from freezing
define MIN_TEMP 200         # -73°C (don't cool below)
define MIN_PRESSURE 50       # Minimum safe pressure

main:
l r0 sensor Temperature
l r1 heater Pressure

slt r2 r0 MIN_TEMP         # Too cold?
blt r3 r1 MIN_PRESSURE      # Pressure too low?

or r4 r2 r3               # Freeze danger?
s heater On 0               # Turn off if dangerous

# Normal heating
s heater Temperature TARGET

yield
j main
```

## Power Management

```ic10
# Adjust heating based on available power
alias heater d0
alias battery d1

alias rPowerLevel r0
alias rHighPower r1

main:
# Read battery power
l rPowerLevel battery Charge

# Battery above 50% = high power mode
sgt rHighPower rPowerLevel 500000  # 500 kJ
beq rHighPower lowPowerMode

highPowerMode:
s heater MaxPressure 200       # Full heating power
j checkTemp

lowPowerMode:
s heater MaxPressure 100       # Limited heating power

checkTemp:
# Normal temperature control loop
...
```

## Related Devices

- **Wall Cooler**: Similar device for cooling
- **Active Vent**: Alternative for temperature control
- **Atmosphere Pipe**: Required for gas network
- **Gas Sensor**: Temperature monitoring

## Differences from Wall Cooler

| Feature | Wall Heater | Wall Cooler |
|---------|------------|-------------|
| Temperature Range | Up to 600K+ | Down to ~200K |
| Power Consumption | Similar range | Similar range |
| Use Case | Heating rooms | Cooling rooms |
| Freeze Risk | No | Yes (if pressure too low) |
| Burn Risk | Yes (if used carelessly) | No |

## See Also

- [wall-cooler.md](wall-cooler.md) - Cooling counterpart
- [gas-sensor.md](../atmospheric/gas-sensor.md) - Temperature sensing
- [active-vent.md](active-vent.md) - Alternative temperature control
- [knowledge/temperature.md](../../../knowledge/temperature.md) - Temperature management

# Gas Properties Reference

Properties and constants for atmospheric control in Stationeers.

## Gas Types and Logic Values

Use these with `RatioX` logic types to read gas composition:

| Gas | Logic Type | Notes |
|-----|------------|-------|
| Oxygen (O2) | RatioOxygen | Breathable, combustion |
| Nitrogen (N2) | RatioNitrogen | Inert filler |
| Carbon Dioxide (CO2) | RatioCarbonDioxide | Toxic at high % |
| Volatiles (H2) | RatioVolatiles | Fuel, explosive |
| Pollutant (X) | RatioPollutant | Toxic waste |
| Water (H2O) | RatioWater | Vapor/condensation |
| Nitrous Oxide (N2O) | RatioNitrousOxide | Anesthetic |

## Atmospheric Constants

### Pressure (kPa)

| Condition | Value | Notes |
|-----------|-------|-------|
| Vacuum | 0 | Space |
| Minimum breathable | 20 | With pure O2 |
| Ideal room | 101.325 | Earth standard |
| Safe maximum | 202.65 | 2 atm |
| Suit warning | 50 | Low pressure alert |

### Temperature (Kelvin)

| Condition | Value (K) | Celsius |
|-----------|-----------|---------|
| Absolute zero | 0 | -273.15°C |
| Water freezing | 273.15 | 0°C |
| Ideal room | 293.15 | 20°C |
| Human comfort min | 283.15 | 10°C |
| Human comfort max | 303.15 | 30°C |
| Water boiling | 373.15 | 100°C |

### Breathable Atmosphere

| Parameter | Min | Ideal | Max |
|-----------|-----|-------|-----|
| Pressure (kPa) | 20 | 101.325 | 202.65 |
| O2 ratio | 0.16 | 0.21 | 0.30 |
| CO2 ratio | 0 | 0 | 0.01 |
| Temperature (K) | 273 | 293 | 313 |

## Gas-Specific Behavior

### Oxygen (O2)
- Required for human survival
- Required for combustion
- Ideal ratio: 21% (0.21)
- **Logic**: `RatioOxygen`

### Nitrogen (N2)
- Inert filler gas
- No biological effect
- Ideal ratio: ~78% (0.78)
- **Logic**: `RatioNitrogen`

### Carbon Dioxide (CO2)
- Toxic above 1%
- Produced by humans, combustion
- Must be scrubbed/filtered
- **Logic**: `RatioCarbonDioxide`

### Volatiles (H2)
- Highly flammable fuel
- Explosive with O2
- Store separately!
- **Logic**: `RatioVolatiles`

### Pollutant (X)
- Toxic waste gas
- Produced by furnaces, some reactions
- Must be vented to space
- **Logic**: `RatioPollutant`

### Water Vapor (H2O)
- Condenses at low temp
- Used in hydroponics
- **Logic**: `RatioWater`

## IC10 Examples

### Check Breathable Atmosphere

```ic10
alias sensor d0
define MIN_O2 0.16
define MAX_CO2 0.01
define MIN_PRESSURE 20

# Read atmosphere
l r0 sensor RatioOxygen
l r1 sensor RatioCarbonDioxide
l r2 sensor Pressure

# Check O2 sufficient
sgt r3 r0 MIN_O2

# Check CO2 safe
slt r4 r1 MAX_CO2

# Check pressure
sgt r5 r2 MIN_PRESSURE

# All conditions met?
and r6 r3 r4
and r6 r6 r5    # r6 = 1 if breathable
```

### Temperature Control

```ic10
alias sensor d0
alias cooler d1
alias heater d2
define TARGET_TEMP 293.15  # 20°C
define TOLERANCE 5

l r0 sensor Temperature

# Calculate difference from target
sub r1 r0 TARGET_TEMP

# Too hot? Run cooler
sgt r2 r1 TOLERANCE
s cooler On r2

# Too cold? Run heater
slt r3 r1 -TOLERANCE
mul r3 r3 -1  # Invert for negative
s heater On r3
```

### Gas Ratio Monitor

```ic10
alias analyzer d0
alias display d1

# Read all gas ratios
l r0 analyzer RatioOxygen
l r1 analyzer RatioNitrogen
l r2 analyzer RatioCarbonDioxide
l r3 analyzer RatioVolatiles
l r4 analyzer RatioPollutant

# Convert O2 to percentage for display
mul r5 r0 100
s display Setting r5
```

## Temperature Conversion

```ic10
# Kelvin to Celsius: C = K - 273.15
define KELVIN_OFFSET 273.15
l r0 sensor Temperature
sub r1 r0 KELVIN_OFFSET  # r1 = Celsius

# Celsius to Kelvin: K = C + 273.15
define TARGET_C 20
add r2 TARGET_C KELVIN_OFFSET  # r2 = 293.15K
```

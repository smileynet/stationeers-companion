---
title: Gas Sensor
category: atmospheric
prefab_hash: 546126601
---

# Gas Sensor

Reads atmospheric conditions including pressure, temperature, and gas composition.

**Prefab Hash**: `546126601`

## Logic Types

### Readable - Atmosphere

| Logic Type | Description | Unit |
|------------|-------------|------|
| Pressure | Total atmospheric pressure | kPa |
| Temperature | Gas temperature | K (Kelvin) |
| Combustion | Combustible atmosphere detected | Boolean |

### Readable - Gas Ratios

| Logic Type | Description | Range |
|------------|-------------|-------|
| RatioOxygen | O2 concentration | 0-1 |
| RatioNitrogen | N2 concentration | 0-1 |
| RatioCarbonDioxide | CO2 concentration | 0-1 |
| RatioVolatiles | H2 (fuel) concentration | 0-1 |
| RatioPollutant | X (toxic) concentration | 0-1 |
| RatioWater | H2O vapor concentration | 0-1 |
| RatioNitrousOxide | N2O concentration | 0-1 |

### Readable - Liquid Ratios

| Logic Type | Description | Range |
|------------|-------------|-------|
| RatioLiquidOxygen | Liquid O2 | 0-1 |
| RatioLiquidNitrogen | Liquid N2 | 0-1 |
| RatioLiquidCarbonDioxide | Liquid CO2 | 0-1 |
| RatioLiquidVolatiles | Liquid H2 | 0-1 |
| RatioLiquidPollutant | Liquid X | 0-1 |
| RatioLiquidNitrousOxide | Liquid N2O | 0-1 |
| RatioPollutedWater | Contaminated water | 0-1 |

### Readable - Device Info

| Logic Type | Description | Unit |
|------------|-------------|------|
| On | Power state | Boolean |
| Activate | Activation state | Boolean |
| Mode | Sensor orientation | Integer |
| PrefabHash | Device type | Hash |
| ReferenceId | Unique device ID | Integer |
| NameHash | Label hash | Hash |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|------|
| On | Enable/disable | Boolean |
| Mode | Set orientation (see below) | Integer |

## Mode Values

| Mode | Orientation |
|------|-------------|
| 0 | Default |
| 1 | Horizontal |
| 2 | Vertical |

## Common Use Cases

### Breathable Atmosphere Check
```ic10
alias sensor d0
alias indicator d1
define MIN_O2 0.16
define MAX_CO2 0.01
define MIN_PRESSURE 20

l r0 sensor RatioOxygen
l r1 sensor RatioCarbonDioxide
l r2 sensor Pressure

sgt r3 r0 MIN_O2       # O2 sufficient?
slt r4 r1 MAX_CO2      # CO2 safe?
sgt r5 r2 MIN_PRESSURE # Pressure ok?

and r6 r3 r4
and r6 r6 r5           # All conditions met?

s indicator On r6      # Green if breathable
```

### Temperature Display
```ic10
alias sensor d0
alias display d1
define KELVIN_OFFSET 273.15

l r0 sensor Temperature
sub r0 r0 KELVIN_OFFSET  # Convert to Celsius
s display Setting r0
```

### Pressure Regulator
```ic10
alias sensor d0
alias vent d1
define TARGET 101.325
define TOLERANCE 5

l r0 sensor Pressure
sub r1 r0 TARGET       # Difference from target
abs r2 r1              # Absolute difference

sgt r3 r2 TOLERANCE    # Outside tolerance?
s vent On r3           # Run vent if needed

sgt r4 r1 0            # Above target?
s vent Mode r4         # 1=outward if high, 0=inward if low
```

### Gas Leak Detection
```ic10
alias sensor d0
alias alarm d1
define MAX_VOLATILES 0.01
define MAX_POLLUTANT 0.005

l r0 sensor RatioVolatiles
l r1 sensor RatioPollutant

sgt r2 r0 MAX_VOLATILES
sgt r3 r1 MAX_POLLUTANT
or r4 r2 r3            # Either dangerous gas?

s alarm On r4
```

## Notes

- Ratio values are 0-1 (multiply by 100 for percentage)
- Temperature is always in Kelvin
- Sensor reads the atmosphere in its grid cell
- Place sensor in the room you want to monitor
- Pipe Analyzer is similar but reads pipe contents

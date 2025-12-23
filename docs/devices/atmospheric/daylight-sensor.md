---
title: Daylight Sensor
category: atmospheric
---

# Daylight Sensor

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Mode | Integer |
| 1 | Horizontal |
| 2 | Vertical |
| Activate | Boolean |
| Horizontal | Float |
| Vertical | Float |
| SolarAngle | Float |
| On | Boolean |
| PrefabHash | Integer |
| SolarIrradiance | Float |
| ReferenceId | Integer |
| NameHash | Integer |
| Activate | Boolean |
| Quantity | Integer |
| On | Boolean |
| PrefabHash | Integer |
| ReferenceId | Integer |
| NameHash | Integer |
| Pressure | Float |
| Temperature | Float |
| Combustion | Boolean |
| RatioOxygen | Float |
| RatioHydrogen | Float |
| RatioCarbonDioxide | Float |
| RatioNitrogen | Float |
| RatioPollutant | Float |
| RatioVolatiles | Float |
| RatioNitrousOxide | Float |
| RatioSteam | Float |
| RatioLiquidOxygen | Float |
| RatioLiquidHydrogen | Float |
| RatioLiquidCarbonDioxide | Float |
| RatioLiquidNitrogen | Float |
| RatioLiquidPollutant | Float |
| RatioLiquidVolatiles | Float |
| RatioLiquidNitrousOxide | Float |
| RatioWater | Float |
| RatioPollutedWater | Float |
| PrefabHash | Integer |
| ReferenceId | Integer |
| NameHash | Integer |
| Activate | Boolean |
| Quantity | Integer |
| PrefabHash | Integer |
| ReferenceId | Integer |
| NameHash | Integer |
| Activate | Boolean |
| Setting | Float |
| Quantity | Integer |
| PrefabHash | Integer |
| ReferenceId | Integer |
| NameHash | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| Mode | Integer |
| Activate | Boolean |
| Horizontal | Float |
| Vertical | Float |
| On | Boolean |
| Activate | Boolean |
| On | Boolean |
| Setting | Float |

## IC10 Example

```ic10
alias device d0  # Daylight Sensor
l r0 device Mode
s device Mode 1
```

---
title: Filtration
category: other
prefab_hash: -348054045
power: 5
---

# Filtration

**Prefab Hash**: `-348054045`

**Power Usage**: 5W

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Filter(Right) | Slot 0 |
| Filter (Left) | Slot 1 |
| v | Slot 2 |
| On | Switch |
| Open | Boolean |
| Lock | Boolean |
| Mode | Boolean |
| Power | Boolean |
| Open | Boolean |
| Mode | Boolean |
| Error | Boolean |
| Lock | Boolean |
| Maximum | Integer |
| Ratio | Float |
| On | Boolean |
| RequiredPower | Integer |
| PressureInput | Float |
| TemperatureInput | Float |
| RatioOxygenInput | Float |
| RatioCarbonDioxideInput | Float |
| RatioNitrogenInput | Float |
| RatioPollutantInput | Float |
| RatioVolatilesInput | Float |
| RatioWaterInput | Float |
| RatioNitrousOxideInput | Float |
| TotalMolesInput | Float |
| PressureOutput | Float |
| TemperatureOutput | Float |
| RatioOxygenOutput | Float |
| RatioCarbonDioxideOutput | Float |
| RatioNitrogenOutput | Float |
| RatioPollutantOutput | Float |
| RatioVolatilesOutput | Float |
| RatioWaterOutput | Float |
| RatioNitrousOxideOutput | Float |
| TotalMolesOutput | Float |
| PressureOutput2 | Float |
| TemperatureOutput2 | Float |
| RatioOxygenOutput2 | Float |
| RatioCarbonDioxideOutput2 | Float |
| RatioNitrogenOutput2 | Float |
| RatioPollutantOutput2 | Float |
| RatioVolatilesOutput2 | Float |
| RatioWaterOutput2 | Float |
| RatioNitrousOxideOutput2 | Float |
| TotalMolesOutput2 | Float |
| CombustionInput | Float |
| CombustionOutput | Float |
| CombustionOutput2 | Float |
| Occupied | Boolean |
| OccupantHash | Integer |
| Quantity | Integer |
| Damage | Integer |
| Class | Integer |
| MaxQuanity | Integer |
| PrefabHash | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| On | Boolean |
| Setting | Integer |
| Setting | Integer |

## IC10 Example

```ic10
alias device d0  # Filtration
l r0 device Filter(Right)
s device On 1
```

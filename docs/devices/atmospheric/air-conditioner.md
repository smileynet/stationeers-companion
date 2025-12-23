---
title: Air Conditioner
category: atmospheric
prefab_hash: -2087593337
power: 10
---

# Air Conditioner

**Prefab Hash**: `-2087593337`

**Power Usage**: 10W

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Start | Touchkey |
| On/Off | Switch |
| Power | Boolean |
| 1 | Powered |
| Open | Integer |
| 1 | Open |
| Mode | Integer |
| 1 | Active |
| Error | Boolean |
| 1 | Error |
| Lock | Boolean |
| 1 | Locked |
| Setting | Integer |
| Maximum | Float |
| Ratio | Float |
| On | Boolean |
| 1 | On |
| RequiredPower | Integer |
| PrefabHash | Integer |
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
| TotalMolesOutput2 | Integer |
| CombustionInput | Boolean |
| CombustionOutput | Boolean |
| CombustionOutput2 | Boolean |
| OperationalTemperatureEfficiency | Float |
| TemperatureDifferentialEfficiency | Float |
| PressureEfficiency | Float |
| RatioLiquidNitrogenInput | Float |
| RatioLiquidNitrogenOutput | Float |
| RatioLiquidNitrogenOutput2 | Float |
| RatioLiquidOxygenInput | Float |
| RatioLiquidOxygenOutput | Float |
| RatioLiquidOxygenOutput2 | Float |
| RatioLiquidVolatilesInput | Float |
| RatioLiquidVolatilesOutput | Float |
| RatioLiquidVolatilesOutput2 | Float |
| RatioSteamInput | Float |
| RatioSteamOutput | Float |
| RatioSteamOutput2 | Float |
| RatioLiquidCarbonDioxideInput | Float |
| RatioLiquidCarbonDioxideOutput | Float |
| RatioLiquidCarbonDioxideOutput2 | Float |
| RatioLiquidPollutantInput | Float |
| RatioLiquidPollutantOutput | Float |
| RatioLiquidPollutantOutput2 | Float |
| RatioLiquidNitrousOxideInput | Float |
| RatioLiquidNitrousOxideOutput | Float |
| RatioLiquidNitrousOxideOutput2 | Float |
| ReferenceId | Integer |
| NameHash | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| Temperature | Display |
| + | Touchkey |
| - | Touchkey |
| Power | Boolean |
| Open | Integer |
| Mode | Integer |
| Lock | Boolean |
| Setting | Integer |
| On | Boolean |

## IC10 Example

```ic10
alias device d0  # Air Conditioner
l r0 device Start
s device Temperature 1
```

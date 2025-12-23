---
title: Gas Fuel Generator
category: power
prefab_hash: 1165997963
---

# Gas Fuel Generator

**Prefab Hash**: `1165997963`

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Power | Boolean |
| Error | Boolean |
| Pressure | Float |
| Temperature | Float |
| RatioOxygen | Float |
| RatioCarbonDioxide | Float |
| RatioNitrogen | Float |
| RatioPollutant | Float |
| RatioVolatiles | Float |
| RatioWater | Float |
| RatioNitrousOxide | Float |
| RatioLiquidNitrogen | Float |
| RatioLiquidOxygen | Float |
| RatioLiquidVolatiles | Float |
| RatioSteam | Float |
| RatioLiquidCarbonDioxide | Float |
| RatioLiquidPollutant | Float |
| RatioLiquidNitrousOxide | Float |
| RatioHydrogen | Float |
| RatioLiquidHydrogen | Float |
| RatioPollutedWater | Float |
| Maximum | Integer |
| Ratio | Float |
| On | Boolean |
| RequiredPower | Float |
| PowerGeneration | Float |
| TotalMoles | Interger |
| PrefabHash |  |
| Combustion |  |

### Writable

| Logic Type | Description |
|------------|-------------|
| Setting | Float |
| On | Boolean |
| Setting | Float |

## IC10 Example

```ic10
alias device d0  # Gas Fuel Generator
l r0 device Power
s device Setting 1
```

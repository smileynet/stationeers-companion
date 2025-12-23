---
title: Active Vent
category: atmospheric
prefab_hash: -842048328
---

# Active Vent

**Prefab Hash**: `-842048328`

## Logic Types

### Readable

| Logic Type | Description |
|------------|-------------|
| Power | Boolean |
| 1 | On |
| Open | Integer |
| Mode | Integer |
| 1 | Inward |
| Error | Boolean |
| 1 | Error |
| PressureExternal | Float |
| PressureInternal | Float |
| Lock | Boolean |
| 1 | Locked |
| Setting | Integer |
| Maximum | Integer |
| Ratio | Float |
| On | Boolean |
| 1 | On |
| RequiredPower | Integer |
| PrefabHash | Integer |
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
| CombustionOutput | Boolean |
| 1 | Yes |
| ReferenceId | Integer |
| NameHash | Integer |

### Writable

| Logic Type | Description |
|------------|-------------|
| Power | Boolean |
| Open | Integer |
| Mode | Integer |
| PressureExternal | Float |
| PressureInternal | Float |
| Lock | Boolean |
| Setting | Integer |
| Maximum | Integer |
| On | Boolean |

## IC10 Example

```ic10
alias device d0  # Active Vent
l r0 device Power
s device Power 1
```

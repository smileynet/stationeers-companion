---
title: Battery
category: power
prefab_hash: 683671518
---

# Battery (Large)

Stores electrical power for later use. Essential for solar setups and backup power.

**Prefab Hash**: `683671518` (Large Battery)
**Small Battery Hash**: `-1900335881`

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|------|
| Charge | Current stored energy | J (Joules) |
| Maximum | Maximum capacity | J |
| Ratio | Charge / Maximum (0-1) | Ratio |
| Power | Current power throughput | W |
| PowerActual | Actual power being used | W |
| PowerPotential | Potential power available | W |
| On | Power state | Boolean |
| Error | Error state | Boolean |
| PrefabHash | Device type identifier | Hash |
| ReferenceId | Unique device ID | Integer |
| NameHash | Label hash | Hash |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|------|
| On | Enable/disable | Boolean |

## Common Use Cases

### Read Battery Percentage
```ic10
alias battery d0
l r0 battery Ratio      # 0.0 to 1.0
mul r0 r0 100           # Convert to percentage
```

### Monitor Total Bank Charge
```ic10
define LARGE_BATTERY 683671518
lb r0 LARGE_BATTERY Charge 1   # Sum of all charges
lb r1 LARGE_BATTERY Maximum 1  # Sum of all capacities
div r2 r0 r1                   # Overall ratio
mul r2 r2 100                  # Percentage
```

### Low Battery Warning
```ic10
alias battery d0
alias alarm d1
define LOW_THRESHOLD 0.2

l r0 battery Ratio
slt r1 r0 LOW_THRESHOLD
s alarm On r1           # Alarm if below 20%
```

## Notes

- Charge is in Joules, not kW or kJ
- Large Battery: 36,000,000 J capacity
- Small Battery: 3,000,000 J capacity
- Use batch operations for battery banks

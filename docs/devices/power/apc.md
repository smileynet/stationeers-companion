---
title: APC
category: power
prefab_hash: -1093957350
---

# APC (Area Power Controller)

**Prefab Hash**: `-1093957350`
**Power**: 10W (idle), varies with load

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Device is powered on | Boolean |
| Power | Current power consumption | Watts |
| MaxPower | Maximum power capacity | Watts |
| Voltage | Current voltage level | Volts |
| Frequency | Grid frequency (Hz) | Hz |
| NetworkDeviceCount | Number of connected devices | Integer |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|-------|
| On | Turn device on/off | Boolean (1=on, 0=off) |
| MaxPower | Set maximum power limit | Watts |

## IC10 Example

```ic10
# APC power monitoring
alias apc d0
alias battery d1

alias rPowerUsage r0
alias rBatteryLevel r1

main:
# Read APC power consumption
l rPowerUsage apc Power

# Read battery level
l rBatteryLevel battery Charge

# If battery low, reduce APC limit
define LOW_BATTERY 100000  # 100 kJ

slt r0 rBatteryLevel LOW_BATTERY
s apc MaxPower 5000      # Reduced power
beqz r0 normalPower

normalPower:
s apc MaxPower 10000     # Full power

yield
j main
```

## Usage Notes

1. **Power Distribution**: APC distributes power from generators/batteries to devices in its area.
2. **Automatic Switching**: Automatically switches between power sources based on availability.
3. **Overload Protection**: Trips if devices draw more than MaxPower setting.
4. **Area Isolation**: Each APC manages a specific area of the base.

## Common Patterns

### Priority-Based Power

Give priority to critical systems:

```ic10
# Check critical systems
l r0 airlockPower On
l r1 lifeSupportPower On

or r2 r0 r1              # If either critical
s apc MaxPower 8000       # Boost power

# Otherwise, normal power
s apc MaxPower 5000
```

### Battery Integration

Coordinate with battery charging:

```ic10
l r0 battery Charge       # Battery level
l r1 apc MaxPower       # APC limit

# If battery full, increase APC limit
sgt r2 r0 500000        # > 500 kJ
s apc MaxPower 10000

# If battery low, decrease APC limit
slt r2 r0 100000        # < 100 kJ
s apc MaxPower 5000
```

## Related Devices

- **Battery**: Stores energy for APC to distribute
- **Solar Panel**: Provides renewable power
- **Gas/Solid Fuel Generator**: Provides backup power
- **Transformer**: Steps voltage up/down

## See Also

- [battery.md](../power/battery.md) - Battery device reference
- [knowledge/power.md](../../knowledge/power.md) - Power system guide

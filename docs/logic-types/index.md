# Logic Types Reference

Logic types are properties that can be read from or written to devices via IC10.

## Categories

| Category | Description | File |
|----------|-------------|------|
| [Readable](readable.md) | Values you can read from devices | Temperature, Pressure, Ratio*, Power |
| [Writable](writable.md) | Values you can write to devices | On, Setting, Mode, Lock |
| [Slots](slots.md) | Slot-based properties | OccupantHash, Quantity, Damage |

## Reading Logic Types

```ic10
l r0 device LogicType      # Read from specific device
lb r0 hash LogicType mode  # Read from all devices of type (batch)
```

## Writing Logic Types

```ic10
s device LogicType value   # Write to specific device
sb hash LogicType value    # Write to all devices of type (batch)
```

## Common Logic Types by Device Category

### Atmospheric Devices
- `Pressure` - Atmospheric pressure (kPa)
- `Temperature` - Temperature (Kelvin)
- `RatioOxygen`, `RatioNitrogen`, etc. - Gas concentrations (0-1)

### Power Devices
- `Charge` - Current stored energy (J)
- `Maximum` - Maximum capacity (J)
- `Ratio` - Charge / Maximum (0-1)
- `PowerActual` - Current power flow (W)

### Logic Devices
- `Setting` - User-adjustable value (0-100 on dial)
- `Mode` - Operating mode
- `Error` - Error state (Boolean)

### All Devices
- `On` - Power/operating state (Boolean)
- `PrefabHash` - Device type identifier
- `ReferenceId` - Unique device ID
- `NameHash` - Label hash

## Finding Device Logic Types

1. Check device documentation in `docs/devices/`
2. Use the Stationeers Wiki
3. In-game: Look at device with tablet/labeler

## Notes

- Not all logic types exist on all devices
- Reading non-existent logic type returns 0
- Writing to read-only logic type has no effect
- Boolean values: 0 = false, non-zero = true

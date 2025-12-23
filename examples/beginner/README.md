# Beginner IC10 Examples

Start here if you're new to IC10 programming in Stationeers!

## Learning Path

### 1. Day/Night Light (`day-night-light.ic10`)
**Lines:** 8
**Concepts:** `alias`, `l` (load), `s` (store), `seqz`, `yield`, `j`

Your first script! Reads a daylight sensor and turns a light on at night.

```
d0 = Daylight Sensor
d1 = Light
```

### 2. Battery Generator (`battery-generator.ic10`)
**Lines:** 14
**Concepts:** `define`, comparison (`slt`, `sgt`), `select`, hysteresis

Monitors battery charge and turns on a backup generator when low.

```
d0 = Battery
d1 = Solid Fuel Generator
```

### 3. Solar Tracker (`solar-tracker-simple.ic10`)
**Lines:** 10
**Concepts:** Reading from one device, writing to another

Copies the sun position from a daylight sensor to a solar panel.

```
d0 = Daylight Sensor
d1 = Solar Panel (tracked)
```

## What's Next?

After mastering these, try:
- `../airlocks/` - Airlock cycling (state machines)
- `../patterns/hysteresis-template.ic10` - Temperature control
- `../patterns/pid-controller-template.ic10` - Precise control

## Tips for Beginners

1. **Always include `yield`** in your main loop, or the game will freeze
2. **Use `alias`** to give devices meaningful names
3. **Use `define`** for values you might want to change later
4. **Test one thing at a time** - add features gradually
5. **Check your wiring** - most "code bugs" are actually connection issues!

## Common Logic Types

| Type | Read/Write | Description |
|------|------------|-------------|
| `On` | R/W | Power state (0 or 1) |
| `Activate` | R | Sensor triggered state |
| `Ratio` | R | Percentage as 0-1 (battery charge) |
| `Temperature` | R | Temperature in Kelvin |
| `Pressure` | R | Pressure in kPa |
| `Horizontal` | R/W | Horizontal angle (0-360) |
| `Vertical` | R/W | Vertical angle (0-90) |

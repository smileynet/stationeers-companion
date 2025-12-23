# Writable Logic Types

Properties that can be written to devices using `s` or `sb` instructions.

## Universal Controls

| Logic Type | Description | Values | Devices |
|------------|-------------|--------|---------|
| On | Enable/disable | 0/1 | Most devices |
| Lock | Lock state | 0/1 | Doors, access |
| Setting | Dial value | 0-100 (varies) | Most devices |

## Doors and Vents

| Logic Type | Description | Values | Devices |
|------------|-------------|--------|---------|
| Open | Open/close | 0/1 | Doors, vents, shutters |
| Mode | Direction/mode | 0-2 | Vents, valves |

### Vent Modes
| Mode | Direction |
|------|-----------|
| 0 | Inward (fill room) |
| 1 | Outward (empty room) |

### Valve/Pump Modes
| Mode | Behavior |
|------|----------|
| 0 | Off |
| 1 | Forward |
| 2 | Reverse |

## Manufacturing

| Logic Type | Description | Values | Devices |
|------------|-------------|--------|---------|
| Activate | Start operation | 0/1 | Furnaces, fabricators |
| RecipeHash | Recipe to make | Hash | Fabricators |
| ClearMemory | Clear settings | 0/1 | Memory devices |

## Solar Tracking

| Logic Type | Description | Range | Devices |
|------------|-------------|-------|---------|
| Horizontal | Horizontal angle | 0-360 | Solar panels |
| Vertical | Vertical angle | 0-180 | Solar panels |

## Sorting/Filtering

| Logic Type | Description | Values | Devices |
|------------|-------------|--------|---------|
| Mode | Sort mode | 0-2 | Sorters |
| Output | Output slot | 0-2 | Sorters |

## Display

| Logic Type | Description | Range | Devices |
|------------|-------------|-------|---------|
| Setting | Display value | Any float | Consoles, LEDs |
| Color | LED color | 0-n | LED displays |
| Mode | Display mode | Integer | Consoles |

## Examples

### Basic On/Off Control
```ic10
alias device d0
s device On 1              # Turn on
s device On 0              # Turn off
```

### Vent Control
```ic10
alias vent d0
s vent On 1                # Enable vent
s vent Mode 0              # Set to inward (fill)
s vent Open 1              # Open the vent
```

### Conditional Control
```ic10
alias sensor d0
alias vent d1
define TARGET 101.325

l r0 sensor Pressure
sgt r1 r0 TARGET           # Above target?
s vent On r1               # Turn on if above
s vent Mode r1             # 1=outward if above, 0=inward if below
```

### Batch Control
```ic10
define VENT_HASH 1234567890
sb VENT_HASH On 1          # Turn on ALL vents of this type
sb VENT_HASH Mode 0        # Set ALL to inward mode
```

### Solar Panel Positioning
```ic10
alias panel d0
alias sensor d1

l r0 sensor SolarAngle     # Get sun angle
s panel Horizontal r0      # Set panel horizontal
s panel Vertical 60        # Set panel vertical
```

### Setting as User Input
```ic10
alias housing db
alias device d0

l r0 housing Setting       # Read dial (0-100)
s device Setting r0        # Apply to device
```

## Common Patterns

### Toggle Pattern
```ic10
alias button d0
alias light d1

l r0 button Activate       # Check button
beqz r0 skip               # Skip if not pressed
l r1 light On              # Get current state
xor r1 r1 1                # Toggle (0→1, 1→0)
s light On r1              # Apply new state
skip:
```

### Threshold Control
```ic10
alias sensor d0
alias actuator d1
define THRESHOLD 50

l r0 sensor Setting
sgt r1 r0 THRESHOLD        # Above threshold?
s actuator On r1           # Enable if above
```

## Notes

- Writing to read-only property has no effect
- Boolean: 0 = false/off, any non-zero = true/on
- Some devices require both On=1 AND Open=1 to operate
- Batch write affects ALL matching devices on network

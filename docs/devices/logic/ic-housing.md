---
title: IC Housing
category: logic
prefab_hash: 1512322581
---

# IC Housing

Holds and executes IC10 chips. The core device for programmable automation.

**Prefab Hash**: `1512322581` (2-slot)
**10-Slot Variant**: Different hash

## Logic Types

### Readable

| Logic Type | Description | Unit |
|------------|-------------|------|
| On | Power state | Boolean |
| Error | Script error state | Boolean |
| Setting | User-adjustable dial (0-100) | Float |
| Activate | External activation signal | Boolean |
| Power | Current power draw | W |
| RequiredPower | Power needed | W |
| PrefabHash | Device type identifier | Hash |
| ReferenceId | Unique device ID | Integer |
| NameHash | Label hash | Hash |

### Writable

| Logic Type | Description | Unit |
|------------|-------------|------|
| On | Enable/disable | Boolean |
| Setting | Set dial value | Float |

## Self-Reference (db)

Inside an IC10 script, use `db` to reference the IC Housing itself:

```ic10
l r0 db Setting        # Read the dial setting
l r1 db On             # Check if powered
l r2 db Error          # Check for errors
```

## Using Setting for Mode Selection

The Setting property (0-100 dial) is commonly used for user input:

```ic10
l r0 db Setting        # Read user's dial setting
beq r0 0 modeOff       # 0 = Off
beq r0 1 modeAuto      # 1 = Auto
beq r0 2 modeManual    # 2 = Manual
j modeOff              # Default
```

## Stack Memory

IC Housing has a 512-value internal stack accessible via `db`:

```ic10
put db 0 r0            # Write r0 to position 0
get r1 db 0            # Read from position 0
push r0                # Push to stack
pop r1                 # Pop from stack
```

## External Activation

Connect a button or lever to trigger the IC:

```ic10
l r0 db Activate       # Check if activated
bnez r0 handleActivation
```

## IC10 Example

```ic10
alias sensor d0
alias vent d1

# Use dial setting as target pressure
l r0 db Setting        # User sets target (e.g., 101)
l r1 sensor Pressure   # Current pressure
sgt r2 r1 r0           # Above target?
s vent On r2           # Turn on if over
yield
j 0
```

## Notes

- 2-slot housing holds 2 IC chips (use screwdriver to swap)
- 10-slot housing for more complex setups
- Error=1 means script crashed (usually missing yield)
- Setting range is 0-100, but can store any float

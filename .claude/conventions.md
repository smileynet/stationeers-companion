# Stationeers IC10 Programming Conventions

## Code Organization

### File Structure
```
examples/
  [category]/[feature-name].ic10
```

Categories:
- `beginner/` - Simple scripts for learning
- `atmosphere/` - Pressure, temperature, gas control
- `power/` - Solar, battery, generator management
- `airlocks/` - Door cycling logic
- `patterns/` - Reusable design patterns
- `temperature/` - Temperature control systems
- `gas-processing/` - Filtration, mixing, processing
- `growing/` - Greenhouse automation
- `manufacturing/` - Crafting automation
- `mining/` - Ore extraction and processing
- `rockets/` - Launch and orbital operations
- `trading/` - Satellite dish and cargo handling

### File Naming
- Use lowercase with hyphens: `solar-tracker.ic10`, `pressure-control.ic10`
- Be descriptive: `auto-furnace.ic10` not `furnace.ic10`
- Version variants with suffix: `script-v2.ic10`, `script-simple.ic10`

## Code Structure

### Required Sections (in order)
```ic10
# ==================================================
# [Script Name]
# ==================================================
# Description: [What this code does]
# Source: [GitHub/Wiki/URL if from external source]
#
# Devices:
#   d0 = [Device type] - [Purpose]
#   d1 = [Device type] - [Purpose]
#
# ==================================================

# === ALIASES ===
# Device connections first, then register aliases
alias device d0
alias rValue r0

# === CONSTANTS ===
# All magic numbers as defines
define TARGET 100
define HYSTERESIS 5

# === INITIALIZATION ===
# Setup code (optional)
move rTarget TARGET

# === MAIN LOOP ===
main:
# Main logic here
yield
j main

# === SUBROUTINES ===
# Optional: Reusable functions
subroutineName:
# Subroutine code
j ra
```

### Naming Conventions

**Aliases:**
- Devices: `[purpose]` (e.g., `roomSensor`, `pressureVent`)
- Registers: `r[CapitalizedPurpose]` (e.g., `rTemp`, `rTarget`)
- Be descriptive, not generic (`sensor` not `d0`, `roomSensor` better)

**Constants:**
- UPPERCASE with underscores: `MAX_PRESSURE`, `TARGET_TEMP`
- Include units in comments: `define TARGET 293.15  # 20C in Kelvin`

**Labels:**
- `camelCase` for jump targets: `main`, `checkPressure`, `fillTank`
- State machines: `stateIdle`, `stateFilling`, `stateDraining`

## Best Practices

### Always Include
1. **Header comments** - Purpose, devices, usage
2. **Yield in loops** - Prevents CPU overrun
3. **Device aliases** - Every d0-d5 should have meaningful alias
4. **Constants** - No magic numbers, use `define`
5. **Line count check** - Target < 100 lines for buffer

### Recommended Patterns
- **Hysteresis** - Use deadband for threshold control to prevent oscillation
- **Indirect registers** - Use `rr<N>` for array-like operations to save lines
- **State machines** - For multi-phase processes
- **Subroutines** - For repeated logic
- **Select** - Use instead of branch chains for ternary logic

### Anti-Patterns
- **Missing yield** - Causes CPU overrun error
- **Repeated device reads** - Cache in register
- **Branch tables** - Use `rr<N>` instead
- **Long lines** - Break up lines > 90 chars
- **No comments** - Add inline comments for complex logic

## Workflow Conventions

### When to Use Which Skill

| User Request | Use Skill |
|-------------|-----------|
| "Create code for..." | ic-generate (curates first) |
| "Find existing scripts" | ic-curate |
| "Show me an example" | ic-example |
| "What does this do?" | ic-explain |
| "Fix my broken code" | ic-debug |
| "Make this shorter" | ic-optimize |
| "Make this cleaner" | ic-refactor |
| "Check if this is valid" | ic-validate |
| "How do I use [instruction]?" | ic-lookup |

### Curation-First Approach

When generating code, always search external sources first:
1. `resource-curator` searches GitHub, Wiki, Reddit, Steam Workshop
2. Create guide in `guides/[topic]-resources.md`
3. Present top resources to user
4. Only generate custom code if user requests it or nothing found

**Bypass with phrases:** "generate new", "write fresh", "create from scratch", "don't search"

## Output Conventions

### Generated Code Location
- New code: `outputs/generated_[YYYY-MM-DD-HHMMSS].ic10`
- Optimized code: `outputs/optimized_[original-name].ic10`
- Validated reports: `outputs/validation_[timestamp].json`

### Guide Format
- External resources: `guides/[topic]-resources.md`
- Include: Summary, top resources, version compatibility, links
- Never copy full code - use 10-15 line previews

## External Tool Integration

### IC10 Validator
```bash
# For agent-based validation
uv run python -m tools.ic10_validator --stdin --format json

# For human-readable output
uv run python -m tools.ic10_validator --file code.ic10
```

### Steam Workshop Downloads
```bash
# Download specific workshop item
uv run python -m tools.steam_scraper --url "https://steamcommunity.com/sharedfiles/filedetails/?id=WORKSHOP_ID"
```

## Version Compatibility Notes

### Known Breaking Changes
- **Trading Update III (Dec 2022)** - Added tier system, interrogation mechanic
- **"Big Changes Coming" (Mar 2025)** - 256-byte stack, `TraderInstruction`, peek/poke

### Outdated Script Indicators
- No tier handling for trading
- No `InterrogationProgress` logic type
- Steam Workshop marked "incompatible"
- Last updated before 2023

### Current Script Indicators
- Uses peek/poke for stack operations
- Handles `TraderInstruction` enum
- References tier system
- Last updated 2024 or later

## Reference

### Device Categories
- Atmospheric: Vent, AC, Gas Sensor, Daylight Sensor
- Power: Solar Panel, Battery, Generator, Fuse
- Fabrication: Arc Furnace, Furnace, Autolathe, Centrifuge
- Logic: IC Housing, Logic IO, Logic Memory, Switch
- Doors: Door, Airlock, Airlock Gate
- Trading: Satellite Dish, Landing Pad
- Storage: Tank, Locker, Shelf

### Common Logic Types
**Readable:**
- `Power` - Boolean: is powered
- `On` - Boolean: is operating
- `Open` - Boolean: is open (doors/vents)
- `Temperature` - Float: in Kelvin
- `Pressure` - Float: in kPa
- `RatioOxygen`, `RatioNitrogen`, etc. - Float: 0-1

**Writable:**
- `On` - Boolean: turn on/off
- `Open` - Boolean: open/close
- `Lock` - Boolean: lock/unlock
- `Setting` - Float: target value
- `Mode` - Integer: operating mode

### Quick Reference

**Hard Limits:**
- Lines: ≤ 128
- Line length: ≤ 90 chars
- Total size: ≤ 4096 bytes
- Registers: r0-r15, ra, sp
- Devices: d0-d5, db

**Must Have:**
- yield or sleep in every loop
- All branch targets defined
- Valid instruction names

**Should Have:**
- Device aliases
- Constants with define
- Header comments
- bdns before optional devices

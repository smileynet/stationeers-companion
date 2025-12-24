# Stationeers Companion

Personal toolkit for Stationeers IC10 programming with Claude AI integration.

## Skills (Auto-Invoked)

Claude automatically uses these skills based on your request:

- **ic-generate** - When you ask to create IC10 code (curates external resources first)
- **ic-curate** - When you ask to find existing scripts or resources
- **ic-example** - When you ask for example code (searches local, then external)
- **ic-explain** - When you paste code and ask what it does
- **ic-debug** - When your IC10 code isn't working
- **ic-optimize** - When you want to improve code efficiency
- **ic-lookup** - When you ask about device properties or instructions
- **ic-refactor** - When you want to improve code structure and clarity
- **ic-validate** - When you want to check code for errors and constraint violations

Just describe what you need - Claude will select the right skill.

### Curation-First Approach

When you ask for IC10 code, the system searches external sources first:
- GitHub repositories (9 community repos)
- Steam Workshop (via SteamCMD)
- Stationeers Wiki
- Reddit r/stationeers
- Web tutorials and guides

Results are saved to `guides/` with links to original sources. Code generation only happens if nothing is found or you explicitly request it.

**Bypass curation** with phrases like "generate new", "write fresh", or "create from scratch".

### Agent Architecture

Skills orchestrate specialized agents that work in parallel or sequence:

**Research Agents** (read-only):
- `resource-curator` - Search external sources, create guides
- `instruction-researcher` - IC10 syntax lookup
- `device-researcher` - Device properties and logic values
- `pattern-finder` - Find local example code
- `code-analyzer` - Analyze code structure

**Implementation Agents** (write capable):
- `code-generator` - Generate IC10 code
- `code-debugger` - Debug and fix broken IC10 code
- `code-optimizer` - Reduce line count
- `code-refactorer` - Improve code structure and clarity
- `code-documenter` - Add documentation

Example workflow for `ic-generate`:
```
resource-curator ───────────→ guides/[topic]-resources.md
         │                              │
         v                              v
    Found resources? ─── YES ──→ Present + ask "want custom?"
         │                              │
         NO                            YES
         │                              │
         └──────────────────────────────┘
                        │
                        v
instruction-researcher ─┐
device-researcher ──────┼─→ code-generator ─→ code-documenter
pattern-finder ─────────┘
```

Example workflow for `ic-debug`:
```
code-debugger ─────────────────→ Fixed code
         │                              │
         v                              v
instruction-researcher ─┐            code-validator (optional)
device-researcher ──────┼─→ verification
```

Example workflow for `ic-optimize`:
```
code-analyzer ─────────────→ Analysis report
         │                              │
         v                              v
code-optimizer ─────────────→ Optimized code
```

## Project Structure

```
docs/                    IC10 reference documentation
  reference/             Instruction syntax and usage
  devices/               Device properties and logic values
  logic-types/           Logic type reference
examples/                Working IC10 code examples
  atmosphere/            Pressure, temperature control
  power/                 Solar, battery management
  airlocks/              Airlock cycling
  patterns/              Reusable patterns (PID, hysteresis)
guides/                  Curated external resource guides
knowledge/               Game knowledge base
  crafting/              Recipes
  gases/                 Gas properties
  hashes/                Prefab hashes for batch operations
tools/                   Python scraping utilities
outputs/                 Generated code output
```

## IC10 Quick Reference

### Constraints

- **Registers**: r0-r15 (general), ra (return address), sp (stack pointer)
- **Device ports**: d0-d5 (external), db (self/housing)
- **Code limits**: 128 lines max, 90 chars/line, 4096 bytes total
- **Execution**: 128 instructions per tick, always use `yield` in loops

### Common Instructions

```ic10
# Device I/O
l r0 device LogicType        # Load value from device
s device LogicType r0        # Store value to device
ls r0 device slot LogicType  # Load from slot
ss device slot LogicType r0  # Store to slot

# Batch operations (network devices by hash)
lb r0 hash LogicType mode    # Load batch (mode: 0=avg, 1=sum, 2=min, 3=max)
sb hash LogicType r0         # Store batch (to all matching devices)

# Math
add r0 r1 r2                 # r0 = r1 + r2
sub r0 r1 r2                 # r0 = r1 - r2
mul r0 r1 r2                 # r0 = r1 * r2
div r0 r1 r2                 # r0 = r1 / r2
mod r0 r1 r2                 # r0 = r1 % r2
abs r0 r1                    # r0 = |r1|
sqrt r0 r1                   # r0 = sqrt(r1)
min r0 r1 r2                 # r0 = min(r1, r2)
max r0 r1 r2                 # r0 = max(r1, r2)

# Comparison (sets r0 to 1 if true, 0 if false)
seq r0 r1 r2                 # r0 = (r1 == r2)
sne r0 r1 r2                 # r0 = (r1 != r2)
sgt r0 r1 r2                 # r0 = (r1 > r2)
slt r0 r1 r2                 # r0 = (r1 < r2)
sge r0 r1 r2                 # r0 = (r1 >= r2)
sle r0 r1 r2                 # r0 = (r1 <= r2)

# Branching
j label                      # Jump to label
jr offset                    # Jump relative by offset lines
beq r0 value label           # Branch if r0 == value
bne r0 value label           # Branch if r0 != value
bgt r0 value label           # Branch if r0 > value
blt r0 value label           # Branch if r0 < value
bge r0 value label           # Branch if r0 >= value
ble r0 value label           # Branch if r0 <= value

# Selection (ternary)
select r0 r1 r2 r3           # r0 = r1 ? r2 : r3

# Control
yield                        # Pause execution for one tick
sleep value                  # Sleep for value seconds
hcf                          # Halt and catch fire (stop)

# Utility
alias name register          # Create alias for register/device
define name value            # Define constant
move r0 r1                   # r0 = r1
```

### Code Template

```ic10
# Description: [What this code does]
# Devices: d0=[type], d1=[type], ...

# === ALIASES ===
alias sensor d0
alias actuator d1
alias rTemp r0
alias rTarget r1

# === CONSTANTS ===
define TARGET 293.15         # 20C in Kelvin

# === MAIN ===
main:
l rTemp sensor Temperature
sgt r2 rTemp TARGET
s actuator On r2
yield
j main
```

### Common Logic Types

**Readable (most devices)**:
- `Power` - Power state (0/1)
- `On` - Operating state (0/1)
- `Open` - Door/vent open state
- `Lock` - Lock state
- `Temperature` - In Kelvin
- `Pressure` - In kPa
- `Ratio*` - Gas ratios (RatioOxygen, RatioNitrogen, etc.)

**Writable**:
- `On` - Turn on/off
- `Open` - Open/close
- `Lock` - Lock/unlock
- `Setting` - Numeric setting (varies by device)
- `Mode` - Operating mode

### Best Practices

1. **Always yield in loops** - Prevents CPU overrun errors
2. **Use aliases** - Makes code readable and maintainable
3. **Use define for constants** - Easy to modify values
4. **Cache device reads** - Read once into register, use multiple times
5. **Comment device assignments** - Document which physical device goes where
6. **Stay under 128 lines** - Optimize when approaching limit
7. **Test incrementally** - Build up complexity gradually

## External Resources

- [Stationeers Wiki - IC10](https://stationeers-wiki.com/IC10)
- [IC10 Instructions Reference](https://stationeers-wiki.com/IC10/instructions)
- [Steam Workshop - Stationeers](https://steamcommunity.com/app/544550/workshop/) (requires SteamCMD to download scripts)
- [IC10 Simulator](https://ic10.dev/)
- [IC10 Emulator](https://ic10emu.dev/)

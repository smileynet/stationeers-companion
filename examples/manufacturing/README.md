# Manufacturing Examples

IC10 scripts for furnaces, production lines, and item routing.

## When You Need This

- Smelting advanced alloys
- Automating production chains
- Sorting and routing items
- Managing vending machines

## Difficulty

**Furnace control is the most complex automation in Stationeers.**

| Script | Lines | Complexity |
|--------|-------|------------|
| `furnace_control_simple.ic10` | Medium | Single furnace |
| `furnace_master.ic10` | High | Multi-furnace |
| `vending_manager.ic10` | High | Item routing |

## Key Concepts

**Furnace Control:**
- Must hit exact temperature AND pressure windows
- Different alloys have different requirements
- Use reagent hashes to detect contents

**Common Alloy Recipes:**
| Alloy | Temperature | Pressure | Ingredients |
|-------|-------------|----------|-------------|
| Steel | 800K+ | 1000kPa+ | Iron + Coal |
| Electrum | 295-400K | 1000kPa+ | Gold + Silver |
| Invar | 400-500K | 200kPa+ | Iron + Nickel |

**Item Routing:**
- Use slot hashes to identify items
- Stackers and sorters for organization
- Vending machines as buffers

## Start Here

1. `furnace_control_simple.ic10` - Learn the basics
2. `furnace.ic10` - More complete implementation
3. `furnace_master.ic10` - Multi-furnace coordination

## Prerequisites

Before attempting furnace automation:
- Understand PID control (`../patterns/pid-controller-template.ic10`)
- Know reagent hash system
- Have working gas supply for pressure control

# Mining Examples

IC10 code examples for mining and resource gathering automation in Stationeers.

## Quick Start by Skill Level

| Level | Example | Lines | Description |
|-------|---------|-------|-------------|
| **Beginner** | [ore-scanner.ic10](ore-scanner.ic10) | 15 | Display ore scanner data on screen |
| **Beginner** | [single-drill-controller.ic10](single-drill-controller.ic10) | 25 | Auto-activate drill with power management |
| **Beginner** | [simple-ore-sorter.ic10](simple-ore-sorter.ic10) | 30 | Route specific ore type to storage |
| **Intermediate** | [multi-drill-coordinator.ic10](multi-drill-coordinator.ic10) | 45 | Power-aware multi-drill sequencing |
| **Intermediate** | [conveyor-belt-controller.ic10](conveyor-belt-controller.ic10) | 40 | Transport system with flow control |
| **Intermediate** | [auto-smelter-array.ic10](auto-smelter-array.ic10) | 55 | Feed arc furnace from ore stockpile |
| **Advanced** | [mining-complex-controller.ic10](mining-complex-controller.ic10) | 90 | Full mining operation coordination |
| **Advanced** | [mining-state-machine.ic10](mining-state-machine.ic10) | 70 | Reusable template for mining operations |

## Beginner Examples

New to mining automation? Start here:

### [ore-scanner.ic10](ore-scanner.ic10) - 15 lines
**Difficulty:** Beginner | **Devices:** 2

Simple script that reads an ore scanner and displays the data on a screen. Great for understanding device I/O and continuous loops.

**Teaches:**
- Basic device reading (`l` instruction)
- Basic device writing (`s` instruction)
- Infinite loops with `yield`

### [single-drill-controller.ic10](single-drill-controller.ic10) - 25 lines
**Difficulty:** Beginner | **Devices:** 2-3

Automates a single mining drill with power-aware hysteresis control. Turns the drill on when battery charge is above 40%, off when below 30%.

**Teaches:**
- Hysteresis control pattern (deadband to prevent oscillation)
- Conditional branching (`bgt`, `blt`, `beq`)
- Power management considerations
- State change optimization (only write when needed)

### [simple-ore-sorter.ic10](simple-ore-sorter.ic10) - 30 lines
**Difficulty:** Beginner | **Devices:** 2

Routes a specific ore type to storage using hash-based detection. Configurable for any ore type (iron, gold, copper, etc.).

**Teaches:**
- Slot operations (`ls` instruction)
- Hash-based item identification
- Equality comparison (`seq`)
- Defines for configuration

## Intermediate Examples

Comfortable with basics? Ready for multi-device coordination:

### [multi-drill-coordinator.ic10](multi-drill-coordinator.ic10) - 45 lines
**Difficulty:** Intermediate | **Devices:** 5

Coordinates multiple mining drills based on available power. Activates different numbers of drills depending on battery charge level.

**Teaches:**
- Multi-device management
- Power budgeting
- Branching logic with multiple conditions
- Status display integration

### [conveyor-belt-controller.ic10](conveyor-belt-controller.ic10) - 40 lines
**Difficulty:** Intermediate | **Devices:** 3

Controls a conveyor belt transport system with item detection. Moves items from mining to storage area with flow control.

**Teaches:**
- Item detection and counting
- Flow rate control
- Feedback loops
- Conditional activation

### [auto-smelter-array.ic10](auto-smelter-array.ic10) - 55 lines
**Difficulty:** Intermediate | **Devices:** 5

Automates an arc furnace array that processes ores from a stockpile. Feeds furnaces, monitors output, and manages ingot storage.

**Teaches:**
- Batch operations (using `lb`/`sb`)
- Multi-unit coordination
- Idle state detection
- Processing pipeline integration

## Advanced Examples

Experienced with IC10? Building complex automation systems:

### [mining-complex-controller.ic10](mining-complex-controller.ic10) - 90 lines
**Difficulty:** Advanced | **Devices:** 6

Complete mining operation coordination using a state machine. Manages drilling, transport, sorting, and smelting in one integrated system.

**States:**
- IDLE: Waiting for power
- MINING: Drill activation
- TRANSPORT: Conveyor operations
- PROCESSING: Smelting active
- EMERGENCY: Low power shutdown

**Teaches:**
- State machine architecture
- Resource allocation
- Complex workflow management
- Emergency handling
- System integration

### [mining-state-machine.ic10](mining-state-machine.ic10) - 70 lines
**Difficulty:** Advanced | **Devices:** Variable

Reusable template for mining operation state machines. Customize states, transitions, and thresholds for your specific setup.

**Teaches:**
- State machine pattern
- Template customization
- Configurable thresholds
- Code organization for complex systems

## Related Resources

### Local Guides
- [Mining Resources Guide](../../guides/mining-resources.md) - Main mining hub with external resources
- [Mining Automation Beginner Guide](../../guides/mining-automation-beginner.md) - Detailed tutorials
- [Mining Automation Advanced Guide](../../guides/mining-automation-advanced.md) - Complex systems

### Related Examples
- [Manufacturing Examples](../manufacturing/) - Furnace, arc furnace, ore stacking
- [Patterns](../patterns/) - State machine, hysteresis, PID templates
- [Gas Processing](../gas-processing/) - Similar batch operation patterns

### Knowledge Base
- [Ore Hash Reference](../../knowledge/hashes/reagent-hashes.md) - Hash values for all ores
- [Crafting Recipes](../../knowledge/crafting/) - Smelting recipes and yields

## Common Patterns

### Hysteresis Control
Used in: `single-drill-controller.ic10`, `conveyor-belt-controller.ic10`

Prevents rapid on/off cycling by using separate thresholds for turning on and off.

```ic10
# Turn ON when value > 40
# Turn OFF when value < 30
# Do NOTHING when 30 <= value <= 40 (deadband)
```

### Hash-Based Sorting
Used in: `simple-ore-sorter.ic10`, `multi-drill-coordinator.ic10`

Identifies items by hash value for routing decisions.

```ic10
define TARGET_HASH -666742878  # Iron ore
ls r0 device 0 OccupantHash
seq r1 r0 TARGET_HASH          # r1 = 1 if iron
```

### State Machine
Used in: `mining-complex-controller.ic10`, `mining-state-machine.ic10`

Manages complex workflows through discrete states and transitions.

```ic10
# States: IDLE, MINING, TRANSPORT, PROCESSING, EMERGENCY
# Check conditions and transition between states
beq rState STATE_MINING doMining
beq rState STATE_TRANSPORT doTransport
```

## Contributing

Have a mining automation example to share? Consider:
1. Test your code in-game
2. Add comments following this style
3. Include difficulty level and line count
4. Document device requirements
5. Submit to the project

## Version Notes

- Tested on Stationeers version 1.0+ (current game mechanics)
- Ore hash values are stable across versions
- Drill behavior may change with game updates

## See Also

- [Main Mining Resources Guide](../../guides/mining-resources.md) - Comprehensive mining hub
- [External Resources](../../guides/mining-resources.md#best-external-resources) - Community scripts
- [IC10 Reference](../../docs/reference/) - Instruction reference

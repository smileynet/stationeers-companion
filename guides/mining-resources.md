# Mining and Resource Gathering Resources Guide

> Last updated: 2025-12-24
> Search terms: mining automation, drill controller, ore sorter, excavator, deep miner, centrifuge, arc furnace

## Summary

Mining automation is one of the most popular IC10 applications in Stationeers, allowing players to create fully automated ore extraction, processing, and storage systems. The game's mining ecosystem has evolved significantly with the Terrain Update, which introduced Deep Miners, Centrifuges, and chute-based logistics systems. These devices can be completely automated through IC10 scripts, enabling hands-off mining operations from resource extraction to smelting.

The mining automation landscape in Stationeers consists of several complementary systems: Deep Miners for autonomous ore extraction, Centrifuges for ore processing, Arc Furnaces for smelting, and chute/sorter networks for logistics. IC10 scripts can coordinate all these devices, creating end-to-end automation that requires minimal player intervention. Community resources range from simple single-device controllers to complex multi-chip systems that manage entire mining colonies.

## Best Resources

### 1. Fully Automated Deep Mining on One IC10 (Best Match)

**Source**: [Reddit r/Stationeers](https://www.reddit.com/r/Stationeers/comments/1cuiubr/fully_automated_lowconfiguration_deep_mining_on/)
**Quality**: 9/10
**Last Updated**: May 2024
**Status**: Current

**What it does**: This is an elegant deep mining automation solution that runs entirely on a single IC10 chip with no additional logic components. The only configuration required is appropriately naming sorters (e.g., "Sorter (Copper)") and arc furnaces using the in-game labeler. No screwdriver configuration needed.

**Key features**:
- Single-chip implementation
- Named-sorter configuration approach
- Includes MIPS program download and world file
- Copy-paste ready design
- Low configuration complexity

**Why it's notable**: This system demonstrates a clever approach to IC10 automation by using device names as configuration, eliminating the need for manual screwdriver settings. The author emphasizes that this makes the system easy to duplicate and share.

**Devices required**: IC10 chip, Deep Miners, Centrifuges, Arc Furnaces, Sorters, Refrigerated Vending Machine

---

### 2. Automatic Deep Miner Control (Steam Workshop)

**Source**: [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2886352385)
**Quality**: 8/10
**Status**: Unknown compatibility (needs verification)

**What it does**: A comprehensive Deep Miner Control System that creates a self-powering, endless source of ore. The script controls Deep Miners, Centrifuges, Refrigerated Vending Machine, Sorter, and Solid Generator in an integrated loop.

**Key features**:
- Automatic device initialization via batch writes
- Logic-controlled coal sorter (no manual computer setup)
- Battery charge ratio calculation for generator control
- Automatic item ejection from vending machine when stacks are full
- Configurable scanning ranges and thresholds
- Self-powering design (coal worlds only)

**Requirements**:
- 1+ Deep Miners (500W each)
- 3+ Centrifuges (100W each) - recommended ratio 2:5 (Deep Miner:Centrifuge)
- 1 IC Housing (50W)
- 1 Refrigerated Vending Machine (5W)
- 1 Sorter (5W)
- 1 Station Battery (any type)
- 1 IC10 Chip
- 1 Solid Generator
- Basic Chutes + Cable Coils

**Setup notes**:
- Must use electric Centrifuges (not Combustion Centrifuge)
- Isolate chip from main data network (uses batch commands)
- Use Heavy Cable for generator output to prevent melting
- Refrigerated Vending Machine required (has integrated stacker)
- Do not attempt to stack ingots (only ores)

**Pinout**:
```
d0 = Solid Generator
d1 = Sorter (coal)
d2 = Refrigerated Vending Machine
```

---

### 3. GitHub - exca/Stationeers-IC10-Automation

**Source**: [GitHub](https://github.com/exca/Stationeers-IC10-Automation)
**Quality**: 7/10
**License**: Available (check repository)
**Last Updated**: Active (63 commits)

**What it does**: Collection of automation projects including a Basic-to-IC10 compiler. While not exclusively focused on mining, contains relevant automation examples and tools that can be adapted for mining systems.

**Key projects**:
- Basic-to-IC10 Compiler - Write mining scripts in BASIC, compile to IC10
- Vending machine automation - Can be adapted for ore storage monitoring
- Printer automation with batch production - Applicable to manufacturing mining equipment

**Why it's useful**: The compiler approach may be valuable for players who find IC10's MIPS assembly challenging. You can write mining automation logic in BASIC and let the compiler handle the IC10 translation.

---

### 4. GitHub - Zappes/Stationeers (Silo Controller)

**Source**: [GitHub](https://github.com/Zappes/Stationeers)
**Quality**: 7/10
**License**: MIT License
**Last Updated**: Active (32 commits)
**Status**: Current

**What it does**: Contains a Silo Controller script designed for automated warehouse management of ores or ingots. This is particularly useful for managing the output of automated mining operations.

**Key features**:
- Silo Controller for storage automation
- Can handle ores or ingots
- Helps build "fully automated warehouse"
- Part of a larger collection of IC10 automation scripts

**Other relevant scripts in repository**:
- Temperature Controller - Useful for mining base environmental control
- Power Monitor - Important for monitoring mining operation power consumption
- Solar Tracker - Can help power remote mining operations

**License**: MIT License - Free to use, modify, and distribute

---

### 5. GitHub - jhillacre/stationeers-scripts

**Source**: [GitHub](https://github.com/jhillacre/stationeers-scripts)
**Quality**: 8/10
**License**: Open (check repository)
**Last Updated**: Active (114 commits)

**What it does**: Comprehensive collection of IC10 scripts with detailed documentation. Contains several scripts directly applicable to mining operations.

**Mining-related scripts**:
- `ore-stacker.ic10` - Automates ore stacking and logistics
- `arc-furnace-array.ic10` - Controls multiple arc furnaces for smelting operations
- `centrifuge-set-controller.ic10` - Manages centrifuge settings
- `printer-logistics.ic10` - Automated manufacturing and logistics

**Documentation**: Repository includes a `docs/` directory with detailed script documentation, status indicators, and implementation notes. Uses a status scale to indicate script maturity.

**Why it's notable**: This is one of the most documented and maintained IC10 script collections available. The author has invested significant effort in making the scripts accessible and understandable.

---

### 6. Steam Workshop - Automated Infinite Drill Station

**Source**: [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2971826224)
**Quality**: Unknown
**Status**: Unknown compatibility (needs verification)

**What it does**: An automated infinite drilling system with full code-based control and logging.

**Key features**:
- Completely coded and automated
- Automatic shutdown when containers are full
- Logged operations for monitoring
- Infinite drilling capability

**Note**: Requires SteamCMD to download actual code. Compatibility with current game version unknown.

---

### 7. Automated Arc Furnace (Steam Community)

**Source**: [Steam Community Discussion](https://steamcommunity.com/app/544550/discussions/0/1644290549102339085/)
**Quality**: Community discussion (not a script)
**Status**: Multi-language discussion

**What it does**: Community discussion about automated arc furnace setups. While not providing a specific IC10 script, this thread may contain valuable insights and approaches for automating arc furnace operations in mining systems.

---

## Categorized Resources

### Beginner Resources

**For players new to IC10 mining automation**:

1. **[Reddit - Fully Automated Deep Mining](https://www.reddit.com/r/Stationeers/comments/1cuiubr/fully_automated_lowconfiguration_deep_mining_on/)**
   - Single-chip solution
   - Minimal configuration
   - Complete with video tour

2. **[Stationeers Wiki - IC10](https://stationeers-wiki.com/IC10)**
   - Official IC10 reference
   - Instruction syntax and usage
   - Best practices

3. **[YouTube - Deep Miner Kit Setup Tips](https://www.youtube.com/watch?v=Lfmz4COLM4g)**
   - Visual learning
   - Hardware setup focus
   - Dead Meme Gaming (13K views)

4. **[Steam Guide - Basic Programming With IC10](https://steamcommunity.com/sharedfiles/filedetails/?id=2616382866)**
   - Fundamentals of IC10
   - Functions and device naming
   - Programming basics

---

### Intermediate Systems

**For players comfortable with IC10, looking for multi-device coordination**:

1. **[Steam Workshop - Automatic Deep Miner Control](https://steamcommunity.com/sharedfiles/filedetails/?id=2886352385)**
   - Multi-device coordination
   - Self-powering system
   - Complex logistics

2. **[GitHub - jhillacre arc-furnace-array](https://github.com/jhillacre/stationeers-scripts)**
   - Multi-furnace control
   - Automated smelting
   - Well-documented code

3. **[YouTube - Episode 34: Deep Mining With Automation](https://www.youtube.com/watch?v=OdOxdW4S4ic)**
   - Let's Play format
   - Late-game automation
   - IC10 code examples

---

### Advanced Automation

**For experienced IC10 programmers seeking full colony automation**:

1. **[GitHub - jhillacre ore-stacker](https://github.com/jhillacre/stationeers-scripts)**
   - Complex logistics management
   - Ore sorting and storage
   - Production-line automation

2. **[GitHub - Zappes Silo Controller](https://github.com/Zappes/Stationeers)**
   - Warehouse-scale automation
   - MIT licensed
   - Integrated with other automation scripts

3. **[GitHub - exca Basic-to-IC10 Compiler](https://github.com/exca/Stationeers-IC10-Automation)**
   - Write complex logic in BASIC
   - Compile to optimized IC10
   - Easier maintenance

---

## Version Compatibility

| Resource | Last Updated | Status | Notes |
|----------|--------------|--------|-------|
| Reddit - Single-Chip Deep Mining | May 2024 | **Current** | Uses modern naming-based configuration |
| Steam Workshop - Deep Miner Control | Unknown | **Unknown** | Needs verification with current version |
| exca/Stationeers-IC10-Automation | Active | **Current** | 63 commits, actively maintained |
| Zappes/Stationeers | Active | **Current** | 32 commits, MIT license |
| jhillacre/stationeers-scripts | Active | **Current** | 114 commits, well-documented |
| Steam Workshop - Infinite Drill | Unknown | **Unknown** | Last updated date not visible |

**Version Notes**: Stationeers mining mechanics have evolved significantly with the Terrain Update. Resources from before 2023 may reference outdated Deep Miner or Centrifuge behavior. All resources listed above appear to be from 2023 or later, indicating compatibility with current game mechanics.

---

## Tutorials & Guides

| Title | Source | Description | Difficulty |
|-------|--------|-------------|------------|
| [Deep Miner Kit Setup Tips](https://www.youtube.com/watch?v=Lfmz4COLM4g) | YouTube (Dead Meme Gaming) | Hardware setup for Deep Miner systems | Beginner |
| [Episode 34: Deep Mining With Automation](https://www.youtube.com/watch?v=OdOxdW4S4ic) | YouTube | Complete automated deep mining setup | Intermediate |
| [Basic Programming With IC10](https://steamcommunity.com/sharedfiles/filedetails/?id=2616382866) | Steam Workshop | IC10 fundamentals and programming basics | Beginner |
| [How to Program Anything with IC10](https://steamcommunity.com/sharedfiles/filedetails/?id=3288129161) | Steam Workshop | Comprehensive IC10 programming guide | Beginner-Intermediate |
| [Stationeers 101 EP 5: Automated Deep Miner](https://www.youtube.com/watch?v=jNjK1FuGnSg) | YouTube | Automated deep miner and centrifuge setup | Intermediate |
| [Thorough Intro to MIPS IC10 Assembly](https://www.youtube.com/watch?v=dhTiHMBKVrs) | YouTube | In-depth IC10/MIPS assembly tutorial | Intermediate-Advanced |
| [Easy Introduction to IC10](https://www.youtube.com/playlist?list=PLRHmcqMWXdLBdNBD3xHhnUK32NaWlXcBU) | YouTube (Playlist) | Complete IC10 programming course | Beginner-Intermediate |

---

## Community Discussions

### Reddit
- **[Fully Automated, Low-Configuration Deep Mining on One IC10](https://www.reddit.com/r/Stationeers/comments/1cuiubr/fully_automated_lowconfiguration_deep_mining_on/)** - Discussion about elegant single-chip mining automation with community Q&A

### Steam Community
- **[Automated Arc Furnace](https://steamcommunity.com/app/544550/discussions/0/1644290549102339085/)** - Multi-language discussion on arc furnace automation approaches
- **[Deep Miner, Centrifuges, and Chutes](https://steamcommunity.com/app/544550/eventcomments/5241649843398292196)** - Announcement and discussion of the Terrain Update mining automation features

---

## Common Mining Automation Patterns

### Device Integration Patterns

**1. Deep Miner → Centrifuge → Vending Machine Flow**
```
Deep Miner (ore) → Centrifuge (dirty ore) → Vending Machine (storage)
```
Most automated mining systems follow this basic flow, with IC10 scripts monitoring and controlling each stage.

**2. Coal-Based Self-Power Systems**
```
Centrifuge → Sorter (coal filter) → Solid Generator → Station Battery
              ↓                      ↓
         reject (ores)        power to all devices
```
Several resources implement self-powering loops using coal from centrifuges.

**3. Batch Operations**
- Use `lb` (load batch) and `sb` (store batch) for controlling multiple identical devices
- Efficiently manage arrays of Deep Miners or Centrifuges with single commands
- Note: Requires isolating chip from main data network

### Configuration Approaches

**1. Named-Based Configuration**
- Name devices descriptively (e.g., "Sorter (Copper)", "Furnace 1")
- IC10 script reads device names to determine function
- Advantages: Easy to set up, no screwdriver needed, copy-paste friendly
- Example: Reddit single-chip solution

**2. Slot-Based Configuration**
- Use device slots to identify function
- Configure via screwdriver
- Advantages: More flexible, supports dynamic reconfiguration
- Example: Most Steam Workshop scripts

**3. Hybrid Approach**
- Combine naming and slot-based approaches
- Use naming for human readability, slots for programmatic access
- Best of both worlds but higher complexity

---

## Frequently Used Logic Types for Mining

### Deep Miner Logic Types
- `On` - Enable/disable mining (0/1)
- `Setting` - Target ore type to mine
- `Power` - Current power state
- `Enabled` - Operational status

### Centrifuge Logic Types
- `On` - Enable/disable centrifuge (0/1)
- `Setting` - Operation mode/settings
- `Power` - Current power state
- `Ratio*` - Gas ratios (for combustion centrifuges)
- `Temperature` - Operating temperature

### Arc Furnace Logic Types
- `On` - Enable/disable furnace (0/1)
- `Setting` - Target recipe
- `Power` - Current power state
- `Temperature` - Operating temperature
- `Pressure` - Internal pressure

### Sorter Logic Types
- `On` - Enable/disable sorter (0/1)
- `Mode` - Sort mode: 0=Split, 1=Filter (Motherboard only), 2=Logic (IC10)
- `Output` - Output: 0=straight, 1=side (requires Mode 2)
- `Lock` - Lock configuration
- `ClearMemory` - Clear settings

**Note**: Mode 1 (Filter) requires Motherboard with whitelist configured via computer interface and is NOT IC10-controllable. For IC10 control, use Mode 2 (Logic mode) with the `Output` logic type, or read `OccupantHash` from slots to activate connected stackers.

### Vending Machine Logic Types
- `Type*` - Item type in slot (asterisk = slot number)
- `Amount*` - Quantity in slot
- `MaxAmount*` - Maximum stack size
- `Setting` - Configuration setting

### Battery Logic Types
- `Charge` - Current charge level
- `Capacity` - Maximum capacity
- `Power` - Power I/O state

---

## Power Considerations

### Device Power Requirements (Typical)
- Deep Miner: 500W
- Electric Centrifuge: 100W
- Combustion Centrifuge: Variable (fuel-based)
- Arc Furnace: 800W (operational), varies during heating
- IC Housing: 50W
- Refrigerated Vending Machine: 5W
- Sorter: 5W

### Power Management Strategies

**1. Battery Buffering**
- Always include Station Battery or Station Battery (Large)
- Smooths out power spikes from arc furnace heating
- Provides backup during generator startup

**2. Generator Control**
- Monitor battery charge ratio
- Enable Solid Generator when battery < threshold
- Disable generator when battery > threshold
- Use Heavy Cable for generator output (prevents melting)

**3. Solar Supplement**
- Use solar trackers to supplement power during day
- Reduce generator fuel consumption
- Particularly useful for remote mining operations

---

## Best Practices Notes

### 1. Isolate Batch Operations
When using `lb`/`sb` (load/store batch) commands for controlling multiple devices:
- Isolate the IC10 chip from your main data network
- Prevents unintended writes to unrelated devices
- Use separate network switches or distinct data networks

### 2. Use Refrigerated Vending Machines
- Integrated stacker allows simultaneous stacking of all ore types
- Cannot stack ingots (ores only)
- Essential for multi-ore mining operations
- Significantly reduces chute complexity

### 3. Ratio Your Devices
**Recommended Deep Miner to Centrifuge ratio**: 2:5
- 2 Deep Miners can feed 5 Centrifuges
- Some centrifuges may be idle briefly
- Better to have excess centrifuge capacity
- Adjust based on your ore mix and power availability

### 4. Plan for Overflow
- Single stack of coal contains more energy than Station Battery can store
- Use Chute Overflow to redirect excess coal
- Add buffer chutes before Solid Generator input
- Prevents system shutdowns from full chutes

### 5. Heavy Cable for Generators
- Solid Generator output must use Heavy Cable
- Normal cable will melt from generator output
- Connect generator output directly to battery input
- Use wattage-appropriate cable for other connections

### 6. Label Everything
- Use labeler on all devices (sorters, furnaces, etc.)
- Name devices descriptively ("Sorter (Copper)", "Furnace 1")
- Makes scripts more readable and debuggable
- Enables name-based configuration approaches

### 7. Monitor IC10 Execution Limits
- IC10 executes 128 lines per tick before force-yielding
- Vending machine slot scans are expensive operations
- Limit slots scanned per tick
- Use configurable scan ranges
- Consider spreading scans across multiple ticks

---

## Alternative Approaches

### AIMEe Robot Mining
While not covered in detail in the resources found, Stationeers supports autonomous mining robots (AIMEe units). These can be programmed with IC10 and may offer an alternative to stationary Deep Miners for certain mining scenarios. Search for "Stationeers AIMEe mining" for more information.

### Manual-First Design
Some players prefer to build manual mining operations first, then gradually automate:
1. Start with manual Deep Miner operation
2. Add simple chute-based sorting
3. Automate centrifuges with IC10
4. Add furnace automation
5. Implement full IC10 control of entire system

### Hybrid Automation
Combine IC10 control with passive automation:
- IC10 for complex logic (battery management, device control)
- Chutes and sorters for simple routing
- Logic gates for basic on/off control
- Reduces IC10 code complexity

---

## Known Issues and Limitations

### Refrigerated Vending Machine Limitations
- Cannot stack ingots, only ores
- Maximum stack size varies by ore type
- Slot scanning is IC10-intensive
- Consider slot scanning when designing scripts

### Combustion Centrifuge Complexity
- Most public scripts focus on electric centrifuges
- Combustion centrifuges require additional logic (fuel, temperature, pressure)
- More complex to automate
- May be better suited for advanced IC10 programmers

### Network Isolation Requirements
- Batch operations (`lb`/`sb`) can affect unintended devices
- Requires network isolation or careful hash selection
- Adds complexity to base design
- Document your network architecture

### World-Specific Considerations
- Self-powering systems only work on worlds with coal
- Ice worlds may require alternative power sources
- Consider world type when selecting automation approach

---

## Additional Resources

### Development Tools
- **[IC10 Simulator](https://ic10.dev/)** - Test IC10 code outside the game
- **[IC10 Emulator](https://ic10emu.dev/)** - Another IC10 testing environment
- **[IC10 VS Code Extension](https://marketplace.visualstudio.com/)** - Syntax highlighting and validation (mentioned in several repos)

### Community Hubs
- **[Stationeers Wiki](https://stationeers-wiki.com/)** - Official game documentation
- **[r/Stationeers](https://www.reddit.com/r/stationeers/)** - Active community discussion
- **[Steam Community](https://steamcommunity.com/app/544550/discussions/)** - Official forums

### Related Guides
- **[Power Management Guide](power-management.md)** - Battery systems and generator control
- **[Atmosphere Automation](atmosphere-automation.md)** - Life support systems

---

## Notes

**License Information**:
- GitHub resources generally have explicit licenses (check each repository)
- Reddit and Steam Community resources may have informal licensing
- Always check before using code in your own projects

**Attribution**:
This guide links to external content. Original authors retain all rights to their code. If you use these resources in your own projects, please credit the original authors.

**Contribution**:
If you find additional mining automation resources or notice broken links, consider contributing to the community by sharing them on r/Stationeers or in the Stationeers Discord.

---

**Sources**:
- [Fully Automated Deep Mining on One IC10 - Reddit](https://www.reddit.com/r/Stationeers/comments/1cuiubr/fully_automated_lowconfiguration_deep_mining_on/)
- [Automatic Deep Miner Control - Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2886352385)
- [exca/Stationeers-IC10-Automation - GitHub](https://github.com/exca/Stationeers-IC10-Automation)
- [Zappes/Stationeers - GitHub](https://github.com/Zappes/Stationeers)
- [jhillacre/stationeers-scripts - GitHub](https://github.com/jhillacre/stationeers-scripts)
- [Automated Infinite Drill Station - Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2971826224)
- [IC10 Reference - Stationeers Wiki](https://stationeers-wiki.com/IC10)
- [Deep Miner Kit Setup - YouTube](https://www.youtube.com/watch?v=Lfmz4COLM4g)
- [Deep Mining With Automation - YouTube](https://www.youtube.com/watch?v=OdOxdW4S4ic)
- [Automated Arc Furnace Discussion - Steam Community](https://steamcommunity.com/app/544550/discussions/0/1644290549102339085/)
- [Deep Miner, Centrifuges, and Chutes - Steam Community](https://steamcommunity.com/app/544550/eventcomments/5241649843398292196)

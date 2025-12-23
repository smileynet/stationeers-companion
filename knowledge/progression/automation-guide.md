# Stationeers Automation Guide

When to use automation, what to automate first, and which examples to use.

## Quick Reference: What to Automate When

| Game Stage | Days | Top Automation Priority | Recommended Approach |
|------------|------|------------------------|---------------------|
| 1. Survival | 1-3 | Solar tracking, night lights | Logic chips OR simple IC10 |
| 2. Resources | 3-7 | Battery backup, water heating | Logic chips OR IC10 |
| 3. Shelter | 7-14 | Airlocks, storm warnings | IC10 recommended |
| 4. Growing | 14-30 | Temperature, pressure, lights | IC10 required |
| 5. Gas Processing | 30-60 | Filtration, fuel mixing | IC10 required |
| 6. Manufacturing | 60+ | Furnaces, vending routing | Complex IC10 |
| 7. Trading | 90+ | Satellites, traders | Complex IC10 |

---

## Stage 1: Immediate Survival (Days 1-3)

### Your Goals
- Set up power (solar panel + battery)
- Basic smelting (arc furnace)
- Basic crafting (autolathe)

### Automation Opportunities

**1. Day/Night Lighting**
- Problem: Manually turning lights on at night
- Solution: `examples/beginner/day-night-light.ic10`
- Complexity: 8 lines, perfect first script

**2. Solar Panel Tracking**
- Problem: Solar panels don't face the sun automatically
- Solution: `examples/beginner/solar-tracker-simple.ic10`
- Complexity: 10 lines

**3. Generator Backup**
- Problem: Power runs out at night
- Solution: `examples/beginner/battery-generator.ic10`
- Complexity: 14 lines, teaches hysteresis

### Can I Use Logic Chips Instead?

Yes! At this stage, Logic Reader/Writer/Compare chips work fine:
- Day/night light: Daylight sensor → Logic Compare → Light
- Generator backup: Battery → Logic Compare → Generator

IC10 is *optional* but good for learning.

---

## Stage 2: Resource Independence (Days 3-7)

### Your Goals
- Secure water (ice crusher)
- Electronics printer + pipe bender
- Liquid piping network

### Automation Opportunities

**1. Water Temperature Control**
- Problem: Water freezes if too cold
- Solution: `examples/atmosphere/water-temp-control.ic10`
- Why: Keeps water liquid for bottle filling

**2. Tank Level Monitor**
- Problem: Tank runs empty unnoticed
- Solution: Pressure sensor on tank + display
- Pattern: `examples/patterns/hysteresis-template.ic10`

### Logic Chips vs IC10

Logic chips still work here. Use IC10 when:
- You need hysteresis (two thresholds)
- You're controlling multiple devices from one sensor
- You want to display status on a console

---

## Stage 3: Shelter & Power Hardening (Days 7-14)

### Your Goals
- Airtight base (walls, doors, airlocks)
- Station batteries
- Storm survival (Mars/Europa)

### Automation Opportunities

**1. Airlock Cycling** ⭐ IC10 Strongly Recommended
- Problem: Manual airlock operation is tedious
- Solution: `examples/airlocks/` (multiple patterns)
- Why IC10: State machines are impractical with logic chips

**2. Storm Warning System**
- Problem: Storms can kill you outside
- Solution: `examples/atmosphere/storm-recall-controller.ic10`
- Features: Klaxon alarm, suit notification, door auto-close

**3. Tracked Solar Panels**
- Problem: Fixed panels lose efficiency
- Solution: Full solar tracker with vertical adjustment
- Files: Look for solar examples in `examples/power/`

### The Airlock Decision Point

This is where most players transition to IC10. Airlocks require:
- State tracking (IDLE → DEPRESSURIZING → OPENING → CLOSING → REPRESSURIZING)
- Multiple device coordination (vents, doors, lights)
- Safety interlocks

With logic chips: 10-15 components, hard to debug
With IC10: 30-50 lines, easy to modify

---

## Stage 4: Atmosphere & Growing (Days 14-30)

### Your Goals
- Hydroponics trays with water
- CO₂/O₂ production
- Temperature control for plants
- Grow lights

### Automation Opportunities

**1. Room Temperature Control** ⭐ Essential
- Problem: Plants die outside their temperature range
- Solution: `examples/patterns/pid-controller-template.ic10`
- Advanced: `examples/atmosphere/temperature-controlled-room.ic10`

**2. Pressure Regulation**
- Problem: Room pressure drifts with gas production
- Solution: `examples/patterns/hysteresis-template.ic10`
- Pattern: Active vent with two pressure thresholds

**3. Grow Light Cycle**
- Problem: Lights waste power at night (some plants need dark)
- Solution: Daylight sensor → light control (like Stage 1)

**4. Greenhouse Air Quality**
- Problem: CO₂/O₂ ratios affect plant growth
- Solution: `examples/atmosphere/greenhouse_air_quality.ic10`

### Key Patterns to Learn

| Pattern | Use Case | Example File |
|---------|----------|--------------|
| Hysteresis | On/off with deadband | `patterns/hysteresis-template.ic10` |
| PID Control | Precise targeting | `patterns/pid-controller-template.ic10` |
| State Machine | Multi-step processes | `patterns/state-machine-template.ic10` |

---

## Stage 5: Gas Processing (Days 30-60)

### Your Goals
- Filtration systems for pure gases
- Storage tanks
- Fuel mixing (H₂ + O₂)
- Advanced alloys

### Automation Opportunities

**1. Filtration Control**
- Problem: Need to filter specific gases to specific tanks
- Solution: `examples/atmosphere/filtercontroller.ic10`

**2. Fuel Mixing**
- Problem: Fuel cells need precise H₂/O₂ ratio
- Solution: `examples/atmosphere/gas-mixer-fuel-regulator.ic10`
- Note: Temperature affects mixing calculations

**3. Tank Pressure Management**
- Problem: Tanks can over-pressurize
- Solution: `examples/atmosphere/tank-pressure-regulator.ic10` (or similar)

### Gas Processing Requires IC10

Logic chips cannot:
- Calculate ratios
- Handle multiple conditions (temp AND pressure)
- Coordinate multiple pumps/valves

---

## Stage 6: Furnace & Manufacturing (Days 60+)

### Your Goals
- Advanced furnace (alloys like Invar, Electrum)
- Precise temperature/pressure control
- Automated production pipelines

### Automation Opportunities

**1. Furnace Temperature Control** ⭐ Critical
- Problem: Alloys require exact temp/pressure windows
- Solution: `examples/atmosphere/furnace_control_simple.ic10`
- Advanced: Multi-furnace coordination

**2. Vending Machine → Furnace Pipeline**
- Problem: Manually moving ores to furnace is tedious
- Solution: `examples/atmosphere/vending_manager.ic10`
- Pattern: Read vending contents, route to correct machine

**3. Ingot Sorting**
- Problem: Mixed ingots from furnace
- Solution: Stack writer systems, sorters with hash detection

### Complexity Jump

Furnace automation is significantly more complex:
- Recipe detection (reagent hashes)
- Precise timing (smelt cycles)
- Multi-device coordination
- Often uses IC stack for data storage

Start with `furnace_control_simple.ic10` before attempting master controllers.

---

## Stage 7: Trading & Endgame (Days 90+)

### Your Goals
- Satellite communication
- Trader interaction
- Ship construction

### Automation Opportunities

**1. Satellite Dish Tracking**
- Problem: Manual dish pointing is slow
- Solution: `examples/trading/sky-scan.ic10` (or similar)
- Features: Auto-scan, signal lock, interrogation

**2. Trader Management**
- Problem: Multiple traders, need to select which to call
- Solution: Full trader controller with selection
- Pattern: State machine + signal storage

### Endgame Complexity

Trading automation requires:
- State machines with 5+ states
- Array storage (signal IDs)
- Indirect register addressing (`rr<N>`)
- Multiple device coordination

---

## Choosing Logic Chips vs IC10

### Use Logic Chips When:
- Single condition → single action
- Learning the game basics
- Power is limited (chips use less power)
- You have space for the component layout

### Use IC10 When:
- Multiple conditions (AND/OR logic)
- State machines (multi-step processes)
- Calculations needed (ratios, PID)
- Space is limited (1 IC vs 10 chips)
- You want display output

### Transition Path

```
Logic Chips → Simple IC10 → State Machines → Complex Systems
   │              │              │               │
   └── Stage 1-2  └── Stage 3    └── Stage 4-5   └── Stage 6-7
```

---

## Example Directory Guide

| Directory | Stage | Description |
|-----------|-------|-------------|
| `examples/beginner/` | 1-2 | First scripts, 5-15 lines |
| `examples/airlocks/` | 3+ | Airlock patterns |
| `examples/patterns/` | 3+ | Reusable templates |
| `examples/atmosphere/` | 4+ | Pressure, vents, basic HVAC |
| `examples/temperature/` | 4+ | Heating, cooling, AC |
| `examples/growing/` | 4+ | Hydroponics, greenhouses |
| `examples/gas-processing/` | 5+ | Filtration, mixing |
| `examples/manufacturing/` | 6+ | Furnaces, vending |
| `examples/trading/` | 7+ | Satellites, traders |

---

## Quick Start Checklist

1. [ ] Complete `examples/beginner/day-night-light.ic10` - your first script
2. [ ] Try `examples/beginner/battery-generator.ic10` - learn hysteresis
3. [ ] Study `examples/patterns/hysteresis-template.ic10` - reusable pattern
4. [ ] Attempt an airlock from `examples/airlocks/` - first state machine
5. [ ] Graduate to temperature control for greenhouses
6. [ ] Tackle furnace automation when you reach alloys

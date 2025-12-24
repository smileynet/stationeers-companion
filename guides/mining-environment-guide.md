# Environment-Specific Mining Guide

Adapt mining operations for different planetary environments.

## Difficulty: All Levels | Prerequisites: None

This guide covers how mining strategies, equipment, and automation vary across Mars, Moon, Venus, and other environments.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Mars Surface Mining](#mars-surface-mining)
3. [Moon/Asteroid Mining](#moonasteroid-mining)
4. [Venus/Underground Mining](#venusunderground-mining)
5. [Universal Principles](#universal-principles)
6. [Code Adaptation Examples](#code-adaptation-examples)

---

## Introduction

### Environment Matters

Each environment in Stationeers presents unique challenges:

- **Atmosphere** affects breathing and equipment
- **Temperature** impacts power needs and survival
- **Solar availability** changes power strategy
- **Ore distribution** varies by location

### Adaptation Strategy

**Universal Concepts:**
- Ore detection (hand scanner)
- Drill operation (same mechanics)
- Hash-based sorting (works everywhere)
- IC10 logic (environment-independent)

**Environment-Specific:**
- Power thresholds (adjust in code)
- Temperature management
- Life support requirements
- Equipment protection

---

## Mars Surface Mining

### Environment Characteristics

| Property | Value | Impact |
|----------|-------|--------|
| **Atmosphere** | Thin CO2 (5-10 kPa) | Can't breathe, pressure suit needed |
| **Temperature** | -60°C to 20°C | Cold nights, moderate days |
| **Solar** | Good day/night cycle | Viable solar power |
| **Ore Distribution** | Balanced variety | All ore types available |

### Mining Strategy

**Best Approach:**
- **Surface mining** for early game (iron, carbon)
- **Underground mining** for mid-game (gold, silver)
- **Deep mining** for late game (uranium, cobalt)

**Advantages:**
- Best overall environment for mining
- Solar power viable
- Moderate temperatures
- Good ore variety

**Challenges:**
- Dust storms reduce visibility/solar
- Thin atmosphere requires life support
- Cold nights increase power usage

### Power Considerations

**Solar Power:**
```
Day: Abundant solar
Night: ~500 seconds (8 minutes)

Batteries needed: 30-50 for overnight
Solar panels: 20-30 for medium operation
```

**Temperature Power Draw:**
- Day: Minimal heating/cooling
- Night: ~200-500W for habitat heating

### Code Adaptations

**Baseline Code:** Mars (standard thresholds)

```ic10
# Standard power thresholds for Mars
define POWER_HIGH 70  # Turn on drills
define POWER_LOW 30   # Turn off drills
```

**Temperature Monitoring (Optional):**
```ic10
# Monitor habitat temperature
alias heater d0
alias tempSensor d1

l rTemp tempSensor Temperature
blt rTemp 293.15 turnOnHeater  # Below 20°C
j endTick

turnOnHeater:
s heater On 1
j endTick
```

### Base Design

**Recommended Layout:**
```
[Pressurized Habitat] (living + command)
         │
    [Solar Array + Battery]
         │
[Processing Area] (unpressurized OK)
         │
    [Mining Drills]
```

**Construction:**
- Metal walls for habitat pressure
- Airlock for entry/exit
- Sealed structure (dust protection)
- Solar array on roof or nearby

---

## Moon/Asteroid Mining

### Environment Characteristics

| Property | Value | Impact |
|----------|-------|--------|
| **Atmosphere** | Vacuum (0 kPa) | Full pressure suit always |
| **Temperature** | -150°C to 100°C | Extreme swings |
| **Solar** | Available but variable | Long nights (no atmosphere warming) |
| **Ore Distribution** | Metal-rich, organic-poor | Excellent metals, scarce carbon |

### Mining Strategy

**Best Approach:**
- **Underground base** preferred (stable temperature)
- **Surface mining** for metals
- **Import organics** (carbon, biomass)

**Advantages:**
- Rich metallic deposits (iron, nickel, gold, silver)
- Clear vacuum (no dust storms)
- Good for solar (no clouds)

**Challenges:**
- Extreme cold (-150°C) requires massive heating
- Extreme heat (100°C in sunlight) requires cooling
- Vacuum hazards (suit breaches fatal)
- Long nights need huge battery banks
- Scarce organics (no carbon for steel)

### Power Considerations

**Solar Power:**
```
Day: Intense solar (no atmosphere)
Night: Very long (location dependent)

Batteries needed: 100+ for long nights
Solar panels: 30-50 for heating load
Heater power: 500-1000W continuous
```

**Generator Backup:**
- Almost essential for heating
- Fuel must be imported or produced

### Code Adaptations

**Lower Power Thresholds:**
```ic10
# Conservative thresholds for Moon
define POWER_HIGH 80  # More buffer for heating
define POWER_LOW 40   # Don't drain too deep

# Extra margin because heating is critical
```

**Temperature Interlock:**
```ic10
# Don't run drills if heater needs power
alias battery d0
alias heater d1
alias drill d2

l rCharge battery Charge
l rHeaterPower heater Power

# Prioritize heater over drill
blt rCharge 20 emergencyMode
sgt rTemp r0 293.15 enableDrill  # Only if warm enough
j disableDrill

emergencyMode:
# Critical power, heater only
s drill On 0
s heater On 1
j endTick

enableDrill:
# Normal operation with heater
bgt rCharge 80 runDrill
s drill On 0
j endTick

disableDrill:
s drill On 0
j endTick
```

### Base Design

**Recommended Layout:**
```
[Underground Habitat]
         │
    [Solar Surface]
    [Battery Bank]
    [Generator Backup]
         │
    [Elevator/Shaft]
         │
    [Mining Operations]
```

**Construction:**
- Underground for temperature stability
- Insulated walls (regolith)
- Airlock (vacuum seal)
- Massive heater capacity
- Import carbon for steel production

---

## Venus/Underground Mining

### Environment Characteristics

| Property | Value | Impact |
|----------|-------|--------|
| **Atmosphere** | High pressure (90+ atm), corrosive | Heavy suit needed, equipment damage |
| **Temperature** | 400°C+ (surface) | Extreme cooling required |
| **Solar** | Limited (clouds/haze) | Generators preferred |
| **Ore Distribution** | Similar to Mars | Standard variety |

### Mining Strategy

**Best Approach:**
- **Pressurized structures** only
- **Generator power** (limited solar)
- **Surface mining** (extreme heat)
- **Import advanced materials** (corrosion damage)

**Advantages:**
- Abundant lead and carbon
- Pressure can be used for atmosphere processing
- Similar ore distribution to Mars

**Challenges:**
- Extreme heat requires constant cooling
- Corrosive atmosphere damages equipment
- High pressure requires heavy construction
- Limited solar (clouds, haze)
- Equipment degrades quickly

### Power Considerations

**Generator Power:**
```
Solar: Limited availability
Generator: Primary power source
Cooling load: 500-1000W continuous

Fuel: Hydrocarbon or hydrogen from atmosphere
```

**Cooling Priority:**
- Cooling > Drills > Everything else
- Failure = rapid equipment damage/player death

### Code Adaptations

**Generator-Based Power:**
```ic10
# Monitor fuel and generator
alias generator d0
alias fuelTank d1
alias cooler d2
alias drill d3

l rFuel fuelTank Setting
blt rFuel 20 lowFuel

# Normal operation
bgt rFuel 50 enableDrills
s drill On 0  # Conserve fuel
j endTick

lowFuel:
# Critical fuel, cooler only
s drill On 0
s cooler On 1
j endTick

enableDrills:
# Normal operation
bgt rFuel 80 runDrills
j endTick
```

**Pressure Monitoring:**
```ic10
# Monitor structure pressure
alias structure d0
alias display d1

l rPressure structure Pressure
bgt rPressure 95 pressureWarning  # Approaching limit
j endTick

pressureWarning:
# Alert on display
s display Setting 999
j endTick
```

### Base Design

**Recommended Layout:**
```
[Pressure Vessel Habitat]
         │
    [Generator Room]
    [Cooling System]
         │
    [Surface Mining]
    (short trips only)
```

**Construction:**
- Pressure-resistant structures
- Active cooling throughout
- Corrosion-resistant materials
- Generator-based power
- Limited surface time

---

## Universal Principles

### Concepts That Apply Everywhere

**Ore Detection:**
- Hand scanner works the same
- Visual indicators similar
- Hash values consistent across environments

**Drill Operation:**
- Same mechanics everywhere
- Power draw varies by ore, not environment
- IC10 control logic identical

**Sorting and Processing:**
- Hash-based sorting works universally
- Furnace recipes same
- IC10 code environment-independent

**What Changes:**
- Power thresholds (adjust defines)
- Temperature management
- Life support requirements
- Equipment protection

### Environment-Independent Code

**Best Practice:** Write code with environment defines

```ic10
# Environment configuration
define ENV_MARS 0
define ENV_MOON 1
define ENV_VENUS 2

define CURRENT_ENV ENV_MARS

# Environment-specific thresholds
beq CURRENT_ENV ENV_MARS marsThresholds
beq CURRENT_ENV ENV_MOON moonThresholds
beq CURRENT_ENV ENV_VENUS venusThresholds

marsThresholds:
move rPowerHigh 70
move rPowerLow 30
j applyThresholds

moonThresholds:
move rPowerHigh 80
move rPowerLow 40
j applyThresholds

venusThresholds:
move rPowerHigh 60
move rPowerLow 20
j applyThresholds

applyThresholds:
# Use rPowerHigh and rPowerLow in logic
```

---

## Code Adaptation Examples

### Power Management by Environment

**Mars (Baseline):**
```ic10
define POWER_HIGH 70
define POWER_LOW 30
```

**Moon (Conservative):**
```ic10
# Higher buffer for heating
define POWER_HIGH 80
define POWER_LOW 40
```

**Venus (Generator):**
```ic10
# Fuel conservation
define FUEL_HIGH 70
define FUEL_LOW 20
```

### Temperature Control

**Mars (Heating at night):**
```ic10
l rTemp sensor Temperature
blt rTemp 293.15 enableHeater  # Below 20°C
s heater On 0
j endTick

enableHeater:
s heater On 1
j endTick
```

**Moon (Always heating):**
```ic10
# Heating critical, always monitor
l rTemp habitat Temperature
blt rTemp 293.15 heaterOn
bgt rTemp 298.15 heaterOff  # Above 25°C
j endTick

heaterOn:
s heater On 1
j endTick

heaterOff:
s heater On 0
j endTick
```

**Venus (Always cooling):**
```ic10
# Cooling critical
l rTemp habitat Temperature
bgt rTemp 303.15 coolerOn  # Above 30°C
s cooler On 0
j endTick

coolerOn:
s cooler On 1
j endTick
```

### Universal Drill Control Template

```ic10
# Environment-aware drill control
# Modify defines for your environment

# === ENVIRONMENT CONFIGURATION ===
# Mars: 70/30, Moon: 80/40, Venus: 60/20
define POWER_HIGH 70
#define POWER_LOW 30

# === DEVICES ===
alias drill d0
alias battery d1

# === MAIN LOOP ===
main:
l rCharge battery Charge

# Environment-adjusted thresholds
bgt rCharge POWER_HIGH turnOn
blt rCharge POWER_LOW turnOff
j endTick

turnOn:
s drill On 1
j endTick

turnOff:
s drill On 0
j endTick

endTick:
yield
j main
```

---

## Resources

### Related Guides
- [Base Design Guide](mining-base-design.md) - Environment-specific layouts
- [Manual Mining Techniques](mining-manual-techniques.md) - Environment considerations
- [Equipment Reference](../knowledge/mining/equipment.md) - Device specifications

### Knowledge Base
- [Ore Deposits](../knowledge/mining/ore-deposits.md) - Environment-specific ore locations

### Examples
- [single-drill-controller.ic10](../examples/mining/single-drill-controller.ic10) - Adapt thresholds for environment
- [multi-drill-coordinator.ic10](../examples/mining/multi-drill-coordinator.ic10) - Power-aware coordination

---

## Summary

Each environment presents unique challenges for mining operations. Adapt your strategies, power systems, and code accordingly. Universal principles apply everywhere—only the thresholds change.

**Key Takeaways:**
1. **Mars:** Balanced environment, solar viable
2. **Moon:** Extreme cold, massive heating needed, import organics
3. **Venus:** Extreme heat, generator power, corrosion issues
4. **Universal:** Ore detection, drilling, sorting work the same
5. **Adapt:** Adjust power thresholds and temperature control

**Next Steps:**
- Choose your environment
- Adapt code thresholds
- Design for environmental challenges
- Test and refine

Happy mining, wherever you are!

# Readable Logic Types

Properties that can be read from devices using `l` or `lb` instructions.

## Universal (Most Devices)

| Logic Type | Description | Unit | Notes |
|------------|-------------|------|-------|
| On | Power state | Boolean | 1 = on, 0 = off |
| Error | Error state | Boolean | Device malfunction |
| PrefabHash | Device type ID | Hash | For batch identification |
| ReferenceId | Unique device ID | Integer | Unique per save |
| NameHash | Label hash | Hash | From labeler tool |

## Power

| Logic Type | Description | Unit | Devices |
|------------|-------------|------|---------|
| Power | Current power | W | Most powered devices |
| PowerActual | Actual power flow | W | Batteries, transformers |
| PowerPotential | Available power | W | Batteries, generators |
| PowerRequired | Power needed | W | Most powered devices |
| Charge | Stored energy | J | Batteries, APCs |
| Maximum | Max capacity | J | Batteries |
| Ratio | Charge / Maximum | 0-1 | Batteries |

## Atmospheric

| Logic Type | Description | Unit | Devices |
|------------|-------------|------|---------|
| Pressure | Gas pressure | kPa | Sensors, tanks, pipes |
| Temperature | Temperature | K | Sensors, furnaces |
| Volume | Container volume | L | Tanks, pipes |
| TotalMoles | Total gas moles | mol | Sensors, tanks |

## Gas Ratios

| Logic Type | Description | Range |
|------------|-------------|-------|
| RatioOxygen | O2 concentration | 0-1 |
| RatioNitrogen | N2 concentration | 0-1 |
| RatioCarbonDioxide | CO2 concentration | 0-1 |
| RatioVolatiles | H2 (fuel) concentration | 0-1 |
| RatioPollutant | X (toxic) concentration | 0-1 |
| RatioWater | H2O vapor concentration | 0-1 |
| RatioNitrousOxide | N2O concentration | 0-1 |

## Liquid Ratios

| Logic Type | Description | Range |
|------------|-------------|-------|
| RatioLiquidOxygen | Liquid O2 | 0-1 |
| RatioLiquidNitrogen | Liquid N2 | 0-1 |
| RatioLiquidCarbonDioxide | Liquid CO2 | 0-1 |
| RatioLiquidVolatiles | Liquid H2 | 0-1 |
| RatioLiquidPollutant | Liquid X | 0-1 |
| RatioLiquidNitrousOxide | Liquid N2O | 0-1 |
| RatioPollutedWater | Contaminated water | 0-1 |

## Device State

| Logic Type | Description | Unit | Devices |
|------------|-------------|------|---------|
| Open | Open state | Boolean | Doors, vents |
| Lock | Lock state | Boolean | Doors, access points |
| Activate | Activation state | Boolean | Buttons, triggers |
| Mode | Operating mode | Integer | Vents, sorters |
| Setting | User dial value | Float | Most devices |
| Combustion | Fire detected | Boolean | Sensors |
| Horizontal | Horizontal angle | Degrees | Solar panels |
| Vertical | Vertical angle | Degrees | Solar panels |
| SolarAngle | Sun angle | Degrees | Solar sensors |
| SolarIrradiance | Sun intensity | W/m² | Solar sensors |

## Recipes/Manufacturing

| Logic Type | Description | Unit | Devices |
|------------|-------------|------|---------|
| RecipeHash | Current recipe | Hash | Fabricators |
| ImportCount | Items to import | Integer | Sorters |
| ExportCount | Items exported | Integer | Sorters |
| Quantity | Item count | Integer | Stackers, vending |
| ClearMemory | Memory cleared | Boolean | Memory devices |

## Examples

### Read Sensor Data
```ic10
alias sensor d0
l r0 sensor Pressure        # Current pressure
l r1 sensor Temperature     # Current temp
l r2 sensor RatioOxygen     # O2 level (0-1)
```

### Read Battery Status
```ic10
alias battery d0
l r0 battery Charge         # Current charge in Joules
l r1 battery Maximum        # Max capacity
l r2 battery Ratio          # Percentage (0-1)
```

### Batch Read (All Batteries)
```ic10
define BATTERY_HASH 683671518
lb r0 BATTERY_HASH Ratio 0   # Average ratio of all batteries
lb r1 BATTERY_HASH Charge 1  # Sum of all battery charges
```

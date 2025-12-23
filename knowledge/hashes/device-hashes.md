# Device Prefab Hashes

Prefab hashes for use with batch operations (`lb`, `sb`, `lbn`, `sbn`).

## Usage

```ic10
# Read from all devices of a type on the network
lb r0 HASH LogicType Mode    # Mode: 0=avg, 1=sum, 2=min, 3=max

# Write to all devices of a type on the network
sb HASH LogicType value
```

## Atmospheric Devices

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Active Vent | -842048328 | Bidirectional pressure control |
| Passive Vent | 238631271 | One-way flow |
| Volume Pump | -321403609 | Standard pump |
| Turbo Volume Pump | 561323117 | High-flow pump |
| Gas Sensor | 546126601 | Reads pressure, temp, gases |
| Pipe Analyzer | 435685051 | Detailed gas analysis |
| Air Conditioner | -2087593337 | Temperature control |
| Filtration | -348054045 | Gas separation |
| Wall Cooler | 1469396920 | Room cooling |
| Wall Heater | 1389046652 | Room heating |

## Power Devices

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Solar Panel | 844961456 | Fixed panel |
| Solar Panel (Heavy) | -1545574413 | Heavy duty fixed |
| Solar Panel (Tracking) | -539224550 | Dual-axis tracking |
| Battery (Small) | -1900335881 | 3000 kJ capacity |
| Battery (Large) | 683671518 | 36000 kJ capacity |
| APC | -1093957350 | Area Power Controller |
| Solid Fuel Generator | -2016970735 | Burns solid fuels |
| Gas Fuel Generator | 1165997963 | Burns H2/Volatiles |
| Stirling Engine | 780058700 | Heat differential |
| Turbine Generator | 1981524447 | Pressure differential |

## Logic Devices

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| IC Housing | 1512322581 | 2-slot IC holder |
| IC Housing (10) | -128473777 | 10-slot IC holder |
| Logic I/O | -345383640 | Network interface |
| Logic Memory | -130638386 | Data storage |
| Logic Switch | 124499454 | Manual toggle |
| Logic Reader | -1010279526 | Reads from network |
| Logic Writer | -1065664980 | Writes to network |
| Dial | 1916992775 | Analog input |
| Lever | -1522907883 | Binary input |
| Button | -1404826541 | Momentary input |

## Fabrication Devices

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Furnace | 545937711 | Basic smelting |
| Arc Furnace | -721824809 | Advanced smelting |
| Autolathe | -1753893214 | Manufacturing |
| Electronics Printer | 683793029 | Circuit fabrication |
| Hydraulic Pipe Bender | -1680875865 | Pipe manufacturing |
| Centrifuge | 1915566057 | Ore processing |
| Recycler | 1729066711 | Item recycling |

## Doors & Airlocks

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Door | 168615924 | Standard door |
| Airlock | -821339274 | Airtight door |
| Airlock Gate | -2127903276 | Large airlock |
| Blast Door | -1693175851 | Heavy door |

## Sensors

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Daylight Sensor | -326478931 | Solar angle |
| Motion Sensor | -1677616158 | Movement detection |
| Occupancy Sensor | 1363084076 | Presence detection |

## Storage

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Locker | 1886693770 | Item storage |
| Crate | 1812015081 | Stackable storage |
| Tank (Small) | -483278802 | 1000L gas storage |
| Tank (Medium) | -1334068458 | 16000L gas storage |
| Tank (Large) | 1520698177 | 64000L gas storage |

## Displays

| Device | Prefab Hash | Notes |
|--------|-------------|-------|
| Console | -413111258 | Computer interface |
| LED Display (Small) | -815193061 | Numeric display |
| LED Display (Medium) | -289015349 | Larger display |

---

## Example: Solar Panel Array Control

```ic10
# Read average solar ratio from all tracking panels
define SOLAR_PANEL -539224550
lb r0 SOLAR_PANEL Ratio 0     # 0 = Average

# Set all panels to specific angle
sb SOLAR_PANEL Vertical 45
sb SOLAR_PANEL Horizontal 90
```

## Example: Battery Bank Monitoring

```ic10
# Sum total charge across all batteries
define BATTERY_LARGE 683671518
lb r0 BATTERY_LARGE Charge 1   # 1 = Sum
lb r1 BATTERY_LARGE Maximum 1  # Total capacity

# Calculate percentage
div r2 r0 r1
mul r2 r2 100
```

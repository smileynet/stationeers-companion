# Game Knowledge Base

Reference data for Stationeers IC10 programming.

## Categories

### [Gases](gases/)

Atmospheric properties and constants for environment control:
- Gas types and logic values
- Pressure and temperature constants
- Breathable atmosphere parameters
- Temperature conversion formulas

### [Hashes](hashes/)

Prefab and item hashes for batch/slot operations:
- Device prefab hashes for `lb`/`sb` batch operations
- Item/reagent hashes for slot operations
- Common device categories (atmospheric, power, logic, etc.)

### [Farming](farming/)

Plant growing reference and compatibility guide:
- Complete plant table with requirements (18 plants)
- Compatibility groups (which plants can share environments)
- Special areas (mushroom room, alien chamber, thermogenic)
- Symbiotic setups and atmosphere targets

## Usage with IC10

This knowledge base supports IC10 programming by providing:

1. **Device hashes** - Required for batch operations to control multiple devices
2. **Gas properties** - Constants for atmosphere monitoring and control
3. **Item hashes** - For sorting and inventory management automation

## Quick Lookup

### Most Common Device Hashes

| Device | Hash | Use Case |
|--------|------|----------|
| Active Vent | -842048328 | Pressure control |
| Gas Sensor | 546126601 | Atmosphere monitoring |
| Solar Panel (Tracking) | -539224550 | Power generation |
| Battery (Large) | 683671518 | Power storage |

### Atmosphere Targets

| Parameter | Target | Range |
|-----------|--------|-------|
| Pressure | 101.325 kPa | 20-202 kPa |
| Temperature | 293.15 K | 283-303 K |
| O2 Ratio | 0.21 | 0.16-0.30 |
| CO2 Ratio | 0 | 0-0.01 |

## Related

- [IC10 Reference](../docs/reference/) - Instruction syntax
- [Device Docs](../docs/devices/) - Device properties
- [Examples](../examples/) - Working code

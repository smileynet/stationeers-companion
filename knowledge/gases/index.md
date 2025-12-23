# Gas Reference

Atmospheric and gas properties for Stationeers IC10 programming.

## Reference Files

### [Properties](properties.md)

Complete gas reference including:
- Gas types and logic values (RatioOxygen, RatioNitrogen, etc.)
- Atmospheric constants (pressure, temperature)
- Breathable atmosphere parameters
- Gas-specific behavior and properties
- IC10 code examples for atmosphere monitoring

## Quick Reference

### Gas Logic Types

| Gas | Logic Type |
|-----|------------|
| Oxygen (O2) | RatioOxygen |
| Nitrogen (N2) | RatioNitrogen |
| Carbon Dioxide (CO2) | RatioCarbonDioxide |
| Volatiles (H2) | RatioVolatiles |
| Pollutant (X) | RatioPollutant |
| Water (H2O) | RatioWater |
| Nitrous Oxide (N2O) | RatioNitrousOxide |

### Key Constants

| Parameter | Value | Notes |
|-----------|-------|-------|
| Ideal pressure | 101.325 kPa | Earth standard |
| Ideal temperature | 293.15 K | 20°C |
| O2 ratio | 0.21 | 21% oxygen |
| Max CO2 | 0.01 | 1% before toxic |

### IC10 Quick Example

```ic10
alias sensor d0
l r0 sensor RatioOxygen
l r1 sensor RatioCarbonDioxide
l r2 sensor Pressure
l r3 sensor Temperature
```

## Related

- [Device Hashes](../hashes/device-hashes.md) - Gas Sensor, Pipe Analyzer hashes
- [Atmosphere Examples](../../examples/atmosphere/) - Working atmosphere control code

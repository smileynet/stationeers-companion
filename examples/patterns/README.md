# Patterns Examples

IC10 code examples for patterns automation in Stationeers.

## Scripts

| Script | Description | Devices |
|--------|-------------|---------|
| [centrifuge-set-controller](centrifuge-set-controller.ic10) | this script manages a centrifuge array pull the lever to sig... | d0 = Lever |
| [larre-farming-controller](larre-farming-controller.ic10) | - | d0 = Arm, d1 = HydroponicDevice, d2 = Bin1 |
| [lights-outdoor-controller](lights-outdoor-controller.ic10) | - | d0 = IsDay, d1 = IsStorm |
| [printer-logistics](printer-logistics.ic10) | Based on Printer Logistics V4 by CowsAreEvil | d0 = printer, d1 = stacker, d2 = sorter |
| [compostercontroller](compostercontroller.ic10) | - | d0 = composter, d1 = vent, d2 = door |
| [cooler](cooler.ic10) | - | d0 = PumpIn, d1 = PumpOut, d2 = Analyzer |
| [plantcontroller](plantcontroller.ic10) | Controller for a set of three hydroponics and harvies. Make ... | d0 = hydro1, d1 = hydro2, d2 = hydro3 |
| [flightcontroller](flightcontroller.ic10) | - | d0 = Automation, d1 = DisplayCountdown, d2 = FuelController |
| [fuelcontroller](fuelcontroller.ic10) | - | d0 = Automation, d1 = Pump, d2 = Display |
| [silodispenser](silodispenser.ic10) | Controller for a single silo, used for dispensing a definabl... | d0 = silo, d1 = displayTotal, d2 = dialAmount |
| [water-filler-pid-controller](water-filler-pid-controller.ic10) | - | d0 = WaterSensor, d1 = Actuator, d2 = WarmWaterTank |
| [diy-condensor-pid-controller](diy-condensor-pid-controller.ic10) | - | d0 = CompressSensor, d1 = Actuator, d2 = SrcSensor |
| [topup-pid-controller](topup-pid-controller.ic10) | - | d0 = FluidSensor, d1 = Actuator |
| [pid-controller](pid-controller.ic10) | - | d0 = Sensor, d1 = Actuator, d2 = SleepToggle |
| [sorter](sorter.ic10) | - | - |
| [manual-sat](manual-sat.ic10) | - | d0 = dSatellite, d1 = dSignalStrength, d3 = dHorizontal |
| [Vending_Machine_Controller](vending_machine_controller.ic10) | This script displays how much of a thing is inside a vending... | d0 = VendingMachine, d1 = QuantityDisplay, d2 = UsedSlotsDisplay |
| [Vending_Counter](vending_counter.ic10) | - | d0 = VendingMachine, d1 = UsedSlotsDisplay, d2 = QueryMemory1 |
| [GameDisplay](gamedisplay.ic10) | - | - |
| [GameDisplay789](gamedisplay789.ic10) | - | - |
| [GameMain](gamemain.ic10) | - | d0 = GoButton, d1 = DisplayChip1, d2 = DisplayChip2 |
| [Chute_Sorter](chute_sorter.ic10) | - | d0 = Chute |
| [Harvie_Automator](harvie_automator.ic10) | Harvie controller  Cows Are Evil Do you want Harvie to harve... | d0 = hydroponics, d3 = harvie, d1 = hydroponics |
| [HydroponicsLight_Multi](hydroponicslight_multi.ic10) | Register Usage: r0 - r2 : Misc r3 : Current average for curr... | - |
| [HydroponicsLight_v2](hydroponicslight_v2.ic10) | - | d0 = Hydroponics |
| [ore_sorter](ore_sorter.ic10) | - | - |
| [SorterControll_DigitalCute](sortercontroll_digitalcute.ic10) | - | d0 = AutolatheSorter, d1 = PipeBenderSorter, d2 = ElectronicsSorter |
| [SoterControll](sotercontroll.ic10) | - | d0 = AutolatheSorter, d1 = PipeBenderSorter, d2 = ElectronicsSorter |
| [auto_item_sorter](auto_item_sorter.ic10) | Controls Sorters to sort items based on hash. Reads item-has... | - |
| [deep_miner](deep_miner.ic10) | - | d0 = MineOn, d1 = CentriOne, d2 = CentriTwo |
| [electric_centrifuge_auto_empty](electric_centrifuge_auto_empty.ic10) | This script loops through up to six centrifuges per chip, ch... | - |

## Sources

- [github.com/Zappes/Stationeers](https://github.com/Zappes/Stationeers)
- [github.com/SnorreSelmer/stationeers_ic10](https://github.com/SnorreSelmer/stationeers_ic10)
- [github.com/Xon/stationeers-ic-scripts](https://github.com/Xon/stationeers-ic-scripts)
- [github.com/drclaw1188/stationeers_ic10](https://github.com/drclaw1188/stationeers_ic10)
- [github.com/jhillacre/stationeers-scripts](https://github.com/jhillacre/stationeers-scripts)

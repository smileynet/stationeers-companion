# Atmosphere Examples

IC10 code examples for atmosphere automation in Stationeers.

## Scripts

| Script | Description | Devices |
|--------|-------------|---------|
| [active-vent-set-controller](active-vent-set-controller.ic10) | drives a bank of active vents from one command set RESPINT w... | d0 = ventCmd, d1 = extSensor |
| [air-conditioner-controller](air-conditioner-controller.ic10) | The AC Setting doesn't match face value. Manage the setting ... | db = Self |
| [air-ratio-control](air-ratio-control.ic10) | Manage Room Gas Ratio via Pumps | d0 = CO2Pump, d1 = NPump, d2 = O2Pump |
| [air-ratio-regulator](air-ratio-regulator.ic10) | Manage Atmospheric Filter (from IC Housing) | d0 = filter, d1 = inputsensor, d2 = outputsensor |
| [airgate-airlock](airgate-airlock.ic10) | use airgate-set-controller with active-vent sets runs a mult... | d0 = doorCommandMemory, d1 = ventCommandMemory, d2 = internalSensorMirror |
| [airgate-set-controller](airgate-set-controller.ic10) | drives a bank of airgates from a shared command set RESPINT ... | d0 = doorCommand |
| [arc-furnace-array](arc-furnace-array.ic10) | turn on and activate arc furnaces that have work. | d0 = ArcFurnace1, d1 = ArcFurnace2, d2 = ArcFurnace3 |
| [automated-filter](automated-filter.ic10) | - | d0 = filtration, d1 = wastesensor, d2 = storagesensor |
| [day-weather-state-mirror](day-weather-state-mirror.ic10) | - | d0 = WeatherStation, d1 = DaylightSensor, d2 = IsDay |
| [gas-burner](gas-burner.ic10) | - | d0 = furnace, d1 = fuelpump, d2 = exhaustpump |
| [gas-fuel-generator-controller](gas-fuel-generator-controller.ic10) | manage a gas fuel generator as backup power | d0 = gfg, d1 = gs, d2 = pr_fuel |
| [gas-mixer-air-regulator](gas-mixer-air-regulator.ic10) | based on CowsAreEvil code from https://youtu.be/O0VLyV2PX9A?... | d0 = airsensor, d1 = nsensor, d2 = o2sensor |
| [gas-mixer-fuel-regulator](gas-mixer-fuel-regulator.ic10) | based on CowsAreEvil code from https://youtu.be/O0VLyV2PX9A?... | d0 = fuelsensor, d1 = h2sensor, d2 = o2sensor |
| [hot-cold-valve](hot-cold-valve.ic10) | - | d0 = HotValve, d1 = ColdValve |
| [nitrogen-condensation-regulator](nitrogen-condensation-regulator.ic10) | fills from a reserve N network to a cooling loop network for... | d0 = CoolingPA, d1 = ReservePA, d2 = TVP |
| [onboard-filtration](onboard-filtration.ic10) | manage a filtration unit via onboard chip slot stop filterin... | db = Self, d0 = Light, d1 = Alarm |
| [ore-stacker](ore-stacker.ic10) | Manages an array of digital flip flop splitters as sorters f... | d0 = Lever, d1 = ThrottleStacker |
| [room-cooler-via-exchange](room-cooler-via-exchange.ic10) | ### Cooler-only PID with safety box ### | d0 = pumpIn, d1 = pumpOut, d2 = loopA |
| [room-heater-via-exchange](room-heater-via-exchange.ic10) | - | d0 = coolsensor, d1 = warmpumpin, d2 = warmpumpout |
| [tank-filler-personal-controller](tank-filler-personal-controller.ic10) | - | d0 = pump, d1 = storage |
| [temp-gated-pressure-regulator](temp-gated-pressure-regulator.ic10) | - | d0 = VP, d1 = TPA, d2 = SPA |
| [vacuum-pipe-evaporator](vacuum-pipe-evaporator.ic10) | D0: Analyzer (target pipe) D1: Liquid Regulator (Setting=L) ... | d0 = A, d1 = R, d2 = P |
| [waste-storage-controller](waste-storage-controller.ic10) | waste recirculation controller for filters | d0 = Waste, d1 = PumpIn, d2 = InPA |
| [water-temp-control](water-temp-control.ic10) | turns on heaters on the network or opens digital values on t... | - |
| [filtercontroller](filtercontroller.ic10) | A controller for a filtration device. Written by Zappes CC B... | d0 = filter, d1 = analyzer, d2 = led |
| [mastercontrol](mastercontrol.ic10) | Sets up 6 filter controllers so they know what to actually f... | d0 = Oxygen, d1 = Nitrogen, d2 = Carbon |
| [furnace](furnace.ic10) | - | d0 = Furnace, d1 = ValveCold, d2 = ValveHot |
| [work](work.ic10) | - | d0 = PumpIn, d1 = PumpOut, d2 = Analyzer |
| [filterpumps](filterpumps.ic10) | - | d0 = pump1, d1 = pump2, d2 = pump3 |
| [airmixer](airmixer.ic10) | - | d0 = mixer1, d3 = analyzer1, d1 = mixer2 |
| [fuelmixer](fuelmixer.ic10) | - | d0 = Mixer, d1 = Analyzer |
| [temperaturecontroller](temperaturecontroller.ic10) | Controller for a number of heaters and coolers Written by Za... | d0 = Sensor, d1 = Display, d2 = dialTarget |
| [condensators](condensators.ic10) | - | d0 = switch, d1 = inputSensor, d2 = outputSensor |
| [evaporators](evaporators.ic10) | - | d0 = switch, d1 = inputSensor, d2 = outputSensor |
| [external-cooler](external-cooler.ic10) | - | d0 = externalSensor, d1 = hotSideSensor, d2 = poweredVent |
| [filterless-air-harvesting-passive](filterless-air-harvesting-passive.ic10) | - | d0 = xFilter, d1 = co2Filter, d4 = extSensor |
| [filterless-air-harvesting](filterless-air-harvesting.ic10) | - | - |
| [paired-ac-units](paired-ac-units.ic10) | - | d1 = debugOuput |
| [staged-water-cooling](staged-water-cooling.ic10) | - | d0 = externalSensor |
| [water-cooler-cooler](water-cooler-cooler.ic10) | - | d0 = externalSensor, d1 = hotWaterSensor, d2 = condensorSensor |
| [water-cooler](water-cooler.ic10) | - | d0 = coldSideSensor, d1 = hotWaterPump, d2 = waterSensor |
| [ac-pressure-controlled](ac-pressure-controlled.ic10) | - | db = ac |
| [air-pump](air-pump.ic10) | - | d0 = theSwitch, d1 = sensor, d2 = tank |
| [air-ratio-pumps](air-ratio-pumps.ic10) | - | d0 = Sensor, d1 = O2_Pump, d2 = CO2_Pump |
| [auto-vent-cooling-tank](auto-vent-cooling-tank.ic10) | - | d0 = Tank, d1 = ActiveVent, d2 = heatPump |
| [bulk_external_air_extraction](bulk_external_air_extraction.ic10) | - | d0 = hotTank, d1 = externalTempSensor |
| [cooling-radiator-valve](cooling-radiator-valve.ic10) | - | d0 = gas, d1 = refrigerant, d2 = valve |
| [external_air_extraction](external_air_extraction.ic10) | - | d0 = tank, d1 = theMachine, d2 = externalVent |
| [external_air_extraction2](external_air_extraction2.ic10) | - | d1 = hotTank, d2 = coldTank, d3 = greenhouseSensor |
| [filteration-till-target-v2](filteration-till-target-v2.ic10) | - | db = filtration |
| [filteration-till-target](filteration-till-target.ic10) | IC10-slot parallel Filtration Control | db = filtration |
| [greenhouse_air_quality](greenhouse_air_quality.ic10) | - | d0 = sensor, d1 = o2_filter, d2 = co2_vent |
| [greenhouse_fill](greenhouse_fill.ic10) | - | d0 = tank, d1 = roomSensor, d2 = vent |
| [ic10-slot-fill-output](ic10-slot-fill-output.ic10) | - | db = filtration, d0 = pump |
| [mirror-vent](mirror-vent.ic10) | - | d0 = vent |
| [parallel-filteration](parallel-filteration.ic10) | - | db = filtration |
| [pressure-pump-for-filtration](pressure-pump-for-filtration.ic10) | - | d0 = harvesterSensor, d1 = harvesterPump, d2 = tank |
| [pressure-pump](pressure-pump.ic10) | - | d0 = SensorSrc, d1 = Pump |
| [ratio-filtration](ratio-filtration.ic10) | activates filtration based on ratios not being desirable | d0 = Sensor, d1 = O2_Filter, d1 = N20_Filter |
| [room-filteration](room-filteration.ic10) | - | db = filtration |
| [staged-temperature-conditioning](staged-temperature-conditioning.ic10) | - | d0 = air_sensor, d1 = pump, d2 = valve |
| [tank-emptier](tank-emptier.ic10) | - | d0 = pump |
| [temperature-conditioning](temperature-conditioning.ic10) | - | d0 = Tank, d1 = TankCooling, d2 = OutputValve |
| [temperature-controlled-room](temperature-controlled-room.ic10) | - | d0 = powerOffDevice, d1 = roomSensor, d2 = door |
| [temperature-independent-fuel-mixer](temperature-independent-fuel-mixer.ic10) | Temperature independent fuel mixing. With output an pressure... | d0 = mixer, d1 = O2_Sensor, d2 = H2_Sensor |
| [toggle-machine-on-output-pressure](toggle-machine-on-output-pressure.ic10) | - | d0 = Sensor1, d1 = theMachine, d2 = Sensor2 |
| [vulcan_ac](vulcan_ac.ic10) | - | d0 = acTank, d1 = externalTempSensor, d2 = ventPump |
| [vulcan_heatexchanger_at_night(powered vent)](vulcan_heatexchanger_at_night-powered-vent.ic10) | - | d0 = externalSensor, d1 = internalSensor |
| [vulcan_heatexchanger_at_night](vulcan_heatexchanger_at_night.ic10) | - | d0 = tank, d1 = tempSensor, d2 = pump |
| [harvie](harvie.ic10) | - | - |
| [night-day-fill-vulcan](night-day-fill-vulcan.ic10) | - | d0 = externalSensor, d1 = dayAirValve, d2 = dayAirSensor |
| [stirling-engine-vulcan](stirling-engine-vulcan.ic10) | - | d0 = tempSensor |
| [room-automation](room-automation.ic10) | - | - |
| [hanger-ac](hanger-ac.ic10) | - | d0 = hangerStateSwitch |
| [sky-scan](sky-scan.ic10) | - | d0 = dSatellite, d1 = dLight |
| [stat-tracking](stat-tracking.ic10) | - | d0 = dRadar, d1 = dLight |
| [Canned_Food_Stack_Writer](canned_food_stack_writer.ic10) | - | - |
| [Ingot_Storage_Stack_Writer](ingot_storage_stack_writer.ic10) | See https://github.com/drclaw1188/stationeers_ic10/tree/main... | - |
| [Ore_Storage_Stack_Writer](ore_storage_stack_writer.ic10) | See https://github.com/drclaw1188/stationeers_ic10/tree/main... | - |
| [Three_Machine_Display](three_machine_display.ic10) | This script displays how much of each thing listed is inside... | d0 = VendingMachine1, d1 = VendingMachine2, d2 = VendingMachine3 |
| [Vending_Manager](vending_manager.ic10) | This script displays how much of each thing listed is inside... | d0 = QueryMemory, d1 = ResponseMemory, d2 = QuantityDisplay |
| [Furnace_Control_Simple_v2](furnace_control_simple_v2.ic10) | SemiPrimes's advanced furnace control (simple version). Requ... | d0 = HotPump, d1 = ColdPump, d2 = ExhaustPump |
| [Furnace_Control_Slave_v2](furnace_control_slave_v2.ic10) | SemiPrimes's advanced furnace control (simple version) See h... | d0 = HotPump, d1 = ColdPump, d2 = ExhaustPump |
| [Furnace_Controller_Stack_Writer](furnace_controller_stack_writer.ic10) | Thanks to CowsAreEvil for the data here Stack programmer for... | - |
| [Furnace_Master_Stack_Writer](furnace_master_stack_writer.ic10) | Stack programmer for furnace vending control 1 - Alloy Hash ... | - |
| [Furnace_Master_v2](furnace_master_v2.ic10) | - | d0 = VendingMachine, d1 = FurnaceIC, d2 = ControlChute |
| [Furnace_Control_Simple](furnace_control_simple.ic10) | Madcat's advanced furnace control (simple version) | d0 = HotPump, d1 = ColdPump, d2 = ExhaustPump |
| [Furnace_Controller](furnace_controller.ic10) | Madcat's advanced furnace control (simple version) | d0 = HotPump, d1 = ColdPump, d2 = OverrideSwitch |
| [Furnace_Master](furnace_master.ic10) | - | d0 = VendingMachine, d1 = FurnaceIC, d2 = Dial |
| [Furnace_Master_Duke](furnace_master_duke.ic10) | - | d0 = RequestMem, d1 = DispenserMem, d2 = FurnaceIC |
| [Furnace_Master_New](furnace_master_new.ic10) | - | d0 = VendingMachine, d1 = FurnaceIC, d2 = Dial |
| [Hot_Tank_System](hot_tank_system.ic10) | - | d0 = Furnace, d1 = HotTank, d2 = HotPump |
| [MoonFurnaceMaster](moonfurnacemaster.ic10) | - | d0 = RequestMem, d1 = DispenserMem, d2 = FurnaceIC |
| [GameStackWriter](gamestackwriter.ic10) | - | - |
| [GameStackWriter2](gamestackwriter2.ic10) | - | - |
| [Automatic_Food_Canning](automatic_food_canning.ic10) | This script automates an Automated Oven and Advanced Packagi... | d0 = Oven, d1 = Packager, d2 = Sorter |
| [Automatic_Food_Canning_v5](automatic_food_canning_v5.ic10) | This script automates an Automated Oven and Advanced Packagi... | d0 = Oven, d1 = Packager, d2 = Sorter |
| [CO2Refill](co2refill.ic10) | - | d0 = PipeSensor, d1 = Pump, db = Filter |
| [GreenhouseMaster_v2](greenhousemaster_v2.ic10) | - | d0 = InsideSensor, d1 = OxygenPump, d2 = NitrogenPump |
| [Greenhouse_Master](greenhouse_master.ic10) | - | d0 = InsideSensor, d1 = OxygenPump, d2 = NitrogenPump |
| [Harvie_Automator_2](harvie_automator_2.ic10) | - | - |
| [Harvie_Automator_3](harvie_automator_3.ic10) | - | d2 = Chute |
| [HydroponicsLight](hydroponicslight.ic10) | - | d0 = Hydroponics, d1 = DaylightSensor |
| [PrinterAutoStop](printerautostop.ic10) | Semiprime's Printer Autostop See https://github.com/drclaw11... | d0 = AutoLathe, d1 = AutoLatheStacker, d2 = ElectronicsPrinter |
| [PrinterMaster](printermaster.ic10) | - | d0 = RequestMem, d1 = Autolathe, d2 = PipeBender |
| [PrinterMaster_v2](printermaster_v2.ic10) | - | d0 = VendingMachine, d1 = Autolathe, d2 = PipeBender |
| [PrinterMaster_v3](printermaster_v3.ic10) | Semiprime's Printer Master See https://github.com/drclaw1188... | d0 = VendingMachine, d1 = Autolathe, d2 = PipeBender |
| [RocketController](rocketcontroller.ic10) | - | d0 = FuelPump, d1 = ModeDisplay, d2 = FuelDisplay |
| [Beacon_And_Lights](beacon_and_lights.ic10) | - | d0 = ProximitySensor, d1 = WeatherStation, d2 = WeatherTimeLED |
| [Health_And_Safety](health_and_safety.ic10) | Hardsuit safety system.  Based on CowsAreEvil version | db = Suit, d0 = Helmet, d1 = Backpack |
| [auto_adv_furnace_library](auto_adv_furnace_library.ic10) | Based on Elmotrix' FurnaceLibraryV4 Removed Prev/Next button... | d0 = Furnace, d1 = FurnaceOn, d2 = LBDial |
| [auto_arc_furnace](auto_arc_furnace.ic10) | Connect Arc Furnaces to the screws, that's all! | - |
| [auto_class_sorter](auto_class_sorter.ic10) | Runs up to six sorters that filter throughput by ItemClass. ... | - |
| [auto_lights](auto_lights.ic10) | Uses Occupancy Sensor and (optional) Daylight Sensor to cont... | d0 = Detector, d1 = DaySens, d2 = Lights |
| [automated_canister_filling](automated_canister_filling.ic10) | Automatic gas-canister filler. !!! Remember to set volume pu... | d0 = CanisterStorage, d1 = FillPump, d2 = EvacPump |
| [cooling_tower_drain](cooling_tower_drain.ic10) | Automatically evacuates cooling-tower when temp is below 40C... | d0 = Sensor, d1 = Pump |
| [filtration](filtration.ic10) | Automated Filtration Control Based on code by CowsAreEvil De... | db = filtration, d0 = diode |
| [gas_mixer](gas_mixer.ic10) | Gas-mixing script. Needs two source-tanks and an output tank... | d0 = TankA, d1 = TankB, d2 = TankOut |
| [heating_cooling](heating_cooling.ic10) | - | d0 = GasSensor, d1 = Thermostat, d2 = TempDisplay |
| [mush_cooler](mush_cooler.ic10) | Connect mush-pipe to Heat Exchanger, use Digital Valve to ex... | d0 = PipeAnalyzer, d1 = DigitalValve |
| [printer_countdown](printer_countdown.ic10) | - | d0 = Dial, d1 = DisplayOrder, d2 = DisplayExport |
| [storm_warning](storm_warning.ic10) | - | d0 = Weather, d1 = Readout, d2 = Announcer |
| [phase-change-heat-dump](phase-change-heat-dump.ic10) | This script is used to open and close a Digital Valve to dum... | d0 = condenser, d1 = valve |

## Sources

- [github.com/Zappes/Stationeers](https://github.com/Zappes/Stationeers)
- [github.com/SnorreSelmer/stationeers_ic10](https://github.com/SnorreSelmer/stationeers_ic10)
- [github.com/Xon/stationeers-ic-scripts](https://github.com/Xon/stationeers-ic-scripts)
- [github.com/drclaw1188/stationeers_ic10](https://github.com/drclaw1188/stationeers_ic10)
- [github.com/jhillacre/stationeers-scripts](https://github.com/jhillacre/stationeers-scripts)

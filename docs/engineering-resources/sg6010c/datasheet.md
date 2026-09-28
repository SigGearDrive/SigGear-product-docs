---
title: SG-6010C Datasheet | 6 Nm, 310 rpm Robot Joint Actuator | SigGear
description: Approved public SG-6010C engineering datasheet with dimensions, torque, speed, electrical parameters, control interfaces and design-in notes.
---

# SG-6010C Technical Datasheet v1.0

**Status:** Approved for Public  
**Release date:** 2026-09-28

SG-6010C is a compact integrated planetary robot joint actuator for applications that require a thin axial profile, moderate torque and relatively high output speed.

Driver, encoder, communication and closed-loop functions apply only to the configuration confirmed in the quotation.

## Key Performance

| Parameter | Value |
| --- | --- |
| Outer diameter | 80.0 mm |
| Product thickness | 34.07 mm |
| Reduction ratio | 9.67:1 |
| Backlash | 15-20 arcmin |
| Rated output torque | 6 Nm |
| Peak output torque | 18 Nm |
| Rated output speed | 310 rpm |
| No-load output speed | 400 rpm |
| Weight | 377 +/- 10 g |
| Allowable radial force | 250 N |
| Allowable axial force | 100 N |

!!! note
    Peak torque is not a continuous rating. Peak-torque duration, duty cycle and thermal suitability must be confirmed for the actual application.

## Motor and Electrical Parameters

| Parameter | Value |
| --- | --- |
| Motor power | 328 W |
| Operating voltage | 24-48 VDC |
| Phase damping | 224 uOhm |
| Phase inductance | 235 uH |
| Phase current full scale | 33 A |
| Rated bus current | 12 A |
| Static working bus current | 0.08 A |
| Motor torque constant | 0.0606 Nm/A |
| Motor structure | 18 slots / 20 poles |
| Thermistor | 10 kOhm B3435 +/-1% |
| NTC B value | 3435 |
| Back EMF constant | 0.0727 Vs/rad |
| Motor KV value | 104 rpm/V |

## Encoder, Driver and Control

The driver-equipped configuration can use the MA600 16-bit single-turn absolute magnetic encoder.

Available control functions for the confirmed driver-equipped configuration can include:

- Position control
- Velocity control
- Torque control
- MIT-style motion control
- PID parameter adjustment
- Calibration and user-zero configuration

## Communication and Expansion

Publicly documented interfaces for the driver-equipped configuration include:

- CAN
- USB Type-C for configuration and debugging
- Second encoder interface supporting I2C / UART on applicable driver-equipped configurations
- Expansion interfaces subject to the selected driver configuration

RS485 and EtherCAT can be evaluated through project-specific expansion hardware.

Driver hardware and firmware can evolve by ordered configuration. Confirm the driver and firmware configuration for the quoted unit before integration.

## Public Engineering Resources

[Download Simplified STEP Model v1.0](../../assets/downloads/sg6010c/SG-6010C_Public_Simplified_STEP_v1.0.step){ .md-button .md-button--primary }

[View Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

## Integration Documentation

Detailed CAN protocol documentation, Quick Start instructions, firmware-specific integration notes and related support files are provided after inquiry so the documentation can be matched to the selected driver and firmware configuration.

[Request Integration Documentation](../../request-cad-sample-quote.md){ .md-button }

## Selection Information Required

Please provide:

- Application and installation position
- Rated and peak torque
- Required output speed
- Operating voltage
- Size and weight limits
- Duty cycle
- Driver and encoder requirement
- Communication interface
- Estimated prototype and annual quantity

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

---
title: SG-8021 Datasheet | 10 Nm, 160 rpm Low-Profile Robot Joint Actuator | SigGear
description: Public SG-8021 engineering reference with published dimensions, torque, speed, electrical parameters, load limits and configuration notes for early evaluation.
---

# SG-8021 Technical Datasheet v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

SG-8021 is a 100 mm low-profile integrated planetary robot joint actuator with a 9.25:1 reduction ratio, 10 Nm rated output torque and 160 rpm rated output speed.

This page consolidates values already published on the current SG-8021 product page. Driver, encoder, communication and closed-loop functions depend on the ordered configuration and must be confirmed in the quotation.

## Key Performance

| Parameter | Published value |
| --- | --- |
| Transmission structure | Planetary gearbox |
| Outer diameter | 100 mm |
| Product thickness | 42.6 mm |
| Reduction ratio | 9.25:1 |
| Backlash | 15-20 arcmin |
| Operating voltage | 24-48 VDC |
| Motor power | 213 W |
| Rated output speed | 160 rpm |
| No-load output speed | 240 rpm |
| Rated output torque | 10 Nm |
| Peak output torque | 30 Nm |
| Weight | 671 g |
| Allowable radial force | 1300 N |
| Allowable axial force | 550 N |

!!! warning
    Peak torque is not a continuous rating. Peak-torque duration, current limit, duty cycle and thermal suitability must be confirmed for the actual application.

## Motor and Electrical Parameters

| Parameter | Published value |
| --- | --- |
| Phase inductance | 290 uH |
| Phase current full scale | 33 A |
| Rated bus current | 12 A |
| Static working bus current | 0.08 A |
| Motor torque constant | 0.046 Nm/A |
| Motor structure | 21 pole pairs |
| Thermistor | 10 kOhm, B3435, +/-1% |
| Back-EMF constant | 0.143 Vs/rad |
| Motor speed constant | 63 rpm/V |

## Driver-Equipped Configuration

The current public SG-8021 product page documents a driver-equipped configuration with functions that can include:

- FOC closed-loop control
- Position control
- Velocity control
- Torque control
- MIT-style motion control
- PID parameter configuration
- Calibration and user-zero configuration
- CAN communication
- USB Type-C configuration / debugging

RS485, EtherCAT and other expansion functions are project-specific and require engineering confirmation.

## Mechanical and Load Evaluation

For early project screening, use the public envelope and load values above.

Final suitability depends on:

- Mounting structure
- Load direction and moment arm
- Duty cycle
- Shock load
- Bearing-life requirement
- Cable / connector orientation
- Driver-equipped or non-driver configuration

[View SG-8021 Mechanical Interface Reference](mechanical-interface.md){ .md-button }

## Internal Structure Reference

The current SG-8021 product page includes a real exploded product photograph showing the planetary transmission, motor and a driver-board configuration.

[View SG-8021 Product and Exploded Structure](../../products/robot-joint-actuators/sg8021.md){ .md-button }

The photograph is an engineering reference image, not a manufacturing drawing. Internal geometry and component details shown in the image should not be used as controlled production dimensions.

## CAD, Drawings and Integration Documentation

A public STEP model is **not currently released in this repository** for SG-8021.

Detailed STEP, controlled drawings, connector / cable information and configuration-specific control documentation should be requested for the intended project.

[Request CAD, Drawing or Integration Files](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Selection Information Required

Please provide:

- Application and joint position
- Rated and peak torque
- Required peak-torque duration
- Required output speed
- Operating voltage
- Installation envelope
- Duty cycle
- Radial and axial load condition
- Driver, encoder and communication requirements
- Prototype quantity and estimated annual quantity

## Related Pages

[SG-8021 Product Page](../../products/robot-joint-actuators/sg8021.md){ .md-button }
[Custom Robot Joint Development](../../custom-engineering/robot-joint-actuator-development.md){ .md-button }
[Robot Joint Selection Guide](../../selection-guides/robot-joint-actuator-selection-guide.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

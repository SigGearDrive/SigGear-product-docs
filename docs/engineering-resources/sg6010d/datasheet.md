---
title: SG-6010D Datasheet | 16 Nm, 100 rpm Robot Joint Actuator | SigGear
description: Public SG-6010D engineering reference with published dimensions, torque, speed, electrical range, load limits and configuration notes for early evaluation.
---

# SG-6010D Technical Datasheet v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

SG-6010D is an 80 mm integrated planetary robot joint actuator for projects that require a higher torque level than the SG-6010C reference platform.

This public datasheet consolidates the specifications already published on the current SG-6010D product page. Driver, encoder, communication and closed-loop functions depend on the ordered configuration and must be confirmed in the quotation.

## Key Performance

| Parameter | Published value |
| --- | --- |
| Transmission structure | Planetary gearbox |
| Outer diameter | 80.0 mm |
| Product thickness | 58.77 mm |
| Reduction ratio | 28.13:1 |
| Backlash | 15-30 arcmin |
| Operating voltage | 24-48 VDC |
| Motor power | 328 W |
| Rated output speed | 100 rpm |
| No-load output speed | 170 rpm |
| Rated output torque | 16 Nm |
| Peak output torque | 50 Nm |
| Weight | 791 g |
| Allowable radial force | 1000 N |
| Allowable axial force | 400 N |

!!! warning
    Peak torque is not a continuous rating. Peak-torque duration, current limit, duty cycle and thermal suitability must be confirmed for the actual application.

## Configuration Boundary

SG-6010D can be supplied in configurations that include:

- Motor + planetary gearbox
- Motor + planetary gearbox + integrated driver + encoder

The final driver, encoder, connector, cable and firmware configuration is confirmed by quotation and order documentation.

## Driver-Equipped Configuration

SigGear has confirmed that the SG6010 driver platform documented in the current SG6010 user manual applies to the driver-equipped SG-6010D configuration.

Confirmed capabilities include:

- 16-bit single-turn absolute magnetic encoder
- FOC closed-loop control
- Position control
- Velocity control
- Torque control
- MIT-style motion control
- CAN Simple
- CANopen (CiA301 / CiA302 / CiA402)
- USB Type-C configuration / debugging
- RS485 / Modbus RTU with the corresponding interface / expansion configuration

EtherCAT and other expansion interfaces remain project-specific and require confirmation.

[View SG-6010D Driver and Communication Reference](driver-communication.md){ .md-button }

## Mechanical and Load Evaluation

For early packaging and load screening, use the published envelope and load limits above.

Final design-in must also consider:

- Actual mounting interface
- Load direction and load offset
- Duty cycle and shock loading
- Peak-torque duration
- Cable / connector orientation
- Driver-equipped or non-driver configuration

[View SG-6010D Mechanical Interface Reference](mechanical-interface.md){ .md-button }

## CAD, Drawings and Integration Documentation

A public STEP model is **not currently released in this repository** for SG-6010D.

Detailed STEP, controlled drawings, CAN / integration documentation and configuration-specific files should be requested for the intended project so the files can be matched to the ordered configuration.

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

[SG-6010D Product Page](../../products/robot-joint-actuators/sg6010d.md){ .md-button }
[Custom Robot Joint Development](../../custom-engineering/robot-joint-actuator-development.md){ .md-button }
[Robot Joint Selection Guide](../../selection-guides/robot-joint-actuator-selection-guide.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

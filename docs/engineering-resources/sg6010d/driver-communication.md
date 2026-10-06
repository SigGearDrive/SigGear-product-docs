---
title: SG-6010D Driver and Communication | CAN, CANopen, RS485, Control Modes | SigGear
description: Confirmed driver-equipped SG-6010D reference covering encoder, CAN, CANopen, RS485 Modbus RTU, control modes and key driver limits.
---

# SG-6010D Driver and Communication Reference v1.0

**Status:** Public engineering integration reference  
**Release date:** 2026-10-06

SigGear has confirmed that the current SG6010 driver platform documented in the SG6010 user manual applies to the **driver-equipped SG-6010D configuration**.

This page summarizes the integration information that is suitable for public engineering evaluation. Firmware revision and ordered hardware configuration must still be confirmed before final integration.

## Driver Electrical Reference

| Parameter | Confirmed manual value |
| --- | --- |
| Rated driver voltage | 15~48 V DC |
| Minimum / maximum driver voltage | 12/72 V DC |
| Rated current | 6 A |
| Maximum line current | 30 A |
| Maximum phase current | 90 A |
| Standby power consumption | <10 mA |
| CAN maximum bitrate | 1 Mbps |
| USB Type-C rate | 10 Mbps |
| Encoder resolution | 16-bit single-turn absolute |
| Driver operating temperature | -20°C to 70°C |
| Motor over-temperature alarm | 90°C, adjustable |
| Driver over-temperature alarm | 90°C, adjustable |

!!! warning
    These are driver-platform limits and are not a substitute for the SG-6010D actuator operating limits, current limits, torque limits or thermal validation for a specific application.

## Confirmed Interfaces

The driver platform includes or supports:

- Power + CAN integrated connector
- USB Type-C debugging / host communication
- Second encoder interface using I2C or UART
- SWD programming / debugging
- Motor temperature input
- Brake / braking-resistor interface
- Minimum / maximum limit-switch inputs
- Expansion interface for additional functions

The expansion slot can support additional interfaces such as RS485 and other project-specific expansion hardware. EtherCAT remains subject to project configuration and confirmation.

## Confirmed Communication Protocols

### CAN Simple

The SG6010 driver manual documents the CAN Simple protocol with:

- Standard 11-bit CAN ID
- 8-byte data frame
- Configurable node ID
- Configurable CAN bitrate
- Factory default CAN bitrate documented as 500 kbps
- Maximum CAN bitrate documented as 1 Mbps

### CANopen

The same driver platform supports CANopen and the manual documents implementation against:

- CiA301
- CiA302
- CiA402

An EDS file is used for CANopen integration. Firmware / EDS revision must be matched to the delivered driver.

### RS485 / Modbus RTU

RS485 with Modbus RTU is supported on the confirmed SG6010 driver platform when the corresponding RS485 interface / expansion configuration is supplied.

The manual documents up to 115200 bps for the RS485 implementation.

## Confirmed Control Modes

The driver platform supports:

- Position control
- Velocity control
- Torque control
- MIT-style motion control

The manual further documents filtered / trajectory / circular position modes, direct / ramped velocity control and direct / ramped torque control.

## Encoder and Feedback

The driver platform uses a 16-bit single-turn absolute magnetic encoder in the driver-equipped configuration.

The second-encoder interface can communicate through:

- I2C
- UART

Final second-encoder hardware, mounting and firmware configuration must be confirmed for the order.

## Integration Boundary

Before final integration, confirm:

- Driver hardware revision
- Firmware revision
- CAN / CANopen / RS485 interface selected
- EDS / endpoint file matched to firmware
- Encoder configuration
- Brake / braking-resistor function
- Connector and cable set
- Current and speed limits
- Customer controller requirements

[Request Integration Files](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Resources

[SG-6010D Technical Datasheet](datasheet.md){ .md-button }
[SG-6010D Mechanical Interface](mechanical-interface.md){ .md-button }
[SG-6010D Product Page](../../products/robot-joint-actuators/sg6010d.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

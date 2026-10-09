---
title: SG-6010HB Driver and Communication | CAN, CANopen, RS485, MIT Control | SigGear
description: Confirmed driver-equipped SG-6010HB integration reference covering 16-bit absolute encoder, CAN Simple, CANopen CiA402, RS485 Modbus RTU, position, velocity, torque and MIT-style control.
---

# SG-6010HB Driver and Communication Reference v1.0

**Status:** Public engineering integration reference  
**Release date:** 2026-10-09  
**Configuration boundary:** Applies to the current **driver-equipped SG-6010HB configuration** using the confirmed SG6010 driver platform.

SigGear has confirmed that the SG6010 driver platform documented in the current SG6010 user manual applies to the present driver-equipped SG-6010HB configuration.

This page summarizes the integration information suitable for early engineering evaluation. Final driver hardware revision, firmware revision, cable set and ordered interface configuration must still be matched to the delivered unit.

## System Voltage Boundary

The mechanical actuator catalog and the driver manual use different voltage descriptions:

| Item | Published / confirmed value |
| --- | --- |
| SG-6010HB catalog rated-voltage range | 12–48 V |
| Driver rated voltage | 15–48 V DC |
| Driver minimum / maximum voltage boundary | 12 / 72 V DC |

For a **driver-equipped SG-6010HB system**, do not treat the driver's 12 V minimum boundary as a rated continuous operating point.

Final power-supply selection should use the actual actuator configuration, required torque-speed point, driver revision and current limits.

## Driver Electrical Reference

| Parameter | Confirmed manual value |
| --- | --- |
| Rated driver voltage | 15–48 V DC |
| Minimum / maximum driver voltage | 12 / 72 V DC |
| Rated current | 6 A |
| Maximum line current | 30 A |
| Maximum phase current | 90 A |
| Standby consumption | <10 mA |
| CAN maximum bitrate | 1 Mbps |
| USB Type-C rate | 10 Mbps |
| Main encoder resolution | 16-bit single-turn absolute |
| Driver operating temperature | -20°C to 70°C |
| Motor over-temperature alarm | 90°C, adjustable |
| Driver-board over-temperature alarm | 90°C, adjustable |

!!! warning
    These are **driver-platform values**. They are not replacements for the SG-6010HB actuator torque, speed, thermal or duty-cycle limits.

## Confirmed Hardware Interfaces

The confirmed driver platform provides or supports:

- Combined power + CAN connector
- USB Type-C debugging / host communication
- Main 16-bit single-turn absolute encoder
- Second-encoder interface using I2C or UART
- SWD programming / debugging interface
- Motor NTC temperature input
- Brake / braking-resistor interface
- Minimum / maximum limit-switch inputs
- Expansion interface for additional project-specific functions

The second-encoder interface does **not** mean that every SG-6010HB is supplied as a dual-encoder unit. The actual second encoder, mechanical mounting and firmware configuration must be confirmed for the ordered version.

## CAN Simple

The SG6010 driver manual documents a CAN Simple protocol with:

- Standard CAN communication
- Configurable node ID
- Position command support
- Velocity command support
- Torque command support
- Current / velocity limit settings
- Periodic message configuration
- MIT-style motion-control commands

The manual documents a **maximum CAN bitrate of 1 Mbps**.

Final node ID, bitrate, command scaling and firmware revision should be confirmed before controller integration.

## CANopen

The confirmed driver platform includes CANopen support.

The manual states implementation against:

- **CiA301**
- **CiA302**
- **CiA402**

The documented CANopen implementation includes the CiA402 servo state machine and operating modes including position-, velocity- and torque-related servo modes.

A matching EDS / object-dictionary revision should be supplied for the delivered firmware when CANopen is selected.

## RS485 / Modbus RTU

The SG6010 manual contains an RS485 communication section using **Modbus RTU**.

The documented implementation states:

- Maximum communication speed: **115200 bps**
- Factory default communication speed: **115200 bps**
- Standard Modbus RTU register operations are documented

RS485 hardware availability depends on the supplied interface / expansion configuration. Confirm the actual connector and hardware version before final integration.

## Control Modes

The driver manual documents four main control families:

- **Position control**
- **Velocity control**
- **Torque control**
- **Motion control / MIT-style control**

Additional documented control behaviors include:

### Position

- Filtered Position Control
- Trajectory / trapezoidal position control
- Circular Position Control

### Velocity

- Direct Velocity Control
- Ramped Velocity Control

### Torque

- Direct Torque Control
- Ramped Torque Control

### MIT-Style Motion Control

Motion control combines position, velocity and torque terms.

The manual notes an important integration distinction: USB-side commands and CAN MIT protocol commands may use different reference-side conventions. Controller integration should therefore follow the exact protocol definition for the delivered firmware rather than assuming that all command channels use the same coordinate convention.

## Encoder and Feedback

The confirmed driver platform specifies a:

**16-bit single-turn absolute main encoder**

A second-encoder interface is available through:

- I2C
- UART

The second encoder is a configurable interface capability, not a universal statement that every delivered SG-6010HB includes two physical encoders.

## Temperature and Protection

The driver platform supports:

- Motor NTC temperature input
- Motor temperature alarm: **90°C adjustable**
- Driver-board temperature alarm: **90°C adjustable**
- Configurable current limit
- Configurable speed limit

The driver manual also documents temperature-dependent current limiting.

These protection functions do not replace application-specific thermal validation.

[View SG-6010HB Thermal Test Record](thermal-test-record.md){ .md-button }

## Expansion Interface Boundary

The driver platform documentation describes an expansion interface capable of supporting additional functions / protocols such as:

- RS485
- EtherCAT
- SPI / USART / I2C / PWM / ADC / GPIO based expansion
- Pulse / direction and other project-specific interfaces

**EtherCAT is not presented here as a standard SG-6010HB interface.** It remains subject to expansion hardware, firmware and project confirmation.

## Integration Checklist

Before final integration, confirm:

- Driver hardware revision
- Firmware revision
- Power-supply voltage and current capability
- CAN / CANopen / RS485 interface selected
- CAN bitrate and node-ID plan
- CANopen EDS / object dictionary revision
- Main / second encoder configuration
- Connector and cable set
- Motor and driver temperature thresholds
- Current and speed limits
- Brake / braking-resistor configuration
- Customer controller architecture
- Whether an expansion interface such as EtherCAT is required

[Request Integration Files](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Resources

[SG-6010HB Product Page](../../products/robot-joint-actuators/sg6010hb.md){ .md-button }
[SG-6010HB Technical Datasheet](datasheet.md){ .md-button }
[SG-6010HB Mechanical Interface](mechanical-interface.md){ .md-button }
[SG-6010HB Thermal Test Record](thermal-test-record.md){ .md-button }
[Exoskeleton Joint Selection Guide](../../applications/exoskeleton-joint-actuators.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

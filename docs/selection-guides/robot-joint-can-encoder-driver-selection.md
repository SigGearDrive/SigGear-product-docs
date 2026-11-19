---
title: Robot Joint CAN, Encoder & Driver Selection Guide | SigGear
description: Engineering checklist for robot joint actuator CAN, encoder, driver and feedback requirements. Clarify control architecture before requesting a joint actuator quotation or prototype.
---

# Robot Joint CAN, Encoder & Driver Selection Guide

A robot joint actuator should not be selected from torque and speed alone. The encoder, driver, control mode and communication interface must match the robot controller and the exact actuator configuration.

SigGear publishes joint products with different electronics arrangements. **Do not assume CAN, RS485, EtherCAT, an integrated driver or an absolute encoder is standard across every model.**

## Start With the Control Architecture

Before requesting a quotation, define which parts are already fixed:

- robot main controller
- motor driver
- motor commutation feedback
- output position feedback
- communication bus
- control mode
- bus voltage
- continuous and peak current limits

If these are still open, provide the robot architecture and the functions required from the joint.

## Encoder Questions

Clarify whether the project requires:

- Hall sensors for commutation
- motor-side encoder
- output-side encoder
- single-turn absolute position
- multi-turn position
- incremental feedback
- redundant feedback
- a specific resolution
- a specific electrical interface

Encoder requirements affect mechanical packaging, wiring, calibration and driver compatibility.

## Driver Questions

Confirm whether the project requires:

- an integrated driver
- an external driver
- position control
- velocity control
- torque / current control
- FOC or another motor-control method
- current and voltage limits
- regenerative-energy handling
- PC configuration / debugging tools

A published actuator may have several electronics variants. The quoted hardware and firmware configuration must be confirmed before prototype release.

## Communication Questions

Common project requirements can include:

- CAN
- RS485
- EtherCAT
- USB for configuration / debugging
- another project-specific interface

The communication choice should be defined together with network topology, update rate, cable length, connector strategy, controller compatibility and required control modes.

## Why “Supports CAN” Is Not Enough

For a robot project, ask for the exact protocol and configuration rather than only the physical bus name.

Useful questions include:

1. Is CAN physically available on this hardware version?
2. Which messages and control modes are supported?
3. Is the protocol fixed or project-configurable?
4. Which encoder and driver version is used?
5. What voltage and current limits apply?
6. Is the communication documentation available for the quoted configuration?
7. What PC tool or commissioning procedure is required?

## SigGear Product References

SigGear's published robot joint product pages identify model-specific electronics where available.

[Planetary Robot Joint Actuators](../products/robot-joint-actuators/index.md){ .md-button .md-button--primary }
[Cycloidal Joint Modules](../products/cycloidal-joint-modules/index.md){ .md-button }
[Robot Joint Datasheets & CAD](../engineering-resources/robot-joint-actuators/quick-downloads.md){ .md-button }

Where a product page labels an interface as optional, project-specific or subject to confirmation, treat it as **not standard until confirmed in the quotation**.

## Minimum Control Information to Send

For an engineering review, provide:

| Category | Information |
| --- | --- |
| Main controller | MCU, industrial controller, Jetson / PC or other controller |
| Bus | CAN, RS485, EtherCAT or other |
| Control mode | position, velocity, torque / current or mixed |
| Feedback | motor-side, output-side, absolute / incremental and required resolution |
| Voltage | nominal and maximum bus voltage |
| Current | continuous and peak current limits |
| Joint behavior | torque, speed, duty cycle and holding requirement |
| Safety | brake, power-off behavior and emergency-stop requirement |
| Prototype | quantity and planned test setup |

## Mechanical and Electrical Selection Must Stay Connected

Changing the reducer ratio, motor, encoder, driver or supply voltage can change the available torque-speed operating point, thermal behavior, package length, wiring and control limits.

For that reason, final actuator selection should be reviewed as one configuration rather than as separate component specifications.

[Robot Joint Actuator Selection Guide](robot-joint-actuator-selection-guide.md){ .md-button }
[Custom Robot Joint Development](../custom-engineering/robot-joint-actuator-development.md){ .md-button }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }

**Contact:** Wanrong Wang · International Sales / Sales Engineer, SigGear · wangwanrong@siggear.com

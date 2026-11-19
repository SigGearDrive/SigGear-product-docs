---
title: Integrated Robot Joint Actuator vs Motor + Gearhead | SigGear
description: Compare an integrated robot joint actuator with a separate motor + planetary gearhead architecture by packaging, control, encoder, serviceability, customization and engineering workload.
---

# Integrated Robot Joint Actuator vs Motor + Gearhead

A robotics team may choose either an integrated robot joint actuator or a separate motor + gearhead architecture. The better starting point depends on how much of the motor, controller, encoder, mechanical interface and joint packaging is already fixed.

SigGear supports both paths: published robot joint actuator platforms and 8–42 mm planetary gearheads that can be evaluated with an existing or selected motor.

## Quick Decision Guide

| Project situation | Practical starting point |
| --- | --- |
| Motor, driver and control stack are already selected | Gearhead-only or motor + gearhead integration review |
| Team wants a compact joint package with motor, transmission and feedback reviewed together | Integrated actuator reference |
| Existing mechanism fixes the motor shaft and mounting pattern | Gearhead / motor-interface review |
| Joint envelope, torque and speed are known but electronics are open | Compare integrated actuator and separate architecture |
| Prototype needs fast mechanical packaging with public CAD | Start from the closest released product platform |
| Production design needs a special shaft, flange, cable or ratio | Project-specific engineering review |

This is a screening guide only. Final selection depends on the complete operating condition.

## Integrated Robot Joint Actuator

An integrated actuator can combine several functions in one joint package, depending on the selected model and configuration:

- motor
- reducer / gearbox
- encoder or feedback device
- output bearing structure
- driver where applicable
- cable / connector arrangement
- joint-side mechanical interfaces

### Potential advantages

- fewer separate mechanical interfaces to define
- compact packaging around one known joint envelope
- easier early CAD integration when a released STEP model is available
- motor, reducer and feedback can be reviewed as one system

### Items still requiring confirmation

- continuous and peak torque
- peak duration
- rated and maximum speed
- driver and encoder version
- communication interface
- brake or power-off behavior
- external loads
- thermal condition
- connector and cable configuration

Do not assume that every integrated actuator includes the same driver, encoder or communication protocol.

[Browse SigGear Robot Joint Actuators](../products/robot-joint-actuators/index.md){ .md-button .md-button--primary }

## Separate Motor + Gearhead Architecture

A separate architecture may be preferred when the robotics team already controls the motor, electronics or mechanical design.

Typical starting conditions include:

- an existing BLDC, DC or other motor must be retained
- the controller and encoder architecture are already fixed
- only the reduction stage needs to change
- the gearbox must fit an existing motor shaft and pilot
- the output shaft or flange is application-specific
- a smaller transmission is needed for a hand, gripper or auxiliary mechanism

SigGear publishes 8P–42P planetary gearhead platforms with public datasheets and CAD resources.

[Browse 8–42 mm Planetary Gearheads](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }
[Motor + Gearhead Integration](../custom-engineering/motor-gearbox-integration.md){ .md-button }

## If You Already Have a Motor

Send:

- motor model or drawing
- nominal voltage
- rated / no-load speed
- shaft diameter and usable length
- mounting-hole pattern
- locating pilot
- required output speed
- continuous and peak torque / load
- maximum diameter and total assembly length

A preliminary ratio may be estimated from motor speed divided by target output speed, but the final configuration also needs stage availability, torque, efficiency, duty cycle and motor operating point.

[Custom Planetary Gearhead for an Existing Motor](../custom-engineering/custom-planetary-gearbox.md){ .md-button }

## Compare the Complete Joint, Not Only the Reducer

When comparing an integrated actuator with a separate motor + gearhead, use the same boundary conditions:

| Category | Compare |
| --- | --- |
| Mechanics | complete diameter, thickness, length, weight, shaft / flange and mounting |
| Performance | continuous torque, peak torque + duration, speed and duty cycle |
| Loads | radial, axial and overturning loads |
| Precision | backlash, accuracy, repeatability and encoder resolution |
| Electrical | voltage, current limits, motor operating point and regenerative behavior |
| Control | driver location, control mode and communication |
| Thermal | housing, mounting material, enclosure and cooling path |
| Service | replaceable subassemblies, cable access and maintenance strategy |
| Production | prototype quantity, customization scope and design freeze |

## SigGear Public Engineering Resources

For standard robot joint products:

[Robot Joint Datasheets, 2D & STEP](../engineering-resources/robot-joint-actuators/quick-downloads.md){ .md-button .md-button--primary }

For separate planetary gearheads:

[12 Gearhead Datasheets, 2D & STEP](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }

## What to Send First

You do not need to decide the architecture before contacting SigGear.

Send the joint or mechanism requirement, existing motor / controller information if any, target torque, speed, installation envelope and prototype quantity. The first review can determine whether an integrated actuator, motor + gearhead assembly or gearbox-only path is more appropriate to evaluate.

[Robot Joint Actuator Selection Guide](robot-joint-actuator-selection-guide.md){ .md-button }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }

**Contact:** Wanrong Wang · International Sales / Sales Engineer, SigGear · wangwanrong@siggear.com

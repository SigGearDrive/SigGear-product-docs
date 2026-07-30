---
title: Humanoid Robot Joint Actuator Selection Guide | Torque, Speed and Gearbox
description: Learn how to select humanoid robot joint actuators by continuous and peak torque, speed, duty cycle, size, weight, backlash, encoder, driver and transmission type.
---

# Humanoid Robot Joint Actuator Selection Guide

Selecting a humanoid robot joint actuator requires matching torque, speed, gearbox architecture, installation size, weight, duty cycle and control requirements for each axis. Shoulder, elbow, wrist, hip, knee, ankle, neck and waist joints should not be sized from peak torque alone.

[Robot Joint Actuator Selection Guide](../selection-guides/robot-joint-actuator-selection-guide.md){ .md-button .md-button--primary }
[View Joint Actuator Products](../products/robot-joint-actuators/index.md){ .md-button }
[Request CAD, Sample and Quote](../request-cad-sample-quote.md){ .md-button }

## Application Overview

Humanoid robots require compact joint actuators for the shoulder, elbow, wrist, hip, knee, ankle, neck and waist axes. Each joint has a different torque-speed cycle, external-load condition, installation envelope, thermal limit and control requirement. A humanoid robot joint actuator should therefore be selected from the complete operating profile, not from peak torque alone.

SigGear supports humanoid robot development with integrated robot joint actuator options, planetary joint actuators, cycloidal joint modules and compact planetary gearbox solutions. Depending on the selected configuration, a joint drive may combine a motor, reducer, encoder and driver, or it may be supplied as a reducer or gearbox for customer-side motor integration.

This page is intended for early-stage model selection, supplier comparison and engineering communication. Final actuator selection, quotation and technical agreement still require review against the controlled drawing, selected ratio, duty cycle, mounting interface and ordered configuration.

## How to Select a Humanoid Robot Joint Actuator

A practical early-stage selection process should cover the following steps:

1. **Define the joint position and motion cycle** — Separate shoulder, elbow, wrist, hip, knee and ankle requirements instead of applying one actuator specification to every axis.
2. **Calculate continuous and peak torque** — Include gravity, acceleration, external forces, mechanism losses and the duration and frequency of peak events.
3. **Match output speed and power** — Check torque and speed at the same operating point and confirm the available voltage and controller current limits.
4. **Set the installation envelope** — Define maximum diameter, axial thickness, length, weight, cable space, bearing arrangement and output interface.
5. **Choose the transmission architecture** — Compare planetary and cycloidal options, or an integrated actuator versus a separate motor and gearbox.
6. **Confirm control and thermal conditions** — Review encoder, driver, communication, duty cycle, cooling, brake and power-off behavior.
7. **Validate with a prototype** — Test the actuator in a representative mechanism with realistic loads, motion cycles and temperature monitoring.

For torque formulas, sizing steps and a complete engineering checklist, use the [Robot Joint Actuator Selection Guide](../selection-guides/robot-joint-actuator-selection-guide.md).

## What a Humanoid Joint Actuator Must Define

A humanoid joint is not defined only by rated torque. The following parameters should be reviewed together:

| Requirement | Why it matters |
| --- | --- |
| Continuous torque | Determines whether the joint can sustain walking, lifting, balancing or holding conditions without overheating. |
| Peak torque and peak duration | Important for acceleration, recovery motion, impact events and short overload conditions. |
| Output speed | Must match the robot motion profile and motor operating range. |
| Outer diameter and axial thickness | Controls whether the actuator fits inside the limb, torso or joint shell. |
| Weight | Affects leg swing inertia, arm payload, power consumption and whole-body balance. |
| Backlash and positioning requirement | Influences stability, repeatability, force control and motion smoothness. |
| Radial, axial and overturning loads | Affect the bearing, housing and output-interface design. |
| Duty cycle and cooling | Determine whether torque values are usable continuously or only for short periods. |
| Encoder, driver and communication interface | Affect closed-loop control, wiring, protocol integration and software development. |

## Joint Positions and Typical Review Focus

### Shoulder Joint

The shoulder may include pitch, roll and yaw axes. It often requires compact packaging, sufficient peak torque for arm acceleration and careful cable routing through the upper body. External loads from the arm, gripper and carried object should be considered.

### Elbow Joint

The elbow usually needs a balance between torque, speed and compact axial length. For prototype humanoid arms, an integrated actuator can reduce assembly work, but the final selection should still confirm continuous holding torque, backlash and thermal conditions.

### Wrist Joint

The wrist is sensitive to size and weight. Lower inertia and compact output interfaces are usually important. Small planetary gearboxes or compact joint actuators may be considered when the required torque is lower than the shoulder or elbow.

### Hip Joint

The hip is one of the highest-load areas in a humanoid robot. It may require higher continuous torque, high peak torque and strong structural support. Overturning moment, radial load, shock load and housing stiffness are especially important.

### Knee Joint

The knee joint is strongly affected by walking, squatting, standing-up and impact recovery cycles. Continuous torque, peak duration, braking strategy, thermal behavior and mechanical safety margin should be reviewed carefully.

### Ankle Joint

The ankle often combines torque, shock load and packaging difficulty. It can be sensitive to backlash, compliance, sealing, cable routing and impact load. Prototype testing is usually important before locking the actuator model.

## Candidate SigGear Joint Products

The following published SigGear models can be considered as starting points for humanoid robot joint evaluation. Final selection depends on the exact joint position, torque-speed cycle, duty cycle, external loads, size limits and control architecture.

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver options depend on selected configuration. |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver. |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver options depend on selected configuration. |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver. |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver. |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and no integrated driver. |

For smaller auxiliary joints, sensor mechanisms, hands, compact wrists or lightweight adjustment axes, SigGear can also evaluate [8–42 mm planetary gearbox](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md) options when the customer already has a motor or needs a customized motor-gearbox combination.

## Integrated Actuator or Separate Gearbox and Motor

A humanoid project may use an integrated actuator or a separate gearbox-and-motor architecture.

An integrated robot joint actuator may be suitable when the engineering team wants a more complete module with a matched motor, reducer, encoder and driver option. This can reduce early prototype integration work and speed up testing.

A separate gearbox and motor solution may be suitable when the robot team already has its own motor, controller, encoder, housing or thermal design. In this case, the gearbox interface, input speed, motor shaft, mounting pattern and output shaft must be confirmed carefully.

SigGear can support both approaches depending on the model, quantity, customization scope and engineering feasibility.

## Planetary or Cycloidal Drive for Humanoid Robots

A planetary joint actuator may be considered when the project prioritizes compact integration, output speed, motor matching flexibility and broad configuration options.

A cycloidal joint module may be considered when the application requires compact high-torque transmission and the selected model's speed, backlash, installation structure and duty cycle match the joint requirement.

Neither transmission type should be selected from a general rule alone. Compare the complete torque-speed cycle, external loads, backlash target, thermal condition, size limit, weight target, control architecture and production plan.

## Control, Encoder and Communication Review

Humanoid robot teams should confirm the control architecture early. Important questions include:

- Is the joint controlled by position, speed, torque or mixed control mode?
- Is the driver integrated into the actuator or placed on a separate robot controller board?
- Is CAN, RS485, PWM or another interface required?
- What encoder resolution and position feedback accuracy are needed?
- Is the control loop closed at the actuator, at the main robot controller or both?
- Are there requirements for current limit, temperature monitoring, fault reporting or brake control?

Communication and control functions vary by selected product and electronics configuration. Do not assume CAN, RS485, EtherCAT, PID, torque control or a specific protocol without confirming the driver and firmware version.

## Torque, Speed and Thermal Selection

For each joint, provide the full motion cycle instead of only the maximum torque value. Useful information includes:

- Continuous torque during holding or walking
- Peak torque and peak duration
- Target output speed and acceleration
- Operating voltage and current limit
- Motion time, rest time and duty cycle
- Ambient temperature and cooling method
- Mounting structure and heat dissipation path
- Expected test duration and service-life target

Peak torque is not a continuous working rating. A joint that can provide short peak torque may still be unsuitable if the repeated duty cycle causes excessive temperature rise.

[Open the torque calculation and actuator sizing guide](../selection-guides/robot-joint-actuator-selection-guide.md)

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Communication and control configuration
- Customer branding and labeling
- Prototype support before production planning

Customization availability depends on technical feasibility, prototype quantity, expected annual volume and the level of engineering change required.

## Information Needed for a Humanoid Joint Selection Review

Please send one requirement set for each joint position. For example, shoulder, elbow, wrist, hip, knee and ankle should be reviewed separately.

Provide:

- Robot type and target application
- Joint position and axis definition
- Continuous torque
- Peak torque and peak duration
- Required output speed
- Operating voltage and current limit
- Maximum outer diameter, thickness and weight
- Radial load, axial load and overturning moment
- Backlash and positioning requirement
- Encoder, driver and communication requirements
- Duty cycle, ambient temperature and cooling method
- Prototype quantity and estimated annual quantity
- Preferred architecture: integrated actuator or separate gearbox and motor

## Request a Joint Selection Review

Send your humanoid robot joint requirements to SigGear for a preliminary model review. Early requirements can be rough, but torque, speed, size, voltage and quantity are needed before a meaningful recommendation can be made.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request CAD, Sample and Quote](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Humanoid Joint Requirements](../contact.md){ .md-button }

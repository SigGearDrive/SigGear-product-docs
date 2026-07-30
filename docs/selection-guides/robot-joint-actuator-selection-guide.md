---
title: Robot Joint Torque Calculation and Actuator Sizing Guide
description: Calculate robot joint torque and select an actuator by continuous and peak torque, speed, duty cycle, size, gearbox type, encoder, driver and thermal limits.
---

# Robot Joint Torque Calculation and Actuator Sizing Guide

Use this engineering guide to estimate robot joint torque, separate continuous and peak requirements, check output speed and power, and shortlist a planetary or cycloidal actuator architecture. Final model approval still requires engineering review and prototype validation.

[Humanoid Robot Joint Guide](../applications/humanoid-robot-joint-actuators.md){ .md-button .md-button--primary }
[View Joint Actuator Products](../products/robot-joint-actuators/index.md){ .md-button }
[Request CAD, Sample and Quote](../request-cad-sample-quote.md){ .md-button }

## Quick Robot Joint Actuator Sizing Workflow

1. Define the joint position, payload, link geometry and complete motion cycle.
2. Estimate gravity, acceleration and external-force torque.
3. Separate continuous torque from peak torque and define peak duration.
4. Check output speed, power, voltage and controller current limits at the same operating point.
5. Confirm diameter, thickness, length, weight and external bearing loads.
6. Compare planetary, cycloidal and integrated-actuator architectures.
7. Confirm encoder, driver, communication, thermal and safety requirements.
8. Validate the selected actuator in a representative prototype.

## Purpose of This Guide

A robot joint actuator should be selected from the complete axis requirement, not from one torque value or a product-family label. The joint position, payload, link geometry, acceleration, external forces, duty cycle, installation envelope, bearing loads, feedback architecture and controller limits all affect the final choice.

This guide provides a practical screening workflow for humanoid robots, quadruped robots, robotic arms, exoskeletons and other rotary-axis systems. Final model approval requires engineering review and prototype validation.

## Step 1: Define the Joint and Mechanism

Prepare a separate requirement sheet for each axis. A shoulder, elbow, wrist, hip, knee or ankle normally has a different load case, motion profile and installation limit.

Record:

- Joint or axis position
- Payload and moving-link mass
- Link lengths
- Center-of-gravity locations
- Joint angle range
- External process forces
- Mechanical stops and collision loads
- Whether the axis is horizontal, vertical or gravity loaded
- Customer-side bearings, belts, pulleys, gears or linkages

Do not apply one actuator specification to every axis of the robot.

## Step 2: Estimate Robot Joint Output Torque

### Gravity Torque

For an initial one-axis estimate, gravity torque may be approximated by:

`T_gravity = m × g × r × sin(theta)`

where:

- `m` is the supported mass
- `g` is gravitational acceleration
- `r` is the distance from the joint axis to the center of gravity
- `theta` describes the mechanism orientation relative to gravity

The worst posture may not be the robot's normal operating posture, so review the full joint-angle range.

### Acceleration Torque

The torque required to accelerate the reflected inertia may be estimated by:

`T_acceleration = J × alpha`

where:

- `J` is the total inertia reflected to the joint output
- `alpha` is angular acceleration

Include the payload, links, tooling and any other moving components.

### External-Force Torque

An external force acting at a distance from the joint axis creates torque:

`T_external = F × r`

where `F` is the external force and `r` is the perpendicular lever arm.

### Preliminary Total

A preliminary requirement should include gravity, acceleration, external forces, friction and mechanism losses. These equations are screening tools only. Flexible structures, impact, control behavior, load sharing and multi-axis dynamics may require a more complete model.

## Step 3: Separate Continuous and Peak Torque

Continuous torque and peak torque are not interchangeable.

### Continuous Torque

Continuous torque must cover sustained motion, repeated cycles and holding conditions without exceeding the approved thermal limits of the selected motor, gearbox and driver configuration.

### Peak Torque

Peak torque is used for short events such as acceleration, disturbance recovery, impact response or starting under load. Specify:

- Required peak torque
- Peak duration
- Frequency of peak events
- Time between peaks
- Controller current limit
- Battery or bus voltage
- Cooling and ambient conditions

Never treat a published peak-torque value as a continuous rating.

## Step 4: Define Speed and the Complete Motion Cycle

Provide:

- Rated output speed
- Maximum output speed
- Acceleration and deceleration
- Travel angle
- Cycle time
- Holding time
- Rest time
- Direction-reversal frequency

Mechanical output power at an operating point is related to torque and angular speed:

`P = T × omega`

Torque and speed must be checked at the same operating point. A product's maximum torque and maximum speed may not be available simultaneously.

## Step 5: Establish the Installation Envelope

Define the maximum:

- Outer diameter
- Axial thickness
- Total length
- Weight
- Cable and connector space
- Driver-board space
- Brake space
- Mounting-flange envelope

Include the complete installed assembly, not only the reducer body. Bearings, output interfaces, covers, connectors and cable bend radius can consume significant space.

## Step 6: Review Radial, Axial and Overturning Loads

Output torque alone does not describe the structural load on a robot joint.

Provide:

- Radial load
- Axial load
- Overturning moment
- Load direction
- Distance from the load to the output bearing
- Impact or shock conditions
- Customer-side bearing arrangement

The output bearing and housing must be evaluated together with the robot structure. An external bearing or additional support may be required when the joint has a large cantilevered load or overturning moment.

## Step 7: Define Positioning and Mechanical Behavior

Specify the completed-axis targets for:

- Backlash
- Positioning accuracy
- Repeatability
- Angular resolution
- Stiffness or compliance
- Backdrivability
- Holding behavior
- Direction-reversal response

Gearbox backlash is only one part of joint behavior. Encoder position, bearing clearance, housing stiffness, link compliance, assembly tolerances and controller tuning also affect the result.

## Step 8: Choose a Transmission and Product Architecture

SigGear publishes both planetary joint actuators and cycloidal joint modules. Neither transmission type should be selected from a general rule alone.

### Planetary Joint Actuators

Planetary joint actuators may be evaluated when their published torque, speed, dimensions and configuration fit the application. SigGear's published planetary joint-actuator range includes SG-6010C, SG-6010D and SG-8021.

[View planetary robot joint actuators](../products/robot-joint-actuators/index.md)

### Cycloidal Joint Modules

Cycloidal joint modules may be evaluated when the selected model's torque, speed, installation and configuration match the axis requirement. SigGear's published range includes CPM-100-25, CPM-80-25 and CPM-78-39.

[View cycloidal joint modules](../products/cycloidal-joint-modules/index.md)

### Published Starting Points

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver and encoder functions depend on selected configuration |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver and encoder functions depend on selected configuration |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and has no integrated-driver claim |

The table is a preliminary shortlist only. Dimensions, weight, external-load capacity, thermal behavior and control configuration must also be checked.

## Step 9: Define Encoder, Driver and Communication Requirements

Confirm whether the project requires:

- Motor commutation feedback
- Output absolute position
- Incremental or absolute encoder
- Position control
- Velocity control
- Torque or current control
- CAN
- RS485
- EtherCAT or another project-specific interface
- External controller or integrated driver
- Required communication rate and protocol details

Driver, encoder, communication and closed-loop functions are model- and configuration-specific. Do not assume that every actuator includes the same electronics.

CPM-78-39 must be treated separately: its standard catalog configuration uses Hall sensors and does not support a general claim of an integrated driver or absolute encoder.

## Step 10: Review Voltage, Current and Power Architecture

Specify:

- Nominal bus voltage
- Minimum and maximum bus voltage
- Continuous current limit
- Peak current limit and duration
- Battery or power-supply capability
- Regenerative-energy handling
- Emergency-stop behavior
- Cable and connector current capacity

The controller current limit directly affects available torque. Electrical limits must be checked together with the motor, thermal design and duty cycle.

## Step 11: Evaluate Thermal Conditions and Duty Cycle

Provide:

- Ambient temperature
- Operating time
- Holding time
- Rest time
- Cycle frequency
- Enclosure and mounting material
- Cooling method
- Airflow or conduction path
- Nearby heat sources

A joint mounted inside a sealed limb or compact housing may behave differently from the same actuator tested in open air. Prototype testing should reproduce the planned installation and motion cycle.

## Step 12: Define Brake, Safety and Power-Off Behavior

For gravity-loaded, wearable or safety-related axes, specify:

- Whether the joint may move when power is removed
- Required holding torque
- Mechanical brake requirement
- Emergency-stop behavior
- Manual release requirement
- Safe direction of motion
- Collision or overload strategy

A brake must not be assumed to be included unless it is explicitly confirmed in the selected configuration and quotation.

## Step 13: Plan Prototype Validation

Prototype testing should include representative:

- Payload and link geometry
- Continuous motion cycles
- Peak events
- Temperature monitoring
- Holding conditions
- Direction reversals
- Encoder behavior
- Controller current limits
- Communication behavior
- External loads
- Power-off and emergency-stop cases

Selection is complete only after the actuator is validated in the actual or representative mechanism.

## Requirement Checklist

Send the following information for engineering review:

| Category | Required information |
| --- | --- |
| Application | Robot type and joint position |
| Mechanics | Payload, link lengths, center of gravity and joint-angle range |
| Torque | Continuous torque, peak torque and peak duration |
| Motion | Rated speed, maximum speed, acceleration, deceleration and cycle time |
| Electrical | Voltage range, current limits and power source |
| Packaging | Maximum diameter, thickness, length and weight |
| External loads | Radial load, axial load and overturning moment |
| Precision | Backlash, accuracy, repeatability and resolution |
| Control | Encoder, driver, control mode and communication interface |
| Environment | Ambient temperature, cooling, contamination and duty cycle |
| Safety | Brake, holding and power-off behavior |
| Commercial | Prototype quantity and annual forecast |

## Related Application Guides

- [Humanoid robot joint actuators](../applications/humanoid-robot-joint-actuators.md)
- [Quadruped robot joint gearboxes](../applications/quadruped-robot-joint-gearboxes.md)
- [Robotic arm joint actuators](../applications/robotic-arm-joint-actuators.md)
- [Exoskeleton joint actuators](../applications/exoskeleton-joint-actuators.md)

## Request a Joint-Actuator Selection Review

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request CAD, Sample and Quote](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Robot Joint Requirements](../contact.md){ .md-button }

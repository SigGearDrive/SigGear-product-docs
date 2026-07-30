# Robotic Arm Joint Actuators and Gearboxes

> **Developing a robotic arm or collaborative robot?** [Open an engineering request](https://github.com/SigGearDrive/SigGear-product-docs/issues/new/choose) or email [wangwanrong@siggear.com](mailto:wangwanrong@siggear.com) with the payload, reach, axis position, torque, speed, backlash, size and quantity. Our engineers will reply within 24 hours.

## Application Overview

Robotic arms, collaborative robots, research manipulators and compact automation systems require reliable joint-drive solutions for base, shoulder, elbow, wrist and rotary-tool axes. A robot arm joint actuator or robot arm gearbox should be selected from the complete mechanism requirement, not from output torque alone.

Each axis has a different payload, reach, center of gravity, inertia, motion profile, duty cycle, positioning target, brake requirement and installation envelope. The correct actuator selection depends on the relationship between torque, speed, backlash, stiffness, thermal behavior, controller capability and mechanical interface.

SigGear supports robotic arm projects with integrated robot joint actuators, planetary joint actuators, cycloidal joint modules and compact planetary gearboxes. Depending on the selected configuration, the solution may be supplied as a complete motor-reducer-encoder-driver module or as a reducer or gearbox for customer-side motor and controller integration.

This page is intended for early-stage supplier comparison, model shortlisting and engineering communication. Final product selection, quotation and technical agreement require confirmation against the controlled drawing, selected ratio, duty cycle, mounting interface, motor configuration and ordered version.

## Key Selection Factors for Robot Arm Joints

| Requirement | Why it matters |
| --- | --- |
| Payload and reach | Determines gravity torque, inertia and the torque required at the base, shoulder and elbow axes. |
| Continuous torque | Must cover repeated motion, holding and process-load conditions within the required duty cycle. |
| Peak torque and peak duration | Important for acceleration, deceleration, collision recovery and short overload events. |
| Output speed and acceleration | Must match cycle time, path planning and production throughput targets. |
| Backlash and repeatability | Affect positioning accuracy, contouring quality, vibration and end-effector precision. |
| Radial, axial and overturning loads | Influence output bearing selection, housing stiffness and mounting-interface design. |
| Brake and holding mode | Critical for vertical axes, gravity-loaded arms and safe power-off behavior. |
| Encoder, driver and communication | Affect closed-loop control, software integration, wiring and diagnostic functions. |
| Thermal condition and duty cycle | Determine whether the selected actuator can work repeatedly without overheating. |

## Axis-by-Axis Review

### Base Axis

The base axis often carries the full arm structure, payload and tooling inertia. Important review items include overturning moment, output-bearing support, acceleration profile, cable routing, backlash and mounting stiffness. A robot arm base joint may need a larger safety margin than a wrist or tool axis.

### Shoulder Axis

The shoulder joint is usually one of the highest-load axes because it moves the upper arm and downstream payload. Continuous torque, peak torque, holding mode, brake requirement and thermal performance should be reviewed carefully. The center of gravity of the full arm link is important for calculation.

### Elbow Axis

The elbow axis often needs a balance between torque, speed, compact axial length and smooth positioning. For collaborative robots and light industrial arms, an integrated actuator may reduce prototype assembly time, but the final selection must still confirm duty cycle, backlash and repeated temperature rise.

### Wrist Axes

Wrist pitch, roll and yaw axes usually require compact size, low weight, smooth motion and good repeatability. Smaller integrated actuators or planetary gearbox solutions may be considered when the payload and external process forces are moderate.

### Rotary Tool Axis

A tool-rotation axis may prioritize speed, positioning, cable routing, compact output interfaces and integration with end effectors. Required radial load, axial load, shaft geometry and expected life should be defined before selecting the gearbox or actuator.

## Candidate SigGear Products

The following published SigGear models can be used as starting points for robotic arm actuator and gearbox selection. Final selection depends on the axis position, complete operating cycle, size limit, load condition and control architecture.

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver options depend on selected configuration. |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver. |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver options depend on selected configuration. |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver. |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver. |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and no integrated driver. |

For smaller axes, grippers, compact rotary tooling or customer-designed servo motor assemblies, SigGear can also evaluate [8–42 mm planetary gearbox](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md) options. These are useful when the customer needs a robot arm gearbox rather than a fully integrated actuator.

## Integrated Actuator or Separate Robot Arm Gearbox

A robotic arm project can use either an integrated actuator or a separate gearbox-and-motor architecture.

An integrated robot joint actuator may be suitable when the project needs a compact module with matched motor, reducer, encoder and driver options. This can simplify prototype assembly and reduce early-stage integration risk.

A separate robot arm gearbox may be suitable when the engineering team already has a servo motor, BLDC motor, controller, brake, encoder or custom housing. In that case, the gearbox input shaft, mounting pattern, ratio, speed limit, thermal condition and output interface must be reviewed carefully.

Neither architecture is automatically better. The right choice depends on the axis load, packaging, control system, supply-chain strategy, prototype schedule and production quantity.

## Planetary Gearbox or Cycloidal Joint Module

A planetary joint actuator or servo planetary gearbox may be considered when compact integration, output speed, motor matching flexibility and broad configuration options are important.

A cycloidal robot joint module may be considered when the selected model's torque, speed, backlash, installation structure and duty-cycle capability match the robotic-axis requirement.

The decision should not be based on a general rule. Compare the full torque-speed cycle, payload inertia, external loads, backlash target, stiffness, thermal condition, size, weight, brake requirement and control architecture.

## Backlash, Stiffness and Positioning Accuracy

Robot arm accuracy is not determined by the reducer alone. Backlash, structural stiffness, bearing arrangement, encoder position, controller tuning, arm-link rigidity and assembly tolerances all influence final positioning and repeatability.

When discussing a robotic arm gearbox or actuator, provide the required positioning accuracy and repeatability at the end effector, not only at the motor or reducer. This helps determine whether the selected gearbox, encoder and mechanical structure are suitable.

## Brake, Safety and Holding Requirements

For vertical or gravity-loaded robot arm axes, specify the required holding condition and power-off behavior. A brake may be needed for safety or position retention, but it should not be assumed to be included unless it is confirmed in the selected configuration, drawing and quotation.

Important questions include:

- Does the axis need to hold position when power is off?
- Is the brake used for safety, parking or emergency stop support?
- What payload and arm posture must be held?
- Is backdrivability required or prohibited?
- Is a mechanical stop, counterbalance or external brake also used?

## Encoder, Driver and Communication Review

Robotic arm teams should confirm the control system early. Important questions include:

- Is the actuator controlled by position, speed, torque or mixed control mode?
- Is the driver integrated into the actuator or placed in the robot controller cabinet?
- Is CAN, RS485, PWM or another interface required?
- Is EtherCAT or another fieldbus handled by the customer controller?
- What encoder resolution, absolute-position requirement and homing method are needed?
- Are current limit, temperature feedback, fault reporting or brake control required?

Communication and control functions vary by selected model and electronics configuration. Do not promise CAN, RS485, EtherCAT, PID, torque control or a specific protocol until the driver and firmware version are confirmed.

## Thermal and Duty-Cycle Validation

A robot arm actuator must be checked against the actual motion cycle. Useful information includes:

- Rated and maximum speed
- Acceleration and deceleration profile
- Continuous torque during motion or holding
- Peak torque and peak duration
- Cycle time and rest time
- Ambient temperature and cooling method
- Mounting structure and heat-dissipation path
- Expected daily operating hours

Peak torque is not a continuous working rating. A drive that can provide short overload torque may still be unsuitable if repeated motion causes excessive temperature rise.

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Brake integration after engineering review
- Communication and control configuration
- Customer branding and labeling
- Prototype support before production planning

Customization availability depends on technical feasibility, prototype quantity, expected annual volume and the level of engineering change required.

## Information Needed for a Robotic Arm Joint Selection Review

Please send one requirement set for each axis. Base, shoulder, elbow, wrist and tool axes should be reviewed separately.

Provide:

- Robot type and target application
- Axis position and motion direction
- Payload, arm reach and center of gravity
- Continuous torque
- Peak torque and peak duration
- Required output speed, acceleration and deceleration
- Operating voltage and current limit
- Maximum outer diameter, thickness and weight
- Radial load, axial load and overturning moment
- Backlash, positioning and repeatability targets
- Brake and power-off holding requirement
- Encoder, driver and communication requirements
- Duty cycle, ambient temperature and cooling method
- Prototype quantity and estimated annual quantity
- Preferred architecture: integrated actuator or separate gearbox and motor

## Request a Robotic Arm Joint Selection Review

Send your robotic arm joint or gearbox requirements to SigGear for a preliminary model review. Early requirements can be approximate, but payload, reach, torque, speed, size, voltage and quantity are needed before a meaningful recommendation can be made.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Open an Engineering Request](https://github.com/SigGearDrive/SigGear-product-docs/issues/new/choose){ .md-button .md-button--primary }
[Send Robotic Arm Requirements](../contact.md){ .md-button }
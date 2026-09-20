---
title: Exoskeleton Joint Actuators and Gearboxes | Selection Guide | SigGear
description: Select exoskeleton joint actuators and gearboxes by assistance torque, speed, size, weight, backdrivability, brake, thermal limits and human-interaction requirements.
---

# Exoskeleton Joint Actuators and Gearboxes

## Application Overview

Powered exoskeletons, rehabilitation robots, wearable assistive devices and industrial support systems require compact joint-drive systems for hip, knee, ankle, shoulder, elbow and other assisted-motion axes. Each joint has a different human-interaction profile, range of motion, torque-speed cycle, installation envelope and safety requirement, so an exoskeleton joint actuator should be selected from the complete wearable system rather than torque alone.

SigGear supplies planetary and cycloidal joint-drive products that can be evaluated for exoskeleton prototypes, rehabilitation equipment and wearable-assistance mechanisms. Depending on the selected model and configuration, a solution may combine a BLDC motor, precision reducer, encoder and driver, or it may be supplied as a separate gearbox or joint module for customer-side integration.

This page is intended for early-stage supplier comparison, model shortlisting and engineering communication. Final actuator selection, quotation and technical agreement require confirmation against the controlled drawing, selected ratio, duty cycle, mounting interface, power-off behavior, human-interaction requirement and ordered version.

## Key Selection Factors for Exoskeleton Joints

| Requirement | Why it matters |
| --- | --- |
| Joint position | Hip, knee, ankle, shoulder and elbow joints have different torque, speed, range and safety requirements. |
| Assistance mode | Walking support, sit-to-stand, lifting assistance and rehabilitation training create different torque-speed cycles. |
| Continuous torque | Must support repeated assistance without excessive temperature rise. |
| Peak torque and peak duration | Important for gait transitions, lifting support, recovery movement and short overload events. |
| Weight and wearable packaging | Joint mass, thickness and cable routing affect comfort, balance and usability. |
| Backdrivability and compliance | Human interaction may require controlled mechanical response, safe movement and low resistance. |
| Holding and brake behavior | Gravity-loaded joints may require power-off holding, controlled release or brake integration. |
| Radial, axial and overturning loads | Wearable frames and misalignment can introduce loads beyond output torque. |
| Encoder, driver and communication | Affect closed-loop control, sensing, software integration and safety limits. |
| Thermal, acoustic and duty-cycle conditions | Determine whether the actuator can operate repeatedly in a wearable environment. |
| System-level validation | A component does not establish completed exoskeleton safety or regulatory compliance. |

## Common Exoskeleton and Wearable-Robot Use Cases

### Rehabilitation Exoskeletons

Rehabilitation exoskeletons may require smooth assisted motion, repeatable joint trajectories, controllable speed and defined safety limits. Provide the assisted joint, range of motion, target therapy motion, continuous torque, peak torque, movement speed, patient interaction mode and required sensing or control functions.

### Walking Assistance and Mobility Support

Lower-limb walking assistance often involves hip, knee and ankle motion with repeated gait cycles. Important review items include gait frequency, walking speed, user mass range, joint angle range, torque-speed profile, duty cycle, battery voltage, thermal behavior and power-off safety behavior.

### Industrial Exoskeletons

Industrial exoskeletons may assist lifting, overhead work, crouching, standing or tool support. These systems often prioritize weight, durability, repeated duty cycle, user comfort, simple maintenance and robust power-off behavior. Provide the working posture, assisted load, motion cycle, expected daily use and environmental condition.

### Upper-Limb and Shoulder Assistance

Shoulder, elbow and wrist assistance axes can have strict packaging and weight limits. Cable routing, center of gravity, external load, joint alignment and user comfort should be reviewed together with torque and speed.

### Research and Prototype Wearable Robots

Research platforms may need flexible actuator configurations, custom control interfaces, encoder feedback, experimental torque-speed settings and fast prototype iteration. Communication protocol, driver configuration, mechanical interface and safety interlocks should be confirmed before ordering.

## Joint-by-Joint Evaluation

Prepare a separate requirement set for every joint position. Do not apply one actuator specification to the whole exoskeleton.

| Joint position | Main review focus |
| --- | --- |
| Hip | Body support, gait assistance, sit-to-stand motion, mounting stiffness, user comfort and peak torque. |
| Knee | Walking cycle, crouching or standing support, impact during gait, brake or holding requirement and thermal behavior. |
| Ankle | Compact packaging, foot clearance, shock load, backdrivability, stiffness and low-profile integration. |
| Shoulder | Wide range of motion, cable routing, user comfort, gravity compensation and low weight. |
| Elbow | Repeated flexion-extension motion, holding behavior, output speed, control response and human interaction. |
| Wrist or auxiliary axis | Compact size, low mass, precision motion, cable routing and lower torque requirements. |

## Assistance Torque and Motion Profile

Provide the required continuous assistance torque, peak torque, peak duration, joint speed, acceleration and complete motion cycle. Walking assistance, lifting support, rehabilitation training, static holding and power-off support create different operating conditions.

Useful information includes:

- Assisted joint and axis definition
- User mass range or payload condition
- Continuous torque during normal motion
- Peak torque and allowed duration
- Joint speed and acceleration
- Range of motion
- Gait frequency or work cycle
- Holding time and rest time
- Emergency or abnormal-load condition

Peak torque should not be treated as a continuous working rating.

## Size, Weight and Wearable Packaging

Specify the maximum outer diameter, axial thickness and mass for every joint position. Bearings, mounting brackets, covers, cables, connectors, sensors and human-interface structures must be included in the available envelope.

Important packaging details include:

- Maximum actuator diameter and thickness
- Maximum allowable joint weight
- Cable exit direction and connector location
- Available mounting structure
- User comfort and clearance constraints
- Whether external bearings support the joint load
- Battery and controller placement
- Protection cover or enclosure design

In wearable systems, a technically capable actuator may still be unsuitable if it is too heavy, too thick or difficult to integrate safely around the user.

## Backdrivability, Compliance and Human Interaction

Human-interactive systems often require controlled mechanical response. State whether the joint must be manually movable, highly backdrivable, softly compliant, self-locking, brake-held or actively controlled at all times.

Confirm:

- Whether manual movement without power is required
- Whether low resistance is required during passive motion
- Whether a brake or holding mode is required
- Whether the user can safely move the joint if power is lost
- Whether compliance comes from mechanics, control or external elastic elements
- Whether torque sensing or current-based force estimation is used

Backdrivability cannot be assumed from gearbox type alone. It depends on motor selection, ratio, friction, controller behavior, load, mechanism geometry and safety strategy.

## Holding, Brake and Power-Off Requirements

For gravity-loaded joints, specify the required holding mode, acceptable motion after power loss and brake requirement. A brake or self-holding function must not be assumed unless it is confirmed in the selected configuration and quotation.

Provide:

- Required holding torque
- Maximum allowed drift or motion after power loss
- Whether fail-safe brake behavior is required
- Whether controlled release is required
- Whether the joint must support standing or lifting loads while unpowered
- Whether manual override is required

Brake selection and power-off behavior must be evaluated together with the completed exoskeleton safety concept.

## External Loads, Joint Alignment and Structure

Radial load, axial load, overturning moment and misalignment can be introduced by the wearable frame and the user's motion. These loads must be reviewed separately from actuator output torque.

Important details include:

- Joint-frame geometry
- Load direction and distance from bearing support
- User-limb alignment tolerance
- Straps, braces and linkage structure
- External bearings or support brackets
- Shock or impact events
- Mechanical stops and limit structures

A joint actuator may meet torque and speed requirements but still require external bearing support if the wearable frame applies large radial, axial or overturning loads.

## Candidate SigGear Products

The following published models can be used as starting points for exoskeleton joint actuator and wearable robot gearbox evaluation. Final selection depends on joint position, torque-speed cycle, weight limit, power-off behavior, control architecture and safety validation plan.

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver options depend on selected configuration. |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver. |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver options depend on selected configuration. |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver. |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver. |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and no integrated driver. |

For lower-load auxiliary axes, compact mechanisms or customer-designed motor assemblies, SigGear can also evaluate [8–42 mm planetary gearbox](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md) options when the project requires a separate reducer or compact gearbox.

## Integrated Joint Actuator or Separate Gearbox

An integrated joint actuator may be suitable when the project needs a compact matched module with motor, reducer, encoder and driver options. This can simplify early prototype assembly and reduce integration time.

A separate gearbox or joint reducer may be suitable when the exoskeleton team already has its own motor, controller, encoder, brake, frame, external bearing or safety architecture. In that case, the input interface, output interface, bearing arrangement, ratio, speed limit, heat path and mechanical stops must be confirmed carefully.

The best architecture depends on wearable packaging, control architecture, safety concept, prototype schedule, serviceability and production quantity.

## Planetary or Cycloidal Joint Drive

A planetary joint actuator may be considered when compact integration, output speed, motor matching flexibility and broader configuration options are important.

A cycloidal joint module may be considered when the selected model's torque, speed, backlash, installation structure and duty-cycle capability match the wearable-joint requirement.

Neither transmission type should be selected from a general rule alone. Compare the complete torque-speed cycle, weight, external loads, mechanical response, thermal conditions, packaging and control architecture.

## Encoder, Driver and Communication Review

Encoder, driver and communication functions vary by model and configuration. Confirm the required position, velocity and torque-control functions, as well as CAN, RS485, PWM, EtherCAT or another project-specific interface when applicable.

Clarify:

- Is the driver integrated or customer-side?
- Is position, speed, current or torque control required?
- Is motor-side or output-side position feedback required?
- What encoder resolution and zero-position behavior are needed?
- Is fault reporting, temperature feedback or current limiting required?
- What communication interface and protocol are required?
- Is controller firmware customization required?

Do not assume CAN, RS485, EtherCAT, PID, torque control or a specific protocol until the electronics configuration and firmware version are confirmed.

## Thermal, Acoustic and Duty-Cycle Conditions

Provide operating time, rest time, ambient temperature, cooling method, installation structure and any acoustic target. Noise, thermal performance and service life must be confirmed for the selected configuration and test condition; they must not be inferred from a general product-family statement.

Useful information includes:

- Repeated motion cycle
- Holding time and rest time
- Peak torque frequency
- Ambient temperature
- Enclosed or ventilated installation
- Heat path through the wearable frame
- Expected daily use time
- Acoustic target for user-facing operation

A wearable actuator that meets short-duration torque requirements may still be unsuitable if repeated human-assist cycles create excessive heat or noise.

## Safety, Compliance and Validation Boundary

The complete exoskeleton system requires project-specific risk assessment, control limits, mechanical stops, emergency behavior and validation. A component page does not establish medical-device approval, rehabilitation-equipment approval or system-level safety compliance.

The equipment manufacturer is responsible for completed-system requirements, including applicable risk management, mechanical and electrical safety, software and control validation, EMC, battery safety, human factors, labeling and regulatory approval.

Component documentation is supplied according to the selected model and agreed project scope. Do not infer medical-device certification, wearable-system certification or functional-safety approval from a general motor or gearbox product page.

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Brake integration after engineering review
- Communication and control configuration
- Low-weight integration review
- Customer branding and labeling
- Prototype support before production planning

Customization availability depends on technical feasibility, prototype quantity, expected annual volume and the level of engineering change required.

## Information Needed for an Exoskeleton Joint Selection Review

Please send one requirement set for each joint position. Hip, knee, ankle, shoulder, elbow and auxiliary axes should be reviewed separately.

Provide:

- Exoskeleton type and target application
- Joint position and axis definition
- User mass range or assisted payload
- Assistance mode: walking, lifting, rehabilitation, holding or other
- Continuous torque
- Peak torque and peak duration
- Output speed and acceleration
- Range of motion and motion cycle
- Operating voltage and current limit
- Maximum diameter, thickness and weight
- Radial load, axial load and overturning moment
- Backdrivability, compliance or holding requirement
- Power-off behavior and brake requirement
- Encoder, driver and communication requirements
- Duty cycle, ambient condition and acoustic target
- Safety validation boundary and mechanical stops
- Prototype quantity and estimated annual quantity
- Preferred architecture: integrated actuator or separate gearbox and motor

## Request an Exoskeleton Joint Selection Review

Send your exoskeleton or wearable robot joint requirements to SigGear for preliminary model evaluation. Early requirements can be approximate, but joint position, user load, torque, speed, range of motion, size, weight, power-off behavior, control interface and quantity are needed before a meaningful recommendation can be made.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Send Exoskeleton Joint Requirements](../contact.md){ .md-button .md-button--primary }

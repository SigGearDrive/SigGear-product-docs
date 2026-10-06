---
title: Custom Robot Joint Actuator Manufacturer & Engineering | SigGear
description: Custom robot joint actuator engineering and manufacturing for humanoid, quadruped, robot arm and exoskeleton projects using planetary or cycloidal transmissions.
---

# Custom Robot Joint Actuator Development

## Start From the Joint Requirement, Not From an Existing Actuator Model

A robotics project does not need to fit an existing SigGear actuator exactly.

You may already know the joint torque, speed and installation envelope. You may also have only a robot mechanism, link geometry, motor preference, CAD concept or early prototype.

SigGear develops and manufactures robot joint actuators, planetary actuator platforms and cycloidal joint modules for robotics and compact motion systems.

SigGear can review the joint as a system and evaluate the actuator gearbox or reducer, motor, sensing, driver and mechanical interfaces together.

Depending on the project, the engineering path may start from:

- an existing SigGear planetary actuator
- an existing SigGear cycloidal joint module
- a gearbox-centered solution for the customer's own motor and controller
- a motor + gearbox combination
- a modified mechanical interface
- a new compact actuator configuration based on the application requirements

[Send Your Joint Requirement](mailto:wangwanrong@siggear.com?subject=Robot%20Joint%20and%20Compact%20Actuator%20Engineering%20Review){ .md-button .md-button--primary }
[Humanoid and Bipedal Robot Joint Engineering](../applications/humanoid-robot-joint-actuators.md){ .md-button }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button }

## What Can SigGear Supply?

Depending on the project and engineering feasibility, the supply scope may include:

- gearbox / reducer only
- motor + gearbox assembly
- planetary robot joint actuator
- cycloidal joint module
- actuator with encoder
- actuator with driver where applicable
- modified mechanical interface
- project-specific joint configuration

The exact configuration depends on torque, speed, packaging, motor, sensing, controller and mechanical-interface requirements.

## Project-Specific and OEM Development

For OEM or project-specific robot joint programs, the engineering review can begin from an existing SigGear actuator platform, the customer's motor/controller architecture, or a new mechanical requirement. Final feasibility depends on the complete torque-speed requirement, packaging, interfaces, electronics configuration and production plan.

## What the Engineering Review Starts With

A meaningful robot-joint review normally needs the axis requirement rather than one isolated torque number.

Useful inputs include:

- robot type and joint position
- payload and moving-link mass
- link length and center-of-gravity location
- continuous torque
- peak torque and peak duration
- output speed and motion cycle
- maximum diameter, thickness, length and weight
- radial / axial load and overturning load where relevant
- operating voltage and controller current limits
- encoder and feedback requirement
- driver and control mode
- communication interface
- power-off behavior and brake requirement
- prototype quantity and expected production volume

If some of these are not known yet, send the mechanism, CAD, sketch or the information already available. The engineering review can identify what needs to be calculated, measured or tested before the actuator architecture is fixed.

## Planetary, Cycloidal or Another Joint Architecture?

SigGear publishes both planetary robot joint actuators and cycloidal joint modules.

Neither structure should be selected from a general rule alone.

The choice needs to consider:

- torque-speed requirement
- installation diameter and axial thickness
- motor speed and motor size
- ratio
- efficiency
- backlash
- external loads
- thermal condition
- noise target
- backdrivability or holding requirement
- encoder / driver architecture
- prototype and production constraints

For a project where the transmission structure has not been decided, send the operating requirement first.

[Custom Planetary Gearbox Engineering](custom-planetary-gearbox.md){ .md-button }
[Custom Cycloidal Transmission Engineering](custom-cycloidal-transmission.md){ .md-button }

## Existing Planetary Joint Reference Platforms

SigGear currently publishes three integrated planetary robot joint actuator reference models:

| Reference model | Transmission | Published rated torque | Published peak torque | Published rated output speed |
| --- | --- | ---: | ---: | ---: |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm |

These products are **reference platforms**, not the only joint configurations SigGear can evaluate.

A new project may require a different:

- reduction ratio
- torque-speed balance
- motor
- outer diameter or axial thickness
- output interface
- housing or mounting structure
- encoder
- driver
- communication arrangement
- cable or connector configuration

Any change must be reviewed as a complete configuration.

## Existing Cycloidal Joint Reference Platforms

SigGear also publishes cycloidal joint-module references:

| Reference model | Transmission | Published rated torque | Published peak torque | Published rated output speed |
| --- | --- | ---: | ---: | ---: |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm |

The published values belong to the listed products only and must not be transferred to a different motor, ratio, diameter or custom configuration without engineering confirmation.

## SG-6010C as a Public Engineering Reference

SG-6010C currently has the most complete public Engineering Pack among the planetary joint actuators.

Public resources include:

- technical datasheet
- mechanical-interface reference
- simplified STEP model

[View SG-6010C](../products/robot-joint-actuators/sg6010c.md){ .md-button .md-button--primary }
[View SG-6010C Datasheet](../engineering-resources/sg6010c/datasheet.md){ .md-button }
[View SG-6010C Mechanical Interface](../engineering-resources/sg6010c/mechanical-interface.md){ .md-button }

Its public product documentation also describes driver-equipped configurations with CAN, USB Type-C, position / velocity / torque control and encoder support. These functions are configuration-dependent and must be confirmed for the quoted hardware and firmware.

## CPM-80-25 as a Public Cycloidal Reference

For cycloidal joint evaluation, CPM-80-25 has a public Engineering Pack including:

- technical datasheet
- mechanical-interface reference
- simplified STEP models
- measured performance data

[View CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md){ .md-button .md-button--primary }
[View CPM-80-25 Measured Performance Data](../engineering-resources/cpm80-25/performance-test-data.md){ .md-button }

Measured test points are engineering evidence for the released configuration and are not universal continuous ratings for a custom joint.

## What Can Be Reviewed in a Custom Joint Project

Depending on the reference platform and project feasibility, the review may include:

| Engineering area | Examples |
| --- | --- |
| Transmission | planetary or cycloidal structure, ratio and gearbox architecture |
| Motor | motor type, speed, power, torque constant and mechanical interface where applicable |
| Packaging | outer diameter, axial thickness, housing and total joint envelope |
| Output | flange, shaft, locating feature and robot-side mounting interface |
| Feedback | Hall / encoder arrangement supported by the selected configuration |
| Driver | integrated or external driver architecture |
| Control | position, velocity or torque control where supported by the selected driver |
| Communication | CAN, RS485 or other supported project-specific interface |
| Safety | brake, power-off behavior and mechanical stops where required |
| Mechanical load | radial, axial and overturning load review |
| Integration | cables, connectors, housing and assembly arrangement |

Not every item can be changed independently. A change to motor, ratio, size, driver or interface may affect torque, speed, thermal behavior, weight, efficiency, life, control limits and cost.

## If You Do Not Know the Required Joint Torque

A robot team can still start the discussion before the torque value is finalized.

Useful inputs include:

- supported mass
- link mass
- payload
- link length
- center-of-gravity location
- acceleration target
- external force
- joint angle range
- motion cycle
- whether the axis works against gravity

For a first single-axis screening, gravity, acceleration and external-force torque can be estimated before the actuator is shortlisted.

[Open the Robot Joint Actuator Selection Guide](../selection-guides/robot-joint-actuator-selection-guide.md){ .md-button .md-button--primary }

## If You Have a Motor or Controller Already

Some robotics teams already have a preferred motor, driver or control stack.

In that case, send the available:

- motor drawing and shaft details
- motor speed / voltage / power data
- controller current limits
- encoder requirement
- communication requirement
- available installation space
- required output torque and speed

SigGear can then evaluate whether the project should use a gearbox-centered joint solution, a motor + gearbox assembly or another integrated actuator approach.

[Motor + Gearbox Integration Engineering](motor-gearbox-integration.md){ .md-button }
[Prototype → Design-In → Production](prototype-to-production.md){ .md-button }
[Open the Engineering Center](../engineering-center/index.md){ .md-button }

## Robot and AI Hardware Applications

Custom joint and compact actuator development may be relevant for:

- humanoid robots
- quadruped robots
- robotic arms
- exoskeletons
- rehabilitation robots
- service robots
- compact rotary automation axes
- AI-enabled hardware products that require compact controlled motion

For smaller mechanisms such as dexterous hands, grippers and compact end effectors, a micro planetary gearbox or gear-motor architecture may be more appropriate than the larger published joint modules.

[Browse Micro Gear Motors](../products/micro-gear-motors/index.md){ .md-button }
[Robot Gripper and Dexterous-Hand Applications](../applications/robot-gripper-gear-motors.md){ .md-button }

These are application areas where SigGear transmission products and engineering review may be relevant. They are not claims that SigGear has a public production case in every listed application.

## Engineering Development Path

A custom robot-joint project may move through:

**Joint Requirement / Robot CAD / Existing Prototype**  
→ **Torque and Motion Review**  
→ **Transmission Architecture Review**  
→ **Motor / Encoder / Driver Review**  
→ **Mechanical Interface and Packaging Review**  
→ **Configuration Drawing**  
→ **Prototype / Sample**  
→ **Representative Joint Test**  
→ **Parameter / Interface Refinement**  
→ **Design Confirmation**  
→ **Pilot Preparation**  
→ **Production**

The exact path depends on how much of the robot architecture is already fixed.

## What to Send First

You do not need to prepare a complete joint specification before contacting SigGear.

For a first review, send what you already have:

1. robot type and joint position
2. link / load information
3. target torque if known
4. target speed
5. maximum joint diameter and thickness
6. operating voltage
7. motor / controller preference if already selected
8. encoder / communication requirement if already defined
9. drawing, CAD screenshot or mechanism sketch
10. prototype quantity and expected production volume if known

If several values are still unknown, the project can start from the robot mechanism and design intent.

## Confidential Robotics Projects

Robot and AI-hardware development often involves unreleased mechanisms, customer CAD and project-specific actuator architecture.

Those projects may be covered by confidentiality agreements and cannot be shown publicly.

SigGear therefore uses public actuator platforms, gearbox platforms, CAD resources, mechanical interfaces and test data to demonstrate real engineering capability without exposing confidential customer designs.

## Discuss Your Robot Joint Project

Send the joint requirement, robot CAD, mechanism, motor or the information you already have.

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Your Joint Requirement](mailto:wangwanrong@siggear.com?subject=Robot%20Joint%20and%20Compact%20Actuator%20Engineering%20Review){ .md-button }

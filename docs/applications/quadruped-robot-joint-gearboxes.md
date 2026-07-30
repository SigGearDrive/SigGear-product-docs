# Quadruped Robot Joint Gearboxes and Actuators

> **Developing a quadruped robot?** [Open an engineering request](https://github.com/SigGearDrive/SigGear-product-docs/issues/new/choose) or email [wangwanrong@siggear.com](mailto:wangwanrong@siggear.com) with the robot mass, joint position, torque, speed, gait cycle, impact condition, size and quantity. Our engineers will reply within 24 hours.

## Application Overview

Quadruped robots require compact and durable joint-drive systems for hip, knee, ankle and auxiliary leg axes. Walking, trotting, turning, stair climbing, slope operation, jumping, landing and recovery motions create different torque-speed and impact-load conditions. A quadruped robot actuator or leg joint gearbox should therefore be selected from the complete gait profile, not from a single peak-torque value.

SigGear supports quadruped robot development with integrated robot joint actuators, planetary joint actuators, cycloidal joint modules and compact planetary gearbox solutions. Depending on the selected configuration, the solution may combine a motor, reducer, encoder and driver, or it may be supplied as a reducer or gearbox for customer-side motor and controller integration.

This page is intended for early-stage supplier comparison, model shortlisting and engineering communication. Final actuator selection, quotation and technical agreement require confirmation against the controlled drawing, selected ratio, duty cycle, mounting interface, impact condition, motor configuration and ordered version.

## Key Selection Factors for Quadruped Robot Joints

| Requirement | Why it matters |
| --- | --- |
| Robot mass and payload | Determines standing load, walking load and impact energy during landing or recovery. |
| Joint position | Hip, knee and ankle joints have different torque, speed, impact and packaging requirements. |
| Continuous torque | Must cover standing, walking and repeated gait cycles without excessive temperature rise. |
| Peak torque and peak duration | Important for acceleration, jumping, impact recovery and short overload events. |
| Output speed and acceleration | Must match gait frequency, stride length, foot trajectory and recovery motion. |
| Backlash and mechanical response | Affect foot placement, balance, compliance, motion smoothness and control stability. |
| Radial, axial and overturning loads | Influence output bearing, housing stiffness and leg-link structure. |
| Shock and impact loads | Critical for landing, obstacle crossing, sudden stops and repeated gait impact. |
| Encoder, driver and communication | Affect closed-loop control, wiring, software integration and diagnostic functions. |
| Thermal condition and duty cycle | Determine whether torque values are usable repeatedly or only for short periods. |

## Joint-by-Joint Review

### Hip Joint

The hip joint usually experiences high structural load because it connects the leg to the robot body and supports body mass, payload and dynamic gait forces. Important review items include continuous torque during standing, peak torque during acceleration, overturning moment, radial load, axial load, mounting stiffness and cable routing.

### Knee Joint

The knee joint is strongly affected by walking, trotting, squatting, jumping and recovery cycles. It may require high peak torque and repeated acceleration while remaining compact and lightweight. Thermal behavior, duty cycle, backlash and impact resistance should be reviewed carefully.

### Ankle Joint

The ankle joint is often sensitive to impact load, backlash, mechanical compliance and packaging. Foot contact, slope operation, landing and uneven-ground walking can create repeated shock loads. The output bearing structure, sealing, cable route and mechanical stops should be discussed during prototype review.

### Auxiliary Leg or Steering Axis

Some quadruped platforms include auxiliary rotary axes, steering structures, sensor-adjustment mechanisms or compact leg-link mechanisms. Smaller integrated actuators or planetary gearboxes may be suitable when torque and impact loads are lower than the main hip or knee joints.

## Gait Profile and Torque-Speed Cycle

For quadruped actuator selection, the complete gait profile is more useful than a single torque number. Provide operating cases such as:

- Standing and holding posture
- Walking on flat ground
- Trotting or fast walking
- Turning and lateral motion
- Starting and stopping
- Slope climbing and descending
- Obstacle crossing
- Jumping, landing or recovery motion
- Maximum payload condition

For each case, define continuous torque, peak torque, peak duration, output speed, acceleration, duty cycle and expected test time. Peak torque should not be treated as a continuous working rating.

## Impact Load and Structural Review

Quadruped robot joints can experience repeated impact and shock. These loads are different from output torque and should be evaluated separately.

Important information includes:

- Robot mass and payload
- Leg length and joint layout
- Foot contact condition
- Maximum landing or recovery event
- Ground surface and obstacle condition
- Radial load, axial load and overturning moment at the joint
- Mechanical stop or compliance design
- Whether external bearings support the joint load

A gearbox or actuator that meets torque and speed requirements may still be unsuitable if the bearing, housing or output interface cannot support the real impact condition.

## Candidate SigGear Products

The following published SigGear models can be used as starting points for quadruped robot actuator and leg joint gearbox evaluation. Final selection depends on the joint position, robot mass, gait cycle, impact condition, size limit and control architecture.

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver options depend on selected configuration. |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver. |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver options depend on selected configuration. |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver. |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver. |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and no integrated driver. |

For small auxiliary mechanisms, sensor modules, compact ankle mechanisms or customer-designed motor assemblies, SigGear can also evaluate [8–42 mm planetary gearbox](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md) options when the application requires a separate reducer or compact gearbox.

## Integrated Actuator or Separate Gearbox and Motor

A quadruped robot project can use an integrated actuator or a separate gearbox-and-motor architecture.

An integrated robot joint actuator may be suitable when the team wants a compact module with matched motor, reducer, encoder and driver options. This can reduce prototype assembly work and speed up early gait testing.

A separate leg joint gearbox may be suitable when the robot team already has its own motor, controller, encoder, brake, housing, external bearing or leg-link structure. In that case, the input shaft, mounting interface, output shaft, ratio, speed limit, bearing arrangement and heat-dissipation path must be confirmed carefully.

The best architecture depends on robot mass, leg layout, required torque-speed cycle, impact condition, serviceability, prototype schedule and production quantity.

## Planetary or Cycloidal Drive for Quadruped Robots

A planetary joint actuator may be considered when the project prioritizes compact integration, output speed, motor matching flexibility and broad configuration options.

A cycloidal joint module may be considered when the selected model's torque, speed, backlash, installation structure and duty-cycle capability match the leg-joint requirement.

Neither transmission type should be selected from a general rule alone. Compare the full torque-speed cycle, impact load, backlash target, stiffness, thermal condition, size, weight, control architecture and prototype validation plan.

## Control, Encoder and Communication Review

Quadruped robots often require responsive closed-loop control. Before selecting a joint actuator, confirm:

- Is the joint controlled by position, speed, torque or mixed control mode?
- Is the driver integrated into the actuator or placed on a robot controller board?
- Is CAN, RS485, PWM, EtherCAT or another interface required?
- What encoder resolution and absolute-position behavior are needed?
- Is current limiting, temperature feedback or fault reporting required?
- Does the robot need power-off holding, brake control or controlled backdrivability?

Communication and control functions vary by selected product and electronics configuration. Do not assume CAN, RS485, EtherCAT, PID, torque control or a specific protocol until the driver and firmware version are confirmed.

## Thermal and Duty-Cycle Validation

Quadruped joints can produce repeated heat because gait cycles often involve frequent acceleration, deceleration, impact recovery and holding. Provide the real operating cycle instead of only maximum torque and speed.

Useful information includes:

- Continuous torque during standing or walking
- Peak torque and peak duration
- Output speed and acceleration
- Gait cycle and duty cycle
- Operating time and rest time
- Ambient temperature and cooling method
- Mounting structure and heat-dissipation path
- Expected daily operating hours and service-life target

Peak torque is not a continuous working rating. A joint that can provide short overload torque may still be unsuitable if repeated gait cycles cause excessive temperature rise.

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Communication and control configuration
- Brake or holding requirements after engineering review
- Customer branding and labeling
- Prototype support before production planning

Customization availability depends on technical feasibility, prototype quantity, expected annual volume and the level of engineering change required.

## Information Needed for a Quadruped Joint Selection Review

Please send one requirement set for each joint position. Hip, knee, ankle and auxiliary axes should be reviewed separately.

Provide:

- Robot type and target application
- Robot mass and maximum payload
- Joint position and axis definition
- Leg length and mechanical layout
- Continuous torque
- Peak torque and peak duration
- Required output speed and acceleration
- Gait profile and duty cycle
- Operating voltage and current limit
- Maximum outer diameter, thickness and weight
- Radial load, axial load and overturning moment
- Shock, landing or obstacle-crossing condition
- Backlash and positioning requirement
- Encoder, driver and communication requirements
- Ambient temperature and cooling method
- Prototype quantity and estimated annual quantity
- Preferred architecture: integrated actuator or separate gearbox and motor

## Request a Quadruped Joint Selection Review

Send your quadruped robot joint requirements to SigGear for a preliminary model review. Early requirements can be approximate, but robot mass, joint position, torque, speed, gait cycle, impact condition, voltage and quantity are needed before a meaningful recommendation can be made.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Open an Engineering Request](https://github.com/SigGearDrive/SigGear-product-docs/issues/new/choose){ .md-button .md-button--primary }
[Send Quadruped Joint Requirements](../contact.md){ .md-button }
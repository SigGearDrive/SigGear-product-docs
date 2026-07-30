# AGV and AMR Wheel Drive Gearboxes and Motors

> **Developing an AGV, AMR or mobile robot?** [Open an engineering request](https://github.com/SigGearDrive/SigGear-product-docs/issues/new/choose) or email [wangwanrong@siggear.com](mailto:wangwanrong@siggear.com) with the vehicle mass, payload, wheel diameter, speed, slope, voltage, braking requirements and quantity. Our engineers will reply within 24 hours.

## Application Overview

AGVs, AMRs, warehouse mobile robots, inspection robots and compact transport platforms require wheel-drive systems matched to vehicle mass, payload, wheel diameter, target speed, acceleration, slope requirement, floor condition and duty cycle. An AGV wheel drive motor or AMR wheel drive gearbox should be selected from the complete traction requirement, not from rated torque alone.

SigGear supplies compact hub gear motors and planetary transmission products that can be evaluated for mobile-robot wheel drives. The standard SG-2877 and SG-2878 catalog configurations combine a BLDC motor, planetary reduction mechanism and Hall sensors. An external controller is required unless a controller is specifically included in the quotation.

This page is intended for early-stage supplier comparison, wheel-drive model shortlisting and engineering communication. Final selection, quotation and technical agreement require confirmation against the controlled drawing, selected configuration, wheel interface, controller, duty cycle and vehicle operating condition.

## Key Selection Factors for AGV and AMR Wheel Drives

| Requirement | Why it matters |
| --- | --- |
| Vehicle mass and payload | Determines the drive force required for acceleration, turning, slope climbing and stopping. |
| Wheel diameter | Converts wheel torque and speed into vehicle tractive force and travel speed. |
| Number of driven wheels | Determines torque per wheel and affects traction, redundancy and vehicle layout. |
| Target speed and acceleration | Controls motor speed, torque demand, controller current and heat generation. |
| Slope and ramp requirement | Often creates the highest continuous or peak torque condition for mobile robots. |
| Floor and traction condition | Rolling resistance and available grip depend on floor material, wheel material and contamination. |
| Braking and holding | Important for stopping distance, parking, slope holding and emergency-stop behavior. |
| Controller and feedback | Hall sensors, encoder options, current limits and communication protocol affect drive behavior. |
| Duty cycle and environment | Continuous operation, start-stop frequency, temperature and sealing affect service reliability. |

## Vehicle Mass, Payload and Load Distribution

For AGV and AMR wheel-drive selection, provide both empty vehicle mass and maximum loaded mass. Load distribution should also be described because a two-wheel drive platform, four-wheel drive platform and differential-drive platform may place different loads on each driven wheel.

The drive system should be reviewed for the worst practical operating condition, including loaded acceleration, turning, ramp operation and stopping. A wheel motor that is acceptable for flat travel may be unsuitable for repeated slope starts or high-frequency start-stop cycles.

## Wheel Diameter, Speed and Torque Relationship

Wheel diameter directly affects both vehicle speed and required wheel torque. A larger wheel can increase travel distance per revolution, but it also increases the torque required at the wheel for the same tractive force.

For meaningful selection, provide:

- Actual rolling diameter of the wheel
- Target continuous vehicle speed
- Maximum vehicle speed
- Required acceleration and deceleration
- Wheel material and tire type
- Whether the wheel is supplied by the customer or integrated with the drive assembly

## Slope, Ramp and Gradeability Review

Slope operation is often a critical condition for AGV and AMR wheel drives. Provide the maximum slope angle or percentage grade, slope length, vehicle mass on the slope and whether the robot must start, stop or hold position on the slope.

Gradeability should be reviewed together with:

- Vehicle mass and payload
- Wheel radius
- Driven-wheel quantity
- Floor friction and tire traction
- Controller current limit
- Battery voltage under load
- Slope duration and duty cycle
- Required braking and parking behavior

Do not evaluate slope capability from motor peak torque alone. Peak torque duration, heat rise, wheel traction and controller protection all matter.

## Floor, Traction and Operating Surface

Different operating surfaces can significantly change the drive requirement. Indoor warehouse floors, epoxy floors, ramps, expansion joints, elevator gaps, thresholds, wet areas and outdoor surfaces may create different rolling resistance and traction conditions.

Please describe:

- Indoor or outdoor operation
- Smooth floor, rough floor or mixed surface
- Ramp, threshold or expansion-joint crossing
- Dust, water, oil or cleaning chemical exposure
- Wheel material and expected tire wear
- Required noise level if the robot operates near people

## Published SigGear Hub Gear Motors

The following published SigGear hub gear motors can be used as starting points for AGV and AMR wheel-drive evaluation:

| Model | Rated voltage | Rated power | Rated speed | Rated torque | Peak torque | Weight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [SG-2877](../products/hub-gear-motors/sg2877.md) | 24 VDC | 45 W | 130 rpm ±10% | 3 Nm | 10 Nm | 780 ±20 g |
| [SG-2878](../products/hub-gear-motors/sg2878.md) | 24 VDC | 75 W | 110 rpm ±10% | 6 Nm | 18 Nm | 1100 ±20 g |

Both models use a 99 mm outer diameter and a 9.75:1 planetary reduction ratio. Final selection depends on wheel diameter, vehicle mass, driven-wheel quantity, target speed, acceleration, slope, braking behavior, duty cycle and controller limits.

For custom wheel-drive mechanisms, compact steering modules, small conveyor wheels or customer-side motor integration, SigGear can also evaluate [8–42 mm planetary gearbox](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md) options when the application requires a separate reducer or compact gearbox instead of a standard hub gear motor.

## Hub Gear Motor or Separate Gearbox Solution

An integrated hub gear motor may be suitable when the mobile robot needs a compact wheel-side drive with motor and planetary reduction mechanism already matched in a standard catalog configuration.

A separate gearbox solution may be suitable when the customer already has a motor, wheel structure, steering module, brake, encoder, suspension or special housing. In that case, the gearbox input shaft, mounting interface, output shaft, wheel connection, speed limit and load condition must be confirmed.

The best architecture depends on vehicle layout, wheel size, payload, controller strategy, serviceability, sealing, quantity and customization scope.

## Controller, Feedback and Communication Boundaries

The standard SG-2877 and SG-2878 catalog configurations use Hall sensors and require an external controller. Integrated drivers, absolute encoders, CAN, RS485, EtherCAT and position or torque closed-loop control are not standard claims unless specifically included in the quotation.

Before selection, confirm:

- Battery voltage and voltage range under load
- Controller current limit and protection strategy
- Hall sensor or encoder requirement
- Speed-control, torque-control or position-control requirement
- CAN, RS485, PWM, EtherCAT or other communication interface requirement
- Whether the controller is supplied by the customer or requested from SigGear
- Fault reporting, temperature monitoring and braking logic requirements

Do not promise a communication protocol or closed-loop control mode until the selected controller, firmware and wiring plan are confirmed.

## Braking, Parking and Slope Holding

Mobile robots often require controlled braking and safe parking behavior. For an AGV or AMR drive system, specify:

- Required stopping distance
- Emergency-stop behavior
- Parking on flat ground or slope
- Whether mechanical brake is required
- Whether regenerative braking is expected
- Whether the vehicle must hold position after power loss
- Maximum slope and payload during holding

A mechanical brake must not be assumed to be included unless it is confirmed in the selected configuration, drawing and quotation.

## Duty Cycle, Heat and Service Life

Wheel-drive systems can experience repeated acceleration, deceleration, turning and load changes. Provide the real operating cycle instead of only maximum vehicle speed.

Useful information includes:

- Travel time and rest time
- Start-stop frequency
- Continuous travel distance
- Ramp frequency and ramp duration
- Daily operating hours
- Ambient temperature
- Cooling or enclosure condition
- Expected service-life target

Peak torque is not a continuous working rating. A wheel drive that can provide short overload torque may still be unsuitable if repeated acceleration or slope operation causes excessive temperature rise.

## Standard Configuration Boundaries

The published SG-2877 and SG-2878 standard configurations include:

- BLDC motor
- Planetary reduction mechanism
- Hall sensors
- Output shaft and mounting structure shown in the approved drawing

Unless explicitly included in the quotation, do not assume:

- Integrated driver
- Absolute encoder
- CAN, RS485 or EtherCAT communication
- Position or torque closed-loop control
- Wheel, tire or vehicle-side mounting hardware
- Mechanical brake
- Vehicle-side suspension or steering structure

## Prototype and Customization Review

Depending on project requirements and engineering feasibility, SigGear can evaluate:

- Output-shaft and mounting-interface customization
- Cable and connector customization
- Wheel-drive assembly requirements
- External controller matching
- Brake or feedback requirements after engineering review
- Customer branding and labeling
- Prototype support before production planning

Customization availability depends on technical feasibility, prototype quantity, expected annual volume and the level of engineering change required.

## Information Needed for an AGV or AMR Drive Selection Review

Please provide one requirement set for each wheel-drive position or vehicle platform.

Provide:

- Vehicle type and application
- Empty vehicle mass and maximum payload
- Load distribution and number of driven wheels
- Wheel diameter and wheel material
- Target continuous speed and maximum speed
- Acceleration and deceleration requirement
- Maximum slope, slope length and slope duration
- Whether the vehicle must start, stop or hold on a slope
- Floor condition and traction environment
- Operating voltage and controller current limit
- Braking, parking and emergency-stop requirements
- Hall sensor, encoder, driver and communication requirements
- Duty cycle, ambient temperature and daily operating hours
- Prototype quantity and estimated annual quantity
- Preferred architecture: hub gear motor or separate gearbox and motor

## Request an AGV or AMR Wheel Drive Selection Review

Send your AGV or AMR wheel-drive requirements to SigGear for a preliminary model review. Early requirements can be approximate, but vehicle mass, payload, wheel diameter, speed, slope, voltage and quantity are needed before a meaningful recommendation can be made.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Open an Engineering Request](https://github.com/SigGearDrive/SigGear-product-docs/issues/new/choose){ .md-button .md-button--primary }
[Send AGV or AMR Drive Requirements](../contact.md){ .md-button }
---
title: Planetary Gearheads for Automatic Pet Feeders & Litter Boxes | SigGear
description: Evaluate SigGear 8–42 mm planetary gearheads for automatic pet feeders, litter boxes and pet doors. Compare compact drive requirements, motor matching and STEP CAD.
---

# Planetary Gearheads for Automatic Pet Feeders, Litter Boxes and Pet Doors

Automatic pet-care products often need **small geared actuators** for portion dispensing, slow rotation, lid movement, latch release and positioning. For OEM engineers developing these mechanisms, a **precision planetary gearhead (planetary gearbox)** can be evaluated when an existing or proposed motor needs lower output speed and more usable output torque within a limited space.

SigGear publishes **12 frame sizes from 8 mm to 42 mm**, covering [Micro (8–16 mm), Miniature (20–32 mm) and Compact (36–42 mm) planetary gearheads](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md). We can review **Gearhead Only** integration with an existing motor or a **Motor + Gearhead Assembly** for a customer-specific design.

!!! note "Engineering application, not a production case study"
    The mechanisms below are potential OEM applications. This page does not claim that a SigGear gearhead has been validated, certified or mass-produced in any specific pet-care product.

[Find a Gearhead — Ratio & Stage Selector](../selection-guides/miniature-planetary-gearbox-selection-guide.md#preliminary-ratio-stage-finder){ .md-button .md-button--primary }
[Compare All 12 Gearhead Models](../products/planetary-gearboxes/index.md){ .md-button }
[Download Public Simplified STEP CAD](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }
[Send a Pet-Device Engineering Inquiry](../request-cad-sample-quote.md){ .md-button }

## Which Smart Pet Mechanisms Might Need a Planetary Gearhead?

| OEM mechanism | Motion to define | First engineering questions |
| --- | --- | --- |
| **Automatic pet feeder** | Auger, metering wheel, rotary plate or dispenser gate | Portion accuracy, food particle size, jam torque, speed, noise and cleaning |
| **Self-cleaning litter box** | Rotating drum, rake, separator or cover | Unbalanced load, starting torque, intermittent duty, stall detection and external bearing support |
| **Automatic pet door** | Latch, flap release or compact opening drive | Closing force, power-off behavior, obstacle detection, manual override and battery consumption |
| **Pet water dispenser or compact valve** | Valve, shutter or positioning mechanism | Flow/pressure load, wet-area separation, duty cycle and corrosion exposure |
| **Treat dispenser or interactive pet device** | Small dispensing, indexing or positioning motion | Repeatability, noise, cycle count, impact load and available diameter |

A gearbox alone does not determine the performance of the device. The customer must evaluate food contact, pet access, moving-part guarding, pinch hazards, firmware behavior and system-level reliability.

## Preliminary Frame-Size Orientation

Use diameter groups only as a **packaging starting point**, never as a suitability or rated-torque guarantee.

| Published SigGear class | Models | Possible first-pass mechanism |
| --- | --- | --- |
| **Micro Planetary Gearheads (8–16 mm)** | [8P](../products/planetary-gearboxes/8p-planetary-gearbox.md), [10P](../products/planetary-gearboxes/10p-planetary-gearbox.md), [12P](../products/planetary-gearboxes/12p-planetary-gearbox.md), [14P](../products/planetary-gearboxes/14p-planetary-gearbox.md), [16P](../products/planetary-gearboxes/16p-planetary-gearbox.md) | Small latches, dispensing gates and compact positioning axes |
| **Miniature Planetary Gearheads (20–32 mm)** | [20P](../products/planetary-gearboxes/20p-planetary-gearbox.md), [22P](../products/planetary-gearboxes/22p-planetary-gearbox.md), [24P](../products/planetary-gearboxes/24p-planetary-gearbox.md), [28P](../products/planetary-gearboxes/28p-planetary-gearbox.md), [32P](../products/planetary-gearboxes/32p-planetary-gearbox.md) | Feed wheels, augers, pet-door actuators and compact rotary mechanisms |
| **Compact Planetary Gearheads (36–42 mm)** | [36P](../products/planetary-gearboxes/36p-planetary-gearbox.md), [42P](../products/planetary-gearboxes/42p-planetary-gearbox.md) | Higher-load rotary or cleaning mechanisms if the actual load requires a larger frame |

For each candidate, compare the model-specific published ratios, allowable torque, stage-dependent length, motor input interface and output-shaft load. **Do not select a gearhead solely from its nominal diameter.**

## Design-In Checklist for Pet-Care OEMs

### Load, torque and blocked mechanisms

For an auger or dispenser, measure operating torque across the expected range of food shapes, container fill levels and humidity conditions. For a rotating drum or rake, include off-center mass and accumulated material. Define **normal load, start-up load, peak load, jam load and jam duration** separately; maximum momentary torque is not a continuous stall rating.

For a pulley, drum or similar rotary drive, the required shaft torque is related to tangential force and effective radius (`T = F × r`). A full assessment also includes friction, acceleration, drivetrain losses and safety margin.

### Output speed, accuracy and control

Specify the loaded motor speed, required actuator output speed, number of revolutions or travel angle per cycle, portioning accuracy and stop-position requirements. Encoder feedback, current sensing, end switches and control electronics are **system-specific**, not automatically included with a gearhead.

### Shaft support and mounting

An auger, drum or cantilevered part can add radial or axial loads to the output shaft. Review the load point and distance from bearing support; external bearings may be needed. Send the motor shaft drawing, mounting pattern, available assembly length and required output coupling.

### Noise, duty and environment

Pets may be sensitive to unexpected movement or sound. Acoustic performance depends on the actual motor, ratio, speed, mounting, enclosure and controller tuning, so a low-noise target must be tested on the final device. Also define cleaning frequency, condensation, dust and debris exposure, food residues and expected cycle life.

**No universal IP rating, food-contact approval, animal-safety certification or complete-device compliance is implied by a standard SigGear planetary gearhead listing.** The OEM must validate the finished assembly.

## Gearhead Only or Motor + Gearhead Assembly?

- **Gearhead Only:** Best when the customer has already chosen a motor. Share motor shaft diameter and length, locating pilot, mounting holes, loaded input speed and envelope.
- **Motor + Gearhead Assembly:** Best when the motor choice remains open. Share the load, required output motion, supply voltage, available space and duty cycle for an engineering review.

Both paths may require customized output shafts, adapters, mounting features or a project-specific motor interface. Feasibility must be confirmed before any promise of compatibility.

## Send These Details to Start an OEM Review

1. Device type: feeder, litter box, pet door, dispenser or other mechanism
2. Sketch or drawing, moving load, transmission geometry and jam condition
3. Output speed, travel angle or dispensing cycle time
4. Continuous load, peak load, stall/obstruction duration and duty cycle
5. Maximum gearhead diameter and complete assembly length
6. Existing motor information or available voltage and motor constraints
7. Shaft load, enclosure, cleaning and environmental requirements
8. Prototype quantity and expected annual production volume

[Request Gearhead CAD, Samples and an Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Read the General 8–42 mm Application Guide](planetary-gearbox-application-families.md){ .md-button }
[Related: Pump, Valve and Fluid-Control Mechanisms](pump-valve-fluid-control-gear-motors.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

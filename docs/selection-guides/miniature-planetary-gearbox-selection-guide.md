---
title: How to Select a Miniature Planetary Gearbox (8–42 mm) | SigGear
description: OEM guide to selecting miniature planetary gearboxes by ratio, rated torque, motor interface, duty cycle, gearbox length and 3D CAD.
---

# How to Select a Miniature Planetary Gearbox for an OEM Design

A miniature planetary gearbox, also called a planetary gearhead, should be selected from its **output load, motor operating point, duty cycle and installation interface**, not the diameter or maximum reduction ratio alone.

This engineering guide links to SigGear's 8–42 mm standard gearbox range. It does not represent a tested application or a claim that any configuration suits every mechanism.

[Compare 8–42 mm Planetary Gearboxes](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }
[Browse Simplified STEP CAD](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button }

## 1. Decide What Needs to Be Supplied

**Gearbox only:** If you already have a motor, provide its model or drawing, operating shaft speed, shaft dimensions, mounting-hole pattern, locating pilot, available axial space and required output. Motor-to-gearbox interface and operating compatibility require review.

**Motor + gearbox assembly:** If the motor has not been selected, provide the power supply, desired output motion, load or torque, available diameter and total length, and operating cycle. SigGear can evaluate a motor-matched gearbox assembly.

## 2. Estimate the Reduction Ratio From Loaded Speed

The preliminary reduction ratio is approximately **motor speed at the operating point divided by target gearbox output speed**. Do not automatically use the motor's no-load speed.

Compare this result with the published stage-specific ratio table of the selected gearbox. Different stages can change overall body length, torque rating and efficiency.

## 3. Compare Continuous and Peak Torque Separately

- **Normal running:** Compare required continuous operating torque with the exact configuration's rated allowable torque, considering cycle and necessary margin.
- **Cutting, startup, impact or jam events:** Consider magnitude, duration and frequency of peak loads. The published maximum momentary torque is **not** a continuous rating.
- **Motor matching:** Output torque estimates depend on the motor shaft torque, selected ratio and the relevant gearbox efficiency. Use the efficiency published for the selected configuration, not a family maximum.

Never transfer a torque rating from one frame size or stage configuration to another without technical confirmation.

## 4. Check the Full Mechanical Interface

Measure the gearbox outer diameter, **stage-dependent body length**, output shaft, flange, mounting holes and motor-side shaft interface. Total motor-plus-gearbox assembly length is not the same as gearbox body length.

Output torque and shaft loads are different constraints. Review radial and axial forces, their application point and whether the mechanism needs an external bearing to support pulleys, pinions, cranks or other cantilevered loads.

[Open Datasheets and Mechanical Interface References](../engineering-resources/planetary-gearboxes/index.md){ .md-button }

## 5. Validate Backlash, Holding, Noise and Environment

A published gearbox backlash value is not a claim of zero backlash or final-system positioning accuracy. Do not assume a planetary gearbox is self-locking. If the design needs power-off holding, check brake and full-mechanism requirements.

Service life, sound level, ingress protection and corrosion resistance must be confirmed for the selected configuration and operating environment; do not infer unlisted ratings.

## 6. Use the Correct CAD

Public SigGear **simplified 4-stage STEP references** are available for 8P, 10P, 12P, 14P, 16P, 20P, 22P, 24P, 28P, 32P, 36P and 42P. They support preliminary external space and mounting checks while omitting internal planetary mechanism detail.

A 4-stage CAD reference is **not interchangeable** with a 1-, 2- or 3-stage configuration. For final Design-In, request the exact ratio/stage drawing and motor interface revision.

[Download Public 4-Stage STEP Models](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button .md-button--primary }

## Application-Specific Engineering Questions

An [electric pruning-shear gearbox](../applications/electric-pruning-shears-planetary-gearbox.md) must be reviewed for blade geometry, cutting force variation, torque spikes and outdoor exposure. An [electric curtain gearmotor](../applications/electric-curtain-blind-window-opener-gear-motors.md) needs track friction, pulley speed, acoustic, holding and safety reviews. A [smart toilet or bidet mechanism](../applications/smart-toilet-bidet-planetary-gear-motors.md) adds low-noise, jam, humidity and cleaning-environment requirements. A [dexterous hand or robot gripper](../applications/robot-gripper-gear-motors.md) requires finger-force or tendon-spool geometry, shaft-load and packaging review. These are potential uses, not published customer case studies.

## What to Send for a First Review

| Item | Useful information |
| --- | --- |
| Motion | Output speed, stroke or rotation, duty cycle |
| Load | Continuous torque or mechanism geometry; peak event if known |
| Packaging | Diameter, total length, mounting and shaft |
| Existing motor | Model, drawing, shaft dimensions and loaded speed |
| Supply scope | Gearbox only or complete motor + gearbox |
| Project stage | Prototype quantity and forecast annual volume |

A motor drawing or mechanism sketch and the information already known are enough to start a preliminary review. Final configuration and performance require engineering confirmation.

**Wanrong Wang — SigGear**  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com?subject=Miniature%20Planetary%20Gearbox%20Selection)

[Request a Planetary Gearbox Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }

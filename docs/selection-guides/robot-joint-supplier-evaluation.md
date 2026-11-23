---
title: How to Evaluate a Robot Joint Actuator Supplier | STEP, Torque & Control | SigGear
description: Procurement and engineering checklist for evaluating robot joint actuator suppliers. Compare model-specific datasheets, torque ratings, STEP files, 2D drawings, encoder, driver, communication, external loads and prototype validation.
---

# How to Evaluate a Robot Joint Actuator Supplier

A robot joint actuator supplier should be evaluated on **configuration-specific engineering evidence**, not only on a torque headline or product photo.

For an early supplier comparison, ask whether the exact model under consideration has usable technical data, mechanical files, electronics information and a path from prototype validation to controlled production release.

## Supplier Evaluation Checklist

| Area | What to request or confirm |
| --- | --- |
| Product identity | Exact model and configuration being quoted |
| Torque | Continuous torque, peak torque, peak duration and test / operating condition |
| Speed | Rated and maximum output speed at the relevant operating point |
| Size | Complete OD, thickness / length, weight and connector envelope |
| Mechanical interface | Output flange / shaft, locating features, mounting pattern and datums |
| CAD | STEP model for packaging and design-in |
| 2D drawing | Interface dimensions, revision status and whether it is a reference or controlled drawing |
| External loads | Radial, axial and overturning load limits where applicable |
| Encoder | Exact encoder / feedback configuration and resolution if published |
| Driver | Integrated or external driver and the quoted hardware / firmware version |
| Communication | CAN, RS485, EtherCAT or another interface for the quoted configuration |
| Thermal / duty cycle | Continuous operation, hold time, peak events and cooling condition |
| Prototype path | Sample availability, validation plan and engineering review |
| Production path | Configuration freeze, controlled drawing and change-control process |

A supplier should not be assumed to support a function simply because another model in the same family supports it.

## Public Engineering Files Matter

For design-in, the most useful public supplier evidence normally includes:

- model-specific technical datasheet
- 2D mechanical reference
- STEP CAD
- clear rated / peak torque definitions
- model-specific driver / encoder / communication information
- test data where available
- engineering contact path for unresolved items

Public CAD is useful for packaging, but final production approval should still use the configuration-controlled interface and drawing revision.

## SigGear Public Robot Joint References

SigGear publishes planetary and cycloidal robot-joint reference products with downloadable engineering files.

[**6 Robot Joint Datasheets, 2D & STEP Downloads**](../engineering-resources/robot-joint-actuators/quick-downloads.md){ .md-button .md-button--primary }

### Planetary actuator references

- [SG-6010C](../products/robot-joint-actuators/sg6010c.md)
- [SG-6010D](../products/robot-joint-actuators/sg6010d.md)
- [SG-8021](../products/robot-joint-actuators/sg8021.md)
- [SG-6010HB](../products/robot-joint-actuators/sg6010hb.md) — separate public reference model

### Cycloidal joint references

- [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md)
- [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md)
- [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md)

These are public reference platforms. Their published ratings and electronics must not be transferred to a different custom configuration without confirmation.

## Questions for the Supplier Before Ordering a Prototype

1. Which exact model / variant is being quoted?
2. What is the continuous torque, and under what duty / thermal condition?
3. What is the peak torque, and how long can the peak be applied?
4. Which STEP file and 2D drawing correspond to the quoted hardware?
5. Is the drawing a reference copy or a revision-controlled production drawing?
6. Which encoder is installed?
7. Is the driver integrated or external?
8. Which communication protocol is supported by this exact version?
9. What current / voltage limits apply?
10. What external bearing loads are permitted?
11. What should be tested in the prototype before design freeze?
12. What changes require a new drawing, firmware or configuration review?

## Supplier Comparison: Keep the Boundary Conditions Equal

Do not compare:

- one supplier's peak torque with another supplier's continuous torque
- reducer-only weight with another supplier's complete actuator weight
- a driver-equipped CAD model with a no-driver mechanical version
- a public reference drawing with a controlled manufacturing drawing
- maximum speed at no load with rated speed under load

Use the same operating point and configuration boundary for every supplier.

## If the Joint Architecture Is Not Decided Yet

If the robot team has not decided between planetary and cycloidal transmission, compare the complete joint requirement first:

[Planetary vs Cycloidal Reducer for Robot Joints](planetary-vs-cycloidal-robot-joint.md){ .md-button }

If the team is choosing between a complete joint actuator and a separate motor + gearhead:

[Integrated Robot Joint vs Motor + Gearhead](integrated-robot-joint-vs-motor-gearhead.md){ .md-button }

For CAN / encoder / driver questions:

[Robot Joint CAN, Encoder & Driver Guide](robot-joint-can-encoder-driver-selection.md){ .md-button }

## Start a Supplier / Engineering Review

Send the target torque, speed, joint envelope, voltage, external loads, encoder / communication requirement and prototype quantity if known.

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)

[Request CAD, Sample or Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }

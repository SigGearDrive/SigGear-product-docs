---
title: Custom Cycloidal Transmission Engineering | Compact Robot Joint and High-Torque Drive Solutions | SigGear
description: SigGear works with engineers on custom cycloidal transmission and compact joint-drive projects, including motor integration, mechanical interfaces, driver configurations, prototype evaluation and design refinement.
---

# Custom Cycloidal Transmission Engineering

## Start From the Joint Requirement, Not the Transmission Assumption

You do not need to decide in advance that the project must use a cycloidal reducer.

For a compact robot joint, actuator or rotary mechanism, the first engineering review should start from the actual requirements:

- continuous and peak torque
- required output speed
- installation diameter and axial length
- load direction and external loads
- motor or motor constraints
- duty cycle
- backlash / positioning requirement
- driver, encoder and communication needs
- prototype and expected production quantity

SigGear can review these inputs and determine whether an existing cycloidal platform, a modified cycloidal configuration, a planetary solution or another arrangement should be evaluated.

[Send Your Joint Requirement](mailto:wangwanrong@siggear.com?subject=Custom%20Cycloidal%20Transmission%20Engineering%20Review){ .md-button .md-button--primary }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button }

## When a Cycloidal Structure May Be Worth Evaluating

A cycloidal transmission may be considered when a project needs a compact rotary joint with a relatively high torque requirement, limited axial space, controlled backlash and a mechanical architecture that can accommodate the selected cycloidal platform.

This does not mean that cycloidal transmission is always the better choice. Final suitability depends on the complete operating condition, including:

- torque-speed cycle
- peak duration
- installation envelope
- radial and axial loads
- efficiency requirement
- thermal condition
- noise requirement
- motor and controller selection
- shock or impact loading
- required service life

For projects where these trade-offs are still unclear, the engineering review should compare the actual application requirements rather than choosing the transmission type from a general rule.

## Common Custom Cycloidal Project Situations

### The current catalog joint does not fit

The project may require a different:

- outer diameter
- axial thickness
- mounting pattern
- locating feature
- output interface
- rear housing
- cable or connector arrangement
- driver / encoder configuration

The first step is to identify which requirements are fixed and which can be adjusted.

### The motor or controller is already selected

A project may start from a customer-selected motor, driver or control architecture.

In that case, useful starting information includes:

- motor drawing and dimensions
- operating voltage
- motor speed
- current / power information
- shaft and mounting interface
- driver type
- encoder or sensor requirement
- communication interface
- available total assembly space

The motor, reducer and interface need to be reviewed as one system rather than as independent parts.

### The customer needs the reducer or mechanical module only

Some projects use the customer's own motor, encoder or controller. Others require an integrated motor + reducer + driver configuration.

The exact supply scope depends on the selected platform and project requirements and must be confirmed during engineering review.

### The torque requirement is known but the architecture is not

If you know the output torque, speed and available space but are not sure whether to use a planetary or cycloidal structure, send those conditions first.

SigGear can compare the available reference platforms and identify what needs to be calculated or tested before the transmission structure is fixed.

## Existing SigGear Cycloidal Reference Platforms

SigGear currently publishes several cycloidal joint-module reference products.

| Reference model | Published transmission | Published reference data |
| --- | --- | --- |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel, 25:1 | 80 mm OD, 10 Nm rated torque, 50 Nm peak torque, 120 rpm rated output speed |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel, 25:1 | 100 mm OD, 25 Nm rated torque, 75 Nm peak torque, 60 rpm rated output speed |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel, 39:1 | 78.7 mm OD, 20 Nm rated torque, 52 Nm peak torque, 48 rpm rated output speed |

These values belong to the published reference models only. They must not be transferred to a new diameter, ratio, motor or custom configuration without engineering confirmation.

## CPM-80-25 as a Public Engineering Reference

CPM-80-25 currently has the most complete public cycloidal Engineering Pack on the SigGear site.

Public resources include:

- technical datasheet
- mechanical-interface reference
- simplified STEP for the no-driver configuration
- simplified STEP for the integrated-driver reference configuration
- measured performance data

[View CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md){ .md-button .md-button--primary }
[View CPM-80-25 Datasheet](../engineering-resources/cpm80-25/datasheet.md){ .md-button }
[View Mechanical Interface](../engineering-resources/cpm80-25/mechanical-interface.md){ .md-button }
[View Measured Performance Data](../engineering-resources/cpm80-25/performance-test-data.md){ .md-button }

The measured performance page contains test points at 24 V, 36 V and 48 V. These measured points are engineering evidence from the released test source and must not be treated as universal continuous operating ratings for a different configuration.

The public rated output torque for CPM-80-25 remains **10 Nm**, with **50 Nm** published peak output torque for preliminary product selection. Peak duration and application suitability require review of the actual current limit, duty cycle, thermal condition and installation.

## What Can Be Reviewed for a Custom Project

Depending on the reference platform and engineering feasibility, the following areas may be reviewed:

| Engineering area | Examples |
| --- | --- |
| Transmission | ratio and cycloidal structure based on the selected platform |
| Motor integration | motor size, speed, shaft, mounting and electrical constraints |
| Packaging | outer diameter, axial thickness, housing and installation envelope |
| Output interface | mounting pattern, flange, locating feature and customer-side mechanical interface |
| Feedback / control | Hall / encoder / driver configuration where supported by the selected platform |
| Communication | CAN or RS485 where supported by the selected driver configuration |
| Performance target | torque, speed, backlash, external loads and duty cycle |
| Assembly | cable, connector and rear-housing arrangement where applicable |

Not every item can be modified independently. A requested change may affect size, torque, speed, efficiency, life, thermal behavior, control hardware or cost.

## Integrated Driver or External Driver?

The SigGear cycloidal reference products do not all use the same electronics.

For example:

- **CPM-80-25** can be supplied with or without an integrated driver, with driver / encoder / communication details confirmed for the selected configuration.
- **CPM-100-25** can be supplied with or without an integrated driver, with the final driver / encoder / connector arrangement confirmed in the quotation.
- **CPM-78-39** uses Hall sensors in its standard catalog configuration and does **not** include an integrated driver or absolute encoder as a standard claim.

Do not assume CAN, RS485, absolute encoder or closed-loop control across all cycloidal models. The electronics must be matched to the quoted configuration.

## What to Send First

A complete specification is not required for the first discussion.

Start with the information you already have:

1. **Application** — robot joint, actuator or other rotary mechanism
2. **Torque** — continuous and peak requirement if known
3. **Peak duration** — if a peak torque is important
4. **Speed** — required output speed
5. **Installation space** — maximum diameter and axial length
6. **External loads** — radial / axial / impact conditions if relevant
7. **Motor / controller** — existing motor or preferred electrical architecture
8. **Interface** — mounting, shaft, flange or drawing if already defined
9. **Project stage** — concept, prototype, pilot or production planning
10. **Quantity** — prototype quantity and expected production volume if known

If torque is not yet defined, send the mechanism geometry, load, arm length or other information that describes the joint.

If the transmission type is not yet defined, send the operating conditions and let the engineering review start from the application.

## Engineering Development Path

A custom cycloidal project may move through:

**Application / Joint Requirement**  
→ **Feasibility Review**  
→ **Cycloidal vs. Alternative Transmission Evaluation**  
→ **Motor / Interface Review**  
→ **Configuration Drawing**  
→ **Prototype or Sample**  
→ **Mechanical / Electrical Test**  
→ **Parameter or Interface Refinement**  
→ **Design Confirmation**  
→ **Pilot Preparation**  
→ **Production**

The exact sequence depends on the maturity of the customer's design and how much of the motor, control and mechanical architecture has already been fixed.

## Applications

Cycloidal transmission may be evaluated for compact rotary joints and mechanisms in areas such as:

- humanoid robots
- quadruped robots
- robotic arms
- exoskeletons
- rehabilitation robots
- compact industrial rotary axes
- other mechanisms requiring a compact high-torque joint drive

These are application areas where cycloidal transmission may be relevant. They are not statements that SigGear has a public customer case in every listed application.

## Confidential Custom Projects

Many custom transmission projects involve unreleased products, proprietary mechanisms or customer drawings and therefore cannot be shown publicly.

SigGear uses public reference products, CAD resources, interface drawings and measured test data to demonstrate real engineering capability without exposing confidential customer designs.

## Not Sure Whether to Use Planetary or Cycloidal?

Send the application, required output motion and installation constraints first.

The engineering discussion should determine which transmission approach deserves further evaluation.

[Open Custom Precision Transmission Engineering](index.md){ .md-button }
[View Custom Planetary Gearbox Engineering](custom-planetary-gearbox.md){ .md-button }

## Discuss Your Cycloidal Transmission Project

Send the information you already have — even if the ratio, motor or final transmission structure is not defined yet.

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Your Joint Requirement](mailto:wangwanrong@siggear.com?subject=Custom%20Cycloidal%20Transmission%20Engineering%20Review){ .md-button }

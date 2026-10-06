---
title: Prototype to Production for Custom Gearboxes | SigGear
description: A practical path from custom gearbox feasibility and prototype testing through design refinement, Design-In, pilot preparation and production release.
---

# Prototype to Design-In and Production

## A Custom Transmission Project Is Not Finished When the First Sample Moves

For an engineering team, the first prototype answers only one question:

**Can this transmission concept work well enough to continue evaluating?**

A production-ready configuration requires more than a successful first sample. The motor, gearbox, ratio, mechanical interface, operating point, materials, driver / encoder configuration where applicable, drawings and inspection requirements need to converge into a controlled configuration that can be manufactured repeatedly.

SigGear works with engineers through this development path for applicable compact transmission projects.

[Discuss Your Project](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Your Drawing or Requirement](mailto:wangwanrong@siggear.com?subject=Prototype%20to%20Production%20Transmission%20Project){ .md-button }

## Start From the Transmission Architecture

If the transmission architecture is already known, continue with the relevant engineering path:

[Custom Planetary Gearbox Engineering](custom-planetary-gearbox.md){ .md-button }
[Custom Cycloidal Transmission Engineering](custom-cycloidal-transmission.md){ .md-button }
[Custom Robot Joint Actuator Development](robot-joint-actuator-development.md){ .md-button }

## Typical Development Path

A project may move through:

**Idea / Requirement / Existing Design**  
→ **Feasibility Review**  
→ **Transmission Architecture Review**  
→ **Preliminary Configuration**  
→ **Prototype / Sample**  
→ **Application Test**  
→ **Design Iteration**  
→ **Design Freeze / Design-In**  
→ **Pilot Preparation**  
→ **Production Release**

The exact sequence depends on how mature the customer's design already is.

A project based on an existing SigGear platform may move faster than a project that requires a different motor, ratio, interface or transmission architecture.

## Stage 1 — Idea, Drawing or Existing Mechanism

The first discussion can start from:

- a product idea
- an existing mechanism
- a customer motor
- a current gearbox that needs to be replaced
- a CAD model or drawing
- a space envelope
- a torque / speed target
- a prototype that does not yet meet the required performance

A complete transmission specification is not required before the first engineering discussion.

Useful starting information includes:

- application
- what needs to move
- load or torque requirement if known
- output speed
- available diameter and length
- operating voltage where applicable
- existing motor or controller if already selected
- shaft and mounting constraints
- prototype quantity
- expected production volume if known

## Stage 2 — Feasibility Review

The purpose of feasibility review is to determine whether the project has a credible engineering path before committing to a final configuration.

The review may include:

- planetary vs. cycloidal transmission structure
- existing SigGear platform vs. modified configuration
- motor suitability
- preliminary ratio
- size and packaging
- output interface
- bearing and external-load conditions
- driver / encoder architecture where applicable
- parameters that still need calculation or testing

The result of this stage is not a guaranteed final design. It is a decision about which concept deserves further engineering work.

## Stage 3 — Preliminary Configuration

Once the architecture is selected, the project can be narrowed into a prototype configuration.

Depending on the product family, this may define:

- gearbox frame size
- stage count and ratio
- motor
- motor-to-gearbox interface
- output shaft or flange
- mounting pattern
- housing or packaging arrangement
- encoder / sensor configuration
- driver configuration
- cable and connector arrangement
- communication interface where applicable

At this stage, some details may still be provisional.

## Stage 4 — Prototype or Sample

The first prototype should be built around a clear engineering question.

Examples:

- does the assembly fit the available space?
- does the motor + gearbox combination reach the required output speed?
- does the joint handle the representative load?
- does the selected ratio provide the expected motion?
- does the shaft or flange interface work with the customer's mechanism?
- does the selected driver / encoder configuration integrate with the controller?

The sample should not be treated as a frozen production design simply because it can rotate or transmit load.

[Open the Sample Validation Workflow](../engineering-center/sample-validation-workflow.md){ .md-button .md-button--primary }

## Stage 5 — Application Test

The prototype should be evaluated in the actual or representative mechanism.

Useful test conditions may include:

- continuous load
- peak load and peak duration
- output speed
- acceleration and deceleration
- duty cycle
- direction reversals
- radial / axial loads
- temperature
- current where applicable
- noise or vibration where relevant
- backlash or positioning behavior where relevant
- encoder / communication behavior
- power-off behavior if important

A test result is meaningful only when the operating condition is recorded.

## Stage 6 — Design Iteration

A prototype that reveals a problem is not automatically a failed project.

The purpose of engineering validation is to identify what must change before the next build.

Depending on the project, iteration may involve:

- ratio
- motor
- output shaft
- mounting pattern
- housing
- axial length
- bearing arrangement
- cable / connector
- driver
- encoder
- current limit
- control configuration
- thermal condition
- assembly method

A change to one parameter can affect several others. For example, changing motor speed or ratio can affect torque, efficiency, gearbox length, thermal behavior and control settings.

Therefore, revisions should be treated as controlled configuration changes rather than isolated adjustments.

## Stage 7 — Design Freeze and Design-In

Before the transmission is treated as designed into the customer's product, the exact configuration should be identifiable.

Typical items to freeze include:

- product / project configuration
- reduction ratio
- motor
- output interface
- motor-side interface
- envelope dimensions
- mounting features
- driver and encoder where applicable
- cable and connector configuration
- firmware / protocol revision where applicable
- approved operating conditions
- drawing revision

The goal is to make sure the customer, SigGear engineering and manufacturing teams are all referring to the same configuration.

[Open the Design-In Checklist](../engineering-center/design-in-checklist.md){ .md-button .md-button--primary }

## Stage 8 — Pilot Preparation

Before a pilot build, the project should move from an engineering sample mindset toward repeatable manufacturing.

Items that may need confirmation include:

- controlled drawing revision
- configuration / BOM definition
- inspection characteristics
- incoming or outgoing test requirements
- critical dimensions
- assembly requirements
- cable / connector definition
- labeling or packaging requirements where relevant
- pilot quantity
- delivery schedule
- change-control expectations

The exact documentation scope depends on the project and must be agreed with the customer.

## Stage 9 — Production Release

A custom transmission should enter regular production only after the configuration and commercial scope have been confirmed.

Production release may require confirmation of:

- final approved configuration
- technical agreement or controlled drawing
- order quantity
- forecast or expected demand where available
- manufacturing and inspection requirements
- packaging / labeling requirements where applicable
- approved changes from the prototype or pilot stage

SigGear does not treat an early sample, preliminary drawing or feasibility concept as an automatic production approval.

## What Engineers Can Change During Development

Depending on the platform and engineering feasibility, development may include review of:

| Area | Examples |
| --- | --- |
| Transmission | planetary / cycloidal structure, ratio, stage count |
| Motor | motor type, speed, power and mechanical interface |
| Packaging | diameter, length, housing and installation envelope |
| Input | shaft, pinion, pilot and mounting interface |
| Output | shaft, flange, mounting pattern and locating features |
| Bearing / load | radial, axial and overturning load arrangement |
| Feedback | Hall / encoder configuration where supported |
| Driver / control | integrated or external driver and supported control functions |
| Connection | cable, connector and communication interface |
| Operating target | torque, speed, backlash, duty cycle and thermal condition |

Not every parameter can be changed independently, and not every requested change is feasible on every product platform.

## Existing Platforms Can Shorten the Development Path

A project does not always require a completely new transmission.

Existing SigGear products can be used as engineering starting points.

Examples include:

- **8-42 mm planetary gearbox platforms** for miniature and compact gear drives
- **32P** with public motor-integration and mechanical-interface resources
- **SG-6010C / SG-6010D / SG-8021** planetary robot-joint reference platforms
- **CPM-80-25 / CPM-100-25 / CPM-78-39** cycloidal reference platforms

A project may use one of these products directly, modify the surrounding interface, or use the platform as a reference while another configuration is evaluated.

[Open Custom Precision Transmission Engineering](index.md){ .md-button }
[Open the Engineering Center](../engineering-center/index.md){ .md-button }

## Confidentiality and Customer Designs

Custom development often involves unreleased products, customer CAD, proprietary mechanisms and future production plans.

These projects may be protected by confidentiality agreements and therefore cannot be shown publicly.

SigGear uses public reference products, engineering resources, manufacturing information and released test data to show its technical capabilities without exposing confidential customer designs.

## What SigGear Does Not Assume

Before a project reaches production release, do not assume that:

- the first prototype is the final production configuration
- a measured short-duration test point is a continuous rating
- a driver feature from one model applies to another
- a public simplified STEP replaces a controlled production drawing
- a requested customization is feasible without engineering review
- a prototype quantity automatically defines production MOQ or pricing
- an application area listed on the website represents a public customer case

## Start From Where Your Project Is Today

You may be at:

**Concept**  
**CAD design**  
**Prototype**  
**Current-product replacement**  
**Sample validation**  
**Design-In**  
**Pilot preparation**

Send the current drawing, motor, mechanism or problem.

SigGear can review what is already defined, what is still missing and what should be validated next.

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Your Project](mailto:wangwanrong@siggear.com?subject=Prototype%20to%20Production%20Transmission%20Project){ .md-button }

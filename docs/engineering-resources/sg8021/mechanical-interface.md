---
title: SG-8021 Mechanical Interface | Public Evaluation Reference | SigGear
description: Public SG-8021 mechanical evaluation reference for envelope, load screening and controlled-drawing request before final robot-joint design-in.
---

# SG-8021 Mechanical Interface v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

This page provides the SG-8021 mechanical information that is already published and suitable for early packaging and load evaluation.

!!! warning
    This is not a manufacturing drawing. Detailed mounting-hole geometry, tolerances, datums, output-interface dimensions and connector clearances are not published here and must be confirmed from the controlled drawing for the ordered configuration.

## Published Mechanical Envelope

| Item | Published value |
| --- | --- |
| Maximum body diameter | 100 mm |
| Overall product thickness | 42.6 mm |
| Product weight | 671 g |
| Allowable radial force | 1300 N |
| Allowable axial force | 550 N |

## Low-Profile Packaging Reference

The 42.6 mm published body thickness makes SG-8021 relevant to projects where axial packaging is a primary design constraint.

Actual installation clearance must still include:

- Connector and cable routing
- Customer-side mounting structure
- Required service / assembly space
- Driver configuration when included

## Load Evaluation Boundary

Published radial and axial force values are useful for preliminary screening. Final suitability still depends on:

- Load direction
- Load offset / moment arm
- Speed
- Duty cycle
- Shock or impact load
- Required bearing life
- Installation stiffness

## Exploded Structure Reference

The SG-8021 product page contains a real exploded photograph of the actuator showing the motor, planetary transmission and a driver-board configuration.

[View SG-8021 Exploded Product Reference](../../products/robot-joint-actuators/sg8021.md){ .md-button }

Use the image to understand product architecture only. Do not derive controlled dimensions, tolerances or production geometry from the photograph.

## Controlled Drawing Reconciliation

Two SG-8021 mechanical drawings have now been reviewed.

- The **driver-equipped drawing** shows an overall axial dimension of **42.06 mm**.
- A separate drawing identified as **SG8021A** shows a different mechanical envelope, including an overall axial dimension of **30.51 +/-0.50 mm**.

The current public product page continues to use **42.6 mm** as the nominal driver-equipped product thickness until the drawing revision and public nominal value are formally reconciled.

These drawings must not be interchanged during final design-in. Use the configuration-matched controlled drawing supplied with the quotation.

A full driver-equipped SG-8021 STEP assembly is available internally for engineering review but is not released here as a public download because it contains full assembly geometry.

## Design-In Boundary

Before final mechanical design, confirm:

- Mounting-hole pattern and thread details
- Output-side interface geometry
- Reference datums and tolerances
- Cable and connector orientation
- Load direction and moment arm
- Shock / impact condition
- Duty cycle
- Driver-equipped or non-driver configuration

## CAD and Controlled Drawing

A public simplified STEP model is **not currently released in this repository** for SG-8021.

For packaging, tolerance stack-up or production design-in, request the current controlled drawing and configuration-matched CAD file.

[Request Controlled Drawing / CAD](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Resource

[SG-8021 Technical Datasheet v1.0](datasheet.md){ .md-button }
[SG-8021 Product Page](../../products/robot-joint-actuators/sg8021.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

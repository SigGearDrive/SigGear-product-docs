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

The SG-8021 product page contains an exploded internal-layout illustration of the motor, planetary transmission and a driver-board configuration.

[View SG-8021 Exploded Product Reference](../../products/robot-joint-actuators/sg8021.md){ .md-button }

Use the illustration for architecture reference only. Do not derive production dimensions or tolerances from it.

## Controlled Drawing Reconciliation

Two SG-8021 mechanical drawings have now been reviewed.

- The **driver-equipped drawing** shows an overall axial dimension of **42.06 mm**.
- A separate drawing identified as **SG8021A** shows a different mechanical envelope, including an overall axial dimension of **30.51 +/-0.50 mm**.

The current public product page continues to use **42.6 mm** as the nominal driver-equipped product thickness until the drawing revision and public nominal value are formally reconciled.

These drawings must not be interchanged during final design-in. Use the configuration-matched controlled drawing supplied with the quotation.

The original driver-equipped SG-8021 full assembly STEP is publicly released (2026-11-18) and contains the complete assembly geometry.

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

[**Download Original Full Assembly STEP — Driver Version**](../../assets/downloads/joint-actuators/SG-8021_Driver_Version_Original_Full_Assembly_20261118.step){ .md-button .md-button--primary }

The file is a **driver-equipped assembly**; it is not a reference for the driverless configuration. No separate simplified STEP is currently published.

For packaging, tolerance stack-up or production design-in, request the current controlled drawing and configuration-matched CAD file.

[Request Controlled Drawing / CAD](mailto:luffy@siggear.com?subject=SigGear%20Engineering%20Inquiry){ .md-button .md-button--primary }

## Related Resource

[SG-8021 Technical Datasheet v1.0](datasheet.md){ .md-button }
[SG-8021 Product Page](../../products/robot-joint-actuators/sg8021.md){ .md-button }

## Engineering Contact

**Luffy Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)

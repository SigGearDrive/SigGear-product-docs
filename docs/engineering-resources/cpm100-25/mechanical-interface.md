---
title: CPM-100-25 Mechanical Interface | Public Evaluation Reference | SigGear
description: Public CPM-100-25 mechanical evaluation reference for envelope, load screening and controlled-drawing request before final cycloidal joint design-in.
---

# CPM-100-25 Mechanical Interface v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

This page provides the CPM-100-25 mechanical information that is already published and suitable for early packaging and load evaluation.

!!! warning
    This is not a manufacturing drawing. Detailed mounting-hole geometry, tolerances, datums, output-interface dimensions and connector clearances are not published here and must be confirmed from the controlled drawing for the ordered configuration.

## Published Mechanical Envelope

| Item | Published value |
| --- | --- |
| Maximum body diameter | 100 mm |
| Overall product thickness | 29.5 mm |
| Product weight | 630 g |
| Allowable radial force | 500 N |
| Allowable axial force | 300 N |

## Confirmed Dual-Encoder Mechanical Variant

The supplied 2D source drawing is labelled **SG2556D** and corresponds to the **48 mm dual-encoder, driver-equipped CPM-100-25D reference**. This source identification does not constitute final engineering release approval.

Its source-drawing envelope includes:

- Maximum outer diameter: **100 mm**
- Overall axial dimension: **48 mm**
- Product weight: **853 g**

This is not the same envelope as the current base public configuration of **29.5 mm / 630 g**.

[View Dual Encoder Variant Reference](dual-encoder-variant.md){ .md-button }

## Configuration Considerations

The public product page shows both:

- A configuration without integrated driver
- A configuration with integrated driver

Packaging, connector and cable details therefore depend on the selected configuration.

Final mechanical clearance must account for:

- Driver housing when included
- Connector and cable routing
- Customer-side mounting structure
- Required assembly / service space

## Load Evaluation Boundary

Published radial and axial force values are useful for preliminary screening only.

Final suitability still depends on:

- Load direction
- Load offset / moment arm
- Speed
- Duty cycle
- Shock or impact load
- Required bearing life
- Installation stiffness

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

Original STEP assembly exports are published for **two distinct variants**:

[**Original Full STEP · Standard 29.5 mm**](../../assets/downloads/joint-actuators/CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step){ .md-button .md-button--primary }

[**Original Full STEP · Dual Encoder + Driver 48 mm**](../../assets/downloads/joint-actuators/CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step){ .md-button }

The 48 mm dual-encoder/driver version has a different envelope from the standard 29.5 mm model. **No simplified reference STEP** is released for CPM-100-25; both links are original full-assembly STEP files. The matching [**SG2556D 48 mm 2D engineering-reference PDF**](../../assets/downloads/joint-actuators/CPM-100-25D_2D_Dual_Encoder_Driver_48mm.pdf) is now public, but it is **not an approved manufacturing-controlled drawing**. A configuration-matched approved controlled 2D drawing remains necessary for production.

[Request Controlled Drawing](../../request-cad-sample-quote.md){ .md-button }

## Related Resource

[CPM-100-25 Technical Datasheet v1.0](datasheet.md){ .md-button }
[CPM-100-25 Product Page](../../products/cycloidal-joint-modules/cpm100-25.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

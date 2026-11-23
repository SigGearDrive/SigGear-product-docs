---
title: SG-6010D Mechanical Interface | Public Evaluation Reference | SigGear
description: Public SG-6010D mechanical evaluation reference for product envelope, load screening and controlled-drawing request before final design-in.
---

# SG-6010D Mechanical Interface v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

This page provides only the SG-6010D mechanical information that is already published and suitable for early project evaluation.

!!! warning
    This is not a manufacturing drawing. Detailed mounting-hole geometry, tolerances, datums, shaft / output-interface dimensions and connector clearances are not published here and must be confirmed from the controlled drawing for the ordered configuration.

## Published Mechanical Envelope

| Item | Published value |
| --- | --- |
| Maximum body diameter | 80.0 mm |
| Overall product thickness | 58.77 mm |
| Product weight | 791 g |
| Allowable radial force | 1000 N |
| Allowable axial force | 400 N |

## Configuration Considerations

The external packaging and connection details can depend on whether the selected unit includes:

- Integrated driver
- Encoder configuration
- Connector / cable configuration

The published product visuals show a driver-equipped reference configuration; a render is not dimensional or photographic proof of a particular delivered unit. Confirm the exact driver, connector and mechanical envelope for the ordered product.

## Controlled Drawing Reconciliation

A supplier-provided 2D assembly drawing labelled **SG6010D** has been checked against the published envelope. The **2D assembly source PDF is now published as a public engineering-reference copy**. Its publication does not constitute approval as a revision-controlled manufacturing drawing.

The drawing confirms:

- Total reduction ratio: **28.13:1**
- First-stage ratio: **9.67:1**
- Second-stage ratio: **2.908:1**
- Overall axial dimension: **58.77 mm** nominal
- Complete actuator weight: **791 g**

The same drawing separates two operating tables:

- **Motor + second-stage reduction test:** 100 +/-10 rpm rated speed, 170 +/-10 rpm no-load speed, 16 Nm rated torque and 50 Nm peak torque.
- **One controller-limited configuration:** 60 +/-10 rpm rated speed, 170 +/-10 rpm no-load speed, 16 Nm rated torque and 45 Nm peak torque.

The second table is configuration-specific and must not replace the base mechanical test values for every SG-6010D order.

An original SG-6010D full assembly STEP is publicly downloadable (released 2026-11-18); it contains full assembly geometry.

## Design-In Boundary

Before final mechanical design, confirm:

- Mounting-hole pattern and thread details
- Output-side interface geometry
- Reference datums and tolerances
- Cable and connector orientation
- Load direction and moment arm
- Shock / impact condition
- Duty cycle
- Thermal environment
- Driver-equipped or non-driver configuration

## CAD and Controlled Drawing

[**Download SG-6010D Original Full Assembly STEP**](../../assets/downloads/joint-actuators/SG-6010D_Original_Full_Assembly_20261118.step){ .md-button .md-button--primary }

[**Download 2D Assembly Reference PDF**](../../assets/downloads/joint-actuators/SG-6010D_2D_Assembly_Drawing.pdf){ .md-button }

There is no separate public simplified STEP for this model; the STEP link above is the complete original assembly. The 2D PDF is a supplier reference, not a manufacturing-controlled release.

The original supplier drawing is now linked as a non-controlled public 2D reference. For tolerance stack-up or production, request the approved configuration-matched controlled drawing.

[Request Controlled Drawing / CAD](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Resource

[SG-6010D Technical Datasheet v1.0](datasheet.md){ .md-button }
[SG-6010D Product Page](../../products/robot-joint-actuators/sg6010d.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)

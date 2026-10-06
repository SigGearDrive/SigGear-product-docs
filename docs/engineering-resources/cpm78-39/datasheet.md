---
title: CPM-78-39 Datasheet | 20 Nm Cycloidal Robot Joint Module | SigGear
description: Public CPM-78-39 engineering reference with controlled-drawing-backed dimensions, torque, speed and motor electrical parameters for early evaluation.
---

# CPM-78-39 Technical Datasheet v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

CPM-78-39 is a compact 39:1 cycloidal robot joint module with 20 Nm rated output torque and 48 rpm rated output speed.

The values below have been reconciled against the current public product record and a SigGear controlled mechanical drawing supplied for engineering review.

## Key Performance

| Parameter | Controlled value |
| --- | --- |
| Transmission structure | Cycloidal pinwheel |
| Outer diameter | 78.7 mm |
| Product thickness | 35.8 mm |
| Reduction ratio | 39:1 |
| Operating voltage | 36 VDC |
| Rated motor power | 200 W |
| Rated output speed | 48 rpm |
| No-load output speed | 54 rpm |
| Rated output torque | 20 Nm |
| Peak output torque | 52 Nm |
| Weight | 600 g |
| Hall angle | 120° |

!!! warning
    Peak torque is not a continuous rating. Peak-torque duration, current limit, duty cycle and thermal suitability must be confirmed for the actual application.

## Motor Electrical Parameters

| Parameter | Controlled value |
| --- | --- |
| Phase resistance | 0.225 ohm |
| Phase inductance | 425 uH |
| Maximum phase current | 13 A |
| Rated bus current | 5 A |
| Static working bus current | 0.1 A |
| Motor structure | 24P28N, drawing notation |
| Temperature sensor | MF52B |
| Back-EMF constant | 0.149 Vs/rad |

## Standard Configuration Boundary

The current standard CPM-78-39 public configuration uses Hall sensors and does not include an integrated driver or absolute encoder as a standard claim.

External driver, encoder, communication interface and closed-loop control solution must be confirmed for the project.

## Backlash Data Boundary

The public product page currently lists an angular backlash range of 5-10 arcmin.

A separate uploaded laboratory report is titled as a backlash test but reports results in N.m rather than angular units. Because the test method and interpretation are not sufficiently defined for public engineering use, those values are **not** used here as an angular-backlash verification.

## CAD and Drawings

A controlled 2D drawing is available for engineering review.

A public STEP model is not currently released in this repository for CPM-78-39.

[Request CAD, Drawing or Integration Files](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Selection Information Required

Please provide:

- Application and joint position
- Rated and peak torque
- Required peak-torque duration
- Required output speed
- Installation envelope
- Duty cycle
- Driver / encoder / communication requirements
- Prototype quantity and estimated annual quantity

## Related Pages

[CPM-78-39 Product Page](../../products/cycloidal-joint-modules/cpm78-39.md){ .md-button }
[Custom Cycloidal Transmission Engineering](../../custom-engineering/custom-cycloidal-transmission.md){ .md-button }
[Robot Joint Selection Guide](../../selection-guides/robot-joint-actuator-selection-guide.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

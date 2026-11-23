---
title: 12 mm Precision Planetary Gearhead Datasheet (12P) | 1–4 Stages | SigGear
description: Public 12P 12 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 12 mm Precision Planetary Gearhead Datasheet (12P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

**Input-speed policy revised:** 2026-11-19 (current 12P engineering data confirms 1,000–50,000 rpm).  

The SigGear 12P is a 12 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 12 mm |
| Number of stages | 1-4 |
| gearhead length range | 11.35–19.60 mm |
| Reduction ratio range | 3.5:1–509.1:1 |
| Rated allowable torque range | 196.1–411.9 mN·m |
| Maximum momentary torque range | 392.3–823.8 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.5° |
| Continuous permissible input speed | 1,000–50,000 rpm |
| Operating temperature range | −40 to 120 °C |

Maximum momentary torque is not a continuous working rating.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 11.35 mm | 3.5 / 4 / 4.75 | 196.1 mN·m | 392.3 mN·m | 90% |
| 2 | 14.10 mm | 12.25 / 14 / 16 / 16.6 / 19 / 22.6 | 294.2 mN·m | 588.4 mN·m | 80% |
| 3 | 16.85 mm | 42.9 / 49 / 56 / 58.2 / 64 / 66.5 / 76 / 79 / 90.25 / 107.2 | 353.0 mN·m | 706.1 mN·m | 73% |
| 4 | 19.60 mm | 150.1 / 171.5 / 196 / 203.7 / 224 / 232.7 / 256 / 266 / 276.4 / 304 / 315.9 / 361 / 375.1 / 428.7 / 509.1 | 411.9 mN·m | 823.8 mN·m | 66% |

## Published Load / Shaft Limits

| Parameter | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 0.8 kgf |
| Shaft axial load | ≤ 0.25 kgf |
| Thrust shaft play | ≤ 0.04 mm |

Only values currently published for 12P are shown. Do not transfer limits from another frame size.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–36 VDC**
- Adapted DC motor power: **below 4 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 12P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

[Download 12P Simplified STEP - 4-Stage Reference](../../assets/downloads/12p/12P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

[Download 12P Full Assembly STEP](../../assets/downloads/12p/12P_Full_Assembly.step){ .md-button }

A simplified public **4-stage STEP reference** is released for early packaging and mechanical Design-In. The full assembly STEP for 12P is now publicly available. It is the original Creo assembly export supplied for this release. The simplified STEP remains a separate 4-stage reference model for preliminary packaging.

For final CAD, provide the selected ratio, stage count and motor interface.

[View 2D Drawing & Full Assembly Release Status](../planetary-gearboxes/public-cad-release-v1.md){ .md-button }

## Selection Information Required

Please provide:

- Required output speed or reduction ratio
- Continuous and momentary output torque
- Motor voltage, power and speed
- Motor shaft diameter and length
- Motor mounting-hole pattern and locating pilot
- Output-shaft requirements
- Radial and axial loads
- Duty cycle and ambient temperature
- Backlash, noise and service-life targets
- Prototype and annual quantity

## Related Product

[View 12P Product Page](../../products/planetary-gearboxes/12p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Luffy Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)

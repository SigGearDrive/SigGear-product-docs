---
title: 42P Motor Integration Guide | 42 mm Planetary Gearbox | SigGear
description: Motor matching and mechanical integration guide for the SigGear 42P 42 mm planetary gearbox, including motor reference range, input interface and information required for a matched motor + gearbox assembly.
---

# 42P Motor Integration Guide

The 42P can be evaluated as a **gearbox-only** solution or as part of a matched **motor + planetary gearbox** assembly.

This guide uses only the currently published 42P gearbox and interface data. Final motor matching depends on the selected ratio, stage count, motor operating point, duty cycle and mechanical interface.

## Published Motor-Matching Reference

| Parameter | Published reference |
| --- | --- |
| Motor type | DC motor |
| Nominal voltage | 3-48 VDC |
| Adapted motor power | Below 200 W |
| Continuous permissible gearbox input speed | <= 8,000 rpm |

These are motor-matching references for the 42P platform, not electrical ratings of the mechanical gearbox itself.

## Current Motor-Side Interface

The current 42P controlled interface drawing shows:

- gearbox body diameter: **42 mm**
- motor-side center opening: **Ø16.0 mm (+0.05 / 0 mm)**
- motor-side mounting: **2 x Ø3.1 mm holes**
- opposed mounting-hole spacing: **25.0 ±0.1 mm**
- stage-dependent gearbox body length: **35.6 / 46.9 / 58.2 / 69.5 mm**

[Open 42P Mechanical Interface v1.1](mechanical-interface.md){ .md-button .md-button--primary }

## Gearbox Operating Limits Relevant to Motor Matching

| Parameter | Public value |
| --- | ---: |
| Rated allowable torque range | 80.0-150.0 kgf.cm |
| Maximum momentary torque range | 160.0-300.0 kgf.cm |
| Continuous permissible input speed | <= 8,000 rpm |
| Backlash at no load | <= 1.2 deg |
| Operating temperature range | -40 to 120 C |

Maximum momentary torque is not a continuous operating rating.

## Information Required for Motor Matching

To evaluate a customer's motor or prepare a SigGear motor + gearbox configuration, provide:

- motor type
- nominal voltage
- rated and peak power
- rated / no-load speed
- motor shaft diameter
- usable shaft length
- pinion / flat / key requirement
- mounting-hole pattern
- locating pilot diameter
- available total assembly length
- target output speed
- continuous output torque
- momentary / peak output torque and duration
- duty cycle
- ambient temperature
- prototype quantity
- estimated annual quantity

If the customer does not know the reduction ratio, motor speed plus target output speed is enough for the first review.

## Integration Workflow

**Application requirement**  
-> check 42 mm envelope  
-> select stage and ratio  
-> check rated torque and input-speed limit  
-> review motor operating point  
-> verify shaft / locating / mounting interface  
-> confirm assembly length  
-> release configuration-matched drawing / CAD  
-> sample validation  
-> design freeze

## CAD and Sample

A simplified public **42P 4-stage STEP reference** is released for early packaging and mechanical Design-In. The detailed 42P full-assembly STEP remains configuration-controlled engineering CAD.

[Download 42P Simplified STEP - 4-Stage Reference](../../assets/downloads/42p/42P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

For final CAD, provide the selected ratio / stage count and motor interface.

[Request Motor + 42P Matching](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

[Open 42P Design-In Pack](design-in-pack.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

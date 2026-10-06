---
title: CPM-100-25 Dual Encoder Variant | SG2556D Controlled Drawing Reference | SigGear
description: Controlled-drawing reference for the CPM-100-25 dual-encoder variant, internally identified as SG2556D, with its separate envelope and operating values.
---

# CPM-100-25 Dual Encoder Variant v1.0

**Status:** Controlled-configuration engineering reference  
**Release date:** 2026-10-06

SigGear has confirmed that the controlled drawing internally identified as **SG2556D** represents the **CPM-100-25 dual-encoder variant**.

This variant must be kept separate from the current base CPM-100-25 public configuration because its axial package, weight and several operating values are different.

## Controlled Drawing Values

| Parameter | Dual-encoder variant |
| --- | --- |
| Product family | CPM-100-25 |
| Internal drawing / configuration code | SG2556D |
| Maximum outer diameter | 100 mm |
| Overall axial dimension | 48 mm |
| Rated voltage | DC 48V |
| Rated output speed | 60 RPM |
| Rated output torque | 25 Nm |
| No-load output speed | 125±10% RPM |
| No-load current | 1.1 A |
| Weight | 853 g |

## Do Not Mix With the Base Public Configuration

The current base CPM-100-25 public datasheet lists a different package and weight.

For this reason:

- **29.5 mm / 630 g** remains the base public CPM-100-25 configuration.
- **48 mm / 853 g** belongs to the confirmed dual-encoder SG2556D variant.
- No-load speed and other configuration-dependent values must be read from the matching controlled drawing.
- Peak torque, backlash, load ratings, driver details and communication functions are not automatically copied from the base configuration unless separately confirmed for the dual-encoder order.

## Mechanical Design-In

The controlled SG2556D drawing defines the mounting and output-interface geometry for this dual-encoder configuration.

The full drawing is not published as a manufacturing drawing on this website. Final design-in should use the configuration-matched controlled PDF and CAD supplied for the project.

## CAD Boundary

A CPM-100-25 assembly STEP has been supplied internally, but the exact configuration must be matched before release to a customer.

No full assembly STEP is published here as a public download.

[Request Dual-Encoder Drawing / CAD](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Resources

[CPM-100-25 Technical Datasheet](datasheet.md){ .md-button }
[CPM-100-25 Mechanical Interface](mechanical-interface.md){ .md-button }
[CPM-100-25 Product Page](../../products/cycloidal-joint-modules/cpm100-25.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

---
title: Design-In Checklist | SigGear Robot Actuators and Gearboxes
description: Engineering checklist for moving a SigGear actuator or gearbox from sample evaluation into a prototype, BOM or design freeze.
---

# Design-In Checklist

Use this checklist when a SigGear product has passed preliminary evaluation and is being considered for the customer's prototype, BOM or design freeze.

The purpose is to prevent a sample configuration from being copied into a final design without confirming the exact mechanical, electrical and operating conditions.

## 1. Product Identity

Confirm:

- exact model
- reduction ratio / stage count
- driver or no-driver configuration
- encoder / sensor configuration where applicable
- motor configuration for gearbox-only or matched motor + gearbox assemblies
- cable / connector configuration where applicable

## 2. Mechanical Interface

Confirm against the applicable controlled information:

- overall envelope
- mounting-hole pattern
- locating diameter / pilot
- output shaft or output flange
- key / spline / pinion definition where applicable
- motor-side interface
- cable / connector clearance
- required assembly direction
- radial and axial load direction

A public simplified STEP is intended for early packaging and mounting evaluation. Use the controlled configuration drawing for final tooling or production release.

## 3. Operating Point

Confirm the actual application requirement:

- continuous torque
- momentary / peak torque
- peak duration
- output speed
- acceleration and deceleration
- motion cycle
- duty cycle
- ambient temperature
- cooling condition
- external radial / axial loads
- backlash or positioning requirement where relevant

Do not base final selection only on a single peak-torque or no-load-speed value.

## 4. Electrical and Control Configuration

For motorized or driver-equipped products, confirm:

- operating voltage
- current limits
- driver version
- encoder configuration
- communication interface
- control mode
- firmware / protocol revision where relevant
- power-off behavior
- brake requirement if applicable

Detailed control documentation should match the ordered driver and firmware configuration.

## 5. Sample Test Outcome

Record what the sample actually demonstrated.

Useful evidence includes:

- mechanical fit confirmed
- first power-up / communication confirmed
- no-load motion confirmed
- representative load test completed
- temperature behavior reviewed where relevant
- observed noise / vibration reviewed where relevant
- faults or integration issues resolved
- remaining risks or assumptions documented

## 6. Configuration Freeze

Before releasing the next prototype or pilot build, confirm:

- exact product configuration
- controlled drawing revision
- agreed customized features, if any
- motor / gearbox / driver combination
- cable and connector definition
- software / protocol version where applicable
- prototype or pilot quantity

If a later hardware or firmware revision is introduced, re-check the affected interface rather than assuming it is identical to the sample.

## 7. Production and Change-Control Inputs

For a project moving beyond prototype, discuss:

- expected pilot quantity
- expected annual volume
- target schedule
- critical inspection requirements
- labeling / packaging requirements if relevant
- change-notification expectations
- any project-specific quality documentation

Availability and scope depend on the selected product and project requirements.

## Design-In Gate

Before treating a product as design-in ready, the project should be able to answer:

1. **Which exact SigGear configuration is being designed in?**
2. **Which controlled drawing or interface definition is being used?**
3. **Which operating condition was validated by the sample?**
4. **Which driver / firmware / communication configuration applies?**
5. **What still needs confirmation before the next build?**

If any of these remain unclear, keep the project in engineering evaluation rather than freezing the design.

## Engineering Resources

[Open the Engineering Center](index.md){ .md-button .md-button--primary }
[Open the Sample Validation Workflow](sample-validation-workflow.md){ .md-button }
[Request CAD, Sample and Quote](../request-cad-sample-quote.md){ .md-button }

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)


## From Design-In to Pilot and Production

A completed Design-In review should lead to a controlled configuration that can be evaluated for pilot preparation. Before production release, confirm the drawing revision, exact configuration, operating conditions, inspection requirements and any project-specific manufacturing or documentation requirements.

[Prototype → Design-In → Production](../custom-engineering/prototype-to-production.md){ .md-button .md-button--primary }

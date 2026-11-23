---
title: Planetary vs Cycloidal Reducer for Robot Joints | SigGear
description: Compare planetary and cycloidal reducer architectures for robot joints by torque, speed, ratio, packaging, backlash, external loads, efficiency, thermal behavior and control integration.
---

# Planetary vs Cycloidal Reducer for Robot Joints

There is no universal rule that makes a planetary or cycloidal reducer the better choice for every robot joint. The correct architecture depends on the complete joint requirement: torque, speed, ratio, size, external loads, backlash target, thermal condition, backdrivability, motor selection, encoder / driver architecture and prototype constraints.

SigGear publishes both [planetary robot joint actuators](../products/robot-joint-actuators/index.md) and [cycloidal joint modules](../products/cycloidal-joint-modules/index.md). The comparison below is an engineering screening guide, not a substitute for configuration-specific validation.

## Quick Comparison

| Engineering question | Planetary architecture | Cycloidal architecture |
| --- | --- | --- |
| Transmission layout | Coaxial multi-gear planetary stages | Eccentric cycloidal reduction with output mechanism |
| Ratio strategy | Ratio depends on stage count and available gear combinations | Ratio depends on the cycloidal mechanism and selected design |
| Torque density | Depends strongly on frame size, stages, materials and bearings | Can be attractive where high reduction and compact joint packaging are required |
| Backlash | Must be checked for the exact gearhead or actuator configuration | Must be checked for the exact cycloidal module and preload / assembly condition |
| Efficiency | Depends on ratio, stage count, speed, lubrication and load | Depends on reduction mechanism, bearings, contact conditions, speed and load |
| External loads | Check output bearing and housing ratings | Check output bearing and housing ratings |
| Backdrivability | Configuration-dependent | Configuration-dependent |
| Noise / vibration | Depends on gear geometry, speed, load and assembly | Depends on eccentric mechanism, bearings, speed, load and assembly |
| Motor / driver integration | Can be gearbox-only, motor + gearbox, or integrated actuator | Can be reducer-centered or integrated joint module depending on the platform |

Do not select a transmission architecture from one row alone.

## When a Planetary Solution Is Worth Evaluating

A planetary solution may be a practical starting point when the project needs:

- a coaxial compact transmission
- a wide choice of frame sizes and ratios
- a gearbox-only solution for an existing motor
- a motor + gearhead assembly
- an integrated actuator based on a planetary transmission
- a small-diameter transmission for hands, grippers, instruments or compact axes

SigGear publishes 8P through 42P planetary gearhead platforms and separate planetary robot-joint actuator references.

[Browse 8–42 mm Planetary Gearheads](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }
[Browse Planetary Robot Joint Actuators](../products/robot-joint-actuators/index.md){ .md-button }

## When a Cycloidal Solution Is Worth Evaluating

A cycloidal solution may be worth evaluating when the project architecture favors:

- high reduction in a compact joint arrangement
- a dedicated joint-module structure
- a different load path from a conventional multi-stage planetary gearbox
- a robot-joint package where the reducer, bearings, motor and electronics are reviewed together

SigGear currently publishes CPM-78-39, CPM-80-25 and CPM-100-25 as cycloidal joint-module references. Their specifications belong to the listed configurations only.

[Browse Cycloidal Joint Modules](../products/cycloidal-joint-modules/index.md){ .md-button .md-button--primary }

## What to Compare Before Choosing

### 1. Continuous and Peak Torque

Define continuous torque, peak torque, peak duration and repetition. Do not compare one supplier's continuous rating with another supplier's short-duration peak value.

### 2. Output Speed

Confirm rated and maximum output speed at the required torque. Maximum torque and maximum speed may not be available at the same operating point.

### 3. Installation Envelope

Compare the complete installed diameter, thickness, motor length, output interface, connectors, driver space and cable bend radius.

### 4. External Loads

A robot joint can apply radial, axial and overturning loads in addition to output torque. Check the complete bearing and housing arrangement rather than only the reducer torque rating.

### 5. Backlash, Accuracy and Repeatability

These are different specifications. Use the exact published or confirmed value for the selected configuration and test method.

### 6. Backdrivability and Holding Behavior

Backdrivability depends on ratio, friction, preload, motor cogging, brake state, lubrication and the complete mechanism. It should be tested in the actual or representative joint.

### 7. Thermal and Duty Cycle

Define continuous motion, holding time, peak events, rest time, ambient temperature and cooling path. Joint packaging can strongly affect thermal behavior.

### 8. Encoder, Driver and Communication

Confirm whether the project requires motor commutation feedback, output position feedback, integrated driver, external driver, CAN, RS485, EtherCAT or another interface. These functions are model- and configuration-specific.

## SigGear Public Reference Platforms

For planetary joint evaluation, start with the [planetary actuator product table](../products/robot-joint-actuators/index.md).

For cycloidal joint evaluation, start with the [cycloidal joint-module product table](../products/cycloidal-joint-modules/index.md).

Public PDF datasheets, available 2D references and STEP files for the standard joint-module set are collected here:

[Robot Joint Datasheets & CAD Downloads](../engineering-resources/robot-joint-actuators/quick-downloads.md){ .md-button .md-button--primary }

## What to Send for an Architecture Review

Provide the information already available:

1. robot type and joint position
2. continuous torque
3. peak torque and peak duration
4. rated and maximum output speed
5. maximum diameter and thickness
6. radial / axial / overturning loads if known
7. voltage and controller current limits
8. encoder and communication requirement
9. brake or power-off requirement
10. prototype quantity and expected production volume

If several items are still unknown, send the mechanism, CAD screenshot or joint concept first.

[Robot Joint Actuator Selection Guide](robot-joint-actuator-selection-guide.md){ .md-button }
[Custom Robot Joint Development](../custom-engineering/robot-joint-actuator-development.md){ .md-button }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }

**Contact:** Wanrong Wang · International Sales / Sales Engineer, SigGear · luffy@siggear.com

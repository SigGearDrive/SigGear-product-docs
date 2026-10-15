---
title: SigGear Planetary Gearbox Selector | 8–42 mm Engineering Selection
description: Preliminary 8–42 mm planetary gearbox selection by motor speed, target output speed, published ratio, stage, gearbox length, rated torque, datasheet and CAD.
---

# How to Select a Miniature Planetary Gearbox for an OEM Design

A miniature planetary gearbox, also called a planetary gearhead, should be selected from its **output load, motor operating point, duty cycle and installation interface**, not the diameter or maximum reduction ratio alone.

This engineering guide links to SigGear's 8–42 mm standard gearbox range. It does not represent a tested application or a claim that any configuration suits every mechanism.

[Compare 8–42 mm Planetary Gearboxes](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }
[Browse Simplified STEP CAD](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button }

## Browse by Diameter Before Ratio Selection

If the mechanical envelope is already known, start from the exact gearbox diameter and then check stage-dependent length, ratio, torque and motor interface:

[8 mm planetary gearbox](../products/planetary-gearboxes/8p-planetary-gearbox.md) · [10 mm](../products/planetary-gearboxes/10p-planetary-gearbox.md) · [12 mm](../products/planetary-gearboxes/12p-planetary-gearbox.md) · [14 mm](../products/planetary-gearboxes/14p-planetary-gearbox.md) · [16 mm](../products/planetary-gearboxes/16p-planetary-gearbox.md) · [20 mm](../products/planetary-gearboxes/20p-planetary-gearbox.md) · [22 mm](../products/planetary-gearboxes/22p-planetary-gearbox.md) · [24 mm](../products/planetary-gearboxes/24p-planetary-gearbox.md) · [28 mm](../products/planetary-gearboxes/28p-planetary-gearbox.md) · [32 mm](../products/planetary-gearboxes/32p-planetary-gearbox.md) · [36 mm](../products/planetary-gearboxes/36p-planetary-gearbox.md) · [42 mm](../products/planetary-gearboxes/42p-planetary-gearbox.md)

Diameter is only the first filter. Final selection still requires the exact ratio/stage, rated load, shaft loading, duty cycle and motor interface.

## 1. Decide What Needs to Be Supplied

**Gearbox only:** If you already have a motor, provide its model or drawing, operating shaft speed, shaft dimensions, mounting-hole pattern, locating pilot, available axial space and required output. Motor-to-gearbox interface and operating compatibility require review.

**Motor + gearbox assembly:** If the motor has not been selected, provide the power supply, desired output motion, load or torque, available diameter and total length, and operating cycle. SigGear can evaluate a **motor with planetary gearbox** as a complete matched assembly.

[Open Motor + Planetary Gearbox Integration Guide](../custom-engineering/motor-gearbox-integration.md){ .md-button }

## 2. Estimate the Reduction Ratio From Loaded Speed

The preliminary reduction ratio is approximately **motor speed at the operating point divided by target gearbox output speed**. Do not automatically use the motor's no-load speed.

Compare this result with the published stage-specific ratio table of the selected gearbox. Different stages can change overall body length, torque rating and efficiency.

## SigGear Planetary Gearbox Selector {#preliminary-ratio-stage-finder}

Use this tool for an initial comparison when you know the **motor operating speed** and **target gearbox output speed**.

**What you enter:** motor operating speed and target output speed; optionally maximum gearbox diameter, maximum gearbox body length, required continuous torque, peak torque and maximum ratio difference.

**What you get:** the closest published ratio, the smallest surviving frame and the shortest surviving gearbox among published configurations that satisfy the entered catalog filters. Requests outside the published limits can be submitted for engineering assessment.

It calculates:

**preliminary target ratio = motor operating speed / target output speed**

and compares that value with the currently published 1–4 stage ratios for SigGear 8P–42P.

Optional filters can remove configurations that exceed a maximum gearbox diameter, maximum **gearbox body length**, published **rated allowable torque** requirement, a **maximum momentary torque** screening threshold, or a user-defined maximum ratio difference. Exceeding a catalog limit does not rule out a customized solution; the results provide a custom engineering review path.

<form id="siggear-ratio-stage-selector" class="siggear-ratio-selector">
  <div class="siggear-selector-grid">
    <label>
      Motor operating speed (rpm)
      <input id="sg-selector-motor-speed" type="number" min="0.01" step="any" required placeholder="Example: 12000">
    </label>

    <label>
      Target output speed (rpm)
      <input id="sg-selector-output-speed" type="number" min="0.01" step="any" required placeholder="Example: 80">
    </label>

    <label>
      Maximum gearbox diameter (mm) — optional
      <input id="sg-selector-diameter" type="number" min="0.01" step="any" placeholder="Example: 32">
    </label>

    <label>
      Maximum gearbox body length (mm) — optional
      <input id="sg-selector-length" type="number" min="0.01" step="any" placeholder="Gearbox only, not total motor + gearbox length">
    </label>

    <label>
      Required continuous output torque — optional
      <input id="sg-selector-torque" type="number" min="0" step="any" placeholder="Compared with published rated allowable torque">
    </label>
    <label>
      Torque unit
      <select id="sg-selector-torque-unit" aria-label="Torque unit">
        <option value="nm">N·m</option>
        <option value="kgfcm">kgf·cm</option>
      </select>
    </label>
    <label>
      Required peak output torque — optional, preliminary screen
      <input id="sg-selector-peak-torque" type="number" min="0" step="any" placeholder="Peak load; duration and frequency require engineering review">
    </label>

    <label>
      Maximum ratio difference (%) — optional
      <input id="sg-selector-ratio-tolerance" type="number" min="0" step="any" placeholder="Example: 5 means keep ratios within 5%">
    </label>
  </div>

  <div class="siggear-selector-actions">
    <button type="submit" class="md-button md-button--primary">Find Published Configurations</button>
  </div>

  <p id="sg-ratio-stage-summary" class="siggear-selector-summary" aria-live="polite"></p>
  <div id="sg-ratio-stage-results" aria-live="polite"></div>
</form>

**Continuous input-speed range — engineering confirmed 15 October 2026:** SigGear's 8P–42P planetary gearbox series supports **1,000–20,000 rpm continuous input speed** for preliminary standard-configuration selection, superseding the earlier published 8,000 rpm upper limit. Input speeds **below 1,000 rpm** or **above 20,000 rpm** are directed to **custom feasibility assessment**. The exact motor, ratio, duty cycle, thermal behavior, torque, and installation interface still require application-specific engineering review.

**Torque and efficiency rules:** published stage-specific rated allowable torque may be used for preliminary continuous-load screening; published maximum momentary torque may be used to rule out unsuitable peak-load candidates but does **not** establish an allowable peak duration or frequency. Exceeding either published torque threshold can be reviewed for customization. Published efficiency is a **stage-level reference**: ratio-specific differences are awaiting separate engineering verification. The tool does not infer motor suitability, safe peak duration, thermal behavior, service life or final design approval.

**Important:** this is a preliminary Design-In aid, not an automatic final selector. It does not add a safety factor, calculate motor shaft torque, predict service life, or prove that a customer's motor shaft / pilot / mounting pattern fits the gearbox.

The results now separate three different first-check questions:

- **Closest Ratio** — the remaining published configuration with the smallest ratio difference.
- **Smallest Surviving Frame** — the smallest diameter that still has at least one published configuration after your active filters.
- **Shortest Surviving Gearbox** — the shortest published gearbox body among the remaining frame candidates.

These labels are not interchangeable and are **not final recommendations**. A smaller frame may have a less suitable ratio, and a shorter gearbox may have lower published rated torque. Confirm the selected **model + stage + ratio + continuous / peak load + motor interface** against the Datasheet and Mechanical Interface.

[Existing Motor — Open Motor-Matching Workflow](../custom-engineering/motor-gearbox-integration.md){ .md-button }
[Open 8P–42P Datasheets & Mechanical Interfaces](../engineering-resources/planetary-gearboxes/index.md){ .md-button }

## 3. Compare Continuous and Peak Torque Separately

- **Normal running:** Compare required continuous operating torque with the exact configuration's rated allowable torque, considering cycle and necessary margin.
- **Cutting, startup, impact or jam events:** Consider magnitude, duration and frequency of peak loads. The published maximum momentary torque is **not** a continuous rating.
- **Motor matching:** Output torque estimates depend on the motor shaft torque, selected ratio and the relevant gearbox efficiency. Use the efficiency published for the selected configuration, not a family maximum.

Never transfer a torque rating from one frame size or stage configuration to another without technical confirmation. If published torque, ratio, or envelope filters produce no catalog match, use **Request Custom Engineering Review** on the results page and attach the application / motor drawing. A successful preliminary match still needs review of actual operating conditions.

## 4. Check the Full Mechanical Interface

Measure the gearbox outer diameter, **stage-dependent body length**, output shaft, flange, mounting holes and motor-side shaft interface. Total motor-plus-gearbox assembly length is not the same as gearbox body length.

Output torque and shaft loads are different constraints. Review radial and axial forces, their application point and whether the mechanism needs an external bearing to support pulleys, pinions, cranks or other cantilevered loads.

[Open Datasheets and Mechanical Interface References](../engineering-resources/planetary-gearboxes/index.md){ .md-button }

## 5. Validate Backlash, Holding, Noise and Environment

A published gearbox backlash value is not a claim of zero backlash or final-system positioning accuracy. Do not assume a planetary gearbox is self-locking. If the design needs power-off holding, check brake and full-mechanism requirements.

Service life, sound level, ingress protection and corrosion resistance must be confirmed for the selected configuration and operating environment; do not infer unlisted ratings.

## 6. Use the Correct CAD

Public SigGear **simplified 4-stage STEP references** are available for 8P, 10P, 12P, 14P, 16P, 20P, 22P, 24P, 28P, 32P, 36P and 42P. They support preliminary external space and mounting checks while omitting internal planetary mechanism detail.

A 4-stage CAD reference is **not interchangeable** with a 1-, 2- or 3-stage configuration. For final Design-In, request the exact ratio/stage drawing and motor interface revision.

[Download Public 4-Stage STEP Models](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button .md-button--primary }

## Application-Specific Engineering Questions

An [electric pruning-shear gearbox](../applications/electric-pruning-shears-planetary-gearbox.md) must be reviewed for blade geometry, cutting force variation, torque spikes and outdoor exposure. An [electric curtain gearmotor](../applications/electric-curtain-blind-window-opener-gear-motors.md) needs track friction, pulley speed, acoustic, holding and safety reviews. A [smart toilet or bidet mechanism](../applications/smart-toilet-bidet-planetary-gear-motors.md) adds low-noise, jam, humidity and cleaning-environment requirements. A [dexterous hand or robot gripper](../applications/robot-gripper-gear-motors.md) requires finger-force or tendon-spool geometry, shaft-load and packaging review.

A [smart lock or access-control mechanism](../applications/access-control-smart-lock-security-gear-motors.md) adds bolt or latch preload, battery-current, jam and power-off requirements. [Pump, valve and dosing mechanisms](../applications/pump-valve-fluid-control-gear-motors.md) require pressure, seal friction, duty-cycle and feedback review. [Camera focus, zoom and sensor-positioning mechanisms](../applications/optical-imaging-camera-module-gear-motors.md) add backlash, vibration and repeatability constraints. [Coffee, beverage and dispensing equipment](../applications/food-beverage-coffee-equipment-gear-motors.md) adds dosing, jam, cleaning-boundary and acoustic requirements.

These are potential engineering uses, not published customer case studies.

## What to Send for a First Review

| Item | Useful information |
| --- | --- |
| Motion | Output speed, stroke or rotation, duty cycle |
| Load | Continuous torque or mechanism geometry; peak event if known |
| Packaging | Diameter, total length, mounting and shaft |
| Existing motor | Model, drawing, shaft dimensions and loaded speed |
| Supply scope | Gearbox only or complete motor + gearbox |
| Project stage | Prototype quantity and forecast annual volume |

A motor drawing or mechanism sketch and the information already known are enough to start a preliminary review. Final configuration and performance require engineering confirmation.

**Wanrong Wang — SigGear**  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com?subject=Miniature%20Planetary%20Gearbox%20Selection)

[Request a Planetary Gearbox Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }

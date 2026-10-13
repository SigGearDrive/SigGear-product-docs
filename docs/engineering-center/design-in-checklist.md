---
title: Design-In Checklist | SigGear Robot Actuators and Gearboxes
description: Engineering checklist for moving a SigGear actuator or gearbox from sample evaluation into a prototype, BOM or design freeze.
---

# Design-In Checklist

Use this checklist when a SigGear product has passed preliminary evaluation and is being considered for the customer's prototype, BOM or design freeze.

The purpose is to prevent a sample configuration from being copied into a final design without confirming the exact mechanical, electrical and operating conditions.

## Planetary Design-In Review Decision

If you arrived from the Sample Validation Workflow with a validated 8P–42P planetary candidate, this panel rechecks the **model + stage + published ratio** and interprets only the normalized sample-validation status / outcome.

<div id="sg-design-in-review" class="siggear-design-in-review" hidden>
  <p id="sg-design-in-review-status">Checking the candidate and sample-review context...</p>

  <div id="sg-design-in-review-content" hidden>
    <div class="siggear-design-in-summary">
      <strong id="sg-design-in-candidate-name"></strong>
      <span id="sg-design-in-candidate-detail"></span>
    </div>

    <div class="siggear-design-in-decision">
      <strong>Automated preliminary decision</strong>
      <p id="sg-design-in-decision-status"></p>
      <p class="siggear-design-in-note">This automated status is only a workflow routing aid. It does not approve Design-In, freeze the design, approve pilot production or release the product for mass production.</p>
    </div>

    <div class="siggear-selector-table-wrap">
      <table>
        <thead>
          <tr>
            <th>Input</th>
            <th>Normalized value</th>
            <th>Meaning</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Candidate</td>
            <td id="sg-design-in-candidate-cell"></td>
            <td>Revalidated against current published ratio-stage data.</td>
          </tr>
          <tr>
            <td>Sample validation status</td>
            <td id="sg-design-in-sample-status"></td>
            <td>Standardized customer-side sample workflow result.</td>
          </tr>
          <tr>
            <td>Engineering outcome</td>
            <td id="sg-design-in-sample-outcome"></td>
            <td>Standardized next-direction selected in the sample workflow.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>Manual Engineering Milestones</h3>

    <div class="siggear-manual-milestones">
      <div>
        <strong>Design Frozen — Human confirmation required</strong>
        <p>Do not treat the design as frozen until the exact configuration, controlled drawing revision, validated operating point, applicable motor / driver / firmware configuration and remaining risks have been reviewed and confirmed by the responsible engineering / project teams.</p>
      </div>
      <div>
        <strong>Pilot Preparation Ready — Human confirmation required</strong>
        <p>Do not treat the project as pilot-ready until Design Freeze has been confirmed and the pilot quantity, schedule, inspection requirements, change-control expectations and project-specific documentation needs have been agreed.</p>
      </div>
    </div>

    <div class="siggear-form-actions">
      <button type="button" id="sg-design-in-email" class="md-button md-button--primary">Prepare Design-In Review Email</button>
      <a id="sg-design-in-datasheet" class="md-button" href="#">Open Datasheet</a>
      <a id="sg-design-in-interface" class="md-button" href="#">Open Mechanical Interface</a>
      <a class="md-button" href="../custom-engineering/prototype-to-production/">Prototype → Pilot → Production</a>
    </div>

    <p id="sg-design-in-action-status" class="siggear-form-status" aria-live="polite"></p>
  </div>
</div>

The Design-In decision panel does not receive the customer's free-text test notes, measured torque / speed / temperature values or other private validation details through the URL.

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

A Sample Validation Workflow status of **Ready to Submit for Design-In Review** means the recorded sample steps are complete enough to submit for engineering review. It does **not** mean the configuration is already Design-In approved, frozen or production released.

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

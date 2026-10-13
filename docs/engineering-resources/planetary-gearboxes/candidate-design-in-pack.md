---
title: Planetary Gearbox Candidate Design-In Pack | Stage-Specific CAD Boundary | SigGear
description: Review a validated SigGear 8P–42P planetary gearbox candidate by model, stage and published ratio, with Datasheet, Mechanical Interface, public 4-stage STEP boundary and controlled configuration CAD request path.
---

# Planetary Gearbox Candidate Design-In Pack

Use this page after the SigGear Ratio & Stage Selection Tool has narrowed the project to a published **model + stage + ratio** candidate.

This page does **not** convert the public 4-stage STEP into stage-specific production CAD. It rechecks the candidate against the current published ratio-stage data and explains which resources can be used for preliminary Design-In.

<div id="sg-candidate-pack" class="siggear-candidate-pack">
  <p id="sg-candidate-pack-status">Checking the candidate against current published data...</p>

  <div id="sg-candidate-pack-content" hidden>
    <div class="siggear-candidate-pack-summary">
      <strong id="sg-pack-candidate-name"></strong>
      <span id="sg-pack-candidate-detail"></span>
    </div>

    <h2>Validated Published Candidate</h2>

    <div class="siggear-selector-table-wrap">
      <table>
        <thead>
          <tr>
            <th>Model</th>
            <th>Diameter</th>
            <th>Stage</th>
            <th>Published ratio</th>
            <th>Gearbox body length</th>
            <th>Rated allowable torque</th>
            <th>Maximum momentary torque</th>
            <th>Efficiency</th>
          </tr>
        </thead>
        <tbody id="sg-pack-candidate-row"></tbody>
      </table>
    </div>

    <h2>CAD Status for This Candidate</h2>

    <div id="sg-pack-cad-boundary" class="siggear-cad-boundary"></div>

    <div class="siggear-form-actions">
      <a id="sg-pack-datasheet" class="md-button md-button--primary" href="#">Open Datasheet</a>
      <a id="sg-pack-interface" class="md-button" href="#">Open Mechanical Interface</a>
      <a id="sg-pack-public-step" class="md-button" href="#">Open Public 4-Stage STEP</a>
      <a id="sg-pack-project-brief" class="md-button" href="#">Request Controlled CAD / Engineering Review</a>
      <a id="sg-pack-dedicated" class="md-button" href="#" hidden>Open Dedicated Model Design-In Pack</a>
    </div>

    <h2>What Each Resource Is For</h2>

    <table>
      <thead>
        <tr>
          <th>Resource</th>
          <th>Use it for</th>
          <th>Do not assume</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Datasheet</td>
          <td>Published stage count, ratio, gearbox body length, torque and efficiency references.</td>
          <td>That the candidate is suitable without checking motor operating point, duty cycle and external loads.</td>
        </tr>
        <tr>
          <td>Mechanical Interface</td>
          <td>Public mounting, shaft and stage-dependent envelope references from the controlled drawing.</td>
          <td>That every final tolerance or customer-specific motor adapter is already released.</td>
        </tr>
        <tr>
          <td>Public STEP</td>
          <td>Frame-level external-interface review using the released simplified 4-stage reference.</td>
          <td>That it represents a 1-, 2- or 3-stage candidate, or that it is final production CAD.</td>
        </tr>
        <tr>
          <td>Controlled configuration CAD / drawing</td>
          <td>Exact selected stage / ratio / interface review before design freeze, tooling or production release.</td>
          <td>Availability before SigGear confirms the project configuration.</td>
        </tr>
      </tbody>
    </table>

    <h2>Controlled CAD Review Readiness</h2>

    Before treating a configuration-specific CAD request as ready for engineering review, the Project Brief checks five items:

    1. **Candidate configuration** — validated model + stage + published ratio.
    2. **Motor / drive-side interface** — existing motor drawing / model, shaft and mounting reference, or a drive-side configuration confirmed by SigGear.
    3. **Output interface** — required shaft, keyway, flange or mounting arrangement.
    4. **Load / duty** — continuous / peak load information and duty cycle / peak duration.
    5. **Installation envelope** — maximum diameter and/or length constraint.

    [Check CAD Review Readiness / Request Controlled CAD](../../../request-cad-sample-quote.md?next_step=cad_review){ .md-button .md-button--primary }

    **Ready for CAD Review** means enough information is present for SigGear engineering to begin a configuration-specific review. It does **not** mean controlled CAD has already been approved or released.

    <h2>Before Design Freeze</h2>

    Confirm at minimum:

    - selected model, stage and ratio
    - exact gearbox body length
    - motor operating speed and duty cycle
    - continuous and peak load
    - radial / axial shaft loads where relevant
    - motor shaft, pilot and mounting interface
    - output interface
    - controlled CAD / drawing revision
    - sample validation in the actual application

    <p>The candidate shown here remains a <strong>preliminary Design-In candidate</strong> until SigGear engineering confirms the exact configuration.</p>
  </div>
</div>

## Public CAD Boundary for the 8P–42P Series

All currently released public STEP files in the standard 8P–42P planetary gearbox series are simplified **4-stage references**.

For a selected **1-, 2- or 3-stage** configuration, the public STEP has a different gearbox body length and must **not** be treated as the exact selected-stage envelope.

For a selected **4-stage** configuration, the public STEP matches the published stage count and can support preliminary external packaging review, but it still remains a simplified public reference rather than ratio-specific production CAD.

[Open 8P–42P Public CAD Release](public-cad-release-v1.md){ .md-button }

[Open Planetary Engineering Resource Library](index.md){ .md-button }

[Open Ratio & Stage Selection Guide](../../selection-guides/miniature-planetary-gearbox-selection-guide.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

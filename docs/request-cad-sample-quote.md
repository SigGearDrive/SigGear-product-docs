---
title: Request CAD, Sample and Quote for SigGear Products
description: Request CAD, STEP files, engineering review, samples and quotations for SigGear robot joint actuators, cycloidal modules, planetary gearboxes and gear motors.
---

# Request CAD, Sample and Quote

Use this page when you need help moving from a product page to an engineering decision: model matching, CAD review, a sample, configuration-specific documentation or quotation preparation.

If you already know the model, include it. If you do not, send the application and the parameters you know — a complete specification is not required for the first review.

For a project that starts from an idea, existing motor, mechanism or custom transmission problem, see the [Custom Precision Transmission Engineering](custom-engineering/index.md) page first.

If the project specifically needs a miniature or compact planetary gearbox, see [Custom Planetary Gearbox Engineering](custom-engineering/custom-planetary-gearbox.md).

If the project involves a compact high-torque joint or a possible cycloidal structure, see [Custom Cycloidal Transmission Engineering](custom-engineering/custom-cycloidal-transmission.md).

If the project starts from an existing motor or needs a complete motor + gearbox solution, see [Motor + Gearbox Integration Engineering](custom-engineering/motor-gearbox-integration.md).

If the project is a robot joint, compact actuator or AI-hardware rotary axis with custom torque, speed, size, sensing or control requirements, see [Custom Robot Joint & Compact Actuator Development](custom-engineering/robot-joint-actuator-development.md).

If the project has moved beyond a first concept and needs a structured path through prototype, testing, Design-In, pilot preparation and production release, see [Prototype to Design-In and Production](custom-engineering/prototype-to-production.md).

## Miniature Planetary Gearbox (8–42 mm) — Choose Your Path

### Path A: Gearbox Only for an Existing Motor

Choose this path when the motor is already selected and you need SigGear to review a compatible planetary gearbox.

For the first review, send only what you already know:

1. **Motor model or drawing**
2. **Motor speed**
3. **Motor shaft diameter / usable shaft length**
4. **Motor mounting pattern / locating pilot**
5. **Required output speed or ratio**
6. **Maximum gearbox / assembly diameter and length**
7. **Load or torque, if known**

If torque or an interface dimension is not known, a motor drawing or mechanism sketch is enough to start.

[Start Gearbox-Only Project Brief](?path=gearbox_only){ .md-button .md-button--primary }

### Path B: Complete Motor + Gearbox Assembly

Choose this path when the motor is still open and you want SigGear to evaluate the drive as one system.

For the first review, send:

1. **Application / what needs to move**
2. **Required output speed**
3. **Load or torque, if known**
4. **Maximum diameter and total length**
5. **Operating voltage**

The final ratio does not need to be calculated before contacting us.

[Start Motor + Gearbox Project Brief](?path=motor_gearbox){ .md-button .md-button--primary }

You do not need a complete specification to start. Missing technical details can be narrowed after the first review.

[Browse 8–42 mm Planetary Gearboxes](products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button }
[View Public Simplified 4-Stage STEP Files](engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }

### Start From the Application

If your project matches one of the current priority application paths, use the dedicated review link so the first email already contains the minimum engineering fields.

[Pruning Shears Review](mailto:wangwanrong@siggear.com?subject=Electric%20Pruning%20Shears%20Planetary%20Gearbox%20Review){ .md-button }
[Electric Curtain / Blind Review](mailto:wangwanrong@siggear.com?subject=Electric%20Curtain%20Blind%20Planetary%20Gear%20Motor%20Review){ .md-button }
[Smart Toilet / Bidet Review](mailto:wangwanrong@siggear.com?subject=Smart%20Toilet%20Bidet%20Planetary%20Gear%20Motor%20Review){ .md-button }
[Dexterous Hand / Gripper Review](mailto:wangwanrong@siggear.com?subject=Dexterous%20Hand%20Robot%20Gripper%20Planetary%20Gearbox%20Review){ .md-button }



## Engineering Project Brief

If you do not want to write a technical inquiry from scratch, use this short project brief. Fill in only what you already know.

This page does **not** send your engineering details to a third-party form service. **Prepare Email to SigGear** opens your local email client with a structured draft addressed to Wanrong Wang. You can attach motor drawings, mechanism sketches, CAD screenshots or other project files before sending.

<form id="siggear-engineering-brief" class="siggear-inquiry-form">
  <div class="siggear-form-grid">
    <label>
      SigGear model reference
      <select id="sg-model" name="model">
        <option value="">Not sure yet</option>
        <option value="8P">8P — 8 mm</option>
        <option value="10P">10P — 10 mm</option>
        <option value="12P">12P — 12 mm</option>
        <option value="14P">14P — 14 mm</option>
        <option value="16P">16P — 16 mm</option>
        <option value="20P">20P — 20 mm</option>
        <option value="22P">22P — 22 mm</option>
        <option value="24P">24P — 24 mm</option>
        <option value="28P">28P — 28 mm</option>
        <option value="32P">32P — 32 mm</option>
        <option value="36P">36P — 36 mm</option>
        <option value="42P">42P — 42 mm</option>
      </select>
    </label>

    <label>
      Project path
      <select id="sg-path" name="path">
        <option value="not_sure">Not sure — please recommend</option>
        <option value="gearbox_only">Gearbox only — I already have a motor</option>
        <option value="motor_gearbox">Complete motor + gearbox assembly</option>
      </select>
    </label>
  </div>

  <div id="sg-selector-candidate" class="siggear-selector-candidate" hidden>
    <strong>Preliminary candidate from SigGear Selection Tool</strong>
    <p id="sg-selector-candidate-summary"></p>
    <p class="siggear-selector-candidate-note">This candidate is rechecked against the current published ratio-stage data before it is included in your project brief. It is not a final engineering selection.</p>
    <input id="sg-selector-candidate-stage" name="selector_candidate_stage" type="hidden">
    <input id="sg-selector-candidate-ratio" name="selector_candidate_ratio" type="hidden">
  </div>

  <label>
    Application / what needs to move
    <textarea id="sg-application" name="application" rows="3" required placeholder="Example: compact curtain drive, robotic gripper, optical adjustment mechanism..."></textarea>
  </label>

  <div id="sg-existing-motor-fields">
    <div class="siggear-form-grid">
      <label>
        Existing motor model / drawing reference
        <input id="sg-motor-model" name="motor_model" type="text" placeholder="Motor model, supplier model or drawing reference">
      </label>

      <label>
        Motor speed
        <input id="sg-motor-speed" name="motor_speed" type="text" placeholder="Example: 12,000 rpm">
      </label>

      <label>
        Motor shaft / usable length
        <input id="sg-motor-shaft" name="motor_shaft" type="text" placeholder="Example: Ø8 mm shaft, 23 mm usable length">
      </label>

      <label>
        Motor mounting / locating pilot
        <input id="sg-motor-mount" name="motor_mount" type="text" placeholder="Hole pattern, pilot diameter, flange or drawing reference">
      </label>
    </div>
  </div>

  <div class="siggear-form-grid">
    <label>
      Required output speed or ratio
      <input id="sg-output" name="output" type="text" placeholder="Example: 35 rpm, or about 100:1">
    </label>

    <label>
      Load / torque, if known
      <input id="sg-load" name="load" type="text" placeholder="Continuous / peak torque or load description">
    </label>

    <label>
      Maximum diameter / length
      <input id="sg-size" name="size" type="text" placeholder="Example: Ø20 mm, total length < 45 mm">
    </label>

    <label id="sg-voltage-field">
      Operating voltage
      <input id="sg-voltage" name="voltage" type="text" placeholder="Example: 12 VDC">
    </label>

    <label>
      Output shaft / mounting requirement
      <input id="sg-output-interface" name="output_interface" type="text" placeholder="Shaft, keyway, flange, hole pattern or drawing reference">
    </label>

    <label>
      Duty cycle / peak duration
      <input id="sg-duty-cycle" name="duty_cycle" type="text" placeholder="Example: 10 s on / 20 s off, peak torque for 1 s">
    </label>

    <label>
      External shaft loads
      <input id="sg-shaft-loads" name="shaft_loads" type="text" placeholder="Radial / axial load if relevant, or write none / unknown">
    </label>
  </div>

  <div id="sg-cad-readiness" class="siggear-cad-readiness" hidden>
    <strong id="sg-cad-readiness-title">Controlled CAD review readiness</strong>
    <p id="sg-cad-readiness-status"></p>
    <ul id="sg-cad-readiness-gates"></ul>
    <p class="siggear-cad-readiness-note">“Ready for CAD Review” means the project brief contains enough information for SigGear engineering to begin a configuration-specific CAD review. It does not mean controlled CAD has been approved or released.</p>
  </div>

  <div class="siggear-form-grid">
    <label>
      Prototype quantity
      <input id="sg-prototype-qty" name="prototype_qty" type="text" placeholder="Example: 2 pcs">
    </label>

    <label>
      Estimated annual volume
      <input id="sg-annual-volume" name="annual_volume" type="text" placeholder="Optional">
    </label>

    <label>
      Company / country
      <input id="sg-company-country" name="company_country" type="text" placeholder="Optional">
    </label>

    <label>
      Project stage
      <select id="sg-project-stage" name="project_stage">
        <option value="">Not specified</option>
        <option value="concept">Concept</option>
        <option value="prototype">Prototype</option>
        <option value="pilot">Pilot</option>
        <option value="production">Production</option>
      </select>
    </label>

    <label>
      What do you need next?
      <select id="sg-next-step" name="next_step">
        <option value="Model recommendation">Model recommendation</option>
        <option value="CAD / STEP review">CAD / STEP review</option>
        <option value="Sample">Sample</option>
        <option value="Quotation">Quotation</option>
        <option value="Engineering review">Engineering review</option>
      </select>
    </label>
  </div>

  <div class="siggear-form-actions">
    <button type="submit" class="md-button md-button--primary">Prepare Email to SigGear</button>
    <button type="button" id="sg-copy-brief" class="md-button">Copy Project Brief</button>
  </div>

  <p id="sg-brief-status" class="siggear-form-status" aria-live="polite"></p>
</form>

A complete specification is not required. If torque, ratio or load is still unknown, describe the mechanism and attach a sketch or screenshot in the email.

## Minimum Information to Start

For a first engineering review, four items are usually enough:

1. **Application** — what is moving and where the gearbox / actuator will be installed
2. **Required output** — torque and speed if known
3. **Installation limit** — maximum diameter, length or a simple sketch if available
4. **What you need next** — model recommendation, CAD / STEP, drawing review, sample or quotation

If you do not know the reduction ratio, send the motor speed and desired output speed if available.

## Helpful Information When Available

The following helps narrow the configuration but does not need to be sent all at once:

- company name and country
- project stage: concept, prototype, pilot or production
- continuous and peak torque
- peak duration
- operating voltage
- motor information for gearbox-only projects
- output shaft / mounting requirement
- duty cycle and peak duration
- radial / axial load conditions
- driver, encoder and communication requirements
- prototype quantity and estimated annual volume
- delivery destination

A mechanism sketch with key dimensions is acceptable for the first review.

## What You Can Request

Depending on the selected product and project stage, SigGear can review requests for:

- preliminary model matching
- released public CAD / STEP resources
- configuration-specific CAD or controlled drawing review
- mechanical-interface review
- prototype sample evaluation
- motor + gearbox matching
- driver / encoder / communication review for applicable products
- quotation preparation

Technical files and final configuration details depend on the selected model and engineering review.

## Public Resources You Can Use Immediately

Before sending an inquiry, check whether the product already has a public Engineering Pack.

[Open the Engineering Center](engineering-center/index.md){ .md-button .md-button--primary }

Current public Engineering Resources cover:

- [SG-6010C](products/robot-joint-actuators/sg6010c.md)
- [SG-6010HB](products/robot-joint-actuators/sg6010hb.md)
- [SG-6010D](products/robot-joint-actuators/sg6010d.md)
- [SG-8021](products/robot-joint-actuators/sg8021.md)
- [CPM-78-39](products/cycloidal-joint-modules/cpm78-39.md)
- [CPM-80-25](products/cycloidal-joint-modules/cpm80-25.md)
- [CPM-100-25](products/cycloidal-joint-modules/cpm100-25.md)
- [8P-42P Planetary Gearbox Engineering Resource Library](engineering-resources/planetary-gearboxes/index.md), covering 8P, 10P, 12P, 14P, 16P, 20P, 22P, 24P, 28P, 32P, 36P and 42P

For the standard **8P–42P planetary gearbox series**, simplified public **4-stage STEP** references are released for all 12 frame sizes. Configuration-matched production CAD and controlled drawings still depend on the selected model, stage count, ratio and motor interface.

## Sample Evaluation

If you already have or plan to order a sample, use the evaluation workflow to separate mechanical fit, first setup, functional testing and application testing.

[Open the Sample Validation Workflow](engineering-center/sample-validation-workflow.md){ .md-button }

## Review Process

1. understand the application
2. identify the closest product / configuration
3. review the public or controlled engineering files needed for the decision
4. prepare the sample or quotation
5. support sample evaluation
6. confirm the configuration before Design-In

[Open the Design-In Checklist](engineering-center/design-in-checklist.md){ .md-button }

## Contact SigGear

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
Email: [wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

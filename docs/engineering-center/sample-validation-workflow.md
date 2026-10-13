---
title: Sample Validation Workflow | SigGear Actuators and Gearboxes
description: A practical sample-evaluation workflow for SigGear robot joint actuators, cycloidal modules and planetary gearboxes, from configuration confirmation to functional testing and design-in review.
---

# Sample Validation Workflow

The goal of a sample evaluation is not only to confirm that a product can rotate or transmit torque. It should also answer whether the selected configuration is suitable for the customer's mechanical, electrical and operating conditions.

This workflow is intended to make the first evaluation more structured and reduce avoidable setup delays.

## Planetary Candidate Sample Validation

If you arrived from a validated 8P–42P Candidate Design-In Pack, this panel rechecks the **model + stage + published ratio** before creating a sample-validation record.

<div id="sg-planetary-sample-validation" class="siggear-sample-validation" hidden>
  <p id="sg-sample-validation-status">Checking the planetary candidate against current published data...</p>

  <div id="sg-sample-validation-content" hidden>
    <div class="siggear-sample-candidate-summary">
      <strong id="sg-sample-candidate-name"></strong>
      <span id="sg-sample-candidate-detail"></span>
    </div>

    <p>This is a customer-side evaluation aid. A recorded “Pass” means the evaluator marked that step as acceptable in their test; it is not an independent SigGear certification or production approval.</p>

    <form id="sg-sample-validation-form">
      <div class="siggear-form-grid">
        <label>
          1. Configuration received
          <select id="sg-sample-config-status">
            <option value="not_checked">Not checked</option>
            <option value="pass">Pass — sample matches expected configuration</option>
            <option value="issue">Issue — configuration mismatch or uncertainty</option>
          </select>
        </label>

        <label>
          2. Mechanical fit
          <select id="sg-sample-fit-status">
            <option value="not_checked">Not checked</option>
            <option value="pass">Pass — fit / mounting acceptable for this test</option>
            <option value="issue">Issue — fit / mounting needs review</option>
          </select>
        </label>

        <label>
          3. No-load / free-rotation check
          <select id="sg-sample-noload-status">
            <option value="not_checked">Not checked</option>
            <option value="pass">Pass — basic no-load / free-rotation check acceptable</option>
            <option value="issue">Issue — alignment, drag, motion or setup concern</option>
          </select>
        </label>

        <label>
          4. Functional test
          <select id="sg-sample-functional-status">
            <option value="not_checked">Not checked</option>
            <option value="pass">Pass — required basic function demonstrated</option>
            <option value="issue">Issue — output / motion / behavior needs review</option>
          </select>
        </label>

        <label>
          5. Representative application-load test
          <select id="sg-sample-application-status">
            <option value="not_checked">Not checked</option>
            <option value="pass">Pass — representative mechanism / load test acceptable</option>
            <option value="issue">Issue — representative application test needs review</option>
          </select>
        </label>

        <label>
          Engineering outcome
          <select id="sg-sample-outcome">
            <option value="not_decided">Not decided yet</option>
            <option value="keep_current_configuration">Keep current configuration for next review</option>
            <option value="change_ratio">Review a different ratio / stage</option>
            <option value="change_motor_or_input">Review motor / input-side configuration</option>
            <option value="revise_mechanical_interface">Revise mounting / shaft / interface</option>
            <option value="more_testing_required">More testing required</option>
            <option value="ready_for_design_in_review">Submit current configuration for Design-In review</option>
          </select>
        </label>
      </div>

      <label>
        Test operating condition / evidence
        <textarea id="sg-sample-test-condition" rows="3" placeholder="Motor / input condition, representative load, output speed, duty cycle, peak duration, temperature or other useful test context."></textarea>
      </label>

      <label>
        Issue / observation notes
        <textarea id="sg-sample-notes" rows="3" placeholder="What was expected, what happened, noise / vibration / temperature observations, fault information, interface issue, or remaining question."></textarea>
      </label>

      <div id="sg-sample-readiness" class="siggear-sample-readiness">
        <strong>Validation status</strong>
        <p id="sg-sample-readiness-status">Validation in Progress — record each step before submitting the configuration for Design-In review.</p>
      </div>

      <div class="siggear-form-actions">
        <button type="button" id="sg-copy-sample-summary" class="md-button md-button--primary">Copy Validation Summary</button>
        <button type="button" id="sg-email-sample-summary" class="md-button">Prepare Validation Email to SigGear</button>
        <a id="sg-sample-datasheet" class="md-button" href="#">Open Datasheet</a>
        <a id="sg-sample-interface" class="md-button" href="#">Open Mechanical Interface</a>
        <a id="sg-sample-design-in-review" class="md-button" href="design-in-checklist.md">Open Design-In Review</a>
      </div>

      <p id="sg-sample-action-status" class="siggear-form-status" aria-live="polite"></p>
    </form>
  </div>
</div>

The detailed operating condition and free-text observations stay in your browser until you copy the summary or open your email client. They are not sent to GA4.

## Before the Sample Is Ordered

Confirm the exact configuration being evaluated.

At minimum, record:

- product model
- ratio or output-speed target
- driver / no-driver configuration where applicable
- encoder requirement where applicable
- operating voltage where applicable
- required communication interface where applicable
- mounting or shaft requirements that affect the sample
- sample quantity

Use the public Engineering Pack before ordering when one is available.

[Open the Engineering Center](index.md)

## When the Sample Is Received

Before installation:

1. confirm the model and quantity received
2. compare the physical configuration with the order or quotation
3. check for visible shipping damage
4. identify the exact driver / connector / cable configuration where applicable
5. use the documentation matched to that configuration

If anything is unclear, confirm the configuration before wiring or modifying the sample.

## Step 1 - Mechanical Fit

Check the sample against the customer's assembly:

- outer diameter and axial length
- mounting-hole pattern
- output shaft or output flange
- locating features
- cable and connector clearance
- motor-side interface for gearbox-only evaluations
- direction of external radial and axial loads

For public models, use the released simplified STEP for packaging and mounting evaluation. Use the controlled drawing before final production release.

## Step 2 - First Power-Up or No-Load Check

For actuator or motorized configurations, first confirm the basic setup before applying the real application load.

Typical checks include:

- supply voltage
- wiring and connector orientation
- communication link where applicable
- enable / basic command response
- direction of motion
- encoder feedback where applicable
- no-load motion

Detailed wiring, protocol and firmware-specific instructions must match the actual driver configuration.

For a gearbox-only sample, first confirm free assembly, input/output alignment and the selected motor interface before loaded testing.

## Step 3 - Functional Test

Run the motion required by the application and record the operating condition.

Useful information includes:

- output speed
- applied or estimated load
- motion cycle
- acceleration / deceleration behavior
- current where applicable
- temperature where relevant
- observed backlash, vibration or noise where relevant
- any communication or control fault

Do not compare a short sample test directly with a lifetime or continuous-duty claim unless the applicable rating and test condition are documented for that configuration.

## Step 4 - Application Test

After the basic function is stable, evaluate the sample in the real or representative mechanism.

Confirm:

- actual installation geometry
- actual load direction
- continuous and peak load condition
- peak duration
- duty cycle
- ambient / cooling condition
- power-off behavior if important
- controller / current-limit conditions for motorized actuators

## If a Problem Appears

Send the smallest useful set of evidence first:

- exact model and configuration
- supply voltage
- controller / driver information
- command or operating mode
- what was expected
- what actually happened
- fault code or log if available
- short video or photo if it helps show the issue

This is usually more useful than sending a long general description without the operating condition.

## Model-Specific Starting Points

### SG-6010C

Public starting resources:

- [Technical Datasheet](../engineering-resources/sg6010c/datasheet.md)
- [Simplified STEP](../assets/downloads/sg6010c/SG-6010C_Public_Simplified_STEP_v1.0.step)
- [Mechanical Interface](../engineering-resources/sg6010c/mechanical-interface.md)

Quick Start, detailed CAN and firmware-specific integration documents are supplied after configuration review.

### CPM-80-25

Public starting resources:

- [Technical Datasheet](../engineering-resources/cpm80-25/datasheet.md)
- [Mechanical Interface](../engineering-resources/cpm80-25/mechanical-interface.md)
- [Measured Performance Data](../engineering-resources/cpm80-25/performance-test-data.md)
- [STEP - No Driver](../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step)
- [STEP - Integrated Driver](../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step)

### 32P

Public starting resources:

- [Technical Datasheet](../engineering-resources/32p/datasheet.md)
- [Mechanical Interface](../engineering-resources/32p/mechanical-interface.md)
- [Motor Integration Guide](../engineering-resources/32p/motor-integration.md)
- [4-Stage Simplified STEP](../assets/downloads/32p/32P_Public_Simplified_STEP_v1.0_4-Stage.step)

The current public 32P STEP represents the 4-stage reference only. Request configuration-specific CAD for other stage arrangements.

## When the Sample Is Ready for the Next Stage

A successful sample test should lead to a concrete engineering decision, for example:

- keep the current configuration
- change the ratio
- change the motor / driver
- revise the mounting or output interface
- request a controlled drawing
- integrate into the next prototype
- prepare for Design-In

[Open the Design-In Checklist](design-in-checklist.md){ .md-button .md-button--primary }
[Prototype → Design-In → Production](../custom-engineering/prototype-to-production.md){ .md-button }
[Request Configuration-Specific Support](../request-cad-sample-quote.md){ .md-button }

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

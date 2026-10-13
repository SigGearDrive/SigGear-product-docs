---
title: Pilot Preparation Review | Design Freeze, Inspection & Change Control | SigGear
description: A structured pilot-preparation review for SigGear projects after Design Freeze, covering controlled revisions, pilot quantity, schedule, inspection, packaging, change control and pilot acceptance planning.
---

# Pilot Preparation Review

Use this review after the project has reached **Design-In Review Ready** and the responsible engineering / project teams have separately confirmed **Design Freeze**.

This page does not approve Design Freeze, Pilot Preparation Ready or Production Release. It helps organize the information needed for a human pilot-preparation review.

<div id="sg-pilot-preparation" class="siggear-pilot-preparation" hidden>
  <p id="sg-pilot-preparation-status">Checking the candidate and Design-In handoff...</p>

  <div id="sg-pilot-preparation-content" hidden>
    <div class="siggear-pilot-candidate-summary">
      <strong id="sg-pilot-candidate-name"></strong>
      <span id="sg-pilot-candidate-detail"></span>
    </div>

    <form id="sg-pilot-preparation-form">
      <div class="siggear-form-grid">
        <label>
          Design Freeze confirmation
          <select id="sg-pilot-design-freeze">
            <option value="not_confirmed">Not confirmed</option>
            <option value="confirmed_by_responsible_team">Confirmed by responsible engineering / project team</option>
          </select>
        </label>

        <label>
          Controlled drawing revision
          <input id="sg-pilot-drawing-revision" type="text" placeholder="Example: DWG-XXXX Rev.B">
        </label>

        <label>
          Configuration / BOM revision
          <input id="sg-pilot-bom-revision" type="text" placeholder="Project configuration or BOM revision">
        </label>

        <label>
          Pilot quantity
          <input id="sg-pilot-quantity" type="text" placeholder="Example: 20 pcs">
        </label>

        <label>
          Target pilot schedule
          <input id="sg-pilot-schedule" type="text" placeholder="Requested build / delivery timing">
        </label>

        <label>
          Critical inspection / acceptance characteristics
          <input id="sg-pilot-inspection" type="text" placeholder="Critical dimensions, functional checks or agreed inspection items">
        </label>

        <label>
          Packaging / labeling requirement
          <input id="sg-pilot-packaging" type="text" placeholder="Requirement, or write standard / not required">
        </label>

        <label>
          Change-notification expectation
          <input id="sg-pilot-change-control" type="text" placeholder="What changes require notification / approval?">
        </label>
      </div>

      <label>
        Pilot acceptance / validation plan
        <textarea id="sg-pilot-acceptance-plan" rows="3" placeholder="What will be checked on the pilot build before moving toward production?"></textarea>
      </label>

      <label>
        Project-specific documentation
        <textarea id="sg-pilot-documentation" rows="3" placeholder="Inspection report, material / quality document, packaging record, traceability requirement, or write not required."></textarea>
      </label>

      <div id="sg-pilot-readiness" class="siggear-pilot-readiness">
        <strong>Pilot preparation review status</strong>
        <p id="sg-pilot-readiness-status">Need Design Freeze Confirmation — the website cannot confirm Design Freeze on its own.</p>
        <ul id="sg-pilot-readiness-gates"></ul>
        <p class="siggear-pilot-note"><strong>Ready to Submit for Pilot Preparation Review</strong> means the checklist is complete enough for a human review. It does not mean Pilot Preparation Ready, pilot build approved or production released.</p>
      </div>

      <div class="siggear-form-actions">
        <button type="button" id="sg-copy-pilot-summary" class="md-button md-button--primary">Copy Pilot Review Summary</button>
        <button type="button" id="sg-email-pilot-summary" class="md-button">Prepare Pilot Review Email to SigGear</button>
        <a id="sg-pilot-datasheet" class="md-button" href="#">Open Datasheet</a>
        <a id="sg-pilot-interface" class="md-button" href="#">Open Mechanical Interface</a>
      </div>

      <p id="sg-pilot-action-status" class="siggear-form-status" aria-live="polite"></p>
    </form>
  </div>
</div>

The drawing revision, BOM / configuration revision, quantities, schedule, inspection details, packaging, change-control requirements and pilot acceptance plan stay in the browser until you copy the summary or open your email client. They are not sent to GA4.

## Pilot Preparation Review Gates

A pilot-preparation review should be able to identify:

1. **Design Freeze confirmation** — confirmed by the responsible engineering / project team, not by the website.
2. **Controlled configuration** — drawing revision and configuration / BOM revision.
3. **Pilot quantity and schedule** — what will be built and when.
4. **Inspection / acceptance definition** — what characteristics must be checked.
5. **Packaging / labeling** — requirement, standard condition or explicitly not required.
6. **Change control** — what changes require notification or approval.
7. **Pilot acceptance plan** — what must be demonstrated before a production-release discussion.

## Manual Milestone Boundary

**Human confirmation required:** **Pilot Preparation Ready** remains a human-confirmed project milestone.

The website never automatically sets:

- Design Frozen
- Pilot Preparation Ready
- Pilot Build Approved
- Production Released

[Open Design-In Checklist](design-in-checklist.md){ .md-button }
[Prototype → Design-In → Production](../custom-engineering/prototype-to-production.md){ .md-button }

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

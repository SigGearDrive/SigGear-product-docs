---
title: Planetary Gearbox Quick Selector 8–42 mm | Ratio, Torque & STEP | SigGear
description: Enter loaded motor RPM and target output RPM to compare SigGear 8–42 mm planetary gearbox stage, ratio, rated torque and length. Download PDF, 2D drawings and STEP files directly.
---

# Planetary Gearbox Quick Selector · Ø8–42 mm

**Enter motor speed + output speed → compare published ratios and rated torque → download PDF / 2D / STEP.**

[**All model downloads**](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }
[**Compare 12 diameters**](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button }

## Find Planetary Gearbox Size, Ratio and Downloads {#preliminary-ratio-stage-finder}

<p id="sg-selector-application-context" class="siggear-selector-context" hidden></p>

<form id="siggear-ratio-stage-selector" class="siggear-ratio-selector">
  <div class="siggear-selector-grid">
    <label>
      Motor loaded speed (rpm)
      <input id="sg-selector-motor-speed" type="number" min="0.01" step="any" required placeholder="e.g. 6000">
    </label>
    <label>
      Target output speed (rpm)
      <input id="sg-selector-output-speed" type="number" min="0.01" step="any" required placeholder="e.g. 140">
    </label>
  </div>

  <details class="siggear-selector-optional">
    <summary>Optional filters: diameter, length, continuous / peak torque, ratio tolerance</summary>
    <div class="siggear-selector-grid">
      <label>
        Maximum gearbox diameter (mm)
        <input id="sg-selector-diameter" type="number" min="0.01" step="any" placeholder="e.g. 32">
      </label>
      <label>
        Maximum gearbox body length (mm)
        <input id="sg-selector-length" type="number" min="0.01" step="any" placeholder="Gearbox body only">
      </label>
      <label>
        Required continuous output torque
        <input id="sg-selector-torque" type="number" min="0" step="any" placeholder="Rated torque filter">
      </label>
      <label>
        Torque unit
        <select id="sg-selector-torque-unit" aria-label="Torque unit">
          <option value="nm">N·m</option>
          <option value="kgfcm">kgf·cm</option>
        </select>
      </label>
      <label>
        Peak output torque (screen only)
        <input id="sg-selector-peak-torque" type="number" min="0" step="any" placeholder="Duration needs review">
      </label>
      <label>
        Maximum ratio difference (%)
        <input id="sg-selector-ratio-tolerance" type="number" min="0" step="any" placeholder="e.g. 5">
      </label>
    </div>
  </details>

  <div class="siggear-selector-actions">
    <button type="submit" class="md-button md-button--primary">Find Published Configurations + Downloads</button>
  </div>

  <p id="sg-ratio-stage-summary" class="siggear-selector-summary" aria-live="polite"></p>
  <div id="sg-ratio-stage-results" aria-live="polite"></div>
</form>

## If No Standard Configuration Fits

The selector only screens the published 8P–42P configurations. A project can still be reviewed when the required motor interface, ratio, shaft, flange, envelope or duty cycle falls outside the standard list.

[**I Already Have a Motor**](../custom-engineering/custom-planetary-gearbox.md){ .md-button .md-button--primary }
[**I Have a Drawing / STEP**](../custom-engineering/custom-gearbox-from-drawing-cad.md){ .md-button }
[**Replace / Redesign Existing Gearbox**](../custom-engineering/gearbox-failure-analysis-durability-redesign.md){ .md-button }
[**Prototype → Volume Production**](../custom-engineering/oem-volume-manufacturing-delivery.md){ .md-button }

## Direct Files — No Selection Needed

| Gearbox | Datasheet PDF | 2D outline PDF | Full assembly STEP |
| --- | --- | --- | --- |
| [**8P · Ø8**](../products/planetary-gearboxes/8p-planetary-gearbox.md) | [PDF](../assets/downloads/8p/8P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/8p/8P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/8p/8P_Full_Assembly.step) |
| [**10P · Ø10**](../products/planetary-gearboxes/10p-planetary-gearbox.md) | [PDF](../assets/downloads/10p/10P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/10p/10P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/10p/10P_Full_Assembly.step) |
| [**12P · Ø12**](../products/planetary-gearboxes/12p-planetary-gearbox.md) | [PDF](../assets/downloads/12p/12P_Planetary_Gearhead_Datasheet_Rev1.1.pdf) | [2D drawing](../assets/downloads/12p/12P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/12p/12P_Full_Assembly.step) |
| [**14P · Ø14**](../products/planetary-gearboxes/14p-planetary-gearbox.md) | [PDF](../assets/downloads/14p/14P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/14p/14P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/14p/14P_Full_Assembly.step) |
| [**16P · Ø16**](../products/planetary-gearboxes/16p-planetary-gearbox.md) | [PDF](../assets/downloads/16p/16P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/16p/16P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/16p/16P_Full_Assembly.step) |
| [**20P · Ø20**](../products/planetary-gearboxes/20p-planetary-gearbox.md) | [PDF](../assets/downloads/20p/20P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/20p/20P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/20p/20P_Full_Assembly.step) |
| [**22P · Ø22**](../products/planetary-gearboxes/22p-planetary-gearbox.md) | [PDF](../assets/downloads/22p/22P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/22p/22P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/22p/22P_Full_Assembly.step) |
| [**24P · Ø24**](../products/planetary-gearboxes/24p-planetary-gearbox.md) | [PDF](../assets/downloads/24p/24P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/24p/24P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/24p/24P_Full_Assembly.step) |
| [**28P · Ø28**](../products/planetary-gearboxes/28p-planetary-gearbox.md) | [PDF](../assets/downloads/28p/28P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/28p/28P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/28p/28P_Full_Assembly.step) |
| [**32P · Ø32**](../products/planetary-gearboxes/32p-planetary-gearbox.md) | [PDF](../assets/downloads/32p/32P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/32p/32P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/32p/32P_Full_Assembly.step) |
| [**36P · Ø36**](../products/planetary-gearboxes/36p-planetary-gearbox.md) | [PDF](../assets/downloads/36p/36P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/36p/36P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/36p/36P_Full_Assembly.step) |
| [**42P · Ø42**](../products/planetary-gearboxes/42p-planetary-gearbox.md) | [PDF](../assets/downloads/42p/42P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D drawing](../assets/downloads/42p/42P_2D_Drawing.pdf) | [Full STEP](../assets/downloads/42p/42P_Full_Assembly.step) |

**Other size groups:** [Micro 8–16 mm](../products/planetary-gearboxes/micro-planetary-gearheads-8-16mm.md) · [Miniature 20–32 mm](../products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm.md) · [Compact 36–42 mm](../products/planetary-gearboxes/compact-planetary-gearheads-36-42mm.md)

<small>Screening uses **loaded motor rpm ÷ target output rpm** and published 1–4 stage ratios. Motor speed is used to calculate ratio candidates; permissible gearbox input speed is **motor- and configuration-dependent** and must be confirmed for the selected operating point. Continuous torque checks use **Rated Allowable Torque**, never momentary torque. The full assembly STEP is not stage-specific approval; original 2D drawings use configuration-dependent length L. Confirm input pinion / mounting, shaft loads, duty cycle and the controlled variant before production. [Detailed selection method](miniature-planetary-gearbox-selection-guide.md).</small>

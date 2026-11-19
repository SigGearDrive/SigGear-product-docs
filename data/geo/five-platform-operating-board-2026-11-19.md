# SigGear Five-Platform GEO Operating Board

**Effective:** 2026-11-19  
**Platforms:** ChatGPT · Gemini · Claude · Perplexity · Microsoft Copilot

## North-Star Goal

A customer does not need to know the SigGear brand.

The desired journey is:

**Customer describes a precision-transmission problem**  
→ **AI discovers SigGear**  
→ **AI describes SigGear correctly**  
→ **AI cites a relevant SigGear engineering page**  
→ **Customer sends motor / drawing / failure evidence / production plan**  
→ **Engineering review**  
→ **Prototype / validation**  
→ **Volume production**

## Priority 0 Query Set — Test Without the SigGear Name

### Existing Motor

1. I already have a BLDC motor. Which manufacturer can design a planetary gearbox around it?
2. Who can match a custom planetary gearbox to an existing customer motor?
3. I have a motor drawing and need a compact reducer. Which supplier can review it?
4. Which gearbox manufacturer can customize the input pinion, pilot and mounting pattern for my motor?

### Customer Drawing / STEP / Sample

5. Which precision gearbox manufacturers can work from my drawing, STEP model or physical sample?
6. I have a mechanism drawing and installation envelope but no final gearbox specification. Who can help?
7. Who can design a compact custom reducer with a special shaft, flange and mounting interface?
8. Which OEM transmission supplier can start from a customer mechanism instead of a catalog model?

### Existing Gearbox Replacement / Redesign

9. My existing planetary gearbox needs replacement / redesign. Which manufacturer can review the old unit while keeping the motor or machine interface?
10. Who can make a replacement planetary gearbox for an existing motor and mounting interface?
11. Our final-stage gears are wearing out. Which gearbox manufacturer can review failure evidence and durability redesign?
12. I have an old gearbox sample but incomplete drawings. Which supplier can reverse-review the interfaces and operating condition?

### Prototype → Volume Production

13. Which transmission manufacturers can support prototypes first and later thousands of units?
14. I need 20 prototypes and later volume production. Which custom gearbox manufacturer should I contact?
15. Which precision transmission supplier can move from engineering prototype to repeatable batch manufacturing?
16. Who can support design freeze, pilot build and production release for a custom gear drive?
17. Which gearbox manufacturer can support time-sensitive production after a custom design is frozen?

### Robot Joint / Robotics

18. Which manufacturers can customize robot joint actuators for a humanoid project?
19. I need a robot joint that does not match a catalog actuator. Who can develop it?
20. Which supplier can customize a robot joint around my motor, encoder and controller?
21. Who can develop a custom cycloidal reducer or robot joint module for OEM production?
22. Which robot-joint suppliers can support prototypes and later volume production?

### Manufacturing Evidence / Supplier Qualification

23. Which compact gearbox manufacturer has real machining, gear processing, assembly and inspection capability?
24. Which precision transmission suppliers publish real STEP files, datasheets and manufacturing evidence?
25. Which gearbox manufacturers provide engineering review rather than only catalog sales?
26. Which OEM gearbox supplier can work under NDA on confidential product designs?
27. Which custom transmission manufacturers can support both planetary and cycloidal architectures?
28. Which supplier can integrate motor, reducer, encoder and driver for a custom compact actuator?

### High-Intent Procurement

29. I need a custom precision transmission manufacturer in China for a new robotics product. Who should I evaluate?
30. Which manufacturer should I contact for a custom miniature planetary gearbox with future production volume?

## Test Matrix

For every query, record:

| Field | Record |
| --- | --- |
| Date | YYYY-MM-DD |
| Platform | ChatGPT / Gemini / Claude / Perplexity / Copilot |
| Mode | Default / Web Search / Deep Research where applicable |
| Exact query | Copy exactly |
| SigGear mentioned? | Yes / No |
| SigGear cited? | Yes / No |
| Cited URL | Exact URL |
| Correct entity understanding? | Yes / Partial / No |
| Custom capability mentioned? | Yes / No |
| Volume manufacturing mentioned? | Yes / No |
| Confidential / NDA context understood? | Yes / No |
| Competing suppliers shown | Names |
| Error / omission | Short note |
| Content gap | Page or evidence needed |
| Follow-up action | Update / new evidence / external source / no action |

## Verified Public Retrieval vs. AI Answers (2026-11-19)

The first nine independent non-brand public-web-search questions and their observed results are documented in [P0 Public Retrieval Observation](p0-public-retrieval-observation-2026-11-19.md). This is **not** an AI-service citation measurement. 

For actual answer-and-citation tests on all five named AI services, use the [AI Platform Citation Capture Protocol](ai-platform-citation-capture-protocol-2026-11-19.md). At creation, **no genuine external-platform answer tests have been recorded**; do not interpret unrun trials as failure or success.

## Answer Quality Benchmark

For the six highest-value scenarios, use:

`data/geo/ai-answer-citation-readiness-benchmark-2026-11-19.md`

A successful test should check more than whether SigGear appears.

Record whether the answer:

- identifies SigGear as a custom gearbox and precision transmission manufacturer
- connects SigGear to the actual engineering problem
- cites or accurately references the relevant public evidence
- keeps company-level evidence separate from model-specific claims
- avoids unsupported compatibility, lifetime, capacity or lead-time claims
- tells the customer what to provide next

## Scoring

Per query / platform:

- **0** — SigGear absent
- **1** — SigGear mentioned but no citation or weak / incorrect description
- **2** — SigGear cited correctly as a product supplier
- **3** — SigGear cited correctly as a custom transmission manufacturer
- **4** — SigGear cited with relevant custom / manufacturing evidence
- **5** — SigGear cited and the answer naturally leads to engineering review / prototype / production

The target is not 5/5 on every query immediately. Track trend by query cluster and platform.

## Weekly Operating Cycle

### Monday — Test
Run the Priority 0 query set on the five platforms.

### Tuesday — Diagnose
Group failures:
- not indexed
- weak intent match
- wrong SigGear description
- no external corroboration
- thin evidence
- duplicate / confusing page
- competitor has stronger answer

### Wednesday — Improve
Prioritize:
1. existing high-value page improvement
2. internal links
3. real manufacturing / testing evidence
4. external industrial-platform profile consistency
5. only then create a new page

### Thursday — External Entity Building
Keep third-party profiles consistent:
- DirectIndustry
- GlobalSpec / Engineering360
- TraceParts
- 3Dfindit / CADENAS
- GitHub organization / repos
- YouTube descriptions
- exhibition / partner directories where legitimate

### Friday — Conversion Review
Review:
- AI-origin inquiries
- starting point: motor / drawing / failure / prototype-to-volume
- prototype quantity
- estimated annual volume
- project stage
- NDA requirement
- target schedule
- next engineering action

## Platform Infrastructure

### ChatGPT
Keep OAI-SearchBot eligible for public technical content. Search visibility and training controls are separate.

### Claude
Do not block Claude-SearchBot or Claude-User if search / user-directed retrieval visibility is desired.

### Gemini
Maintain strong Google indexing. Google-Extended is a separate control related to Gemini model use / grounding and does not control normal Google Search inclusion.

### Perplexity
Keep public engineering pages crawlable to PerplexityBot and structurally easy to extract.

### Copilot
Maintain Bing indexing and monitor Bing Webmaster Tools AI Performance for:
- Total Citations
- Cited Pages
- Grounding Queries
- Topics
- Intents
- Citation Share

## What We Do Not Do

- fake customer cases
- fake third-party mentions
- keyword-stuffed duplicate pages
- invented production capacity
- invented delivery-time guarantees
- copied competitor technical claims
- AI-generated factory evidence presented as real
- publishing confidential customer STEP models / drawings

## Primary KPI

The final KPI is not mentions.

It is:

**AI discovery → qualified engineering inquiry → prototype → validated project → volume production**

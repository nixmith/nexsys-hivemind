<!--
file: context/instructions/Research_15_Ecosystem_Positioning_Scan_Brief.md
purpose: Dispatchable research brief — Research 15: Ecosystem & Competitive Positioning Scan (strategic register). Gap-relative to the strategy layer (context/strategy/) + the endorsed INV-CE-01 positioning baseline. Feeds M5-C website/docs + the strategy layer ONLY — this research CANNOT mint code obligations.
audience: researcher (generic deep research permitted for evidence; disposition pass in the DOCS Project), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-12 (PM, Cowork) per context/planning/2026-06-11_M7-blueprint_research-architecture.md. Runs SIMULTANEOUSLY with Research 14-A and Research 14-B — REC ranges are partitioned; this brief is fully self-contained (never reference a sibling return).
dispatch-target: TWO-STAGE PERMITTED — evidence-gathering MAY run as generic deep research (the Research-13 masthead fallback, made primary here: the evidence is entirely external); the DISPOSITION PASS (§4b) always runs in-Project against the strategy files. If run as one in-Project session with adequate web reach, that satisfies both stages.
rec-block: REC-171–185 (reserved; high-water at authoring = REC-140, Research 13; siblings hold 141–155 and 156–170 — do not exceed 185)
baseline: homesynapse-core HEAD `7c73c91` (M6.2) · strategy layer at context/strategy/ (5 files, listed §0.2) · launch target 2026-11-25
-->

# RESEARCH BRIEF: Research 15 — Ecosystem & Competitive Positioning Scan

*Target: M5-C website/docs (the P6 non-preemptable lane) + the `context/strategy/` layer refresh. Date: 2026-06-12.*

You are a strategic-landscape researcher for NexSys, whose first product is HomeSynapse Core — a local-first, event-sourced smart home runtime (Java 21, Raspberry-Pi-class hardware, launch target 2026-11-25) positioned as a **trust brand**: local-first, privacy-preserving, user-owned data, no cloud dependency for core function. Your task is a **positioning evidence scan**: where the ecosystem is moving (certification, platform strategy, licensing, privacy expectations) and where a trust-brand local-first system wins or loses commercially — mapped against the strategy NexSys has already written, so the PM can refresh the strategy layer and arm the M5-C website with evidence-grade superiority material.

**This research CANNOT mint code obligations.** Your deliverable feeds marketing/positioning/strategy documents. Any code-facing implication routes to FUTURE-PARKING in the disposition table — it will be considered only through the formal pipeline, later, by others. A positioning scan that starts redesigning the engine has left its register and those findings will be discarded.

**The disposition table (§4b) is the load-bearing deliverable.**

---

## 0. Quote-back gate [DO THIS FIRST]

Open your return by quoting back, **verbatim**: (a) the §0.2 strategy-file list (all five filenames); (b) the §0.3 INV-CE-01 positioning baseline paragraph; (c) the §0.4 register rule ("This research CANNOT mint code obligations…" sentence). If you cannot quote them, STOP and return INCOMPLETE. A return that fails the quote-back is discarded unread past §0.

## 0.1 Authoritative state (do not work from memory)

- homesynapse-core HEAD: **`7c73c91`** (2026-06-11). Engineering state is NOT your register — you need only: the runtime is real, event-sourced, local-first, in Phase-3 implementation, config system shipped, automation engine contracts frozen, launch target **2026-11-25**.
- Research numbering: this is **Research 15**, REC range **171–185**. Research 14-A/14-B (automation UX/engineering) run simultaneously with their own ranges; you must not reference or anticipate them.

## 0.2 The strategy layer (your gap-relative baseline — the disposition pass runs against THESE)

In `nexsys-hivemind/context/strategy/` (for the in-Project disposition pass; the `.docx` files need the docx tooling):

1. `Six_Battlefields_MVP_Strategy.md`
2. `Revenue_Model_and_Licensing_Strategy.md`
3. `From_Platform_to_Institution_NexSys_Strategic_Report.docx`
4. `NexSys_Data_Value_Engine_Strategy.docx`
5. `HomeSynapse_MVP_Data_Readiness_Specification.docx`

**Minimum read set for the disposition pass (the floor):** files 1 and 2 in full; the executive-summary/positioning sections of 3–5. If the evidence-gathering stage runs as generic deep research without strategy-file access, the disposition pass in-Project MUST re-run every finding against this read set before bucketing — a bucket assigned without reading the strategy file it cites is invalid.

## 0.3 The endorsed positioning baseline (quote back in §0)

**INV-CE-01 — the YAML file is the sole source of truth; UI/CLI/REST all read/write that same file. There is structurally no HA-style `.storage`-vs-YAML split-brain.** Research 13 (2026-06-10, assessed A−) **endorsed this split-brain-immunity claim as flagship website-grade superiority material** — it is the calibration example of what "evidence-grade positioning material" means: a structural property competitors demonstrably lack, provable from our architecture, matched to documented competitor pain. Your job includes finding MORE claims of this grade (and honestly flagging where claimed superiority is NOT supported by evidence).

Standing positioning facts you may rely on: local-first (core function with WAN down), event-sourced immutable history (deterministic replay), per-scope encryption infrastructure shipped, secrets encrypted at rest, no phone-home telemetry and no cloud dependency in core function, single-binary-class deployment on user-owned hardware, open governance posture per the licensing strategy (file 2 governs — read it rather than assuming a license).

## 0.4 Register rule (quote back in §0)

**This research CANNOT mint code obligations. Its RECs route to strategy/M5-C buckets or FUTURE-PARKING only; no REC may name a milestone, an amendment, a type, a module, or a contract change as its recommendation.**

---

## 1. Research questions (answer ALL five; strategic register)

### RQ1 — Matter/Thread certification dynamics + trajectory

Current state and 12–24-month trajectory of Matter (CSA) and Thread: certification cost/process for a small vendor (actual fee schedules, membership tiers, testing requirements — primary sources); Matter's delivered-vs-promised reality (cited device-category coverage, multi-admin friction, version adoption lag); Thread border-router fragmentation; whether non-certified local control of Matter devices is viable (and the legal/trademark constraints on saying so). Verdict: what should a launch-window local-first runtime DO about Matter positioning-wise (embrace/bridge/wait), and what does certification economics mean for the revenue model (file 2)?

### RQ2 — Platform strategy shifts

Documented strategy moves and their community reception: Home Assistant / Nabu Casa / Open Home Foundation commercialization arc (what changed, what users fear/welcome — cited); SmartThings' post-Groovy trajectory and Aeotec hardware story; Apple HomeKit/Home local-control posture and its walled-garden economics; Google/Amazon local-execution pushes (Matter-driven) vs their cloud-account dependencies; Hubitat/Homey positioning between local and cloud. For each: what the move signals about where the market believes value sits (local vs cloud, hardware vs subscription vs data). Verdict per platform: the positioning lesson for a trust-brand entrant.

### RQ3 — The local-first/privacy positioning landscape

Who else claims local-first/privacy-first, and what does the claim earn them? Evidence of demand: documented cloud-shutdown/outage incidents driving migrations (Insteon, SmartThings outages, Tuya incidents — what users DID); privacy-regulation tailwinds (EU Data Act, right-to-repair, IoT security labeling) with citations; willingness-to-pay signals for local-first (Hubitat/Homey sales models, HA Cloud conversion signals, crowdfunding outcomes). Honesty check: evidence of the local-first claim NOT mattering (mass-market indifference signals). Verdict: which positioning claims have evidence behind them for the M5-C website, and which are trust-brand wishful thinking.

### RQ4 — Open-source governance + licensing risk patterns

Recent licensing/governance ruptures and their costs: the HashiCorp BUSL → OpenTofu fork; Redis relicensing → Valkey; Elastic → OpenSearch (and the 2024 AGPL return); open-core tension case studies in home automation specifically (HA's choices, any CLA controversies). Patterns: what triggers community forks, what governance structures retain trust (foundations vs BDFL vs corporate), how dual-licensing/open-core lands with the home-automation audience. Gap-relative: file 2 (Revenue Model and Licensing Strategy) is the baseline — your findings confirm, refine, or challenge its choices WITH EVIDENCE. Verdict: the licensing-risk map for NexSys's chosen model.

### RQ5 — Where a trust-brand local-first system wins/loses commercially

Synthesis RQ: across RQ1–RQ4 evidence, where does the trust brand convert to revenue (and where does it not)? Candidate win surfaces to test against evidence: privacy-sensitive household segments; prosumer/self-hosted communities (size estimates with sources); institutional/insurance/energy adjacencies (the strategy layer's NexSys Grid/Assure concepts — files 3/4); regions with strong privacy regulation. Candidate loss surfaces: mass-market convenience buyers; ecosystem-locked households; price-sensitive segments vs free cloud tiers. Verdict: a ranked, evidence-cited map of commercial surfaces for the strategy refresh — explicitly marking where the existing strategy files' assumptions are CONFIRMED, REFINED, or CHALLENGED.

---

## 2. Mandatory document format

```
# Research 15: Ecosystem & Competitive Positioning Scan
*Target: NexSys strategy layer + M5-C website/docs. Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — FIRST] — per §0 above.

## 1. Executive Summary [M] — 5–8 verdict bullets; every bullet takes a position with a
     one-sentence defense. "X is worth investigating" is banned. Flag the single
     highest-impact strategic finding AND the single best new website-grade claim found.

## 2. Landscape Deep Dives [M] — one subsection per RQ1–RQ4 domain. Each: (a) the
     current state, precisely, with dates; (b) ≥1 direct quotation from a primary
     source WITH URL; (c) the trajectory call (12–24 months, defended); (d) the
     positioning lesson, citing the §0.2/§0.3 baseline item it is relative to.

## 3. Cross-Cutting Analysis [M]
   - 3.1 The positioning map: claim | evidence grade (documented-incident /
         user-action / survey / inference) | competitors who can/cannot match it |
         website-ready? (the INV-CE-01 calibration bar).
   - 3.2 The strategy-assumption audit: strategy-file assumption (cite file + section)
         → CONFIRMED / REFINED / CHALLENGED, with the evidence.
   - 3.3 The risk register: certification, licensing, platform-shift risks ranked by
         (probability × impact), each with its earliest-warning indicator.
   - 3.4 Honesty section: where the trust-brand thesis is WEAKEST per the evidence.

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, REC-171 through at most REC-185, ranked by strategic
         impact × evidence grade. Each REC: the claim/risk; evidence (≥1 primary
         source); the gap-relative statement (which strategy file/section it
         touches); the concrete recommendation (a positioning move, a website claim,
         a strategy-file edit, a risk watch-item — NEVER a code/contract change).
   - 4b. THE DISPOSITION TABLE [M — load-bearing]: EVERY REC maps to EXACTLY ONE of:
           ALREADY-POSITIONED (the strategy layer already says it — cite file + section)
         | M5-C-WEBSITE-INPUT (evidence-grade superiority/positioning material,
           INV-CE-01-calibration quality)
         | STRATEGY-UPDATE (a specific strategy-file refresh — name file + section +
           the delta)
         | FUTURE-PARKING (code/product-facing implication — parked verbatim for the
           formal pipeline; NOT an obligation on anyone)
         | REJECT (reasoned — evidence says the positioning move is wrong).
         No REC in two buckets. No bucket empty by laziness — if genuinely empty, say why.

## 5. Caveats and Open Questions [M] — source reliability; fast-moving items with
     expiry dates (mark each finding's freshness horizon); explicit INCOMPLETE-EVIDENCE
     declaration if web reach was too shallow.

## 6. Appendix: Sources [M] — URL families grouped by domain; every factual claim traceable.
```

(There is deliberately NO §7 code-implications section in this format — that is the register fence.)

## 3. Evidence standards (non-negotiable)

1. **Primary sources with URLs, dated.** Foundation announcements, fee schedules, license texts, official blogs, post-mortems, dated forum/community threads. A claim without a citation is a vibe. Strategic claims decay — date everything and state each finding's freshness horizon.
2. **Mom-Test discipline for demand claims.** What users/companies DID (migrated, forked, paid, churned, shut down) outranks surveys; surveys outrank punditry. The HashiCorp→OpenTofu fork is the calibration case for governance claims; the Insteon shutdown for cloud-dependency claims.
3. **Take positions.** Every section concludes with a verdict; trajectory calls are mandatory (a landscape scan without trajectory is a Wikipedia article).
4. **Gap-relative or it didn't happen.** Every finding cites the strategy file/section (or §0.3 baseline item) it confirms, refines, or challenges.
5. **Web search/evidence-gathering is the point.** If reach is too shallow on any RQ, declare INCOMPLETE-EVIDENCE in §5 rather than padding.

## 4. Guardrails (violations = the finding is discarded)

1. **You cannot mint code obligations (§0.4).** No REC recommends a milestone, amendment, type, module, contract, or implementation change. Code-facing implications → FUTURE-PARKING, stated as neutral observations.
2. **Do not re-derive engineering claims.** The runtime's properties (§0.3 standing facts) are given; you neither verify nor redesign them. If evidence makes you doubt a standing fact's market value, that is a §3.4 honesty finding about POSITIONING, not an engineering finding.
3. **The licensing strategy file is the baseline, not a draft.** RQ4 findings confirm/refine/challenge it with evidence; the licensing decision itself is Nick's, through the strategy layer.
4. **REC numbering: 171–185 ONLY** (append-only global register; siblings own 141–170; high-water 140).
5. **Stay in register.** Automation UX evidence and engine prior art are the SIBLING researches' registers — if you trip over them, one line in §5, move on.
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM runs the standard 6-step A–F assessment. **Your return folds LAST** (after both engineering/UX returns — positioning only markets what survives engineering reality). Disposition rows route: ALREADY-POSITIONED → coverage attestation; M5-C-WEBSITE-INPUT → the M5-C content backlog (the P6 lane — this is the primary consumer); STRATEGY-UPDATE → PM-drafted strategy-file refreshes for Nick's veto (PM drafts, Nick vetoes content — the M5-C rule); FUTURE-PARKING → the parking register, untouched until a formal pipeline picks it up; REJECT → recorded anti-positioning with reasoning. Your §3.2 strategy-assumption audit is the highest-leverage section — it determines whether the strategy layer gets refreshed or re-confirmed. A finding that cannot be placed in that machine is a finding you should sharpen or drop.

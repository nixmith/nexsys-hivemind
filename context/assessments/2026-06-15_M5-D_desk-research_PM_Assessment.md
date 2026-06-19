<!--
file: context/assessments/2026-06-15_M5-D_desk-research_PM_Assessment.md
purpose: PM assessment + disposition of the M5-D desk-research return(s) on verifiable erasure (Track A) and
         DER/VPP settlement telemetry (Track B), produced by the interview-coaching lane 2026-06-15 and handed
         to the PM. Grades the return, runs a verification ledger against PRIMARY sources for the load-bearing
         post-2025 specifics, ADJUDICATES the Track-A/Track-B decision state against current ground truth,
         routes findings to lock points, and re-scopes the erasure interview ask. Treats all of it as VERIFIED
         BACKGROUND/EVIDENCE — not a decision, not a FINDINGS return.
audience: Nick, PM, the Track-2 app-bootstrap charter session, the future energy/Grid milestone
state-type: assessment
status: COMPLETE 2026-06-15
grade: A- (return 1) ; the PM-driven clause-language follow-up (return 2) folded
returns:
  - homesynapse-core-docs/research/returns/2026-06-15_M5-D_desk-research_erasure-energy_background_RETURN.md (rehomed from track1-interview-coaching/, md5-verified identical)
  - context/assessments/2026-06-15_M5-D_desk-research_ANGLE2-clause-language_TrackA.md (the Track-A procurement/clause-language angle, PM-driven this session; rehomed from the loose track1-interview-coaching/ lane in the 2026-06-18 cleanup)
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 at-rest write-path encryption committed); watermark AMD-93; Doc 15 LOCKED; AMD-86 RATIFIED.
guardrail: this assessment does NOT edit AMD-86 or Doc 15. Any re-open moves only via the formal pipeline (re-open -> DOCS review -> ratify). Background calibrates the prior; only buyer past-behavior (the interviews) produces FINDINGS.
-->

# PM Assessment — M5-D Desk Research (Verifiable Erasure / DER Settlement Telemetry)

## Grade: A- (return 1)

A strong, honestly-calibrated background brief that does exactly what good desk research should: it separates *what the law/standard requires* from *what vendors market*, leads with falsifiable hypotheses + base rates, flags confidence + recency per finding, and is honest about "not found" (the tamper-evident-log gap; the CNIL secondary quotes). It does not tell the founder what he wants to hear — its bottom line is that provable cryptographic destruction is **rare/false as a legal mandate**, which is the high-value, prior-confirming result. The minus: a cluster of load-bearing claims sits past the PM's May-2025 horizon and the return's own CAVEAT-2 flags them unverified; and §3 is statutory text, not the real procurement clause language the A3 falsifier needs (its CAVEAT-3) — a gap the PM drove a follow-up to fill (return 2 below).

## Verification ledger (the post-2025 specifics — spot-checked against PRIMARY/reputable sources, NOT trusted)

The return's value concentrates in recent (2025–2026) events past the PM horizon, so they were treated as claims-to-verify. **All four load-bearing clusters VERIFIED; no fabrication found.**

- **EDPB 2025 Coordinated Enforcement (right to erasure) — VERIFIED.** 32 supervisory authorities participated; the report (published mid-Feb 2026) draws on responses from **764 controllers**; **nine DPAs opened formal investigations**; the "**verify… and be able to demonstrate such erasure**" recommendation + "basic pseudonymisation/partial masking would not fulfil… deletion" framing are real (EDPB CEF report PDF live at edpb.europa.eu). The "7,943 contacted / 23 fact-finding" specifics come from the cited Reed Smith summary and were not independently re-confirmed, but the load-bearing figures (764 / 9 / 32 / Feb-2026 / the recommendation) hold. *This is the return's strongest "some provability is expected" signal — and it is genuine.*
- **NIST SP 800-88 Rev. 2 — VERIFIED.** Finalized **26 Sep 2025** (Rev.1 withdrawn that date). Cryptographic Erase = **one optional Purge technique** for qualifying self-encrypting drives, not a mandate; modernized for cloud/virtual/encrypted environments; verification (not crypto specifically) is the non-negotiable element. Matches the return verbatim.
- **US state privacy-law wave — VERIFIED.** **20 states** with comprehensive laws in effect in 2026 (MultiState, counting Florida's narrower law); **Indiana, Kentucky, Rhode Island effective 1 Jan 2026** (Koley Jessen, IAPP). None mandate cryptographic destruction. (A minor source-counting ambiguity — "19 before + 3" vs "20" — is a known convention difference, not an error; the return flagged the Florida-counting caveat itself.)
- **FERC Order 2222 RTO timelines — VERIFIED.** **SPP Q2 2030**; **MISO Phase 1 by 1 Jun 2027 / Phase 2 by 1 Jun 2029**; **PJM energy/AS ~1 Feb 2028** (capacity ~Feb 2027). Order 825 5-minute settlement + PJM 5-min (Apr 2018) + ERCOT 15-min all consistent with the live tariffs.

## The decision-state adjudication (the handoff's §2 — verified against the files, not assumed)

The 2026-06-07 interview guide framed **Track A** = "re-open AMD-86 BEFORE M6 freezes the write path" and **Track B** = author the C9 energy shape. Both framings are now **stale**, but not identically — and the precise reason matters:

### (a) Track B (energy / C9): EFFECTIVELY CLOSED — stop the energy interviews and energy research.
Correcting the premise: the AMD-92 ratification checklist ratifies **B2 C8 only** (the `actorRef` four-kind stamping). **C9 — the energy event shape — was NOT formally ratified** in the 2026-06-12 bundle (those were automation amendments; there are **zero energy event types** in the MVP today; the only "C9" closure was the §3.4 energy-*encryption*-posture reconciliation: energy stays plaintext-at-rest at MVP). So C9-shape is technically still an open, regret-proof design question — but it should be **parked for interview purposes regardless**, because:
1. The energy event family is **post-MVP** (Grid/VPP); nothing is written to the immutable log in an energy shape yet, so the regret-proof freeze point is the **future energy/Grid milestone (before the first energy event is written)** — NOT now. Stopping now forecloses nothing.
2. The desk research **already answers the shape** with high confidence: a simple shape (real power, cumulative Wh, V, I) at **clock-aligned 5-/15-/60-min intervals** from a **meter-of-record at ANSI C12.20 Class 0.5/0.2** (or via approved M&V/baseline) is sufficient to settle; sub-minute telemetry is dispatch/visibility, not settlement. The only real considerations — accuracy-class, interval alignment, measurement provenance — are **metadata slots reservable in the schema** without interviews.
3. Energy is on **no current gate** (the snapshot gates the interviews to app-bootstrap + the M6.3 restore-half R-α — both crypto/erasure, not energy).
**Ruling:** stop energy interviews + energy research. When the post-MVP energy/Grid milestone is actually scoped, author the regret-proof energy event shape from the desk findings (interval + accuracy-class slot + provenance slot + reserved Tier-2 fields: production Wh, net import/export, reactive power/PF, frequency, battery SoC, EV state), and validate with a real Grid buyer **only if one is in hand at that time**. No speculative energy interviews now.

### (b) Track A (verifiable erasure): the AMD-86 re-open trigger is MOOT; the interviews are downgraded to opportunistic product/roadmap signal.
The trigger existed to catch a qualifying buyer **before M6 froze the write path** — because the cost of getting the write-path-encryption seam wrong was irreversible. **M6 is now frozen, and it froze in the *correct* posture:** M6.3 shipped encrypt-on-write for `[identity, presence_personal]` with per-scope KEK/DEK (M6.2) + durable counter-nonce — so **future shreddability is fully preserved** (destroy a scope KEK -> that scope crypto-shredded; chain + other scopes intact). Per the interview guide's own logic, the only thing the trigger ever changed was whether the shred **operation** (the KEK-destruction API + erasure UI + the "demonstrate erasure to an auditor with retained audit log" capability, Doc 15 §3.6) ships at MVP vs post-MVP. **A late buyer-"yes" now costs only *scheduling* that operation (a recoverable feature WU) — NOT the irreversible seam.** The asymmetry that justified running the interviews at a low hit-rate has collapsed.

Layered on top: the desk research's base rate (H-A1 FALSE/RARE) and the PM-driven clause-language follow-up (return 2) both say a **contracted** crypto-shred-with-tamper-evident-audit-log requirement is **rare** — the contractual norm is "return or destroy + certify in writing" (attestation). So a qualifying YES was always unlikely, and now even a YES isn't write-path-decision-grade.

**Ruling:** the dedicated erasure interviews are **no longer decision-grade-urgent**; do not run a dedicated erasure-interview push for the AMD-86 trigger. Residual value is **opportunistic**: if Nick is in institutional conversations anyway, keep ONLY the A3 "show me the clause" falsifier as a cheap, high-signal probe — but **reframed** as PRODUCT/ROADMAP signal (when to schedule the Doc 15 §3.6 shred operation; Assure/Care institutional positioning; an input to the **parked** crypto lane — app-bootstrap + R-α + the key-portability brief, which already requires that backup/restore preserve crypto-shred). It is NOT an AMD-86 re-open. (Full re-scoped ask: `context/assessments/2026-06-15_M5-D_erasure-interview_RESCOPED_brief.md`.)

**Net for Nick's in-person time:** Track A worth = **low** (opportunistic only); Track B worth = **zero now** (parked to the energy milestone). This frees the in-person lane.

## The PM-driven follow-up (handoff §4 — the next deep-research angle, DRIVEN this session)
Ran the Track-A **procurement / clause-language** angle (kit Angle 2) via a web-grounded research sub-session to fill CAVEAT-3. Result (`…ANGLE2-clause-language_TrackA.md`): **verifiable cryptographic erasure + a retained tamper-evident audit trail is RARE as contracted language.** Near-universal is "return or destroy + certify in writing" (EU SCC Clause 8.5 verbatim; CAIQ DSP-02.1 yes/no; ISO 27001 A.8.10 one sentence; SOC 2 C1.2 method-agnostic; DPA/BAA boilerplate). Rigorous proof (NIST 800-88 cert, NAID AAA, HIPAA) is **media/ITAD** documentation, not SaaS per-tenant cryptographic proof. Honest counter-signal: 2024–2026 buyers are pushing past self-attestation, and NIST 800-88 r2 (Sep 2025) blesses CE + "searchable and tamper-evident" sanitization docs — the building blocks are legitimate and increasingly cited, just **not yet crystallized into standard contract clauses.** This both **confirms the first return's base rate from a second angle** and gives Nick the **A3 recognition vocabulary** (the three registers + the killer "name the method AND the retained artifact" follow-up). Honest gaps: SIG verbatim paywalled; SOC2/HITRUST/NIST-appendix specifics secondary.

## Disposition + routing
- **Both returns are VERIFIED BACKGROUND/EVIDENCE — not decisions, not FINDINGS.** Return 1 rehomed to docs `research/returns/` (md5-identical); return 2 lives in the interview-prep lane. This assessment is the citable hivemind artifact.
- **-> Erasure roadmap / crypto lane (parked):** the shred *operation* (Doc 15 §3.6) is a post-MVP feature WU whose **priority** the interviews/clauses inform; it interacts with R-α backup/restore + the key-portability brief (recovery must preserve crypto-shred). No action now; tracked.
- **-> Strategy positioning:** the defensible posture is "standard attestation already satisfies the law; verifiable cryptographic erasure + a tamper-evident log is where we *exceed* it" — a differentiator, **never** positioned as a legal mandate (no primary source makes it one). The EDPB Feb-2026 "demonstrate such erasure" direction + the 2024–2026 "harder proof" trend are the tailwind to cite honestly.
- **-> Future energy/Grid milestone:** author the regret-proof energy shape from the desk findings (above); validate with a real Grid buyer only if one is in hand.
- **-> No Core/M7 impact.** This lane blocks nothing on the interview-independent path (M7.1 issued; proceeding).

## Escalations / guardrails (carry to Nick; do not decide)
- **AMD-86 / Doc 15 stay inviolate** — no edit except the formal re-open -> DOCS review -> ratify pipeline. Nothing here trips it (the trigger is moot, not tripped).
- The **shred-operation scheduling** (MVP-adjacent vs post-MVP) is a product/roadmap call for Nick when the crypto lane un-parks (post-interview).
- The **energy event shape** is a future-milestone design call (desk-research-ready).

## Commit message (handed to Nick — bang-free, quote-free; git commit -F)
```
docs(assess): M5-D desk-research assessment + Track-A/B adjudication; rehome erasure-energy return

PM assessment of the interview-coaching lane desk research (verifiable erasure /
DER settlement telemetry). Grade A-: honestly-calibrated, primary-sourced, base-
rate-first. Verification ledger: all four load-bearing post-2025 clusters checked
against primary/reputable sources and CONFIRMED (EDPB 2025 CEF right-to-erasure
report 764 controllers / 9 formal investigations / 32 SAs / Feb-2026 / demonstrate-
such-erasure; NIST SP 800-88 Rev.2 final 26 Sep 2025, crypto-erase = optional purge;
20 US state privacy laws in effect 2026 + IN/KY/RI on 1 Jan 2026; FERC Order 2222
SPP Q2-2030 / MISO 2027-2029 / PJM ~Feb-2028). No fabrication.

Adjudication: Track B (energy/C9) CLOSED for interview purposes (C9-shape was NOT
ratified -- only B2 C8 actorRef stamping was -- but energy is post-MVP, zero energy
event types exist, the shape is desk-research-answerable, and it gates nothing; the
regret-proof freeze point is the future energy milestone, not now). Track A erasure
trigger MOOT: M6 froze the write path in the correct encrypt-on-write posture, so a
late buyer-yes costs only scheduling the post-MVP shred operation, not the
irreversible seam; interviews downgraded to opportunistic A3 product/roadmap signal,
NOT an AMD-86 re-open.

Drove the next angle (Track-A procurement/clause-language) to fill the return CAVEAT-3:
verifiable cryptographic erasure + tamper-evident audit log is RARE as contracted
language; the norm is return-or-destroy + certify-in-writing (SCC Clause 8.5, CAIQ
DSP-02.1, ISO 27001 A.8.10, SOC 2 C1.2). Confirms the base rate; gives the A3
recognition vocabulary.

Return rehomed to research/returns/ (md5-verified). Background/evidence, not a
decision. AMD-86 / Doc 15 untouched (formal pipeline only). No Core/M7 impact.

Files: context/assessments/2026-06-15_M5-D_desk-research_PM_Assessment.md
       homesynapse-core-docs/research/returns/2026-06-15_M5-D_desk-research_erasure-energy_background_RETURN.md
       track1-interview-coaching/2026-06-15_M5-D_desk-research_ANGLE2-clause-language_TrackA.md
```

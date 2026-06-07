<!--
file: context/assessments/2026-06-07_M5-D_energy-erasure_interview_guide.md
purpose: M5-D evidence lane — a structured, Mom-Test interview guide for the launch-window energy/institutional conversations. Two instruments: (A) the verifiable-erasure questions = the AMD-86 §3 re-scope-up trigger (a launch-window buyer requiring operational crypto-shredding re-opens AMD-86 BEFORE M6 freezes the write path); (B) the energy-data shape questions (D4 shape-now-features-later) that lock the regret-proof MVP energy event shape. PM authors the instrument; Nick runs the interviews.
audience: Nick (runs the interviews), PM
update-cadence: once (instrument), then the FINDINGS block is filled as interviews land
state-type: decision-support / instrument
status: GUIDE READY — awaiting interviews. Independently reviewed 2026-06-07 (separate agent, adversarial re-derivation vs source) → RATIFY (clean; the AMD-86 §3 trigger framing + the strategy grounding verified to source); two suggested edits folded.
last-verified: 2026-06-07 against AMD-86 §3 (RATIFIED), decision D2/D4, Doc 15 (LOCKED) §3.4/§3.6, the language-replatform assessment §5.2 (the Mom-Test template this extends), and the strategy layer (data-readiness §1/§4/§6; institution report Part 3; data-value engine Part 4/5).
guardrail: ONLY these erasure interviews can trigger an AMD-86 re-open — and only via the formal AMD pipeline (re-open → DOCS review → ratify). The interviewer never edits AMD-86 or Doc 15. Locked Doc 15 stays inviolate.
-->

# M5-D — Energy + Erasure Interview Guide (Mom-Test instrument)

**Lane:** M5-D (evidence / commissioned). **Owner of the run:** Nick. **Author:** PM.
**Two decisions this feeds:**
1. **The AMD-86 §3 re-scope-up trigger** — does any launch-window buyer *require* operational crypto-shredding (verifiable erasure)? A qualifying "yes" re-opens AMD-86 **before M6 freezes the write path** (via the formal pipeline).
2. **The regret-proof MVP energy event *shape* (decision D4 / C9)** — what energy fields/granularity must the MVP shape expose so post-MVP energy features (NexSys Grid/VPP, Assure energy attestation) are **non-breaking** on the immutable log?

---

## 0. How to use this — the Mom-Test discipline (read first)

This extends the language-replatform assessment's §5.2 Mom-Test questions (`context/assessments/2026-06-06_core-language-replatform-assessment.md` §5.2). The rule (Rob Fitzpatrick's *The Mom Test*): **never ask "would you want X?"** — everyone says yes. Ask about **past behavior, real budgets, and current pain.** "Have you ever paid for verifiable erasure / put it in an RFP?" beats "do you need verifiable erasure?" A vague "that'd be nice" is a **NO** for trigger purposes; a "yes, here's the contract/RFP/regulatory clause" is a **YES**.

**Grounding, not personas.** The audiences below are the real institutional motions in the strategy layer — NexSys **Grid** (utilities / VPP / DER aggregators), NexSys **Assure** (insurers), NexSys **Care** (healthcare / aging-in-place), and any launch-window data-sharing pilot. Do not invent personas; interview the buyers these products actually target (`From_Platform_to_Institution_NexSys_Strategic_Report.docx` Part 3; `Revenue_Model_and_Licensing_Strategy.md` post-MVP streams).

**What's genuinely at stake (so you read the answers correctly):**

- **Encrypt-on-write is already MVP regardless of these interviews.** Per Doc 15 §3.4 + AMD-86 §2, the sensitive-PII categories (`identity`, `presence_personal`) are written **encrypted-per-scope from launch** — so future shreddability is preserved no matter what. The **only** thing the erasure trigger changes is whether the **shred *operation*** (the KEK-destruction API + erasure triggers/UI — Doc 15 §3.6) ships **at MVP** instead of post-MVP. A "no" loses **no** future optionality; it just defers the operation. Don't over-read a soft "yes."
- **The trigger re-sizes M6.** Re-opening AMD-86 to pull operational crypto-shred into MVP would size **M6 UP** (M6 would build the shred operation, not just the key-management infrastructure). That is exactly why the call must be made **before M6 freezes the write path** — and why the bar for tripping it is high.

---

## PART A — The verifiable-erasure questions (the AMD-86 §3 re-scope-up trigger)

**Audience:** institutional buyers most likely to impose erasure terms — **Care/healthcare** (HIPAA + right-to-erasure + retained audit log is where this bites hardest), **Assure/insurers**, **Grid/utilities** with data-sharing agreements, and any **GDPR/CCPA-driven** launch-window data-sharing pilot.

**The distinction every answer must be scored against (this is the whole game):**

| Capability the buyer describes | Trips the trigger? | Why |
|---|---|---|
| "We want to be able to **delete a customer's data**" (wipe everything for that home) | **NO** | Served by **whole-installation reset** at MVP (Doc 15 §3.6, D2). No crypto-shred needed. |
| "Data subjects can **revoke consent** and we stop sharing" | **NO (mostly)** | The Data Sovereignty API (post-MVP) revokes *future* sharing; stopping a data flow ≠ destroying retained data. |
| "We must **provably, irreversibly erase a specific data subject's / a specific scope's data, while RETAINING the immutable audit log**, and demonstrate the erasure to an auditor/regulator" | **YES** | This is **operational crypto-shredding** (Doc 15 §3.6 / INV-PD-07): destroy the scope KEK → that scope unreadable, chain + every other scope still valid. The immutability-vs-erasure tension only this resolves. |
| "Our **contract/RFP/regulation** names provable cryptographic destruction / certified erasure with a retained tamper-evident record, on a **launch-window timeline**" | **YES (qualifying)** | A real, near-term, contracted requirement — the high bar that justifies re-sizing M6. |

**The questions (ask in order; the later ones only matter if an earlier one opens the door):**

**A1.** *"Walk me through the last time a customer or regulator made you delete or erase data. What exactly did you have to do, what did you have to prove, and to whom?"*
— **Tests:** real past erasure behavior and whether *proof* (not just deletion) was required. Listen for "we had to certify/attest/show an auditor."
— **Decision it feeds:** AMD-86 re-open (Y/N). **Threshold:** an answer describing **provable** erasure **with a retained audit record** → escalate to A2/A3. "We just deleted the account" → NO.

**A2.** *"When you erase a data subject's records, do you also have to KEEP an audit trail proving the rest of the history is intact — i.e., erase the data but retain a tamper-evident log that it happened?"*
— **Tests:** the exact immutability-vs-erasure conflict crypto-shredding exists for. This is the discriminator between "whole-install reset" (no retained log) and "crypto-shred" (erase scope, retain chain).
— **Decision it feeds:** AMD-86 re-open. **Threshold:** "yes, we must retain the audit log AND prove the PII is gone" → strong trigger signal; proceed to A4/A5.

**A3.** *"Has 'cryptographic erasure,' 'crypto-shredding,' 'certified destruction,' or 'verifiable deletion' ever appeared in one of your RFPs, security reviews, data-processing agreements, or compliance audits? Can you show me the clause?"*
— **Tests (Mom-Test core):** whether this is a real procurement line item vs an engineer's wish. The "show me the clause" is the falsifier.
— **Decision it feeds:** AMD-86 re-open. **Threshold:** a **named clause in a real document** the buyer would transact on → qualifying YES.

**A4.** *"If you were piloting with us in the next [launch window], would provable per-scope/per-subject erasure be a **go/no-go** to sign — or a roadmap item you'd accept landing later?"*
— **Tests:** timeline-binding. The trigger is specifically about the **launch window** (before M6 freezes the write path). A "roadmap item, fine later" answer means the post-MVP default holds.
— **Decision it feeds:** AMD-86 re-open **timing**. **Threshold:** "**go/no-go to sign in the launch window**" from a buyer who will actually sign → trips the trigger. "Nice, but later is fine" → NO (post-MVP default holds; future shreddability already preserved by encrypt-on-write).

**A5.** *"Which regulation or standard actually forces this for you, and on what timeline — GDPR Art. 17 with a retained audit log, HIPAA, a state privacy law, a data-sharing agreement clause?"*
— **Tests:** the real compliance gate and its date (especially relevant for **Care**/HIPAA and EU-facing **Grid/Assure** partners).
— **Decision it feeds:** AMD-86 re-open + how to scope it. **Threshold:** a **mandatory, dated** regime that binds within the launch/M6 window → qualifying YES.

### A — Decision rule (what tally trips the AMD-86 re-open)

- **TRIGGER TRIPPED →** escalate to re-open AMD-86 **iff ≥ 1 launch-window buyer is a qualifying YES**: a real, near-term/contracted/LOI-or-RFP-or-regulation requirement for **operational, verifiable, per-scope/per-subject crypto-shredding with a retained audit log**, that is **go/no-go to sign within the launch window** (A3 clause OR A4 go/no-go OR A5 mandatory-dated, with A1/A2 confirming it is *provable erasure + retained log*, not whole-install-reset). The bar is **one** genuine buyer — because the cost of getting the write-path-encryption seam wrong is irreversible, a single real, contracted requirement is decision-grade.
- **TRIGGER NOT TRIPPED →** the D2 / AMD-86 default holds: operational crypto-shred stays **post-MVP**; the sensitive categories are still encrypted-on-write at MVP (shreddability preserved); record the interviews as "erasure not launch-window-binding" in the findings block and the OR / M6 sizing notes.
- **What "escalate" means (the guardrail):** write an `ESCALATION TO NICK` with the qualifying evidence and recommend re-opening AMD-86 **through the formal AMD pipeline** (re-open AMD-86 → full DOCS-Project review → ratify) **before M6 starts/freezes**. **The interviewer/PM does NOT edit AMD-86 or Doc 15 directly** — only the formal pipeline moves a ratified privacy invariant. This is the explicit M5-D guardrail.

> **Honest expectation (so a "no" isn't read as a failure to probe).** The institutional products that would impose this (Assure, Care, Grid data-sharing, the Data Sovereignty API) are **post-MVP** (`From_Platform_to_Institution...` Part 3/Part 6; data-value engine Phase 3–4). Most current insurer programs "require only proof of installation and activation, not continuous data streams," and the attestation model means **institutions receive signed attestations, not raw data** — so launch-window erasure pressure is *structurally low*. A well-run interview set most likely returns **NOT TRIPPED**. The value of asking is that the *one* exception (an early Care/HIPAA pilot, an EU institutional partner with an Art. 17 clause) is caught **before** the write path freezes — which is the entire point of running it now.

---

## PART B — The energy-data shape questions (D4: shape now, features later)

**Audience:** energy/grid B2B buyers — utilities, VPP/DER aggregators, grid-services desks (the §5.2-A audience) — plus anyone who has actually integrated DER telemetry for settlement.

**What's being decided (and what's NOT):** decision **D4** is *shape now, features later* — author the **regret-proof MVP energy event shape (C9)** so post-MVP energy features don't require a breaking schema/log change. The MVP already generates energy telemetry from day one via Zigbee smart plugs (`data-readiness §4`: `instantaneous_power`, `accumulated_energy`, `voltage`, `current`; aggregates: total consumption Wh, total production Wh, net import/export, peak power w/ timestamp, cost estimate, self-consumption ratio). These questions test whether that shape has a **field or granularity gap** a real settlement/attestation process would need — because the event log is immutable, so a missing field is a now-or-never cost (same logic as D2/erasure). **Do NOT build energy features from these answers** (D4) — only confirm/extend the shape.

**The questions:**

**B1.** *"Walk me through the data you actually ingest to settle a VPP dispatch or DR event. What fields, what time granularity, and what accuracy — in numbers — from your last DER integration?"*
— **Tests (Mom-Test):** real settlement data requirements vs aspiration. OpenADR/FERC-2222 settlement is second-to-minute (language assessment §2.2) — listen for the actual interval (1 s? 1 min? 15 min?) and whether they need **interval-boundary alignment** (clock-aligned 15-min intervals) and **revenue-grade accuracy** flags.
— **Decision it feeds:** the C9 energy shape — sampling-interval / aggregation-window field + timestamp precision + an accuracy/provenance flag.
— **Threshold:** a **named granularity or accuracy** the MVP shape can't currently express (e.g., sub-second timestamps, clock-aligned interval markers, measurement-uncertainty flag) → add the field/metadata slot to C9 **now**.

**B2.** *"Beyond consumption, which of these do you require for settlement or capacity estimation: production (Wh), net import/export, reactive power / power factor, voltage, current, frequency, phase, battery state of charge, EV-charge state?"*
— **Tests:** the field set. The data-value engine says "NexSys Grid requires energy telemetry, **battery state, EV status**" — and grid services sometimes need **reactive power / power factor / frequency**, which the current shape (real power, Wh, V, I) doesn't carry.
— **Decision it feeds:** C9 — whether the energy entity shape needs **slots for production / battery SoC / EV state / reactive power / frequency** even though no MVP device produces them (so adding them in Tier-2 is non-breaking — `data-readiness §4`: "the pipeline architecture cannot be safely changed under load").
— **Threshold:** a field a **real buyer's settlement/capacity process** requires → reserve the slot in the C9 shape now (shape, not feature).

**B3.** *"What do you require to TRUST an energy number for settlement money to change hands — a meter certification, a signature, a tamper-evident audit trail, a specific measurement standard (e.g., revenue-grade metering, IEEE/ANSI class)?"*
— **Tests:** whether the moat-relevant asset is the **auditable, tamper-evident event log** (which NexSys already has — Doc 15 hash chain) and whether the energy event needs **measurement provenance** (which meter/CT produced it, with what accuracy class).
— **Decision it feeds:** C9 — a **measurement-provenance / source-device-identity** field on the energy event; and confirms the hash-chain (Doc 15) is the trust substrate (no shape change needed for that part).
— **Threshold:** "we need provenance / certified-source attribution per reading" → add a provenance slot to C9.

**B4.** *"Do you settle/attribute per-circuit or per-appliance, or only whole-home? And do you need the reading tied to a stable device identity that survives a device swap?"*
— **Tests:** granularity of attribution + whether the **three-layer identity model** (ULID binding keys survive device replacement — Six Battlefields §6) must thread into the energy event so a swapped meter doesn't break a settlement series.
— **Decision it feeds:** C9 — per-circuit/per-entity attribution + stable entity-identity reference on the energy event.
— **Threshold:** "we attribute per-circuit and need continuity across device swaps" → ensure the energy event carries the stable entity identity (likely already true via the envelope; confirm it's in the *energy* shape).

**B5.** *"For tariff/cost and price-responsive dispatch — do you send a price/DR signal the home acts on, and do you need the home's response recorded against that signal for settlement?"*
— **Tests:** whether the energy event/aggregate needs a **tariff-reference / price-signal-correlation** slot (the aggregate spec has "cost estimate if tariff data is available" — but settlement may need the *signal* the response was measured against, correlated via the envelope's correlation/causation IDs).
— **Decision it feeds:** C9 — a tariff/price-signal-reference field (or confirmation that correlation/causation IDs + a price-signal event suffice without an energy-shape change).
— **Threshold:** "we settle response-against-signal" → ensure the shape (or the correlated signal event) can express it without a future breaking change.

### B — Decision rule (what requires an energy-shape addition NOW)

- **ADD TO THE C9 SHAPE NOW** any field, granularity, metadata slot, or identity reference that (i) a **real** buyer's **actual** settlement/attestation/capacity process requires (Mom-Test: from past integrations or named contracts, not "would be nice"), AND (ii) **cannot be added later without a breaking change** to the immutable log / persisted event shape. Reserve the slot even if no MVP device populates it ("shape now"). Record each addition with the buyer evidence that justified it.
- **DO NOT ADD** anything justified only by "that'd be useful" or that can be derived/added later non-breakingly (e.g., a pure aggregate computable from already-captured fields, or anything addable as a new event type without touching existing rows).
- **DO NOT BUILD FEATURES** (D4): VPP enrollment, settlement engines, dashboards, price-response automations are all post-MVP. The output of Part B is a **shape decision (C9)**, authored as a regret-proof energy event/entity schema artifact that passes the contract-freeze-readiness gate (round-trips / enforceable / owner-doc) — same bar as every M5-B schema decision.
- **Guardrail:** energy stays **plaintext-at-rest at MVP** (Doc 15 §3.4) — the energy *shape* work (C9) is independent of the encrypted-scope set (OQ-15-2). Nothing in Part B changes the encrypted-scope list or touches Doc 15. *(Reconciliation, symmetric with the microbench spec: the strategy layer — data-readiness §1/§6 — labels energy a "sensitive / crypto-shred scope," but **Locked Doc 15 §3.4 governs** — energy is plaintext-at-rest at MVP; encrypting it is a Doc 15 §14 post-MVP item, not an MVP shape or scope question.)*

---

## FINDINGS — (empty until interviews land)

```
PART A — Verifiable-erasure (AMD-86 §3 trigger)
  Buyer / segment: __________  (Grid / Assure / Care / data-sharing pilot)
  A1 past erasure + proof required?  ____   A2 erase-but-retain-audit-log?  ____
  A3 named clause in RFP/DPA/audit?  ____   A4 go/no-go in launch window?  ____   A5 mandatory regime + date?  ____
  → Qualifying YES?  NO / YES   (if YES, attach the evidence)
  ... (repeat per buyer) ...
  AGGREGATE: ≥1 qualifying YES?  → TRIGGER TRIPPED (escalate: re-open AMD-86 via formal pipeline BEFORE M6) / NOT TRIPPED (default holds)

PART B — Energy shape (D4 / C9)
  Buyer / segment: __________
  B1 granularity/accuracy gap: __________   B2 required fields beyond {power,Wh,V,I}: __________
  B3 provenance/trust requirement: __________   B4 per-circuit + identity-continuity: __________   B5 tariff/price-signal: __________
  → Shape additions required NOW (field + the buyer evidence + why non-breaking-later is impossible): __________
  AGGREGATE C9 shape decision: __________   (authored as the regret-proof energy event/entity schema artifact)

Escalations raised (ESCALATION TO NICK): __________
```

---

## Appendix — source citations

- **The trigger:** AMD-86 §3 ("The M5-D energy/institutional interviews carry the **verifiable-erasure question** as the re-scope-up trigger — if a launch-window buyer requires it, this amendment is revisited *before* M6 freezes the write path"); decision D2 + sub-decision (`context/decisions/2026-06-06_post-M4_M5-window_decisions.md`); Doc 15 §3.6 (crypto-shred operation post-MVP; whole-install reset is the MVP recourse), §3.4 (encrypt-on-write at MVP preserves shreddability).
- **Energy shape (D4):** decision D4; `context/strategy/HomeSynapse_MVP_Data_Readiness_Specification.docx` §4 (energy entity template, power_measurement attributes, aggregate output fields, Path 1/Path 2, "pipeline architecture cannot be safely changed under load"); `NexSys_Data_Value_Engine_Strategy.docx` Part 4 ("Grid requires energy telemetry, battery state, EV status"); `From_Platform_to_Institution...` Part 3 (OpenADR 3.x / FERC 2222; second-to-minute settlement).
- **Mom-Test template extended:** `context/assessments/2026-06-06_core-language-replatform-assessment.md` §5.2 (A. energy/grid B2B; B. insurance/healthcare institutional; the "don't ask would-you-want, ask past-behavior" rule).
- **Institutional buyers (not invented personas):** `Revenue_Model_and_Licensing_Strategy.md` (NexSys Grid/Assure/Care post-MVP streams); `From_Platform_to_Institution...` Part 3 (Grid as VPP middleware; Assure as privacy-preserving attestation — "insurers receive only the attestation, not raw data"; Care as ambient monitoring).
- **Trust substrate (no shape change needed for it):** Doc 15 hash chain (§3.3); Six Battlefields §5 (Energy Intelligence), §6 (identity survives device swap).

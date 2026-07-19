<!--
file: context/programs/matter-design/00_PROGRAM_STATUS.md
purpose: Program-of-record status file for the Matter/Integrations Design Program — phase tracker, §-beat log, ruling ledger, audit protocol, and lane launch lines. The MAIN hub (v34+) consumes §-pointer beats from THIS file; the program hub is its only writer.
audience: the program hub (single writer); Nick (rulings + purchases); the MAIN hub (pointer consumption only).
state-type: current (program-scoped; NO project spine state lives here — HEADs, watermarks, milestone status re-derive at the spine per truth-hierarchy).
status: CURRENT — beat 1 (launch), 2026-07-19.
charter: context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md (RULED by Nick 2026-07-19 — pm-handoff v33 beat 5, verbatim there).
write-isolation (ABSOLUTE): this program writes ONLY under context/programs/matter-design/. Never the spine, never core/docs/bench/skills. Commits are Nick's, ordered with exact counts per env-model §10.
-->

# Matter/Integrations Design Program — Status

**Mission:** the complete pre-code pipeline for the next integrations, Matter first: research fan-out (A) → one-turn-rulable deliberation memos (B) → a Doc-19-class design draft + independent adversarial review (C) → the implementation plan + Matter bench charter (D). **ZERO code. Never a core write. Never gate work.**

**The standing price (Nick's ruling, unchanged):** the Gen4 Shelly plugs stay stimulus-only, radios NEVER provisioned · J1 is FROZEN (the mid-Aug criteria checklist is ratified; criteria-draft §2 NON-criteria item 2 explicitly fences multi-protocol out of the gate) · code sequencing stays the MAIN hub's post-M14-sweep call, and never before the Doc-19 Lock.

---

## Phase tracker

| Phase | Item | State | Artifact |
|---|---|---|---|
| A | A1 stack survey | **AUTHORED — dispatch on Nick's word** | `dispatches/2026-07-19_A1_stack-survey_lane_prompt.md` → `returns/A1_stack-survey_return.md` |
| A | A2 transport + hardware | **AUTHORED — dispatch on Nick's word** | `dispatches/2026-07-19_A2_transport-and-hardware_lane_prompt.md` → `returns/A2_transport-and-hardware_return.md` |
| A | A3 architecture fit | **AUTHORED — dispatch on Nick's word** | `dispatches/2026-07-19_A3_architecture-fit_lane_prompt.md` → `returns/A3_architecture-fit_return.md` |
| A | A4 moat translation | **AUTHORED — dispatch on Nick's word** | `dispatches/2026-07-19_A4_moat-translation_lane_prompt.md` → `returns/A4_moat-translation_return.md` |
| A | A5 integration #2 + certification | **AUTHORED — dispatch on Nick's word** | `dispatches/2026-07-19_A5_integration-2-and-certification_lane_prompt.md` → `returns/A5_integration-2-and-certification_return.md` |
| B | B1 stack choice · B2 V1-Matter scope cut · B3 DUT purchase list + budget · B4 certification posture · B5 integration-#2 sequencing | PENDING (authored after A returns + two-layer audits; AMD-99 R-A..R-E ruling-box pattern, REC + default per question) | `memos/` |
| C | Doc-19-class design draft (13-section DESIGN_DOC_TEMPLATE bar) → independent adversarial review → fold | PENDING (gated on B rulings) | `design/` |
| D | Implementation plan (P1-sized milestones · interface-spec obligations · coding-instruction sequence · Matter bench/test charter · hardware/install impacts · entry gate) | PENDING (gated on C) | `plan/` |

**Lane launch lines (Nick — fresh Cowork conversation each; lanes may run in parallel; each is write-isolated to its ONE return file):**

```
Follow all instructions in nexsys-hivemind/context/programs/matter-design/dispatches/2026-07-19_A1_stack-survey_lane_prompt.md
Follow all instructions in nexsys-hivemind/context/programs/matter-design/dispatches/2026-07-19_A2_transport-and-hardware_lane_prompt.md
Follow all instructions in nexsys-hivemind/context/programs/matter-design/dispatches/2026-07-19_A3_architecture-fit_lane_prompt.md
Follow all instructions in nexsys-hivemind/context/programs/matter-design/dispatches/2026-07-19_A4_moat-translation_lane_prompt.md
Follow all instructions in nexsys-hivemind/context/programs/matter-design/dispatches/2026-07-19_A5_integration-2-and-certification_lane_prompt.md
```

Do NOT load the nexsys-project-manager skill in the lanes — they are research lanes, not the PM hub. A1/A2/A4/A5 are web-research-heavy; A3 is repo-read-heavy (its dispatch embeds the verbatim `module-info.java` per the Research-6 lesson).

---

## Audit protocol (standing — every return)

Two-layer, the v28+ discipline: **layer 1** = the lane's own evidence tags ([VERIFIED-current + URL + fetch-date] / [community-reported] / [inference] / [banked: path §]); **layer 2** = hub adjudication of every load-bearing claim against PRIMARY sources (spot re-fetches for web claims; repo reads at source for code/doc claims) — labels are claims, quotes are evidence. Findings correct in place → delta re-audit → ACCEPT recorded here as a beat. Only ACCEPTED returns feed Phase B memos.

## STOP-and-escalate (to Nick, and where core-shaped, via the MAIN hub)

Anything implying a core change · any gate-criteria interaction (J1 FROZEN) · strategy calls (pricing, brand, certification spend — B4 packages the decision; Nick rules) · any hardware on the bench network (Matter DUTs are NEW purchases Nick rules at B3; lab-network isolation design rides A2 evidence) · anything touching the live fleet (5 devices / 5 entities on ch20/0x774c — the Matter program never perturbs it).

---

## Ruling ledger (verbatim, append-only; pointered onto the spine by the MAIN hub)

- **R-0 (2026-07-19, the chartering ruling — recorded pm-handoff v33 beat 5):** no hasty Matter code; commit real capacity NOW to all necessary research, deliberations/debate, full & comprehensive designs, and an implementation plan/procedure, coordinated by this dedicated program hub; everything ready for diving in. Price: Gen4 plugs stimulus-only radios-off · J1 FROZEN · no core writes from the program ever · code sequencing = the MAIN hub's post-sweep call.
- B1–B5: OPEN — memos pend Phase-A returns.

---

## §-beat log (newest first; the MAIN hub consumes these as pointers)

### 2026-07-19 — beat 1: PROGRAM LAUNCH — tree created · A1–A5 AUTHORED · dispatch on Nick's word

Launch grounding executed per the charter's required reads (roadmap return §§0/1/3/4–8 · Doc 18 · Doc 08 §§0–3 · integration-api MODULE_CONTEXT + module-info · Doc 17 · the doctrine brief · criteria §2 NON-criteria · Six Battlefields + Revenue Model · pm-handoff v33 beats 4–5 · the v34 prompt · W29/W30). Program-scoped freshness: PASS (snapshot/pm-handoff coherent at v33 beat 5, 2026-07-19; W30 pre-minted; no CONFLICTED signal; the full 11-check rides the v34 main-hub launch — this program takes no spine writes). Five lane dispatches authored to the dispatch-craft bar (baseline + baseline-shift + known-hazards + evidence/decision separation + one-return-file write isolation + two-layer-auditable evidence tags). **Next:** Nick launches lanes (any order, parallel-safe) → returns land in `returns/` → hub two-layer audits → Phase B memos.

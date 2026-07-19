<!--
file: context/programs/matter-design/00_PROGRAM_STATUS.md
purpose: Program-of-record status file for the Matter/Integrations Design Program — phase tracker, §-beat log, ruling ledger, audit protocol, and lane launch lines. The MAIN hub (v34+) consumes §-pointer beats from THIS file; the program hub is its only writer.
audience: the program hub (single writer); Nick (rulings + purchases); the MAIN hub (pointer consumption only).
state-type: current (program-scoped; NO project spine state lives here — HEADs, watermarks, milestone status re-derive at the spine per truth-hierarchy).
status: CURRENT — beat 2 (Phase A returned + audited; Phase B memos AWAITING RULINGS), 2026-07-19.
charter: context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md (RULED by Nick 2026-07-19 — pm-handoff v33 beat 5, verbatim there).
write-isolation (ABSOLUTE): this program writes ONLY under context/programs/matter-design/. Never the spine, never core/docs/bench/skills. Commits are Nick's, ordered with exact counts per env-model §10.
-->

# Matter/Integrations Design Program — Status

**Mission:** the complete pre-code pipeline for the next integrations, Matter first: research fan-out (A) → one-turn-rulable deliberation memos (B) → a Doc-19-class design draft + independent adversarial review (C) → the implementation plan + Matter bench charter (D). **ZERO code. Never a core write. Never gate work.**

**The standing price (Nick's ruling, unchanged):** the Gen4 Shelly plugs stay stimulus-only, radios NEVER provisioned · J1 is FROZEN (criteria-draft §2 item 2 fences multi-protocol out of the mid-Aug gate) · code sequencing stays the MAIN hub's post-M14-sweep call, and never before the Doc-19 Lock.

---

## Phase tracker

| Phase | Item | State | Artifact |
|---|---|---|---|
| A | A1 stack survey | **RETURNED + AUDITED: ACCEPT** | `returns/A1_stack-survey_return.md` |
| A | A2 transport + hardware | **RETURNED + AUDITED: ACCEPT** | `returns/A2_transport-and-hardware_return.md` |
| A | A3 architecture fit | **RETURNED + AUDITED: ACCEPT** | `returns/A3_architecture-fit_return.md` |
| A | A4 moat translation | **RETURNED + AUDITED: ACCEPT-WITH-NOTES** (the §8-7 named re-checks + the spec-verbatim pass ride Phase C as Q-A4-6) | `returns/A4_moat-translation_return.md` |
| A | A5 integration #2 + certification | **RETURNED + AUDITED: ACCEPT** | `returns/A5_integration-2-and-certification_return.md` |
| B | B1 stack · B2 scope cut · B3 DUTs/budget/isolation · B4 certification posture · B5 sequencing + spike | **AUTHORED — AWAITING NICK'S RULINGS (five boxes, one turn)** | `memos/2026-07-19_B1-B5_deliberation-memos.md` |
| C | Doc-19-class design draft → independent adversarial review → fold | PENDING (opens on B1/B2 rulings) | `design/` |
| D | Implementation plan + Matter bench charter + entry gate | PENDING (gated on C) | `plan/` |

## Audit protocol (standing — every return)

Two-layer, the v28+ discipline: **layer 1** = the lane's own evidence tags ([VERIFIED-current + URL + fetch-date] / [community-reported] / [inference] / [banked: path §]); **layer 2** = hub adjudication of every load-bearing claim against PRIMARY sources (spot re-fetches for web claims; repo reads at source for code/doc claims) — labels are claims, quotes are evidence. Findings correct in place → delta re-audit → ACCEPT recorded here as a beat. Only ACCEPTED returns feed Phase B memos.

## STOP-and-escalate (to Nick, and where core-shaped, via the MAIN hub)

Anything implying a core change · any gate-criteria interaction (J1 FROZEN) · strategy calls (pricing, brand, certification spend — B4 packages; Nick rules) · any hardware on the bench network (B3 rules DUTs; the isolation ruling precedes first commissioning) · anything touching the live fleet (5 devices / 5 entities on ch20/0x774c — the Matter program never perturbs it).

**Pointers for the MAIN hub (consume at leisure; nothing here blocks the program):**
- **Doc-drift ×2, layer-2 CONFIRMED at source:** Doc 12 §3.8 Step 6.1 still says integration discovery "uses ServiceLoader (LTD-17)" — as-built is the explicit factory list with ServiceLoader banned (DECIDE-04; ArchUnit `noServiceLoader`). Doc 18 §4 row 6 says `SchemaRegistry.registerIntegrationSchema` is "built, unwired" — it is production-wired (`HomeSynapseCore.java:1343/1350`). Both are docs-repo currency fixes on the MAIN hub's flow.
- **A future Doc-01-class contract question is coming from Phase C:** confirm-before-ack ordering (memo B2 item 7 / A4 Q-A4-1) — if the design needs Doc-01 §3.8 prose to change, that is an amendment through the MAIN hub, never this program.

---

## Ruling ledger (verbatim, append-only; pointered onto the spine by the MAIN hub)

- **R-0 (2026-07-19, the chartering ruling — recorded pm-handoff v33 beat 5):** no hasty Matter code; commit real capacity NOW to all necessary research, deliberations/debate, full & comprehensive designs, and an implementation plan/procedure, coordinated by this dedicated program hub; everything ready for diving in. Price: Gen4 plugs stimulus-only radios-off · J1 FROZEN · no core writes from the program ever · code sequencing = the MAIN hub's post-sweep call.
- **B1 (stack choice):** OPEN — memo delivered, REC (a) matterjs-server sidecar + four riders; default (a).
- **B2 (V1-Matter scope cut):** OPEN — memo delivered, REC controller-only / WiFi-Ethernet-first / A4-rows-1–3 wave 1 / bridges-in-design / IP+ECM-first commissioning; default as REC.
- **B3 (DUTs + budget + isolation):** OPEN — memo delivered, REC approve phase-1 core $265.94 (+ZBT-2 $48.95; MSS315 optional) · all-Shelly DUT exclusion AFFIRM · isolation Option C; default: no purchase.
- **B4 (certification posture):** OPEN — memo delivered, REC (a)→(c)@Hub-trigger + the $0 lab-quote rider + the Adopter-join reserve; default (a) de facto.
- **B5 (sequencing + spike):** OPEN — memo delivered, REC O1 reaffirm + RATIFY the spike re-charter (post-B1 + post-gate-read); default O1, no spike.

---

## §-beat log (newest first; the MAIN hub consumes these as pointers)

### 2026-07-19 — beat 2: ALL FIVE A-RETURNS IN → TWO-LAYER AUDIT ACCEPT ×5 → THE B1–B5 MEMOS AUTHORED — five ruling boxes await Nick

All five lanes returned same-day (~230 dated primary-source fetches across them). Hub layer-2 executed: **6/6 repo spot-checks CONFIRM at source over the bridge** (IsolationLevel javadoc · the supervisor's RESERVED_SUBPROCESS startup rejection · the SERIAL/virtual thread fork · the Zigbee SERIAL descriptor + its comment · the Doc-12 ServiceLoader drift · the schema-registration wiring) and **5/5 web spot-checks CONFIRM on re-fetch** (CSA fee table exact · matterjs-server VID default 0xFFF1 + the unauthenticated-WS warning · matter.js 0.17.5 Thread-gap closure + 1.6.0 · the TP-Link energy-cluster statement · the python-matter-server archive banner). Verdicts: A1/A2/A3/A5 ACCEPT · A4 ACCEPT-WITH-NOTES (mirror-tagged spec quotes honest; the named re-checks ride Phase C's verbatim pass). Three banked-base corrections accepted with evidence (openHAB record t/127907 · the "2–4 versions" phrasing · no maintained Java SPAKE2+). Headline movements since the 07-10 base: BLE→Thread name-gap CLOSED (matter.js 0.17.5) · matterjs-server GA-in-HA while README says Beta · python-matter-server archived read-only · #843 silent-subscription-death named as the day-one ALIVE bench scenario · zero WiFi battery sensing exists (the trigger layer is 100% Thread) · the CHIP SDK has no 1.6 tag a month after spec. **The B1–B5 memos are authored one-turn-rulable** (`memos/2026-07-19_B1-B5_deliberation-memos.md`): B1 REC matterjs-server sidecar + four riders (corpus-fidelity capture law · the IsolationLevel amendment named for the Lock · WS loopback law · custody rows) · B2 REC the scope cut (WiFi-first honestly framed "a phase, not a resting place") · B3 REC phase-1 DUTs $265.94 + ZBT-2 front-load + isolation Option C · B4 REC uncertified-honest-now → certify at the Hub trigger (+$0 lab-quote rider) · B5 REC reaffirm the standing order + ratify the spike re-charter. **Next: Nick rules the five boxes (one turn); Phase C opens on B1/B2.**

### 2026-07-19 — beat 1: PROGRAM LAUNCH — tree created · A1–A5 AUTHORED · dispatch on Nick's word

Launch grounding executed per the charter's required reads (roadmap return §§0/1/3/4–8 · Doc 18 · Doc 08 §§0–3 · integration-api MODULE_CONTEXT + module-info · Doc 17 · the doctrine brief · criteria §2 NON-criteria · Six Battlefields + Revenue Model · pm-handoff v33 beats 4–5 · the v34 prompt · W29/W30). Program-scoped freshness: PASS (snapshot/pm-handoff coherent at v33 beat 5, 2026-07-19; W30 pre-minted; no CONFLICTED signal; the full 11-check rides the v34 main-hub launch — this program takes no spine writes). Five lane dispatches authored to the dispatch-craft bar (baseline + baseline-shift + known-hazards + evidence/decision separation + one-return-file write isolation + two-layer-auditable evidence tags). **Next:** Nick launches lanes (any order, parallel-safe) → returns land in `returns/` → hub two-layer audits → Phase B memos.

<!--
file: context/programs/matter-design/00_PROGRAM_STATUS.md
purpose: Program-of-record status file for the Matter/Integrations Design Program — phase tracker, §-beat log, ruling ledger, audit protocol. The MAIN hub (v34+) consumes §-pointer beats from THIS file; the program hub is its only writer.
audience: the program hub (single writer); Nick (rulings + purchases); the MAIN hub (pointer consumption only).
state-type: current (program-scoped; NO project spine state lives here — HEADs, watermarks, milestone status re-derive at the spine per truth-hierarchy).
status: CURRENT — beat 3 (B1–B5 RULED; Phase C OPEN), 2026-07-19.
charter: context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md (RULED by Nick 2026-07-19 — pm-handoff v33 beat 5, verbatim there).
write-isolation (ABSOLUTE): this program writes ONLY under context/programs/matter-design/. Never the spine, never core/docs/bench/skills. Commits are Nick's, ordered with exact counts per env-model §10.
-->

# Matter/Integrations Design Program — Status

**Mission:** the complete pre-code pipeline for the next integrations, Matter first: research fan-out (A ✓) → one-turn-rulable deliberation memos (B ✓ RULED) → a Doc-19-class design draft + independent adversarial review (C — OPEN) → the implementation plan + Matter bench charter (D). **ZERO code. Never a core write. Never gate work.**

**The standing price (unchanged):** the Gen4 Shelly plugs stay stimulus-only, radios NEVER provisioned · J1 is FROZEN (criteria-draft §2 item 2 fences multi-protocol out of the mid-Aug gate) · code sequencing stays the MAIN hub's post-M14-sweep call, and never before the Doc-19 Lock.

---

## Phase tracker

| Phase | Item | State | Artifact |
|---|---|---|---|
| A | A1–A5 research lanes | **CLOSED — RETURNED + AUDITED ACCEPT ×5** (A4 accept-with-notes) + **Nick's independent re-derivation: 7/7 repo + 5/5 web CONFIRM, CONCUR** | `returns/` |
| B | B1–B5 deliberation memos | **RULED 2026-07-19 (Nick — all five, verbatim in the ledger below)** | `memos/2026-07-19_B1-B5_deliberation-memos.md` |
| C | Doc-19 design draft → independent adversarial review → fold | **OPEN** — the authoring charter is banked; the draft is the next work product | `design/2026-07-19_phase-C_design-charter.md` → `design/19-matter-integration_DRAFT.md` |
| C-side | The spike (ratified at B5) | CHARTERED-HELD: post-gate-read (after Sun 2026-08-16); DUT order per B3; +RSS measurement obligation (Nick's sharpening) | rides the charter §6 |
| C-side | C-1..C-4 counsel questions → the Pelton consult Mon 2026-07-21 | HAND-OFF CUT — Nick carries it into the counsel queue | `memos/2026-07-19_C1-C4_counsel-handoff_pelton.md` |
| C-side | B4-r1 lab-quote engagement ($0) | AUTHORIZED — request drafts cut for Nick's send | `memos/2026-07-19_B4-r1_lab-quote-request-drafts.md` |
| D | Implementation plan + Matter bench charter + entry gate | PENDING (gated on C) | `plan/` |

## Audit protocol (standing — every return)

Two-layer, the v28+ discipline: layer 1 = the lane's own evidence tags; layer 2 = hub adjudication of every load-bearing claim against PRIMARY sources — labels are claims, quotes are evidence. Only ACCEPTED returns feed memos. (Executed for A1–A5 at beat 2; independently re-derived by Nick at beat 3 — CONCUR.)

## STOP-and-escalate (to Nick, and where core-shaped, via the MAIN hub)

Anything implying a core change · any gate-criteria interaction (J1 FROZEN) · strategy calls · any hardware on the bench network (the isolation ruling [Option C] precedes first commissioning) · anything touching the live fleet (ch20/0x774c — never perturbed).

**Pointers for the MAIN hub:**
- **Doc-currency fixes ×3 — INTAKEN BY NICK onto his/the MAIN hub's flow (beat 3):** Doc 18's stale "built, unwired" in **two** places (§2/line 59 substrate list + §4 row 6/line 94 — Nick's own catch extended the program's row-6-only pointer) · Doc 12 §3.8 ServiceLoader text · Doc 12 watchdog/sd_notify text (A3 §9-NB5). Batched to a convenient docs-repo commit; nothing blocks on them.
- **Coming from Phase C:** the IsolationLevel/descriptor amendment PROPOSAL (ratifies at Lock, MAIN-hub flow) · the confirm-before-ack question (Q-A4-1) IF it needs Doc-01 §3.8 prose changes — amendment through the MAIN hub, never this program.

---

## Ruling ledger (verbatim, append-only; pointered onto the spine by the MAIN hub)

- **R-0 (2026-07-19, the chartering ruling — pm-handoff v33 beat 5):** no hasty Matter code; commit real capacity NOW to all necessary research, deliberations/debate, full & comprehensive designs, and an implementation plan/procedure. Price: Gen4 stimulus-only radios-off · J1 FROZEN · no core writes ever · code sequencing = the MAIN hub's post-sweep call.
- **B-HEADER (2026-07-19, Nick, verbatim):** *"Verdict: I CONCUR with the ACCEPT ×5 and second all five RECs. I did not take its audit on faith — I re-derived its layer-2 sample myself, at source and on the live web, before forming a view."* His record: 7/7 repo CONFIRM (incl. the full INV-RF-01 text — line-270 out-of-process pre-authorization + the "Addressed failure mode: Home Assistant's single-process architecture" line, *"[making] accepting whole-JVM death a self-refutation"*) · 5/5 web CONFIRM (#843's title adds *"wedge-mode reproduced on 1.2.2"* — stronger than the return's summary).
- **B1 — RULED (a) matterjs-server sidecar + ALL FOUR RIDERS.** Verbatim why: *"(b)/(c) violate INV-RF-01 as written — verified at the invariant's own text; (d) honestly priced at ~70–140 WUs with no maintained Java SPAKE2+ in existence; (a) is where the ecosystem's center of gravity provably moved (HA migrated one-way; openHAB converged independently; the predecessor is archived)."* Riders r1–r4 are Phase-C design LAW.
- **B2 — RULED as written.** Verbatim why: *"The scope cut is honest ('a phase, not a resting place'); ALIVE-as-law with #843 as the first scenario family is the doctrine transferring; the O1+O3 provenance direction is architecturally right and consistent with the S31 best_effort logic."*
- **B3 — RULED: approve phase-1 core + ZBT-2 front-load + isolation Option C.** Verbatim why: *"Option C is our own Zigbee posture (containment at the edge, never mid-path translation); ZBT-2 follows the ruled radios-front-load principle; the MSS315 checkbox is genuinely optional — my lean is take it ($53 for a second energy vendor's confirm envelopes), not load-bearing."* **Recorded: MSS315 IN per the stated lean** (droppable at order time without re-ruling). Order timing stands per the memo: at the spike charter (~post-Aug-17) or earlier at Nick's discretion; pre-order riders (CSA-DB per-SKU spot-check; re-verify the two single-citation prices) stand.
- **B4 — RULED (a) → (c) @ T1-Hub trigger + BOTH RIDERS.** Verbatim why: *"Free, honest, HA-normalized, totally reversible; the $0 lab quote converts a hardware-scoped ceiling into a real number; the Adopter-join reserve is a one-week fuse held for exactly the right moment."* **r1 lab-quote engagement AUTHORIZED** (drafts cut, beat 3); r2 Adopter-join held in reserve. C-1..C-4 ride the Pelton consult Mon 2026-07-21 (Nick's timing call, verbatim: *"hand them into that queue at zero marginal cost. Wording stays counsel's; nothing gates on the answers."*)
- **B5 — RULED: O1 reaffirm + RATIFY the spike re-charter.** Verbatim why: *"'The Lock binds, not the queue' is the load-bearing insight and it is correct — Matter-first buys zero acceleration and forfeits the substrate rehearsal; the spike's post-B1 + post-gate-read fencing protects the freeze window; J1 untouched."*
- **Phase-C sharpenings (Nick, 2026-07-19 — accepted as design rows, not ruling changes):** (1) **the Pi memory budget is a BLOCKING design row** — sidecar RAM has no published absolutes, sits outside `-Xmx` and JFR's sight; the spike produces first measured RSS; the design carries a priced total-device budget (JVM 2G cgroup + Node + OS on Pi-class). (2) **Pin Node 24.x LTS at packaging time** (22 floor hits security-EOL 2027-04-30, inside product life; 24.x runs to 2028). (3) B1-r1 underlined: capture doctrine priced INTO the stack choice *"is the difference between a corpus and testimony."*

---

## §-beat log (newest first; the MAIN hub consumes these as pointers)

### 2026-07-19 — beat 3: **B1–B5 RULED (all five, per REC — verbatim in the ledger)** · Phase C OPEN · the counsel hand-off + lab-quote drafts CUT

Nick concurred with the ACCEPT ×5 after independently re-deriving the layer-2 sample (7/7 repo at HEAD + 5/5 web — his record in the ledger; one strengthening find: #843 "wedge-mode reproduced on 1.2.2"; one correction-class catch: Doc 18's stale text appears in TWO places — the three docs-repo touches are intaken on HIS flow, nothing blocks). All five boxes ruled per REC; MSS315 in per the stated lean; the spike ratified post-gate-read; the lab-quote engagement authorized; his two sharpenings folded (Pi-memory-budget → BLOCKING · Node 24.x pin). **Cut this beat:** the Phase-C design charter (`design/2026-07-19_phase-C_design-charter.md` — the Doc-19 authoring brief: template §0–§16 map with per-section input inventory, the design-law list, the BLOCKING inventory, the adversarial-review lane plan, the continuation line) · the C-1..C-4 counsel hand-off for Monday's Pelton consult · the two B4-r1 quote-request drafts. **Next:** Nick hands the counsel file into the Pelton queue + sends the quote requests at leisure; the hub authors `design/19-matter-integration_DRAFT.md` per the charter (this conversation or a fresh program-hub session on the charter's launch line — ONE program-hub session at a time; this session retires the moment a successor launches).

### 2026-07-19 — beat 2: ALL FIVE A-RETURNS IN → TWO-LAYER AUDIT ACCEPT ×5 → THE B1–B5 MEMOS AUTHORED

All five lanes returned same-day (~230 dated primary-source fetches). Hub layer-2: 6/6 repo spot-checks CONFIRM at source (IsolationLevel javadoc · RESERVED_SUBPROCESS startup rejection · the SERIAL/virtual fork · the Zigbee SERIAL descriptor · the Doc-12 ServiceLoader drift · the schema-registration wiring) + 5/5 web spot-checks CONFIRM (CSA fees exact · VID default 0xFFF1 + the unauthenticated-WS warning · matter.js 0.17.5 Thread-gap closure + 1.6.0 · the TP-Link energy-cluster statement · the python-matter-server archive). Verdicts: A1/A2/A3/A5 ACCEPT · A4 ACCEPT-WITH-NOTES. Headlines since the 07-10 base: BLE→Thread name-gap CLOSED · matterjs-server GA-in-HA (README still Beta) · python-matter-server archived · #843 = the day-one ALIVE scenario · zero WiFi battery sensing exists · CHIP has no 1.6 tag. Memos authored one-turn-rulable.

### 2026-07-19 — beat 1: PROGRAM LAUNCH — tree created · A1–A5 AUTHORED · dispatched

Launch grounding per the charter's required reads; program-scoped freshness PASS; five lane dispatches authored to the dispatch-craft bar.

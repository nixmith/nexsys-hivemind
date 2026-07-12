<!--
file: context/assessments/2026-07-11_go-no-go-criteria_draft.md
purpose: DRAFT criteria checklist for the mid-August (~Aug 16) go/no-go — every criterion binary-or-measured, evidence-defined, MUST/SHOULD-tagged, with current status and the named evidence producer. Ends with the gate-day protocol sketch. Exists so the mid-Aug call is made on evidence, not vibes (Nick's ruling, v27 beat 3).
date: 2026-07-11 (lane return date; authored 2026-07-10 America/Chicago, soak day 1)
audience: Nick (rules the gate); the hub (evidence steward; carries ratified criteria into orchestration); the bench/frontend lanes (they produce the missing evidence).
state-type: assessment / decision-support DRAFT — becomes the gate artifact only on Nick's ratification.
status: **RATIFIED 2026-07-12 (Nick — verbatim rulings: pm-handoff v30 beat 2). The §RATIFICATION block below is the OPERATIVE layer** (statuses of record + Q1–Q4 applied + the I3a/I3b split + J1 FROZEN); the draft body beneath it is preserved as authored with its 2026-07-10 statuses. Prior status: RETURNED by the executive-briefs lane (Track B lane (c), dispatched v27 beat 3). Authored 2026-07-10 (America/Chicago), soak day 1; filed under the lane's 2026-07-11 return date. All statuses are as-of 2026-07-10 and go stale with every beat — the hub re-derives at ratification and again at gate day.
grounding: PROJECT_SNAPSHOT v27 beats 1–3 + the certified M9.4/M9.5 backlog row + the 15-row ruled post-soak stack (backlog, 2026-07-10) · nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md (iteration log + acceptance-run block + the 2026-07-10 correction) · MVP §2.2/§2.3/§4/§8 · Six_Battlefields_MVP_Strategy.md · context/planning/2026-06-28_mid-august-go-no-go_readiness-review.md (the four-gate frame this draft descends from) · pm-handoff v27 beats 1–3 (rulings verbatim).
-->

# Mid-August Go/No-Go — Criteria Draft (for ratification)

## RATIFICATION — 2026-07-12 (Nick; the operative layer; J1's process FROZEN)

RATIFIED by Nick 2026-07-12 (rulings verbatim: `context/handoff/pm-handoff.md` v30 beat 2). This block supersedes every in-table "Status 2026-07-10" cell per the draft's own §5. **J1 is FROZEN: no criterion is added, removed, re-tagged, or re-worded without an explicit Nick re-ruling recorded in pm-handoff.** The hub re-statuses once more at gate day, against artifacts only (§4).

**Rulings applied:** **Q1** — C1 = MUST N ≥ 200 · C1b = SHOULD N ≥ 500; ONE false CONFIRM at any N = automatic STOP + root-cause, overriding the count; the §1-C statistics + reachability assumption accepted as the basis of record. **Q2** — I3 SPLIT: **I3a [MUST]** = fix landed (✅ `1627978`+`3590fca`, CI-green) + B1's usb-reenumeration scenario green in the DIRECT-ATTACHED topology; **I3b [SHOULD]** = the hub-attached leg (Rosonway-gated — a MUST never depends on a third-party delivery). **Q3** — D1 = MUST 5 classes; D2 = SHOULD the button 6th (R2(B): the 01P adopts battery-only; presses log-visible, absent from the device model — deliberate scoping of record). **Q4** — the read = Sunday 2026-08-16; evidence-freeze = Friday 2026-08-14 EOD; nothing lands between freeze and read. **Carriers named** — A4 (kill −9): the first post-deploy bench session with spare minutes; H3 (clean-image fresh install): the named weekend slot Aug 8–9. **Tally after the split: 21 MUST · 8 SHOULD.**

**Adjudication of record (2026-07-12, ruled with the B1 contract ruling — rider 4; J1 stays FROZEN, nothing reopens):** I3a's frozen text ("B1's usb-reenumeration scenario green in the direct-attached topology") is **SATISFIED by B1's OPERATOR manual variant** — Nick, verbatim: *"the OPERATOR manual variant is one of B1's two tiers, so a green OPERATOR rep Monday satisfies the row as frozen. Record that adjudication with the ratification block so gate day reads it, not argues it."* Gate day reads this adjudication; it does not re-litigate the tier.

**Statuses of record as of 2026-07-12 (ratification re-status; the gate-day pass re-derives again):**

| Row | Tag | Status 2026-07-12 |
|---|---|---|
| A1 | M | IN PROGRESS — soak day 3 on `04f5f70`; exit ≥ 2026-07-13 ~07:50; RSS/log deltas recorded at close-out against the stated bounds |
| A2 | M | PENDING — Monday, runbook Phase 7 steps 20–26 verbatim |
| A3 | M | PENDING — Monday, after A1+A2 (the hub writes the close-out) |
| A4 | S | PENDING — carrier NAMED (ruled): the first post-deploy bench session with spare minutes |
| B1 | M | ✅ DONE (banked 2026-07-09/10; re-proven on 72 h-aged state by A2) |
| B2 | M | PENDING — the first Wave-2 bench session (Monday's pinned order, post-deploy) |
| C1 | M | IN PROGRESS — ~25/200 recorded verdicts, ZERO false. RATIFICATION NOTE (honesty): the reachability assumption's scriptable suite executions now ride the CMD-API WU (discovered 2026-07-12 — the v1.1 HTTP surface is READ-ONLY; no REST command stimulus exists; AUTO command scenarios are blocked until it lands; N accumulates via waves/OPERATOR meanwhile) |
| C1b | S | as C1 |
| C2 | M | organic proof ✅ banked; suite port PENDING (B2) — the commanded-to-current class needs CMD-API for AUTO; device-absent + rejoin classes are wave-drivable OPERATOR |
| C3 | M | proof ✅ banked (record positions 589/593/644); suite port PENDING (B2, same caveat) |
| C4 | S | PENDING — B2 assertion; instrument-first arm if event timestamps do not discriminate dispatch-vs-RTT |
| D1 | M | 2 of 5 classes; Wave-2 joins = Monday's pinned order; the four dossiers DELIVERED + audited (`ada8b46`) |
| D2 | S | PENDING — same sessions; R2(B) governs the button's shape |
| E1 | M | ✅ DONE — CODE-LANDED `a1f0f77` CI-green; full-bar two-layer audit ACCEPT (v28) |
| E2 | M | rail HELD to date; silicon leg PENDING — Monday (ONE fresh formation under the generated seed = the SD-5 discharge, composing with Wave-2 joins) |
| E3 | S | PENDING E2 |
| F1 | M | ✅ DONE — CODE-LANDED `1aa809d` CI-green; two-layer audit ACCEPT (v29) |
| F2 | M | PENDING — Monday silicon (SNZB-02P reports→AVAILABLE + a genuine offline leg; never-false-ALIVE both directions) |
| G1 | M | PENDING — the explainability-lane dispatch refresh is the hub's queued act (Tuesday-tolerant; ALSO an M14-trigger condition per R1b); FE-7's data path is live code-side per F1 |
| G2 | S | PENDING F2 + G1 |
| H1 | M | ✅ green on `1aa809d` (both workflows; continuous obligation to gate day) |
| H2 | M | IN MOTION — B0 ✅; B1 authored + dispatched → ⛔ G-B1-2 STOP 2026-07-12 (the command endpoints unwired; hub-owned grounding miss, corrected on the record — pm-handoff v30 beat 2); B1-reduced re-dispatch pending Nick's ruling; the FULL AUTO suite rides CMD-API |
| H3 | M | harness ✅ (install-smoke green standing); the clean-image rep = the NAMED slot Aug 8–9 |
| H4 | S | PENDING — Monday's deployed-build restart rep |
| I1 | M | ✅ banked; watch-rows OPEN by design, read at gate day (INV-CH22 recurrence = live-threat STOP) |
| I2 | M | PENDING — Monday's close-out sweep (grep evidence, commands cited) |
| I3a | M | fix ✅ landed CI-green; the direct-attached usb-reenumeration leg PENDING — Monday-achievable via the OPERATOR manual variant under the reduced-B1 ruling |
| I3b | S | PENDING — the hub-attached leg, Rosonway-gated |
| J1 | M | ✅ RATIFIED + FROZEN 2026-07-12 (this block) |

## 0. The frame, restated in one paragraph

Mid-August (~Aug 16) is a **readiness checkpoint toward the Nov 25 launch, not the launch** and not Tier-1 close-out (the 2026-06-28 review's frame, unchanged). What HAS changed since that review: gate 1 (engine) was already done; the bench has since run first-light through a full acceptance arc; **the moat is silicon-certified and in its 72 h soak on `04f5f70`**. So the June question — "is each gate credibly on track?" — matures at gate day into a harder, better question: **"is the evidence in hand?"** Every criterion below is written so the answer is yes/no or a number, with the artifact that proves it named in the row. Where a criterion is not yet met, the row says PENDING and names who produces the evidence — as of 2026-07-10 all but two PENDING rows have a ruled backlog row or dispatched lane behind them; the two exceptions (A4's kill −9 rep and H3's clean-image fresh-install rep) are cheap operator-session add-ons with **no scheduled carrier yet** — §5 flags them so ratification assigns carriers rather than gate day discovering the gap.

**Verdict rule (proposed):** all MUSTs green → **GO** (Nov 25 track holds). Any MUST red → **NO-GO or CONDITIONAL-GO** — conditional requires a named remediation, a date ≤ 2 weeks out, and a re-read of just the red rows; a second red read on the same row = NO-GO. SHOULD misses never block, but each is priced into the post-gate runway plan on the record — never silently dropped.

## 1. The criteria checklist

Legend: **[M]** = MUST (gate-blocking) · **[S]** = SHOULD (priced, non-blocking) · Status as of 2026-07-10 (soak day 1). "Producer" = who owns producing the missing evidence.

### A. Certification durability (the soak and its exit)

| # | Criterion (binary/measured) | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| A1 | The 72 h soak completes on the certified build `04f5f70`: zero crashes, zero event loss, zero un-triaged anomalies (any health-glance anomaly interrupts everything — Nick's rail); memory/log growth MEASURED, not eyeballed — RSS recorded at entry and close-out, bound: close-out RSS ≤ 512 MB (the MVP §8.2 idle budget) with a flat trend (final-48 h RSS delta < 10%); bench-log growth linear-with-traffic per the bench log-retention policy (no runaway class) | [M] | Soak logs (`bench-2026-07-10-075035.log`+) + the close-out intake block appended to the bench acceptance record, **including the recorded RSS + log-size deltas against the stated bounds** | IN PROGRESS — entered 07:50:35 Pi-local 2026-07-10; exit ≥ 2026-07-13 ~07:50; a restart resets the clock | Nick (glances) + hub (close-out intake) |
| A2 | NQ-6 exit-act restart spike ×3 **on the soaked build, before any pull/deploy** (Monday-pinned order): `projection_live` position ≥ the recorded aged P0 ("well beyond 14"), the SAME two 5b entity ULIDs API-to-API, `device_relinked` ×2, zero `device_proposed`, the rehydration INFO — all ×3 | [M] | Runbook Phase 7 paste-block results (banked 2026-07-10 — Monday is mechanical), appended to the record | PENDING — scheduled Monday 2026-07-13 | Nick (operator) + hub (intake) |
| A3 | Certification CLOSED on the record — the close-out block written, the M9.4/M9.5 backlog row flipped to certified-CLOSED | [M] | The bench acceptance record close-out block + the backlog row | PENDING — Monday, after A1+A2 | Hub |
| A4 | One deliberate `kill -9` rep on a post-soak bench session: zero event loss across the hard kill, clean rehydration to the same entity ULIDs (the MVP §8.1 write-ahead-durability invariant, exercised as SIGKILL rather than the pkill/restart class already proven) | [S] | A bench-session log block: kill −9 → boot → `projection_live` at the expected position + ULID continuity | PENDING — cheap add-on to any post-soak session; never mid-soak | Nick + hub (recipe rides the runbook) |

### B. Identity durability

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| B1 | Identity holds across process restart, full network loss + restore-from-custody, and fresh re-formation — same device/entity ULIDs, relink-not-repropose, API-to-API continuity | [M] | The acceptance record: DURb block + closing legs L1 (superior variant) + L2; "identity held across THREE networks in one night" | ✅ **DONE 2026-07-09/10** (and re-proven on 72 h-aged state by A2 when it runs) | — (banked) |
| B2 | Wave-2 joins do not disturb standing identities: after adopting the new classes (D1), the original two devices' ULIDs are unchanged API-to-API | [M] | `/api/v1/entities` before/after the Wave-2 bench session; adoption lines showing new IDs only for new devices | PENDING — rides the first Wave-2 bench session (Monday order, after deploy) | Nick (bench) + hub (intake) |

### C. The honest-verdict envelope (the moat, measured)

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| C1 | **Zero false CONFIRMs across ≥ N = 200 cumulative recorded verdicts** (certified §51 scorecards + scenario-suite runs + organic soak/bench verdicts). Any single false CONFIRM at any N = automatic gate STOP + root-cause — the one-way door outranks the count | [M] | §51-class scorecards in the record (event-store positions cited) + B2-ported suite assertion logs + the nightly digest once B3 lands | ~25 verdicts, zero false (certification night). N accumulates via B1→B3 + Wave-2 sessions | Bench sessions (Nick) + B1–B3 automation (Coder/hub) |
| C1b | Stretch envelope: N ≥ 500 by gate day | [S] | Same artifacts | as C1 | same |
| C2 | Timeout honesty stays organic-proven in three classes (device-absent · rejoin race · commanded-to-current-value) with the classes ported into the scenario suite and green on the deployed build | [M] | The acceptance-run block (three organic classes, cited) + B2 suite results | ✅ proven 2026-07-10 on `04f5f70`; suite port PENDING (B2) | Coder (B2 port) + bench |
| C3 | Supersession verdict-free + immediate honest-UNCONFIRMED (identify-class, with the measured reason string) reproduce in the suite | [M] | Record: supersession probe (pos 589/593, 1 ms) + identify 81 ms verdict (pos 644); B2 suite green | ✅ proven; suite port PENDING (B2) | Coder (B2) |
| C4 | Automation trigger-to-action p50/p99 measured on the bench-hero path from event timestamps (target: p99 < 50 ms engine-side per MVP §8.1; device RTT excluded and reported separately) | [S] | A B2 scenario assertion on event-store timestamps, or a close-out measurement block | PENDING — brightness CONFIRMED 0.33 s / identify verdict 81 ms exist as round-trip references; the engine-side split is unmeasured | Coder (B2 assertion) + hub |

**Why N = 200 (the proposal Nick was asked for):** at N = 200 with zero false CONFIRMs, a true false-CONFIRM rate of 1% would have been seen with ~87% probability (1 − 0.99²⁰⁰); at N = 500, ~99.3%. Reachability assumption, stated: the certification night yielded ~25 verdicts across ~15 automation runs (**~1.7 verdicts/run observed**) — N = 200 therefore needs on the order of ~120 automation runs ≈ 8 certification-night-scale suite executions, comfortable once B1/B2 make a suite execution scriptable even if B3 lands late; N = 500 needs ~19 further suite-nights, i.e., B3 running nightly from roughly the last week of July. Hence 200 MUST / 500 SHOULD. The count is cumulative-recorded (positions citable), never sampled.

### D. Fleet breadth (Wave-2 — "how many classes is a credible v1?")

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| D1 | **≥ 5 Zigbee device CLASSES adopted, reporting-configured, and confirmability-characterized** on the bench: light (Hue LCA017) · motion/IAS (SNZB-03P) · temp/humidity (SNZB-02P) · contact (SNZB-04P) · powered plug actuator (S31 Lite zb) — each with its dossier-grade confirmation characterization (lane (a)'s corpus standard) | [M] | Per-class `device_adopted` + `reporting_configured` + verdict lines in bench logs; the four Wave-2 dossiers (lane (a), Monday-blocking) | 2 of 5 classes today (light, motion). Wave-2 units unboxed; joins scheduled in Monday's pinned order | Lane (a) dossiers + Nick (bench joins) + hub (intake) |
| D2 | 6th class: button (SNZB-01P) adopted + characterized; S31 energy telemetry ingested if the unit exposes it (the battlefield-5 credibility start) | [S] | Same artifact classes | PENDING — same sessions | same |

**Why 5 classes is the credible-v1 floor (add/cut with argument, as briefed):** five classes cover the MVP §2.3 Tier-1 spread that Zigbee can carry alone — lighting (actuate+confirm), security-sensor primitives (motion, contact = the IAS/report-only side), environment (temp/humidity = sleepy reporting posture), and a mains actuator (plug = the second confirmable actuator class, breaking the single-actuator-class dependence on Hue firmware quirks). It exercises both moat directions (confirmable command + honest-can't-confirm) across sleepy and mains postures. Below 5, "works with devices" rests on two devices and one actuator class — demo-credible, not v1-credible. Above 6 is breadth-for-breadth's-sake: the D5 ruling already fenced M9 to the curated Wave-1/2 hero set, and 50+ devices is a Tier-1 *budget* goal (MVP §8.2), not this gate.

### E. Seed custody (SD-5 — the hard gate)

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| E1 | SEED-CUSTODY landed: generated TCLK seed on NEW formations, custodied encrypted via SecretStore (AMD-68 atomic key+seed write), restore reproduces AS-FORMED, transient join key unchanged (joiner bootstrap), zero module-info edges — CI green, **audit at the full bar regardless of tempo (Nick's rail: SD-5 never trades rigor for speed)** | [M] | The landed WU + CI on the pushed commit + the two-layer audit record; grounding already banked (`context/pre-verifications/WU-SEED-CUSTODY.md`, 12 DPs) | PENDING — instruction authoring was the hub's beat-4 act (2026-07-10); Track A as-ready dispatch | Coder + hub (audit) + Nick (CI glance) |
| E2 | The **no-non-bench-network hard gate honored end-to-end**: no network other than the bench's exists before E1 lands; the first post-E1 formation on silicon demonstrates the generated-seed path (bench leg in Monday's order or the first session after landing) | [M] | The standing SD-5 rail (backlog row + pm-handoff) + the post-E1 formation's log block (seed minted, custodied, never logged) | Rail HELD to date; silicon leg PENDING | Nick (bench leg) + hub |
| E3 | The public "generated-seed" security statement is writable truthfully and bounded: "production networks form with generated, encrypted-at-rest key material; the well-known key is never a production network key" (scoped to NEW formations; the bench network predates it) | [S] | E1+E2 evidence; one paragraph in the close-out | PENDING E1/E2 | Hub |

### F. Availability honesty (the ALIVE fix — never-false-ALIVE's other half)

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| F1 | AVAIL-ALIVE landed: the existing `StandardAvailabilityTracker` wired (construct at initialize · onFrame→recordFrame · timeout evaluation + the mains read-ping arm · per-entity transition publish), honoring the ruled MUST-NOTs (never TX-accept, never NCP keepalives, never join-handler pins, never emit at construction; the M-1 empty-persisted-map trap) | [M] | The landed WU + CI + the audit record (the verbatim watch-outs are in the backlog row) | PENDING — mechanism-without-driver #6 (grounded v27 beat 1); sequenced INSIDE the explainability push | Coder + hub |
| F2 | Availability honesty **demonstrated on silicon**: cut a device's power → honest offline transition within the ruled windows (the AVAIL-ALIVE row's constants: mains read-ping arm ~10 min; battery/sleepy 25 h — no false ALIVE ever); restore → online on evidence; the entity view stops reading UNKNOWN for live, reporting devices | [M] | A bench-session log block + `/api/v1` before/after + (once FE-7 lands) the availability tile | PENDING F1 | Nick (bench) + hub |

### G. The explainability surface (what minimum FE-7 demo counts)

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| G1 | **The minimum FE-7 demo**, live against the bench Pi over the FROZEN v1.1 read-API (never mocks, never improvised shapes): (a) *why did it fire* — the causal chain for a real bench-hero run rendered end-to-end; (b) *why didn't it* — a real non-firing explanation including the no-change class (ruling (b): log-derived, and the explanation NEVER upgrades or replaces a verdict); (c) *did it actually confirm* — the verdict vocabulary rendered: CONFIRMED with latency, honest-UNCONFIRMED with its measured reason, deliberately-superseded verdict-free | [M] | A scripted ≤10-minute demo run at gate day + screenshots; each tile's log token matching the underlying event (the log-token↔tile continuity from the positioning notes) | PENDING — **the explainability WU dispatch is itself the pending act** (Tuesday-tolerant rail); no lane return exists yet; FE-7 builds against the frozen v1.1 contract once dispatched | Frontend lane + hub (audit) + bench (real data) |
| G2 | The availability tile renders F2's honest states (integrates F with G) | [S] | The same demo | PENDING F1/F2 + G1 | Frontend lane |

### H. Operability (the regression floor + install)

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| H1 | CI green on HEAD at gate day — both workflows (`ci.yml` + `install-smoke`), the gates of record | [M] | The Actions runs on the gate-day HEAD | ✅ green on `04f5f70` (certified); continuous obligation | CI + Nick's glance |
| H2 | B1 scenario runner landed and **the ported suite (B2: the §51 legs + timeout/supersession/identify classes) green on the deployed build**; the FULL suite runs pre-milestone as ruled — gate day reads the latest full-suite green | [M] | `bench.sh scenario/suite` output + the nightly digest (B3) if landed | B0 ✅ (charter + SCENARIO_FORMAT, 2026-07-10); B1 = first post-soak bench WU; B2/B3 sequenced behind it | Coder (B1/B2/B3) + bench |
| H3 | Install path reproducible: install-smoke green (standing) **plus one documented fresh install onto a clean Pi image** (install.sh or deb) reaching a healthy boot (health-probe green) with the runbook's steps as written | [M] | The install-smoke run + a fresh-install log block (runbook appendix) | Harness ✅ (gate #4 green per W28 entry); the clean-image rep PENDING — can ride any post-soak session; Monday's deploy is an update-path rep, not a fresh-install rep | Nick + hub (runbook) |
| H4 | Restart honesty re-rep ×1 on the DEPLOYED post-weekend build (NQ-6-class glance points) — proves the weekend WUs didn't regress the DUR proof | [S] | One restart's glance-point block | PENDING — rides Monday's deploy silicon legs | Nick + hub |

### I. Security posture (the custody fence + statements)

| # | Criterion | Tag | Evidence artifact | Status 2026-07-10 | Producer |
|---|---|---|---|---|---|
| I1 | The custody fence stands as demonstrated: never-adopt/never-clobber under a real foreign-network incident (six honest PIE boots, ch22), recovery from own custody, core stayed up with the integration isolated. **Watch-rows honest at gate day:** INV-CH22 recurrence during the soak = live-threat STOP (interrupts everything, including this gate's timeline); zero recurrence = single-occurrence-artifact stands as the honest position ("we do not know the writer") | [M] | The acceptance record (incident + recovery blocks) + the standing INV-CH22 / WATCH-0xFFFF rows read at gate day | ✅ evidence banked 2026-07-10; watch-rows OPEN by design | Hub (watch) + Nick (rules a STOP if tripped) |
| I2 | Key-material hygiene re-swept at close-out: network key/seed never logged (INV-SE-03 class), custody files present and encrypted, the soak logs sweep clean | [M] | The close-out sweep block (grep evidence, commands cited) | Custody persistence ✅ (certified); the close-out sweep PENDING (Monday) | Hub + Nick |
| I3 | M9.6-RO (reopen identity-capture fix) landed + verified through B1's USB-interruption scenario **in both topologies** (direct-attached + hub-attached, Nick's rail) — the honest availability defect closed | [S] — see §3 Q2 | The landed WU + the B1 scenario run ×2 topologies | PENDING — root re-attributed + field-confirmed 2026-07-10; fix is field-hardening #1, sequenced post-soak; detection/backoff honesty already proven | Coder + bench |

### J. Non-criteria discipline

| # | Criterion | Tag | Evidence artifact | Status | Producer |
|---|---|---|---|---|---|
| J1 | The gate is read against THIS ratified checklist and its §2 non-criteria — no criterion added at the table, no Wave-3 item smuggled in as a blocker | [M] | The ratified version of this file, frozen pre-gate | PENDING ratification (Nick) | Nick (ratifies) + hub (freezes) |

**Tally: 20 MUST rows · 8 SHOULD rows.**

## 2. Explicit NON-criteria (gate-shaped things this gate does NOT ask)

Named so nobody re-litigates them at the table (each with the reason it's fenced):

1. **50+ devices / the 60-device home** — MVP §8.2 budget goal and the Tier-2 proof scenario respectively; the gate rides the curated Wave-1+2 hero fleet (D1). Scale validation is Tier-1-completion work on the Nov runway.
2. **Z-Wave, Matter/Thread, energy-monitor integration, local-WiFi breadth** — integration sequencing is lane (b)'s decision-brief and Nick's ruling; nothing multi-protocol gates mid-Aug. (The Shelly plugs in hand are bench *stimulus* hardware for B3, not a product integration claim.)
3. **The energy dashboard / six months of history** — battlefield 5, Tier 2 by charter.
4. **The full §8.1 latency-invariant measurement campaign under load** (event-publish p99 < 10 ms, replay > 10k/s at scale) — the invariants stay binding as architecture targets; the gate takes soak stability + the C4 hero-path measurement as its evidence tier. A formal load campaign belongs to Tier-1 close, on hardware, after breadth.
5. **Full crash-isolation demonstration across integrations** — structurally undemonstrable with one integration; the achievable half (integration PIEs honestly, core stays up — proven ×6 in the ch22 incident) is already banked under I1. The two-adapter demo is Tier 2.
6. **hsctl / HS-RADIO as product surfaces** — the product-surface crossing is a named STOP (ruled 2026-07-10); bench-tooling tier only.
7. **B4/B5 (labeled-tuple corpus, advisory-only learning)** — post-gate by their own charter; AIOT-INV-1 fences autonomy regardless.
8. **CMD-LANES / scene-group fanout + the §3.10 FIFO AMD** — ruled Wave-2-trigger (single-lane is defensible at the gate fleet size); CMD-DEADLINE and FRAME-CTR are sequenced field-hardening, after M9.6-RO.
9. **Website launch / public content / the LICENSE flip** — Nov-runway concerns with their own briefs and gates (naming blocks them, not this gate; LICENSE consumes lane (b)).
10. **The skills-constellation buildout** — design doc chartered; buildout explicitly post-go/no-go.
11. **The reopen defect as a trust question** — it never was one (zero false state through the deaf window; detection honest). It gates as availability hardening only, per I3/Q2.

## 3. Open questions for Nick (each collapses to one line at ratification)

- **Q1 — N for the verdict envelope.** REC: MUST N ≥ 200, SHOULD N ≥ 500, zero-false-CONFIRM at any N is the overriding STOP. (Rationale in §1-C.)
- **Q2 — M9.6-RO: MUST or SHOULD?** REC: **SHOULD** as written (availability-not-trust; detection already honest; an app restart recovers) — but if the mid-Aug story includes "unattended field posture," promote to MUST and it still fits the window (fix is scoped, B1 is its harness).
- **Q3 — fleet floor at 5 or 6 classes.** REC: MUST 5 + SHOULD the button (D2) — the button adds a class of *stimulus*, not a new confirmability posture.
- **Q4 — pin the gate date.** REC: **Sunday Aug 16** as the read, with Friday Aug 14 as the evidence-freeze (nothing new lands between freeze and read; the read is reading, not landing).

## 4. Gate-day protocol sketch (one page)

**When:** evidence freeze Fri 2026-08-14 EOD → the read Sun 2026-08-16 (Q4). **Who:** Nick (rules), the hub session (evidence steward — opens artifacts, never argues for a row it can't point to). **Time-box:** 60–90 min. **Standing rule:** labels are claims, artifacts are evidence — every row is read against its named artifact, never against memory or a summary.

**Read order:**

1. **Threshold check (5 min):** the soak/certification A-rows and the watch-rows (I1). A tripped INV-CH22-class live threat = the gate adjourns to a STOP-and-rule; don't read 22 rows into a live incident.
2. **The MUST ladder (40–60 min), in dependency order:** A1→A2→A3 (certification) · B1/B2 (identity) · E1/E2 (SD-5) · C1/C2/C3 (the envelope — open the scorecards, cite positions) · D1 (fleet, against the lane-(a) dossiers) · F1/F2 (availability) · H1/H2/H3 (CI, suite green, fresh install) · I1/I2 (posture) · G1 **last and live** — the FE-7 demo runs against the bench Pi in the room, ≤10 min, the three questions answered on real data.
3. **The SHOULD sweep (10 min):** A4 · C1b/C4 · D2 · E3 · G2 · H4 · I3 — each green/red noted; reds priced into the runway plan explicitly.
4. **The verdict (5 min):** apply §0's rule. The ruling + per-row tally is appended to this file (which was frozen at Aug 14), a snapshot beat records it, and the bench record gets a one-line pointer. CONDITIONAL-GO names its rows, remediations, dates, and the single re-read date.

**What GO means (so the word is bounded):** the four June gates read as evidence-in-hand for a curated-fleet v1, and the Nov 25 runway proceeds on the ruled post-gate stack (breadth, hardening, website/launch surfaces). **What it does not mean:** Tier-1 acceptance (50 devices), any multi-protocol claim, or any public-surface readiness beyond what G1/H3 demonstrated.

## 5. Honest gaps in this draft

- Statuses freeze at 2026-07-10 (soak day 1). The weekend Track-A WUs (seed-custody, M9.6-RO, AVAIL-ALIVE, explainability dispatch, B1) were ruled-but-unlanded at authoring; the hub should re-status every row at ratification rather than trusting this table.
- C4's engine-side latency split assumes event timestamps discriminate dispatch-vs-RTT cleanly; if they don't, C4 needs an instrument-first arm before it can be measured (the bench discipline: never theorize twice about the same silence).
- Two criteria have no scheduled carrier as of 2026-07-10: H3's "clean Pi image" fresh-install rep (~an hour of operator time and an SD card) and A4's kill −9 rep (~minutes inside any post-soak session) — flagged so each gets a named slot at ratification rather than a gate-day surprise.
- This lane read the spine and the record; it did not read code. Any row that contradicts the source at ratification loses to the source (truth hierarchy).

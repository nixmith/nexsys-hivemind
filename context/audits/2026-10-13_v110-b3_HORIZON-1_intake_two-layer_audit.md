<!--
file: context/audits/2026-10-13_v110-b3_HORIZON-1_intake_two-layer_audit.md
purpose: Pass 2 of HORIZON-1 — the hub's intake of the return (`research/2026-10-12_HORIZON-1_…`, 127,779 B, md5 f29982af…) and of the v109 hub's pass-1 analysis (`audits/2026-10-12_v109-post-close_HORIZON-1_…`, 12,571 B), both read with equal suspicion; the hub's own re-reads at the bytes; every finding ACCEPTED / CORRECTED / DEFERRED into eleven register rows; the session map fitted to Nick's hours against THE HORIZON's rows; the first charters. Pass 3 (strategy v2, by Dec 1) is ROADMAP-1's.
audience: Nick · v111 and every hub after it (the map and the rulings are cited by id) · the lanes this file charters
state-type: intake audit (two layers; the ruling of record for HORIZON-1)
status: FILED v110 beat 3 (Tue 2026-10-13 ~16:5x CT; instrument 2026-10-13T21:53:36Z)
-->
# HORIZON-1 intake — pass 2 (the ruling)

## §0 Verdict
**ACCEPT the return as the critical review of record, with four corrections and one re-weighting; ACCEPT the v109 analysis as pass 1, with two corrections.** Both are better than the plan they reviewed. The body honoured its cap (44.8 KB with Appendix A; §0–§8 = 31.6 KB); Appendix B (83 KB) was not chartered and was read by id only (A7 holds). Of the 31 findings, 7 additions and 5 decisions: **24 ACCEPTED, 5 CORRECTED (F2, F3, F6, F13's reading, F16), 9 DEFERRED to a named date**, none REJECTED. They fold into **eleven register rows (IR-192..202)**, one per lane or rule — not thirty-one — and a session map of **11 sessions that REPLACE rows of THE HORIZON** (§4). The window's first charters: **GATE-2** (bench, desk; its first step is IR-191's breakdown, options to Nick by Thursday) and **SCHEMA-1** (research → docs; by Nov 2 — D-v110-3's date, not the return's Oct 20); LICENSE-1 follows SCHEMA-1 on the one-research-lane rule, by Nov 2.

## §1 Layer 1 — the two documents against each other
- **Where v109 corrected the return and the hub agrees:** F1 (the invariant and the pragma disagree; the autocheckpoint claim unsupported — the exposed tail is what the kernel has not written back) · SCHEMA-1 at Nov 2, not Oct 20 (the frozen build writes PI-2's bytes regardless) · the coordinator probe as the most urgent item (PI-2's card; `KIT-STORAGE: a` now adds a new stick of the same SKU — its default ship is v14, so the reflash is EXPECTED, not a contingency) · A1 capacity · A3 the moat is ACK-1 + R2.
- **Where the hub disagrees with BOTH (evidence in §2):** F2's growth figure is low by 3–9× against tonight's measured rig · F6's "no transport" rests on an in-JVM datagram the record already tried on JDK 21; a child-process transport exists on a stock JDK · F16's regulatory urgency is EU/UK law applied to a US pre-pilot company · the return's F3 misses the attribute-value upcaster SPI and the degraded-event fallback that exist.
- **Where the hub disagrees with v109:** its §2.5 self-indictment (F13) is right in number and wrong in remedy for THIS fortnight — the spine's cost is the freeze's price; the measure is kept (D-v110-8), the redesign is PROCESS-2's (post-run), nothing changes in the window · its A3 "ACK-1 first among post-run coder units" is right in rank and wrong in date: ACK-1 changes `command_result`'s vocabulary and cannot land on the pilot build between the freeze lift (Nov 2) and the first installs (Nov 19) — its DESIGN brief is December's (J9 as written), the code January's (§4).

## §2 Layer 2 — the hub's own re-reads (device shell; core `176adad`, bench `6a40a10`, hivemind `99c65df`)
1. **F2 — CORRECTED at the instrument.** Tonight's F1 on the rig store: 1,876,566 rows in 940,638,208 B = **501 B/row**; 184,743 rows in 46.4 h = **95.6 k rows/day = 47.9 MB/day ≈ 17.5 GB/yr for TEN devices** (`state_reported` 1,202,395 = 64 % — the metering plugs' reports; `state_changed` 631,933 = 34 %). The return's "2–6 GB/yr for a 20-device home" (dev-box 488 B/event) is 3–9× low because it priced the event, not the fleet's reporting posture. The rate is a policy knob (the reporting posture, R-H's constant) before it is a retention problem — SCHEMA-1's rule must price both. Consequence for the run: ≈ 1.8 GB at Oct 30 on the SD; for a home: the SSD at kit (`KIT-STORAGE: a`).
2. **F6 — CORRECTED.** `distribution/systemd/homesynapse.service` at `176adad` `:8–:14`, `:117–:135`: the sd_notify transport is HELD (OR-M13-SDNOTIFY) because "OpenJDK 21 throws" — Java's Unix-domain channels are stream-only (`SOCK_STREAM`), and `NOTIFY_SOCKET` is a datagram socket. That rules out the in-JVM write, not the transport: **`NotifyAccess=all` + `systemd-notify --ready` / `WATCHDOG=1` from a child process is a documented transport on a stock JDK** (systemd checks the sender's cgroup, not its PID). Cost: one fork per 30-s pet. Not proven on the target JDK — the DANGER block stands until a post-run unit proves it (IR-197); but §C's "FFM for `sd_notify`" is not the only road, and not the cheapest.
3. **F13 — RECOUNTED:** 702 commits, 614 touch `pm-handoff.md` = **87 %**; 529 files under `context/audits/`; v110 so far 1 of 1. The number stands; the remedy is PROCESS-2's (post-run), the measure reported at every close (D-v110-8).
4. **F3 — SHARPENED.** `core/device-model/…/AttributeValueUpcaster.java:39` is an upcaster SPI (AMD-47; AMD-47-INV-02 "upcaster before derivation") for attribute VALUES; `DegradedEvent.java:20–59` is the fallback for an unreadable payload (its `schemaVersion ≥ 1` kept). What is missing is a PAYLOAD upcaster keyed on `schema_version` and a golden-bytes corpus per type/version — SCHEMA-1 reads both before it writes the rule.
5. **F16 — RE-WEIGHTED.** CRA Art. 14 (reporting from Sep 11, 2026), RED (Aug 1, 2025) and PSTI (Apr 29, 2024) bind products placed on the EU / UK markets; the pilot is two US households and the beachhead is unruled. POSTURE-1 (Dec 31) is the right artifact; the urgency is DEFERRED to the beachhead ruling (Dec 1–14) — an EU/UK beachhead makes it a 2027-Q1 gate.
6. **Not re-read (disclosed):** §5's prices and URLs (the dates match the hub's own knowledge); F18's loop lines (the lane re-read the javadoc); F27's `:835–849`; the bench-side F26 / F31 (GATE-2 settles them); Appendix B's prior-art lists.

## §3 The rulings (every finding, addition and decision → its row or date)
| Id | Ruling | Where it lives |
|---|---|---|
| F1 (durability vs power cut) | ACCEPT, re-weighted as v109: a correctness item, not a safety failure; the claims caveat NOW, the fix post-run | **IR-192** (TAIL-1); the claim register's caveat (b5) |
| F2 (retention / growth) | CORRECTED (§2.1): 17.5 GB/yr at the rig's posture | **IR-193** (SCHEMA-1) |
| F3 (schema evolution) | SHARPENED (§2.4) | IR-193 (SCHEMA-1) |
| F4 (explain 404 after a crash) · F5 (no regression guard; IR-29/30) | ACCEPT; post-run, one unit + one contract test | **IR-196** (HYGIENE-1) |
| F6 (watchdog transport) | CORRECTED (§2.2) | **IR-197** (APPLIANCE-1; the child-process proof first) |
| F7 · F27 (fixed windows; sequential probes; the false-dark class) | ACCEPT; the φ-accrual / suspicion-level design is R2 | **IR-198** (AVAIL-2 = R2) |
| F8 (counters; WARN at INFO) | ACCEPT; R4 / FAILCHAN's existing risk rows | no new row (OR-FAILCHAN · the closure counter) |
| F9 · F17 · F24 (good, load-bearing) | ACCEPT — PROTECT; F9's three places named in a test | IR-196 (one test) |
| F10 (51 sleeps; no fault injection) | ACCEPT → SIM-1 (Q1 named) | §4 |
| F11 (no 2027) · F14 (the paying buyers) | ACCEPT → ROADMAP-1 (pass 3) | §4; D1 |
| F12 (license on disk; instruments unsigned) | ACCEPT; N1 is Nick's this week | **IR-200** (LICENSE-1) |
| F13 (process) | ACCEPT the number; the remedy PROCESS-2 | D-v110-8; §4 |
| F15 (the Hue; seeded-dark never re-asked) | ACCEPT; rows exist | OR-HUE-REPORTING-DEAD · IR-162/163 |
| F16 (regulatory) | RE-WEIGHTED (§2.5) → POSTURE-1 | **IR-201** |
| F18 (`/runs` scans from 0 per poll) | ACCEPT; measure the poll's cost on the Pi during the run (DIAG-1's data), then a latest-run projection | **IR-199** |
| F19 · F29 (no restore; stick swap re-pairs) | ACCEPT; the kit card records EUI64; the weekly copy interim | **IR-194** (RESTORE-1) |
| F20 (update paths; non-atomic `mv`; unsigned) · F23 (SBOM) | ACCEPT; the rows exist (R9 UPGRADE-1, B4 PKG-ATTEST-1); SBOM → HYGIENE-1 | IR-196; THE HORIZON R9/B4 |
| F21 (the token at WARN → journald) | ACCEPT; one line + the ruling, before DIAG-1 ships any journal | IR-196 |
| F22 (no OpenAPI/TLS; unserved routes) | ACCEPT; the public-or-internal ruling by Dec 14, before P6 publishes | IR-196; D-v110-25 |
| F25 · F26 (APS ack; idempotent confirm) | ACCEPT — the moat; ACK-1's design brief Dec, code Jan (§1) | **IR-195** (ACK-1) |
| F28 + A5 (v13 pin; the kit firmware policy) | ACCEPT; PI-2's card carries the probe and the reflash | **IR-202** |
| F30 (mesh telemetry/OTA/groups) | DEFER → MESH-1 (Q1 named) | §4 |
| F31 (a PASS proves honesty) | ACCEPT → GATE-2 | the GATE-2 charter |
| A1 (capacity) | ACCEPT → §4 | — |
| A2 (the clock after a power cut) | ACCEPT → SCHEMA-1's question + TAIL-1's pull | IR-193; IR-192 |
| A3 (the moat) · A4 (GATE-2's evidence first) · A5 · A6 (the pilot's data) · A7 (the lane's deviations; the stale-bytes rule) | ACCEPT | IR-195; the GATE-2 charter; IR-202; OUTREACH-2's note (b5); **the stale-bytes rule → pm-lessons** |
| D1 (December's product) | ACCEPT (b): three beachhead briefs + one professional call before Nov 25 → ROADMAP-1 | §4 |
| D2 (the license line) | ACCEPT (b) as the H10's recommendation — Nick rules at LICENSE-1's return; both instruments signed before any flip | IR-200 |
| D3 (the event contract) | RULED by Nick: SCHEMA-1 by Nov 2 (D-v110-3) | IR-193 |
| D4 (Matter/Thread) | ACCEPT (b): MATTER-1, one question, Q1 | §4 |
| D5 (the process after December) | ACCEPT (c) as the recommendation → PROCESS-2 | §4 |

## §4 The session map, fitted (Nick's hours ≈ 30 h/week Oct 15 → Dec; 40–60 from December; sessions REPLACE rows)
The return priced 12 sessions at ≈ 140 h of LANE time. What Nick spends is the dispatch, the intake read and the ruling (≈ 1–2 h per session), the rig sittings (≤ 2 h each) and his own research hours (MODEL-1). Fitted that way, the map displaces four of THE HORIZON's rows and adds no evening the calendar does not already hold.
| # | Session · lane | Nick's h | Lane h | When | Replaces / rides |
|---|---|---|---|---|---|
| 1 | **GATE-2** · bench (desk; the copy + the corpus) | 2 (the Thu read; N3 by Oct 22) | 6 | Oct 13 → Oct 22 | B3's grader re-cut (the pre-registration gains the fitness bars) |
| 2 | **SCHEMA-1** · research → docs | 1.5 (the ruling) | 8 | Oct 13 → Nov 2 | the research slot (one lane at a time) |
| 3 | **LICENSE-1** · research → Nick + counsel | 3 (counsel; the signing) | 6 | after SCHEMA-1 → Nov 2 | C4's gate (the receipt + the two instruments) |
| 4 | **TAIL-1** · bench (the 20-pull trial) + one measured unit | 2 (one R6 evening) | 12 | Nov 3–9 the trial; the fix lands before B4 only if measured cheap, else January | one of R6's matrix evenings |
| 5 | **HYGIENE-1** · coder (the token line; the `mv`; the unserved routes; F9's test; SBOM in CI) | 1.5 | 12 | Nov 10–18 | J8's "fixes only" window (its five PRs ARE fixes) |
| 6 | **RESTORE-1** · coder + bench (VACUUM INTO on a timer; EUI64 + counters; a stick-swap drill) | 2 (the drill) | 24 | design brief Dec; code + drill Jan | J9 (one of its five briefs) + one Jan R-row |
| 7 | **ACK-1** · coder (`messageSentHandler`; read-back; `command_result` v1.2) | 1.5 | 16 | design brief Dec; code Jan (the first coder unit after the cohort) | J9 (one of its five briefs) |
| 8 | **ROADMAP-1** · hub + Nick (pass 3: strategy v2) | 10 | 10 | Nov 10 → Dec 1 | C8's inputs (the beachhead ruling gains written candidates + the procedure) |
| 9 | **PROCESS-2** · research → hub (ADRs; a tracker; the retirement rule; the skills as proposals) | 3 | 8 | Nov 3 → Dec 14 | the hub's own post-run slot |
| 10 | **POSTURE-1** · research → docs | 1 | 8 | Dec | new (Dec 31); urgency per the beachhead |
| 11 | **AVAIL-2** (= R2, φ-accrual + the suspicion level) · research → coder | 1.5 | 10 | Dec research; Jan code | the IR-137/138 line after the run |
| — | **MODEL-1** (TLA+; Nick's) · **SIM-1** · **MATTER-1** · **PROVENANCE-1** · **LEDGER-1** · **MESH-1** · **PROBE-1** · **APPLIANCE-1** | Nick's own / Q1 | — | Q1 2027, named in ROADMAP-1 | — |
Nick's total above Oct 15 → Dec 14: ≈ 29 h over nine weeks ≈ 3.2 h/week — inside the 30 h/week THE HORIZON already spends on its rows. **RUNTIME-1** (Nick's §C) is measurement, not a session: PI-2's first SSD boot (boot-to-ready, RSS, the replay rate — `KIT-STORAGE: a`'s addition) and BC10's cold start + Sunday's rehearsal (boot cost vs store size) feed it at no cost; its ADR is pass 3's.

## §5 The first charters and the order
1. **GATE-2 — DISPATCH-READY** (`instructions/2026-10-13_bench-lane_GATE-2_…`): step 1 IR-191's breakdown on the desk copy and the landed classifier over the S31 corpus — by cause (bench · device · unattributed; idempotent sends named), by device and command class, over time; in plain words what the hero can say today; step 2 the candidate bars (confirmed ratio · restarts = 0 · probe-answered ratio · store-growth ceiling) as pre-registrations, dry-run on the corpus; the options to Nick by Thursday; N3 by Oct 22.
2. **SCHEMA-1 — DISPATCH-READY** (`instructions/2026-10-13_research-lane_SCHEMA-1_…`): the event contract — the envelope's version and the payload upcaster rule (beside AMD-47's value upcaster and `DegradedEvent`), retention by correlation chain priced against §2.1's rate and the reporting posture, the snapshot rule (boot cost as a function of store size — Nick's §3), the clock-quality question (A2), `logical_time`/`node_id`'s reservation (R8) → one page + a golden-bytes test design; no Java inside the freeze; by Nov 2.
3. **LICENSE-1** — cut when SCHEMA-1 returns (one research lane at a time); by Nov 2; its H10 is D2's (b) as the recommendation.

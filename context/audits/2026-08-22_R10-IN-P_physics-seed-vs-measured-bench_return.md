<!--
file: context/audits/2026-08-22_R10-IN-P_physics-seed-vs-measured-bench_return.md
purpose: R10-IN-P return — the MEASURED-FEASIBILITY column RS-2 left empty. Adjudicates the physics-aware direction (the 2026-08-04 seed → the L-E return → RS-2 §3's three options) against what the bench has ACTUALLY MEASURED and FILED: the fleet's channels, the corpus's cadence, per-option feasibility with attended-hours arithmetic against A-14's floor, the conflicts the charter must rule, and PROPOSED (never-run) instrument blocks. Executed per context/instructions/2026-08-22_research-lane_R10-IN-P_physics-seed-vs-measured-bench_brief.md.
audience: the R-10 charter session (reads this beside RS-2 §3 and the 2026-08-04 seed); the hub (intake, two-layer audit); Nick.
state-type: research return / measured-feasibility read (point-in-time; write-isolated — this file is the lane's only write, uncommitted; the hub stages it).
status: RETURNED 2026-08-22 (filing day, America/Chicago), ahead of the Fri 2026-08-28 EOD stamp.
laws-held: READ-ONLY on all five repos (zero edits, zero commits, zero staging — census at §6.4) · NO HARDWARE: the Pi was never reached and no reach was attempted; every measured figure below is quoted from a FILED return/bundle/record by path:line, never from the Pi and never from memory · banked verdicts are FINAL and nowhere re-derived (law 16) — RS-2's §3 options, L-E's §5.3 ledger, the S-10 ranking, THE READ's 21-MUST walk are cited, never re-adjudicated · ZERO DESIGN AUTHORITY: options and costs only; every §5 block is PROPOSED and marked "after R-5" · the D5 language law on every restatement (the deterministic floor is MISSING from the field, not SUPERIOR; L2/L3 without L1 are unsound; L1 without L2 is insufficient) · archives and bundles read by sample, never whole · every gap stated as "absent from the filed corpus," never "does not exist" (§6.3).
repo HEADs at read (read-only, unchanged): nexsys-hivemind `c974b52` · nexsys-bench `4539f13` · homesynapse-core `89a912e` · homesynapse-core-docs `a53f474` · nexsys-skills `5105abc`.
-->

# R10-IN-P — the physics-aware seed vs the measured bench (filed 2026-08-22)

## §0 The verdict, in one paragraph

**Option A is feasible on the fleet as filed, and RS-2 priced it with a hardware line it does not need — but the arm that makes it a *model* pilot is not feasible without a purchase, and the arm that makes it *cheap* is blocked behind R-5.** The correction that carries the decision: RS-2 §3.1 scopes A as "extend [P1-A] with ONE numeric environmental channel on the bench (a temperature/humidity sensor class)" and prices "new bench hardware (small)" — but the temperature/humidity sensor class **has been on the fleet since 2026-07-18**. `nexsys-bench/scenarios/constants.yaml:65` carries `01KXW0157SP56CCSGJCNDCSQNG   # SNZB-02P temp/humidity/battery` in the remembered-ULID set; it relinks 6/6 at every boot of record and read `✓ Available · Current` at gate morning (`context/audits/2026-08-16_G1_rehearsal_complete-record_and_gate-day-brief.md:233`). So RS-2 §3.3-Q1's existence half is **YES, answered from the fleet manifest**. The measured answer is a third one RS-2 did not have available: the channel exists **on silicon and is silent in the record** — no filed `reporting_configured` count, no filed temperature or humidity value, no corpus dossier, no capture fixture, no scenario, in either repo (§6.3 rows 1–7). The gap is instrumentation-of-the-record, not hardware. That makes A's first arm cheaper than RS-2 priced it (one loopback read, weekday-parallel, ~0 weekend hours) and A's *thermal-study* arm dearer (it needs an outdoor series the corpus does not carry — floor cost ≈ $16.90 for a second SNZB-02P at the acquisition brief's own 2026-06 price, `context/planning/2026-06-21_device-acquisition-and-test-strategy_brief.md:46`, plus a join evening, plus a siting problem: the unit's rated range is −10~60 °C, which a Chicago January is outside). **Cost, against A-14's 15 h/wk weekend-anchored floor: A as RS-2 scopes it ≈ 2.5+ weekend blocks ≈ 37+ h, i.e. ~2.5 weeks of the entire floor, and it cannot start before ~Sep 19–20 because every arm that touches the nightly is behind the R-5 fence. A narrower pilot RS-2 did not name — the ALIVE-anchor inter-report envelope (§4 lead, §3.1-A′) — costs ≈ 1.5 weekend blocks, needs no purchase, no outdoor series, and no new adoption word at all, because it lands entirely inside the already-adopted P1-A class (ii).** Option B costs zero hours and, on one measured fact RS-2 could not see, costs **no data either**: the event store is never pruned by hand (`nexsys-bench/docs/bench-log-retention-policy.md:11`), so if the 02P reports at its declared posture the log has been accruing ≈48 numeric samples/day for ≈34 days regardless of the charter's word. Decline costs the claims window and the characterization — not the corpus.

---

## §1 The fleet + the channels, as filed

**The fleet of record: 6 devices / 6 entities** (`nexsys-bench/scenarios/constants.yaml:52-68`, re-mint of record 2026-07-21 read AT the instrument; `watermark: 25065` at :75). Re-proven API-to-API at every boot-health since — the six-ULID set is byte-identical at `2026-07-26_deploy-evening_return.md:79`, `2026-08-16_G11_pre-fire_recovery_instrument-record.md:50`, and the G1 rehearsal's device list (`:233`).

| # | Device (class) | Entity ULID / EUI-64 | Channels as filed | Numeric? | Environmental? | `reporting_configured` of record |
|---|---|---|---|---|---|---|
| 1 | Philips Hue LCA017 (light, mains router) | `01KX1PA4HSJ581GASYB7DHE40F` / `0x00178801101A09BB` | `on` (bool) · `brightness` + `brightness_percent` · `color_temperature` (mireds 153–447 ≈ 2237–6536 K) · `effect` (color_loop, write-only) | YES (actuated) | **no** | **3/3 verified** (go/no-go `:36`) |
| 2 | SONOFF SNZB-03P (motion/occupancy, sleepy) | `01KX1PB9AAB4VB3E10BD477TV3` / `0xF044D3FFFE9C78D7` | `occupancy.occupied` (bool, cluster `0x0406` — IAS enrolled but **zero** IAS frames; single active path) · `battery.battery_pct` | battery only | **no** | **2/3** honest-degraded sleepy (go/no-go `:36`) |
| 3 | **SONOFF SNZB-02P (temp/humidity, sleepy)** | `01KXW0157SP56CCSGJCNDCSQNG` / `0xF044D3FFFED2A201` | **`temperature_measurement` (`0x0402`) · `humidity_measurement` (`0x0405`) · `battery`** — EP1, profile `0x0104`, device type `0x0302`; in-clusters `0x0000,0x0001,0x0003,0x0020,0x0402,0x0405,0xFC11,0xFC57` | **YES** | **YES — the fleet's only one** | **ABSENT from the filed corpus** (§6.3 row 2) |
| 4 | SONOFF SNZB-01P (button, sleepy) | `01KXW13WF0D6TYGN13WXHTG87K` / `0xF044D3FFFE1C1E8E` | `battery` only — adopted **battery-only** per the R2(B) ruling; presses log-visible, absent from the device model (no `button` entity type in Doc 02 §3.10) | battery only | **no** | not filed |
| 5 | SONOFF S31 Lite zb (plug, mains) | `01KXW1W1SBJZERC9MBAMV2DWKE` / `0x00124B002FA8D1C5` | `on_off` → attribute `on` (bool); read path `data.attributes.on.value` | **no** | **no** | **clusters=1 verified=0 degraded=1** + `confirmation_downgraded … posture=VERIFIED_REPORTS/SLEEPY outcome=best_effort` (constants `:204-207`) |
| 6 | SONOFF SNZB-04P (contact, sleepy) | `01KY12MQW954E4XYNKH0Y5H8VX` / `0x449FDAFFFE688F57` | IAS `contact` (bool, `ZoneStatusChangeNotification`) · `battery` · custom `tamper` (`0xFC11`, tolerate-unknown) | battery only | **no** | **clusters=2 verified=1 degraded=1** (`context/handoff/2026-07-21_04p-adoption_bench-session-report_for-hub-adjudication.md:64`) |

**The numeric/boolean split, decided:** exactly **one** device carries a continuous environmental channel, and it carries two of them (temperature, humidity). Every other numeric on the fleet is either an actuated setpoint (Hue brightness/CT) or a diagnostic (battery %). **Illuminance: no silicon** — the canonical attribute `illuminance_lux` exists in the schema (`context/coding-instructions/archive/M4.0b-3_Typed_Change_Detection_Comparator.md:76`) but no fleet device reports it; the 03P's in-cluster set is occupancy + power only (`nexsys-bench/corpus/devices/sonoff-snzb-03p-motion.md:24-27`). **Energy: none, resolved AT the instrument** — "the S31 Lite zb exposes NO metering surface … the capture shows no ElectricalMeasurement/Metering clusters" (go/no-go `:37`, D2 row; dossier `:52`), and the two Shelly plugs ordered 2026-07-10 remain unprovisioned (`constants.yaml:152-154`, `plug: available: false`). L-E `:81`'s P3 finding is confirmed at HEAD-of-record: energy corroboration is **hardware-first**, not compute-first.

**The declared reporting posture for the one environmental channel** (Doc 08 §3.7 defaults the `ReportingConfigurator` attempts unless a profile overrides — dossier `:32`, `:130`): temperature `min 10 s / max 3600 s / change 10 (= 0.1 °C)`; humidity `10/3600/100 (= 1 %)`; battery `3600/62000/0`. Our temperature reportable-change is **10× more sensitive than z2m's shipped default** (0.1 °C vs 1.0 °C) — the wave's one real delta, flagged then, still unresolved: **C-14 is OPEN** — "02P | firmware honors 0.1 °C reportable-change? | Phase 1 (stimulus) | OPEN" (`context/assessments/2026-07-15_wave2-setup-and-joins_operator-return.md:263`). SONOFF's own page states no change *threshold* at all (≥1 report/60 min; 5 s minimum on change — dossier `:131`).

**The honesty line on availability.** The 02P is designated the fleet's **availability-ALIVE anchor** (`2026-07-15_wave2-setup-and-joins_operator-return.md:44`), and F2 CLOSED GREEN at THE READ (`2026-08-16_THE-READ…:51`). But the positive half was proven on the **03P**, not the 02P: "a battery sleepy's report flipped UNAVAILABLE→AVAILABLE in ~22 s (the 03P wave 14:28:15Z → read 14:28:37Z; **in-class for the row's 02P wording** — the 02P itself self-healed organically the same morning)" (go/no-go `:42`). And availability evidence is **any frame**, not a value report: `lastEvidenceAt` sources are "every `onFrame` … + every answered ping" (`2026-07-31_WU-AVAIL-SEED_return.md:35`). **So "the 02P is AVAILABLE" proves frames arrive; it does not prove a numeric temperature reaches the log.** That distinction is the whole of §3's Q1 residue and the whole of §5 block P-1.

---

## §2 The corpus, as filed

### §2.1 Event cadence — measured two ways, from read-model `viewPosition` deltas

`viewPosition` is the read-model position; the constants law pins the registry `projection_live` replay-head and states the read-model "runs ahead and is NEVER pinned here" (`constants.yaml:70-75`). Treating a `viewPosition` **delta** as the log's append count over the same interval is this lane's **[INFERRED]** step, so labeled; both ends of each window are quoted verbatim from filed records.

| Window | Start (path:line) | End (path:line) | Δ positions | Elapsed | Rate |
|---|---|---|---|---|---|
| **W1 — well-stamped both ends** | `91229` @ `2026-08-16T05:44:17.103484856Z` (`2026-08-16_G1_rehearsal…:188`) | `104220` @ `2026-08-20T23:59:59.684724880Z` (`2026-08-20_midweek-FE-deploy_sitting-record.md:49`) | 12,991 | 4 d 18 h 15 m 42.6 s = **4.7609 d** | 12,991 ÷ 4.7609 = **2,729 events/day** |
| **W2 — date-stamped, one coarse end** | `55378` @ `2026-07-31 11:45Z` (go/no-go `:42`) | `91127` @ 2026-08-13 (`2026-08-09_H3-clean-image…:216`; the same return's timeline puts health-green 07:35:41 EDT = 11:35Z and cold-boot 07:47:12 EDT = 11:47Z, `:48-49`, with the bench restore following) | 35,749 | ≈**13.0 d** | 35,749 ÷ 13.0 = **2,750/day** (sensitivity: a 20:00Z read on 08-13 gives 13.34 d → 2,680/day) |
| **W3 — the negative control (radio absent)** | `91127` @ 2026-08-13 | `91229` @ 2026-08-16 05:44:17Z | **102** | 2.749 d | **37/day** |

**Reading: ≈2.7 k events/day across the six-device fleet with the nightly running; ≈37/day with the radio out.** W3 is the control that makes W1/W2 a *fleet* figure rather than an app figure — the coordinator fd was lost between the 08-13 restore and the G-11 recovery at 02:08 CT on 08-16 (`2026-08-16_G11_pre-fire_recovery_instrument-record.md:17-22` — ⏺1a, `(no ttyUSB fd)` on pid 9767; the fd returns at `:55-60`), and the G1 record notes independently that "the event log did not advance at all" across a 40-minute gate-morning window (`:278`). **Per-device sanity check, not a derivation:** the S31's own measured day cadence is `+9 stateVersion in 45 minutes ≈ one device-originated report per ~5 minutes` ⇒ ~288/day for one device (`2026-08-04_B3_night3_R8-R9-addendum_and_night4-baseline.md:20`) — consistent in order with 2.7 k/day across six devices plus command/run/verdict traffic. **No per-device or per-attribute census of the log exists in the filed corpus** (§6.3 rows 3–4).

### §2.2 The verdict corpus (the `confirmed | unconfirmed` moat figures, as ratified)

**≈1,728 cumulative recorded verdicts, ZERO false CONFIRM**, from the acceptance record's verdict-envelope block: **19 `state_confirmed` · 1,024 `command_confirmation_timed_out` · 685 `command_result`**, store **13,790 events at exit**, 2026-07-13/14 — 8.6× the N≥200 MUST and 3.5× the N≥500 SHOULD (go/no-go `:31`; doctrine `:15`). Zero false CONFIRM held through THE READ ("C1 ✓ EXCEEDED (≈1,728 verdicts, zero false CONFIRM; door intact through the Aug-16 digest)", `2026-08-16_THE-READ…:201`), including the first **unattended** exhibit (`2026-08-02_B3_night2…:36`).

### §2.3 The s31 settle measurements and the boot-window physics (the seed's own live finding, as filed)

| Quantity | Measured value | Source |
|---|---|---|
| Confirmation window (S31 on/off) | **5.369 s** source-declared (`ExpectedOutcome`, the instrument of record per playbook §8 F-8 `:102`); **5.136 s** and **5.19 s** measured at expiry | constants `:236-238`; `2026-08-02_B3_night2…:15`; R8/R9 addendum `:14` |
| ON-edge confirm, idle clock | **107.5 ms** (S-1 rep 1, ACCEPTED→DISPATCHED 3.7 ms) · **111 ms** (S-1) · 3.8–5.0 s (Rep A, polling-granular) | `2026-07-28_B2_suite-port_return.md:202`; constants `:236-238` |
| Settle confirm at +40–55 s post-resume | **143 ms** (Aug-2) and **3.59 s** (Aug-3, 10 s after a deliberate dongle power-cycle) | R8/R9 addendum `:14` |
| Boot-adjacent cold mesh | asserted `turn_on` entered a mesh up **0.772 s** (`network_resumed` 04:30:51.004 → ACCEPTED 04:30:51.776) ⇒ TIMED_OUT, three park-verified nights | R8/R9 addendum `:14`; constants `:174-179` |
| Report-to-edge sufficiency bracket | 16 s insufficient / 60 s sufficient; **the interval itself is UNMEASURED and deliberately not relied upon** | constants `:213-215` |
| Other immediate classes | identify 54.2 / 66.1 ms ACKNOWLEDGED-"unconfirmed"; supersession 22.3 ms ACKNOWLEDGED-"superseded" | B2 `:204-207` |

### §2.4 What the nightly actually accrues — the number nobody has stated

The nightly writes **ONE line per night**: `<date> <evidence-class> AUTO floor: N/M · bench-hero <restore> · ON-latency <value>` (`nexsys-bench/tools/runner/nightly_digest.py:133-139`), where ON-latency is the DISPATCHED→CONFIRMED distance extracted from that night's `command-confirm-s31` bundle — one device, one quantity, `n/a(<verdict>)` on a SKIP/FAIL night, **never fabricated** (`:5-6`, `:135-136`, `:161-164`). The filed series (`2026-08-15_bench-evening_pre-READ_operator-return.md:139-157`, a verbatim `tail -n 30` of `~/hs-bench/digests/nightly.log`, plus 2026-08-16 at `context/handoff/2026-08-16_THE-READ_navigator-packet.md:24`):

| Nights filed | Numeric ON-latency values | Values | `n/a(FAIL)` | Accrual rate |
|---|---|---|---|---|
| **16** (2026-08-01 → 2026-08-16) | **6** | 3.65 s · 0.30 s · 0.17 s · 0.36 s · 0.16 s · 0.30 s | 10 | **0.375 values/night ≈ 2.6/week** |

**This is the entire continuously-accumulating numeric series the platform produces today.** No percentile is computed from it here: the corpus's own hazard discipline governs — the n=3 C4 distribution is "cited as existence of the instrument, never as statistics" (L-E `:45`). Any research arm whose plan reads "rides the nightly corpus" must quote 6-in-16, not the nightly's existence.

**Bundle shape and retention:** each failing/asserting leg writes a bundle of `scenario.yaml · resolved.json · app-log-slice.log (or an explicit ABSENT line) · api-captures.json · verdict.txt · MANIFEST.txt`; `journal-slice.txt` was **DROPPED at B3.1 A-6** with the drop recorded in the MANIFEST so its absence is never mistaken for evidence (`nexsys-bench/tools/runner/bundles.py:118-199`, `:158-165`). Retention: bundles "adopt this policy wholesale (bundles copy off nightly with the digest; Pi keeps a 7-day window)"; **the event store is explicitly NOT covered — "it is the product's log and is never pruned by hand"** (`nexsys-bench/docs/bench-log-retention-policy.md:33`, `:11`).

### §2.5 Fixtures, corpus, and the history-seeded class (counts, sizes, span)

| Artifact class | Count | Bytes | Date span | Environmental content |
|---|---|---|---|---|
| `nexsys-bench/fixtures/` real captures | **2** | 8,194 + 10,468 | both **2026-07-01** | none — Hue confirmation-windows, 03P motion walk-test |
| `nexsys-bench/fixtures/runner-demo/` synthetic | 19 | 602–5,623 | 2026-07 | none (liveness/boot/reseat mutants) |
| `nexsys-bench/corpus/devices/` dossiers | **2** | 17,075 + 10,893 | 2026-07-01 | none — Hue + 03P only |
| `nexsys-bench/corpus/raw/` ZHA diagnostics | 4 | 17,669–22,857 | 2026-07-01 | none |
| `nexsys-bench/scenarios/*.yaml` | **12** (11 + constants) | 2,953–21,811 | 2026-07-12 → 2026-08-05 | **none reference the 02P** |
| `nexsys-bench/bench-logs/` | 8 | 9,015–108,160 | **2026-07-10 → 2026-07-13** — i.e. **entirely pre-Wave-2-joins (2026-07-18/19)** | none |

**The history-seeded class (arc-11) is doctrine, not yet a scenario file.** The compounding-testing doctrine names it as "the missing tier — scenarios seeded with adversarial-but-lawful history … B2+ scenario authoring treats 'what does the log already carry?' as a first-class scenario parameter" (`context/process/2026-07-18_compounding-testing-doctrine.md:32`). No scenario in the 12 declares a seeded-history precondition. The doctrine's `§5` measured-envelope ledger (`:41`) is the closest thing to a filed envelope corpus and it is a hand-maintained list of dated exhibits, not a regenerating series. **B4 — "the labeled-tuple corpus … per-device latency envelopes regenerate continuously; drift becomes data" — is a RULED but UNBUILT bench phase** (`nexsys-bench/docs/2026-07-10_bench-automation-charter.md:21`), fenced "post-gate by their own charter" (go/no-go `:159`). **B4 is P1-A's structural home and it does not exist.**

### §2.6 L-E's P1-A envelope-corpus inputs, present vs absent

| P1-A input (L-E `:51`) | Present today? | Evidence |
|---|---|---|
| A nightly that runs unattended | **PRESENT** | 16 filed digest nights; `auto-suite` = 9 ruled legs (`constants.yaml:257-266`) |
| Per-attribute report timestamps in a machine-readable artifact | **ABSENT** | the digest carries one latency; bundles carry `api-captures.json` only for the asserting leg (`bundles.py:168-172`) |
| A per-device envelope store | **ABSENT** | "no per-device measured envelope is stored or consumed anywhere in core today" (L-E `:46`) — re-confirmed: no IR home either (§4.3) |
| A numeric environmental channel on the fleet | **PRESENT (silicon) / ABSENT (record)** | `constants.yaml:65` vs §6.3 rows 1–7 |
| A read path to the log for a census | **ABSENT on the frozen API** | `GET /api/v1/events` → router 404, `application/json`, 159 B (`sitting-record:51`; G1 `:257-261`) |
| Variance-band + rig-scope publishing method | **PRESENT (adjudicated)** | C-3 reshape; doctrine `:36-43` |
| Outdoor/weather context (for the thermal arm only) | **ABSENT entirely** | no weather ingest, series, or integration in either repo (§6.3 row 9) |

---

## §3 Per-option measured feasibility (RS-2 §3 A/B/C)

**The weekend ledger every cost below is priced against** (A-14 floor 15 h/wk weekend-anchored, `context/research/2026-08-02_A14_attended-hours_charter-input.md:20`; the shape — bench-adjacent hours concentrate on weekends, weekday hours are laptop/automated — is A-14 `:22`'s own **INFERENCE, flagged there for one-word confirm at the charter**, adopted as S-10's `sizing-basis:` (`context/assessments/2026-08-14_S10_close_ranked-program.md:6`), and **no confirming word is in the filed corpus**, §6.3 row 12). One weekend block ≈ 15 h at the floor; S-10 `:36` sizes Tier 1 as two weekend blocks.

| Weekend | Dates | Claimed by | Bench hands? | Source |
|---|---|---|---|---|
| W1 | Aug 22–23 | R-1/R-2 card sitting (Blocks 1–3, daylight) · R-9 · R-7b · W-HIVE-1 | YES | `PROJECT_SNAPSHOT.md:17`; v56 prompt `:55-56` |
| W2 | Aug 29–30 | R-3/PKG-E2E-1 → R-4 (~45-min re-rep) → **THE FENCE LIFT** | YES | v56 `:59`; S-10 `:17-18` |
| W3 | ~Sep 5–6 | **R-10, the charter weekend** (one weekend deliberation, hub + Nick) | no (deliberation) | S-10 `:30`; v56 `:45` |
| W4+ | ~Sep 12– | Tier 2 residue: **R-5** the settle-instrument redesign (R-6/R-7/R-8 landed early, 2026-08-22) | YES | S-10 `:22`; snapshot `:17` |

⇒ **The earliest weekend on which a new nightly leg is lawful is the one AFTER R-5 lands — ~Sep 19–20, five weekends past the charter.** The queue in front of it is R-4 → R-4.5 (L-F Shape A, proposed at I-1) → R-5 (re-sequenced after Shape A at I-2) → the new leg (`2026-08-15_LE-LF_late-returns_two-layer-audit_v52-beat-5.md:58-59`).

### §3.1 (A) ADOPT-NOW-SCOPED — decomposed into four arms, because they do not cost the same

| Arm | (a) EXISTS (cite) | (b) ABSENT — and what would provide it | (c) First honest measurable milestone (incl. the honest null) | (d) Attended hours vs the A-14 floor | (e) Layer + D5 sentence |
|---|---|---|---|---|---|
| **A0 — the channel census** (RS-2 §3.3-Q1's residue) | the device (`constants.yaml:65`), the entity (G1 `:233`), the read verb `bench.sh state <ulid>` → `GET /api/v1/entities/<ulid>/state` (`nexsys-bench/tools/bench.sh:77`), the `{value}`-nested `/state` dialect (B2 `:210`; constants `:110-114`) | nothing to build | **One `/state` read.** Milestone: the 02P's attribute key set + `lastReported` freshness on the wire. **Honest null: the drawer returns battery only and no temperature key** ⇒ the channel is adopted-but-unmapped and A's substrate genuinely is missing ⇒ RS-2's own tripwire fires, fall back to B (RS-2 `:205`) | **~0.5 h, WEEKDAY-parallel, 0 weekend hours.** Precedent on the record: the **Thursday** 2026-08-20 midweek FE-deploy sitting ran browser + loopback reads over the tunnel with no bench hands (`sitting-record:9`) | **L1-enrichment.** *The bench measures what this device's evidence channel actually does; the platform's verdicts already refuse to claim more than that channel supports. That deterministic floor is what the field does not build — not a better model, and not a substitute for one.* |
| **A1 — the cadence scenario** (the ALIVE-anchor leg) | the scenario is **already authored in prose**: `snzb02p-report-cadence-alive-anchor` (AUTO, long-horizon) with its positives and its `Forbidden: device_proposed` (`2026-07-11_wave2-device-dossiers_research-return.md:150`); the runner needs **no new mechanic** — `log:`/`api:`/`within:`/`requires:` are all v0 (`SCENARIO_FORMAT.md:78-87`) | the YAML file itself; two `constants.yaml` keys (an `auto-suite` entry at `:257-266`, a capability gate if wanted) | **One night's decisive verdict** on the leg. Milestone: ≥1 temperature-or-humidity `state_reported` within `3700 s`, availability never UNAVAILABLE across the run. **Honest null: the leg goes red on a healthy device** ⇒ the declared 3,600 s max-interval is not honored ⇒ that is itself a filed P1 finding, and a better one than a green | **≤0.5 weekend block (~7 h), GATED on R-5** — an `auto-suite` entry is a nightly touch and the fence is standing ("the s31 legs/nightly HANDS OFF until R-5", `PROJECT_SNAPSHOT.md:21`; v56 `:33`). Earliest start ~Sep 19–20 | **L1-enrichment.** Same sentence as A0. |
| **A2 — P1-A proper: the envelope extraction** | the digest formatter already extracts one timing from `api-captures.json` (`nightly_digest.py:167-221`); C-3 variance/rig-scope method adjudicated; B4 is a **ruled** phase (`bench-automation-charter.md:21`) | a per-attribute inter-report extraction + its storage; B4 is **unbuilt**; **and a read path** — see §4.4 | **The first envelope with a stated variance band and rig-scope declared.** Honest null: the distribution is degenerate (every interval = the max-interval) ⇒ the device is a metronome, the envelope is one number, and the "measured envelope" thesis gains a boring but honest first datum | **≈1 weekend block (~15 h) + N nights of accrual.** Accrual arithmetic: today's instrument yields **0.375 numeric values/night** (§2.4); at the 02P's declared floor (max-interval 3,600 s) the channel itself offers **48 samples/day = 1,440/month**, but nothing captures them yet | **L1-enrichment.** *Measured envelopes turn a copied field constant into this device's own number — the 25 h `BATTERY_OFFLINE_SILENCE` (L-E `:43`) is z2m's default, not a measurement. Closing that loop is the floor the field leaves open.* |
| **A3 — the 2R2C identification study** | replay determinism (counterfactual-grade evaluation, RS-2 `:163`); RC is cheap on Pi-class (RS-2 `:116`) | **an outdoor temperature series — absent entirely**; a second sensor; a siting decision; and A0+A1+A2 first | a PRE-STATED accuracy bar, published either way (RS-2 §3.3-Q2's protocol) | **NOT SIZABLE from the filed corpus.** Floor cost: **≈$16.90** for a second SNZB-02P (`2026-06-21_device-acquisition-and-test-strategy_brief.md:46`, re-price at consumption) + one join evening (the Wave-2 precedent: 3 devices in one attended evening, 2026-07-18/19) + **a siting problem the corpus already names: rated range −10~60 °C** (dossier `:131`) — a Chicago January is outside it, so "outdoor" may mean a garage or a purchased outdoor-rated part | **L2 — and the D5 line must not blur it.** *A thermal model over this home's own record is a reasoner, not a witness: it proposes, is labeled as proposing, and the harness continues to enforce on measured evidence alone. A floor without such reasoners is insufficient; reasoners without the floor are unsound.* |

**Total A as RS-2 §3.1 scopes it (all four arms): ≈2.5+ weekend blocks ≈ 37+ h ≈ 2.5 weeks of the entire 15 h/wk floor, earliest start ~Sep 19–20, plus a purchase.** Against RS-2's own honest note that A competes with SP-4 "and if both cannot fit, SP-4 is senior" (`:204`) — SP-4 needs **zero** new instrumentation and its instrument already runs unattended (L-E `:121-125`, `:137`). On the measured hours, **both do not fit before winter.**

### §3.1-A′ The narrower pilot RS-2 did not name (the §4 lead, stated here as an option)

**A0 + A1 + A2 restricted to INTER-REPORT INTERVALS — the ALIVE-anchor envelope. No values, no thermal model, no outdoor series, no purchase, no L2 surface.** Why it is the honest first cut: (i) it is *entirely inside* the already-adopted P1-A class (ii) (L-E `:51`, `:237`) — it needs a **scheduling** word from the charter, not an **adoption** word; (ii) it is L1-enrichment by RS-2's own mapping ("P1–P3 … are L1-ENRICHMENT — evidence about the evidence channel — which is why the L-E return could recommend P1-A as bench method without touching the model question", RS-2 `:148`), so it carries **none** of the honesty load RS-2 §2.2 prices for inference surfaces; (iii) its first product surface is the one RS-2 §2.2 row 2 **already sanctions** — "expected next report by ~T, from measured cadence" (`:172`); (iv) it feeds SP-4 (the pilot L-E ordered first) and SP-1 directly; (v) it converts the field-standard 25 h silence constant into a per-device measured number, which is exactly the loop L-E `:48` says "nobody — external or internal — yet closes." **Cost: ≈1.5 weekend blocks + accrual, A0 weekday-parallel, A1/A2 behind R-5.** **Honest null available at every step**, and the null is publishable method evidence, not a loss.

### §3.2 (B) DECLINE-WITH-TRIPWIRES

(a) EXISTS: everything B needs — nothing. (b) ABSENT: nothing. (c) First measurable milestone: the tripwires themselves, each dated and checkable (RS-2 `:212`, T1–T6). (d) **Hours: zero.** (e) **L1. D5 sentence:** *The deterministic evidence floor keeps compounding without a model layer; the floor is what is missing from the field, and nothing in a decline weakens it.*

**One measured fact the charter should have before it declines, which RS-2 could not see:** the event store "is NOT covered by this policy — it is the product's log and is never pruned by hand" (`bench-log-retention-policy.md:11`). The 02P was adopted **2026-07-18 20:32:11 CT** (G1 `:233`) — **≈34 days** to filing day. **If** the channel reports at its declared posture, the log has been accruing ≈48 numeric samples/day across those days ⇒ **≈1,630 samples, less ≈130 for the radio-absent window (§2.1 W3) ⇒ ≈1,500 — none of it lost, none of it decaying, none of it read.** Conditional on A0 settling the "if," **decline costs the claims window and the characterization; it does not cost the corpus.** That materially strengthens B relative to RS-2's own framing of it, and it is the strongest single argument for running **A0 alone** (≈0.5 weekday hours) even under a B ruling: the cheapest possible act settles the highest-value unknown, and the asset accrues either way.

### §3.3 (C) RE-COMMISSION-DEEPER — the five questions, re-priced against the measured bench

| RS-2 Q | Status after this lane | Measured cost to finish |
|---|---|---|
| **Q1** "What numeric environmental channels exist in the event log at HEAD, at what density, from which device classes?" | **Half-answered here** (channel + device class + declared density, §1) — the *realized* density half remains, and RS-2's "a grep plus a log census" is **not available**: `GET /api/v1/events` 404s (§4.4) | **A0 (≈0.5 h weekday) + §5 block P-2's 2-hour bracket + P-3's human-tier census.** Not "hours" of research — minutes of hands |
| **Q2** the 2R2C fit against a pre-stated bar | unchanged; gated on A3's purchase + outdoor series | ≥1 weekend block after A0–A2 |
| **Q3** the consent/privacy calculus for occupancy inference | unchanged; desk-note scale; **no occupancy-inference surface is proposed by anything in this return** | desk |
| **Q4** enterprise/insurer WTP | unchanged, out of scope for any repo lane | interviews |
| **Q5** FP/FN operating points for plausibility surfaces | unchanged; and **P3 is hardware-blocked regardless** (no energy telemetry, §1) | literature |

**Measured verdict on C:** commissioning a deeper lane to answer Q1 is now **disproportionate** — Q1's remaining half is a two-hour bracket with ≤5 minutes of hands (§5). C's real content is Q2/Q4/Q5, and Q2 is downstream of a purchase.

---

## §4 The conflicts the charter must rule

**§4.1 A2 mutates the instrument SP-4 writes about.** RS-2 `:204` names the hours competition; the measured conflict is sharper than hours. SP-4 is a **methodology paper about the nightly** — "the bench IS the apparatus … the method, not the numbers, is the paper" (L-E `:122`). A1 adds a leg to `auto-suite`; A2 changes the digest's extraction. **A methods paper whose apparatus changes mid-series must either date-fence its series or re-baseline.** Three orderings exist and the charter picks one: (i) A1/A2 land **before** SP-4's series opens; (ii) SP-4's series is **date-fenced** at the A2 landing and says so in the paper; (iii) A2 defers past SP-4's writing window. This lane names the fork; it does not choose.

**§4.2 R-5 blocks A1/A2 by date AND overlaps them by content.** The fence is standing and explicit (`PROJECT_SNAPSHOT.md:21`; v56 `:33`). Beyond the date: R-5's own scope absorbs "the bar-vs-distribution window-sizing NOTE" and "the transition-aware question's instrument half" (S-10 `:22`) — the **same** instrument surface a per-attribute cadence extraction would touch. Landing two edits to one instrument in the wrong order costs a re-baseline. Queue of record after I-1/I-2: R-4 → R-4.5 → R-5 → A1.

**§4.3 The corpus-model IR has no home for a measured envelope on a read-only channel — the exact fields, named.** In `nexsys-bench/docs/2026-06-28_phase-2_corpus-model_IR-schema-and-onboarding-pipeline.md` (schema-version 2):

| Field | Line | Why it does or does not carry a measured numeric envelope |
|---|---|---|
| `confirmation[]` | `:28`, `:34-44` | **Per ACTUATING capability.** The 02P has none — `confirmation: []` by construction (dossier `:136`). The one block designed to hold measured evidence-contract facts is structurally unreachable for the fleet's only environmental channel. |
| `reportingOverrides` | `:29` | Exists, but is a **DECLARATION** field — the values the `ReportingConfigurator` attempts (dossier `:32`). Nothing in it is measured. |
| `entities[].capabilities[].deltas` | `:27` | Overrides on a `generic/cap/*` template; not provenance-bearing, not rig-scoped. |
| `provenance.fieldTags` (`[REF]` / `[CONFIRM-ON-BENCH]`) | `:30` | **The natural hook** — a measured envelope is precisely the thing that RETIRES a `[CONFIRM-ON-BENCH]` tag. |

⇒ **The minimal schema move, named as a cost line and not as a design:** a per-capability `reportingEnvelope` block (measured, rig-scoped, provenance-bearing, `n` disclosed) beside `reportingOverrides`, plus the `fieldTags` transition. **Second-order and load-bearing:** schema v2 *emits* into the shipped `homesynapse-core/integration/integration-zigbee/src/main/resources/zigbee-profiles.json` (dossier `:9`, `:19`). A new IR block that emits **nothing** is free and bench-local; one that **emits** is a core-resource change plus a governance amendment in the AMD-CAND-1/AMD-CAND-4 pattern (`:36`, `:63`). **Whether the envelope emits is the schema decision the charter would be authorizing** — and it is not stated anywhere in RS-2 §3.1's cost line.

**§4.4 The read surface has no events endpoint — a charter-visible cost RS-2 could not price.** `GET /api/v1/events?sort=DESC&limit=50` → **404, `application/json` (not `problem+json`), 159 B** — the router-level not-found; "the events endpoint charters (post-V1)" (`sitting-record:51`; G1 `:257-261`; FE preflight Check 5 in `2026-08-21_FE-lane_never-triggered-fixture_F-S3_return.md:30`). The bench charter's assertion surface is **API-FIRST**, with the ruled rider quoted verbatim: *"if a §51-class assertion needs an event the frozen v1.1 surface doesn't expose, that is a contract conversation brought to me — never a raw-SQLite fallback inside a scenario"* (`bench-automation-charter.md:41`). A per-attribute cadence census over the log is exactly that class. **Three lawful paths, and the charter picks:** (a) a contract conversation about an events endpoint; (b) a scenario that measures cadence from `/state` reads and log tokens rather than from the log — the R-9 method (`R8-R9-addendum:20`), which needs no contract change; (c) a **human-tier** SQLite census outside the scenario tier, for which `bench.sh events` (`tools/bench.sh:76`) is the existing sanctioned precedent — noting it filters to command/verdict event types and **does not include `state_reported`**. Path (b) is the cheapest and is what §5 block P-2 proposes.

**§4.5 The physics half's first product surface is downstream of the dialect half — and the same session decides both.** F-S2, measured live: the `/state` wire serves **epoch-second numbers**; the NEW-3-hardened client refuses to coerce non-string instants and renders **honest absence** (`sitting-record:34`) — so the device drawer renders every attribute value as `—` (G1 `:243-249`). RS-2 §2.2 row 2's prediction-labeled readout lands on exactly that surface. v56 `:45` puts the **FE-STATE-DIALECT core-half decision in R-10's own hands**, with the FE lane idle until it (`:74`). **Sequencing ruling wanted, cheap:** if the charter adopts any physics arm whose surface is user-visible, the dialect half is its prerequisite, and the two words should be ordered in one breath.

**§4.6 A-14's sizing inference is still unconfirmed and every hour figure above rides it.** A-14 `:22` flags "bench-adjacent hours concentrate on weekends; weekday hours are predominantly laptop/automated" as an **INFERENCE (flag for one-word confirm at the charter)**. S-10 adopted it as `sizing-basis:` (`:6`) on 2026-08-14. **No confirming word appears in the filed corpus.** A0's whole cheapness claim — "weekday-parallel, 0 weekend hours" — is an application of that inference (with one supporting precedent: the Thursday-evening loopback sitting). One word settles it.

---

## §5 The PROPOSED instrument blocks (never run; the hub dispatches, or does not)

**Standing marking on all three: AFTER R-5; s31/nightly untouched.** All three are loopback reads that touch no scenario, no constant, no `auto-suite` entry, and never address the S31 — **flagged for the charter, never asserted:** the fence's own wording is "the s31 legs/nightly HANDS OFF" (`PROJECT_SNAPSHOT.md:21`), which may or may not reach a read of a different device over the tunnel. If the charter reads the fence narrowly, P-1 is a five-minute weekday act and Q1 closes this month. **This lane holds all three behind R-5 as briefed.** Authored to playbook §8: goal + done-when first, WHERE-label **inside** the block, full paths, verified verbs only, zero placeholders, expected AND failure tokens named, ⏺ paste-either-way, STOP-gates in their own block (`context/process/bench-troubleshooting-playbook.md:97-101`, `:106-116`).

> **Verb-existence check performed at authoring** (playbook §8 (4)): `state <ulid>`, `entities`, `events`, `api_token`, `digest [N]` are all dispatched verbs in the case statement at `nexsys-bench/tools/bench.sh:67-103`. **Vocabulary honesty (playbook §8 (9)):** the attribute KEY NAMES below are the schema's canonical candidates (`temperature_c`, `humidity_pct`, `battery_pct` — `context/assessments/2026-06-26_converter-db-embed-pipeline-design.md:117-118`; `M4.0b-3…:76`) and are **NOT verified on this device's wire** — discovering the real key set is what P-1 is *for*, so P-1 asserts nothing and only records.

### ⏺ P-1 — THE CHANNEL CENSUS (~2 min hands; expected tokens ~40 lines; the one-command answer to RS-2 §3.3-Q1)

**Goal:** learn whether the fleet's one environmental channel puts numeric values on the wire, and what its keys and freshness are.
**Done-when:** one `/state` body for the SNZB-02P is pasted, either way.
**Anti-actions:** do NOT restart the app · do NOT touch the S31 · do NOT run a scenario or the suite · do NOT paste any request-header screenshot (F-S1: header captures are token-carriers).

```
# Pi terminal
/home/homesynapse/nexsys-bench/tools/bench.sh state 01KXW0157SP56CCSGJCNDCSQNG
```

**⏺ RECORD — paste the whole body either way.** What the read decides: (1) an `attributes` map with a temperature-like and a humidity-like key **present with numeric values** ⇒ the channel is live in the state store and A0 is GREEN; (2) `attributes` carrying **battery only** ⇒ the channel is adopted-but-unmapped ⇒ RS-2 `:205`'s tripwire fires; (3) HTTP 404 / empty body ⇒ instrument problem, not a device finding — re-read `bench.sh entities` first and paste that. Also record verbatim: `lastReported`, `lastChanged`, `stateVersion`, and any `stale`/`staleAfter` field. **Expected dialect (measured, so you are not surprised):** the live `/state` wire nests values as `data.attributes.<key>.value` (B2 `:210`; constants `:110-114`) and serves instants as **epoch-second NUMBERS**, not strings (F-S2, `sitting-record:34`) — a bare number where you expected a timestamp is CORRECT here.

### ⏺ P-2 — THE CADENCE BRACKET (the R-9 method applied to the 02P; ≤5 min hands across a 2 h window)

**Goal:** bracket the 02P's realized inter-report interval against its declared 3,600 s max-interval, and settle C-14's direction.
**Done-when:** three `/state` reads at T, T+60 min, T+120 min are pasted with their wall-clock times.
**Why 2 hours and not 15 minutes — stated so it is not shortened:** the doctrine's resolution rule binds — *"the bench out-waits its instrument's resolution; an experiment shorter than the evidence cadence measures nothing, honestly"* (`compounding-testing-doctrine.md:28`). The declared max-interval is 3,600 s, so any bracket under ~1 h is uninformative by construction. The **waits are unattended**; only the three reads are hands.
**Anti-actions:** do NOT breathe on, warm, or handle the sensor between reads (that is a *different* experiment — the dossier's `snzb02p-temp-delta-stimulus`, `:152`) · do NOT restart the app mid-bracket (a restart re-seeds the clock) · do NOT touch the S31.

```
# Pi terminal — run this line THREE times: at T, at T+60 min, at T+120 min
date -u +%H:%M:%SZ; /home/homesynapse/nexsys-bench/tools/bench.sh state 01KXW0157SP56CCSGJCNDCSQNG
```

**⏺ RECORD ×3 — note the clock on each.** Read the deltas exactly as R-9 did (`R8-R9-addendum:20`): `stateVersion` advance and `lastReported` movement across the three reads. **Interpretation stated in advance:** `lastReported` moving ~hourly with a small `stateVersion` delta ⇒ the max-interval floor is the whole cadence ⇒ **C-14 resolves toward "the 0.1 °C change is not driving reports"** ⇒ realized density ≈48 samples/day, 12× below the DYD 5-minute reference (RS-2 `:53`). `lastReported` moving many times per hour ⇒ the change-arm is live ⇒ fitting-grade density exists today. `lastReported` frozen across all three ⇒ a **finding**, not a null: an ALIVE-anchor that is not reporting.

### ⏺ P-3a — STOP-GATE for the log census (its own block, per playbook §8 (1))

**Goal:** establish that `state_reported` is a queryable `event_type` before anyone writes a census query against it.
**Done-when:** one event-type tally is pasted.
**Tier note, binding:** this is the **human debug tier**, never a scenario assertion — the bench charter's rider forbids raw SQLite inside a scenario (`bench-automation-charter.md:41`); `bench.sh events` (`tools/bench.sh:76`) is the existing sanctioned precedent for a human-run read of this exact DB, using only the columns proven there.

```
# Pi terminal
sqlite3 /home/homesynapse/hs-bench/data/homesynapse-events.db \
  "SELECT event_type, COUNT(*) FROM events GROUP BY event_type ORDER BY 2 DESC;"
```

**⏺ RECORD the whole tally.** **STOP HERE.** If no row names `state_reported` (or the local equivalent), P-3b does not run and the hub re-authors against whatever vocabulary the tally shows. Only on a `state_reported` row does the hub dispatch P-3b.

### ⏺ P-3b — THE PER-DAY CENSUS (dispatch ONLY after P-3a's gate answers; ~1 min hands)

```
# Pi terminal
sqlite3 /home/homesynapse/hs-bench/data/homesynapse-events.db \
  "SELECT date(ingest_time) AS d, COUNT(*) FROM events WHERE event_type='state_reported' GROUP BY d ORDER BY d;"
```

**⏺ RECORD the whole table.** This is the §2.1 `viewPosition` inference's falsifier and the §3.2 "≈1,500 samples accrued" claim's direct test. **Expected shape if the model in §2.1 holds:** a per-day count in the high hundreds to low thousands, with a visible trough across 2026-08-13→08-16 (the radio-absent window). A flat or absent trough refutes this lane's W3 control and should be filed as such.

---

## §6 Sources, harvest, and what could not be found

### §6.1 Sources (path:line; all under `nexsys-hivemind/` unless prefixed `nexsys-bench/`)

`nexsys-bench/scenarios/constants.yaml` :52-68, :70-75, :110-114, :129-154, :174-179, :204-215, :236-238, :246-266 · `nexsys-bench/tools/bench.sh` :67-103 (esp. :74, :76, :77, :90) · `nexsys-bench/tools/runner/nightly_digest.py` :5-6, :133-139, :161-164, :167-221 · `nexsys-bench/tools/runner/bundles.py` :118-199, :158-165 · `nexsys-bench/scenarios/SCENARIO_FORMAT.md` :69-87 · `nexsys-bench/docs/2026-07-10_bench-automation-charter.md` :18-22, :26-29, :31-36, :41-45 · `nexsys-bench/docs/bench-log-retention-policy.md` :11, :33 · `nexsys-bench/docs/2026-06-28_phase-2_corpus-model_IR-schema-and-onboarding-pipeline.md` :21-32, :34-44, :46-53 · `nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md` :17, :19, :65 · `nexsys-bench/corpus/devices/sonoff-snzb-03p-motion.md` :24-27, :35, :39, :48-53 · `nexsys-bench/corpus/devices/philips-hue-white-a19.md` :26, :34, :45-78 · `nexsys-bench/README.md` :29-33 · context/audits/2026-08-21_RS2_physics-world-model_charter-evidence_return.md :53, :116, :144, :148, :151-163, :167-177, :202-205, :212, :217-221, :225 · context/research/2026-08-15_LE_physics-aware-deep-research_return.md :43-48, :51-53, :81, :87, :121-125, :137, :237-256 · context/research/2026-08-04_physics-aware-core_strategic-seed_charter-input.md :14, :18-22, :44 · context/research/2026-08-02_A14_attended-hours_charter-input.md :20-23 · context/assessments/2026-08-14_S10_close_ranked-program.md :6, :17-22, :30, :36, :42, :51 · context/strategy/Substrate_Thesis_v0.md :99-110, :152-177, :229-239 · context/assessments/2026-07-11_go-no-go-criteria_draft.md :31, :36, :37, :42, :97, :159 · context/assessments/2026-07-11_wave2-device-dossiers_research-return.md :32, :52, :109-153, :184-190 · context/assessments/2026-07-15_wave2-setup-and-joins_operator-return.md :44, :113-138, :263 · context/assessments/2026-06-26_converter-db-embed-pipeline-design.md :117-118 · context/audits/2026-08-16_THE-READ_gate-record_and_verdict.md :49, :51, :159, :201 · context/audits/2026-08-16_G1_rehearsal_complete-record_and_gate-day-brief.md :188, :233-249, :257-261, :272-278 · context/audits/2026-08-16_G11_pre-fire_recovery_instrument-record.md :17-22 (⏺1a), :34, :50, :55-60 (⏺1c) · context/audits/2026-08-15_bench-evening_pre-READ_operator-return.md :135-158 · context/audits/2026-08-20_midweek-FE-deploy_sitting-record.md :9, :16, :34, :49, :51 · context/audits/2026-08-21_FE-lane_never-triggered-fixture_F-S3_return.md :30 · context/audits/2026-08-20_R1R2_return.md :11, :23 · context/audits/2026-07-28_B2_suite-port_return.md :196-212, :263-265 · context/audits/2026-08-02_B3_night2_command-confirm-s31_evidence-read.md :14-20, :36-39 · context/audits/2026-08-04_B3_night3_R8-R9-addendum_and_night4-baseline.md :14, :20, :24 · context/audits/2026-07-31_WU-AVAIL-SEED_return.md :35, :37 · context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md :48-53, :216-217 · context/audits/2026-08-15_LE-LF_late-returns_two-layer-audit_v52-beat-5.md :50, :58-64 · context/process/2026-07-18_compounding-testing-doctrine.md :15, :19, :25-32, :36-43, :47 · context/process/bench-troubleshooting-playbook.md :64-71, :97-102, :106-116 · context/handoff/2026-07-19_04p-adoption_BENCH-STOP_learn-persist-finding.md :200-213 · context/handoff/2026-07-21_04p-adoption_bench-session-report_for-hub-adjudication.md :64 · context/handoff/2026-08-22_PM-mission-control_v56_orchestrator_session_prompt.md :30-33, :44-45, :53-59, :72-74 · context/handoff/2026-08-16_THE-READ_navigator-packet.md :24 · context/status/PROJECT_SNAPSHOT.md :17, :21 · context/planning/2026-06-21_device-acquisition-and-test-strategy_brief.md :12-14, :41-46 · context/coding-instructions/archive/M4.0b-3_Typed_Change_Detection_Comparator.md :76.

### §6.2 Harvest (5 lines, for the hub's process fold)

1. **The verb-existence rule extends to ENTITY CHANNELS.** Before a brief conditions an option on "does channel X exist," read the fleet's own manifest: `constants.yaml:63-68` answered RS-2 §3.3-Q1's existence half in one line, and the option shipped priced with a hardware purchase it does not need. Candidate: the authoring checklist's (a)/(b)/(c) surface check gains a fourth arm — **the fleet manifest is a surface**.
2. **Adopted ≠ characterized, and D1 conflates them.** "5 OF 5 CLASSES" is true on ADOPTION and silent on MEASUREMENT: the 02P has no dossier, no fixture, no scenario, and no `reporting_configured` count. Candidate: the class census gains a second column (`adopted | characterized`), so a future gate cannot read breadth as depth.
3. **State the instrument's numeric yield whenever a research arm claims to ride it.** The nightly produces **6 values in 16 nights, one device, one quantity** (§2.4). Any plan whose sentence is "rides the nightly corpus" should quote that rate beside the claim.
4. **`viewPosition` is the cheapest event-cadence instrument in the record and is currently harvested by archaeology** across five scattered returns. Candidate: one line per operator return — `viewPosition <n> at <ISO instant>` — makes log growth a first-class series at zero marginal cost.
5. **A charter option whose gating question is "does the log carry X" must name its read path at authoring** — the frozen v1.1 surface has no events endpoint (`/api/v1/events` → 404), and the bench charter forbids the SQLite fallback inside a scenario. The C-class authoring check has a research-lane analogue.

### §6.3 What this lane could not find in the filed corpus (each a candidate instrument, not a claim of absence)

1. Any **temperature or humidity VALUE** from the SNZB-02P, in either repo. *(→ P-1)*
2. Any **`reporting_configured` line for the SNZB-02P** — the counts are filed for Hue (3/3), 03P (2/3), 04P (2/1/1), S31 (1/0/1), and for no one else. *(→ a boot-log grep at the next Pi touch)*
3. Any **per-device or per-attribute census** of the event log. *(→ P-3b)*
4. Any **`state_reported` row count**, ever — `bench.sh events` filters to command/verdict types only. *(→ P-3a/P-3b)*
5. A **corpus dossier for the 02P** — `corpus/devices/` holds Hue + 03P only, both dated 2026-07-01.
6. A **capture fixture for the 02P** — `fixtures/` holds two real captures, both 2026-07-01, neither environmental.
7. Any **scenario referencing the 02P** — 12 scenario files; the ALIVE-anchor leg exists only as prose in the dossier (`:150`).
8. **C-14's answer** — whether the firmware honors the 0.1 °C reportable-change; OPEN since 2026-07-15. *(→ P-2)*
9. Any **outdoor/weather series, ingest, or integration** anywhere in the five repos.
10. Any **energy or power telemetry** — the S31 Lite exposes none at the instrument; the Shelly plugs are unprovisioned.
11. The **digest and on-latency logs themselves** — they live on the Pi (`~/hs-bench/digests/`); only quoted lines are filed, and 16 nights are the filed extent.
12. Any **confirming word on A-14's weekend-concentration inference**, which A-14 `:22` itself flagged for one-word confirm at the charter and which S-10 `:6` adopted as the sizing basis regardless.
13. Any **illuminance channel on the fleet** — the canonical attribute exists in the schema; no device reports it.

### §6.4 Read-only census + coverage honesty

**Writes: exactly ONE file — this one, uncommitted.** Zero edits, zero `git add`, zero commits, zero staging in any of the five repos; HEADs unchanged and quoted in the frontmatter. Other 2026-08-22 lane returns sit untracked in `context/audits/` alongside it — at this lane's final porcelain read: `…BRAND-SPRINT-1…`, `…FE-SWAP-CENSUS…`, `…R10-IN-L_liveness-and-notify-transport…`, `…W-HIVE-1_hivemind-token-economy…` (four, two of which appeared during this lane's session) — per the lane pattern; the hub stages them. **No hardware:** the Pi was never reached, no reach was attempted, and every measured figure is quoted from a filed artifact by path:line. **Read whole:** the R10-IN-P brief · the 2026-08-04 seed · A-14 · the S-10 close · RS-2 (whole) · the compounding-testing doctrine · the bench automation charter · the retention policy · the IR-schema doc · `bench.sh` · `constants.yaml`. **Read by section or by targeted grep** (disclosed, not smoothed): L-E (§0, §1.1, §1.3, §2.4–2.6, §5.3 — §§3–4 by grep only) · the Substrate Thesis (§3.1, §5, §9) · THE READ · the G1 rehearsal · B2 (§12.2, §12.8–12.9) · the wave-2 dossiers (§0.4, §1–§3) · the playbook (§8) · the go/no-go draft (rows B2/C1–C4/D1/D2/F2, §D) · the v56 prompt (§§2–4, §6) · the FE F-S3 return (§0–§1). **Not read:** the pm-handoff spine at v56 · any core Java at HEAD (read-only honored; every AS-BUILT statement rides L-E's cites or a filed operator record) · the runner engine (`engine.py`, 71,958 B — sampled by grep only). **Weakest claims in this return, named:** (1) the `viewPosition`-delta-as-append-count step in §2.1 is an INFERENCE and P-3b is its falsifier; (2) §3.2's "≈1,500 samples accrued" is conditional on the declared reporting posture being honored, which is exactly C-14 and exactly unmeasured; (3) every hour figure in §3 rides A-14's unconfirmed weekend-concentration inference (§4.6).

---

*Return complete. Filed 2026-08-22 at `context/audits/2026-08-22_R10-IN-P_physics-seed-vs-measured-bench_return.md` — the lane's only write, uncommitted; the hub stages it. Research-only held: ZERO design authority — §3 is costs, §4 is forks, §5 is PROPOSED blocks marked "after R-5; s31/nightly untouched" and never run. Nothing here adopts, declines, schedules, or moves code. Route-back: intake at the hub; read at the R-10 charter session beside RS-2 §3 and the 2026-08-04 seed.*

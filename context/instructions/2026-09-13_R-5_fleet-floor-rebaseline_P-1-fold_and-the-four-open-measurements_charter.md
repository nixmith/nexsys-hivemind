<!--
file: context/instructions/2026-09-13_R-5_fleet-floor-rebaseline_P-1-fold_and-the-four-open-measurements_charter.md
purpose: The R-5 charter — the plan of record's "bench floor re-baselined on the fleet; the s31/nightly hands-off ends; the nightly becomes the soak's instrument" — in two parts. PART A (the desk; a bench lane; dispatch-ready): P-1's fold into the scenario format and the runner, the harness exit-code and time-bound rulings, the ULID-provenance audit's result and fix, the fleet line in the nightly digest. PART B (the rig; after H8-a; the packet is CUT at the beat that names the slot, through THE PRIOR-LEDGER GATE): the re-baseline runs, the C-003 counterfactual window, the null-arm block, the re-seen/adopted split, the second O-2 reading. Every claim below carries its instrument.
audience: the bench lane (Part A; a fresh Cowork conversation) · the hub (Part B's packet cutter; the intake) · Nick (§A7 is his paste; `R5: <day> <hh:mm>` names Part B's slot)
state-type: lane charter (Director mode; Part A's Files table governs; Part B is a design for a packet, not a packet)
status: PART A EXECUTED — returned 2026-09-13 (`context/audits/2026-09-13_R-5A_return.md`, 9 = 8 M + 1 A; the gates 28/30/14) + R-5A-ii (6 M; the gates 29/43/18), audited ACCEPT at v73 beats 5–6, landed bench `f3631cb` by Nick's hands — banked v73 beat 7 (Sun 2026-09-13 ~18:1x CT; instrument 2026-09-13T23:18:34Z). PART B CHARTERED — the packet is cut on `R5: <day> <hh:mm>`, after H8-a's slot, through THE PRIOR-LEDGER GATE (v74). Was: PART A DISPATCH-READY (the bench is idle; P-1 landed `1201368`) · PART B CHARTERED.
-->

# R-5 — the fleet floor, the P-1 fold, and the four measurements R-4c left open

## §0 What R-5 is, in one paragraph
The bench floor (`nightly_digest`'s `floor:` line — `9/9 PASS` or the SKIP-honest `8/9 PASS · 1 SKIP(…)`) was last baselined on a three-device registry; R-4c completed the fleet (six of six `in_adopt_list=1` on the held card, C-003 minted with a bound). R-5 re-baselines the floor on that fleet, ends the s31/nightly HANDS-OFF fence, folds P-1's driver into the format the bench already reserves, and runs the four measurements R-4c could not: the counterfactual that would make the ZDO surface's causal role a fact rather than a hypothesis (F-R4c-A), the null arm of LASTREPORTED-1b, the re-seen/adopted split after a power event, and O-2's second reading. Resolution is not adoption (F-R4c-A) is a constraint on every line below; a device ULID is not stable across cards (F-R4-2) is another.

---

# PART A — the desk fold (a bench lane; no device is touched; dry-run is the only mode you run)

## §A0 The lane contract (every line binds)
- `date -u` first; state your instrument limit (the bench card is NOT yours to touch; you write files under `nexsys-bench/` and run `--dry-run` and the selftests on your desk). CT = UTC−5, once.
- **The one deliverable:** `nexsys-hivemind/context/audits/<your CT date>_R-5A_return.md` — §0 card first (≤2.5 KB: the census `N = a M + b A` with exact paths · P1–P4 adjudicated · the three gates with counts · DP-1/DP-2 as taken), then §1 per-file deltas, §2 the gates, §3 pushback and observations, §4 the WUCP Phase-1 checklist. **Cap ≤10 KB, a ceiling** (3 KB + ~1 KB per row). Your last line, in the file and printed to Nick: `RETURNED <path> <bytes>`.
- **Write-set:** the §A3 Files table only. `scenarios/*.yaml` other than `constants.yaml` stay untouched (the suite of record; the hands-off lifts at Part B, on the rig, not on the desk). Never `git add`/`commit`; Nick lands with a card.
- **The fence:** no command at any device; the harness's live leg stays REFUSED until `HARNESS-PLUG:`; every new code path is exercised by a test or by `--dry-run`.
- **Tests first, every row;** the gates verbatim: `python3 -B tools/harness/test_harness.py` (19 checks at `1201368`) · `python3 -B tools/runner/nightly_digest.py --selftest` (21 checks) · the new `python3 -B tools/runner/test_engine.py` (row A1's home — no engine test exists today: `git ls-files tools | grep -i test` = `tools/harness/test_harness.py` only; format law #13 grounds the new file here beside `engine.py`).
- **Predictions (adjudicate first):** P1 — the census is §A3's table exactly or the deviation is declared. P2 — every row's new checks are RED at HEAD by construction (the key, the code, the exit value, the field do not exist) and GREEN after; name any preservation check. P3 — `harness.py`'s `REFUSED` reads `2` after A3 and `test_harness.py` pins it against the engine's table (a string read from `tools/runner/README.md`'s exit-code section, not a literal copied twice). P4 — at least one cite here is wrong at your HEAD; you file the corrected line.

## §A1 The ground (read at bench `1201368`; re-read, cite in your return)
- `scenarios/SCENARIO_FORMAT.md:18` `requires: []  # [] | [plug] | [usb-power] | [operator]`; `:24` the reserved stimulus `# - plug: {target: hue-wall, act: off, settle: 5s}`; §2 rule 1 and §5 close the format (additive-only; further changes STOP-gated) — **this charter is the STOP-gate's word for exactly the `plug:` key** (the P-1 audit's ruling 2, 2026-09-13).
- `docs/2026-09-13_P-1_power-harness_design.md:106`–`:129` §4 "The fold plan (R-5)" — the grammar: `requires: [harness-plug]`; `plug: {target, act: cycle, at: <offset from window-open>, off_for, dut_profile, ready_token}`; the engine calls the harness's guards; the plug's `state_reported` enters the bundle as a first-class positive; no promoted plug ⇒ SKIPPED.
- `tools/harness/harness.py:58` `REFUSED = 3  # DISTINCT from the engine's REFUSED=2`; `:112`–`:114` the state ledger `~/hs-bench/harness/<plug>.json` (`windows: {window: [epoch]}`; a dry-run never writes it); `:135` `record_cycle`; `:144` `window_stamps`; `:159` the device-scoped hazard span; `:456` `--window` required, caller-supplied, never defaulted.
- `tools/runner/engine.py:88` the status vocabulary `PASS | FAIL | SKIPPED | REFUSED | DEFERRED`; `:189` anti-vacuous (an empty `positive:` is REFUSED).
- `tools/runner/nightly_digest.py:103` `floor_text(legs)` — the `floor:` field's forms; `:8` `--selftest`.
- `scenarios/constants.yaml:115` `s31-entity: "01KXW1W1SBJZERC9MBAMV2DWKE"` under `command.`; `:403` the comment naming the same ULID; `:283` `# MINTED 2026-07-31 from the P-1 paste:` (the quiesce arc's P-1).
- **The ULID audit, re-derived by the hub (R-4c ask; the audit §5.4):** `grep -rn '01KXW0156Z\|01M2DKJWVD'` over the bench, `web-ui`, the docs and the live instructions = 0 hits outside records and audits; the one persisted card-minted id in the bench is `constants.yaml:115` (the S31's entity, minted by the BENCH card). It is valid only while the bench card is in the slot — the held card minted a different ULID for the same silicon (F-R4-2, `01KXW0156Z…` vs `01M2DKJWVD…`).

## §A2 Settled decisions (rulings of record; not open)
- **SD-A1 — one spelling for one act:** the reserved `plug:` stimulus gains the harness grammar (design §4); no parallel `harness:` key. `requires: [harness-plug]` is the coverage flag; absent ⇒ the scenario reports SKIPPED in the suite summary, never silently narrowed.
- **SD-A2 — the chokepoint stays one:** the engine drives a `plug:` stimulus THROUGH the harness module's guarded entry (import, not a subprocess), so the safety table (`maxCyclesPerWindow`, `minSecondsBetweenCycles`, the unknown-profile refusal, the device-scoped hazard span) and the `NETWORK_CALLS` chokepoint remain the only network path for a plug act. A `--dry-run` suite run plans the act and prints the refusals; the live leg is REFUSED until `HARNESS-PLUG:`.
- **SD-A3 — exit codes:** the harness adopts the engine's vocabulary (`REFUSED` = 2); `--dry-run` prints the table it uses.
- **SD-A4 — the time bound:** the per-window cycle cap gains `windowSeconds` (the ledger records window-open; a cycle whose `at:` offset falls outside `windowSeconds` is REFUSED); `--window` stays required and caller-supplied.
- **SD-A5 — the year-month disambiguation:** `constants.yaml:283`'s comment reads `MINTED 2026-07-31 from the P-1 (quiesce, 2026-07) paste`; the power-harness P-1 (2026-09) is named where the harness block cites it. No file is renamed.
- **SD-A6 — ULID provenance:** every ULID the bench persists declares the card that minted it beside it (`# minted-by: bench-card <EUI64>`), and the runner refuses a scenario whose ULID's declared card is not the card in the slot (the registry's device list carries the EUI64 → the check is one API read; DP-1 decides the read). No silent use of a foreign card's id.
- **SD-A7 — the fleet line:** `nightly_digest` prints beside `floor:` a `fleet:` field — `fleet: <adopted>/<expected> · re-seen <n>` — read from the card's registry at digest time (the F-R4c-A split: a device the registry already knows that announces is RE-SEEN; a new registry row is ADOPTED; two numbers, never one).

## §A3 Files (the table governs)
| # | Path | A/M | What |
|---|---|---|---|
| 1 | `scenarios/SCENARIO_FORMAT.md` | M | §1: the `plug:` stimulus grammar (design §4, verbatim keys) and `requires: [harness-plug]`; §5: one dated line — "reopened for the `plug:` key by the R-5 charter (2026-09-13); closed again after" |
| 2 | `tools/runner/engine.py` | M | the `plug:` stimulus honoured through the harness's guarded entry (SD-A2); `requires: [harness-plug]` ⇒ SKIPPED when no promoted plug; the plug's `state_reported` a first-class positive |
| 3 | `tools/runner/test_engine.py` | A | the engine's first tests: a `plug:` scenario plans in dry-run (no network — the chokepoint tally 0), refuses live without `HARNESS-PLUG:`, reports SKIPPED without the promoted plug, refuses an empty `positive:` (the preservation check, named) |
| 4 | `tools/harness/harness.py` | M | `REFUSED = 2` (SD-A3); `windowSeconds` (SD-A4); the guarded entry exported for the engine |
| 5 | `tools/harness/test_harness.py` | M | the exit-code pin against the README table; `windowSeconds` refusal; the entry's tally stays 0 in dry-run |
| 6 | `scenarios/constants.yaml` | M | `:283` the year-month (SD-A5); `:115` the provenance comment (SD-A6); `windowSeconds` in the harness block |
| 7 | `tools/runner/nightly_digest.py` | M | the `fleet:` field (SD-A7) + its selftest fixtures |
| 8 | `docs/2026-09-13_P-1_power-harness_design.md` | M | §4 gains one status line: folded by R-5 Part A (the date, the return path) |
| 9 | `tools/runner/README.md` | M | the exit-code table's harness line; the `fleet:` field documented |
**Census claim: 9 = 8 M + 1 A.**

## §A4 Two scope decisions you take and declare
- **DP-1 — the registry read for SD-A6/SD-A7:** the runner already reads the card's API for `api:` assertions (`engine.py`, the frozen v1.1 read surface); use the same client for the device list; if the read surface does not expose the EUI64 beside the deviceId, say so and fall back to the count-and-ids identity check (the fleet's six ids as adopted on the card in the slot), declared.
- **DP-2 — where `windowSeconds` lives:** the harness profile block in `constants.yaml` (default) or a per-window CLI flag; one of the two, declared, with the ledger recording window-open either way.

## §A5 What to watch out for
- The format's STOP-gate (§5) is real: touch only the `plug:` key and its `requires` value; any other format change is a STOP and a line in your §3.
- The hazard span is DEVICE-scoped (`harness.py:159`): `windowSeconds` bounds a window, it does not reset the device budget.
- The 2026-09-12 bench regression (`7/9 · FAIL command-confirm-s31`, self-recovered 09-13; R-4c ask #9): your changes must not touch the S31 confirm path's scenario; the `fleet:` field is additive to the digest line, never a re-grade.
- Register C in every comment and digest string; no product name (`{{NAME}}` where one would appear).

## §A6 Success criterion (binary)
The census is §A3 exactly (or declared); the three gates green with their counts (`test_harness.py` 19 → N, `--selftest` 21 → N, `test_engine.py` new); `grep -n '^REFUSED = ' tools/harness/harness.py` reads `2`; `grep -c 'minted-by:' scenarios/constants.yaml` ≥ 1 and the runner's refusal for a foreign-card ULID has a test; a `--dry-run` suite plan over a `plug:` scenario prints offsets from window-open only and a chokepoint tally of 0; the return on disk with its `RETURNED` line.

## §A7 The dispatch line (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected)
```
date -u first. You are the R-5 Part A bench lane for NexSys/HomeSynapse. Baseline: nexsys-bench at 1201368, porcelain empty. Read nexsys-hivemind/context/instructions/2026-09-13_R-5_fleet-floor-rebaseline_P-1-fold_and-the-four-open-measurements_charter.md PART A whole (§A0–§A7), then nexsys-bench/docs/2026-09-13_P-1_power-harness_design.md §4, scenarios/SCENARIO_FORMAT.md §1–§2 and §5, tools/runner/README.md, tools/harness/harness.py and its test. Write only the §A3 files. No live command anywhere; --dry-run and the selftests are the only things you run. Tests RED at HEAD first, each row. Never git add/commit. Write the return to nexsys-hivemind/context/audits/<today CT>_R-5A_return.md (≤10 KB; §0 card first; P1–P4 adjudicated first; the last line `RETURNED <path> <bytes>`) and say that one line to Nick.
```

---

# PART B — the rig session (after H8-a's slot; EXCLUSIVE at the rig; the packet is cut on `R5: <day> <hh:mm>`)

## §B0 The rules the packet inherits
- **THE PRIOR-LEDGER GATE (pm-lessons 2026-09-13):** before Part B's packet goes LIVE, its cutter greps `context/audits/2026-09-12_R-4c_measurement-only_operator-record.md` §9 (D-1..D-11) and its §14 asks — and R-4b's — for every command string and every named witness the packet reuses, fixes each hit or carries it as a named deviation, and lists the greps in the cutting beat's audit. Known carries: D-3 the anonymous origin gate as the standing §1 (GitHub's published artifact digest, read signed-out, hashed against the zip); D-5 the nested-quote `dpkg-query` (fixed form only); D-10 the read-2 diff prints RAW API values for new rows; D-11 the grade read and `sudo shutdown -h now` are never one paste; D-9 no witness that a prior §0 says does not exist.
- **The artifact:** the newest green `.deb` on `main` at the cut (114b's landing or later), through §1's gate; the held card (the fleet card) IN, the bench card OUT and restored at the end (B5 outranks everything after B3, as R-4c's did).
- **The measurement-shape law:** every block below pre-registers the shape and the direction and carries its inverse arm.
- **The fences that lift and the ones that stay:** the s31/nightly HANDS-OFF ends AT this session's B1 (the re-baseline is the first run under the lifted fence); `network_formed` = POWER OFF + STOP; never `--allow-downgrades`; `TOKLEN-OK`; the hub never commits; the operator says back one line per block.

## §B1 The re-baseline (the deliverable of R-5)
Two consecutive nightly-suite runs on the fleet card under the lifted fence; the `floor:` line of each filed verbatim with the new `fleet:` field (Part A landed first — a Part B without Part A files the census by hand from the registry read). **Prediction P-B1:** `floor: 9/9 PASS` or the SKIP-honest form with the SKIP named; `fleet: 6/6 · re-seen 0` on a quiet card. **Inverse:** a second `FAIL command-confirm-s31` (the 09-12 self-recovering shape) is a finding, not noise — the bundle path filed.

## §B2 The counterfactual window (F-R4c-A; R-4c §14 ask 2)
One open window (the R-4c length). **Arm 1 (the rejoin):** the SNZB-01P `0xF044D3FFFE1C1E8E` is provoked to REJOIN — battery pull-and-reinsert inside the window — and the log is read for `rejoin_candidate … source=tc_join`. **Prediction P-B2:** a `tc_join` candidate line follows the resolution and the device adopts over the same ZDO path (`device_adopted … entities=1`). **Arm 2 (the inverse, run first on a different sleepy device already adopted, or on the 01P before the pull):** a short press only — resolution (`ieee_addr_rsp`), `source=unknown_sender`, no `tc_join`, no adoption, no error (R-4c's shape). Both arms filed with the ZDO lines and their millisecond gaps. A `tc_join` without adoption, or an adoption without `tc_join`, refutes the hypothesis and is the headline.

## §B3 The null-arm block (LASTREPORTED-1b; R-4c §14 ask 3; the audit §5.3)
On the `device_adopted` line of §B2 arm 1 (or of any adoption in the session): within 60 s, `GET /api/v1/entities` and print the new deviceId's entity `lastReported` RAW (expected `null` — the observation the diff script's `None` default masked, D-10); after its first `state_reported`, GET again and print the instant. **Prediction P-B3:** `null`, then an ISO-8601 instant equal to the first report's, never the adoption or boot time. Twenty lines, cut into the packet by the hub; TR-1b's driver may carry it later as a verb.

## §B4 The re-seen/adopted split (F-R4c-A as a constraint; the audit §5.2)
One power-cycle of the fleet card (the operator's hands — P-1's live leg is not promoted): after boot, the registry count and ids are read; every device that announces is counted RE-SEEN (a known row) or ADOPTED (a new row). **Prediction P-B4:** `re-seen 6 · adopted 0`; a new row for known silicon is F-R4-2's collision reproduced on one card and is the headline. This is the rehearsals' rule, measured once before they start.

## §B5 The restore and the second readings
The clean stop graded (`Result=success · ActiveState=inactive · ExecMainStatus=143` closes O-2 on a second reading — its own block, never in one paste with the shutdown, D-11); `S31-LABEL: <A> <W>` if H8-a did not read it; the bench card back IN; `network_formed` on the bench card is the last token. The hub banks: the floor line ×2, `fleet:`, P-B1..P-B4 adjudicated, O-2, the S31 label, and the deviations ledger — the Part B return through the same intake.

## §B6 Out of scope (both parts)
The 72-hour rehearsals (October; driven by P-1's live leg after `HARNESS-PLUG:`); the Hue's fourth silence (P-1's live-leg target); the docs' scenario catalogue; any change under `homesynapse-core/`; the rename program.

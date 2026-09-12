<!--
file: context/instructions/2026-09-11_bench-lane_P-1_power-harness-primitive_charter.md
purpose: P-1 — the power-harness primitive as a bench verb: an adopted, commandable, self-confirming smart plug used as a software-addressable mains switch, so a scenario can apply or remove power to a device under test at a chosen offset inside a window, with the plug's own state report as the in-band proof. Operator-originated (Nick, R-4b, 2026-09-04; the record's §9 P-1 block, recorded in full). This charter turns the observation into a driver script with enforced safety limits, a reserved role, and an honest limit on what it proves. Its FIRST LIVE RUN is gated: the bench's only commandable plug is the S31, and s31/nightly are HANDS OFF until R-5.
audience: the P-1 lane (a fresh Cowork conversation with ClaudeFolder connected; a bench lane — Python/bash in nexsys-bench; Nick's hands commit) · Nick (dispatches; rules the gate word) · the hub (audits)
state-type: lane charter (design + a driver script; the live leg gated)
status: ISSUE-READY (authored v70 beat 6, Fri 2026-09-11 ~18:2x CT; instrument 2026-09-11T23:28:13Z). Dispatches on Nick's paste when the two core lanes are running or landed; the October 72-h rehearsals gate on P-1.
baseline: nexsys-bench 4539f13 (tools/bench.sh · tools/runner/{engine,drivers,runner,bundles,nightly_digest}.py · scenarios/SCENARIO_FORMAT.md · scenarios/constants.yaml) · core 1e26912 (the write plane: POST /api/v1/entities/{entityId}/commands at RestFilters.java:482; the per-command read GET /api/v1/commands/{id} as command-confirm-s31.yaml:128 uses it; GET /api/v1/entities at :196).
precedents: TR1-B2 = DRIVER (a verb outside the scenario format lives in tools/ as a driver until R-5 folds it) · the R-4b record §7-A (the hue-via-plug experiment: the human left the timing loop and the next attempt was decisive) · constants.yaml:42–50 (the Hue power-topology finding: the lamp was unpowered via the S31 relay; HUE-RESET = wall power) · the Hue LCA017 6× power-cycle factory reset (the hazard the safety table exists for).
-->

# P-1 — the power harness: a plug as a test instrument (design + driver; live leg gated)

## §0 The lane contract
- `date -u` first; state your instrument limit (the bench card is NOT yours to touch in this lane; you write files in `nexsys-bench/` and run the driver in `--dry-run` on your desk). CT = UTC−5, once.
- **The one deliverable:** `nexsys-hivemind/context/audits/<your CT date>_P-1_return.md` (≤12 KB, a ceiling; §0 card first: the census with exact paths, P1–P4 adjudicated, the dry-run transcript's counts, the open questions; the last line `RETURNED <path> <bytes>`, printed to Nick).
- **Write-set:** `nexsys-bench/tools/harness/` (new) · `nexsys-bench/scenarios/constants.yaml` (one additive block, §3) · `nexsys-bench/docs/2026-09-1x_P-1_power-harness_design.md` (new). Nothing under `scenarios/*.yaml` (the suite of record; s31/nightly HANDS OFF until R-5), nothing in `tools/bench.sh`, `tools/nightly.sh`, `tools/runner/`. Never `git add`/`commit`; Nick lands with a card.
- **The fence, in one line:** this lane fires NO command at any device. The driver's only executed mode in this lane is `--dry-run`, which prints the plan and the refusals. The first live run is its own operator packet after R-5 (or after a second plug is adopted as the dedicated harness — Nick's word `HARNESS-PLUG: <entity>`).
- **Predictions (adjudicate first):** P1 — the census is `3 A + 1 M` (the driver, its test, the design doc; the constants block). P2 — the safety tests are RED at HEAD (the module does not exist) and GREEN after; the three refusals (`maxCyclesPerWindow`, `minSecondsBetweenCycles`, an unknown profile) each have a test that exercises the refusal with no network. P3 — `--dry-run` against the constants prints a plan whose every timestamp is an offset from window-open, never a wall clock, and names the plug's `state_reported` as the proof line. P4 — you find at least one cite in this charter that is wrong at your baseline and file the corrected line.

## §1 What this implements
**The verb** (`tools/harness/harness.py`, invoked as `python3 tools/harness/harness.py cycle --plug <entity-id> --at <seconds-from-window-open> [--off-for <seconds>] [--dry-run]`, and `power --plug <id> --to on|off`):
1. Reads the plug's profile from `constants.yaml` §`harness:` (§3): its entity id, its role (`harness`), its rating, the limits.
2. Refuses, before any network call, when: the plug is not declared with role `harness`; the requested cycle count in the window exceeds `maxCyclesPerWindow`; the gap since the last cycle (kept in a small state file under `~/hs-bench/harness/`) is under `minSecondsBetweenCycles`; the device under test's profile (`--dut-profile`) declares `powerCycleHazard: factory-reset` and the cycle count would cross its `resetCycles − 1` threshold. Every refusal prints one line starting `harness.refused: reason=…` and exits 3.
3. In live mode (NOT this lane): POST `/api/v1/entities/{plug}/commands` with `turn_off`, then after `--off-for` seconds `turn_on`, each followed by the per-command read `GET /api/v1/commands/{id}` until `phase_terminal` or a timeout, then the entity read for the plug's `state_reported` instant — printed as `harness.proof: plug=<id> transition=off|on commanded_at=<T> reported_at=<T'> command=<id>`.
4. Settle: after `turn_on`, the driver waits for the DUT's own readiness signal named by `--ready-token <journal token>` if given, else prints `harness.settle: unmeasured` and does not claim readiness.
5. The honest limit, printed on every run: `harness.proves: power_applied_at=<T'> — not that the device booted, joined or is healthy`.

**The role.** A plug declared `role: harness` is never also a device under test in the same leg; the driver refuses a `--dut` equal to the harness plug.

**The design doc** (`docs/…_P-1_power-harness_design.md`, ≤8 KB): the six things the harness buys (repeatability · in-band ground truth · protocol independence · matrix sweeps · cold-boot behaviours · regression), each in one paragraph with the R-4b evidence line; the safety table; what it proves and does not; the fold plan (a `harness:` stimulus key in the scenario format at R-5, when the format reopens); the shopping line (a second plug as the dedicated harness, so the S31 stays the DUT it is).

## §2 The ground (re-read; cite in your return)
- The write plane: `RestFilters.java:482` `app.post("/api/v1/entities/{entityId}/commands", …)`; the per-command read is used at `scenarios/command-confirm-s31.yaml:128` (`path: "/api/v1/commands/${let.command_id}"`); the entity read `RestFilters.java:196`.
- The S31 is the bench's commandable plug: `constants.yaml` `command.s31-entity`; its confirm posture is best_effort (command-confirm-s31.yaml's header, 2026-07-31).
- The Hue power topology: `constants.yaml:42–50` (the lamp was unplugged from the S31 on 2026-07-29; HUE-RESET = wall power). The Hue LCA017's factory reset is a rapid 6× power dance — the number `resetCycles: 6` goes in its profile row with that cite, and the driver's threshold is `resetCycles − 1`.
- The driver lineage: `tools/bench.sh` (`api_token()` reads `~/hs-bench/config/initial_api_token`; the driver reads the token the same way, never prints it).

## §3 Files (the table governs)
| Path | M/A | What |
|---|---|---|
| `nexsys-bench/tools/harness/harness.py` | A | the verb; stdlib only (`urllib`, `json`, `argparse`, `time`); `--dry-run` executes no network call |
| `nexsys-bench/tools/harness/test_harness.py` | A | the refusals (three tests, no network); the plan printer (one test: offsets only); run with `python3 -m pytest tools/harness` or `python3 -m unittest` — ground which the bench uses at `tools/runner/README.md` |
| `nexsys-bench/docs/<CT date>_P-1_power-harness_design.md` | A | the design doc (§1) |
| `nexsys-bench/scenarios/constants.yaml` | M | ONE additive block `harness:` — `plugs: [{entity: <the S31 id from command.s31-entity>, role: harness-candidate, rating_w: <from the S31 datasheet, cited>, maxCyclesPerWindow: 2, minSecondsBetweenCycles: 60}]`, `dut_profiles: [{profile: philips_hue_white_color_a19, powerCycleHazard: factory-reset, resetCycles: 6}]`; `role: harness-candidate` (not `harness`) until Nick's `HARNESS-PLUG:` word — the driver refuses a candidate in live mode |

## §4 What to watch out for
- The fence: no live command from this lane; `--dry-run` is the only executed mode; a live run is an operator packet after R-5 or the `HARNESS-PLUG:` word.
- The token never enters a file or a log line.
- Offsets, never wall clocks, in the plan; the proof line carries the wire's instants.
- Do not add a `sqlite:` or a new stimulus key to the scenario format (B1 of SCENARIO_FORMAT: the format is closed until R-5); the fold is a paragraph in the design doc, not an edit.
- The S31 is the worst-confirming commandable device on the bench (best_effort); the proof line reports what the wire says and the design doc says why a dedicated plug is the real instrument.

## §5 Out of scope
Any live power cycle · any change to the nightly, the suite of record, `bench.sh`, the runner · a second plug's adoption (Nick's, at the rig) · the scenario-format key (R-5).

## §6 Success criterion (binary)
DONE when: the census matches §3; the refusal tests are RED at HEAD then GREEN; `--dry-run` prints the plan, the refusals and the honest limit line; the design doc names the six uses with their R-4b lines and the safety table; the return is filed with its `RETURNED` line.

## §7 The dispatch line (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected)
```
date -u first. You are the P-1 bench lane for NexSys/HomeSynapse. Baseline: nexsys-bench at 4539f13, porcelain empty. Read nexsys-hivemind/context/instructions/2026-09-11_bench-lane_P-1_power-harness-primitive_charter.md WHOLE, then nexsys-hivemind/context/audits/2026-09-04_R-4b_re-rep_operator-record.md §9's P-1 block (the observation, verbatim) and §7-A, then nexsys-bench/scenarios/SCENARIO_FORMAT.md §1–§2 and tools/runner/README.md. Write only the §3 files. No live command anywhere; --dry-run is the only mode you run. Tests RED at HEAD first. Never git add/commit. Write the return to nexsys-hivemind/context/audits/<today CT>_P-1_return.md (≤12 KB; §0 card first; P1–P4 adjudicated first; the last line `RETURNED <path> <bytes>`) and say that one line to Nick.
```

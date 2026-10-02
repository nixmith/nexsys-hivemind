<!--
file: context/audits/2026-10-02_v92-b2_constants-remint_audit.md
purpose: v92 beat 2 — the constants RE-MINT 9 → 10 in `nexsys-bench/scenarios/constants.yaml` (the SNZB-06P24 adopted at REHEARSAL 1b): the figures re-read at the capture, the guarded splice and its asserts, the corpus dry-run (FAIL on the old constants → PASS on the new, against the real closed boot), the four desk gates, the card (the gated landing + BENCH-PULL-6), and one clock-law correction to the record.
audience: the v92 hub · the v93 boot · Nick (§0 and §5)
state-type: audit (one beat)
status: FILED v92 beat 2 (Fri 2026-10-02 ~08:2x CT; instrument 2026-10-02T13:27:03Z)
-->

# v92 beat 2 — the constants re-mint to the fleet of 10

## §0 Verdict
**The re-mint is on Nick's desk, dry-run on the corpus and gated; the card is two blocks.** `scenarios/constants.yaml` (md5 `9407fafe6554` → `9b0af47b3376`; 43,910 → 44,706 B; +10 lines; `git diff --numstat` 12/2): `fleet.devices` and `fleet.entities` 9 → 10; `remembered-ulids` + `01M3Y4YA6YSYQWVE9ET8FT4HWQ` (ten entries = the capture's entity set, asserted); the fleet block's re-mint comment and the growth line; every other key YAML-identical (asserted). The corpus dry-run — `runner.py scenario boot-health --against` the closed boot `bench-2026-10-02-075042.log` with `entities-after.json` as the scripted api — FAILS on the old constants at exactly the three fleet asserts and PASSES on the new (5 log positives + 1 api line; 10 rows; all 10 ULIDs). The four desk gates are green after the edit. Block 1 lands it (1 file, gated) → `BENCH: LANDED <sha>`; Block 2 pulls it to the Pi with the three selftests, the constants md5 and the pinned-core check → `BENCH-PULL-6: <sha> · 42/0 · 26/0 · 27/0 · 9b0af47b3376`. BC7's card (beat 3) reads Block 2's after-sha at Part A and never moves the core before it.

## §1 The figures, re-read at the capture (`_scratch/v90/thu1001/reh1b/pi-capture/`; Pi stamps are America/New_York, UTC−4)
| Figure | Instrument | Value |
|---|---|---|
| The join | `bench-2026-10-02-070945.log`, the `zigbee.device_adopted` line for `01M3Y4YA6KMH7JDEF5YMMJ3YND` | `07:10:41.409` Pi = **2026-10-02T11:10:41Z** = 06:10:41 CT; `device=0xA4C13814CE41FFFF … entities=1` |
| The closed boot | `bench-2026-10-02-075042.log` | `registry.projection_live: devices=10 entities=10 position=849602` (07:50:53 Pi) · `zigbee.adoption_maps_rehydrated: devices=10` · `relinked=10 permit=0` (the capture's own summary line) |
| The entities | `entities-after.json` (`meta.timestamp` 2026-10-02T11:51:27Z, `viewPosition` 852331) | 10 rows; the new row `entityId 01M3Y4YA6YSYQWVE9ET8FT4HWQ · availability AVAILABLE · deviceId 01M3Y4YA6KMH7JDEF5YMMJ3YND · lastReported 11:48:31Z` |
| The Pi's offset | `S0-friday-state.txt` `pi-clock 11:04:55Z` beside the log's local stamps; the closed boot's 07:50:53 local against the entities read 11:51:27Z | UTC−4 (EDT) — holds |
The splice re-reads the first three rows from the files before it edits (a `device_adopted` line beginning `07:10:41.409`; the two boot strings present; 10 rows with the new ULID AVAILABLE) — the figures are never typed from a report.

## §2 The splice (`_scratch/v92/b2/remint_constants.py`) — what it asserted before its one write
Bench HEAD `ede32c9`, porcelain empty, no lock; the file's md5 `9407fafe6554…`, no `\r`. Three anchors, each found once: (A1) the fleet block's two T4 comment lines + `devices: 9` + `entities: 9` → the same two lines + the eight-line REHEARSAL 1b comment + `devices: 10` + `entities: 10`; (A2) the G4-2 ULID line → itself + the SNZB-06P24 line; (A3) the "Grown 2 -> 6" comment → itself + the "6 -> 9 … 9 -> 10" line. Post-conditions on the text: `devices: 10`/`entities: 10` once each and no `9`; the new ULID once; the `remembered-ulids` block parses to 10 distinct Crockford ULIDs equal to the capture's entity set; line count +10; `yaml.safe_load` gives `fleet == {devices: 10, entities: 10}`, the list's last element the new ULID; the two YAML trees minus `fleet` and `remembered-ulids` EQUAL (nothing else moved); no trailer string. Then the write; the md5 after `9b0af47b3376`.

## §3 The corpus dry-run (`_scratch/v92/b2/dry/`)
- **The fixture, from a REAL capture (labeled so in its first line):** `boot-075042.log` = the closed boot log, byte-copied; `boot-075042.api.yaml` = `{responses: {"/api/v1/entities": [{status: 200, body: <entities-after.json>}]}}` — the runner's sibling convention (`engine.load_api_fixture`); never placed under `fixtures/runner-demo/`, whose files are SYNTHETIC by rule.
- **BEFORE (constants at 9) — `dry-before.txt`, exit 1:** `[X] expected-not-seen: log 'registry.projection_live: devices=9 entities=9' min=25065 (saw 0/1)` · `[X] expected-not-seen: log 'zigbee.adoption_maps_rehydrated: devices=9' (saw 0/1)` · `[X] expected-not-seen: api /api/v1/entities {"rows": 9, "ulids": [… 9 …]}` · `[FAIL] boot-health`. The other positives (two `device_relinked`, `network_resumed: channel=20 panId=0x774c`, `port_identity_captured: … pinnedOnly=false`) and the forbidden `device_proposed` were satisfied — the failure is the fleet count alone. The pre-registration ("the three fleet asserts fail; nothing else") HELD.
- **AFTER (constants at 10) — `dry-after.txt`, exit 0:** `[PASS] boot-health — 5 log positive(s) + 1 api line(s) satisfied against the fixtures (api: scripted SYNTHETIC responses)`; `provenance: 1 declared ULID(s) present in the card's own /api/v1/entities (minted-by hs-dev-1)`.
- **What the dry-run proves and what it does not:** the constants and the scenario agree with the fleet the Pi actually booted at 07:50 Pi on `40412f9`; it says nothing about `5b0e20c` (BC7's Part C grades THAT boot — the same `--against` on tonight's boot log is the card's first post-restart read, before the api is read live).

## §4 The desk gates (after the edit; `desk-gates.txt`)
`python3 -B tools/test_bench_sh.py` 27/0 · `tools/runner/test_engine.py` 42/0 · `tools/harness/test_harness.py` 29/0 · `tools/verify72h/test_verify72h.py` 26/0; porcelain after the runs: `scenarios/constants.yaml` alone (no bytecode — `-B`). The gates read temp constants by design (they fence the tools, not the repo's values); the repo's values are graded by §3.

## §5 The card (`_scratch/v92/b2/card_b2_bench.txt`) and the prior-ledger gate
Block 1 = THE THURSDAY ORDER's T4 form under the IR-101 gate (the md5 printed before the add; `expect 1`; the trailer grep; `commit -F`; push). Block 2 = BENCH-PULL-5's block (`_scratch/v88/b3/card_b3_bench.txt` Block 2) with three edits: the `permit-join` usage probe dropped (BH-3 is landed; the verb is BC7's), a `constants-md5 … fleet: devices: 10 entities: 10` line added (the pull's proof that the Pi runs the re-mint), the expected `before:` widened to `ede32c9` OR `d093a95` (BENCH-PULL-5 was never said — IR-76's record is this block's `before:`). The prior-ledger greps: `BENCH-PULL` in the v89 b1 audit and the v88 b3 card (the form); `constants.yaml` in the T4 card (the form); the 1b intake audit §4 for the ULID and the figures (equal). THE RESTORE RUNS BEFORE THE GAP: the card edits nothing on the Pi beyond the pull; no restore is owed.

## §6 A clock-law correction to the record
The brief's rig row (v90 b6) and D-v90-17 wrote the join as "Fri 07:10 CT" / "completed at 07:10". The instrument's line is `07:10:41.409` on the Pi's clock (UTC−4) = 11:10:41Z = **06:10:41 CT** — inside the 06:02–06:58 CT sitting, as the 1b audit's own envelope says. The brief's row is corrected this beat (D-v92-8); the v90 DR is a closed record and stands as written with this section as its correction; the ordering claim (the join after the 03:30 nightly) holds in every clock.

## §7 Layer 2
Re-executed: the capture's three figures (`grep`, `json`); the splice run on the device with every assert; `git diff --numstat` 12/2 and porcelain 1; the dry-run before and after (exit codes and verdict lines); the four selftests' last lines. Not re-executed: the Pi (Block 2 is Nick's); the commit (Block 1 is Nick's); the nightly's Saturday read (the pre-registration rides BC7's card).

<!--
file: context/audits/2026-09-27_v83-b4_BC5-intake_the-close_audit.md
purpose: The v83 beat-4 audit — THE CLOSE: BENCH-CORE-5 intaken two-layer at its outputs (`context/audits/2026-09-27_BENCH-CORE-5_outputs.txt`, 8,352 B, sha256 `b8573e71fbeb3136…`; the guide notes 19,624 B); IR-83's immediate probe adjudicated (the race PATTERN, confounded by the pre-IR-61 checkpoint; the deterministic probe named); IR-61's second attestation seen live; Monday's nightly re-registered on `1f1d1e0`; v84's text cut; v83 CLOSED at four (D-v83-21, the context rule).
audience: the v83 hub · Nick (§0) · v84 (§0, §2)
state-type: audit (filed once)
status: FILED — v83 beat 4, THE CLOSE (Sun 2026-09-27 ~18:2x CT; instrument 2026-09-27T23:24:29Z)
-->

# v83 beat 4 — BENCH-CORE-5 intaken; the close

## §0 The verdicts
- **BENCH-CORE-5 ACCEPT.** The one line's every number at its own output line (§1): `deployed=1f1d1e0` · boot-health 6/6 · 0 forbidden · rows 383977 → 384512 · relinked 9 · plugs A/A/A · `ir61-class-in-tree=1` (`state-store-0.1.0-SNAPSHOT.jar`) · the serving JVM (pid 31470) started 23:02:52Z, after the launcher was written at 23:00:09Z · both prior-ledger fixes visible · the key ABSENT (`key-lines=0`; seven pre-boot logs at `permit_join_opened=0`) · the backup at `~/hs-backup/20260927T225733Z`. The sitting ran 22:54–23:08Z = **17:54–18:08 CT** (14 min 12 s), inside the 20:15 CT bound. **The bench card is on `1f1d1e0`.** Monday's 03:30 CT nightly is RE-REGISTERED on it: `8/9 PASS · fleet: 9/9 · re-seen 9`, 0 forbidden — the same line; IR-61 touches no scenario the nightly reads.
- **IR-61's second attestation, live (reading (ii)):** at 23:06:19Z and 23:08:19Z all six `staleAfter` values are set and every one equals its plug's last report **+ 1200.000 s** (G4-1 23:06:16.145 → 23:26:16.145; TR3 23:03:18.544 → 23:23:18.544; G4-2 the same pattern) — `power_meter`'s threshold by THE DERIVATION RULE, read on the wire. `stale=False` on all, correctly (each within its window).
- **IR-83's immediate probe: the race PATTERN, CONFOUNDED — not adjudicated as observed.** The TR3 read ≈ 23:03:1xZ, 8 s before its first post-boot report (23:03:18.544Z), gave `staleAfter=None` with `lastReported=22:53:18.535Z`. Two causes fit: (a) the 22:53:18 report was in the replayed tail and resolved on a registry miss (the race); (b) the checkpoint the new core resumed from was written by `e96dce8`, which never set `staleAfter` — so every entity's checkpointed value was null and TR3 had no tail report. Tonight cannot separate them. **The deterministic instrument (PI-PROBE-2, Monday, read-only):** in the B1 backup (`~/hs-backup/20260927T225733Z/homesynapse-events.db`, 22:57:33Z), the state projection's row in `view_checkpoints` against TR3's (`01M3DM74SGEY7RXVDYSM4PK2XA`) last `state_reported` `global_position` — the report's position above the checkpoint's = it was in the tail = the race CONFIRMED; at or below = the confound. Also found at the source: the state projection logs **no LIVE line** (`awaitProjectionLive()` polls `projectionMode()` silently), which is why the card's reading (a) read "one line only" — IR-61b gains an observability row (`state.projection_live: position=…` beside the registry's). The ordering gate stays IR-61b's first row either way (design, not a patch).
- **P4 sample 3 = A/A/A** (BC5's orderly restart; IR-56's class 0 of 3). The rehearsal's kill −9 is sample 4 and decides IR-56's shape (D-v83-17).
- **The §7 probe:** `384123 rows, ciphered=0`; `command_result` payloads are `blob`-typed but readable JSON with **snake_case keys** (`target_entity_ref`, `command_t…`) — VERIFY-72H-A decision 4's opaque branch is not needed on this card; the lane's fixtures must use the codec's snake_case, checked at its intake.
- **v83 CLOSED at beat 4** (D-v83-21; the context rule): v84's text LIVE (`context/handoff/2026-09-27_v84_dispatch-text.md`); THE ONE DELIVERABLE carries to v84 unexecuted — Mon at `REH1:`'s hour (09:00 by the record; Nick's message said noon).

## §1 Layer 2 — the one line at the outputs' lines
| The line said | The output line | Verdict |
|---|---|---|
| deployed 1f1d1e0 | B3 `deployed=1f1d1e0`; B2 `Updating e96dce8..1f1d1e0 · Fast-forward · clone: 1f1d1e0 feat(state-store): IR-61 …` | ✔ |
| boot-health 6/6 | B3 `[PASS] boot-health — 6/6 positive · 0 forbidden`; bundle `boot-health-20260927T230307Z` | ✔ |
| rows 383977→384512 | B0 `383977`; B3 `384512`; B1 backup `384198`; the probe `384123` — monotone; integrity `ok` twice | ✔ |
| relinked 9 · plugs A/A/A | B3 `relinked=9 adopted=0 formed=0 resumed=1 config_issue=0`; B4 two PLUGS lines, all AVAILABLE | ✔ |
| ir61-class-in-tree=1 | B3 `ir61-class-in-tree=1 jar=state-store-0.1.0-SNAPSHOT.jar` | ✔ |
| staleAfter@180s 3 set | B4 @23:08:19Z: 1790551698.129 · 1790551398.545 · 1790551695.982 (all = last report + 1200 s) | ✔ |
| TR3-immediate null | B3 `TR3-immediate: avail=AVAILABLE stale=False staleAfter=None lastReported=1790549598.535246` (= 22:53:18.535Z) | ✔ read; adjudicated §0 |
| live-order one line only | B3 one `registry.projection_live` line (19:02:58.838 Pi-local, the relaunch's) — no state-projection live token exists at the source | ✔ |
| probe ciphered=0 | B0b `probe: 384123 rows, ciphered=0` + two readable `command_result` rows | ✔ |
| outputs 8352 · notes 19624 | `wc -c` 8352 / 19624; sha256 `b8573e71fbeb3136…` | ✔ |
Timestamps: Pi log lines are UTC−4 (`19:02:15.419` = 23:02:15Z = 18:02:15 CT); the `===` stamps are UTC — converted here, never carried.

## §2 The guide's sixteen observations, ruled
Obs. 1 (17:54–18:08 CT; no nightly since BC4) · 2 (one poll) · 3 (the fixes hold) · 5 (two boots) · 6 (the evidence chain) · 10 (A/A/A; the operator note recorded, not acted on) · 12 (rates ≈ 67/min) · 13 (18/42 tasks, 26 s) · 15 (the artifacts) — accepted as read. **Obs. 4 (IR-77):** `config/` mtime moved again at boot-health's relaunch (third time) — IR-77's row gains the third sample; still a read, not a fix. **Obs. 7:** correct — the token does not exist; IR-61b's observability row. **Obs. 8:** the guide's "race pattern" is the right words for what was read; the hub's adjudication is §0 (confounded). **Obs. 9:** the arithmetic re-done here (§1). **Obs. 11:** snake_case — into VERIFY-72H-A's intake. **Obs. 14:** cosmetic (the `grep -n` prefix; `cache_loaded=` label) — carried to the next card's cut. **Obs. 16:** B0b's gate is pre-boot by design; tonight's two boots are covered by the unchanged `zigbee.yaml` hash and `key-lines=0` — accepted; the next card's B4 could add the current boot's `permit_join_opened` count (one grep) — noted for BC6.

## §3 Not re-executed, disclosed
The Pi (nothing touched after the sitting); the backup's checkpoint position (PI-PROBE-2 is Monday's); VERIFY-72H-A's progress (its return file is the proof); the twelve untouched entity bodies; the boot log beyond the lines the card printed.

## §4 Definition of done (the close)
- [x] BC5's return exists at the named paths; audited two-layer; this audit filed; the outputs and notes filed under `context/audits/`. [x] The nightly re-registered on `1f1d1e0`. [x] IR-83 adjudicated; PI-PROBE-2 named; IR-61b's rows grow by one. [x] v84's text cut. [x] The DR §3d; CLOSED. [ ] The close card (b3 + b4) handed → `HIVE: LANDED <sha>`. [x] The next act named: Monday — paste v84's text at the rehearsal's hour; `REH1:` and `TM:` in the first message.

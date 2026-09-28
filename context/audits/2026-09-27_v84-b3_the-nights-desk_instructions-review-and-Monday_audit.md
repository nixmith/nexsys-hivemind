<!--
file: context/audits/2026-09-27_v84-b3_the-nights-desk_instructions-review-and-Monday_audit.md
purpose: The v84 hub's beat-3 audit — the night's desk: IR-61b and LOCK-1 authored as one Java lane in series, IR-61b reviewed independently (DISPATCH WITH EDITS, E1–E10, applied), PI-PROBE-2's read-only card and VERIFY-72H-A2's charter cut, Monday's order of acts filed as one packet; the premise correction (the state projection already logs its catch-up); the layer-2 record.
audience: the hub · Nick · v85
state-type: audit (filed once; never edited)
status: FILED — Sun 2026-09-27 ~21:1x CT (instrument 2026-09-28T02:12:16Z)
-->

# v84 beat 3 — the night's desk

## §0 Verdict
FOUR INSTRUCTIONS CUT AND ONE REVIEW FILED; nothing dispatched tonight (every dispatch waits for Monday's paste, D-v84-12). `BENCH: LANDED 9fa2382` banked at the instrument (9 files = 4 M + 5 A; porcelain 0; pushed; no trailer; no lock). The one premise the night corrected: D-v83-25 said the state projection logs no LIVE line — it does (`StateProjection.onCaughtUp()` :588); IR-61b adds no line (D-v84-14).

## §1 The files
| File | What | Size |
|---|---|---|
| `context/instructions/2026-09-27_coder-lane_IR61b_staleness-config-keys_boot-ordering-gate_coding-instruction.md` | the §9 keys (`StalenessConfig`, `StateStoreSchema`); the ordering gate before `subscribeRuntime(projectionInfo, stateProjection)` (:647); T1–T4; premises at `1f1d1e0` with the hub's counts (§6, 16 rows); REVIEWED and re-cut | 26,153 B |
| `context/instructions/2026-09-27_coder-lane_LOCK-1_integration-id_and_migration-bytes_pinned_coding-instruction.md` | two pinning tests (`6V1CMGY2HKF4H1FGZ4H7F257FS` = `deriveStable("zigbee")`, hex `db0b290f…`; the five migration digests computed at `1f1d1e0` by `git show \| sha256sum`); the ONE Java paste (LOCK-1 then IR-61b) in its §14 | 13,347 B |
| `context/audits/2026-09-27_IR61b_independent-review.md` | the in-conversation review by an agent that had not seen the authoring (19 source copies at `1f1d1e0` + Doc 03); DISPATCH WITH EDITS E1–E10 | 10,214 B |
| `context/instructions/2026-09-27_PI-PROBE-2_boot-replay-race_checkpoint-vs-last-report_operator-card.md` | one read-only block on the B1 backup; the reading rule explicit (TR3's last report ABOVE the state projection's `view_checkpoints` position = the RACE; at or below = the CONFOUND) | 4,565 B |
| `context/instructions/2026-09-27_bench-lane_VERIFY-72H-A2_grader-payload-keys_snake_case_charter.md` | IR-89's fix: the eight reads → snake_case; the fixtures re-cut; ONE real-payload test; the `/state` keys pinned against the FROZEN v1.1 contract (camelCase, `contract.ts` :272–:274); deviation 5's line | 7,512 B |
| `_scratch/v84/2026-09-28_MONDAY_the-order-of-acts.md` | Monday whole, one file: Acts 1–8 with every block inline (BENCH-PULL-2 and PI-PROBE-2 byte-identical to their cards — `diff` = 0), one line back each | 11,073 B |

## §2 The review, taken apart (the hub's layer 2 on the reviewer)
E1 (the state projection already logs `caught up at position`) — RE-VERIFIED at `StateProjection.java` :572–:590; the new line DROPPED. E8 (the bus flips LIVE before `onCaughtUp()`) — RE-VERIFIED at `TransitionCoordinator.java` :142 `setMode(LIVE)` / :156 `onCaughtUp()`; T3's order assertion carries §9.9's caveat and a five-run red count before the gate. E2/E9 (:647, :621–:625, :606–:610, :1428) — re-verified by grep, applied. E3/E4 (the plug's ULID is minted at adoption — T2 and T3b re-cut around `adoptGen4()` → rewrite `homesynapse.yaml` → `restart(NO_STOPWATCH)`) — applied; `RealCoreFixture` :258–:274, :347–:352 taken from the reviewer's read, not re-executed. E5 (T4 via `configurationService().reload()` :1607 and `ReloadResult.issues()`) — re-verified (`ReloadResult.java` :34; `ConfigurationService.java` :82); applied. E6 (null YAML keys; `P..D` rejected as `parseIso8601` does) — applied to §4. E7 (`EntityId.parse` :56) — re-verified; applied. E10 (the :671–:676 "ONE sanctioned addition" comment) — applied to §3 row 3. The reviewer's §6 (not verifiable from the copies: `StandardConfigurationService`'s handling of an unregistered section, the bus order, MODULE_CONTEXT, build deps) → the Coder's §6 re-run and §10 pushback cover each.

## §3 Layer 2 — re-executed and not
Re-executed: the bench landing at porcelain (`9fa2382`, 4 M + 5 A, 0 trailers, 0 locks); the sixteen §6 greps of IR-61b at `1f1d1e0`; the migrations' five digests and the `zigbee` id's hex and Crockford form (the record's three evidence reads carry the literal); `.gitattributes` :9; the config module's `state_store` absence; `nightly.sh`'s pull grep (none); the two packet blocks against their cards (`diff` = 0). Not re-executed: `RealCoreFixture`'s restart path (the reviewer's read); whether `rawMap()` keeps an unregistered section (the Coder's §10 STOP covers it); the Pi (untouched).

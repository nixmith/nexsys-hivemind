<!--
file: context/audits/2026-09-29_v87-b3_PJ2_WUCP-Phase-2_audit.md
purpose: v87 beat 3 — WUCP Phase 2 (PM closeout) for PJ-2, landed as `146468c` + `8deef4b`: the MODULE_CONTEXT rows verified at source, the gate, the return's [INFO] and §5 findings dispositioned, the register rows, the Open Risks row, the one Check-11 STALE found.
audience: the v87 hub · the v88 boot (by §0) · the docs card's author (§3)
state-type: audit (WUCP Phase 2)
status: FILED — Tue 2026-09-29 ~17:1x CT (instrument 2026-09-29T22:18:59Z)
-->

# v87 beat 3 — WUCP Phase 2 for PJ-2

## §0 Verdict
**PHASE 2 CLOSED.** Six MODULE_CONTEXT rows landed and hold at source; no deferred build gate; twelve [INFO]s and seven §5 findings dispositioned (one Open Risks row, two register rows, three docs-card rows); one Check-11 STALE found in the landed rows (a copied-forward count → IR-103). Nothing blocks the Java queue.

## §1 The MODULE_CONTEXT rows (Step 1 — verified, not re-authored)
`git show --stat 146468c -- '*MODULE_CONTEXT.md'`: `api/rest-api` (12 ±) · `core/event-model` (+2) · `integration/integration-api` (6 ±) · `integration/integration-runtime` (+4) · `integration/integration-zigbee` (+24) · `lifecycle/lifecycle` (+2). Read whole (the `+` lines). Spot-checks at source (`8deef4b`): `EventTypes` public String constants = **75** (the row says 73→75 ✓); `PERMIT_JOIN_OPENED` at :306, `PERMIT_JOIN_CLOSED` at :312 ✓; `PairingWindowPort.java` tracked under rest-api ✓ (the nested `PairingWindowView` — I1); `permit_join_key_ignored` at 2 sites in integration-zigbee ✓; the module-info claim ("ZERO impact; rest-api does not require integration-api") consistent with the squash's stat (no `module-info.java` changed).
**One STALE (Check 11):** rest-api's `**Total: 29 public types + 10 package-private + 1 module-info.java = 40 Java files**` (:152; PJ-2 incremented the prior "38"). Source: 52 `.java` under `api/rest-api/src/main/java/com/homesynapse/api/rest` + `module-info.java` = **53**; `^public (class|interface|record|enum)` top-level in 33 files, 19 package-private. The prior 38 was stale against 51 — a count copied forward, not regenerated. No fabricated type (not CONFLICTED). → IR-103; the line is fixed by the next rest-api unit's card (a core docs commit under Nick's hands).

## §2 The gate (Step 2a) and the coder-handoff (Step 2)
Deferred Build Gate: **none** — coder-handoff :3 "`check` green in the lane; CI on the landing sha is the gate of record"; CI green on `146468c` and `8deef4b` (Nick, Mon 21:07 CT). The PJ-2 entry's landing clause now carries the shas and this Phase 2's close.

## §3 The return's findings, dispositioned
| Finding | Disposition |
|---|---|
| I1–I10, I12 (shapes, moved constants, the never-false-ALIVE read, the header, the fixtures' dropped key, the R1-green absence pins, the porcelain count) | recorded in the rows; nothing to carry |
| I11 — the endpoint's 5-s `get` holds one `hs-http` Jetty pool thread (`javalinMinThreads/MaxThreads` from the profile) | accepted as argued (an operator's onboarding call; bounded by the timeout); no row |
| F1 — the bench pairs by the key only; a key-driven boot on PJ-2's core opens nothing | **OR-BENCH-FENCE-PJ2** opened (pm-handoff Open Risks); the pinned clone (BC6b's form) is the standing control until BH-3 |
| F2 — `[SYSTEM]` category fallback for the two events (D3) | IR-100 (the docs card: Doc 01 §4.4) |
| F3 — at-rest snake_case vs REST camelCase, consistent with every other event | the docs card: Doc 03's row for `permit_join_opened/closed` payload keys |
| F4 — the close has no log line by design; the event is the record | the docs card: Doc 03 §9's token table records the silence; IR-95's vocabulary row beside it |
| F5 — the shared `integration(id)` subject; a `SequenceConflictException` = ONE WARN, unobserved · F6 — the three closers' CAS pinned by construction, no three-thread test | **IR-102** — an instrument row on BH-3's card first (conflict grep; closed = opened in the store), a race test only on a hit |
| F7 — the cloud container's Maven route rate-limited (429) | the cloud form's environment note (D-v86-6; the lesson of 2026-09-28); no row |

## §4 The register (Step 4) and the docs card's list
IR-98 (count pins) and IR-99 (one status table) stay OPEN → W-SKILLS-10 (Wed); IR-100 stays OPEN → the docs card. New: IR-102, IR-103. The docs card's list now: IR-81 (Doc 03 §3.8's status line) · AMD-53 :78 · Doc 02 §3.5 · Doc 03 §9's `PT…` (D-v84-13) · IR-100's Doc 01 §4.4 row · D4's fourth WARN token · IR-95's §3.9 outcome vocabulary · IR-97's `event_time` definition · F3's payload-key row · F4's close-silence row · the `permit_join_duration` schema text (IGNORED since PJ-2; its removal is the `CONFIG-ERROR:` decision, IR-90).

## §5 Not done here, and why
The traceability index (`homesynapse-core/docs/traceability/`) and `phase-3-milestone-backlog.md` carry no IR rows; IR-class units are queued in the register and THE WEEKS AHEAD §2 — the same reading v84 b5 made for IR-61b. MODULE_CONTEXT edits are core-tree writes (Nick's hands) — the one correction (IR-103) rides the next rest-api card rather than a docs-only commit tonight.

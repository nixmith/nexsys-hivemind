<!--
file: context/instructions/2026-09-21_coder-lane_IR40-IR44_time-range-plan-on-the-index_startup-report-automation-arm_coding-instruction.md
purpose: IR-40 + IR-44 on the Java slot (D-v78-1 — Nick's JAVA-QUEUE, ACCEPT): (a) `SqliteEventStore.readByTimeRange` planned on `idx_events_event_time` through the shipped sqlite-jdbc 3.51.3 instead of the rowid walk that makes `explainRun` O(N) (MEASURE-2b F-2: 1.8 → 90.5 ms at 500k rows), with the plan asserted by a test; (b) the `automation` arm of `HomeSynapseCore.recommendationFor` so a FATAL identity companion names its file and the operator's act. Two trivial-to-small rows, one session, one return; every mechanism claim names its code path at `d2cddb1`.
audience: the Coder lane (a host-side Claude Code session in homesynapse-core; the nexsys-coder skill) · the hub (the intake) · Nick (§14)
state-type: coding instruction (the Java slot; one session; one return)
baseline: core `d2cddb1` (LINK-READ) — re-verify at issue with `git log -1 --oneline`
status: RETURNED + ACCEPT v78 beat 5 (Wed 2026-09-23 ~00:2x CT; instrument 2026-09-23T05:20:53Z) — the return `context/audits/2026-09-21_IR40-IR44_return.md` (11,998 B); the core card cut (6 = 5 M + 1 A); EXECUTED when CI is green on the landing sha. Was: DISPATCH-READY v78 beat 4 (2026-09-21T19:01:04Z) — dispatched on Nick's paste of §14. Returns to `context/audits/<filing-date>_IR40-IR44_return.md`.
-->

# IR-40 + IR-44 — the time-range read on its index; the startup report's automation arm

## §0 The lane contract (read first; every line binds)
- `date -u` first; CT = UTC−5. The read-set is §2; the write-set is §3 — a file not in the table is a deviation, reported. Tests first (red, then green); `./gradlew check` green; the tree left at porcelain, uncommitted, unstaged. The return ≤ 12,000 B, §0 first, at `context/audits/<filing-date>_IR40-IR44_return.md`; the last line of your last message: `RETURNED <path> <bytes>`. A mechanism claim names its code path; a number names its instrument. Pushback with evidence at the bytes (§10); never a silent re-scope. Before writing a byte: grep `FROZEN` in every MODULE_CONTEXT.md you will touch and `containsExactly` in the tests of every log line you will change — a frozen token is a pin (the LINK-READ lesson); a hit is a fork raised to the hub, not a choice.

## §1 What this implements
**(a) IR-40 — the plan.** `SELECT_BY_TIME_RANGE_SQL` (`SqliteEventStore.java:220–:226`: `WHERE global_position > ? AND COALESCE(event_time, ingest_time) >= ? AND … < ? ORDER BY global_position ASC LIMIT ?`) is planned by sqlite-jdbc 3.51.3 (`gradle/libs.versions.toml:17`) as `SEARCH events USING INTEGER PRIMARY KEY (rowid>?)` — a walk from `afterPosition` upward testing the time predicate on every row until `LIMIT` fills, so a narrow window near the log's end costs the whole log. `explainRun`'s only time-range read is `StandardExplanationService.triggeredInWindow` (`:1140–:1155`; `readByTimeRange(from, to, after, SCAN_BATCH)` with `SCAN_BATCH = 500`, `:115`) over `[t − HINT_LEAD, t + HINT_LAG)` around the run's ULID timestamp (`:1120–:1121`) — a window of a few rows. The index exists: `V001__initial_event_store_schema.sql:61` `idx_events_event_time ON events(COALESCE(event_time, ingest_time))`, and the SQL's predicate already matches its expression (`:217–:218`). The fix is the plan, not the schema: `FROM events INDEXED BY idx_events_event_time` in `SELECT_BY_TIME_RANGE_SQL` — SQLite then reads the window's rows from the index, filters `global_position > ?` and sorts the few by position for the `LIMIT`; the contract of `readByTimeRange` (`EventStore.java:141`: `[from, to)`, ascending position, `afterPosition`/`maxCount`) is unchanged. `INDEXED BY` is chosen over a rewrite because it fails loudly if the index ever disappears — a migration that drops or renames it breaks the test in §7, never the plan silently. (The `:773–:774` sibling query is a `LIMIT 1` existence read; leave it unless the plan test shows the same walk — then the same clause, said in the return.)
**(b) IR-44 — the arm.** `HomeSynapseCore.recommendationFor(String subsystem)` (`HomeSynapseCore.java:1638`; called at `:465` into `new StartupFailureReport(phase, subsystem, recommendation)` `:467`; the record `lifecycle/.../StartupFailureReport.java`, 2,194 B — NOT under `app/` as IR-44's row says; the hub corrects the row) has no arm for the automation subsystem: a FATAL identity companion (AUTO-ID-1 T8: an unreadable or malformed `automations.ids.yaml`, wired at `:677–:678` as `configDir.resolve("automations.ids.yaml")`) prints the default recommendation and exit 99. Add the arm: the recommendation names the companion's path and the operator's act (the file is engine-managed — restore it from the newest `~/hs-backup/` copy or delete it so the engine mints fresh ids and says so; never hand-edit), in the C12-04 operator voice the record's other arms use.

## §2 Files to read before starting (the minimum read set — mandatory)
`core/persistence/MODULE_CONTEXT.md` and `lifecycle/lifecycle/MODULE_CONTEXT.md` and `core/automation/MODULE_CONTEXT.md` — by grep only (`readByTimeRange`, `SELECT_BY_TIME_RANGE`, `idx_events_event_time`, `recommendationFor`, `StartupFailureReport`, `FROZEN`); they are 196 KB / 113 KB / 145 KB and are never read whole · `SqliteEventStore.java:170–:232, :672–:700, :765–:780` · `EventStore.java:130–:145` · `V001__initial_event_store_schema.sql:50–:62` · `StandardExplanationService.java:110–:118, :1115–:1160` · `HomeSynapseCore.java:455–:470, :670–:680, :1630–:1665` · `StartupFailureReport.java` whole · `HomeSynapseCoreStartupFailureTest.java` (6 tests; the shape yours follows) · `MeasureReadPathIT.java:40–:130, :300–:330` (the MEASURE2B line; `HOMESYNAPSE_MEASURE2B_ROWS`) · the persistence module's existing store tests (`git ls-files 'core/persistence/src/test/*SqliteEventStore*'`) for the temp-database-with-migrations idiom · `HomeSynapseArchRules.java` (`NO_DIRECT_TIME_ACCESS`).

## §3 Files to create or modify (the Files table governs)
| # | File | Change |
|---|---|---|
| 1 | `core/persistence/src/main/java/com/homesynapse/persistence/SqliteEventStore.java` | `SELECT_BY_TIME_RANGE_SQL` gains `INDEXED BY idx_events_event_time` (`:220–:226`); the Javadoc at `:216–:219` states why (the rowid walk; MEASURE-2b F-2; the loud failure on a dropped index). Nothing else in the file. |
| 2 | `core/persistence/src/test/java/com/homesynapse/persistence/SqliteEventStoreTimeRangePlanTest.java` | NEW: T1–T3 (§7) on a temp database built by the real migrations, through the shipped driver. |
| 3 | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | the `automation` arm in `recommendationFor` (`:1638`); the subsystem string is whatever `:465`'s caller passes for the automation phase — read it at the call sites (`git grep -n 'failStartup\|recommendationFor' lifecycle/`), never invent it. |
| 4 | `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreStartupFailureTest.java` | T4 (§7), in the file's existing shape. |
| 5 | `core/persistence/MODULE_CONTEXT.md`, `lifecycle/lifecycle/MODULE_CONTEXT.md` | one row each: the `INDEXED BY` and its test; the arm. Nothing else. |
No module-info, Gradle, migration or configuration change. No change under `core/automation` (the caller's paging is right once the plan is).

## §4 Technical specification
`module-info.java` of `com.homesynapse.persistence` and `com.homesynapse.lifecycle` are unchanged by this unit and are not re-embedded (no JPMS proposal); `java.sql` is already required by persistence. The plan test uses `EXPLAIN QUERY PLAN` on the exact SQL string (expose it package-private as `static final String` if it is private — say so in the return) with bound-parameter placeholders, asserts one `detail` row contains `USING INDEX idx_events_event_time` and none contains `USING INTEGER PRIMARY KEY`. The database: a temp file, the real migrations applied the way the store's own tests do it (never a hand-written schema). The arm: a plain string in the existing switch's voice; no new type.

## §5 Locked decisions and invariants that apply
Doc 01 §4.2 (the index key and the `COALESCE` semantics — `:217–:218`) · INV-WRITER-01 untouched (a read-path change only) · the `[from, to)` contract (`EventStore.java:141`) · `NO_DIRECT_TIME_ACCESS` (the tests inject `Clock`; the plan test needs no clock) · C12-04 (the operator hint's voice).

## §6 P2 consumer/pin survey (run by the hub at `d2cddb1`)
`readByTimeRange`: one implementation (`SqliteEventStore.java:672`), one production caller (`StandardExplanationService.java:1146`), the interface (`EventStore.java:141`); the SQL string is private — its only reader is the store. `recommendationFor`: one definition (`:1638`), one caller (`:465`). `StartupFailureReport`: constructed at `:467` only. No frozen token is touched (the `lifecycle.startup_failed` line at `:468` keeps its keys; only the recommendation's TEXT for one subsystem changes — grep `containsExactly` in `HomeSynapseCoreStartupFailureTest` before editing: if a test pins the default recommendation for the automation subsystem verbatim, that is a fork, raised, not re-cut).

## §7 Test requirements (red first; each named in the return)
- T1 `SqliteEventStoreTimeRangePlanTest.plan_usesTheEventTimeIndex`: `EXPLAIN QUERY PLAN` of `SELECT_BY_TIME_RANGE_SQL` → a detail row with `USING INDEX idx_events_event_time`; no row with `USING INTEGER PRIMARY KEY`. RED before row 1 (the rowid walk is the current plan — quote the red's detail text in the return).
- T2 `…_semanticsUnchanged`: 1,000 rows with `event_time` spread over an hour; a 5-minute window read with `afterPosition` at the window's midpoint and `maxCount = 7` returns exactly the 7 rows after that position inside `[from, to)`, ascending — the same list the pre-change SQL returns (compute the expected list from the inserted data, not from the old query).
- T3 `…_failsLoudlyWithoutTheIndex`: on a connection where the index is dropped, the query throws (SQLite's `no such index`) — the loud failure is the point of `INDEXED BY`.
- T4 `HomeSynapseCoreStartupFailureTest.automationCompanionFatal_recommendsTheFileAndTheAct`: boot with a malformed `automations.ids.yaml` in the config dir (the AUTO-ID-1 T8 shape — reuse its fixture if the test tree has one; `git grep -n 'ids.yaml' lifecycle/lifecycle/src/test`); the `StartupFailureReport`'s recommendation names `automations.ids.yaml` and the operator's act; the exit code unchanged (99 by the ExitCode contract as AUTO-ID-1 left it).
- The measurement, read not gated: run `MeasureReadPathIT` once with `HOMESYNAPSE_MEASURE2B_ROWS=10000,100000,500000` (the seeding takes minutes at 500k — the IT's own cap applies) and quote the three MEASURE2B lines' `q1_ms` in the return beside F-2's baseline (1.8 ms at 10k → 90.5 ms at 500k). Pre-registered by the hub: q1 at 500k ≤ 3 × q1 at 10k; q2–q6 unchanged within noise. A miss is a finding, not a failure of the unit — the plan test is the gate.

## §8 MODULE_CONTEXT.md — the two rows §3 row 5 names. Nothing else.

## §9 What to watch out for
> **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches production code in every non-whitelisted module and only `app`'s tests — this module's TEST code is a convention your review alone enforces.

- `INDEXED BY` binds to the index NAME; the migration's name is the contract (`V001…:61`). Do not add a migration.
- The `ORDER BY global_position … LIMIT` after an index range means a sort of the window's rows — the window is small by construction (`HINT_LEAD/HINT_LAG`); say the two constants' values in the return.
- The startup-failure path tears down and rethrows (`:466–:476`); T4 asserts the REPORT, not the log line.
- MEASURE-2b's seeding at 500k is minutes; run it once, in the background, and do not block the tests on it.

## §10 Coder pushback welcome
If `EXPLAIN QUERY PLAN` shows the shipped driver already choosing the index for a narrow window and the walk only for a wide one — show both plans; the hub then decides whether `INDEXED BY` still lands (the row's premise is F-2's measurement, which used the default clock step, a narrow window). If the subsystem string for the automation phase is not a single literal, say what it is.

## §11 Out of scope
Any change to `triggeredInWindow`'s paging or `SCAN_BATCH`; other queries' plans (a finding if seen); the `StartupFailureReport` record's shape; `app/`; anything under `web-ui/`.

## §12 Success criterion (binary)
`./gradlew check` green; T1–T4 green and T1/T4 red-first; the three MEASURE2B lines quoted; the return ≤ 12,000 B at its path with §0 first; porcelain lists exactly §3's files (row 2 new).

## §13 Work unit completion (WUCP Phase 1)
The return after §0: §1 what changed (per file, line spans) · §2 the tests (names; red text; green) · §3 deviations · §4 the survey as found · §5 findings for the register · §6 the coder-handoff entry text · §7 instrument limits.

## §14 The dispatch line (Nick pastes into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`, on `main` at `d2cddb1`)
```
Invoke the nexsys-coder skill. Execute nexsys-hivemind/context/instructions/2026-09-21_coder-lane_IR40-IR44_time-range-plan-on-the-index_startup-report-automation-arm_coding-instruction.md exactly: date -u first; re-verify the baseline (git log -1 --oneline = d2cddb1); read §2's set by the ranges given (MODULE_CONTEXT.md files by grep only, never whole); write §3's rows and nothing else; tests first (§7); ./gradlew check green; leave the tree at porcelain, uncommitted; write the return to nexsys-hivemind/context/audits/<today's CT date>_IR40-IR44_return.md (≤ 12,000 B, §0 first) and end your last message with exactly: RETURNED <that path> <bytes>.
```
Nick says back `IR40: RETURNED <path> <bytes>`.

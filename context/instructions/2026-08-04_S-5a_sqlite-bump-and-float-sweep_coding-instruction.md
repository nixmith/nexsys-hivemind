<!--
file: context/instructions/2026-08-04_S-5a_sqlite-bump-and-float-sweep_coding-instruction.md
purpose: S-5a — the sqlite-jdbc WAL-corruption-class bump (3.51.2.0 → 3.51.3.0, the named fixed release) + the float-serialisation exposure sweep (the R-1 §6.6/B-1 rider), split from STATE-DIALECT P2 per the milestone-sizing smell test so the safety-critical dependency fix lands before Aug-8 without waiting on the dialect work.
audience: the Coder (core lane, host-CC desk)
status: ISSUE-READY. baseline: core `60d3ab5` CLEAN (hub-verified 2026-08-04; the DEPLOYED build). Return → `context/audits/2026-08-04_S-5a_return.md`. The lane commits NOTHING.
-->

# Coding Task: S-5a — sqlite-jdbc 3.51.3.0 + the float-serialisation exposure sweep

**Subsystem:** Persistence (build catalog + a read-only exposure survey)
**Design Doc:** Doc 04 Persistence Layer (Locked) — no contract changes here
**Phase:** 3-Implementation (dependency maintenance + survey)
**Task Brief Reference:** S-5 (the freeze-runway small-fix stack), first item; premise host-validated at the R-intake adjudication B-1 and re-confirmed on the deployed classpath (`sqlite-jdbc-3.51.2.0.jar` visible in the Aug-3 and Aug-4 gate pgreps)

## What This Implements

`gradle/libs.versions.toml:17` pins `sqlite-jdbc = "3.51.2.0"` — the LAST UNFIXED version of the 2010→2026 WAL corruption bug (fixed in engine 3.51.3 / driver **3.51.3.0**, 2026-03-16; the R-1 research finding, host-validated 2026-07-31). Our exposure profile is exactly the bug's: WAL mode + a pooled Java writer with ≥2 connections on one file (`DatabaseExecutor: readThreads=2` + the write path). This WU lands the one-line bump to the NAMED fixed release and closes the rider that travels with it: a disposition survey proving the codebase has ZERO dependence on SQLite's float-to-text rendering (the engine 3.53.0 15→17-significant-digit change — not in this bump, but the survey is the cheap insurance that makes every FUTURE bump safe by record).

## Files to Read Before Starting (minimum read set)

| File | Why |
|---|---|
| `gradle/libs.versions.toml` | The single edit site (:17) |
| `core/persistence/MODULE_CONTEXT.md` | Gotchas + contracts for the module whose driver changes (no version-string pins exist there — hub-verified — but the WAL/write-coordinator gotchas frame the regression surface) |
| `core/persistence/src/main/resources/db/migration/events/` (all 5 migrations) | The REAL-column census input for the sweep (§Survey) |
| `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` + `DatabaseExecutor.java` | The PRAGMA/WAL configuration and connection topology the bump must not disturb |

## STOP-on-Mismatch Gates

| Check | Expected |
|---|---|
| `gradle/libs.versions.toml:17` | exactly `sqlite-jdbc        = "3.51.2.0"` (alignment-spaces included) |
| core porcelain | CLEAN at `60d3ab5` before any edit |
| Version-string consumers | repo-wide grep for `3.51.2` finds ONLY the toml line + `docs/archive/project-state-reports/…2026-04-08.md` (an ARCHIVE snapshot — never updated; disposition: leave byte-untouched). Any OTHER hit is a STOP-and-report |

## Files to Create or Modify

| Action | File | Description |
|---|---|---|
| MODIFY | `gradle/libs.versions.toml` | `:17` → `sqlite-jdbc        = "3.51.3.0"` (the named fixed release — EXACTLY this version; if Gradle cannot resolve the artifact, STOP and report — never hunt versions) |

Zero Java source changes are expected. If the survey (below) finds a real exposure, it is a FINDING routed to the hub in the return — not a fix in this WU.

## P2 Consumer/Pin Survey

Version-string consumers enumerated above (toml + one immutable archive doc). No enum/registry/sealed-set/count-pin is touched; no module boundary is crossed; **ARCH-RULE-REACH: N/A** (zero source changes mandated). No module-info changes (none possible from a catalog version bump). §4c: no new tests are mandated; if you elect to touch any non-app test code anyway, the Clock-injection convention applies as PM-review-enforced (`coding-instruction-format.md` §Arch-Rule Test-Clock Reminder governs).

## The Float-Serialisation Exposure Survey (the B-1 rider — read-only, disposition table in the return)

For each class, enumerate occurrences and disposition each (`NO-EXPOSURE` with one-line reasoning, or `FINDING` with the evidence):

1. **REAL columns:** census all 5 event-store migrations for `REAL`/`FLOAT`/`DOUBLE` column types. (Expected: zero — timestamps are INTEGER micros; payloads are serialized blobs/text.)
2. **SQLite-rendered float text:** grep persistence SQL for `CAST(… AS TEXT)`, `quote(`, `printf(`, `GROUP BY`/`ORDER BY`/`=` comparisons on any float-typed expression, and any Java code reading a float column via `getString`.
3. **Hash/diff over SQLite output:** any code hashing, checksumming, or byte-comparing rows/exports where a float rendered BY SQLITE (not by Jackson) could appear.
4. **Jackson float paths (context line only):** note that payload float formatting is Jackson's, independent of the driver — one sentence in the return so the boundary is on the record.

**Expected verdict: ZERO exposure — filed so every future driver/engine bump inherits the survey instead of re-deriving it.**

## Verification Gates

1. Shift-left (P5): `./gradlew :core:persistence:compileJava` targeted, then the module's tests targeted — GREEN.
2. **Full `./gradlew check` — this WU's CC-lane grant** (the WU-AVAIL-SEED precedent): run it in-session against the final tree; quote the task count + BUILD SUCCESSFUL in the return. CI on the pushed commit remains the gate of record (D1) after the hub's commit order.
3. Dependency-truth check: `./gradlew :core:persistence:dependencies --configuration runtimeClasspath | grep sqlite` (or the equivalent) shows `3.51.3.0` and no residual `3.51.2.0` anywhere in the resolution.
4. Red-first disclosure per #18: a version bump has no red-able fixture; the existing 156-task suite IS the preservation gate — predict green-by-construction, disclosed.

## What to Watch Out For

- The bump is DRIVER+ENGINE (the driver bundles its engine). Watch the check run for any PRAGMA/journal-mode warnings that differ from baseline — a changed default would surface here first; quote any delta verbatim in the return rather than adapting to it.
- Deployed-runtime note (context, not action): the Pi runs the OLD jar until the next installDist deploy — the H3 trip (Aug-8/9) carries it; the return should state this so nobody reads the desk green as a deployed fix.
- Do NOT touch `jackson`, `snakeyaml`, or any sibling catalog line — one version, one WU.

## Coder Pushback Welcome

Standard: evidence-based pushback outranks the instruction; STOP-and-report beats silent adaptation.

## Out of Scope

STATE-DIALECT P2 (S-5b, authors separately) · FE-LIVE-V112 (f)/(g) (FE lane) · any schema/migration change · any float-exposure FIX (finding-only this WU) · the Pi deploy (H3).

## Success Criterion

DONE when: the toml line reads `3.51.3.0`; targeted + full check GREEN in-session with outputs quoted; the resolution check shows no 3.51.2.0 residue; the survey's disposition table is complete with the expected zero-exposure verdict (or honest FINDINGs); census **exactly 1 M** (`gradle/libs.versions.toml`); WUCP Phase 1 complete; return filed.

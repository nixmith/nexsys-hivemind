<!--
file: context/audits/2026-09-12_FIX-2b-ii-i_return.md
purpose: Coder return for FIX-2b-ii part (i) — the run hand-off instrument (lines A–D, kind E, the hero IT's per-loop assertion, the soak census line); §0 card first. Part (ii) untouched (gated).
audience: the hub (audit) · Nick (commits)
state-type: lane return
status: DELIVERED 2026-09-12 CT — REPO-COMPLETE, LIVE-VERIFICATION PENDING (CI on the push = the gate of record; the first bus-soak sample after the landing = §7's criterion)
-->

# FIX-2b-ii (i) return — the run hand-off named (2026-09-12 CT)

## §0 The card

**Verdict: DONE (repo-complete) — 8 = 8 M + 0 A; 0 [REVIEW] + 7 [INFO] + 1 observation; nothing STOP-grade. P1–P2 HELD (P2's `check` half owed to CI — Deferred Build Gate).** Baseline `ff1a6e1` at `git log -1 --oneline`, porcelain EMPTY at launch (18:11Z). Instruction read whole; part (ii) / §7 not touched. STOP gates: (1) HEAD = `ff1a6e1` · (2) the two `switch (kind)` hits are a test-local explanation kind (`NonFiringExplanationServiceTest:565`, `StandardExplanationServiceTest:541`); no switch over `DeliveryAnomaly.Kind` anywhere · (3) `grep -n logback core/automation/build.gradle.kts` = 0; `lifecycle/lifecycle/build.gradle.kts:79` = `testImplementation(libs.logback.classic)` · (4) five `@Test`s at `:90 :166 :225 :271 :320`; the confirm test = `heroLoop_motionToHonestConfirmed` (`:94`). Every §1/§2 line number matched the tree. Not a duplicate dispatch (no return on disk; tree clean). Preflight: 1–5, 7 PASS; 6 = the loaded plugin copy `diff -rq`-equal to `nexsys-hivemind/coder` (no `~/.claude/skills/nexsys-coder` on this desk); 12 STALE — hub hygiene (non-today live `status:`: RS3-WMARKET-2 · H8a · R-4c · P-1 · EXPLAIN-114a). 18:11Z launch → 18:3xZ filing; CT = UTC−5 → **2026-09-12**.

**Census — CORE (`git --no-optional-locks status --porcelain`): EXACTLY 8 = 8 M + 0 A + 0 D; ZERO staged; ZERO commits by the lane; `git diff --stat -- '*module-info.java'` = EMPTY.** `git diff --numstat`: `StandardRunManager.java` +42/−1 · `StandardActionExecutor.java` +5/−0 · `DeliveryAnomaly.java` +15/−4 · `InProcessEventBus.java` +10/−0 · `HeroLoopHardwareFreeIT.java` +67/−0 · `BusSoakIT.java` +14/−21 · `BusPositionCensusIT.java` +100/−9 · `core/automation/MODULE_CONTEXT.md` +2/−0. Added lines: `synchronized` 0 · `Instant.now|currentTimeMillis|nanoTime|systemUTC` 0 · `System.out` in `src/main` 0; every file LF. HIVEMIND: 1 A (this file) + 2 M (`coder-handoff.md` prepended, `coder-lessons.md` appended).

**P1–P2, adjudicated first (the red-first table):**
| # | Predicted | Observed |
|---|---|---|
| P1 | the row-5 assertions red at HEAD production, zero matching lines | **HELD** — `git grep -c 'automation.run_handoff' -- core` = 0 at HEAD; rows 5–7 written first, then `./gradlew :lifecycle:lifecycle:test --tests '*HeroLoopHardwareFreeIT*' --rerun --offline` at 18:20:52Z → `compileTestJava` EXECUTED (`-Werror` clean), **5 completed / 1 failed** at `HeroLoopHardwareFreeIT.java:183`: `[automation.run_handoff] Expected size: 1 but was: 0 in: []` (XML `failures="1"`, 18:21:06Z) |
| P2 | compile green under `-Werror`; `check` green | **HELD (compile + module gates); `check` DEFERRED** — rows 1–4 written; the same line at 18:22:42Z → `:core:event-bus:compileJava` · `:core:automation:compileJava` · `:lifecycle:lifecycle:compileTestJava` EXECUTED, **5/5** green (18:22:51Z), the four tokens in `<system-out>`. Gates 18:24:17–18:25:01Z (`--rerun` after each test task, `--offline`; every `:test` EXECUTED, result mtimes 18:24:21–18:25:00Z): `:core:automation:test` **211**/27 · `:core:event-bus:test` **230**/38 · `:lifecycle:lifecycle:test` **81**/19 (the gate shape — the two tagged ITs absent) · `:app:homesynapse-app:test` **30**/7 (the arch rules incl. `NO_DIRECT_TIME_ACCESS`) · `spotlessCheck` ×3 green. The tagged pair (`--tests '*BusSoakIT*' --tests '*BusPositionCensusIT*' --rerun -PincludeBusSoak`, 18:23:48–18:23:53Z): 2/2 green — `bus.soak: loops=20 ok=20 timed_out=0 p50_ms=26 p99_ms=35 max_ms=35 anomalies=0` · `bus.position_census_total: runs=20 subscribers=6 missed=0 unscored_missed=1`; **§7's criterion on the desk: `grep -c 'automation.run_handoff' TEST-…BusSoakIT.xml` = 20 = the loop count** (body 20 · step 20 · `run_thread_died` 0 · `NOTIFY_SKIPPED_LIVE` 0). `./gradlew check` NOT run — owed to CI on Nick's push of exactly the 8 atop `ff1a6e1`. P4 held: the hero test's capture reads exactly 1 / 1 / 1 |

**The grammar, as printed** (`run_body_entered` carries the same head + `thread=`; `run_thread_died` at ERROR with the stack; a bus-soak timeout adds `automation.handoff_census: runId= handoff= body= step0= died=` after the FIX-2b-i reading, in the stdout AND the thrown message):
```
automation.run_handoff: runId=01KDVDNA00V2E724XAG2YQ6TC9 automationId=01KDVDNA00V2E724XAG2YQ6TBN mode=admitted thread=automation-run-01KDVDNA00V2E724XAG2YQ6TBN-01KDVDNA00V2E724XAG2YQ6TC9
automation.action_step_started: runId=… automationId=… index=0 type=CommandAction
```

## §1 Deviations — 0 [REVIEW] · 7 [INFO] · 1 observation

- **[INFO] I1 — the census values are COUNTS, not `<0|1>`.** `handoffCensus` prints the number of lines for the run (`1` healthy · `0` the step that never happened · `2` the double hand-off P4 names) — identical to the instruction's reading on every value ≤ 1; keyed as row 6 says (the store's newest `automation_triggered` payload `runId`, matched as the `runId=<ulid> ` prefix).
- **[INFO] I2 — the shared static widened; the soak's two privates hoisted.** `BusPositionCensusIT.timeoutDiagnostic(core, dumpDir, captured, what, awaited)` (+`List<ILoggingEvent>`; the five call sites updated; the hero IT's private sibling untouched). `attachLineCapture()` + `homesynapseLogger()` are the census IT's statics; `BusSoakIT` imports them (its `attachAnomalyCapture`/`coreLogger` removed; the `startsWith("bus.delivery_anomaly")` filter unchanged). Test tree only.
- **[INFO] I3 — `logHandoff(run, mode, thread)`**, one private static helper for line A's four sites (one format string; `thread` is a `String`, `"none"` on the two VT-less paths, so `run.vt` is never dereferenced there).
- **[INFO] I4 — the hero IT keys on the store.** The lines are checked against the `automation_triggered` payload `runId`; `run_handoff` and `run_body_entered` are exact counts of 1 over the test's whole capture (attached before boot, the soak's precedent).
- **[INFO] I5 — one javadoc clause in `DeliveryAnomaly`** (row 3's file): the emitter contract names kind E beside `NOTIFY_NOT_VISIBLE` as publisher-thread emitted (it is — `notifyEvent`).
- **[INFO] I6 — javadoc at the changed sites:** a "Structured log tokens" paragraph on `StandardRunManager`'s class javadoc; `startRun`'s names the handler as observation-only.
- **[INFO] I7 — two MODULE_CONTEXTs untouched by the 8-file census:** `core/event-bus` (kind E — the hub's Phase 2 delta, as §2 says) and `lifecycle/lifecycle` (the `automation.handoff_census:` grammar + the parent-logger capture; one paragraph beside its FIX-2a/2b-i notes).
- **Observation O1 (for P3's census arm):** `NotifyingEventPublisher:48/:56` calls `bus.notifyEvent(P)` on the CALLER's thread after each publish, so two publishers' notifies can land out of position order; a LIVE subscriber that delivered P2 first has checkpoint ≥ P1 when P1's notify arrives → kind E, and P1 is a real miss BELOW the checkpoint. Sample #11's `first_missed=24` > `checkpoint=23` is a miss AT the head, which the guard cannot produce (23 < 24 offers) — a red repeating that shape with kind E absent is the likelier arm (§7 → REPRO-1). Not acted on.

## §2 Sweeps and limits

- **INV/LTD:** the instruction cites none by id. Standing: LTD-11 (added `synchronized` = 0) · LTD-04 (ids reach the lines as Crockford strings via `RunId`/`AutomationId.toString()` = `value.toString()` — the log boundary) · NO_DIRECT_TIME_ACCESS (0 wall-clock reads added; `app` 30/30 green) · AMD-42 §3.4.1 `SubscriberMode` verified at `SubscriberMode.java:8`; kind E's guard reads `runtime.mode()` under the `rwLock.readLock()` the loop already holds — no queue lock. Glossary: Run · Subscriber · Checkpoint are entries.
- **Zero behavior change** beside the lines and the kind: no catch widened, the guard's `continue` unchanged, the `Error` propagates through the handler exactly as before.
- **Instrument limits:** the `automation.handoff_census` path runs only on a timeout — this desk does not reproduce the class, so it is verified by reading and guarded (a gather failure prints `automation.handoff_census: unavailable: <cause>` and never hides the reading or the dump); the pair's green run exercised the widened capture and signature. Full `./gradlew check` not run in-lane (CLAUDE.md's gate is Nick's; the targeted gates stand in). `List.copyOf(appender.list)` on a live appender is the FIX-2a precedent.

## §3 WUCP Phase 1

- [x] MODULE_CONTEXT.md updated for: core/automation (one GOTCHA: the VT name form · lines A–D + their sites · the `RuntimeException`-only catch and what an `Error` leaves behind · the census grammar)
- [x] coder-handoff.md prepended (the Deferred Build Gate flag at its top)
- [x] Deferred build gate flag: **YES** — `./gradlew check` on `ff1a6e1` + the 8, owed to CI on Nick's push
- [x] coder-lessons.md appended: the leaf-vs-parent logger capture
- [x] Cross-agent note: not needed
- [x] NEXT WU named: the hub's audit → Nick's commit (exactly the 8) + push → `check` green = the gate of record → the first `bus-soak` artifact after the landing shows `automation.run_handoff` × loops in `<system-out>` (§7's criterion) → part (ii) dispatches only on a red that names its row → EXPLAIN-114a after (i)
- Timestamp: 2026-09-12 18:3x UTC (Sat 2026-09-12 ~13:3x CT)

RETURNED context/audits/2026-09-12_FIX-2b-ii-i_return.md 9978

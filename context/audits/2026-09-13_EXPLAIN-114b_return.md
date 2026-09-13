<!--
file: context/audits/2026-09-13_EXPLAIN-114b_return.md
purpose: Coder return for EXPLAIN-114b (maintainability under the v1.1.4 freeze). §0 first; the hub audits; Nick commits.
status: DELIVERED — REPO-COMPLETE, hub audit pending
-->

# EXPLAIN-114b return — maintainability under the v1.1.4 freeze (filed 2026-09-13 CT)

## §0 The card
- **Verdict: DELIVERED.** Baseline `a458a64`, porcelain empty at boot. `date -u` 2026-09-13T19:27:34Z ⇒ CT = UTC−5 = 14:27 CDT, once; filed 2026-09-13 CT. Instrument: a 24-core Windows desk, JDK 21.0.4, `--offline`; not the runner.
- **Census (lock-free porcelain): 7 = 6 M + 1 A + 0 D — the Files table exactly (P1 HELD).** `core/automation/`: M `MODULE_CONTEXT.md` · M `StandardExplanationService.java` · M `NonFiringExplanation.java` · M `StandardExplanationServiceTest.java`; `api/rest-api/`: M `MODULE_CONTEXT.md` · M `AutomationEndpointsTest.java` · **A** `NonFiringExplanations.java` (test tree). Nothing outside the seven paths; staged nothing, committed nothing.
- **P2 HELD:** `readByType(` 5 → **1**. **P3 HELD:** the gate line verbatim, green in one round 19:43:42–:47Z — automation **232** · rest-api **156** (3 skip) · lifecycle `compileJava` executed · `spotlessCheck` UP-TO-DATE against its fresh pass 19:43:16Z on identical bytes. **P4:** HEAD IS `a458a64`, so no cite moved; three imprecise — the class javadoc is `:44–:92` (not `:70–:130`), the compact constructor's checks `:108–:112` (not `:96–:102`), the test's FIXED clock = the static imports `:7–:8` + `setUp` `:76` (not `:39–:60`); all others exact.
- **§12:** (1) rest-api 156/156 (3 skip) unchanged; the rest-api test-tree diff = `AutomationEndpointsTest` (+25/−20) + the new fixture — rows 4 and 5 only. (2) the `-U0 … grep -E '^[-+]\s*(assert|then|verify)'` count = **11 with row 3's hunk** (T1–T3's own `+` lines), **0 without**. (3) `readByType(` **1** · `public NonFiringExplanation(` **0**.
- **DP-1:** `InMemoryEventStore.readByType` honors `maxCount` as read (`:203–:216`: `maxCount` matches collected, `hasMore = totalMatching > maxCount`) — T1/T2 seed 501 same-type markers and the walk pages twice. A read-through `CountingEventStore` (test-local, no clock) counts `readByType` per type and records the `maxCount` passed — T3's instrument, reused by T1/T2.
- **Tests, sorted (#18):** T1–T3 written FIRST, run at HEAD with production untouched — **green-by-construction, disclosed** (19:39:31Z; class 37 → 40, 0 failures). T4 — **red SEEN** 19:42:06Z after the deletion with the fixture in place: `compileTestJava FAILED`, exactly the 6 short-form sites `:61 :118 :138 :157 :171 :269`; the two canonical sites and the fixture compiled; migrated → green 19:43:16Z. **Deviations:** `[REVIEW]` none · `[INFO]` I1–I5 (§3).

## §1 What changed per file (order written: 3 → 1 → 4 → 2 → 5 → 6/7)
1. **`StandardExplanationService`** (1057 → 1069; +`Predicate`). `private void scanType(String eventType, Predicate<EventEnvelope> visitor)` — the ONE `readByType` site: `SCAN_BATCH` per page from 0, ascending; `true` continues, `false` stops; ends at the first `false` or `!hasMore()`; never catches. `private EventEnvelope lastMatching(String, Predicate<EventEnvelope>)` — a full walk, last match wins. A private static final `Slot` is the lambda's capture cell. Visitors: `listRuns` (the `before` filter + `cap + 1` window verbatim; `continue` → `return true`; the `hasMore` tail untouched) · `latestTerminalRun` = `lastMatching`, the four rejections `return false`, the WARN inside · `latestDisabled` = `lastMatching` on the payload's `automationId`, still called only on the `DISABLED` branch · `latestRunByAutomation` (the put) · `locateTriggered` (`return false` on the match — the `:997` early return preserved). Javadocs updated; no public signature moved.
2. **`NonFiringExplanation`** (205 → 168): the 10-, 9- and 8-arg constructors and their javadocs deleted (`:115–:156`); one javadoc paragraph names the fixture; the header and the compact constructor's five null checks byte-unchanged.
3. **`StandardExplanationServiceTest`** (985 → 1143): T1 `listRuns_pagesAcrossScanBatchBoundary` · T2 `latestDisabled_seesMarkerOnSecondPage` · T3 `explainRun_stopsAtFirstTriggeredMatch`; a private `SCAN_BATCH = 500` mirror (pinned by T3); helpers `seedDisabled` (the `NonFiringExplanationServiceTest` dialect verbatim), `seedTriggeredMarker`, a 4-arg `definition(…, boolean enabled, …)` the 3-arg delegates to; the `CountingEventStore`. Every existing test byte-unchanged.
4. **`NonFiringExplanations`** (A): `static of(automationId, automationName, enabled, verdict, lastRelevantRunId, explanation, triggerSummary, lastEvaluation)` = the canonical 13 with the five nullable tail components `null` — what the deleted conveniences delegated; `withNoCommandsIssued` · `withTriggerRef` · `withDisabledFacts(Instant, String)` · `withDefinitionKey` return copies; `build()` calls the one canonical constructor.
5. **`AutomationEndpointsTest`** (+25/−20): all 8 sites `new NonFiringExplanation(` → `NonFiringExplanations.of(…)…build()`, every literal in place — site 3 `.withNoCommandsIssued(Boolean.TRUE)`, site 5 `.withTriggerRef(…)`, site 6 (T14) `.withDisabledFacts(Instant.parse("…00:00:11Z"), "repeated_failure").withDefinitionKey(DEFINITION_KEY)`, site 7 (T15) `.withDefinitionKey(DEFINITION_KEY)`; no assertion or comment line touched.
6. **`core/automation/MODULE_CONTEXT.md`** (+2 lines): the `EXPLAIN-114b status` blockquote under the 114a note (now `:31`): SD-1's contract, SD-2's one constructor + the fixture, T1–T4 as the guard, "wire byte-identical", 229 → 232.
7. **`api/rest-api/MODULE_CONTEXT.md`** (+4/−2): the `:320` cell now reads "a bare or acknowledged `DISPATCHED` (no classifying event; a superseded one carries the superseding result's instant — R3, `5f918c7`)" (the flagged phrase 1 → 0); one `EXPLAIN-114b` paragraph after the 114a Tests line names `NonFiringExplanations` as the fixture of record.

## §2 Gates, freshness, sweeps
- **Runs (UTC, `--offline`):** R0 19:39:21–:31 the class alone on HEAD's service → 40/40. R1 19:41:07–:10 `:core:automation:test` on the helper → **232**/0 (`compileJava` executed, `-Werror` clean). R2 19:42:03–:06 `:api:rest-api:compileTestJava` after the deletion → **FAILED, 6 errors** (T4). R3 19:43:13–:16 `compileTestJava spotlessCheck` after the migration → green. **R4 19:43:42–:47 the gate line verbatim** `./gradlew :core:automation:test :api:rest-api:test :lifecycle:lifecycle:compileJava spotlessCheck --offline` → green, 5 executed: automation XML rewritten 19:43:45Z (232/0/0/0), rest-api XML 19:43:46Z (156/3 skip/0/0), `HomeSynapseCore.class` 19:43:47Z.
- **Deferred Build Gate: YES** — `./gradlew check` (ArchUnit in `:app`) owed to CI on Nick's push; no rule's reach changes.
- **Preflight:** `CODER FRESHNESS PREFLIGHT — 2026-09-13 19:3x UTC — PASS (all 7 + Check 12)`. Check 1/2: the instruction + v73 b2 = the plan of record; snapshot `a458a64` = HEAD. Check 6: `nexsys-hivemind/coder` == the loaded skill copy; no `~/.claude/skills` mirror on this desk. Check 12: H8a (the spine's running lane) + today's two; one LIVE prompt; `weeks/` 0.
- **Sweeps:** INV-SA-03 — reads only · `NO_DIRECT_TIME_ACCESS` `ArchRules:98` — no clock read added · diff-only grep `Instant.now|systemUTC|currentTimeMillis|nanoTime|synchronized|System.out|Thread.sleep|TODO` = 0 · SD-3: `module-info` ×2 unchanged · `git grep -c 'new NonFiringExplanation('` = 8 (service) + 1 (the fixture's `build()`); `AutomationEndpointsTest` 0.

## §3 Pushback / observations
- **`[REVIEW]` none** — executed as written.
- **I1 `[INFO]` — the `with…` style for row 4:** one 8-arg `of` + four single-fact withers + `build()`, so a 114c component is a field and a wither in the fixture, never a constructor on the record; sites 6/7 (canonical at HEAD) migrated too, per row 5's "the 8 sites".
- **I2 — the capture cell:** SD-1's `void scanType` kept exactly; `lastMatching`/`locateTriggered` write their result through a private static final `Slot` rather than a one-element array.
- **I3 — one assertion each beyond §7's letter:** T1/T2 also assert the page count (`reads(type) == 2`); T3 pins `lastMaxCount() == SCAN_BATCH`, binding the test-local 500 to the production constant.
- **I4 —** the existing 3-arg `definition(…)` now delegates to the new 4-arg `enabled` form (same slug and trigger; its one caller unchanged).
- **I5 — T4's order:** fixture (A) → deletion → red → migration → green, so the red is the deletion's alone; the dispatch line's order would have shown no red.
- **Observation:** the 114a Tests sentence in `api/rest-api/MODULE_CONTEXT.md` ("the 8-arg and 5-arg conveniences keep the older fixtures compiling") is now historical for the `NonFiringExplanation` half; left as the dated record (§8(b) named one phrase and one line). `RunExplanation`/`AutomationSummary` conveniences untouched.
- **Next WU:** 114c — the v1.1.5 additive keys (`parentRunId`, condition text, the by-id read, `forDuration` `firingValue`), after the freeze note and HERO-1c's needs; the hub authors it. DISABLED-2 stays on the formal path (§11).

## §4 WUCP Phase 1: Coder Closeout
- [x] MODULE_CONTEXT.md updated for: core/automation (the 114b status blockquote), api/rest-api (the R3 cell + the fixture paragraph)
- [ ] coder-handoff.md — not by this lane (instruction §0: the hub files the entry)
- [x] Deferred build gate flag: YES (`./gradlew check` on the landed SHA owed to CI)
- [x] coder-lessons.md appended: No new pattern
- [x] Cross-agent note posted: Not needed (channel retired)
- Files 7 = 6 M + 1 A (§0) · gates §2 · instruments and DP-1 §0 · deviations §3 · next WU 114c (§3)
- Timestamp: 2026-09-13 19:50 UTC

RETURNED nexsys-hivemind/context/audits/2026-09-13_EXPLAIN-114b_return.md 9978

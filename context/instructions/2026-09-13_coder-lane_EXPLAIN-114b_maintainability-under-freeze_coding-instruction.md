<!--
file: context/instructions/2026-09-13_coder-lane_EXPLAIN-114b_maintainability-under-freeze_coding-instruction.md
purpose: The coding instruction for EXPLAIN-114b — the maintainability landing under the FROZEN v1.1.4 read-API: one paging loop replaces five copies of the type-index scan in StandardExplanationService; NonFiringExplanation keeps one constructor and the rest-api tests get a fixture; the two MODULE_CONTEXT phrases the 114a audit left for the hub. Wire byte-identical; no key, verdict, nesting or rendering changes.
audience: the Coder lane (host-side Claude Code in homesynapse-core, the nexsys-coder skill) · the hub (the intake) · Nick (§14 is his paste)
state-type: coding instruction (Director mode; the Files table governs)
status: EXECUTED — returned 2026-09-13 19:53Z (`context/audits/2026-09-13_EXPLAIN-114b_return.md`, 9,978 B; 7 = 6 M + 1 A), audited ACCEPT at v73 beat 3 (`context/audits/2026-09-13_v73-b3_EXPLAIN-114b_intake_two-layer-audit.md`), landed core `fed99e8` by Nick's hands, CI green (all checks; the closure counter 2/20) — banked v73 beat 4 (Sun 2026-09-13 ~15:5x CT; instrument 2026-09-13T20:57:14Z). Findings IR-1..IR-3 in `context/planning/improvement-register.md`; 114c's docket in the audit §5. Was: DISPATCH-READY — authored v73 beat 2.
-->

# EXPLAIN-114b — the maintainability landing under the v1.1.4 freeze

## §0 The lane contract (read first; every line binds)
- `date -u` first; state your instrument limit; CT = UTC−5, derived once.
- **Return path:** `nexsys-hivemind/context/audits/<CT-filing-date>_EXPLAIN-114b_return.md`, one file. §0 card first (≤2.5 KB: the census `N = a M + b A` with exact paths · the four predictions adjudicated · the three instruments in §12 with their readings · DP-1 as you took it) · §1 what changed per file · §2 the gates run with counts · §3 pushback and observations · §4 the WUCP Phase-1 checklist. **Cap ≤10 KB** (3 KB + 1 KB per Files-table row) — a ceiling, not a target; the §0 card is what the hub reads first; a shorter return with the same receipts is a better return. Your last line, in the file and printed: `RETURNED <path> <bytes>`.
- **Baseline:** `git log -1 --format=%h` is `a458a64` and `git status --porcelain` is empty; anything else: stop and report. Every line number in this file was read at `a458a64` (`sed -n`, `grep -n` — the commands are beside the claims); if a cite has moved, re-derive it at your HEAD and file the corrected line (P4).
- **Write-set:** the seven paths of the §3 Files table only. Never `module-info.java` (§4 pins zero change and says why), never `build.gradle.kts`, never `web-ui/**`, never any payload or event type, never `context/decisions/*`. You commit nothing and stage nothing; Nick lands the tree with a card after the hub's audit. Your §4 carries the checklist; the hub files the coder-handoff entry.
- **Build discipline:** the gate line, verbatim: `./gradlew :core:automation:test :api:rest-api:test :lifecycle:lifecycle:compileJava spotlessCheck --offline` — green in one round is the target; `./gradlew check` runs as CI on Nick's push and is the gate of record. Scripts over ~15 lines are written with the Write tool and run by path — no long heredocs.
- **The freeze governs the whole shape:** v1.1.4 is FROZEN (`5f918c7`). This WU changes NO byte on the wire: no key, no order, no casing, no nesting, no rendering, no verdict, no sentence. §12's instruments make that a measurement, not a promise.
- **Tests first, honestly sorted (format law #18):** this WU has **no red-at-HEAD row** — it preserves behavior. Its guard is three preservation fixtures (T1–T3) written FIRST and green at HEAD, disclosed as green-by-construction; the constructor collapse is compile-guarded (T4: after the three constructors are deleted, `:api:rest-api:compileTestJava` compiles only because the fixture is in place). Say so per test in your §0.
- **Predictions, pre-registered; adjudicate them first in your §0:** P1 — the census is the Files table (§3) exactly, or the deviation is declared with its cause. P2 — after the edit `grep -c 'eventStore.readByType(' StandardExplanationService.java` reads `1` (it reads `5` at `a458a64`). P3 — the four Gradle tasks are green in one round; the automation count is 229 + the T1–T3 rows, rest-api stays 156 (3 skip). P4 — at least one line cite in this instruction has moved at your HEAD, or you state that none did.
- **One scope decision you take and declare — DP-1, the page-boundary seed:** `InMemoryEventStore.readByType` honors `maxCount` (`core/event-model/src/testFixtures/java/com/homesynapse/event/test/InMemoryEventStore.java:192–:204` — `validatePagination`, then a matching loop; read it). Default: T1/T2 seed `SCAN_BATCH + 1` (501) same-type markers so the scan pages twice. If you find the fixture does NOT page as read, say so and use a small paging decorator over the store in the test — declared, not silent.

## §1 What this implements
Two maintainability changes the 114a audit named (§4 growth points 1 and 2) and two MODULE_CONTEXT phrases it left for the hub, inside the frozen v1.1.4 contract: (a) **one type-index scan** — `StandardExplanationService` pages the event store's type index in five hand-copied loops (`listRuns` `:136`–`:165`, `latestTerminalRun` `:424`–`:450`, `latestDisabled` `:464`–`:479`, `latestRunByAutomation` `:490`–`:508`, `locateTriggered` `:991`–`:1005`; `grep -n 'eventStore.readByType(' … = 5 hits`); after this WU exactly one private helper pages and the five callers are visitors; (b) **one constructor** — `NonFiringExplanation` (a 13-component record, `:83`) carries three convenience constructors (10-, 9- and 8-arg at `:122`, `:136`, `:150`; `grep -c 'public NonFiringExplanation(' = 3`) used ONLY by `AutomationEndpointsTest` (8 sites: `:61 :118 :138 :157 :171 :194 :216 :269`; `git grep -n 'new NonFiringExplanation(' -- '*/src/main/*'` shows the 8 production sites all use the canonical 13-arg form: `StandardExplanationService:267 :278 :309 :318 :332 :367 :383 :391`); after this WU the record has its canonical constructor only and the test sites build through a rest-api test fixture; (c) the `settledAt` "JSON null when" cell in `api/rest-api/MODULE_CONTEXT.md:320` corrected to the R3 rule; (d) a §EXPLAIN-114b paragraph in `core/automation/MODULE_CONTEXT.md`.

## §2 Files to read before starting (minimum read set — mandatory)
- `core/automation/src/main/java/com/homesynapse/automation/StandardExplanationService.java` — the five scan regions named in §1, `SCAN_BATCH` (`:98`), `automationOf` (`:1030`), the class javadoc `:70`–`:130`.
- `core/automation/src/main/java/com/homesynapse/automation/NonFiringExplanation.java` — whole (205 lines): the record, the compact constructor's null checks (`:96`–`:102`), the three convenience constructors, `LastEvaluationView` (`:166`).
- `core/event-model/src/main/java/com/homesynapse/event/EventStore.java:113` (`EventPage readByType(String eventType, long afterPosition, int maxCount)`) and `EventPage.java:34`–`:42` (`events`, `nextPosition`, `hasMore`).
- `core/event-model/src/testFixtures/java/com/homesynapse/event/test/InMemoryEventStore.java:192`–`:230` — `readByType`'s paging (DP-1).
- `core/automation/src/test/java/com/homesynapse/automation/StandardExplanationServiceTest.java` — the seeding helpers (`seedRun`, `seedRunWithResult`; the FIXED clock at `:39`–`:60`) so T1–T3 reuse them; `NonFiringExplanationServiceTest.java` — read only its fixture section to keep dialects identical.
- `api/rest-api/src/test/java/com/homesynapse/api/rest/AutomationEndpointsTest.java` — the 8 constructor sites and what each varies (verdict, `lastEvaluation`, `noCommandsIssued`, `triggerRef`, the disabled pair, `definitionKey`).
- `core/automation/MODULE_CONTEXT.md` — the EXPLAIN-114a status note (`:29`) and the v1.1.4 GOTCHA (`:351`); `api/rest-api/MODULE_CONTEXT.md:300`–`:330` — the B3 table row you correct.

## §3 Files to create or modify (the Files table governs)
| # | Path | A/M | What |
|---|---|---|---|
| 1 | `core/automation/src/main/java/com/homesynapse/automation/StandardExplanationService.java` | M | ONE private paging helper (§4); the five loops become visitors; no public signature changes; the class javadoc's scan sentence updated |
| 2 | `core/automation/src/main/java/com/homesynapse/automation/NonFiringExplanation.java` | M | the three convenience constructors deleted (`:122`–`:160`); the record javadoc says "one constructor; tests build through `NonFiringExplanations` in rest-api's test tree" |
| 3 | `core/automation/src/test/java/com/homesynapse/automation/StandardExplanationServiceTest.java` | M | T1–T3 (§7), green at HEAD, written first |
| 4 | `api/rest-api/src/test/java/com/homesynapse/api/rest/NonFiringExplanations.java` | A | the test fixture: one static factory with the canonical 13 args defaulted, plus the named variants the 8 sites need (a `with…` style or overloads — your call, declared) |
| 5 | `api/rest-api/src/test/java/com/homesynapse/api/rest/AutomationEndpointsTest.java` | M | the 8 sites build through the fixture; **no assertion line changes** (§12 instrument 2) |
| 6 | `core/automation/MODULE_CONTEXT.md` | M | §8 (a) |
| 7 | `api/rest-api/MODULE_CONTEXT.md` | M | §8 (b) |
**Census claim: 7 = 6 M + 1 A.** A second new test class for T1–T3 is a declared deviation (8 = 6 M + 2 A), not a fault — say why in §3 of the return.

## §4 Technical specification
### Settled decisions (not open questions)
- **SD-1 — the helper's contract.** `private void scanType(String eventType, Predicate<EventEnvelope> visitor)` (name your own if the tree suggests better; declare it): visits every retained envelope of `eventType` in ascending global position, `SCAN_BATCH` per page, starting at position 0; the visitor returns `true` to continue and `false` to stop; the loop ends at the first `false` or when `page.hasMore()` is false. `listRuns` keeps its sliding window as the visitor's body (the `before` cursor filter stays in the visitor); `latestTerminalRun` and `latestDisabled` keep "last match wins" (always continue); `latestRunByAutomation` keeps its map put; `locateTriggered` returns `false` on its match (HEAD already returns early at `:997` — the early stop is preserved, not added). A thin `lastMatching(String eventType, Predicate<EventEnvelope> match)` over `scanType` for the two "latest" walks is allowed; two helpers at most, ONE `readByType` call site.
- **SD-2 — the constructor collapse is a test fixture, not a builder.** A builder is production surface for test convenience; the record keeps its canonical constructor and compact null checks byte-unchanged. The fixture `NonFiringExplanations` (test tree of rest-api, the only module that used the short forms) exposes defaults that reproduce EXACTLY the values the 8 sites passed today (read each site; a default that differs from what a site passed is a silent assertion change — §12 instrument 2 catches it).
- **SD-3 — zero `module-info.java` change (format law #14 walked):** no new package, no new export, no new `requires` — the fixture lives in an existing test package; `java.util.function.Predicate` is in `java.base`. The two files, verbatim at `a458a64`, so you can see the pin is honest:

`core/automation/src/main/java/module-info.java`:
```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * Automation engine module: trigger-condition-action rules, cascade governor,
 * command dispatch, and pending command tracking.
 *
 * <p>This module defines the public API contracts for the HomeSynapse automation
 * subsystem. It exports sealed type hierarchies (triggers, conditions, actions,
 * selectors), data records (automation definitions, run contexts, pending commands),
 * and service interfaces consumed by the REST API, WebSocket API, Observability,
 * and Lifecycle modules.</p>
 */
module com.homesynapse.automation {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;

    // M4.0b-4a: PendingCommand's javadoc references com.homesynapse.value
    // .AttributeValue (via {@link Expectation#evaluate}); declared non-transitive
    // (value is not on automation's public API). The type is also reachable
    // transitively through `requires transitive com.homesynapse.device`; the edge
    // is declared explicitly at its use site per the relocation design note.
    requires com.homesynapse.value;

    // M7.1: the engine's automation_engine bus subscriber imports event-bus
    // (a legal core->core edge). The config edge that FIX-07 proposed re-adding
    // is NOT taken: core->config is forbidden by assertAllowedModuleDependencies
    // at EVERY scope (a stricter gate than the exported-API §authoring check).
    // The automations.yaml schema registration + definition-document load ride
    // the composition root (lifecycle/app), which may depend on both core and
    // config; the loader itself consumes an already-parsed Map (no config edge).
    //
    // AB-3: bumped plain -> transitive. The public AutomationEngineAssembly seam
    // (composition-root access to the automation_engine subscriber) returns the
    // event-bus Subscriber interface, putting it on this module's exported API.
    // The -Xlint:exports authoring rule (api <-> requires transitive) then
    // requires transitive here (lockstep: build.gradle.kts uses api(...)). The
    // concrete AutomationEngineSubscriber stays package-private; only the
    // Subscriber interface is exposed (same pattern as lifecycle's HomeSynapseCore
    // accessors returning event-bus/event/state types via requires transitive).
    requires transitive com.homesynapse.event.bus;

    // M7.1: the Phase-3 implementations (registry, evaluators, loader,
    // duration timers) log via SLF4J. Non-transitive — no SLF4J type appears
    // on the exported API (LTD-15 / DECIDE-01), mirroring state-store/persistence.
    requires org.slf4j;

    exports com.homesynapse.automation;
}
```

`api/rest-api/src/main/java/module-info.java`:
```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * REST API module — public-facing HTTP interface types for HomeSynapse.
 *
 * <p>Defines request/response records, service interfaces, pagination contracts,
 * authentication types, RFC 9457 error model, and ETag/caching contracts that
 * endpoint handlers (Phase 3) and the WebSocket API module (Block N) compile
 * against. M3.6e.1 adds the first production HTTP plumbing — the
 * {@link com.homesynapse.api.rest.RestFilters#installReadinessGate
 * RestFilters.installReadinessGate} method that registers a readiness
 * gate on {@code /api/*} traffic until the State Projection reaches
 * {@code SubscriberMode.LIVE}.</p>
 */
module com.homesynapse.api.rest {
    // M3.6e.1: ReadinessFilter consumes ReadinessSource (state-store) and
    // observes SubscriberMode (event-bus) via that source. The Javalin
    // Handler interface lives in io.javalin. SLF4J is used for DEBUG-level
    // rejection logs.
    requires transitive com.homesynapse.state;
    requires com.homesynapse.event.bus;

    // M7.5a: the run-query endpoints consume ExplanationService + RunExplanation/
    // RunSummary INTERNALLY (package-private handlers + the Object-erased
    // installRunQueryEndpoints gateway param), so this edge stays PLAIN
    // (non-transitive) — automation is not on rest-api's exported API.
    // build.gradle.kts already has implementation(project(":core:automation")).
    requires com.homesynapse.automation;

    // M7.5a: the causal-chain handler parses the raw command-parameter JSON string
    // (command_issued.parameters) into the wire `params` object. rest-api is the JSON
    // boundary (LTD-08) and already has implementation(libs.jackson.databind); used
    // only inside a package-private handler, so PLAIN requires.
    requires com.fasterxml.jackson.databind;

    requires io.javalin;
    requires org.slf4j;

    exports com.homesynapse.api.rest;
}
```

### Wire shapes after this WU
Identical to v1.1.4 (`5f918c7`) byte for byte — §12 instrument 1 (the existing shape tests, unchanged) and instrument 2 (no assertion line changed) are the proof; no table is repeated here because nothing on the wire moves.

### Event types produced or consumed — none produced; the reads of `automation_completed`, `automation_disabled`, `automation_triggered` through the type index are unchanged in type, order and count of pages (SD-1).
### Configuration parameters — none. Error handling — unchanged: a malformed payload yields null; the helper never catches.

## §5 Locked decisions and invariants that apply
INV-SA-03 (the projection is a pure function of the log — the helper reads, never stores); the v1.1.4 freeze (CG-123's pattern — additive keys only; this WU adds none); D4 (one lane per path-domain — the Java domain is yours alone); the clock law `HomeSynapseArchRules:98` (`NO_DIRECT_TIME_ACCESS`; the §9 paste-block). No locked decision is touched.

## §6 P2 consumer/pin survey (done at authoring; re-run the greps)
- `git grep -l NonFiringExplanation -- '*.java'` = 7 files, none under `lifecycle/` or `app/` (`GetNonFiringEndpoint`, `AutomationEndpointsTest`, `RunEndpointsTest`, `ExplanationService`, `NonFiringExplanation`, `StandardExplanationService`, `NonFiringExplanationServiceTest`) — the constructor deletion breaks only `AutomationEndpointsTest`, which row 5 migrates first.
- `git grep -n 'new NonFiringExplanation(' -- '*.java'` = 16 sites: 8 canonical in `StandardExplanationService`, 8 short in `AutomationEndpointsTest`; `RunEndpointsTest` names the type without constructing it.
- `grep -c 'eventStore.readByType(' StandardExplanationService.java` = 5 (the P2 baseline). No other class in `core/automation` pages a type index (`git grep -n 'readByType' -- 'core/automation/src/main/*'` = the 5 hits, one file).
- ARCH-RULE-REACH: no module or layer boundary is crossed; no new package.
- `grep -rn 'SCAN_BATCH\|501' StandardExplanationServiceTest.java NonFiringExplanationServiceTest.java` = 0 hits — no test crosses a page boundary today; T1–T2 are the first.

## §7 Test requirements (written first; sorted per format law #18)
| T | Test (class) | Sorting | What it pins |
|---|---|---|---|
| T1 | `listRuns_pagesAcrossScanBatchBoundary` (`StandardExplanationServiceTest`) | green-by-construction | 501 `automation_completed` markers for one automation; `listRuns(Optional.of(id), 0, 5)` returns the newest 5 in the existing order with `hasMore` true — the page-2 markers are seen |
| T2 | `latestDisabled_seesMarkerOnSecondPage` (same) | green-by-construction | 500 same-type markers of another automation then one `automation_disabled` for a configuration-disabled automation; `explainNonFiring` reports `DISABLED` with `disabledAt` = that marker's instant and its `reason` — the last page is scanned |
| T3 | `explainRun_stopsAtFirstTriggeredMatch` (same) | green-by-construction | a counting `EventStore` decorator: the run's `automation_triggered` on page 1 of 2 ⇒ exactly ONE `readByType(AUTOMATION_TRIGGERED, …)` call (HEAD returns early at `:997`; the helper must keep that) |
| T4 | the compile guard (no new method) | — | after row 2's deletion, `:api:rest-api:compileTestJava` compiles ONLY because row 4's fixture is in place and row 5 is migrated; run `./gradlew :api:rest-api:compileTestJava --offline` between the deletion and the migration once to SEE the red, and say so |
Existing: automation 229 (`build/test-results` at `a458a64`; re-derive) and rest-api 156 (3 skip) stay green with no assertion edited.

## §8 MODULE_CONTEXT.md update
(a) `core/automation/MODULE_CONTEXT.md`: one paragraph under the EXPLAIN-114a status note (`:29`) headed **EXPLAIN-114b (maintainability under the v1.1.4 freeze)**: the one paging helper and its visitor contract (SD-1); the fact that `NonFiringExplanation` has one constructor and where the test fixture lives (SD-2); the page-boundary tests T1–T3 as the guard; "wire byte-identical to v1.1.4". (b) `api/rest-api/MODULE_CONTEXT.md:320`: replace the phrase `DISPATCHED` (no classifying event; a superseded DISPATCHED included — flagged) with: a bare or acknowledged `DISPATCHED` (no classifying event; a superseded one carries the superseding result's instant — R3, `5f918c7`) — `grep -c 'a superseded DISPATCHED included — flagged' api/rest-api/MODULE_CONTEXT.md` = 1 at `a458a64`, 0 after; and one line naming `NonFiringExplanations` as the rest-api test fixture for the record.

## §9 What to watch out for
- The `listRuns` visitor must keep the `before` filter and the `cap + 1` window exactly (`:138`–`:161`); `hasMore` on `RunPage` derives from the extra element — do not "simplify" it.
- `latestDisabled` is read only on the `DISABLED` verdict (`:462`) — keep that laziness; the helper must not pre-scan.
- The FIXED clock: every new test injects `Clock` like the class's existing fixtures; T3's decorator must not touch time.
- The fixture's defaults: copy the 8 sites' literal values before deleting anything; a default that "looks equivalent" (e.g. `null` vs `Boolean.FALSE` for `noCommandsIssued`) changes what the endpoint serializes and instrument 2 will show a changed assertion or a red shape test.
- Spotless: the gate line includes `spotlessCheck`; run `spotlessApply` on the touched files before the final round if it complains.
> **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces.

## §10 Coder pushback welcome
If one helper cannot serve all five callers without contortion (e.g. `listRuns`'s window reads cleaner with a second, specialised helper), say so with the shape you chose — two helpers, one `readByType` site, is inside SD-1. If a fixture default cannot reproduce a site's value exactly, keep that site on the canonical 13-arg constructor and say which. If T1/T2's 501-event seed is slow under the existing helpers, seed the minimum that crosses one boundary and state the count.

## §11 Out of scope
**DISABLED-2** (R2 — an auto-disabled automation whose YAML still says enabled never reports `DISABLED`): it changes a verdict's reach on the frozen contract and the log lacks a re-enable rule (`StandardRunManager:162` "until operator re-enable" — no event, no path); the hub routes it through the formal path (an amendment proposal on the read-API contract and Doc 07 §3.7), then code — not this WU. **The v1.1.5 keys** (`parentRunId`, condition text, the by-id read, I5's `forDuration` `firingValue`) — 114c, after the freeze note and HERO-1c's needs. The 27 hand-sized `LinkedHashMap`s in the endpoints (growth point 4) — cosmetic, untouched. Any FE change. Any payload or event-type change. `web-ui/**`.

## §12 Success criterion (binary) — three instruments, read and filed in §0
1. The existing shape tests pass unchanged: `./gradlew :api:rest-api:test --offline` green, 156 (3 skip), and `git diff --stat -- 'api/rest-api/src/test/*'` names only rows 4 and 5.
2. **No assertion line changed:** `git diff -U0 -- '*Test.java' | grep -E '^[-+]\s*(assert|then|verify)' | wc -l` reads `0` (T1–T3 are additions in a new region and are excluded by construction: report the count with and without row 3's hunk).
3. **One scan:** `grep -c 'eventStore.readByType(' core/automation/src/main/java/com/homesynapse/automation/StandardExplanationService.java` reads `1`; `grep -c 'public NonFiringExplanation(' …/NonFiringExplanation.java` reads `0` (the canonical constructor is the record header; the compact constructor remains).
Done when: the census is the Files table (or the declared deviation); T1–T3 were written first and green at HEAD, disclosed; T4's red was seen and stated; the four Gradle tasks are green in one round; the three instruments read as above; `git diff --stat` shows nothing outside the seven paths; the return is on disk at the named path with its `RETURNED` line.

## §13 Work unit completion (WUCP Phase 1)
Your §4 checklist: files touched with counts; the gates and their counts; the two MODULE_CONTEXT edits; the three instruments' readings; DP-1 as taken; deviations by tag; the next WU named (114c — the v1.1.5 additive keys, after the freeze note; the hub authors it).

## §14 The dispatch line (Nick pastes into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`)
```
date -u first. Boot as the nexsys-coder skill. Baseline: `git log -1 --format=%h` is a458a64 and `git status --porcelain` is empty; stop and report otherwise. Execute nexsys-hivemind/context/instructions/2026-09-13_coder-lane_EXPLAIN-114b_maintainability-under-freeze_coding-instruction.md exactly: read its §0 contract and §2 read-set first; adjudicate P1–P4 in your §0 card; take DP-1 from the source and declare it. This WU changes no byte on the wire — it is a refactor under the v1.1.4 freeze: write T1–T3 first (green at HEAD, disclosed), then the one paging helper, then the rest-api test fixture and the 8 site migrations, then delete the three convenience constructors (see T4's red once), then the two MODULE_CONTEXT edits. Write only the seven paths of its §3 Files table; never module-info, build files, web-ui or any payload; run `./gradlew :core:automation:test :api:rest-api:test :lifecycle:lifecycle:compileJava spotlessCheck --offline`; read the three §12 instruments and file their readings; stage nothing, commit nothing. Scripts over ~15 lines go through the Write tool and run by path. Write nexsys-hivemind/context/audits/<today's CT date>_EXPLAIN-114b_return.md (≤10 KB, §0 card first) and end it, in the file and printed, with: RETURNED <path> <bytes>.
```

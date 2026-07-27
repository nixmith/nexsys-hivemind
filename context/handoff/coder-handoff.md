<!--
file: context/handoff/coder-handoff.md
purpose: Coder session continuity — current task, deferred build gate, next WU, recent closeouts.
audience: Coder, PM
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-07-27 (Coder, DASH-SERVE closeout — the DASH-SERVE DELIVERED entry prepended [newest, authoritative for current task + next WU]; core repo, working tree on `2040a66` (clean at dispatch, P0 exact), census EXACTLY 13 (12 M + 1 new fixture), all in-session gates GREEN incl. full `./gradlew check` [this WU's CC-lane grant: the targeted loop + one full check + the mandated Node-free grep, quoted] + in-session mutation verification M1–M3 with named kills + cmp-proven restores; hub two-layer audit precedes any commit; ZERO [REVIEW] — seven [INFO]s ride the entry; next WU = B2 [bench lane, hub-authored; core QUIET until the M14 WUs].) Prior: 2026-07-27 (v39 hub, beat 1 — the WU-DASH-SERVE DISPATCH entry prepended [newest, authoritative for current task + next WU; it supersedes the SKIP-VIS entry's next-WU=B2 pointer per the v38 beat-8 ratified sequencing: DASH-SERVE first (core lane, the idle Coder), B2 second (bench lane, hub-authored)]. Launch preconditions: Nick's skills-mirror sync (Check 9 mismatch recorded at the v39 launch) + the beat-1 hivemind push. Working tree baseline core `2040a66` clean.) Prior: 2026-07-26 (Coder, SKIP-VIS closeout — the SKIP-VIS DELIVERED entry prepended [newest, authoritative for current task + next WU]; core repo, working tree on `4bc1258` (clean at dispatch, P0 exact), all in-session gates GREEN incl. full `./gradlew check` ×2 [this WU's CC-lane grant: the targeted loop + one full check; the second check is the gate of record against the final tree] + in-session mutation verification M1–M3 with cmp-proven restores + a 4-lens adversarial review fleet (zero code defects); hub two-layer audit precedes any commit; ZERO [REVIEW] — seven [INFO]s ride the entry). Prior: 2026-07-22 (Coder, CMD-API closeout — the CMD-API DELIVERED entry prepended [newest, authoritative for current task + next WU]; core repo, working tree on `355a711` (clean at dispatch), all in-session gates GREEN incl. full `./gradlew check` [this WU's CC-lane grant] + in-session mutation verification M1–M3 with cmp-proven restores; hub two-layer audit precedes any commit; ONE [REVIEW] rides it — the app-tree ArchUnit Rule 9 scoping). Prior: 2026-07-22 CMD-API (kept below). The LEARN-PERSIST→M9.5-DUR-era entries + chain ROTATED 2026-07-26 (v38 hub, beat 5) → archive/coder-handoff-entries-rotated-2026-07-26.md; git history.
-->

# Coder Session Handoff

---

## WU-DASH-SERVE — the dashboard serve path (package · mount · the ruled (A) auth exemption; core repo) — DELIVERED (2026-07-27)

> **DEFERRED GATE (hub, then Nick):** the hub's two-layer audit precedes ANY commit order (this entry + the completion report + the cross-agent note are the audit inputs). Deferred Build Gate: **NO** — the full `./gradlew check` RAN in-session, GREEN. Working tree: core **`2040a66`** (clean at dispatch, P0 exact) + EXACTLY 13 porcelain entries = the instruction's census (12 M + 1 new fixture `lifecycle/lifecycle/src/test/resources/dashboard/index.html`). Pre-verification: ALL pins P0–P15 verified against the working tree pre-code (P14 verified against the actual Javalin 6.7.0 jar via javap: `cfg.staticFiles.add(Consumer<StaticFileConfig>)` with public `hostedPath`/`directory`/`location` fields · `cfg.spaRoot.addFile(String,String,Location)` · `Location.CLASSPATH` · `ctx.method()` → `HandlerType`; zero mismatches, zero pushback needed).
> ```
> ./gradlew :api:rest-api:test :lifecycle:lifecycle:test :app:homesynapse-app:test --rerun
>                                        # BASELINE at HEAD pre-edit (forced-fresh, 68/68 tasks
>                                        #   executed): rest-api 104/0/0 · lifecycle 56/0/0 ·
>                                        #   app 19/0/0 (the SKIP-VIS "104" record matched — no drift)
> red-first (tests written FIRST)        # rest-api compileTestJava FAILED: 7 missing-symbol sites on
>                                        #   isPublicShellRequest = all 3 new unit legs red-by-compile
>                                        #   (helper absent — disclosed as such); lifecycle 14 tests:
>                                        #   rootRedirects RED (401 where 302 expected) ·
>                                        #   shellServes RED (401 where 200 expected) ·
>                                        #   writeAndDataRoutesStayGuarded GREEN-BY-CONSTRUCTION
>                                        #   (disclosed [INFO]: it is the preservation fixture — its
>                                        #   three asserts ARE the HEAD-preserved behaviors, incl. the
>                                        #   encoded traversal already 400 at HEAD, which also proved
>                                        #   the %2e%2e probe reaches isPathSafe on the wire)
> green ×2 (per-task --rerun, executed-state verified)
>                                        # rest-api 107/0/0 (6 @Test in RestFiltersAuthTest) ·
>                                        #   lifecycle 59/0/0 (14 @Test in HomeSynapseCoreTest) ·
>                                        #   app 19/0/0 — two fresh JVMs; Javalin's redirect observed
>                                        #   302 (the smoke pin's code), SPA fallback + HEAD 200 live
> mutation verification (in-session)     # M1 (+POST to the exemption): KILLED by the NAMED
>                                        #   dashboardWriteAndDataRoutesStayGuarded (POST leg 404≠401);
>                                        #   M2 (startsWith "/dash"): KILLED by the NAMED
>                                        #   isPublicShellRequest_rejectsEverythingElse
>                                        #   (the /dashboardevil row); M3 (exemption ABOVE isPathSafe):
>                                        #   KILLED by the NAMED EXACT-400 traversal row — the probe
>                                        #   SERVED under the mutant (200, expected 400): the order
>                                        #   contract is the security property. Restores cmp-verified
>                                        #   byte-identical ×3.
> ./gradlew check                        # FULL GATE GREEN — 157 actionable tasks, 91 executed
>                                        #   (run 1, the final tree). Node-free grep (steady state,
>                                        #   run 3 after clearing a git-invisible empty scaffold dir —
>                                        #   see [INFO]-6): EVERY :web-ui:dashboard: task
>                                        #   NO-SOURCE/UP-TO-DATE (compileJava NO-SOURCE ·
>                                        #   processResources NO-SOURCE · test NO-SOURCE · check
>                                        #   UP-TO-DATE = the module WAS in the graph); grep for
>                                        #   npmInstall|npmBuild|stageDashboard|jar → ZERO lines.
> ```
> **Per-DP:** DP-1 `:web-ui:dashboard` = bare-`java` resources jar, staging at `build/staged-dashboard`, npm attaches to the jar task ONLY, doLast self-assert on `dashboard/index.html`, legacy `src/main/resources/dashboard` swept by clean. DP-2 app `testRuntimeClasspath` `exclude(module = "dashboard")` (production `runtimeClasspath`/installDist untouched). DP-3 `staticFiles`+`spaRoot` CLASSPATH mount in the create lambda + `app.get("/", redirect /dashboard/)` after installAuth; install sequence otherwise untouched. DP-4 `isPublicShellRequest` classifier + the authorize() early-return BETWEEN isPathSafe and authenticate; installAuth Javadoc amended. DP-5 both install-smoke copies + setup-node@v4 '22' (byte-identical, diff-verified) + run-smoke.sh serve asserts (302 / 200, sections renumbered 6→7→8). **Deviations: ZERO [REVIEW]/[BLOCKING], seven [INFO]** (null-path guard the tests mandate; ZipFile import — Kotlin DSL shadows `java` as the extension accessor; clean sweeps the legacy staging dir; red-leg-6 green-by-construction; smoke section renumber; local removal of the git-invisible empty `src/main/resources/static` scaffold dir so the local gate matches fresh-checkout NO-SOURCE; the order-proof test also pins the hazard side — isPublicShellRequest(traversal)==true). **Next WU: B2 (bench lane — the hub authors it; core goes QUIET until the M14 WUs).** Commit staging at the hub's order: EXPLICIT paths, exactly the 13-file census, core-repo only.

---

## WU-DASH-SERVE — the dashboard serve path (package · mount · the ruled (A) auth exemption; core repo) — DISPATCH READY (2026-07-27, v39 hub beat 1)

> **Current task (the next Coder session executes this):** read `context/pre-verifications/WU-DASH-SERVE.md` (P0–P15 — verify every pin, STOP on mismatch), then execute `context/instructions/2026-07-27_DASH-SERVE_dashboard-serve-path_coding-instruction.md`. Baseline: core **`2040a66`** clean (the deployed build of record). **CC-lane grant:** `./gradlew :api:rest-api:compileJava :api:rest-api:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test :app:homesynapse-app:test` + **ONE full `check`** — plus the mandated **Node-free grep assert** on the check output (quoted in the completion report, presence AND absence lines). **NO `assemble`/`installDist`/`:web-ui:dashboard:jar` in-session** (npm is not in the grant; the packaging leg's gate of record is `install-smoke.yml` on the pushed commit). Tests FIRST (6 new: 3 unit + 3 e2e; red-first with recorded counts; M1–M3 mutation legs with named kills + cmp-proven restores). **Census EXACTLY 13** (12 M + 1 new test fixture) — anything else in porcelain is a STOP. The hub's two-layer audit precedes ANY commit; staging will be EXPLICIT paths. **Next WU after this one: B2 (bench lane — the hub authors it; core goes QUIET until the M14 WUs).**

---

## SKIP-VIS — Explanation Honesty (raw outcome carry · silent-skip verdict honesty · the triggeredAt fix; DP-4 GO; core repo) — DELIVERED (2026-07-26)

> **DEFERRED GATE (hub, then Nick):** the hub's two-layer audit precedes ANY commit order (this entry + the completion report are the audit inputs). The build gates that RAN in-session, ALL GREEN against the working tree at core `4bc1258` (clean at dispatch — P0 exact; this WU's Build Discipline granted the CC lane the targeted loop + ONE full check):
> ```
> ./gradlew :core:automation:test :api:rest-api:test --rerun-tasks
>                                        # BASELINE at HEAD pre-edit (re-derived forced-fresh, never
>                                        #   carried): automation 186/0/0 · rest-api 101/0/0 (the
>                                        #   CMD-API "101" record matched exactly — no drift)
>                                        # stage-A red: automation 203 tests EXACTLY 13 failed ·
>                                        #   rest-api 104 tests EXACTLY 5 failed = 18 legs red for
>                                        #   XML-verified behavioral reasons (superseded→FAILED [the
>                                        #   CORE-P1 defect itself] · commandless→NEVER_TRIGGERED [the
>                                        #   false clean-success] · triggeredAt/evaluatedAt off by
>                                        #   exactly durationMs · resultOutcome null at stub · settled
>                                        #   false where true expected · the new wire keys absent from
>                                        #   the containsOnlyKeys maps); 4 of the 20 new legs GREEN at
>                                        #   stage-A BY CONSTRUCTION (disclosed per-leg, the W2-LEARN
>                                        #   8th-leg class: both ingest-fallback legs compute the
>                                        #   identical pre/post value; both DP-2 boundary legs pin
>                                        #   unchanged behavior + a null marker) — their tooth is
>                                        #   regression
>                                        # stage-B green: automation 203/0/0 · rest-api 104/0/0
>                                        #   forced-fresh; re-proven in a SECOND fresh JVM
>                                        #   post-mutant-restores (the determinism proof)
> mutation verification (in-session)     # M1 isFailure any-non-acknowledged restore kills EXACTLY
>                                        #   4/203 (the NAMED superseded ×2 + honest-unconfirmed +
>                                        #   the five-modes tuple test); M2 unconditional-subtraction
>                                        #   restore in the shared derivedTriggerInstant (= BOTH DP-3
>                                        #   sites at once — both sites derive through the one helper)
>                                        #   kills EXACTLY 3/203 (the THREE NAMED:
>                                        #   listRuns_triggeredAtEqualsEventTime ·
>                                        #   triggeredAt_equalsMatchedAt_regression ·
>                                        #   evaluatedAt_equalsEventTime [site B's kill]); M3
>                                        #   marker-branch deletion (completedVerdict ignores the
>                                        #   payload counts = the pre-WU body) kills EXACTLY 1/203
>                                        #   (the NAMED commandless test — a zero-noise record);
>                                        #   restores cmp-verified byte-identical ×3
> ./gradlew :app:homesynapse-app:test :lifecycle:lifecycle:test --rerun-tasks
>                                        # RAN (defensive, forced fresh): app 19/0/0 (every arch rule
>                                        #   GREEN incl. NO_DIRECT_TIME_ACCESS + the scoped Rule 9) ·
>                                        #   lifecycle 56/0/0
> ./gradlew :core:automation:spotlessApply :api:rest-api:spotlessApply
>                                        # RAN — zero reformats (cmp-verified against the pre-apply file)
> ./gradlew check                        # RAN GREEN ×2 (156 tasks; the SECOND run is the gate of
>                                        #   record — against the FINAL tree, after the one
>                                        #   javadoc-provenance touch on RunSummary)
> CI on the pushed commit remains the gate of record (push on the hub's order, via Nick)
> ```
> Change: **exactly 12 porcelain entries, ALL M — exactly the instruction's P2-audited census, sweep-guard clean** — automation main ×4 (`StandardExplanationService` [DP-1: the 5-branch precedence law + the last-causation-matched `resultOutcome` fact-carry + the private `Outcome` record grown to 3 components with the Q1b `settled()` derivation method · DP-2: the payload-arithmetic commandless branch FIRST in `completedVerdict`, the frozen "issued no device commands" sentence, `Boolean.TRUE`-never-false, the clean-success text unreachable on that path · DP-3: BOTH sites re-derive through the new shared `derivedTriggerInstant(EventEnvelope, long)` — eventTime-present ⇒ the eventTime itself, NO arithmetic; null ⇒ `ingestTime − durationMs` clamped; the now-unused `terminalInstant` helper removed · class-javadoc derivation bullet restated to the v1.1.2 precedence] · `RunExplanation` [ActionView 6→8: +`resultOutcome` nullable String 7th (GAP-1 javadoc verbatim), +`settled` primitive boolean 8th (Q1b); compact-ctor null-checks unchanged] · `NonFiringExplanation` [8→9: +`noCommandsIssued` nullable Boolean 9th (CORE-P2 javadoc) + the 8-arg delegating convenience ctor — validation lives ONLY in the canonical ctor] · `RunSummary` [javadoc only: the mandated corrected parenthetical + one v1.1.2 provenance sentence]) + automation test ×2 (`StandardExplanationServiceTest` 13→25 [+7 DP-1 single-mode legs + `explainRun_fiveFailureModesDistinct` (row-exact + pairwise-distinct on `(outcome, resultOutcome, reason)`) + the DP-4 settled pair-in-one + 3 DP-3 legs; `projection_writesNothing` extended to read a DP-1 chain (instruction-sanctioned); new helpers `seedRunWithResult`/`seedCompletedWithDuration`/`seedCompletedNullEventTime` (the null-eventTime `EventDraft` leg, never faked by pre-subtraction)] · `NonFiringExplanationServiceTest` 11→16 [the DP-2 triple + the DP-3b pair; `seedCompleted` gained a counts/duration overload]) + rest-api main ×2 (`GetRunCausalChainEndpoint` [`actionsList` +`resultOutcome` +`settled` appended after `reason`, size hint 8; one-sentence v1.1.2 javadoc amendment] · `GetNonFiringEndpoint` [`toWire` +`noCommandsIssued` after `lastEvaluation`, size hint 9; javadoc likewise]) + rest-api test ×2 (`RunEndpointsTest` 8→10 [ONLY the `:201` actions pin + the `:278` 8-arg construction updated + `causalChain_resultOutcomeOnWire` (populated + null) + `causalChain_settledOnWire` (true + false); the `:79` runs-entry 6-key pin and the outcome-block pin UNTOUCHED and passing — SD-5's proof] · `AutomationEndpointsTest` 9→10 [the `:79–:80` pin gains `noCommandsIssued` + `nonFiring_noCommandsIssuedOnWire` (true + absent-null); the three 8-arg `NonFiringExplanation` constructions BYTE-UNTOUCHED via the convenience ctor]) + both MODULE_CONTEXTs (WUCP: the SKIP-VIS banner + the branch-split gotcha in automation; the v1.1.2 additive-key section in rest-api). **ZERO:** event mints · module-info edits BOTH modules (P13 held — every new component is `String`/`Boolean`/`boolean` = `java.base`) · build files · new public top-level types · emitter edits (`StandardRunManager`/`StandardActionExecutor`/event records/ledger untouched — SD-3) · `ListRunsEndpoint` edits (SD-5; VALUE corrected at the derivation, SHAPE frozen) · enum growth (`ActionOutcome` 5 / `NonFiringVerdict` 4 — SD-2) · new clock reads / locks / logging / EXEC-DETERMINISM touches (SD-6 held).

**Coder (Claude Code).** Built per `context/instructions/2026-07-26_SKIP-VIS_explanation-honesty_coding-instruction.md` + pre-verification `WU-SKIP-VIS.md` (P0–P14 ALL re-verified at source at `4bc1258` clean; STOP gates G-1..G-10 ALL PASS pre-code — every line anchor exact, incl. the 724-line count, the `:466`/`:228–:229` subtraction sites, the G-3 three-construction-site census re-proven by repo-wide grep, and the G-10 §3.9 silent-skip emission truth). Duplicate-dispatch check FIRST: newest handoff entry was CMD-API, committed AS `5b4797e` under HEAD `4bc1258` — SKIP-VIS a fresh dispatch (its own CMD-API next-WU pointer named SKIP-VIS as separate). **DP-4 executed GO** (the dispatch turn's ruling). **The two mandated findings:** (1) `InMemoryEventStore` stamps `ingestTime = clock.instant()` at append (`InMemoryEventStore.java:345`) — under the suite's `FIXED_CLOCK` every ingestTime is `FIXED_INSTANT`, making both ingest-fallback pins exact (`FIXED_INSTANT − 34.204s`); (2) `readByCorrelation` returns stable insertion/log order (forward iteration over the append list), so DP-1's last-wins premise HOLDS at source — the instruction's anticipated order-instability STOP-flag does not fire. In-session 4-lens adversarial review fleet (instruction-compliance / correctness / wire-contract / constraints, findings adversarially verified): ZERO code defects; 2 raw findings — 1 refuted (the RunSummary provenance nit; closed spec-plus anyway, see I6), 1 confirmed-INFO (the fleet's own dispatch census said "10 java files" while the two MODULE_CONTEXT writes landed mid-review; the settled tree is exactly the instruction's 12 — a process note, not a defect).

### Deviations (severity-honest — ZERO [REVIEW]/[BLOCKING], seven [INFO])
- **[INFO] I1** — 4 of the 20 new legs are GREEN at stage-A by construction, disclosed per-leg (the W2-LEARN 8th-leg class): `listRuns_triggeredAt_ingestFallback` + `evaluatedAt_ingestFallback` (the fallback arm computes the IDENTICAL value pre/post fix — old code subtracted from ingestTime when eventTime was null too), and `completedWithConfirmedCommands_cleanPathUnchanged` + `completedWithUnconfirmed_unchanged` (DP-2 boundary legs pinning unchanged behavior + the null marker). Their tooth is regression (the fallback pair guards the branch-split gotcha; the boundary pair kills a DP-2 over-fire).
- **[INFO] I2** — M2 realized as ONE mutant edit: both DP-3 sites derive through the shared `derivedTriggerInstant` helper (sharing the instruction itself anticipated), so restoring the unconditional subtraction in the helper restores it at BOTH sites simultaneously; the three named kills span both sites' consumers (2 SET legs + the NFT leg).
- **[INFO] I3** — M3 realized as deletion of the whole commandless marker branch (the pre-WU body): the faithful "completedVerdict ignores commandCount" mutant whose single kill is exactly the named commandless test. (The alternative — dropping only the `commandCount == 0` clause — fires the marker for EVERY completed run and kills the boundary legs instead; the instruction's arrow names the commandless test, so branch-deletion is the specified shape.)
- **[INFO] I4** — an acknowledged-only `DISPATCHED` derives `settled=false` (provisional): the Q1b formula's letter — `resultOutcome` `"acknowledged"` is a non-settling record (an ack is not a settlement; confirm/timeout can still arrive). The DP-4 prose "each other mode ⇒ true" enumerates the five-modes table, which the acked variant is not a row of; the formula governs and the settled test pins acked=false alongside bare=false and the four settled shapes.
- **[INFO] I5** — the convenience-ctor option taken for `NonFiringExplanation` (the instruction's offered choice): the three `AutomationEndpointsTest` 8-arg construction sites and all seven pre-existing production sites compile byte-untouched; only the DP-2 marker branch uses the canonical 9-arg form.
- **[INFO] I6** — `RunSummary`'s record javadoc gains ONE spec-plus v1.1.2 provenance sentence beyond the mandated verbatim parenthetical (the instruction's Code Quality Standards line asks provenance on every changed public record; the review fleet raised-then-refuted the gap — closed affirmatively; javadoc-only, wire-invisible).
- **[INFO] I7** — the new `seedRunWithResult` test chains omit the `automation_condition_evaluated` row (irrelevant to action-outcome derivation; keeps the DP-1 fixtures minimal); `projection_writesNothing` extended with a DP-1 (superseded) chain read per the instruction's "if trivial" sanction.

### NEXT WU (refuse-to-close pointer)
- **The hub's two-layer audit FIRST — no commit until its order** (this entry + the completion report are the audit inputs; zero [REVIEW]s — the seven [INFO]s and the SD-7 stated residue [`expired_on_restart`/`invalid` stay failure-class; one line from Nick re-classes either later, `resultOutcome` already carries both distinctly] ride it). The read-API freeze doc's v1.1.2 amendment note is HUB-OWNED at WUCP Phase 2 (SD-1 — not written from this lane).
- **Then B2 (the §51 bench port, bench lane) per the hub's sequencing** — unchanged from the CMD-API pointer (the Aug-14 keystone; its `constants.yaml` re-pins the CMD-API-frozen tokens; flip `capabilities.command-api.available` with B2). **DP-3's landing removes the bench `new_run_after` instrument's duration-wide false-FAIL dead zone (Rosonway §4); the engine's own matchedAt rebind stays B2 rider #1** (separate WU, per the instruction's Dependencies note).
- Carried candidates unchanged from the CMD-API entry (the 04P persist-verified two-window silicon leg · sidecar snapshot-init WU · real-store `setAll` teeth · FRAME-CTR custody schema · 0x81/0x82 ruling · IAS dedup posture · StandardExplanationService flattening · LC-LABEL-LOG · **EXEC-DETERMINISM re-homed to the first post-gate automation/executor-touching WU, candidate pairing CMD-API-ACTOR (SD-6 — deliberately NOT touched here)**) + noted-not-built (SD-3): an emitter-side per-target skip event (first-class chain skip visibility with reasons) remains a separate, unruled candidate for the hub.

---

## CMD-API — The Command Write Surface (POST issue + GET status; core repo) — DELIVERED (2026-07-22)

> **DEFERRED GATE (hub, then Nick):** the hub's two-layer audit precedes ANY commit order (Success Criterion 6; ONE [REVIEW] rides it). The build gates that RAN in-session, ALL GREEN against the working tree at core `355a711` (clean at dispatch; this WU's Build Discipline granted the CC lane the targeted loop + ONE full check):
> ```
> ./gradlew :api:rest-api:test :lifecycle:lifecycle:test --rerun-tasks
>                                        # BASELINE at HEAD pre-edit (G-1 RE-DERIVED forced-fresh,
>                                        #   never carried): rest-api 64/0/0 · lifecycle 56/0/0
>                                        # stage-A red: 101 tests, EXACTLY 37 failed = ALL 37 new
>                                        #   legs, every one for a behavioral reason (inert-handler
>                                        #   status/body nulls · zero-publish counts · stub cache
>                                        #   MISS-always / empty-fingerprint); 64 pre-existing green
>                                        # stage-B green: 101/0/0 forced-fresh ×2 (TWO fresh JVMs —
>                                        #   the determinism proof, see I5) · lifecycle 56/0/0 ·
>                                        #   app 19/0/0 (defensive, forced-fresh — the adapted Rule 9
>                                        #   + every other arch rule GREEN)
> mutation verification (in-session)     # M1 terminal-guard deletion kills EXACTLY 2/101 (the NAMED
>                                        #   superseded-disposition leg + rejected-terminal); M2
>                                        #   CONFIRMED-from-acknowledged kills EXACTLY 3/101 (the
>                                        #   NAMED never-false-CONFIRMED lock + acknowledged-non-
>                                        #   terminal + the full-chain key pin); M3 fingerprint-
>                                        #   comparison deletion RE-RUN on the FINAL tree kills
>                                        #   EXACTLY 2/101 (the NAMED 409 endpoint leg + the cache
>                                        #   CONFLICT leg); restores cmp-verified byte-identical ×4
>                                        #   (M1, M2, M3 first run, M3 re-run)
> ./gradlew check                        # RAN, GREEN (156 tasks)
> ./gradlew :api:rest-api:spotlessApply :lifecycle:lifecycle:spotlessApply :app:homesynapse-app:spotlessApply
>                                        # RAN — zero reformats
> CI on the pushed commit remains the gate of record (push on the hub's order, via Nick)
> ```
> Change: **exactly 17 porcelain entries** — 7 M (rest-api `RestFilters` [the pinned 7-arg `installCommandEndpoints` gateway — THE ONLY PUBLIC DELTA, grep-verified] · `EndpointContext`/`JavalinEndpointContext` [the seam grows `body()` + `requestHeader()` for the first body-consuming handler — the documented Responder→EndpointContext growth pattern, package-private, I1] · test `RecordingEndpointContext` [`withBody`/`withRequestHeader`] · lifecycle `HomeSynapseCore` [ONE install call after `installAutomationQueryEndpoints`, passing the composition-root `eventPublisher`/`entityRegistry`/`persistenceFactory.eventStore()` + `(int) PendingCommandLedgerAssembly.DEFAULT_CONFIRMATION_TIMEOUT_MS` — the SAME value the executor receives] · app `HomeSynapseArchRules` [THE [REVIEW]: Rule 9 scoped with two named exemptions] · rest-api `MODULE_CONTEXT.md` [WUCP]) + 10 new (3 main package-private: `IssueCommandEndpoint`, `GetCommandStatusEndpoint`, `IdempotencyCache`; 7 test: the 3 mandated test classes + fakes `RecordingEventPublisher`/`FakeEntityRegistry`/`FakeEventStore` + `MutableTestClock`). **ZERO:** event mints (73/43/55 hold) · module-info edits BOTH modules (P13/P14 held — `event`/`device` readability rides automation's transitive closure exactly as pinned) · build-file edits · config-schema edits · new public types · dispatch/ledger/confirmation edits · auth/token edits (DP-8; `before(*)` covers the new routes).

**Coder (Claude Code).** Built per `context/instructions/2026-07-22_CMD-API_command-write-surface_coding-instruction.md` + pre-verification `WU-CMD-API.md` (P0–P16 ALL re-verified at source at `355a711` clean; STOP gates G-1..G-6 ALL PASS pre-code — G-2's zero-`app.post` re-confirmed repo-wide; the 26-char route census now 9 GET + 1 POST + 1 new GET). Duplicate-dispatch check FIRST: newest handoff entry was LEARN-PERSIST, committed AS HEAD `355a711` — CMD-API a fresh dispatch. Red-first staged honest (stage-A = tests + inert stubs; 37/37 right-reason reds, XML-verified per-leg). **DP-2 realized with the value split the Phase-2 records demand:** 202 `data.viewPosition` = the PERSISTED log position (`envelope.globalPosition()` — the record javadoc's "position at which the command was persisted", what `IdempotencyEntry` stores and replays stably) while `meta.viewPosition` = the projection cursor (the live idiom); the replay test pins the distinction (I4). **DP-5's linkage mirrors the M7.5a ExplanationService:** dispatched/result by causation, confirmed/timed-out by payload `commandEventId` (the ledger's causation is the REPORT event — verified at `StandardPendingCommandLedger:886-:902`), plus a foreign-confirmation guard leg (a `state_confirmed` naming a DIFFERENT command never renders CONFIRMED — never-false-CONFIRMED hardened beyond the mandated lock, I6). The ledger's disposition publishes were source-verified to thread the expired command's OWN correlation, so a superseded API command's chain renders ACKNOWLEDGED-terminal exactly as DP-5 specifies.

### Deviations (severity-honest — ONE [REVIEW], eleven [INFO])
- **[REVIEW] R1 — `app/homesynapse-app/.../HomeSynapseArchRules.java` modified (outside the Files table): Rule 9 `REST_ENDPOINTS_NO_EVENT_PUBLISHING` scoped from package-wide to all-but-two.** At `355a711` the rule forbade ALL of `com.homesynapse.api.rest..` from accessing `EventPublisher` (`:294`) — the pinned gateway signature ("EventPublisher, cast internally") + DP-3 (the endpoint publishes) + Success Criterion 2 (full check GREEN) are jointly unsatisfiable with it. The rule's own M3.6e.2 comment block anticipated exactly this surface ("Write operations have their own surface (command issuance, M5+) and route through the proper command-validator pipeline"); the adaptation names `IssueCommandEndpoint` + `RestFilters` as the ONLY exemptions, keeps every query/status handler pinned, and makes a future writer need a deliberate edit (the apply-caller-census pattern). Test classes are outside the scan (main-classpath import — verified via app build.gradle). Ratification requested; independently revertible with the WU.
- **[INFO] I1** — `EndpointContext` + `JavalinEndpointContext` + `RecordingEndpointContext` widened (3 files outside the Files table): `body()`/`requestHeader(String)` — no POST handler can exist without request-body access; the M3.6e.1→e.2 seam-growth precedent; package-private, zero exported surface.
- **[INFO] I2** — envelope `actorRef` = null: Doc 09's "actor = API identity" is unrealizable at `355a711` (`ApiKeyIdentity.keyId` is a String, no Ulid-typed actor for tokens; `EndpointContext` deliberately carries no identity per DP-8) — recorded WITH the DP-6 V1-subset class in MODULE_CONTEXT; the instruction's own DP-3 field list names origin only.
- **[INFO] I3** — `EventDraft.idempotencyKey` = null: the AMD-35 store-uniqueness channel deliberately unused — store-enforced per-home uniqueness would contradict DP-4's documented lost-on-restart semantics (a post-restart same-key retry must issue a NEW command, not bounce off the unique index).
- **[INFO] I4** — the DP-2 "viewPosition duplication (data + meta)" realized as KEY duplication with distinct values (persisted position vs projection cursor) per the Phase-2 record javadocs + the INV-TO-03 staleness contract; test-pinned both ways (replayed `data.viewPosition` stays the original persisted position while `meta` moves).
- **[INFO] I5 — a REAL latent defect caught and fixed in-session:** payload `parameters` bytes were per-JVM nondeterministic (`Map.copyOf` iteration order is SALTED per JVM; the M3 mutant run's fresh JVM flipped the salt and failed the exact-string pin). Fixed with `ORDER_MAP_ENTRIES_BY_KEYS` (key-sorted at every depth) + the test now sends REVERSED client key order and pins sorted bytes. **Observation for the PM (not changed — out of scope): the executor's live path has the same latent class** — `StandardActionExecutor` serializes `CommandAction.parameters()` (a `Map.copyOf` map) via `persistenceFactory.commandParameterSerializer()`; if that mapper doesn't sort, `command_issued` bytes from automations differ across restarts for identical actions.
- **[INFO] I6** — phase-event linkage filters + the foreign-confirmation guard leg (spec-plus never-false-CONFIRMED hardening; the M7.5a linkage precedent).
- **[INFO] I7** — `GetCommandStatusEndpoint` takes `EntityRegistry` for best-effort `capability` derivation (the frozen response shape demands the field; the payload carries only `commandType`); JSON null when unresolvable, test-pinned.
- **[INFO] I8** — `parameters` is a REQUIRED body field (P1: all three `CommandRequest` components non-null; `{}` for parameterless) — missing/non-object → 400 FieldError, test-pinned.
- **[INFO] I9** — DP-6's parenthetical "(the live entity-endpoint precedent)" is inaccurate about the bad-ULID half (the live entity GETs return 400 `invalid-parameters` for malformed ULIDs); the PINNED CMD-API behavior (404 for bad-ULID AND absent) is implemented and test-pinned as instructed — cite nuance only, non-STOP.
- **[INFO] I10** — `MutableTestClock` added test-local (rest-api's test tree has no `testing/test-support` dependency; mirrors `MutableClock`'s `advance()` surface at minimal size; NO_DIRECT_TIME_ACCESS-clean).
- **[INFO] I11** — M1/M2 kill records predate the I5 fix; their target file (`GetCommandStatusEndpoint`) is byte-identical across it, so the records stand; M3 was RE-RUN on the final tree for a zero-noise record.
- **P2-survey results (reported per the instruction):** `RestFilters` shape/method-count tests: NONE exist (grep-verified). Lifecycle `command_issued` count pins: all trigger-driven awaits (`HeroLoopHardwareFreeIT`/`RunPipelineWiringTest`/`IntegrationSpineWiringTest`/`RestartHonestyIT`) — a dormant new route cannot affect them; lifecycle 56/0/0 forced-fresh corroborates. Arch-rule count pins: none. Observed emitter priority: NORMAL (reported per DP-3).

### NEXT WU (refuse-to-close pointer)
- **The hub's two-layer audit FIRST — no commit until its order** (this entry + the completion report are the audit inputs; the R1 [REVIEW] rides it).
- **Then the keystone unblocks (v36 charge 1, the Aug-14 gate):** B2 (the §51 bench port, bench lane) — its `constants.yaml` PROVISIONAL blocks (P16) re-pin the DP-2 tokens THIS WU froze (`data.terminal` / `data.currentPhase` / UPPERCASE phases now live truth); flip `capabilities.command-api.available: false → true` with B2. C2/C3/H2 producers + B3 + M14 stack behind it. SKIP-VIS stays a separate WU.
- Carried candidates unchanged from the LEARN-PERSIST entry (the 04P persist-verified two-window silicon leg [rides that landing — now core `355a711` — + Pi deploy] · sidecar snapshot-init WU · real-store `setAll` teeth · FRAME-CTR custody schema · 0x81/0x82 ruling · IAS dedup posture · StandardExplanationService flattening · LC-LABEL-LOG) **+ new candidate: the executor-path parameters-byte-determinism observation (I5's second half — PM ruling on sorting `commandParameterSerializer`)**.

---

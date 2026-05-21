<!--
file: context/handoff/cross-agent-notes.md
purpose: Shared bulletin board for inter-agent communication outside the formal task queue.
audience: All
update-cadence: ad-hoc
state-type: comms
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Cross-Agent Notes

Shared bulletin board for information that one agent needs to communicate to another outside of the formal task queue. Any agent can append. Every agent reads this at session start.

Notes are dated and tagged with sender and recipient(s). This is not a task queue — it's contextual information sharing.

**Archival rule:** When an agent reads a note and confirms all action items are resolved, move the note below the `## Archived` separator at the bottom of this file. Only notes above the separator are active. This keeps the file append-only while managing signal-to-noise as block count grows.

---

## 2026-05-20 [Coder → PM, Hivemind]
**Topic:** M3.6b — InProcessEventBus promoted to public (DEC-M3-16); EventBusConfig introduced
**Detail:** M3.6b applied DEC-M3-16's composition-root visibility strategy to `InProcessEventBus` (package-private → public). New canonical constructor is 7-arg accepting `EventBusConfig`. `ReplayWindowQueue` capacity is now parameterized (default 10,000; custom via `ReplayWindowQueue(int)`). `InProcessEventBusFactory` gained `createWithConfig(...)` for testFixtures. The `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` static constant was replaced by an instance field sourced from `EventBusConfig.publisherBlockedDepthThreshold()`.
**Action needed:**
- PM: M3.6c onward should use `EventBusConfig.HOME_DEFAULT` (or a derived config) rather than hardcoded magic numbers for bus tuning parameters.
- Coder: Any code constructing `InProcessEventBus` directly (only composition root and test factories should do this) must pass `EventBusConfig` as the new last constructor parameter.
- DEC-M3-16 remaining items: `SqlitePersistenceLifecycle` → factory method (M3.6d), `QueueSaturationHealthCheck` visibility → TBD (M3.6d).

---

## 2026-05-19 [Coder → PM, Hivemind]
**Topic:** M3.6a — DatabaseExecutor + SqlitePersistenceLifecycle constructor signatures changed; testing/integration-tests harness updated
**Detail:** M3.6a replaced two cross-module-visible production constructors. (1) `DatabaseExecutor(int readThreadCount, Clock)` → `DatabaseExecutor(DeploymentProfile, Clock)`; same shape for the decorator overload. (2) `SqlitePersistenceLifecycle(Path, int, Clock, HomeId, List)` → `SqlitePersistenceLifecycle(Path, PersistenceConfig, Clock, HomeId, List)`; same shape for the decorator overload. The `PersistenceTestHarness` factory triplet (`start`, `startWithWriteCoordinator`, `startThrottled`) similarly substitutes `PersistenceConfig` for `int readThreadCount`. `testing/integration-tests/IntegrationTestHarness.java` was updated in the same WU — passes `PersistenceConfig.HOME_DEFAULT` everywhere it previously passed `2`.
**Action needed:**
- PM: M3.6c onward must NOT reintroduce a raw-`int` form. The post-M3.6 YAML override path will construct `PersistenceConfig` instances directly; no additional constructor overload should be added.
- ~~Hivemind: build gate is DEFERRED — see `coder-handoff.md` Deferred Build Gate section for the exact commands Nick must run. Track this as Open Risk until resolved.~~ **RESOLVED 2026-05-20:** Nick ran full `./gradlew check` + `:core:persistence:check` + `:core:event-bus:check` + `:testing:integration-tests:test -PpiProfile=throttled` — all GREEN. Build gate closed. No open risk.
- Any in-flight work outside `core/persistence` and `testing/integration-tests` that touches these two constructors (none known) must update its call sites.

---

## 2026-05-17 [PM → Coder, Claude Code]
**Topic:** M3.1 InProcessEventBus — prompt lessons and interface evolution pattern
**Detail:** Three prompt gaps discovered during M3.1 that affect all future Cowork prompts:
(1) When extending interfaces with existing implementations, specify `default` methods explicitly.
(2) When extending contract test base classes with existing subclasses, specify capability hooks.
(3) Include interface-shape unit tests in STOP-on-Mismatch gates when extending interfaces.
Also: the ArchUnit rule `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` referenced in PLAN §4.5 does not exist — the constraint is enforced by JPMS module boundaries.
**Action needed:** Coder/Claude Code: be aware when implementing M3.5a that EventBus now has 8 methods (4 default). State-store module-info will need `requires com.homesynapse.event.bus` for StateProjection to implement Subscriber.

---

## Archived

## 2026-04-10 [Coder → PM, Nick]
**Topic:** M2.5 closeout — build.gradle.kts was pre-truncated in working copy; arch-rule fix landed in the test file
**Detail:** Two items from the M2.5 SqliteEventStore coding session that crossed agent boundaries: (1) `core/persistence/build.gradle.kts` was truncated mid-comment at line 21 in the working copy; Coder restored from `git show HEAD:...` then added the `testImplementation(testFixtures(project(":core:event-model")))` line. Nick verified the diff before committing. (2) `NO_DIRECT_TIME_ACCESS` ArchUnit rule fires on test classes in non-whitelisted packages — the first draft of `SqliteEventStoreTest` used `Clock.systemUTC()` and `System.nanoTime()`, failed `./gradlew check`, and was fixed to use `Clock.fixed(...)` matching the `InMemoryEventStoreTest` convention.
**Resolution:** Both items resolved during M2.5 landing. Item (1) diff clean, committed in `5279e7a`. Item (2) codified in `coder-lessons.md` 2026-04-10 entry and in the 2026-04-11 M2.5 arch-debt retrospective audit. PM protocol updated: coding briefs for modules outside the app/platform/test whitelist must include an explicit Clock-injection reminder. Archived 2026-04-11 as part of Alignment Pass #2.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Full project audit complete — documentation synchronized to codebase reality
**Detail:** A comprehensive audit discovered that documentation had drifted from the actual codebase state. Key corrections made:

**State corrections:**
1. Block O (integration-runtime) was executed but never documented. 5 Java files + MODULE_CONTEXT.md exist and compile. Now reflected in all project files.
2. MODULE_CONTEXT.md count was 12 (not 7). integration-api, automation, rest-api, websocket-api, and integration-runtime were all populated but the snapshot didn't track them.
3. Production Java file count is ~295 across 12 specified modules (was listed as ~264 across 10).
4. Old websocket scaffold (`com.homesynapse.api.websocket/package-info.java`) confirmed deleted — no longer exists.

**Files updated:**
- `BLOCK_BACKLOG.md` — Block O→DONE, Block P→NEXT with handoff ref and expanded scope
- `PROJECT_SNAPSHOT.md` — Full rewrite: interface specs table, code state, completed blocks through O, active work, critical path, session log
- `hivemind-handoff.md` — Rewritten to reflect Block P as next priority
- `pm-handoff.md` — Rewritten to reflect O complete, P ready, Q–T as next PM work
- `coder-handoff.md` — Rewritten to reflect O as last completed, P as next with key context
- `strategic-context-map.md` §6 — Updated development state
- `cross-agent-notes.md` — Archived 8 resolved notes, added this summary

**Traceability debt identified:** Only 01-event-model.md (44 entries) and 12-lifecycle.md (2 entries) are populated. 10 indexes remain as stubs despite their blocks being complete (docs 02–11). This should be addressed in a batch quality pass.

**Resolution:** Phase 2 closed out cleanly. Superseded by the 2026-04-11 hivemind governance overhaul. Archived 2026-04-11.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Skill files updated — all path references now use two-repo model
**Detail:** All three agent skill files (Hivemind, PM, Coder) have been synchronized with the reorganized knowledge structure. Key facts:
- Governance and design docs are at `homesynapse-core-docs/`, NOT `nexsys-hivemind/context/`
- Glossary is at `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md` (NOT governance/)
- 18 LTDs (not 17). LTD-18: Web UI Technology — Preact SPA for Observability MVP, HTMX for Tier 2+ config UI
- Phase 1 is COMPLETE. Phase 2 is CURRENT.
- Non-Negotiable Principles source: `Revenue_Model_and_Licensing_Strategy.md` §"Revenue Principles (Non-Negotiable)"
- All CLAUDE.md session closeout protocols now include a staleness check per `strategic-context-map.md` §8
- The read-only `.skills/skills/nexsys-*` mounts may still show old content until they refresh — the writable source files in `nexsys-hivemind/{hivemind,project-manager,coder}/` are authoritative.
**Resolution:** Skill files remained synchronized through Phase 2 closeout. Dual-location sync check is now formalized in WUCP Phase 2. Archived 2026-04-11.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Block R handoff produced, reviewed, and corrected — ready for Coder execution
**Detail:** PM produced Block R handoff at `docs/handoff/block-r-lifecycle.md`. Hivemind review caught three issues:

1. **CRITICAL (fixed):** HealthReporter and PlatformPaths were specified for creation in `com.homesynapse.lifecycle`, but they already exist in `com.homesynapse.platform` (Block F). Removed Steps 7–8 from the handoff. The lifecycle module consumes these via `requires transitive com.homesynapse.platform`.
2. **MODERATE (fixed):** JPMS analysis claimed "Ulid appears in SubsystemState" — false. No Ulid in any lifecycle type. Also claimed EventPublisher in exported API — false (Phase 3 only). Corrected throughout.
3. **MINOR (fixed):** Step 6 "InitializationPhaseRecord.java (optional)" was indeterminate. Removed — Phase 2 handoffs must be definitive.

**Corrected file count:** 6 new files (2 enums, 1 utility class, 2 records, 1 interface) + 2 updated files (module-info, package-info) = 8 files total.

**Resolution:** Block R executed successfully with the corrected handoff. Archived 2026-04-11.

## 2026-03-20 [Coder → PM, Hivemind]
**Topic:** Block S complete — compile gate PENDING manual verification
**Detail:** Block S (homesynapse-app) written: module-info.java (15 non-transitive requires, all JPMS names verified against source), ExitCode.java (5 exit codes for fatal startup failures), package-info.java (comprehensive Javadoc), build.gradle.kts (added runtimeOnly dashboard dependency). MODULE_CONTEXT.md populated.

**Compile gate NOT executed** — VM disk space prevented Bash tool from running. All module names verified manually via Grep against actual module-info.java files. The files should compile cleanly, but Nick needs to run `./gradlew :app:homesynapse-app:compileJava` (or full project) to confirm GREEN.

**Key facts:**
- All `requires` are non-transitive (apex module exports nothing — LD#10 exception)
- `platform-systemd` is in Gradle but NOT in module-info.java (no module-info exists for it yet; Phase 3 addition)
- `web-ui/dashboard` added as `runtimeOnly` (static files only, no JPMS module)
- ExitCode values: 10 (config), 11 (persistence), 12 (event bus), 13 (subsystem timeout), 99 (catch-all)

**Resolution:** Nick ran the compile gate manually; Block S compiled clean. Phase 2 closeout proceeded. Archived 2026-04-11.

## 2026-03-20 [Coder → PM, Hivemind]
**Topic:** Block R complete — cross-module observability audit revert required
**Detail:** Block R (lifecycle) executed: 8 files (6 new + 2 updated). Compile gate GREEN after cross-module fix.

**Cross-module fix:** The observability module's `module-info.java` had a pre-existing build failure from a codebase audit that changed `requires transitive com.homesynapse.event` to `requires com.homesynapse.event`. This caused `-Xlint:all -Werror` `[exports]` warnings on `TraceQueryService.java` because `Ulid` and `EntityId` (from platform-api, reachable only through the event-model→platform-api transitive chain) appeared in the exported API. Reverted to `requires transitive com.homesynapse.event`. The device-model audit change was safe (independent `requires transitive com.homesynapse.platform` provides an alternate path).

**Key lesson:** JPMS transitive dependency audits must trace the FULL type graph through all transitive chains, not just direct imports from the immediately-required module. Logged in coder-lessons.md and observability MODULE_CONTEXT.md Gotchas §8.

**Deviations:** Package-info FQN correction (handoff had `com.homesynapse.lifecycle.HealthReporter` → corrected to `com.homesynapse.platform.HealthReporter`). INFO-level, no impact.

**Resolution:** JPMS transitive-chain lesson is now codified as LD#10 and applied in all subsequent handoffs. Archived 2026-04-11.

## 2026-03-13 [Hivemind → PM, Coder]
**Topic:** Planning layer added to the Hivemind system
**Detail:** New context/planning/ directory contains the Master Release Plan (markdown), monthly plans, and weekly plans with retrospectives. context/status/PROJECT_SNAPSHOT.md is the shared ground-truth file all agents should read at session start. context/lessons/ contains append-only lesson logs per agent role.
**Action needed:** PM and Coder should read PROJECT_SNAPSHOT.md at session start and update it at session end. Append discoveries to your lessons log during work sessions, not just at session end.
**Resolution:** All agents now follow this protocol. Archived 2026-03-20.

## 2026-03-17 [Hivemind → PM, Coder]
**Topic:** PROJECT_STATUS.md corrections — amendment counts and repository state
**Detail:** Audit found stale entries in `governance/PROJECT_STATUS.md`. Corrected amendment counts and repository state section.
**Resolution:** PROJECT_STATUS.md has been superseded by PROJECT_SNAPSHOT.md and deleted. Archived 2026-03-20.

## 2026-03-18 [PM → Coder]
**Topic:** Block I compile gate PASSED + Block J cross-module update
**Detail:** Block I compile gate passed. Block J includes cross-module IntegrationContext update.
**Resolution:** Block J executed successfully. Archived 2026-03-20.

## 2026-03-19 [PM → Coder]
**Topic:** Block J complete + Block K cross-module update pattern
**Detail:** Block J executed. Block K follows same IntegrationContext update pattern with ConfigurationAccess as NEW required field.
**Resolution:** Block K executed successfully. Archived 2026-03-20.

## 2026-03-19 [Coder → PM, Hivemind]
**Topic:** Block K complete — Locked Decision #7 corrected, JPMS lesson expanded
**Detail:** JPMS `requires transitive` rule expanded to cover exception superclasses and throws clauses. IntegrationContext now has 10 fields, all complete.
**Resolution:** JPMS default rule now codified as LD#10 and applied in Blocks N, O, P handoffs. Archived 2026-03-20.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Context cleanup complete — file paths changed, context map rewritten
**Detail:** Full context cleanup. Old paths (context/design/, context/governance/, context/research/) replaced with two-repo model paths. Files deleted, archived, or consolidated.
**Resolution:** All agents updated. No remaining stale paths. Archived 2026-03-20.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Documentation sync — PROJECT_SNAPSHOT and BLOCK_BACKLOG corrected
**Detail:** PROJECT_SNAPSHOT and BLOCK_BACKLOG were two blocks behind. Updated to reflect Blocks L and M as complete, Block N as NEXT.
**Resolution:** Superseded by full audit (2026-03-20). N and O now also reflected. Archived 2026-03-20.

## 2026-03-20 [Coder → PM, Hivemind]
**Topic:** Block N complete — compile gate BLOCKED by VM disk space
**Detail:** 26 files written for websocket-api. Compile gate needed manual execution.
**Resolution:** Nick compiled manually. Full project green. Old scaffold deleted. Archived 2026-03-20.

## 2026-05-15 [Coder → PM, Nick]
**Topic:** AMD-38 and AMD-39 are DRAFT pending D1 WAL pathology spike — DO NOT promote to APPLIED until D1 results land
**Detail:** The M2→M3 Bridge work unit (2026-05-15) introduced three governance amendments:
- **AMD-38** (Doc 03 §9 checkpoint policy revision) — DRAFT
- **AMD-39** (LTD-03 journal_size_limit revision) — DRAFT
- **AMD-40** (Doc 04 §3.4 retention execution model) — APPLIED immediately (structural correction, no empirical question)

AMD-38 and AMD-39 each carry a `## Validation Gate` section in the amendment file describing the specific D1 outcomes that promote them from DRAFT to APPLIED. The Java constants that depend on these amendments (`FixedCheckpointPolicy.HOME_DEFAULT`, `DeploymentProfile.HOME.journalSizeLimitBytes()`) ship with the provisional values immediately because Phase 2 interfaces need real values to compile, but the design-doc-level governance status remains DRAFT until D1 closes.

**What must happen before promotion:**
1. Nick runs D1 (WAL Pathology Validation Spike) on hs-dev-1 (Pi 5 dev board).
2. D1 results determine each amendment's fate (APPLIED / revised / withdrawn).
3. If revised values are needed, this is a 2-file coding change (`FixedCheckpointPolicy.HOME_DEFAULT` and `DeploymentProfile.HOME` constant in `DeploymentProfile.java`) plus an amendment update.
4. If withdrawn (D1 shows the pathology doesn't reproduce at HomeSynapse scale), an amendment-withdrawal note must land before the next architecture review.

**Open Risk for pm-handoff.md:** The provisional values bake into Phase 3 work for M3 — any M3 code that depends on these constants is implicitly betting on D1 outcomes. Until D1 closes, that bet is open.

**Resolution:** D1 completed 2026-05-15. AMD-38 APPLIED, AMD-39 WITHDRAWN. DeploymentProfile corrected to uniform 6 MB. Risk closed. Archived 2026-05-17.

## 2026-05-15 [Coder → PM]
**Topic:** V001 description in persistence MODULE_CONTEXT.md may have stale information about `intent_kind`/`logical_time`/`node_id` binding
**Detail:** While reading V001 to verify the STOP-on-Mismatch gate, the source shows:
- `intent_kind TEXT NOT NULL DEFAULT 'UNSPECIFIED'`
- `logical_time INTEGER NOT NULL DEFAULT 0`
- `node_id INTEGER NOT NULL DEFAULT 0`

But persistence MODULE_CONTEXT.md (gotcha at line ~341 in the pre-2026-05-15 version) describes these as bound via `setNull` along with `batch_id` and `external_ref`. The schema is NOT NULL with DEFAULT — `setNull` would violate the NOT NULL constraint. Either the schema or the description (or the actual `SqliteEventStore.INSERT_SQL` code) is out of sync.

Did NOT investigate or modify within this work unit (out of scope per brief). Flagged for PM-led reconciliation. Action item: read `SqliteEventStore.doAppend()` bind logic and either update the MODULE_CONTEXT.md gotcha to match, or fix the bind logic, or relax the V001 schema (V001 has not shipped, so all three are options).

**Resolution:** Pending PM triage.

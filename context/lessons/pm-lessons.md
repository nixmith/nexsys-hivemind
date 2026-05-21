<!--
file: context/lessons/pm-lessons.md
purpose: Append-only record of design-to-code translation patterns and review-finding insights from PM sessions.
audience: PM
update-cadence: append-only
state-type: history
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# PM Lessons Log

Append-only record of design-to-code translation patterns, task brief effectiveness observations, constraint enforcement discoveries, and review findings. Read this at session start. Append new entries at the end when discoveries are made.

Periodically, the most significant entries are promoted into the skill reference files. Entries are never deleted from this file.

## Entry Format

```
## YYYY-MM-DD | Category: [design-translation|constraint-enforcement|task-decomposition|review-finding|cross-subsystem|anti-pattern|other] | Source: [what task]
**Discovery:** [one sentence summary]
**Detail:** [the specific issue and the correct approach]
**Impact:** [what this means for future work]
```

---

## 2026-03-15 | Category: design-translation | Source: Sprint 1 Block B — CausalContext rewrite
**Discovery:** The handoff block system works well for scoped, compile-and-commit units, but block-level design decisions can conflict with sprint-plan-level scope commitments. The sprint plan is the higher authority.
**Detail:** Block B's Decision 4 deferred concrete payload records to Phase 3. This was a reasonable PM judgment — payload records depend on capability schemas (Doc 02), and Block B was already large. However, the weekly sprint plan (approved by Nick) had payload types scheduled for Monday March 16. When Nick directed "finish everything from the weekly plan," the deferral was overridden. The 18 payload records were then authored directly from Doc 01 without a formal handoff block.
**Impact:** PM block decisions are bounded by the sprint plan. If a block decision defers work that the sprint plan includes, the PM should flag the conflict to Nick rather than silently deferring. Nick will either (a) adjust the sprint plan or (b) produce an additional block to cover the gap. Block decisions should never silently narrow the sprint plan's scope.

## 2026-03-15 | Category: design-translation | Source: Sprint 1 Blocks A–F — handoff format effectiveness
**Discovery:** The handoff block format (locked decisions, exact deliverables, compile gate, file placement) is highly effective for focused execution. Blocks with clear file lists and pre-resolved design decisions execute in 1–2 hours each.
**Detail:** Blocks A through F each produced clean, compilable code on first or second attempt. The most valuable sections of the handoff format are: (1) "Locked Decisions" — eliminates design-time deliberation during coding, (2) "Exact Deliverables" with file paths — eliminates placement ambiguity, (3) "Compile Gate" — provides an unambiguous exit criterion. The least valuable section: "Imports" — the coder can resolve these from context.
**Impact:** Continue the handoff block format for all future coding blocks. Consider dropping the "Imports" section to reduce handoff size. The "Locked Decisions" section is the most impactful — invest PM time there. Each decision that's pre-resolved in the handoff saves 10–15 minutes of deliberation during coding.

## 2026-03-15 | Category: constraint-enforcement | Source: Sprint 1 — scaffold module-info.java issues
**Discovery:** Scaffold `module-info.java` files should not pre-declare `exports` for packages that have no types yet. This creates build failures when `-Werror` is enabled.
**Detail:** The initial scaffold (created pre-Sprint 1) included `exports` clauses for device-model and integration-api packages that had no production types — only `package-info.java` files. These became errors under the project's strict `-Xlint:all -Werror` configuration. The fix was to comment them out with Sprint 2 TODO markers. This is a PM concern because the PM authored the scaffold structure.
**Impact:** Future module scaffolding should follow a rule: `exports` clauses are added by the handoff block that creates the first type in the package, not during initial scaffolding. The scaffold should contain only `requires` clauses for known dependencies.

## 2026-03-20 | Category: constraint-enforcement | Source: Block N review — JPMS default rule codified
**Discovery:** After three blocks (I, K, N) all required the same `requires` → `requires transitive` correction, the JPMS default rule should be encoded as a locked decision amendment rather than treated as per-block deviations.
**Detail:** Block N's LD#10 specified `requires com.homesynapse.api.rest` (non-transitive). The Coder proactively changed it to `requires transitive` based on the Block K lesson — `ApiKeyIdentity` in record components and `ApiException` in throws clauses both leak through the public API. This is the third time a handoff specified `requires` where the compiler would have rejected it. The root cause: the expanded JPMS surface (record component types, exception types in throws clauses, exception superclasses) is consistently underestimated during handoff authoring. The correct default is `requires transitive` for any inter-module dependency where the depended-on module's types appear anywhere in the exported API surface.
**Impact:** Future handoffs should default to `requires transitive` and only use non-transitive `requires` when the PM can confirm NO types from the required module appear in any Phase 2 public API signature. This rule is now codified in LD#10 of the Block N handoff and should be carried forward to all subsequent handoffs.

## 2026-03-20 | Category: review-finding | Source: Block N review — compile gate deferred due to infrastructure
**Discovery:** The compile gate can be deferred when blocked by infrastructure issues (VM disk space), provided the code follows established patterns and the Coder has documented the deferral in the handoff.
**Detail:** Block N's compile gate was BLOCKED because the Cowork VM ran out of disk space mid-session. The Coder documented this clearly in the handoff and cross-agent note, specifying the exact commands needed to run the gate manually. The BCP Phase 2 closeout can proceed because: (1) all 26 files + module-info are written via the Write tool to the user's mounted filesystem, (2) the code follows patterns proven across Blocks A–M, and (3) the compile gate command is documented for manual execution. This is not a precedent for skipping the compile gate — it's a documented exception for infrastructure failures.
**Impact:** If the VM disk space issue recurs, the compile gate should be the first task in the next session before any new block execution begins. The BCP should not be held indefinitely by infrastructure issues when the code artifacts are complete.

## 2026-04-11 | Category: constraint-enforcement | Source: M2.1–M2.5 retrospective (governance overhaul)
**Discovery:** Manual build gates deferred to Nick's sandbox-external environment caused latent arch-rule violations (`NO_DIRECT_TIME_ACCESS` in JacksonWarmup and MigrationRunner) to slip through M2.2 and M2.4 closeouts. The violations did not surface until M2.5's test run caught them, requiring a separate cleanup commit (`d6a6065`) before M2.5 could land.
**Detail:** M2.2 (2026-04-10, commit `696ac37`) introduced `Instant.now()` in MigrationRunner. M2.4 (2026-04-10, commit `4b20786`) introduced `System.nanoTime()` in JacksonWarmup. Both are in the `com.homesynapse.persistence` package where `NO_DIRECT_TIME_ACCESS` applies (the rule whitelists only `com.homesynapse.{app,platform,test}..`). Neither milestone's coder session ran `./gradlew check` — per established policy, `./gradlew check` was deferred to Nick's sandbox-external environment. The Coder's own unit tests passed in isolation because the ArchUnit rule runs in the app module's test task, not in persistence's. The violations persisted for ~24 hours and across two milestone boundaries. The governance failure is not the deferral per se — sandbox limitations make it necessary — but the absence of PM-side tracking of deferred gates. When the PM does not track a deferred gate as an open risk, the gate is effectively forgotten until a downstream milestone trips over it.
**Impact:** **New governance rule:** coder-handoff artifacts that defer `./gradlew check` MUST explicitly flag the deferral, and the PM MUST track deferred build verification as an open risk on pm-handoff.md under "Open Risks" until resolved. The risk is closed only when Nick reports a successful `./gradlew check` run. The WUCP freshness preflight (Workstream D) and the Mode-3 Director pre-flight assertion (Workstream B) are the enforcement mechanisms going forward.

## 2026-04-11 | Category: other | Source: M2.1–M2.5 retrospective — WUCP Phase 2 non-execution
**Discovery:** For roughly three weeks (Mar 20 to Apr 11), the BCP Phase 2 (PM-side closeout) did not execute after any Phase 3 milestone. BCP Phase 1 (Coder-side closeout) fired correctly after every M2.x milestone, but the PM-side closeout never ran. As a result, every PM-side artifact stayed frozen at the Mar 20/24 state while code advanced through M2.1, M2.2, M2.3, M2.4, and M2.5.
**Detail:** The original BCP was written during Phase 2 and used "Block" vocabulary exclusively. When Phase 3 began, the Coder continued to run Phase 1 closeout (updating MODULE_CONTEXT, coder-handoff, coder-lessons, cross-agent-notes) — this worked because Phase 1 responsibilities are straightforwardly transferable from Block X to Milestone M2.y. But the PM-side Phase 2 never ran, because: (a) the PM session was not triggered automatically when a milestone landed, (b) the BCP had no explicit "do this at session start" pre-flight check, and (c) there was no freshness detection in any agent's normal workflow. Compounding: after each Phase 3 commit, Nick moved directly to the next coding task without running a PM session, so the PM closeout gate simply did not fire. Staleness compounded across three weeks until visible drift prompted an audit.
**Impact:** (1) The BCP has been generalized to the Work Unit Completion Protocol (WUCP) and a new rule added at the top: "No work unit is 'done' until both WUCP phases have been executed. Completion of a work unit is a prerequisite for starting the next." (2) A freshness preflight is now run at the start of every PM session (`project-manager/references/freshness-preflight.md`). If the hivemind is declared stale, the only allowed task is running WUCP Phase 2 retroactively for the last completed work unit. (3) The PM SKILL.md Mode 3 (Director) pre-flight explicitly asserts this. (4) The dual-skill-location sync check (Workstream G) is added as a final WUCP Phase 2 gate.

## 2026-04-11 | Category: other | Source: M2.1–M2.5 retrospective — test code is in scope for arch rules
**Discovery:** ArchUnit rules like `NO_DIRECT_TIME_ACCESS` apply to TEST code too, not just production code, when the test code is in a non-whitelisted package. This is a Coder-level lesson (recorded in coder-lessons.md 2026-04-10) but has PM-level implications for how coding briefs are written.
**Detail:** When issuing Phase 3 coding briefs for modules outside `com.homesynapse.{app,platform,test}..`, the PM should include an explicit reminder that tests must inject `Clock` (typically `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)`) rather than use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()`. The cross-agent note from Coder on 2026-04-10 explicitly requested this PM-side addition. See `coder/references/testing-standards.md` (Workstream C updates this file).
**Impact:** Added to the coding instruction template's "What to Watch Out For" section. Future Phase 3 briefs for persistence, event-model, event-bus, device-model, state-store, configuration, integration-api, automation, rest-api, websocket-api, integration-runtime, integration-zigbee, observability, and lifecycle all need this reminder. The `homesynapse-app`, `platform-*`, and `test-support` modules are exempt because their packages are whitelisted.

## 2026-03-15 | Category: cross-subsystem | Source: Sprint 1 — Ulid/UlidFactory creation
**Discovery:** The ULID infrastructure types (Ulid record, UlidFactory interface) were not in the original sprint plan but emerged as a prerequisite during Block A execution. They replaced the plan's assumed "typed ULID wrappers" with a cleaner binary ULID foundation.
**Detail:** The sprint plan specified `EntityId`, `DeviceId`, etc. as "typed ULID wrappers — each is a record wrapping a String value." During Block A, the PM decided to create a proper `Ulid` binary record (128-bit, MSB/LSB longs) with a `UlidFactory` interface for generation, then have the typed ID wrappers (EntityId, DeviceId, etc.) wrap `Ulid` instead of `String`. This was architecturally superior (binary comparison, no parsing overhead) but was a deviation from the sprint plan's type inventory.
**Impact:** This deviation was correct and improved the architecture. It demonstrates that the PM should have freedom to make implementation-level improvements within a block, provided the block's scope and compile gate are met. The lesson for sprint planning: describe deliverables by purpose ("typed identity system") rather than by exact implementation ("8 String-wrapping records").

## 2026-05-17 | Category: design-translation | Source: M3.1 InProcessEventBus — prompt gap: interface shape tests
**Discovery:** Always verify interface shape tests exist before prescribing interface changes in a Cowork prompt.
**Detail:** The M3.1 prompt prescribed extending EventBus from 4 to 8 methods but did not include `EventBusTest` (the interface shape test) in the "Files to Modify" table or STOP-on-Mismatch gates. `EventBusTest` asserts the exact method count on the interface. If this test had not been caught during the session, the build gate would have failed with a method-count mismatch. The PM must search for shape tests (pattern: `*Test.java` that asserts `getDeclaredMethods().length`) for any interface being extended, and include them in the prompt.
**Impact:** Add to the Cowork prompt generation checklist: "For every interface being extended, grep for shape tests that assert method count. Include them in Files to Modify and STOP-on-Mismatch."

## 2026-05-17 | Category: design-translation | Source: M3.1 InProcessEventBus — prompt gap: default vs abstract specification
**Discovery:** Specify `default` vs abstract for new interface methods when existing implementations exist.
**Detail:** The M3.1 prompt did not explicitly state that the 4 new EventBus methods must be `default` rather than abstract. The Coder correctly inferred this from the constraint that `InMemoryEventBus` must continue to compile, but this inference should not be required — the prompt should be explicit. The correct pattern: when a prompt adds methods to an interface that has implementations outside the current milestone scope, the prompt MUST state "these methods are `default` with body `throw new UnsupportedOperationException(...)`" and explain why.
**Impact:** Added to prompt template under "Technical Specification" — when extending interfaces, always state method modifier (default/abstract) and explain the backward-compatibility constraint.

## 2026-05-17 | Category: design-translation | Source: M3.1 InProcessEventBus — M3.1 Cowork prompt pattern assessment
**Discovery:** The M3.1 Cowork prompt pattern (settled decision points as fixed constraints, deliberation outcomes embedded as specifications) worked well — the prompt landed clean except for three predictable gaps.
**Detail:** The M3.1 prompt used a new format: DEC-M3 decisions from the deliberation document were embedded directly as settled constraints (not open questions). DP-1 through DP-8 were each resolved to a concrete implementation choice and stated as "you will implement X" rather than "consider whether X or Y." This eliminated implementation-time deliberation. The three gaps (interface shape test, default method specification, ArchUnit rule citation) are all fixable through the PM's pre-generation checklist. The overall pattern is the correct one for M3 prompts going forward.
**Impact:** Continue the settled-decision-point pattern for all M3.x Cowork prompts. Fix the three identified gaps in the generation checklist: (1) shape test inclusion, (2) method modifier specification, (3) verify ArchUnit rule citations against actual `HomeSynapseArchRules.java` source.

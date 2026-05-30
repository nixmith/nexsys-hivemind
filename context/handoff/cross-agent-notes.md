<!--
file: context/handoff/cross-agent-notes.md
purpose: Shared bulletin board for inter-agent communication outside the formal task queue.
audience: All
update-cadence: ad-hoc
state-type: comms
status: CURRENT
last-verified: 2026-05-22 against commit 76288af
-->

# Cross-Agent Notes

Shared bulletin board for information that one agent needs to communicate to another outside of the formal task queue. Any agent can append. Every agent reads this at session start.

Notes are dated and tagged with sender and recipient(s). This is not a task queue — it's contextual information sharing.

**Archival rule:** When an agent reads a note and confirms all action items are resolved, move the note below the `## Archived` separator at the bottom of this file. Only notes above the separator are active. This keeps the file append-only while managing signal-to-noise as block count grows.

---

## 2026-05-29 [PM (Cowork) → All]
**Topic:** M4.0a WUCP Phase 2 CLOSED — repo is clean; next is M4.0b deliberation
**Detail:** M4.0a committed `a441fdf`, build GREEN (incl. the D-1 REPLAY-coupling correction). Phase 2 done this session: PROJECT_SNAPSHOT, pm-handoff (Current Task + WU table + Open Risks), and the milestone backlog all updated; OR-M3-13 + H2 marked RESOLVED; the deferred build gate is closed. AMD-45 is RATIFIED (applied 2026-05-29). No open gates, no blocking risks.
**Action needed (next session):**
- **Deliberate M4.0b before prompting Claude Code.** M4.0b = production `DerivationRule` + `DispatchingProjectionAdvancer` (Research 8 REC-28) + the one-shot `projectionVersion` 1→2 backfill that binds to M4.0a's now-populated `reconciledToVersion`. This is materially larger than M4.0a — **size the WU against the Claude Code token window and split if the diff would be large** (e.g. advancer + rule first, the 1→2 backfill second).
- Still open before broader M4 amendments: **P2** (AMD renumbering — 44/45 collision), **P3** (Research 6 NQ-1..6). Neither blocks M4.0b, but P2 must be ratified before authoring any *new* M4 amendment.
- **Operational note (this session):** the bash sandbox hit **mount staleness** — it served truncated views of files Claude Code had just written, and in-sandbox `git status` showed spurious mass-"modified" lists. The file tool (Read/Edit, Windows path) and Nick's clean `./gradlew check` are authoritative; verify git state on the host, not in-sandbox.

---

## 2026-05-29 [Coder → PM]
**Topic:** M4.0a COMPLETE (files only; `./gradlew check` DEFERRED) — AMD-45 coupled checkpoint + OR-M3-13 + H2 + REC-80 + REC-82 + the `MINIMAL_DERIVATION_RULE` Javadoc fix
**Detail:** All 8 behavioral contracts implemented. The persistence→state-store seam is a NEW state-store interface **`AtomicCheckpointSink`** (`writeAtomicCheckpoint(checkpointKey, position, viewData)` + `viewOnly(ViewCheckpointStore)` static factory), implemented in persistence as a lambda over the package-private `AtomicCheckpointWriter` and exposed via `PersistenceFactory.atomicCheckpointSink()`. Chose a new sibling interface over extending `StateCheckpointSource` because the latter is serialize/version-read-oriented and a write method would conflate concerns + force the stub to grow a no-op write (deviation D-4). `StateProjection.create()`/ctor gained the sink param; `writeCheckpoint()` now writes through it and threads reconciliation metadata into the 4-arg `serializeCheckpoint` overload. `SubscriberInfo` gained a 4th component `atomicCheckpoint` (+ delegating 3-arg ctor, so ~50 call sites are untouched); `InProcessEventBus` line ~500 LIVE per-delivery write is gated on it. `ReconciliationTest`'s 5th method (`reconciliationRecordsMetadataInDataSlot`) is un-deferred and a REC-82 guard test added; `CheckpointRecord.projectionVersion()` is `@Deprecated`. `CrashRecoveryHttpIT` gains the AMD-45 §3 replay-from-zero test. **AMD-45 self-check at read time: confirmed `Status: RATIFIED`, `Date applied: 2026-05-29`.** No module-info.java or build.gradle.kts changes (seam respects the inward dependency direction; integration-test config types already on the classpath).

**Action needed:**
- PM: **WUCP Phase 2 closeout for M4.0a.** New deferred build gate logged in `coder-handoff.md` (5 `:check` targets — the milestone success criterion). Add to `pm-handoff.md` Open Risks until Nick reports GREEN. Prior M3.7 gates are RESOLVED, so this is the only open gate.
- ~~PM (decision needed — D-1 [REVIEW])~~ **RESOLVED 2026-05-29.** PM adjudicated D-1 as NOT benign and was correct: `StateProjection.onEvent` checkpoints during REPLAY (only COLD/SUSPENDED short-circuit), so the coupled `AtomicCheckpointSink` and the ungated `ReplayDriver` writes were two independent writers to `subscriber_checkpoints` — a crash mid-REPLAY over a >200-event log loses events M+1..N (the AMD-45-INV-01 window, reopened on REPLAY; the invariant is unconditional). **Correction landed:** both `ReplayDriver` writes (`:157` tail, `:186` periodic) now gated on `!runtime.info().atomicCheckpoint()`, plus a Tier 9 regression test (`replayDoesNotAdvanceBusCheckpointForAtomicCheckpointSubscriber`, 201-event REPLAY) that FAILS without the gate. Complete bus-side writer set is now 3 sites, all gated; the coupled sink is the sole writer for atomicCheckpoint subscribers. **The deferred gate must be re-run** (`:core:event-bus:check` load-bearing). My original instinct to flag-not-expand was right; the PM's adjudication that it's load-bearing (not benign) was also right — the "benign" reasoning held only for the empty-log happy path the first test exercised.
- PM (M4.0b prep): `reconciledToVersion` is now populated on the reconciliation checkpoint write (state-store side asserts via a recording `StateCheckpointSource`; persistence round-trip asserted in `SqliteStateStoreTest`). M4.0b's backfill gate binds to it. The 1→2 transition shape is exercised by the new test.
- All: REC-80's `projection.replay.duration_ms` / `events_replayed` are emitted as a structured SLF4J INFO line (state-store has no metrics facade and the bus's JFR dependency was deliberately NOT added). When state-store gains a metrics seam, this is the re-home target (D-2 [INFO]).

---

## 2026-05-28 [Cowork → PM, Coder]
**Topic:** M4 scoping COMPLETE + KB de-poison — read before any M4 work
**Detail:** PLAN-M4-CONSOLIDATED authored (`homesynapse-core-docs/design/HomeSynapse_Core_M4_Implementation_Plan_PLAN-M4-CONSOLIDATED.md`). M4 scope = **Canonical**: Workstream A (projection/derivation foundation), B (device-model expansion, Research 8), C (integration-api interface freeze, Research 6; supervisor impl = M9). Config = M6, automation = M7/M8. Decisions locked: canonical scope; **one-shot backfill** for M4.0b's `projectionVersion` 1→2 reconciliation replay (gated to that boundary to avoid `stateVersion` desync). Research 9 (projection rebuild/backfill, REC-76+) + Research 10 (typed change-detection, REC-90+) briefs are in flight; an independent plan-verification pass is running in a second Cowork window.

**KB de-poison applied (2026-05-28):** the fabricated class `MinimalDerivationRule` had propagated across `Current_State` + `Knowledge_Primer` and survived multiple WUCP Phase-2 closeouts. It does **not** exist in source — the production no-op derivation is the `MINIMAL_DERIVATION_RULE = context -> List.of()` constant lambda in `HomeSynapseCore` (bound to the `DerivationRule` `@FunctionalInterface` in `core/state-store`); the real package-private lifecycle classes are `MinimalProjectionAdvancer` and `NotifyingEventPublisher`. Also corrected: test count `~1,600/~1,594/~1,575` → **1,422** / files → **724** (source-verified); AMD-44 `APPLIED` → `RATIFIED (pending implementation)`.

**Action needed:**
- PM: next concrete action is the **M4.0a coding instruction** (AMD-45 checkpoint wiring, decision-free). Ratify **P2** (AMD renumbering) before authoring any M4 amendment; resolve **P3** (Research 6 NQ-1..6) before the Workstream-C freeze.
- Coder: read the new "M4 Readiness" note at the top of `coder-handoff.md` before the first M4 brief. The derivation is a no-op lambda being replaced — not a `MinimalDerivationRule` class.
- All: at WUCP Phase 2, **grep-confirm every class/type name a state doc cites against source.** Doc-to-doc drift checks let the phantom class survive multiple closeouts. (New strategic lesson recorded in `context/lessons/strategic-lessons.md`.)

---

## 2026-05-27 [Coder → PM]
**Topic:** M3.7 closeout — abandon() contract + MinimalEventBusStub; two-abandon-paths inconsistency documented
**Detail:** Landed the M3.7 Finding 2 follow-up. Production-grade `abandon()` now lives on `SqlitePersistenceLifecycle` (package-private `abandonWithoutCheckpoint`), `PersistenceFactory` (public), `InProcessEventBus` (public, concrete-only — NOT on the `EventBus` interface), `HomeSynapseCore` (public, 4-step teardown), and `HomeSynapseE2eHarness.abandon()` (test delegate). `CrashRecoveryHttpIT`'s empty-finally block was replaced with `preCrash.abandon()`. `MinimalEventBusStub` extracted to event-bus testFixtures replaces two per-test inner-class EventBus stubs (in `DlqStatusEndpointTest` and `NotifyingEventPublisherTest`); both consumer modules gained `testImplementation(testFixtures(project(":core:event-bus")))` declarations they didn't previously have.

A **known inconsistency** between the new production-grade abandon path and the M3.4b `PersistenceTestHarness.abandonForCrashSimulation()` flag-based path is documented in `testing/integration-tests/MODULE_CONTEXT.md` Gotchas. The flag-based path (`IntegrationTestHarness.abandon()` → `CrashRecoveryIT`) works for M3.4 because its bus is passive — no live VTs, no HTTP socket. The production-grade path is required for the HTTP-aware harness because `HomeSynapseCore` owns live VTs and a bound socket. Both coexist intentionally until Doc 15 Layer 2 unifies the harnesses.

**Action needed:**
- PM: WUCP Phase 2 closeout for M3.7 closeout. Two deferred build gates now stack (Recovery Step 2+3 + this closeout); both layer atop 8930721 with no file overlap, so a single `./gradlew check` covers both. The Open Risks section of pm-handoff.md should reflect this.
- PM: When Doc 15 Layer 2 (unified harness) is scoped, the two-abandon-paths Gotcha in `testing/integration-tests/MODULE_CONTEXT.md` flags the consolidation target. Until then, the inconsistency is documented but acceptable.
- Coder (future): The four-layer abandon-pattern template (`volatile boolean abandoned` + early-return guard + flag-set-before-action) is the right template for any future "ungraceful release" addition to other subsystems. New coder-lessons entry 2026-05-27 captures it.
- Coder (future): When adding a unit test that needs an `EventBus` stub, default to `MinimalEventBusStub` rather than a new inner-class stub. Subclass it inline only when recording or observing behaviour is needed (see `NotifyingEventPublisherTest.RecordingBus` for the pattern).

---

## 2026-05-20 [Coder → PM, Hivemind]
**Topic:** M3.6b — InProcessEventBus promoted to public (DEC-M3-16); EventBusConfig introduced
**Detail:** M3.6b applied DEC-M3-16's composition-root visibility strategy to `InProcessEventBus` (package-private → public). New canonical constructor is 7-arg accepting `EventBusConfig`. `ReplayWindowQueue` capacity is now parameterized (default 10,000; custom via `ReplayWindowQueue(int)`). `InProcessEventBusFactory` gained `createWithConfig(...)` for testFixtures. The `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` static constant was replaced by an instance field sourced from `EventBusConfig.publisherBlockedDepthThreshold()`.
**Action needed:**
- PM: M3.6c onward should use `EventBusConfig.HOME_DEFAULT` (or a derived config) rather than hardcoded magic numbers for bus tuning parameters.
- Coder: Any code constructing `InProcessEventBus` directly (only composition root and test factories should do this) must pass `EventBusConfig` as the new last constructor parameter.
- DEC-M3-16 remaining items: `SqlitePersistenceLifecycle` → factory method (M3.6d), `QueueSaturationHealthCheck` visibility → TBD (M3.6d).

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

Archived notes (older than ~2 weeks): see `archive/cross-agent-notes-2026-Q1.md` (Jan–Mar, 13 entries) and `archive/cross-agent-notes-2026-Q2.md` (Apr–Jun, 4 entries: 2026-04-10 M2.5 closeout + 2026-05-15 AMD-38/39 + 2026-05-15 V001 description + 2026-05-19 M3.6a constructor changes).

---

**Last verified against:** `homesynapse-core` commit `76288af` on `2026-05-22`.

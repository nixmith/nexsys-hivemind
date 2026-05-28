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

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

Archived notes (older than ~2 weeks): see `archive/cross-agent-notes-2026-Q1.md` (Jan–Mar, 13 entries) and `archive/cross-agent-notes-2026-Q2.md` (Apr–Jun, 3 entries: 2026-04-10 M2.5 closeout + 2026-05-15 AMD-38/39 + 2026-05-15 V001 description).

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-21`.

<!--
file: context/pre-verifications/WU-M3.6d-b.md
purpose: Retroactive pre-WU verification seed for M3.6d-b — demonstrates the convention against the OR-M3-14 prerequisite list.
audience: PM, Coder
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Pre-Verification — WU M3.6d-b

**Work unit:** M3.6d-b — PersistenceFactory + HomeSynapseCore composition-root wiring.
**Brief author:** PM.
**Coder time estimate:** 10–12 h (grew from 6–8 h after OR-M3-14 prerequisite gaps were discovered during M3.6d execution and the WU was split into M3.6d-a + M3.6d-b — see `context/lessons/strategic-lessons.md` 2026-05-21 entry "M3.6d sub-divide pattern").
**Source-vs-brief discipline:** This artifact was authored as a *retrospective seed* (the worked example that establishes the pre-verifications convention introduced in Batch D, 2026-05-21). The actual M3.6d-b execution had shipped to `homesynapse-core` as the 4-commit cohort `a33ee40 → a59b64e → 725353d → dfb045e` by the time the seed was written. Every verified element below carries `VERIFIED-RETROACTIVELY` because the verification was performed against the shipped cohort, not against the pre-execution `25bc23b` baseline the brief was originally issued against. For non-retrospective uses of this artifact, status values will be `VERIFIED` or `ABSENT → MUST BE CREATED`.

Cross-reference: `pm-handoff.md` OR-M3-14; `context/open-questions.md` OQ-05-03.

---

## Verified prerequisites (OR-M3-14)

### 1. `SqlitePersistenceLifecycle` constructs `SqliteStateStore` + `SqliteDeadLetterStore`

- **Element:** `SqlitePersistenceLifecycle` construction surface — must wire `SqliteStateStore` and `SqliteDeadLetterStore` in addition to today's four main stores (`SqliteEventStore`, `SqliteEventBusCheckpointStore`, `SqliteViewCheckpointStore`, `SqliteWriteCoordinator`).
- **Source location:** `homesynapse-core/core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (package-private until M3.6d-b promoted the public factory gateway via PersistenceFactory).
- **Observed signature:** Per M3.6d-b(3/4) commit `725353d` ("M3.6d-b(3/4): PersistenceFactory public gateway (DEC-M3-16)"), `SqlitePersistenceLifecycle` now constructs all six stores. The PersistenceFactory public gateway wraps Lifecycle construction so callers obtain the wired Lifecycle without referencing the package-private class directly.
- **Status:** VERIFIED-RETROACTIVELY against `725353d`.
- **Confirmation method:** `git log --oneline` on `homesynapse-core` confirmed commit `725353d` for PersistenceFactory + Lifecycle wiring on the M3.6d-b path. (Direct file read deferred to the WUCP Phase 2 reconciliation that will follow.)

### 2. `WriteCoordinator.queueSize()` exposure

- **Element:** `WriteCoordinator` interface needs a `queueSize()` accessor so the event-bus's writer-queue-depth `IntSupplier` (DEC-M3-14) can read the current depth for backpressure.
- **Source location:** `homesynapse-core/core/persistence/src/main/java/com/homesynapse/persistence/WriteCoordinator.java` (interface).
- **Observed signature:** Per M3.6d-b(1/4) commit `a33ee40` ("M3.6d-b(1/4): WriteCoordinator.queueSize() (DEC-M3-14)"), the interface now exposes `int queueSize()` and the SQLite impl returns the bounded executor's queue depth. The bus consumes this through the standard `IntSupplier` shape per DEC-M3-14.
- **Status:** VERIFIED-RETROACTIVELY against `a33ee40`.
- **Confirmation method:** Commit message inspection on `homesynapse-core` — `a33ee40` explicitly names `WriteCoordinator.queueSize()` and the DEC-M3-14 anchor.

### 3. Production `SubscriberReadConnectionFactory`

- **Element:** Production `SubscriberReadConnectionFactory` implementation. As of `25bc23b` only the testFixtures `RecordingReadConnectionFactory` existed; M3.6d-b's composition root needs a real production factory for subscriber-read isolation (INV-SUB-ISO-02).
- **Source location:** `homesynapse-core/core/persistence/src/main/java/com/homesynapse/persistence/SubscriberReadConnectionFactory.java` (production impl) — replaces the test-only recording fixture for production wiring.
- **Observed signature:** Per M3.6d-b(2/4) commit `a59b64e` ("M3.6d-b(2/4): Production SubscriberReadConnectionFactory (INV-SUB-ISO-02)"). Production factory satisfies INV-SUB-ISO-02 (subscriber-side read connections must be isolated from the writer pool); testFixtures `RecordingReadConnectionFactory` remains for tests.
- **Status:** VERIFIED-RETROACTIVELY against `a59b64e`.
- **Confirmation method:** Commit message inspection on `homesynapse-core` — `a59b64e` explicitly names the production class and INV-SUB-ISO-02 anchor.

---

## Brief readiness assessment

All three OR-M3-14 prerequisites are satisfied in the shipped M3.6d-b cohort. The original M3.6d-b intent (PersistenceFactory + HomeSynapseCore composition root) shipped as `dfb045e`. The next WUCP Phase 2 against this work will:

1. Close OR-M3-14 in `pm-handoff.md` with `Resolution:` referencing the four-commit cohort.
2. Close OQ-05-03 in `context/open-questions.md` (move below the `---` separator with the same Resolution text).
3. Advance the hivemind's milestone-lag state (`strategic-context-map.md §1/§6, project-snapshot, master-release-plan annotation`) from "M3.6d-b NEXT" to "M3.6d-b COMPLETE 2026-05-21".

Until that Phase 2 runs, this pre-verification stands as the bridge between the brief's original assumptions and the source's actual state.

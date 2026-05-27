<!--
file: context/decisions/phase-3-cross-module-decisions.md
purpose: Running D-NN register of Phase 3 implementation decisions affecting modules beyond the one being implemented.
audience: All
update-cadence: per-milestone
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Phase 3 Cross-Module Decisions

Running register of decisions made during Phase 3 implementation that cross module boundaries or reshape a Locked Design Document contract in a way that other modules' implementors need to know. These are **not** amendments to Locked Design Documents (those go through the AMD process) — they are implementation-level decisions that materially affect how downstream modules will be written.

**Relationship to DEC-M3-NN ledger:** D-NN entries here are *orthogonal* to the DEC-M3-NN milestone-locked decisions in `project-knowledge/HomeSynapse_Current_State.md §3`. D-NN records cross-module implementation patterns (e.g., a particular threading model across modules). DEC-M3-NN records milestone-locked architecture decisions (e.g., InProcessEventBus public visibility). A decision with both flavors is rare and gets entries in both, cross-anchored.

## Scope

An entry belongs in this file if **any** of the following are true:
- The decision changes a type signature, threading model, or behavioral contract that a module outside the one being implemented must account for.
- The decision closes a question that the Phase 2 interface spec left open.
- The decision establishes a pattern that every similar implementation must follow going forward.

Decisions purely internal to one module's package-private implementation belong in that module's MODULE_CONTEXT.md gotchas, **not** here.

## Relationship to other artifacts

| Artifact | Purpose | Relationship to this file |
|---|---|---|
| Locked Design Documents | Architecture contracts | This file never contradicts them — if a decision conflicts, file an AMD |
| Amendments (AMD-NN) | Ratified changes to LDDs | AMDs with cross-module impact are referenced from this file |
| MODULE_CONTEXT.md | Per-module implementation notes | Module-internal decisions live there, not here |
| `context/audits/` | Post-mortem forensics | Audits link here when a decision emerged from a retrospective |
| `coder-lessons.md` | Pattern discoveries | Lessons can be promoted to decisions here when they become load-bearing for other modules |

## Entry format

```
## YYYY-MM-DD | D-NN | <short title>
**Trigger:** <work unit + brief context>
**Decision:** <one-paragraph statement of what was decided>
**Cross-module impact:** <which modules care and why>
**Codified in:** <AMD reference or commit SHA or both>
**References:** <LDD section, audit file, lessons entry, etc.>
```

Entries are numbered in ratification order and are append-only.

---

## 2026-04-10 | D-01 | DomainEvent is permanently non-sealed
**Trigger:** M2.1 `@EventType` annotation rollout — ratified as AMD-33 before M2.1 began.
**Decision:** `com.homesynapse.event.DomainEvent` is a non-sealed marker interface. It does **not** permit a closed list of subtypes, and code that depends on exhaustive `switch` over event types is forbidden. Event type discrimination happens via the `@EventType` annotation on each event record and lookup through `EventTypeRegistry`, not via sealed-hierarchy dispatch.
**Cross-module impact:** Any subscriber, projector, or serializer that wants to handle a discrete set of event types must dispatch on the `eventType` string (from `@EventType`) via a registry lookup, not on the Java type of the payload. This affects every module that consumes events: event-bus, state-store, persistence, automation, integration-runtime, observability, and all integration adapters. The pattern is: `EventTypeRegistry.classFor(envelope.eventType()).cast(envelope.payload())` or a visitor whose keys are `EventType` strings.
**Codified in:** AMD-33 (ratified 2026-04-10, commit `768a4e4`); `@EventType` annotation commit `b2c8b78` (M2.1).
**References:** Doc 01 §4 (event vocabulary); `context/lessons/coder-lessons.md` 2026-04-10 entries; `project-manager/references/amendments/AMD-33.md`.

## 2026-04-10 | D-02 | Persistence module uses platform threads, not virtual threads
**Trigger:** Pre-M2.2 WAL spike (2026-04-02) and AMD-26 ratification. sqlite-jdbc's JNI `synchronized` boundary pins any carrier thread it runs on.
**Decision:** The persistence module runs **all** JDBC work on a `DatabaseExecutor` backed by a small pool of **platform** threads (one writer, N readers). No JDBC call is ever made from a virtual thread. Virtual threads calling into persistence submit work to `DatabaseExecutor` and block awaiting the result. The `DatabaseExecutor` is the only entry point; direct `Connection` access is package-private and hidden behind `EventPublisher`, `EventStore`, and the migration runner.
**Cross-module impact:** Every caller that talks to persistence (event-bus publish path, state-store projection path, configuration read path, observability storage path) uses virtual threads as normal and submits work through the persistence API — they do not see the platform-thread boundary. The crucial invariant: **nothing holds a JDBC `Connection` reference across a virtual-thread boundary**. Review any future code that passes `Connection` or `ResultSet` out of persistence.
**Codified in:** AMD-26 + AMD-27 (ratified during Phase 3 prep); `DatabaseExecutor` commit `d24f628` (M2.3); `SqliteEventStore` commit `5279e7a` (M2.5).
**References:** Doc 04 §3 (persistence threading); WAL spike report `d48df13`; `project-manager/references/amendments/AMD-26.md` and `AMD-27.md`.

## 2026-04-10 | D-03 | Persistence module internals are package-private
**Trigger:** M2.2 migration framework design review; ratified as AMD-32 before M2.3.
**Decision:** All implementation classes inside `com.homesynapse.persistence` (`SqliteEventStore`, `DatabaseExecutor`, `MigrationRunner`, `TimeConversion`, `EventCategoryMapping`, `EventPayloadCodec`, `EventTypeRegistry`, `JacksonWarmup`, V001 schema loader, etc.) are **package-private**. The module's `module-info.java` exports only the Phase-2-interface-spec packages (`com.homesynapse.persistence.api` and what the design doc specifies). Production code outside persistence can reach these internals only by going through the exported interfaces.
**Cross-module impact:** Consumers must not `requires transitive com.homesynapse.persistence` for the internal packages — they don't exist on the module graph. Any future wiring of persistence into `PersistenceLifecycle.start()` happens inside the persistence module or inside `app/homesynapse-app` (which owns composition). Tests across module boundaries must go through the public API; reflection-based access into persistence internals is forbidden by ArchUnit rules.
**Codified in:** AMD-32 (ratified pre-M2.3); persistence `module-info.java` in commits `696ac37` (M2.2) and subsequent.
**References:** Doc 04 §2 (exported interfaces); `project-manager/references/amendments/AMD-32.md`.

## 2026-04-11 | D-04 | Clock must be injected everywhere outside the app/platform/test whitelist
**Trigger:** M2.5 arch-debt retrospective — M2.2 `MigrationRunner` used `Instant.now()` and M2.4 `JacksonWarmup` used `System.nanoTime()`. Both failed `./gradlew check` against the `NO_DIRECT_TIME_ACCESS` ArchUnit rule once the gate was finally run.
**Decision:** Every class that reads wall-clock time, monotonic time, or generates time-dependent values **outside** the ArchUnit whitelist (`com.homesynapse.app..`, `com.homesynapse.platform..`, `com.homesynapse.test..`) takes a `java.time.Clock` via constructor injection. Test code in non-whitelisted packages uses `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` and delegates per-test uniqueness to JUnit 5 `@TempDir` or a deterministic counter. `System.nanoTime()` is forbidden outside the whitelist even for benchmarking — use an injected clock or a platform-api timing helper.
**Cross-module impact:** Every Phase 3 module (event-bus, state-store, automation, integration-runtime, observability, rest-api, websocket-api, lifecycle) will hit this rule the moment it writes time-aware code. Constructor signatures must take `Clock`. Records, utility classes with static time reads, and benchmarking fields are the three patterns most likely to trip the rule. The arch rule is the authoritative gate; local unit-test runs do not catch it — only `./gradlew check` at the app module scans the full classpath.
**Codified in:** Arch-debt fix commit `d6a6065` (2026-04-11); retrospective `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`.
**References:** `HomeSynapseArchRules.noDirectTimeAccess`; `coder-lessons.md` 2026-04-10 entry on `NO_DIRECT_TIME_ACCESS`; `InMemoryEventStoreTest` and `SqliteEventStoreTest` as reference implementations.

## 2026-04-10 | D-05 | Every event record and payload-carrying test double carries `@EventType`
**Trigger:** M2.1 + M2.i + M2.5 — the persistence layer needs string-keyed dispatch (per D-01) and the migration-time category table needs to enumerate the full event-type vocabulary.
**Decision:** Every production event record (27 types as of M2.5) and every payload-carrying test double used in contract tests (`TestPayload` in `EventStoreContractTest`) declares `@EventType("<snake_case_name>")` on the type. `EventTypeRegistry.register(...)` is called for each one at composition time. `EventTypeAnnotationTest` enforces the production count; adding a new event type means updating (a) the new `@EventType` annotation, (b) `EventTypeAnnotationTest` expected count, (c) `EventCategoryMapping` static table, and (d) `EventCategoryMappingTest.explicitMappingCount_matchesDocEnumeration`.
**Cross-module impact:** Event-model, persistence, event-bus, state-store, automation, and all integration adapters. Any module that defines a new event record — including integration modules that define integration-namespaced events like `zigbee.device_announce` — must annotate it. Integration-namespaced events that don't appear in `EventCategoryMapping` resolve to the `[SYSTEM]` fallback per INV-PD-07, but their `@EventType` string is still required for registry dispatch.
**Codified in:** M2.1 commit `b2c8b78`; M2.i intermission commit `e9e7827` (IntegrationLifecycleEvent subtypes); M2.5 commit `5279e7a` (TestPayload annotation).
**References:** Doc 01 §4.4 (event vocabulary); `EventTypeRegistry`; `EventCategoryMapping`; depends-on D-01.

## 2026-04-10 | D-06 | V001 schema may be amended pre-launch; no migration file is cut for amendments
**Trigger:** M2.5 — `SqliteEventStore` discovered that `SubjectRef` reconstruction required a `subject_type` column, which was not in the original V001 schema. Added mid-M2.5.
**Decision:** Until launch (2026-11-25), the V001 migration file may be amended in place to add columns, indexes, or constraints. Amendments carry a dated comment header in the V001 SQL file documenting the change. No V002 migration file is cut for pre-launch schema changes — the assumption is that no production data exists, every developer runs a fresh install, and the migration runner re-applies V001 from scratch. **After launch, this rule reverses: any schema change must ship as a new `VNNN_descriptive_name.sql` migration file, and V001 becomes frozen.**
**Cross-module impact:** Any Phase 3 work that needs schema changes (state-store for projection tables, configuration for settings storage, observability for trace storage) follows the same pre-launch-amendable / post-launch-immutable rule for its own `V001_*.sql` files. The `MigrationRunner` has Flyway-style semantics and trusts the V001 file contents — it does **not** detect amendments. Developers must wipe their local `events.db` after pulling a V001 amendment.
**Codified in:** V001 schema amendment 2026-04-10 (subject_type column); M2.2 commit `696ac37` (MigrationRunner); M2.5 commit `5279e7a`.
**References:** Doc 04 §6 (migration strategy); `MigrationRunner` Javadoc; this rule is NOT a Locked Technical Decision — it is an implementation-level policy pending formalization before launch.

## 2026-04-10 | D-07 | Event categories are derived at write time via `EventCategoryMapping`
**Trigger:** M2.5 `SqliteEventStore` implementation — the caller's `DomainEvent` draft does not carry category information, but the `events` table column `categories` (CSV) must be populated.
**Decision:** `EventCategoryMapping.categoriesFor(eventType)` is a compile-time `Map.ofEntries` covering all 27 production event types per Doc 01 §4.4, with `[SYSTEM]` as the fallback for unknown or integration-namespaced types per INV-PD-07. `SqliteEventStore.publish()` calls this mapping at write time and persists the result. Categories are **not** part of the `DomainEvent` envelope or the `@EventType` annotation; they are derived metadata. The CSV encoding uses plain `","` with no escaping, which is safe because all `EventCategory` values are ASCII-only `UPPER_SNAKE_CASE` identifiers. Any future category value containing punctuation breaks this encoding silently and must be preceded by a switch to length-prefixed or JSON-array encoding.
**Cross-module impact:** Event-bus subscribers that filter by category, state-store projections keyed by category, observability category dashboards, and any future reporting or analytics surface — all read the `categories` column as source of truth and do **not** re-derive from event-type. Adding a new event type requires adding an entry to `EventCategoryMapping` *before* the first event of that type is published, or it will be silently persisted as `[SYSTEM]`.
**Codified in:** M2.5 commit `5279e7a` (`EventCategoryMapping` + `EventCategoryMappingTest`); persistence MODULE_CONTEXT.md gotcha on CSV encoding.
**References:** Doc 01 §4.4 (event vocabulary and category assignment); INV-PD-07 (integration-namespaced fallback); depends-on D-05.

## 2026-05-20 | D-08 | Visibility promotion requires transitive `-Xlint:exports` verification (DEC-M3-17)
**Trigger:** M3.6d-a discovered during execution that `QueueSaturationHealthCheck`'s public-promotion (authorized by DEC-M3-16) could not ship in isolation: the constructor's `Consumer<HealthSignal>` parameter chain leaks both `HealthSignal` (record) and `HealthLevel` (enum), both of which were package-private. Promoting only the class would have failed `-Xlint:exports` (errors under `-Werror`).
**Decision:** Every cross-module visibility promotion in `core/*` must verify transitive accessibility before authorization. The minimum-viable promotion unit is the full type closure reachable through public constructor parameters, public method signatures, public field types, and public return types — not just the class being promoted. In M3.6d-a, this translated to a 3-type promotion (QueueSaturationHealthCheck + HealthSignal + HealthLevel) instead of the brief's 1-type promotion. Recorded as **DEC-M3-17** in the M3 Phase 3 Locked Decisions ledger (DEC-M3-16 addendum). Pre-promotion checklist: list every type appearing in the candidate's public constructor signatures, public method signatures, public field types, and return types; for each, confirm the type itself is already public; if any are package-private, the promotion expands to the full closure or the brief must use a factory pattern instead.
**Cross-module impact:** Every future visibility promotion in `core/*` (especially M3.6d-b's `SqlitePersistenceLifecycle` factory and any subsequent M4+ subsystem promotion). The factory-pattern alternative — keeping the impl class package-private and exposing only a `Public Factory.create(...)` returning an interface — is the right move when the public closure would expand uncomfortably (DEC-M3-16's plan for SqlitePersistenceLifecycle). The 3-type chain in M3.6d-a was acceptable because `HealthSignal` and `HealthLevel` are stable, semantically meaningful types that downstream consumers (observability, M3.6e MaterializedStateQueryService) will reasonably reach for.
**Codified in:** M3.6d-a commit `25bc23b` (2026-05-20); DEC-M3-17 entry in `HomeSynapse_Current_State.md` §3 and `HomeSynapse_Core_Locked_Decisions.md` §16; coder-lessons.md M3.6d-a entry #1.
**References:** DEC-M3-16 (M3.6b 2026-05-20, `df2743a`) — the parent decision that authorized the composition-root visibility strategy. JLS §6.6 on accessibility. `-Xlint:exports` documentation. Java module-info `exports` semantics.

## 2026-05-22 | D-09 | M3.7 closes OR-M3-17/OR-M3-18 with `MinimalProjectionAdvancer`, not `DispatchingProjectionAdvancer`
**Trigger:** M3.7 coding-instruction scoping session (Cowork PM, 2026-05-22). The two `NO_OP_*` placeholders in `HomeSynapseCore` step 5 (OR-M3-17 `NO_OP_DERIVATION`, OR-M3-18 `NO_OP_ADVANCER`) must be resolved before M3.7 can exercise the projection pipeline end-to-end. Two candidate closures: (a) `MinimalProjectionAdvancer` per Research 3 REC-20 — bounded-window read forwarding every envelope to the processor, with a trivial empty-list derivation rule; (b) the real `DispatchingProjectionAdvancer` per Research 8 REC-28 — per-event-type dispatch via the `@EventType` registry, which requires the M4-amendment-deliberation window to close.
**Decision:** M3.7 ships with `MinimalProjectionAdvancer` (package-private final class in `lifecycle/lifecycle`, constructed by `HomeSynapseCore`, reads from `EventStore.readFrom(fromPosition, Math.min(maxRows, 500))` and forwards every envelope to the processor callback). `NO_OP_DERIVATION` is renamed to `MINIMAL_DERIVATION_RULE` (the empty-list path IS the M3.7 closure semantic — full derivation logic lands when `state_changed` derivation is wired per DEC-M3-10). The full M4.0 replacement (Research 8 REC-28's `DispatchingProjectionAdvancer`) is explicitly OUT OF SCOPE for M3.7. OR-M3-17 and OR-M3-18 close at M3.7 commit; OR-M3-18 remains open as a forward pointer to M4.0 only if Nick re-opens it for the dispatching variant.
**Cross-module impact:** `lifecycle/lifecycle` gains one new package-private type (`MinimalProjectionAdvancer`) and modifies `HomeSynapseCore` step 5 to consume it. No state-store or persistence changes — the advancer is a composition-root concern. Future M4.0 work will replace `MinimalProjectionAdvancer` with `DispatchingProjectionAdvancer` (likely a sibling file in the same package, with the composition root flipping the field). The M3.7 → M4.0 cutover is a single-line change in `HomeSynapseCore.start()`.
**Codified in:** `context/instructions/M3.7_E2E_Integration_Tests.md` (this session's coding instruction); pending M3.7 commit (TBD by Coder).
**References:** Research 3 PM Assessment REC-20 (the M3.7-scoped minimal advancer); Research 8 v2 PM Assessment §M3.7 Impact ("M3.7 proceeds as planned with `MinimalProjectionAdvancer`; OR-M3-17 stays open through M3.7; closes at M4.0 with REC-28") and REC-28 (the M4.0 dispatching variant); OR-M3-17 + OR-M3-18 entries in `pm-handoff.md`; `HomeSynapseCore.java` lines 152/170/261-269.

## 2026-05-22 | D-10 | M3.7 absorbs M3.6f-shaped pre-work (HTTP IT for endpoints + DLQ `oldestParkedAt`)
**Trigger:** M3.7 coding-instruction scoping. Two optional pre-M3.7 follow-ups surfaced from M3.6e.2: (a) real-Jetty HTTP integration tests for the five M3.6e.2 endpoints (currently tested only through `RecordingEndpointContext` stub), and (b) `oldestParkedAt` field plumbing in `SubscriberDlq` (closes M3.6e.2 D-2 deviation where `DlqStatusEndpoint` had to omit the field). Two options: (a) split as a separate pre-M3.7 closeout WU (M3.6f); (b) absorb into M3.7 as the first scenarios + a small internal extension.
**Decision:** Both follow-ups are absorbed into M3.7. The HTTP IT for the five M3.6e.2 endpoints (`/api/v1/entities`, `/api/v1/entities/{id}`, `/api/v1/entities/{id}/state`, `/internal/dlq`, `/internal/projection`) is exactly what `HomeSynapseE2eHarness` (Research 3 REC-16) exists to do — it would be artificial to split it into a separate WU. The DLQ field plumbing is a tiny delta (one `Instant parkedAt` field on `DlqEntry`, one `Clock` injection into `SubscriberDlq`, one new `oldestParkedAt()` accessor, one 6th field `oldestParkedAt: Instant` on `SubscriberSnapshot`, one response-shape extension in `DlqStatusEndpoint`) that fits naturally into M3.7's scope. No M3.6f WU is created.
**Cross-module impact:** `core/event-bus` gains a 6th `SubscriberSnapshot` field (5→6), a `Clock`-aware `SubscriberDlq` constructor (signature change), and an extended `DlqEntry` nested record. `api/rest-api` extends `DlqStatusEndpoint`'s response shape (adds `oldestParkedAt` per response entry). `lifecycle/lifecycle`'s `InProcessEventBus` wiring passes the bus's `Clock` to `SubscriberDlq`. Production consumers of `EventBus.subscribers() → List<SubscriberSnapshot>` see a non-null new field — backward-incompatible at the record level (any prior code unpacking the snapshot will need recompilation; no such code exists outside the bus module today).
**Codified in:** `context/instructions/M3.7_E2E_Integration_Tests.md`; pending M3.7 commit.
**References:** M3.6e.2 D-2 deviation in `coder-handoff.md`; `SubscriberDlq.java` source; M3.6e.2 brief's "Coder Pushback Welcome" section which invited the omission; the integration-tests harness pattern from M3.4a/M3.4b.

## 2026-05-22 | D-11 | M3.7 proceeds in parallel with M4-amendment-deliberation window (zero technical coupling)
**Trigger:** The pm-handoff Next Tasks #6 framing prior to this session gated M3.7 on "after the M4 amendment-deliberation window closes." That window covers Research 4 DQ-1/2/3/5, Research 6 NQ-1..6, and Research 5 REC-56 (deferred on Research 6 REC-41). Each is pending Nick strategic decision. The conservative framing implied that any of them might affect M3.7. A technical-coupling audit during the M3.7 scoping session found zero overlap.
**Decision:** M3.7 is decoupled from the M4-amendment-deliberation window. The gate is removed from pm-handoff Next Tasks #6. Audit findings: (1) M3.7 exercises the M3 stack (persistence + event-bus + state-store + lifecycle + rest-api endpoints already shipped through M3.6e.2). (2) None of the pending M4 amendments change anything M3.7 touches — Research 4 is automation-engine (M7), Research 6 is integration-runtime (M9), Research 5 is configuration (M6); all are M4+ subsystems. (3) The only M4-shaped dependency is `DispatchingProjectionAdvancer` (Research 8 REC-28), which Decision D-09 explicitly defers to M4.0. (4) `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` already aggregates the 22 core event types — no new event types pending in the amendment window would affect M3.7's test scenarios. M3.7 proceeds immediately; M4-amendment work continues on its own track.
**Cross-module impact:** Process-only — affects scheduling, not source. Future PM sessions can read this decision when deciding whether subsequent milestones similarly decouple from pending amendment work — the right question is always "does the amendment change a type, contract, or behavior this milestone touches?" not "is there an amendment in flight?"
**Codified in:** pm-handoff.md Next Tasks #6 update (this session); `context/instructions/M3.7_E2E_Integration_Tests.md` (the absence of any M4-amendment dependency in the brief is the deliverable).
**References:** Research 4 v3 PM Assessment (DQ-1/2/3/5 open); Research 6 v1 PM Assessment (NQ-1..6 open); Research 5 v2 PM Assessment (REC-56 deferred on Research 6 REC-41); Research 8 v2 PM Assessment §M3.7 Impact (independent confirmation that M3.7 is unblocked).

## 2026-05-22 | D-12 | M3.7 uses the established M3.6 Claude Code workflow (no protocol changes)
**Trigger:** M3.7 coding-instruction scoping session needed to confirm the execution workflow before issuing the instruction.
**Decision:** M3.7 executes via the same workflow used for the seventeen M3.6 sub-WUs (M3.6a through M3.6e.2): Claude Code in `acceptEdits` mode, Opus 4.7 xhigh, deny `git commit` / `git push` / `./gradlew` per the standing project CLAUDE.md. PM-generated coding instruction → Claude Code executes (writes files only; no build, no test, no commit) → Nick reviews diff via `git status` / `git diff` → Nick runs `./gradlew check` externally → Nick commits if GREEN → PM runs WUCP Phase 2. The Coder does NOT run the build gate; that's Nick's job. The Completion Report flags any build-gate-relevant concerns (e.g., expected `./gradlew check` commands) under a `Deferred Build Gate` section in `coder-handoff.md`.
**Cross-module impact:** Process-only. Codifies the M3.6 cadence as the default for all remaining M3 + M4 + future milestones. Any deviation (e.g., a milestone needing on-device validation per the M3.4b Pi-profile pattern) is an exception that requires explicit PM authorization in the instruction.
**Codified in:** `context/instructions/M3.7_E2E_Integration_Tests.md` (Build Discipline section); pm-handoff Next Tasks #6 update.
**References:** Seventeen M3.6 Claude Code WUs (May 17 – May 22, 2026) — see Project Snapshot Recent Session Log; project CLAUDE.md standing policy; M3.6e.1 "two fix rounds" precedent (the Coder produced corrective patches without running gradlew).

---

## How to add an entry

1. Assign the next available `D-NN` number (append-only, never renumber).
2. Use the entry format above. Be specific about cross-module impact — vague impact statements are the enemy of this file's usefulness.
3. Update the relevant MODULE_CONTEXT.md files with a pointer to the decision: `See `context/decisions/phase-3-cross-module-decisions.md` D-NN`.
4. If the decision originated from an audit or retrospective, link the audit file.
5. If the decision raises the bar for an architecture invariant, consider whether an AMD is also required — decisions here cannot override LDDs.

---

**Last verified against:** `homesynapse-core` commit `76288af` on `2026-05-22`.

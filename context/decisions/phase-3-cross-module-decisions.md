# Phase 3 Cross-Module Decisions

Running register of decisions made during Phase 3 implementation that cross module boundaries or reshape a Locked Design Document contract in a way that other modules' implementors need to know. These are **not** amendments to Locked Design Documents (those go through the AMD process) — they are implementation-level decisions that materially affect how downstream modules will be written.

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

---

## How to add an entry

1. Assign the next available `D-NN` number (append-only, never renumber).
2. Use the entry format above. Be specific about cross-module impact — vague impact statements are the enemy of this file's usefulness.
3. Update the relevant MODULE_CONTEXT.md files with a pointer to the decision: `See `context/decisions/phase-3-cross-module-decisions.md` D-NN`.
4. If the decision originated from an audit or retrospective, link the audit file.
5. If the decision raises the bar for an architecture invariant, consider whether an AMD is also required — decisions here cannot override LDDs.

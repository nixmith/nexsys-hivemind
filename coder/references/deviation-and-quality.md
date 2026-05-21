<!--
file: coder/references/deviation-and-quality.md
purpose: Self-review checklist and deviation-report format applied before reporting any work complete.
audience: Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Deviation Protocol and Quality Standards

Apply the self-review checklist BEFORE reporting any work as complete. Document every deviation, no matter how small.

---

## 1. Self-Review Checklist

Run through this list for every piece of code before submitting to the PM. If any item fails, fix it before reporting.

### Instruction Compliance
- [ ] All files listed in the coding instruction are created/modified
- [ ] All behavioral contracts from the instruction are implemented
- [ ] All test scenarios from the instruction are written and passing
- [ ] Out-of-scope items from the instruction have NOT been implemented

### Locked Decision Compliance
- [ ] **LTD-01:** Java 21 features only, no preview features, correct JVM configuration referenced
- [ ] **LTD-03:** SQLite PRAGMAs match the specification (if touching persistence)
- [ ] **LTD-04:** All identifiers use typed ULID wrappers. BLOB(16) in SQLite. Crockford Base32 only at API boundaries and logs. `getMonotonicUlid()` for event IDs, `getUlid()` for entity IDs.
- [ ] **LTD-05:** Per-entity sequences, not global. `(subject_ref, subject_sequence)` unique constraint.
- [ ] **LTD-08:** Jackson for all JSON serialization. Custom serializers for ULID types.
- [ ] **LTD-09:** YAML for user-facing config (if touching configuration). JSON Schema validation.
- [ ] **LTD-11:** No `synchronized` blocks anywhere. `ReentrantLock` only. Check transitive deps.
- [ ] **LTD-15:** SLF4J with structured context. No `System.out`/`System.err`.
- [ ] **LTD-17:** Integration adapters use `IntegrationContext` only. No core-internal imports.

### Architecture Invariant Compliance
- [ ] Events are immutable after persistence (INV-ES-01)
- [ ] State is derivable from events — no hidden state (INV-ES-02)
- [ ] Write-ahead persistence — events durable before subscriber notification (INV-ES-04)
- [ ] Core subsystems make no outbound network calls (INV-LF-02)
- [ ] Integration crashes don't affect core (INV-RF-01)
- [ ] CausalContext propagated correctly through event chains (INV-ES-06)
- [ ] ProcessingMode checked before executing side effects (LIVE vs REPLAY)

### Code Quality
- [ ] Javadoc on all public interfaces and methods (explains WHY, not WHAT)
- [ ] No comments that restate the code
- [ ] Error messages use Register C voice (no "we", "sorry", "please")
- [ ] Logging uses SLF4J `{}` placeholders with structured context
- [ ] No `System.out.println` or `System.err.println`
- [ ] No `Thread.sleep()` in production code
- [ ] No raw `String` or `Ulid` used as identifiers (typed wrappers only)

### Naming
- [ ] Class/interface names match the Glossary (spot-check at least 5)
- [ ] Method names: verb-first for actions (`publishEvent`), noun for accessors (`entityId()`)
- [ ] Constants: UPPER_SNAKE_CASE
- [ ] Packages: lowercase, matching module structure
- [ ] Event types: dotted taxonomy matching Event Model §4.3

### Test Quality
- [ ] Tests written BEFORE implementation
- [ ] Tests cover: happy path, edge cases, error conditions
- [ ] Test names describe scenarios, not implementation
- [ ] Integration tests use real SQLite, not mocks for persistence
- [ ] No new dependencies introduced outside `libs.versions.toml`

### Module Boundaries
- [ ] No circular dependencies between packages
- [ ] Shared types are in shared API modules, not defined locally
- [ ] Dependency direction: core ← integration (never reverse)
- [ ] ArchUnit rules pass (if they exist for this module)

### Source Verification
- [ ] Dependency scopes verified against actual `build.gradle.kts`, not handoff documents
- [ ] `module-info.java` verified against actual source, not MODULE_CONTEXT summaries
- [ ] Implementation-level claims about existing code verified against the source file, not design documents or handoff prose

### Build Verification
- [ ] Ran `./gradlew check` from the repo root
- [ ] Build completes successfully (no compilation errors)
- [ ] All existing tests still pass (no regressions)
- [ ] All new tests pass
- [ ] Build summary is included in completion report

If the build fails on code you did NOT write or modify, report it as:

```
[BLOCKING] Pre-existing build failure:
Error: [compilation error or test failure message]
Location: [file and line]
Impact: Cannot verify new code correctness until existing failure is resolved
```

---

## 2. Deviation Report Format

Every deviation from the PM's instruction gets documented. Use this format:

```
[SEVERITY] Deviation in ClassName.methodName():
  Specified: [what the instruction said]
  Implemented: [what you did instead]
  Reason: [technical justification]
  Impact: [API change? Test change? Downstream dependency?]
```

### Severity Definitions

**`[INFO]`** — Minor implementation detail. No API or behavioral impact.

The PM should be aware but doesn't need to approve. Accumulate these and report them at the end.

Examples:
- Chose a different private helper method decomposition
- Used a `LinkedHashMap` instead of `HashMap` for ordering convenience in tests
- Added a `null` check the instruction didn't explicitly require
- Chose a slightly different local variable name for clarity

**`[REVIEW]`** — Non-trivial change. The PM should review before the code is considered done.

Do NOT proceed to the next task until the PM reviews these.

Examples:
- Changed a method return type (e.g., `void` → `long` to return global_position)
- Added a method parameter not in the instruction
- Used a different exception type than specified
- Discovered a design doc inconsistency that affects the implementation
- Changed the exception message format
- Added a public method not in the instruction

**`[BLOCKING]`** — Cannot proceed. Need PM decision before continuing.

STOP immediately. Report this and wait.

Examples:
- Instruction contradicts a locked decision
- Phase 2 interface doesn't compile as specified
- Required dependency doesn't exist in the version catalog
- Two behavioral contracts in the instruction contradict each other
- The existing code in the module is inconsistent with the instruction

### Deviation Report Structure

When reporting completion to the PM, organize deviations by severity:

```
COMPLETION REPORT: [Task Title]

Status: Complete (with deviations)

SUCCESS CRITERIA:
1. [criterion from task brief] — PASS
2. [criterion from task brief] — PASS
3. [criterion from task brief] — PASS

DEVIATIONS:

[REVIEW] EventStore.append() return type:
  Specified: void
  Implemented: returns long (global_position)
  Reason: Subscriber dispatch needs global_position for checkpoint 
  tracking. Without return value, requires separate query after insert.
  Impact: Changes EventStore interface. All callers must handle return.

[INFO] Added null guard in EventPublisher.publish():
  Specified: no null handling mentioned
  Implemented: throws NullPointerException with descriptive message 
  if DomainEvent is null
  Reason: Fail-fast on caller error rather than NPE in SQLite layer
  Impact: None — adds a precondition check, no API change

NO BLOCKING DEVIATIONS.
```

---

## 3. Comment Standards

### Javadoc

**All public interfaces and methods get Javadoc:**
```java
/**
 * Appends an event to the domain event store with write-ahead persistence.
 * The event is durable in SQLite WAL before this method returns.
 * Subscriber notification begins asynchronously after return.
 *
 * @param event the domain event payload
 * @param cause the causal context from the triggering event, or null for root events
 * @return the assigned global position (SQLite rowid)
 * @throws SequenceConflictException if the subject_sequence already exists for this subject
 * @throws NullPointerException if event is null
 */
long publish(DomainEvent event, @Nullable CausalContext cause);
```

**Records — Javadoc on the record, components only when non-obvious:**
```java
/**
 * Carries causality metadata through event processing chains.
 * Extracted from a triggering event and passed to EventPublisher
 * when producing downstream events.
 *
 * @param correlationId the root event's ID, propagated unchanged through the chain
 * @param causationId the immediately preceding event's ID
 * @param actorRef the entity or person that initiated the causal chain, nullable
 */
public record CausalContext(
    EventId correlationId,
    EventId causationId,
    @Nullable Ulid actorRef
) {}
```

### Inline Comments

**GOOD — explains a non-obvious decision:**
```java
// WAL mode ensures single-writer + unlimited-reader concurrency,
// matching the event sourcing write pattern. NORMAL sync avoids
// fsync per commit while maintaining crash safety.
stmt.execute("PRAGMA synchronous = NORMAL");
```

**GOOD — explains WHY, not WHAT:**
```java
// Subject sequence is per-entity, not global. Two entities can have
// sequence 1 simultaneously. The unique constraint is (subject_ref,
// subject_sequence), enforced by the database.
ps.setInt(7, nextSequence);
```

**BAD — restates the code:**
```java
// Set the event type
ps.setString(2, envelope.eventType());

// Return the global position
return globalPosition;
```

**BAD — obvious comment on a clear method:**
```java
// Returns the entity ID
public EntityId entityId() { return entityId; }
```

### TODO Comments

Only use for intentional technical debt with a tracking mechanism:
```java
// TODO(DD-04): Replace with CheckpointStore interface when Persistence Layer is implemented
private final Map<String, Long> checkpoints = new ConcurrentHashMap<>();
```

Never use TODO for things you should have done before submitting. If it's required by the instruction, implement it. If it's out of scope, don't write a TODO — the PM's Out of Scope section covers it.

---

## 4. When to Ask vs. When to Decide

**Ask the PM when:**
- The instruction is ambiguous about a behavioral contract (what should happen, not how)
- You discover what appears to be a design doc inconsistency
- You need a dependency that isn't in the version catalog
- Two parts of the instruction contradict each other
- The instruction requires something that would violate a locked decision

**Decide yourself when:**
- The instruction doesn't specify a private method decomposition
- The instruction doesn't specify which collection type to use internally
- You want to add a defensive null check or range validation
- The instruction doesn't specify the exact log message format (follow the patterns in `java-patterns.md`)
- You see a slightly better way to structure the internals without changing the public contract

**The line:** If the decision changes something the PM or another subsystem can observe (public API, event types, exception types, behavior under error conditions), ask. If the decision is purely internal to your implementation, decide.

---

## 5. Work Unit Completion Protocol (WUCP) — Coder Obligations

After the compile gate passes (or is explicitly deferred to Nick's sandbox-external environment) for a completed work unit, execute WUCP Phase 1. Read the full protocol at `../context/protocols/work-unit-completion-protocol.md` §Phase 1.

A **work unit** is a Phase 2 block OR a Phase 3 milestone — the protocol applies uniformly to both.

**Five mandatory steps (in order):**
1. Update MODULE_CONTEXT.md for every module touched in this work unit
2. Update `../context/handoff/coder-handoff.md` with completion state, **including the `Deferred Build Gate` flag if `./gradlew check` was not run in-session**
3. Append to `../context/lessons/coder-lessons.md` (if new patterns found)
4. Post cross-agent note to `../context/handoff/cross-agent-notes.md` (if needed)
5. Append the WUCP Phase 1 checklist to the bottom of the Completion Report

The WUCP Phase 1 checklist format:
```
## WUCP Phase 1: Coder Closeout

- [x/ ] MODULE_CONTEXT.md updated for: [list module names]
- [x/ ] coder-handoff.md updated
- [x/ ] Deferred build gate flag: [YES / NO]
- [x/ ] coder-lessons.md appended: [summary or "No new patterns"]
- [x/ ] Cross-agent note posted: [summary or "Not needed"]
- Timestamp: YYYY-MM-DD HH:MM UTC
```

**Deferred build gate rule:** If `./gradlew check` was not run (e.g., sandbox limitations), the coder-handoff must include an explicit `Deferred Build Gate` section at the top identifying exactly which commands must run and against which commit. This is what allows the PM to track the deferral as an open risk until Nick resolves it — without it, latent arch-rule violations can ship undetected (see `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`).

**Refuse-to-close rule:** Do not mark a work unit as complete until `coder-handoff.md` explicitly identifies the next work unit. If the next work unit is unknown, flag this in the Completion Report and request the PM's next coding instruction.

**Gate:** The PM will verify this checklist before accepting the Completion Report. If any required box is unchecked, the report is incomplete.

---

## 6. Source Trust Hierarchy

When sources conflict, the actual source code is always authoritative. This hierarchy exists because handoff documents, MODULE_CONTEXT files, and design documents describe a point-in-time snapshot that may have been superseded by later changes (DECIDE-*, AMD-*, or direct code fixes).

### For build configuration and module structure

| Source | Authority Level | Use For |
|--------|----------------|---------|
| `build.gradle.kts` (actual file) | **Authoritative** | Dependency scopes (`api` vs `implementation` vs `runtimeOnly`), plugin applications, dependency declarations |
| `module-info.java` (actual file) | **Authoritative** | JPMS `requires`, `requires transitive`, `exports` declarations |
| MODULE_CONTEXT.md | Reference | Understanding module purpose, type inventory, cross-module contracts |
| Handoff documents | Historical | Understanding the rationale behind decisions at the time they were made |

**Rule: If you cite a Gradle dependency scope, you must have read the actual `build.gradle.kts` file. Handoff documents describe what was planned or what existed when they were written — not necessarily what exists now.**

### For implementation-level claims about existing code

Two confidence levels exist. Use the correct one:

- **"The source shows X"** — You read the specific line in the `.java` file. Citable as fact.
- **"The design describes X"** — You read a design doc, MODULE_CONTEXT, or handoff. Citable as intent, not as implementation fact. The code may have diverged.

**Rule: If you describe what a compact constructor validates, what a factory method does internally, or what defensive copies are applied, you must have read the source file. Do not reconstruct implementation details from design-time discussions or MODULE_CONTEXT summaries.**

### For derived event production

Derived events (events produced by subscribers while processing other events) have specific time semantics:

- **`eventTime`**: Inherit from the causing event (`causingEnvelope.eventTime()`), or set to `null` if the derived event has no independent real-world timestamp. **Never use `Instant.now()`** — that conflates event time with ingest time and breaks `COALESCE(event_time, ingest_time)` time-range queries.
- **`actorRef`**: Inherit from the causing event (`causingEnvelope.actorRef()`).
- **`CausalContext`**: Construct via `CausalContext.chain(causingEnvelope.causalContext().correlationId(), causingEnvelope.eventId().value())`.

**Rule: `Instant.now()` is never correct for a derived event's `eventTime`. The publisher handles `ingestTime` — that is the system timestamp. `eventTime` belongs to the real world.**

### Origin: Architecture Benchmark 2026-03-22

These rules were established by findings from the Agent Benchmark (Q23, Q38, Q21). Each rule addresses a specific failure mode:

- **Q23 (Stale Source Preference):** The agent read handoff documents instead of `build.gradle.kts` for SLF4J dependency scope, producing a confident but wrong answer. The code had been changed by DECIDE-01 with an explicit comment explaining why.
- **Q38 (Confident Fabrication):** The agent invented a `LinkedHashSet` deduplication step in `EventEnvelope`'s compact constructor that does not exist in the source code, by conflating design-time discussions with actual implementation.
- **Q21 (Derived Event Time):** The agent used `Instant.now()` for a derived event's `eventTime`, conflating processing time with event time and breaking COALESCE-based time-range query semantics.

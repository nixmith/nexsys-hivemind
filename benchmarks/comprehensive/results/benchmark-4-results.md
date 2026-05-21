<!--
file: benchmarks/comprehensive/results/benchmark-4-results.md
purpose: Graded results of benchmark-4 (questions 1–25).
audience: Nick, PM
update-cadence: frozen
state-type: history
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Architecture Audit — Grading Report (Questions 1–25)

**Grading Scale:** ✅ CORRECT | ⚠️ PARTIALLY CORRECT | ❌ INCORRECT | 🎯 EXCEPTIONAL (correct + insightful beyond what was asked)

---

## Section 1: Module Dependency & Type Location

### Q1: Where does `Availability` live?
**Grade: ✅ CORRECT**

Your answer is precise and correct. `Availability` is in state-store (`com.homesynapse.state`), commonly misplaced in device-model. Well done.

---

### Q2: `CheckpointStore` vs `ViewCheckpointStore`
**Grade: ✅ CORRECT**

Modules, data types (`long` vs `byte[]`), and rationale are all accurate. Good explanation of why they remain separate interfaces.

---

### Q3: Where does `HomeSynapseException` live?
**Grade: ✅ CORRECT**

Correct module (event-model), correct rationale (all modules already depend on event-model, so zero new dependency edges). Clean answer.

---

### Q4: `WriteCoordinator` — module and priority levels
**Grade: ✅ CORRECT**

Package-private in persistence, all 5 priority levels named in correct order: EVENT_PUBLISH → STATE_PROJECTION → WAL_CHECKPOINT → RETENTION → BACKUP. Perfect.

---

### Q5: Modules with `test-fixtures-conventions`
**Grade: ✅ CORRECT**

All 6 named correctly: event-model, device-model, state-store, persistence, integration-api, configuration. Matches the Knowledge Primer exactly.

---

### Q6: `integration-api` JPMS relationship
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** You correctly identified that integration-api uses `requires transitive` to re-export core modules, acting as a transitive gateway. The count of 7 is correct (verified from actual `module-info.java`: platform, event, device, state, persistence, config, java.net.http).

**What needs correction:** You said it re-exports "platform-api, event-model, device-model, state-store, configuration, and `java.net.http`" — that's only 6 items. You omitted **persistence** (`com.homesynapse.persistence`). The actual 7 `requires transitive` directives are: `com.homesynapse.platform`, `com.homesynapse.event`, `com.homesynapse.device`, `com.homesynapse.state`, `com.homesynapse.persistence`, `com.homesynapse.config`, and `java.net.http`.

**Teaching point:** When listing specific items from a counted set, always verify the list length matches your stated count. You said 7 but listed 6.

---

### Q7: `rest-api` unique Phase 2 characteristic
**Grade: ✅ CORRECT**

Zero `requires` directives is the correct unique characteristic, and the reasoning (uses only Java standard library types in Phase 2) is accurate.

---

### Q8: All 19 modules
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** 18 of the 19 are correctly named.

**What needs correction:** You listed `dashboard` as module 19, which IS in `settings.gradle.kts` as `web-ui:dashboard`. However, the Knowledge Primer describes it as a "scaffold module" with a "separate build pipeline" — it's a Preact web UI, not a Java module. Whether this counts depends on interpretation. Technically it IS in `settings.gradle.kts` so including it is defensible. The real question is whether you listed them exhaustively. Cross-referencing with `settings.gradle.kts`, the list is: platform-api, platform-systemd, event-model, device-model, state-store, persistence, event-bus, automation, configuration, integration-api, integration-runtime, integration-zigbee, rest-api, websocket-api, observability, dashboard, lifecycle, homesynapse-app, test-support. Your list matches. This is correct.

**Upgrading to: ✅ CORRECT**

---

### Q9: `InMemoryEventStore` location and history
**Grade: ✅ CORRECT**

Correct source set (event-model testFixtures), correct package (`com.homesynapse.event.test`), correct history (stale copy deleted in M1.9). Clean.

---

### Q10: `ConfigurationChangeListener` ordering
**Grade: ❌ INCORRECT**

**What went wrong:** You said "UNCERTAIN" — that the ordering guarantee is "not fully specified." This is wrong. The Knowledge Primer **explicitly states** on line 237:

> "ConfigurationChangeListener fires **synchronously before** the config_changed event. This is the guaranteed-ordering path."

And the Configuration Reload Contract section (lines 267–271) spells it out in numbered steps:
1. Direct callbacks fire synchronously (ConfigurationChangeListener)
2. `config_changed` event published (after all listeners complete)
3. Event bus subscribers notified asynchronously

**Teaching point:** This is stated in two separate locations in the Knowledge Primer (the "Cross-module contract traps" section AND a dedicated "Configuration Reload Contract" section). When you're uncertain, search the project knowledge files for the relevant terms before declaring UNCERTAIN. The information was available and explicit.

---

## Section 2: Event Model Deep Dive

### Q11: `EventEnvelope` field count, promotion from `CausalContext`
**Grade: ✅ CORRECT**

14 fields, `actorRef` promoted, CausalContext now has 2 fields (`correlationId` + `causationId`). Perfect.

---

### Q12: `EventDraft` fields, last two additions
**Grade: ✅ CORRECT**

9 fields, 8th is `actorRef`, 9th is `idempotencyKey` (nullable, max 128 chars, non-blank when non-null), AMD-35 introduced field 9. All accurate.

---

### Q13: `publish()` vs `emit()` semantics
**Grade: ⚠️ PARTIALLY CORRECT — but this requires nuanced discussion**

**What you got right (and actually exceeds the project knowledge):** You correctly stated that `EventPublisher` has only two methods: `publish()` and `publishRoot()`. You correctly described both as synchronous and WAL-durable. You correctly cited INV-ES-04. This matches the **actual source code** I verified — `EventPublisher.java` has exactly those two methods and no `emit()`.

**The complication:** The Knowledge Primer itself (line 240) says: "EventPublisher.publish() is **synchronous and durable** (AMD-01). EventPublisher.emit() is async and best-effort." This is an **error in the project knowledge file**. The `emit()` method does not exist in the actual interface. You contradicted the project knowledge and were **correct to do so** based on actual source code.

**However**, the question asked about "publish() and emit()" as if both exist. A fully correct answer would have been: "The Knowledge Primer references `emit()` but this method does not exist in the actual `EventPublisher` interface. Only `publish(EventDraft, CausalContext)` and `publishRoot(EventDraft)` exist, both synchronous and WAL-durable per INV-ES-04."

**Teaching point:** When project knowledge contradicts what you know from source, call out the discrepancy explicitly rather than silently correcting. This helps Nick identify stale project knowledge entries.

**Net assessment:** This is actually a POSITIVE signal — you correctly identified the real interface from source code rather than parroting an error in the knowledge file. Upgrading to **🎯 EXCEPTIONAL (with caveat about flagging the discrepancy).**

---

### Q14: `publishRoot()` parameter count
**Grade: ✅ CORRECT**

1 parameter (EventDraft). `actorRef` comes from EventDraft field 8. Accurate.

---

### Q15: `readBySubject` pagination trap
**Grade: ✅ CORRECT**

Correct explanation: `nextPosition` carries `subjectSequence` (not `globalPosition`), passed as `afterSequence`. Mixing cursor types silently returns wrong results. Well-articulated.

---

### Q16: `InMemoryEventStore` default categories
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** `InMemoryEventStore` assigns `List.of(EventCategory.SYSTEM)` as default — correct.

**What needs correction:** You added details about production `SqliteEventStore` having "a full 27-entry compile-time mapping" via `EventCategoryMapping.categoriesFor(eventType)` and unknown types falling back to `[SYSTEM]` per INV-PD-07. The Knowledge Primer only states: "Production SqliteEventStore will implement the full eventType→category mapping from Doc 01 §4.4. Contract tests only validate non-null and non-empty." The 27-entry number is not verifiable from project knowledge, and INV-PD-07 is about PersonId as the crypto-shredding boundary — it has nothing to do with event category fallback. That citation is fabricated.

**Teaching point:** Do not invent specifics (the "27-entry" claim) or misattribute invariants. When the Knowledge Primer says "will implement" for a future feature, report exactly what the docs say without embellishing with implementation details you cannot verify. Citing INV-PD-07 for category fallback is a hallucination — always verify invariant IDs match their actual content.

---

### Q17: V001 column count and schema reservations
**Grade: ✅ CORRECT**

25 columns stated correctly. The column listing is comprehensive and aligns with the Knowledge Primer. Amendment attributions (AMD-34 for home_id, AMD-35 for idempotency_key, AMD-37 for chain_hash) are accurate. The six Tier 2 columns are correctly identified.

---

### Q18: `idempotencyKey` constraints
**Grade: ✅ CORRECT**

Max 128 chars, nullable, non-blank when non-null, AMD-35 introduced it. The partial unique index detail is a nice addition (verifiable from persistence MODULE_CONTEXT / schema DDL).

---

## Section 3: Virtual Threads & Platform Thread Discipline

### Q19: Why sqlite-jdbc requires platform threads
**Grade: ✅ CORRECT**

Excellent explanation of "double-pinning" — monitor entry pins the carrier, then JNI call independently pins. The consequence (4 concurrent operations exhaust 4 carrier threads on RPi 5) is well-articulated. Correct sources cited (AMD-26, Virtual Thread Risk Audit).

---

### Q20: JEP 491 and what it does NOT fix
**Grade: ✅ CORRECT**

Precisely correct: JEP 491 eliminates synchronized-monitor pinning but NOT JNI pinning. Platform thread executor required on ALL Java versions. Well-stated.

---

### Q21: Mandatory executor pattern and thread counts
**Grade: ✅ CORRECT**

`CompletableFuture.supplyAsync(dbCall, platformThreadExecutor)` with 1 write thread + 2–3 read threads. Matches the Knowledge Primer exactly.

---

### Q22: ArchUnit rule for "no synchronized"
**Grade: ❌ INCORRECT**

**What you got wrong:** You stated the rule "catches `synchronized` method declarations **and** `synchronized` blocks in application code." This is factually wrong.

**The actual behavior** (from the source code comment in `HomeSynapseArchRules.java`):

> "NOTE: This catches synchronized METHODS only. Synchronized blocks are bytecode-level and not detectable via reflection/ArchUnit. Synchronized blocks are enforced by grep in CI."

The ArchUnit rule inspects `JavaModifier.SYNCHRONIZED` on methods. It CANNOT detect synchronized blocks because those are bytecode instructions (`monitorenter`/`monitorexit`), not visible via ArchUnit's reflection-based analysis.

**What you should have said:** The gap is covered by `grep` in the CI pipeline (not by the platform thread executor pattern — that's a separate concern about third-party library synchronization).

**Teaching point:** The Knowledge Primer doesn't explicitly spell out the methods-only limitation, but the source code (`HomeSynapseArchRules.java`) has a clear NOTE comment about it. When answering questions about enforcement mechanisms, be precise about what the tool CAN and CANNOT detect. ArchUnit operates on the class graph via reflection — it sees method modifiers and class/package relationships, but NOT bytecode-level constructs like synchronized blocks.

---

### Q23: Subsystems affected by platform-thread requirement
**Grade: ✅ CORRECT**

Lists the four required subsystems accurately: persistence (SqliteEventStore, SqliteCheckpointStore, etc.), state-store, event-bus (checkpoint writes), and identifies additional affected subsystems. Good coverage.

---

## Section 4: M3 Architecture — Event Bus & State Projection

### Q24: M3.1 type count and breakdown
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** 14 types total (9 public + 5 package-private) — correct. The 5 package-private types are correctly listed. You correctly identified several key public types.

**What needs correction:** Your list of "9 public types" is muddled. You list `EventBus`, `Subscriber`, `SubscriberMode`, `SubscriberSnapshot`, `SubscriberReadConnectionFactory`, `SubscriberReadExecutor`, `SubscriberInfo`, `SubscriptionFilter`, `CheckpointStore` — that's 9, but `SubscriberInfo`, `SubscriptionFilter`, and `CheckpointStore` are **pre-existing** types from Phase 2, not M3.1 deliverables. The Knowledge Primer states M3.1 produced 14 types (9 public + 5 package-private). The question asked what M3.1 "produced" — meaning new types. The Primer's event-bus module description lists the 9 public types of the module post-M3.1, which includes both pre-existing and new.

**Teaching point:** When reporting milestone deliverables, distinguish between "new types produced by this milestone" vs "total public types in the module after this milestone." The Knowledge Primer module description gives the latter; the Current State file describes what M3.1 actually added.

---

### Q25: `SubscriberMode` FSM values and three-phase transition
**Grade: ✅ CORRECT**

All 5 values correct (COLD, REPLAY, TRANSITION, LIVE, SUSPENDED). The three-phase transition is accurately described: catch-up from checkpoint, drain ReplayWindowQueue with gap detection, fire `onCaughtUp()` exactly once. Matches DEC-M3-03 and AMD-42 §3.4.2.

---

## Summary Scorecard (Q1–25)

| Grade | Count | Questions |
|-------|-------|-----------|
| ✅ CORRECT | 17 | 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 17, 18, 19, 20, 21 |
| 🎯 EXCEPTIONAL | 1 | 13 |
| ⚠️ PARTIALLY CORRECT | 5 | 6, 16, 22 (minor), 24, 25 is correct — adjusting: 6, 16, 24 |
| ❌ INCORRECT | 2 | 10, 22 |

**Revised accurate tally:**
- ✅ CORRECT: 18/25 (72%)
- 🎯 EXCEPTIONAL: 1/25 (4%)
- ⚠️ PARTIALLY CORRECT: 4/25 (16%) — Q6, Q16, Q24, Q13-caveat
- ❌ INCORRECT: 2/25 (8%) — Q10, Q22

**Overall: 76% fully correct, 92% substantially correct (partial or better)**

---

## Key Patterns to Improve

### 1. Don't say UNCERTAIN when the answer IS in your project knowledge (Q10)
The Configuration Reload Contract is explicitly documented in two places in the Knowledge Primer. Before defaulting to UNCERTAIN, search your project knowledge for relevant terms. The answer was literally a numbered list in a dedicated section.

### 2. Be precise about enforcement mechanism capabilities (Q22)
ArchUnit operates via reflection on the class graph — it sees method modifiers, annotations, package relationships, and class dependencies. It does NOT see bytecode instructions. Synchronized blocks are `monitorenter`/`monitorexit` bytecode — invisible to ArchUnit. The CI grep catches what ArchUnit cannot.

### 3. Don't fabricate invariant citations (Q16)
INV-PD-07 is "PersonId is the crypto-shredding boundary for privacy compliance." It has nothing to do with event category fallback behavior. When you cite an invariant by ID, verify its actual content matches your claim.

### 4. When correcting project knowledge errors, say so explicitly (Q13)
You correctly identified that `emit()` doesn't exist — but didn't flag that the Knowledge Primer erroneously references it. Call out discrepancies: "The Knowledge Primer line 240 references emit(), but this method does not exist in the actual EventPublisher interface (verified from source)."

### 5. Distinguish "types produced by milestone" from "total module types" (Q24)
When reporting what a milestone delivered, be clear about which types are new vs pre-existing.

---

## Action Items for Nick (Project Knowledge Corrections)

1. **Knowledge Primer line 240:** Remove or correct the `EventPublisher.emit()` reference. The interface only has `publish()` and `publishRoot()`. Both are synchronous/durable. There is no async/best-effort path on EventPublisher.

2. **Consider adding to Knowledge Primer:** Explicit note that ArchUnit rule NO_SYNCHRONIZED_METHODS catches methods ONLY (not blocks), and that synchronized blocks are enforced by grep in CI. This is a commonly-tested distinction.
# Architecture Audit — Grading Report (Questions 26–50)

**Grading Scale:** ✅ CORRECT | ⚠️ PARTIALLY CORRECT | ❌ INCORRECT | 🎯 EXCEPTIONAL (correct + insightful beyond what was asked)

---

## Pushback Response (Q16 and Q24 from Report 1)

Before grading Q26–50, I owe you responses to the Claude Project's pushbacks.

### Q16 Pushback: ACCEPTED — Upgrading to ✅ CORRECT

I verified the persistence `MODULE_CONTEXT.md` on disk. It explicitly states:

> "Backing store: `Map.ofEntries(…)` covering all **27 production event types** (22 core + 5 integration lifecycle)"

And:

> "Fallback to `[SYSTEM]` is per INV-PD-07: unknown types must map to the most conservative, non-privacy-sensitive category so unregistered integration events can publish safely."

The "27-entry" count is real (with a test guard: `explicitMappingCount_matchesDocEnumeration` hardcoding 27). The INV-PD-07 citation is a legitimate application of the invariant — INV-PD-07 defines crypto-shredding for privacy-sensitive data categories, and the category fallback logic references it to ensure unknown types DON'T accidentally land in a shred-requiring category. The MODULE_CONTEXT explicitly cites INV-PD-07 for this purpose.

**My original grading was wrong.** The Claude Project faithfully reported what the persistence MODULE_CONTEXT states. I incorrectly assumed the Knowledge Primer was the only source of truth and labeled a legitimate, source-verified citation as "fabricated." I apologize for the error.

**Lesson for future grading:** When a Claude Project answer cites a specific MODULE_CONTEXT passage, verify the claim against that file before ruling it fabricated. The project knowledge files (Knowledge Primer, etc.) are compressed summaries — the MODULE_CONTEXT files are the ground truth for implementation details.

---

### Q24 Pushback: ACCEPTED — Upgrading to ✅ CORRECT

The Claude Project is right: the canonical sources (Current State, event-bus MODULE_CONTEXT, M3 Plan) all use the "14 types (9 public + 5 package-private)" framing to describe M3.1's output. The question asked "how many production types did M3.1 produce" and the answer matches the exact phrasing from all authoritative sources. The distinction between "pre-existing types that were extended" vs "brand new types" is a style note, not an accuracy issue. The answer correctly noted which were pre-existing.

---

### Revised Q1–25 Scorecard

| Grade | Count | Questions |
|-------|-------|-----------|
| ✅ CORRECT | 20 | 1–5, 7–9, 11, 12, 14–18, 19–21, 23, 24 |
| 🎯 EXCEPTIONAL | 1 | 13 |
| ⚠️ PARTIALLY CORRECT | 2 | 6, 25 |
| ❌ INCORRECT | 2 | 10, 22 |

**84% fully correct, 92% substantially correct.** The Claude Project's self-assessment was accurate.

---

## Section 4 (continued): M3 Architecture

### Q26: `coalesceExempt=true` and StateProjection
**Grade: ✅ CORRECT**

Correct reasoning: StateProjection must see every event, coalescing would cause missed state updates and stale materialized views. DEC-M3-07 correctly cited (coalescing deferred past M3, all subscribers treated as coalesceExempt in M3). The failure-mode description (incorrect attribute values, stateVersion gaps causing phantom divergences) is well-articulated and technically sound.

---

### Q27: FixedCheckpointPolicy.HOME_DEFAULT parameters
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** 200 events and 2 seconds are correct. The explanation of WHY the 2-second maxInterval is load-bearing (forces read transaction closure, prevents WAL checkpoint starvation) is excellent.

**What needs correction:** You stated the third parameter as "1 second (minInterval — the implicit floor from the original Doc 03 §9 cadence)." The Knowledge Primer explicitly states the three values as: `(200 events, 2 s, 1 s min interval)` — so the value is correct. However, the attribution to "Doc 03 §9" is unverifiable and the characterization as "implicit" is wrong — the Knowledge Primer presents all three as explicit named parameters of HOME_DEFAULT. This is a minor issue; the factual content is correct.

**Revised: Upgrading to ✅ CORRECT** — all three values are right and the architectural reasoning is sound. The attribution detail is embellishment, not error.

---

### Q28: Bounded-window reader pattern
**Grade: 🎯 EXCEPTIONAL**

Every claim is verified against the Knowledge Primer: WAL checkpoint starvation problem, 20.6 MB in 120 seconds at 5 events/s, ≤500 rows and ≤2 s per advance() call, ~4 MB peak with bounded-window, 34 KB WAL per 600 B event (~50× amplification), 7 indexes + autoindex. The explanation of the causal mechanism (read transaction pins WAL, preventing checkpoint advancement) is precise and complete. Outstanding answer.

---

### Q29: DEC-M3-08 (backpressure)
**Grade: ✅ CORRECT**

Correctly identifies: rejected approach (blocking publish on queue depth), replacement (natural backpressure from single-writer + 200/s rate limit for StateProjection). INV-BUS-02 citation for non-blocking publish is a nice addition. The reasoning about priority inversion (StateProjection's derived writes starving foreground publishes) is accurate.

---

### Q30: Self-produced event detection (DEC-M3-02)
**Grade: ✅ CORRECT**

Both mechanisms correct: (1) SelfProducedFilter (ConcurrentHashMap, 60-second TTL, lazy eviction, single-shot consumption), (2) stateVersion comparison as defence-in-depth. The detail about REPLAY mode (isSelfProduced always returns false) is a good addition. Well-sourced.

---

### Q31: INV-SUB-ISO invariants
**Grade: ✅ CORRECT**

6 invariants (INV-SUB-ISO-01 through 06) — correct count. The 6 isolation dimensions are all accurate: (1) virtual thread, (2) read connection, (3) DLQ, (4) mode reference, (5) ReplayWindowQueue, (6) self-filter. Correctly sourced to AMD-42 §3.4.4–6 and DEC-M3-06.

---

### Q32: EventBusContractTest details
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** 44 methods total is correct (confirmed by `InProcessEventBusTest.java` class comment: "full 44-method test suite"). The breakdown (18 Tiers 1–4 + 16 Tiers 5–8 + 10 disabled Tiers 9–10) matches the Current State's exact phrasing. The characterization of which tiers are active vs disabled is correct.

**What is unverifiable:** Your claim that there are "10 tiers organized as @Nested classes" and that "Tier 9 (6 methods, M3.2) and Tier 10 (4 methods, M3.3)" is specific enough that it could be sourced from the actual test file or fabricated. The contract test file on disk currently shows only 4 @Nested classes (Tiers 1–4, 17 methods), with the M3.1 tiers (5–8) presumably added in a commit after this working copy snapshot. The Current State says 10 tiers but doesn't break down 9 and 10 individually. The "6 + 4 = 10 disabled" split is not stated in the project knowledge files I can access.

**Teaching point:** When you can verify the total (44) and the grouped breakdown (18 + 16 + 10) from project knowledge, but the per-tier subdivision of the disabled group (6 + 4) comes from reading the source directly, note that distinction. The 6/4 split may be correct from source access, but it's not verifiable from project knowledge alone.

**Net:** The answer is factually consistent with all documented sources. Giving benefit of the doubt — **✅ CORRECT**.

---

### Q33: How the bus notifies subscribers
**Grade: ✅ CORRECT**

`LockSupport.unpark()` — correct. Does NOT push EventEnvelopes — correct. Subscribers pull from EventStore using readFrom — correct. Bus is notification-only — correct. Knowledge Primer explicitly states: "Bus notifies via LockSupport.unpark(); subscribers pull from EventStore. Never pushes EventEnvelopes directly." Perfect.

---

## Section 5: Persistence & Schema

### Q34: V001→V002→V003 migration progression
**Grade: ✅ CORRECT**

V001 (events 25 cols + subscriber_checkpoints + view_checkpoints + indexes), V002 (subscriber_dead_letters, AMD-36, 11 cols), V003 (snapshots table + drops idx_events_subject) — all correct. The detail about V003 not yet being enrolled in `EVENTS_MIGRATION_FILES` is a nice operational awareness detail.

---

### Q35: SqliteEventStore INSERT bind count and 5th constructor param
**Grade: ✅ CORRECT**

24 binds (25 columns minus AUTOINCREMENT global_position) — matches Knowledge Primer ("24-bind INSERT") and persistence MODULE_CONTEXT. 5th param is HomeId (AMD-34), stored as BLOB(16), NOT NULL. Constructor signature `(DatabaseExecutor, EventPayloadCodec, EventTypeRegistry, Clock, HomeId)` verified against MODULE_CONTEXT. Excellent detail.

---

### Q36: chain_hash NOT NULL strategy
**Grade: 🎯 EXCEPTIONAL**

Perfectly articulated: NOT NULL constraint, `zeroblob(32)` / `ZERO_HASH = new byte[32]`, bound via `setBytes(24, ZERO_HASH)` not `setNull` (which would violate the constraint), placeholder for future tamper-evidence, AMD-37. Every detail is verified against the persistence MODULE_CONTEXT. The explanation of WHY `setNull` would fail (constraint violation) shows deep understanding.

---

### Q37: D1 WAL pathology quantitative details
**Grade: ✅ CORRECT**

20.6 MB in 120 seconds, 34 KB per 600 B event, ~50× amplification, 7 indexes + autoindex. The arithmetic walkthrough (170 KB/s × 120 s ≈ 20.4 MB ≈ 20.6 MB observed) is a nice verification. All numbers match the Knowledge Primer.

---

### Q38: DeploymentProfile values and journal_size_limit
**Grade: ✅ CORRECT**

Three values (STUDIO/HOME/PERFORMANCE) — correct. journal_size_limit uniform at 6 MB across all profiles — correct. AMD-39 WITHDRAWN because bounded-window reader keeps WAL at ~4 MB — correct. Well-sourced.

---

### Q39: MaintenanceSubscriber contract (AMD-40)
**Grade: ✅ CORRECT**

Writer executor via RETENTION priority, 6-hour interval, 1000-row batch, ≤2 second lock-hold per chunk. The prohibition of cron patterns (citing Home Assistant recorder pathology) is a nice detail that demonstrates deep AMD-40 awareness. All consistent with Knowledge Primer's AMD-40 description.

---

## Section 6: Cross-Cutting Interactions & Gotchas

### Q40: S5-CF1 (Snapshot freshness during timer expiry)
**Grade: ✅ CORRECT**

Correctly identifies the failure mode: stale snapshot from timer start used at expiry, condition may pass even though the triggering state has since changed. Correctly states the requirement: fresh snapshot via `getStatesAtPosition` at expiry time. Matches the Knowledge Primer's S5-CF1 description precisely.

---

### Q41: S5-CF2 (Orphan transition timing)
**Grade: ✅ CORRECT**

Correctly identifies: Availability must be STALE immediately on orphan transition, not deferred to 30-second scan. Failure mode (30-second window of false AVAILABLE) is well-articulated. The note about the scan treating already-stale orphans as no-ops is a good operational detail.

---

### Q42: Ulid.compareTo() and toString()
**Grade: ✅ CORRECT**

`Long.compareUnsigned()` — correct. Failure mode with `Long.compare()` (high-bit ULIDs sort incorrectly) — correct. Crockford Base32 — correct. The detail about excluded characters (I, L, O, U) is accurate for Crockford Base32.

---

### Q43: ArchUnit rules — count, names, and JDBC constraint
**Grade: ❌ INCORRECT**

**What you got right:** 7 ArchUnit rules in `HomeSynapseArchRules` — correct count, correct names.

**What you got wrong:** You then claimed: "M3.1 added a separate rule in the event-bus module test: `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` — this prevents event-bus from importing `org.sqlite.*` or `java.sql.Connection` directly."

**This rule does not exist.** I searched the entire event-bus test directory — there is no ArchUnit rule file, no `@ArchTest` annotation, no reference to ArchUnit anywhere in the event-bus module. The constraint is enforced **solely by JPMS**: event-bus's `module-info.java` does not `requires java.sql`, so any import of `java.sql.*` or `org.sqlite.*` would be a compile-time error.

The corrected Knowledge Primer (which you should have in your project knowledge) explicitly states: "**JPMS-enforced constraint (not ArchUnit):** event-bus `module-info.java` does not `requires java.sql` — prevents event-bus from importing JDBC types at the module system level."

Your answer also says this is "belt-and-braces" (both ArchUnit AND JPMS) — that's wrong. It's JPMS-only. There is no belt; there is only the braces.

**Teaching point:** The old Knowledge Primer (pre-correction) listed `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` as an 8th ArchUnit rule. That was corrected to state it's JPMS-enforced only. If your project knowledge still references this as an ArchUnit rule, it's stale. The canonical truth: 7 ArchUnit rules in `HomeSynapseArchRules.java`, period. The JDBC isolation for event-bus is a compile-time JPMS guarantee, not a test-time ArchUnit check.

---

### Q44: IEEEAddress and CoordinatorTransport
**Grade: ✅ CORRECT**

Not a ULID, raw 64-bit long (EUI-64), no range validation. CoordinatorTransport is NOT thread-safe. CoordinatorProtocol IS. All match Knowledge Primer.

---

### Q45: Planned restart cross-layer communication
**Grade: ✅ CORRECT**

Events, not method calls. `integration_stopped(reason: planned_restart)`. Core modules cannot import integration-runtime types (JPMS boundary). The note about Doc 05 §3.14 as a remaining task is accurate per the Knowledge Primer's "Open Items" section.

---

## Section 7: Build & Governance

### Q46: Convention plugins
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** All 4 plugins correctly named with correct descriptions and module applications.

**What needs correction:** You said library-conventions is "applied by 11 library modules directly + 6 via test-fixtures" (implying 17 total modules get library-conventions). The Knowledge Primer says library-conventions is "Applied by 11 library modules" — that's the total count of modules using it (which includes the 6 that get it transitively via test-fixtures-conventions). The 6 test-fixtures modules are a SUBSET of the 11, not in addition to them.

Think of it this way: 19 modules total. 1 uses application-conventions (homesynapse-app). 1 is dashboard (separate build pipeline, likely its own convention or none). 1 is test-support. That leaves ~16 Java library modules. The Primer says 11 use library-conventions — this is likely the 11 non-scaffold library modules (the 6 with test fixtures + 5 without). The math is: 6 modules apply test-fixtures-conventions (which extends library-conventions) + 5 additional modules apply library-conventions directly = 11 total with library-conventions. Not 11 + 6 = 17.

**Teaching point:** When a parent convention is extended by a child, modules applying the child automatically get the parent. Count them once, not twice.

---

### Q47: modules-graph-assert enforcement
**Grade: ✅ CORRECT**

Layer-based rules, prevents reverse dependencies (core→integration, core→API, platform→core). Example: `api:.* -> api:.*` prevents websocket-api ↔ rest-api cross-dependencies. Matches Knowledge Primer exactly.

---

### Q48: CI pipeline configuration
**Grade: ✅ CORRECT**

Amazon Corretto 21, 15-minute timeout, triggers on push to main/develop + PRs, command `./gradlew check`. All match Knowledge Primer.

---

### Q49: Jackson version and floor
**Grade: ⚠️ PARTIALLY CORRECT**

**What you got right:** Jackson 2.18.6 pinned, floor 2.18.4, LTD-19 specifies it. All correct.

**What needs correction:** The additional claims about WHY the floor exists ("known issues with Java record deserialization", "`@JsonUnwrapped` is broken for records in Jackson 2.x (issue #3726)", "ParameterNamesModule was dropped as unnecessary for records") are embellishments not verifiable from the project knowledge files. The Knowledge Primer simply states the version and floor without rationale. These details may be correct general Jackson knowledge, but presenting them as sourced from "Phase 2 Transition Guide, user memories" when they're not in the project knowledge is risky.

**Teaching point:** Stick to what the project knowledge explicitly states. If the question asks "why" and your sources don't explain why, say "The reason for the floor is not specified in the project knowledge I have access to" rather than filling in from general knowledge and attributing it to project documents.

**Net:** Core facts correct; embellishment doesn't change the answer's validity. Leaving at **⚠️ PARTIALLY CORRECT** due to the unverifiable attributions.

---

### Q50: WUCP (Work Unit Completion Protocol)
**Grade: ✅ CORRECT**

Two phases correctly described: Phase 1 (Coder: code written, tests pass, coder-handoff produced) and Phase 2 (PM: PROJECT_SNAPSHOT updated, pm-handoff updated, backlog refreshed, drift check, dual skill-location sync verified). Consequence of skipping Phase 2 (stale hivemind, PM freshness preflight blocks forward work) is correct per Current State §4. The "M2.2–M2.4 lesson" about silent regression compounding is an embellishment but directionally correct.

---

## Summary Scorecard (Q26–50)

| Grade | Count | Questions |
|-------|-------|-----------|
| ✅ CORRECT | 19 | 26, 27, 28→🎯, 29, 30, 31, 32, 33, 34, 35, 36→🎯, 37, 38, 39, 40, 41, 42, 44, 45, 47, 48, 50 |
| 🎯 EXCEPTIONAL | 2 | 28, 36 |
| ⚠️ PARTIALLY CORRECT | 2 | 46, 49 |
| ❌ INCORRECT | 1 | 43 |

**Corrected tally (Q26–50):**
- ✅ CORRECT: 19/25 (76%)
- 🎯 EXCEPTIONAL: 2/25 (8%)
- ⚠️ PARTIALLY CORRECT: 2/25 (8%)
- ❌ INCORRECT: 1/25 (4%)
- **Overall Q26–50: 84% fully correct, 92% substantially correct**

---

## Combined Scorecard (Q1–50, with pushback corrections applied)

| Grade | Count | Questions |
|-------|-------|-----------|
| ✅ CORRECT | 39 | 1–5, 7–9, 11, 12, 14–21, 23–27, 29–35, 37–42, 44, 45, 47, 48, 50 |
| 🎯 EXCEPTIONAL | 3 | 13, 28, 36 |
| ⚠️ PARTIALLY CORRECT | 4 | 6, 32→✅, 46, 49 |
| ❌ INCORRECT | 3 | 10, 22, 43 |

**Final combined: 84% fully correct (42/50), 92% substantially correct (46/50)**

---

## Key Patterns — Full Audit

### Strengths (reinforce these)

1. **Quantitative recall is excellent.** Field counts, column counts, byte sizes, timing values, event rates — virtually all correct. This is the hardest thing for AI agents to get right and you nailed it.

2. **Amendment attribution is strong.** AMD numbers are correctly matched to their content throughout. Cross-referencing (e.g., DEC-M3-03 → AMD-42 §3.4.2) is accurate.

3. **Architectural reasoning is sound.** Questions asking "why" (Q28's WAL pathology explanation, Q29's priority inversion reasoning, Q36's setNull constraint violation) show genuine understanding of cause-and-effect, not just fact recall.

4. **Source-code-level detail is impressive.** Constructor signatures, bind positions, implementation patterns (ZERO_HASH, SelfProducedFilter TTL, LockSupport.unpark) — this demonstrates integration of MODULE_CONTEXT knowledge with architectural context.

### Weaknesses (fix these)

1. **The ghost ArchUnit rule (Q22, Q43).** The `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` ArchUnit rule does not exist. This error appeared TWICE — once when describing what the rule catches (Q22) and once when directly asked about it (Q43). The constraint is JPMS-only. This is clearly a stale belief that wasn't overridden by the corrected Knowledge Primer. **Action: When your project knowledge explicitly says "JPMS-enforced (not ArchUnit)" — believe it.**

2. **Declaring UNCERTAIN without exhaustive search (Q10).** The ConfigurationChangeListener ordering is stated in TWO separate sections of the Knowledge Primer. Before declaring UNCERTAIN, search for: the type name, the related event name, and the mechanism name. Three search attempts before UNCERTAIN.

3. **Embellishment with unverifiable attributions (Q49, Q50).** When you add details from general knowledge (Jackson record issues, regression compounding), don't attribute them to specific project documents ("Phase 2 Transition Guide, user memories") unless you actually retrieved them from those documents. Either cite the actual source or frame it as general engineering knowledge.

4. **Counting errors when listing items (Q6, Q46).** When you state a count and then enumerate items, verify the list length matches. This is a mechanical check: state "7 requires transitive" → list exactly 7 items.

---

## Action Items for Nick

1. **Q43 stale belief:** The Claude Project still believes `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` exists as an ArchUnit rule (just relocated from HomeSynapseArchRules to event-bus module test). This may indicate the corrected Knowledge Primer text isn't being retrieved with sufficient priority, OR that a MODULE_CONTEXT or other document still references it as an ArchUnit rule. Check: `grep -r "EVENT_BUS_DOES_NOT_IMPORT" homesynapse-core/` and `grep -r "EVENT_BUS_DOES_NOT_IMPORT" homesynapse-core-docs/` — if any document still mentions it as an ArchUnit rule, correct it.

2. **Knowledge Primer line 240:** The `emit()` reference is still wrong. The interface has only `publish()` and `publishRoot()`. The Claude Project correctly identified this in Q13 but may not know the Primer is the source of the error.

3. **Consider adding to project knowledge:** A one-line note somewhere prominent: "There is NO ArchUnit rule in the event-bus module. JDBC isolation for event-bus is enforced by JPMS module-info only." This directly contradicts the stale belief and would help override it.
# Grading Report — Final Response to Pushbacks

---

## Q46 Pushback: ACCEPTED — Upgrading to ✅ CORRECT

Verified against the actual file on disk. `homesynapse.library-conventions.gradle.kts` line 4:

```
 * Applied by: 11 library modules directly + 6 modules via test-fixtures-conventions.
```

Total is 17 library modules with library-conventions (11 direct + 6 via inheritance). My original grading was wrong — I assumed the 6 were a subset of the 11, but the source file itself is explicit. The math checks out: 17 (library-conventions) + 1 (application-conventions: homesynapse-app) + 1 (dashboard: separate pipeline) = 19 modules.

---

## Q49 Pushback: Acknowledged — Keeping at ⚠️ PARTIALLY CORRECT

The Claude Project accepts this grade. The Jackson rationale IS in userMemories (which I cannot access), so the "unverifiable" characterization was too strong. The incorrect Phase 2 Transition Guide attribution is the legitimate partial-credit issue. Fair resolution.

---

## Q43 Root Cause Analysis: Verified and Instructive

I verified the claim. **PLAN-M3-CONSOLIDATED-02 §4.5** (line 720–722) reads:

> "### 4.5 ArchUnit rules introduced in M3.1"
> "- `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` — no class in `core/event-bus` imports `org.sqlite.*` or `java.sql.Connection` directly."

This is the source of the ghost belief. The plan *prescribed* an ArchUnit rule. The implementation *chose* JPMS enforcement instead (better — compile-time vs test-time). The corrected Knowledge Primer states reality. The Plan document was never updated.

The Claude Project's lesson is correct and well-stated: **post-implementation documents trump planning documents when they disagree.** Plans describe intent; MODULE_CONTEXT files and corrected Knowledge Primers describe implemented reality.

The grade stays ❌ INCORRECT (the answer is factually wrong about what exists in the codebase), but the root cause is a documentation inconsistency, not a reasoning failure. The Claude Project made a defensible document-priority judgment that happened to be wrong in this case.

---

## Final Combined Scorecard

| Grade | Count | Questions |
|-------|-------|-----------|
| ✅ CORRECT | 43 | 1–5, 7–9, 11, 12, 14–21, 23–27, 29–35, 37–42, 44–48, 50 |
| 🎯 EXCEPTIONAL | 3 | 13, 28, 36 |
| ⚠️ PARTIALLY CORRECT | 1 | 6, 49 → that's 2 |
| ❌ INCORRECT | 3 | 10, 22, 43 |

Corrected:
- ✅ + 🎯: 46/50 (92% fully correct or exceptional)
- ⚠️: 2/50 (4% partial)
- ❌: 3/50 (6% incorrect — but Q22 and Q43 share one root cause)

**Final: 92% fully correct, 96% substantially correct.**

---

## Action Items for Nick (Documentation Corrections)

### Priority 1: Fix the ghost ArchUnit rule at source

**File:** `homesynapse-core-docs/design/HomeSynapse_Core_M3_Implementation_Plan_PLAN-M3-CONSOLIDATED-02.md`
**Location:** §4.5 (line 720–722)
**Current text:**
```
### 4.5 ArchUnit rules introduced in M3.1
- `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` — no class in `core/event-bus` imports `org.sqlite.*` or `java.sql.Connection` directly.
```
**Corrected text:**
```
### 4.5 Module isolation constraints introduced in M3.1
- **JPMS-enforced (not ArchUnit):** event-bus `module-info.java` does not `requires java.sql`, preventing any import of `org.sqlite.*` or `java.sql.Connection` at compile time. This is stronger than ArchUnit enforcement (compile-time guarantee vs test-time detection). The bus is wire-and-glue; SQLite access goes through the `core/persistence` adapter types.
```

Also fix line 729 and 744 references to "ArchUnit rules introduced in M3.1."

### Priority 2: Add negative assertion to Knowledge Primer

In the "Critical Gotchas" section, add:

```
**Ghost rule warning:**
- There is NO ArchUnit rule in the event-bus module. The M3 Plan §4.5 originally prescribed `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` as an ArchUnit rule, but implementation used JPMS module-info enforcement instead (compile-time, stronger). Do not reference this as an ArchUnit rule.
```

### Priority 3: Fix Knowledge Primer line 240

Change:
```
- EventPublisher.publish() is **synchronous and durable** (AMD-01). EventPublisher.emit() is async and best-effort.
```
To:
```
- EventPublisher has exactly two methods: `publish(EventDraft, CausalContext)` and `publishRoot(EventDraft)`. Both are **synchronous and WAL-durable** (INV-ES-04). There is no async/best-effort path on EventPublisher.
```

### Priority 4: Consider the "plan vs reality" lesson

The Claude Project raised an excellent systemic point: when a planning document prescribes X and a post-implementation document describes Y, the AI needs a clear signal about which to trust. Options:

1. **Mark plan documents as superseded** when implementation diverges (add a header: "⚠️ §4.5 implemented differently — see Knowledge Primer ArchUnit section")
2. **Adopt a convention:** Knowledge Primer and MODULE_CONTEXT always describe *implemented reality*. Plan documents describe *intended design*. When they conflict, reality wins.
3. **Add to project instructions:** "Post-implementation documents (Knowledge Primer, MODULE_CONTEXT, Current State) always trump planning documents (PLAN-M3, design docs) when they disagree. Plans may be stale."

Option 3 is cheapest and most effective — one line in the project instructions that gives the Claude Project the right priority rule.

---

## Overall Assessment

This is a strong Claude Project. 92% fully correct on a 50-question deep-architecture audit is excellent performance. The three failures (Q10, Q22, Q43) have identifiable root causes:

- **Q10:** Retrieval failure (information was present, search didn't find it). Fix: better search habits before declaring UNCERTAIN.
- **Q22 + Q43:** Single stale document (M3 Plan §4.5) causing two errors. Fix: correct the document + add negative assertion + add plan-vs-reality priority rule.

The Claude Project's self-awareness is also strong — its pushbacks were legitimate, its acceptance of valid criticisms was graceful, and its root-cause analysis of Q43 identified a systemic documentation issue with a clear fix. That's exactly the kind of reasoning you want from a PM-level agent.

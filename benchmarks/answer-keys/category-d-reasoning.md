# Category D — Architectural Reasoning (Human-Graded)

These questions have no single correct answer — they test the Claude Project's ability to reason about cross-cutting concerns, failure modes, and design trade-offs. Nick grades these using rubrics.

## Grading Rubric

| Score | Criteria |
|-------|----------|
| 🎯 EXCEPTIONAL | Correct reasoning + identifies non-obvious implications or connections |
| ✅ CORRECT | Sound reasoning, correct citations, identifies the key concern |
| ⚠️ PARTIAL | Partially correct but misses a key mechanism or cites wrong source |
| ❌ INCORRECT | Fundamentally wrong reasoning or completely misses the point |

## Question Bank

### D-001: WAL Pathology Causal Chain
**Question:** Explain the causal chain from "StateProjection holds a read transaction" to "WAL grows without bound." Include the quantitative evidence from D1.

**Rubric:**
- Must identify: read transaction pins WAL → wal_checkpoint cannot advance → WAL accumulates
- Must cite: D1 spike results (20.6 MB, 120s, 5 events/s)
- Must explain: WHY the bounded-window pattern fixes it (close/reopen breaks the pin)
- Bonus: mentions write amplification (34 KB / 600 B / 50×) as contributing factor

---

### D-002: Self-Produced Event Loop Prevention
**Question:** StateProjection publishes `state_changed` events. Those events are delivered back to StateProjection via the bus. Explain the full prevention mechanism — primary and defence-in-depth — and what happens during REPLAY mode.

**Rubric:**
- Must identify: SelfProducedFilter (primary) — ConcurrentHashMap, 60s TTL, single-shot
- Must identify: stateVersion comparison (defence-in-depth) — incoming ≤ current = skip
- Must explain REPLAY: filter is empty/inactive, all events are from history not self
- Bonus: mentions TTL expiry race condition and why stateVersion covers it

---

### D-003: S5-CF1 Timer Freshness
**Question:** When AMD-25's temporal duration timer fires, what goes wrong if you use the original snapshot instead of a fresh one? Describe the specific failure scenario.

**Rubric:**
- Must describe: condition was true when timer started, became false during window
- Must identify: stale snapshot passes validation, action fires on resolved condition
- Must cite: getStatesAtPosition / AMD-03 as the correct mechanism
- Bonus: identifies deduplication vs. evaluation as separate concerns

---

### D-004: Virtual Thread Carrier Exhaustion
**Question:** Explain how 4 concurrent sqlite-jdbc calls on virtual threads can deadlock the entire application on a Pi 5. What is "double-pinning" and why does JEP 491 not fix it?

**Rubric:**
- Must explain: synchronized native → monitor pin + JNI pin simultaneously
- Must identify: Pi 5 has limited carrier threads (ForkJoinPool default = CPU cores)
- Must explain: 4 calls exhaust carriers → all other VTs cannot schedule
- Must explain: JEP 491 fixes monitor pinning only, not JNI pinning
- Bonus: connects to executor sizing (1 write + 2-3 read = bounded below carrier count)

---

### D-005: Cross-Layer Communication Constraint
**Question:** Integration-runtime manages adapter lifecycle. The automation module needs to know when an integration is performing a planned restart. Why can't automation simply import a type from integration-runtime? How does HomeSynapse solve this?

**Rubric:**
- Must identify: JPMS boundary — core modules cannot import integration-runtime
- Must identify: events as the communication mechanism
- Must name: integration_stopped(reason: planned_restart) event
- Must explain: this preserves the dependency direction invariant
- Bonus: cites Doc 05 §3.14 as the pending specification for this pattern

---

### D-006: Orphan Transition Timing
**Question:** Why must orphan Availability be set to STALE immediately upon integration failure, rather than waiting for the periodic 30-second staleness scan?

**Rubric:**
- Must identify: 30-second window of false AVAILABLE status
- Must identify: consumers (dashboards, automations, REST API) acting on stale state
- Must distinguish: periodic scan = natural staleness; orphan = explicit lifecycle event
- Bonus: mentions duplicate stale event prevention (scan treats already-stale as no-op)

---

### D-007: Bounded-Window vs Active Checkpoint
**Question:** The system has both a bounded-window reader pattern (ProjectionAdvancer) and an optional ActiveCheckpointService. Explain why the bounded-window pattern is "load-bearing" while the active checkpoint is "defense-in-depth." What would break if you removed each one?

**Rubric:**
- Must explain: bounded-window closes transactions, allowing wal_checkpoint to advance
- Must explain: active checkpoint issues PASSIVE checkpoints on a timer
- Must identify: removing bounded-window → D1 pathology returns (unbounded WAL)
- Must identify: removing active checkpoint → system still works (wal_autocheckpoint suffices)
- Must cite: D1 validation showed redundancy under nominal load, but protective under degraded

---

### D-008: Priority Inversion in Write Executor
**Question:** DEC-M3-08 rate-limits StateProjection's derived writes to 200/s. Explain the priority inversion risk that motivates this and what happens without the limit.

**Rubric:**
- Must identify: StateProjection publishes state_changed events via the single writer
- Must explain: without limit, rapid event intake → rapid state_changed production → writer saturated
- Must identify: foreground event publishes (device reports, commands) get starved
- Must cite: WritePriority ordering (EVENT_PUBLISH > STATE_PROJECTION)
- Bonus: explains that WritePriority ordering alone isn't sufficient (projection could still flood at equal throughput)

---

## Adding New Questions

When adding a D-category question:
1. It must test reasoning, not recall (if it has one factual answer, it belongs in A/B/C)
2. Write the rubric BEFORE running the question (prevents post-hoc rationalization)
3. Include "Bonus" criteria for exceptional answers
4. Tag with the milestone/amendment that makes it relevant

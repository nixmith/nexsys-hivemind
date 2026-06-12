# Research 9 Brief — Event-Sourced Projection Rebuild, Versioning, and Backfill

*Target: HomeSynapse Core M4 (Workstream A — projection/derivation foundation, WUs M4.0a/M4.0b). Hand this to the research surface. Output must follow the mandatory research format below.*

## Why this research exists

M4 makes state materialization real for the first time. Today the production derivation rule is a **no-op** (`MINIMAL_DERIVATION_RULE = context -> List.of()` in `HomeSynapseCore`), so the canonical attribute map is never populated. M4.0b replaces it with a real `DerivationRule` and a `DispatchingProjectionAdvancer`. That change is a **projection-logic version bump**, which under the project's own execution model (AMD-41 §3.2.4) forces a reconciliation pass: discard checkpoint, clear state, replay from position 0. We have **decided** to add a **one-shot backfill** during that 1→2 replay so historical entity attributes reconstruct from the `state_reported` log rather than being empty until each device next reports.

This area was never a dedicated research topic (Research 2–8 covered event model, device model, automation, config, integration runtime, API — not projection rebuild). It is now the M4 critical path and the highest-risk design surface. This brief closes that gap.

## The questions (what we need answered)

1. **Projection rebuild strategies.** How do mature event-sourced systems rebuild a read model / projection when the projection logic changes? Replay-from-zero vs. blue-green/parallel rebuild (build the new projection alongside the old, then cut over) vs. snapshot-anchored partial replay. Trade-offs on constrained hardware (single SQLite file, ~4-core Pi).
2. **Projection versioning.** How is a "projection version" tracked and how does a version mismatch trigger a rebuild? Patterns for detecting "this checkpoint was written under different logic" and recovering safely. (We have AMD-41 §3.2.4's `projectionVersion` mismatch → replay-from-zero already; we want to know if there's a better-proven pattern and what the pitfalls are.)
3. **Backfill / catch-up semantics.** When a *new* derived event type is introduced (here: `state_changed` derived from `state_reported`), what are the established patterns for backfilling historical derived state during a rebuild? Specifically: is it sound to *compute* derived state during replay and apply it to the read model **without re-emitting** the derived events into the log (since the historical log predates the rule)? How do systems avoid double-counting when, on *later* rebuilds, the derived events DO exist in the log?
4. **Idempotency cursors under rebuild.** We use a monotonic `stateVersion` that "advances on every processed event" as an idempotency/staleness cursor. What are the failure modes of such cursors during rebuild/backfill (double-increment, divergence between rebuilds), and how do mature systems keep them deterministic and consistent across replays?
5. **Determinism guarantees.** Our derivation must be deterministic under re-execution (it re-runs on every replay; AMD-41 §3.2.2). What disciplines do event-sourced frameworks enforce to keep projection handlers deterministic (clock injection, no external reads, pure functions of (prior state, event))? What breaks determinism in practice?
6. **Constrained-hardware rebuild performance.** Our checkpoint policy (AMD-38) forces a 2-second read-tx cadence; AMD-41 §3.2.3 defers a snapshot store until full replay exceeds **5 seconds** on the Pi 4 reference. What are realistic replay-from-zero times for event logs of, say, 10k / 100k / 1M events on constrained hardware, and what techniques (snapshotting, batched apply, bounded windows) keep first-boot rebuild within budget? When is a snapshot store worth activating?
7. **Schema/sealed-hierarchy upcasting during rebuild.** We are simultaneously expanding the `AttributeValue` sealed hierarchy and replacing `labels` with `SemanticTag` (with an `AttributeValueUpcaster` SPI). How do event-sourced systems upcast old stored events during replay without breaking determinism, and how does upcasting interact with a projection-version rebuild?
8. **Testing rebuilds.** How are projection rebuilds, backfills, and idempotency-under-replay tested? Property-based approaches (replay invariants), golden-master, real-blob deserialization tests.

## Platforms / prior art to survey (primary sources required)

At least: **Axon Framework** (event processors, replay/reset, `@DisallowReplay`, tracking tokens, projection rebuild), **EventStoreDB / Kurrent** (projections, `$ce`/`$et` streams, idempotent projections), **Marten** (projection rebuild, async daemon, "rebuild" semantics), **Akka Projections / Lagom** (offset stores, exactly-once vs at-least-once projection handlers), and at least one smart-home reference (**Home Assistant** `recorder` + `restore_state`/`RestoreEntity` for how it restores entity state on restart, and whether it backfills). Optional: Marten/Kurrent "Proof-Oriented Event Sourcing" material on replayable state spaces.

For each platform: how it solves the problem, at least one primary-source quotation (docs / issue tracker / maintainer statement) with URL, known pain points from community reports, and the specific lesson for HomeSynapse.

## Verified HomeSynapse context — use these EXACT facts; do not invent type names

The single biggest failure mode in prior research (Research 3/4/6/7/8) was fabricating type names without source access. Ground every recommendation in the following, which are source-verified as of the M3.7 closeout. If you need a type not listed here, mark it "must verify against source," do not invent it.

- **`DerivationRule`** — `@FunctionalInterface` in `core/state-store` (`com.homesynapse.state`): `List<EventDraft> evaluate(DerivationContext context)`. Production binding today is the no-op lambda `MINIMAL_DERIVATION_RULE` in `HomeSynapseCore`. The successor advancer is **`DispatchingProjectionAdvancer`** (Research 8 REC-28; dispatch-by-`@EventType`, constructor-injected package-private handlers, **no ServiceLoader** per DECIDE-04).
- **`StateProjection`** (`com.homesynapse.state`) runs a strict two-phase model per AMD-41 §3.2.1: READ (rule evaluates, derived drafts buffered, read-tx closes) then PUBLISH (LIVE only). On REPLAY/TRANSITION the rule re-executes but publishing is suppressed; the `SelfProducedFilter` is bypassed so determinism (not the stale filter) carries correctness (§3.2.2). `processBatch` is the catch-up/REPLAY path; `onEvent` is the LIVE path.
- **`applyToState`**: on inbound `state_reported` it advances `stateVersion`/`lastReported`/`lastUpdated` but leaves `attributes` untouched; on inbound `state_changed` it does `newAttrs.put(key, new StringValue(value))` (idempotent on value) and sets `lastChanged`, `stateVersion + 1`.
- **`EntityState`** (9 fields): `entityId, attributes, availability, stateVersion, lastChanged, lastUpdated, lastReported, staleAfter, stale`. Documented contract: `stateVersion` "advances on every processed event — not just mutations" and is a "reliable idempotency cursor."
- **`projectionVersion`**: wired as `1` in `HomeSynapseCore`'s `StateProjection.create(...)`. AMD-41 §3.2.4: a persisted-vs-running mismatch discards the checkpoint, clears the `StateStore`, and replays from position 0 (escape hatch config `homesynapse.projection.allow_stale_snapshots`).
- **Checkpoint**: AMD-38 (200 events / 2 s / 1 s min); `AtomicCheckpointWriter` (in `com.homesynapse.persistence`) couples subscriber + view checkpoint in one SQLite transaction (M4.0a / AMD-45). AMD-41 §3.2.3 defers `SqliteSnapshotStore` until replay > 5 s on Pi 4 (V003 `snapshots` table already migrated).
- **The locked M4.0b decision**: one-shot backfill — apply re-derived drafts to in-memory state during the 1→2 reconciliation replay **only**, gated to that boundary, because applying re-derived drafts AND logged `state_changed` on later replays would double-increment `stateVersion`.
- **Store reality**: the `StateStore` is an in-memory `ConcurrentHashMap`; the event store is SQLite (WAL, single-writer, bounded-window reads per the D1 spike). Java 21, virtual threads, no `synchronized` (LTD-11).

## Constraints on the output

- Follow the mandatory format below. Every factual claim traceable to §6 sources.
- **REC numbering starts at REC-76** (continues the global sequence; Research 7 ended at REC-75). Each REC: gap citation, lesson source, the specific change (record/interface/handler/config shape), backward-compat assessment, effort estimate, and target WU (M4.0a / M4.0b-1 / M4.0b-2).
- For any HomeSynapse type/field you reference beyond the list above, write "VERIFY: <name> against source" rather than asserting it. If a recommendation conflicts with the verified inventory, surface the conflict in §5 (do not silently break the inventory).
- Distinguish **what is settled** (the one-shot backfill decision, replay-from-zero on version bump) from **what we are asking you to inform** (whether replay-from-zero is the right rebuild strategy at our scale, whether/when to activate the snapshot store, the precise backfill-gating mechanism, determinism disciplines, idempotency-cursor safety).

## Mandatory research format

```
# Research 9: Event-Sourced Projection Rebuild, Versioning, and Backfill — {subtitle}
*Target: HomeSynapse Core M4 (M4.0a/M4.0b). Date: YYYY-MM-DD.*

## 1. Executive Summary [M]   — 5–8 verdict bullets, each a bold claim + one-sentence defense; flag the single highest-impact finding.
## 2. Platform / Literature Deep Dives [M]   — one subsection per system; (a) how it solves rebuild/backfill, (b) ≥1 primary-source quote + URL, (c) known pain points, (d) specific HomeSynapse lesson.
## 3. Cross-Cutting Analysis [M]   — concept-mapping table (HomeSynapse | Axon | EventStoreDB | Marten | Akka | HA); gap analysis ranked by impact; over-abstraction analysis; competitive assessment (where our two-phase + bounded-window + atomic-checkpoint model is genuinely strong, with qualifying language).
## 4. Amendment Recommendations [M]   — REC-76+ ; ranked by (impact × confidence) / cost; the backfill-gating mechanism, snapshot-activation trigger, determinism discipline, and idempotency-cursor safeguards should each yield a concrete REC.
## 5. Caveats and Open Questions [M]   — source reliability; unresolved tensions; what needs an empirical Pi spike vs. what the literature settles.
## 6. Appendix: Sources [M]
## 7. HomeSynapse Code-Level Implications [O]   — concrete handler/rule/config shapes, the precise replay-time hook for the one-shot backfill, snapshot-store activation criteria, MODULE_CONTEXT impact.
```

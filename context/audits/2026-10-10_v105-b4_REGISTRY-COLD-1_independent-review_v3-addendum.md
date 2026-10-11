<!--
file: _scratch/v104/b4/REGISTRY-COLD-1_independent-review_v3-addendum.md
purpose: REVIEW-RC1's focused re-read of the hub's four edits (v2 → v3) against homesynapse-core 409547c; verdict, each claim graded at the bytes, exact edits
v3 reviewed: _scratch/v105/b4/REGISTRY-COLD-1_instruction_v3.md -- 42,195 B, md5 9ba00d35ed2dd1573aa9ad46736e80d1 (asserted before reading); v2 8d68079f86f5baa208bf002a40112d9d; `diff v2 v3` = the six hunks named
reviewer: REVIEW-RC1; read-only everywhere except this file; 2026-10-10 23:17–23:24 UTC
-->

# REGISTRY-COLD-1 v3 — addendum (the hub's four edits)

## Verdict: **EDITS** — 6 edits (A1–A6), all mechanical (each OLD occurs once in v3; checked). Two correct a false premise sentence and a wrong path prefix; two make the §4.3 code compile against §4.2 (`skipped` has no source); two make K-2's five-row outcome unambiguous. The design the hunks carry (Nick's (a) with parity) holds at the bytes.

## The five claims

1. **The durable trace (H1) — WRONG in one clause, conclusion HOLDS.** `InProcessEventBus.java:401–:402`: `SubscriberDlq dlq = new SubscriberDlq(` / `info.subscriberId(), PersistentDlqWriter.noop(), clock);` — the noop wiring holds. But a non-noop writer IS constructed in `src/main`: `PersistenceFactory.java:252–:254` `public PersistentDlqWriter deadLetterWriter() { return lifecycle.deadLetterStore()::park; }` ("the production PersistentDlqWriter", `:250`). What is true is that no `src/main` caller passes it to the bus: `git grep deadLetterWriter()` → `PersistenceFactory.java:252` (the declaration), `module-info.java:33` (a comment), `PersistenceFactoryTest.java:67`, `:93` — nothing else. `SubscriberDlq.java` declares no `Logger` (grep `LOG|Logger|log\.` → none); `park(DeadLetter)` (`:111–:125`) builds the entry, pushes the ring, calls `persistentWriter.park` — no log line. So a parked row today leaves the in-memory `dlqDepth` only. Edit A1 rewords the premise.
2. **The supervisor's arms (H1) — HOLDS, one prefix WRONG.** `SubscriberSupervisor.java:102` `} catch (RuntimeException e) {` (parked `:122`, crash `:125`); `:128` `if (crashCount() >= CIRCUIT_BREAKER_THRESHOLD) {` → SUSPENDED `:129–:132`; `:136` `} catch (Error e) {` → "Infrastructure: immediate SUSPENDED, bypass DLQ" (`:137–:141`); `:142` `} catch (Exception e) {` → SUSPENDED (`:146–:149`). `crashCount()` (`:172–:178`) counts the rolling 10-min window, so five crashes inside one replay trip it. Today the fifth surfaces as the gate's throw: `HomeSynapseCore.java:1514` `"registry projection did not reach LIVE within ~30s during startup");` — the file is `L/` (src/main), and v3 writes `LT/` (§0b's legend: `LT/` = the `src/test/…` twin). Edit A2.
3. **`skipped=` (H2) — HOLDS for the pins; WRONG for the instruction's own code.** `git grep -n 'projection_rebuilt'` in core → 0; `BootOrderingGateIT` matches the prefix `registry.projection_live: ` only (`:52`); K-1 (`:161`) and §13 (`:227`) carry the four-field form; no three-field form remains in v3 (grep `rows= head= ms=` → 0). But §4.3's code block logs `skipped` (`:110`) while §4.2 still says the method "returns `long`, the envelopes passed to `onEvent`" (`:90`) and the block declares only `long rows = …` (`:106`): `skipped` has no source, and the lane would have to invent one. Edits A3, A4 give it one (a package-private `skipped()` accessor on the subscriber, read on `main` before `subscribeRuntime` — the same happens-before edge §4.3 names).
4. **K-2's model (H3) — HOLDS as a test; the wording is ambiguous once.** With the same throwing stub on both ways, the four-row case skips the same four positions on both (a throw leaves `lastAppliedPosition` and the registries untouched, `RegistryProjectionSubscriber.java:85–:116`), so EQUAL-minus-those-rows and `skipped=4` are well-defined; the five-row case trips the model at the fifth as `:128` does and the rebuild throws at `REBUILD_CRASH_THRESHOLD`. R-5 (`:158`: one row → WARN, skipped; five → `IllegalStateException`) agrees; §12's list (`R-1..R-5 and K-1..K-3`) needs no change. The ambiguity: "the case FAILS" and "both ways FAIL" can be read as the TEST failing; the sub-case passes when both ways fail. Edits A5, A6.
5. **The retyped constant (H4) — HOLDS.** `SubscriberSupervisor.java:52` `private static final int CIRCUIT_BREAKER_THRESHOLD = 5;` — private, not importable. No rule in `HomeSynapseArchRules.java` (`:74`–`:425`: synchronized, time, ServiceLoader, direction, filesystem, internal, JsonTypeInfo, query-service, REST, Jackson, mutators) constrains a `static final int` in `com.homesynapse.lifecycle`. No §0b instrument (rows 2, 6, 20–23) and no §6 survey count sees it. Nothing to update.

## The edits (OLD occurs once in v3; non-overlapping)

**A1** (claim 1 — §4.2 — the premise, as the bytes have it)

Old:
~~~~
(`B/InProcessEventBus.java:401`–`:402`; no non-noop writer is constructed in `src/main`)
~~~~
New:
~~~~
(`B/InProcessEventBus.java:401`–`:402`; the production writer exists — `PersistenceFactory.deadLetterWriter()` `:252`, `SqliteDeadLetterStore::park` — but no `src/main` caller passes it to the bus: its only callers are `PersistenceFactoryTest:67`, `:93`)
~~~~

**A2** (claim 2 — §4.2 — the path prefix)

Old:
~~~~
`LT/HomeSynapseCore.java:1514`
~~~~
New:
~~~~
`L/HomeSynapseCore.java:1514`
~~~~

**A3** (claim 3 — §4.2 — where `skipped` comes from)

Old:
~~~~
- Package-private instance method; returns `long`, the envelopes passed to `onEvent`.
~~~~
New:
~~~~
- Package-private instance method; returns `long`, the envelopes passed to `onEvent` (the throw arm's rows included — they were passed). A package-private `long skipped()` accessor returns the throw arm's count (a plain field written on `main` during the rebuild, read on `main` before `subscribeRuntime` — §4.3's edge covers it; 0 when nothing threw).
~~~~

**A4** (claim 3 — §4.3 — the code block declares `skipped`)

Old:
~~~~
long rows = registrySubscriber.rebuildFromIndex(store, head);               // (2)
~~~~
New:
~~~~
long rows = registrySubscriber.rebuildFromIndex(store, head);               // (2)
long skipped = registrySubscriber.skipped();                                 // (2b) the throw arm's count, 0 normally
~~~~

**A5** (claim 4 — §7 K-2 — the model's stop is not the test's failure)

Old:
~~~~
and SUSPENDING — the model stops and the case FAILS — at the fifth, as `:128` does)
~~~~
New:
~~~~
and SUSPENDING — the model stops and reports SUSPENDED — at the fifth, as `:128` does)
~~~~

**A6** (claim 4 — §7 K-2 — the five-row sub-case's pass condition)

Old:
~~~~
with FIVE → both ways FAIL (the old way's model SUSPENDs, the new way throws `IllegalStateException`) — the test that keeps the retyped threshold from drifting from the bus's.
~~~~
New:
~~~~
with FIVE → both ways FAIL (the old way's model reports SUSPENDED, the new way throws `IllegalStateException`); the sub-case asserts both outcomes and is green when both occur — the test that keeps the retyped threshold from drifting from the bus's.
~~~~

**Check.** The six OLD texts each occur once in v3 (`str.count == 1`, asserted) and do not overlap; applied in memory the result is 42,832 bytes. Hunks untouched: the new §9 bullet (H4), K-1's and §13's `skipped=0` (H2), §4.1.

## Not verified here
- Whether `Subscriber.onEvent`'s declared signature admits a checked exception (it would decide whether `:142` is reachable from the registry's `onEvent`); the §4.2 sentence is right either way.
- The crash window's clock: the supervisor reads the injected `Clock` (`:103`); under a fixed test clock every crash is "inside the window", so the five-row case trips as written.

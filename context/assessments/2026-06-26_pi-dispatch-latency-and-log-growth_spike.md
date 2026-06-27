<!--
file: context/assessments/2026-06-26_pi-dispatch-latency-and-log-growth_spike.md
purpose: Empirical spike return for the §1 deeper-M7 architecture beat — the two Pi-class numbers the ratified decision record (2026-06-25) commissioned: (1) the added latency of the logical-event-driven, physically co-located command-dispatch hop vs a direct in-process call, to VALIDATE D1's co-location mitigation is negligible (D1 is RATIFIED — this confirms, it does not decide); and (2) the event-log growth rate (bytes/event, append throughput) + projection-rebuild (replay) time as the log grows, to SIZE D4's snapshot cadence + retention/compaction windows. Honors D2 (pure-function replay) in both harnesses. Dispatched as Session V2-A of the v6 hub parallel fan-out v2.
audience: PM (v6 hub), Nick, the Core lane (M7.4a dispatch subscriber + the D4 retention/snapshot design), the Hardware bench (Session D — the Pi re-run).
state-type: assessment (empirical spike return)
status: RETURNED 2026-06-26 by Session V2-A. Dev-machine baseline complete; Pi pass is Nick's (run `spike/dispatch-latency-and-log-growth/run.sh` unchanged on the Pi).
sources-discipline: All numbers are measured on this dispatch's dev sandbox (specs in §2) and are labeled MEASURED. The 1e7 figures are EXTRAPOLATED from the measured 1e4–1e6 curve and labeled as such. The Pi figures are NOT measured here — they are bounded by the dev numbers via the stated CPU/storage ratio logic and must be confirmed by the Pi run. Throwaway spike code lives at homesynapse-core/spike/dispatch-latency-and-log-growth/ (labeled disposable; slated for the hub's standing git rm).
-->

# Pi Dispatch-Latency + Log-Growth Spike — Return (2026-06-26)

## 0. TL;DR (the two numbers + the two verdicts)

1. **Dispatch-seam latency (validates D1).** The co-located event-driven hop
   (executor emits `command_issued` → in-process synchronous bus → a co-located
   dispatch subscriber consumes it, same JVM/thread) adds **~1.9 ns/op** over a
   direct in-process `dispatch(cmd)` call (direct ≈ 0.63 ns/op; event-driven ≈
   2.54 ns/op; median of 20 trials × 20M ops, post-JIT). Against a realistic
   device-dispatch cost of tens-of-µs to ms, that seam is **0.0002%–0.19%** of
   one dispatch. **D1's co-location mitigation is confirmed negligible.** Even
   scaling the seam 5× for the Pi (~10 ns) leaves it 3–5 orders of magnitude
   below the actuation it precedes.

2. **Log growth + replay (sizes D4).** **~488 bytes/event on disk** (constant
   across 1e4–1e6; SQLite WAL, LTD-03 PRAGMAs, schema = the real `events` table,
   includes the `idx_events_entity` index). Append **~60k–98k events/sec** at a
   500-event commit batch. Projection-rebuild (full ordered replay → in-memory
   entity projection): **44 ms @ 1e4 → 108 ms @ 1e5 → 625 ms @ 1e6**, extrapolating
   to **~6–7 s @ 1e7** on the dev box. The **knee is between 1e6 and 1e7**:
   rebuild stays sub-second to ~1e6, becomes multi-second by 1e7, and the
   on-disk size hits the Home-Assistant multi-GB Recorder wall (~465 MB @ 1e6 →
   ~4.6 GB @ 1e7). **D4 should snapshot so that the live replay tail is bounded
   to ≤ ~1e6 events** (see §6 for the cadence + retention shape).

3. **D2 (pure-function replay) — PASS.** The dispatch subscriber acts only in
   LIVE mode; a REPLAY pass of 1,000,000 `command_issued` events produced
   **zero** dispatch side-effects (asserted in-harness; a non-zero count exits
   non-zero). B2's replay is a pure fold into an in-memory map — no device I/O,
   no network, no write-back. The structural basis for D2's CI test holds.

---

## 1. Methodology

Two standalone throwaway benchmarks (plain `javac`/`java` + sqlite-jdbc; no
Gradle, no `module-info` — deliberately self-contained so it touches neither the
production multi-module build nor the shared version catalog, and so Nick can
run it on the Pi unchanged). Source + `run.sh` + README live under
`homesynapse-core/spike/dispatch-latency-and-log-growth/` (labeled THROWAWAY).

**Benchmark 1 — dispatch-seam overhead (`DispatchLatencyBenchmark.java`).**
- *Path A (direct):* an "executor" calls `sink.dispatch(cmd)` directly. The sink
  is a no-op that accumulates a field read at the very end (defeats dead-code
  elimination) and bumps a separate dispatch counter (the D2 probe).
- *Path B (co-located event-driven):* the executor allocates a `command_issued`
  event and emits it into a minimal in-process **synchronous** bus (a subscriber
  list + a REPLAY/LIVE mode flag, in-thread fan-out — the *shape* of the real
  bus's REPLAY→LIVE FSM reduced to the part that costs latency). A registered
  **dispatch subscriber** consumes it **only when mode==LIVE** and calls the
  **same** no-op sink. The `command_issued` allocation is kept — it is the honest
  per-command cost of the event-driven hop.
- *Measurement:* ≥ 2,000,000 warmup iterations running **both** paths (so both
  JIT-compile), then 20 trials of 20,000,000 iterations each, interleaving A and
  B per trial to share thermal/scheduling conditions. Reported as fractional
  ns/op (so the sub-ns seam is visible): **median + p99** for each path and the
  **delta (B − A)**. The seam is then expressed as a fraction of 1 µs / 10 µs /
  100 µs / 1 ms device-dispatch costs.
- *D2 assertion:* flip the bus to REPLAY, feed 1,000,000 of the same events,
  assert the dispatch counter does not advance. PASS/FAIL printed; FAIL exits 2.

**Benchmark 2 — log growth + replay (`LogGrowthBenchmark.java`).**
- *Engine/schema:* SQLite in **WAL** mode (the real persistence engine — the
  existing `spike/wal-validation` subdir confirms it). The **LTD-03 production
  PRAGMAs** are applied verbatim (WAL; synchronous=NORMAL; cache_size=-128000;
  mmap_size=1 GiB; temp_store=MEMORY; journal_size_limit=6 MB; busy_timeout=5000).
  The `events` table mirrors the real one (Doc 04 §4.1 / Doc 01 §4.2):
  `global_position INTEGER PRIMARY KEY AUTOINCREMENT, event_id BLOB(16),
  entity_ref BLOB(16), entity_sequence INTEGER, event_type TEXT, event_time
  TEXT, ingest_time TEXT, payload BLOB`, plus `idx_events_entity (entity_ref,
  entity_sequence)`. The index is included on purpose — it is in the real store
  and it is part of the honest on-disk cost.
- *Payload:* a representative `state_changed`-shaped JSON-ish envelope
  (~360 bytes: typed old/new `{"t":..,"v":..}` values, entity ULID, capability,
  unit, origin, actor, zigbee source, seq) with fields varied per row so it is
  not trivially compressible.
- *Append:* N events inserted in batches of `batch` (one transaction per batch —
  the realistic commit/fsync cadence), 200 entities with per-entity monotonic
  `entity_sequence`. Throughput = events/sec for the append phase. A separate
  **commit-cadence sweep** (batch = 1, 10, 50, 100, 500, 2000) at the smallest N
  exposes fsync sensitivity.
- *On-disk bytes/event:* a `PRAGMA wal_checkpoint(TRUNCATE)` folds the WAL into
  the main file; bytes/event = (main file size) / N.
- *Replay:* a full ordered `SELECT ... ORDER BY global_position` scan folding the
  latest event per entity into an in-memory `HashMap` (a derived token from the
  payload is mixed in so the fold touches the bytes and can't be optimized away).
  **Pure** — no external side-effects (D2). Reported as ms + events/sec at
  N = 1e4, 1e5, 1e6.

**Why these are valid across JDK versions / on the Pi.** The seam measurement is
a JVM in-process call-vs-emit comparison; no JDK-21-only feature is required (we
nonetheless ran on the HomeSynapse target, JDK 21). sqlite-jdbc 3.45.3.0 bundles
native libraries for aarch64/arm, so `run.sh` compiles and runs on the Pi as-is.

---

## 2. Dev-machine specs (the baseline — and why it is an optimistic upper bound)

| Property | Value |
|---|---|
| JVM | Eclipse Temurin **OpenJDK 21.0.11** (LTS), 64-bit Server VM, JDK 21 (HomeSynapse target) |
| CPU | **AMD Ryzen 9 7900X** (Zen 4), x86_64, **2 vCPUs visible**, ~**4.69 GHz**, under Microsoft Hyper-V |
| RAM | 3.8 GiB in the sandbox |
| DB-bench storage | **ext4 on `/dev/sda1`** (local virtual disk) — fast, SSD-class write path |
| Spike-dir storage | **FUSE overlay** (`/sessions/.../mnt/ClaudeFolder`) — see caveat below |
| sqlite-jdbc | org.xerial **3.45.3.0** (JDK11+ safe; bundles aarch64/arm natives) |

**This dev box is an OPTIMISTIC upper bound vs the Pi.** A Raspberry Pi 4/5 ARM
core is roughly **3–5× slower** per-thread than this Zen-4 part at ~4.7 GHz, and
**SD-card random-write + fsync is far slower** than this ext4-on-virtual-SSD
path. Therefore: **append-throughput and on-disk-fsync numbers are an optimistic
ceiling** the Pi will fall well short of (worst on per-event fsync); **replay
time transfers better** (it is CPU + sequential-scan bound) — scale it by the
CPU ratio (≈ ×3–5). Present dev numbers as the baseline; the Pi run via `run.sh`
gives ground truth.

**Storage caveat (important for whoever re-runs this).** SQLite WAL mode does
**not** work on the FUSE-mounted repo directory — attempting it throws
`SQLITE_IOERR_DELETE` (WAL needs real `mmap`/`unlink`/shared-memory file ops the
overlay does not provide). The DB benchmark was therefore run on local **ext4**
(`/tmp`), and `run.sh` writes its scratch DBs to a local real FS by default,
never into the repo tree. This is a dev-sandbox artifact, not a Pi concern (the
Pi's SD/SSD ext4 is a real FS) — but the rule "run the DB bench on a real FS"
is baked into the script.

---

## 3. Benchmark 1 results — dispatch-seam latency (validates D1)

**MEASURED** (median of 20 trials × 20,000,000 ops, ≥ 2M warmup, both paths
JIT-compiled; JDK 21.0.11; Ryzen 9 7900X):

| Path | median (ns/op) | p99 (ns/op) |
|---|---|---|
| A — direct in-process `dispatch(cmd)` | **0.629** | 0.815 |
| B — co-located event-driven hop (emit `command_issued` → subscriber) | **2.538** | 2.673 |
| **Δ (B − A) = the seam cost** | **1.909** | — |

Per-trial variance is tight (A: 0.62–0.82 ns; B: 2.29–2.67 ns across 20 trials),
so ~1.9 ns is a stable estimate of the added cost (event-object allocation +
one virtual `accept` + the LIVE-mode check + the list fan-out).

**The seam as a fraction of a realistic device-dispatch cost** (the argument that
makes "negligible" quantitative). A real Zigbee/device dispatch is microseconds
(in-memory serialize + handoff) to milliseconds (radio round-trip / confirm):

| Realistic device-dispatch cost | Seam (1.9 ns) as a fraction |
|---|---|
| ~1 µs | **0.19 %** |
| ~10 µs | **0.019 %** |
| ~100 µs | **0.0019 %** |
| ~1 ms | **0.00019 %** |

**D1 VERDICT — CONFIRMED (co-location latency is negligible).** D1 is already
RATIFIED; this validates the load-bearing assumption behind it. Even on the Pi,
scaling the seam ~5× to ~10 ns, the co-located hop is **3–5 orders of magnitude**
smaller than the device actuation it triggers — it is unmeasurable in any
end-to-end command-latency budget. The latency objection that was "the only
thing the hybrid had" (decision record §D1) is empirically closed: the seam
correctness is bought essentially for free. Nothing here argues for the in-process
side-channel; the event-driven shape carries no meaningful latency penalty.

---

## 4. Benchmark 2 results — log growth + replay (sizes D4)

**MEASURED** (SQLite WAL, LTD-03 PRAGMAs, 200 entities, 500-event commit batch,
ext4; JDK 21.0.11; Ryzen 9 7900X):

| N (events) | append (ev/s) | DB on disk | **bytes/event** | **replay (ms)** | replay (ev/s) |
|---|---|---|---|---|---|
| 10,000 | 59,218 | 4.87 MB | 487.0 | **43.9** | 227,667 |
| 100,000 | 97,910 | 48.97 MB | 489.7 | **107.7** | 928,888 |
| 1,000,000 | 86,222 | 487.76 MB | 487.8 | **625.4** | 1,598,946 |
| 10,000,000 *(EXTRAPOLATED)* | ~85k | **~4.65 GB** | ~488 | **~6,000–7,000** | ~1.5M |

Observations:
- **bytes/event is dead-constant at ~488 bytes** across two orders of magnitude
  (payload ~360 B + two 16-B IDs + row/index overhead). On-disk size is therefore
  trivially linear in event count: **~465 MB per million events**, **~4.6 GB at
  10M**. That is squarely the Home-Assistant multi-GB Recorder-wall the prior-art
  study warned about — and it arrives at ~10M events, which on a busy home is a
  matter of months, not years (see §6).
- **Replay grows with the log and trends to linear at scale.** The effective
  replay rate rises from ~228k ev/s (1e4, JIT still warming, fixed overheads
  dominate) to ~1.6M ev/s (1e6, steady state). Using the steady-state rate, 1e7
  replays in ~6–7 s on the dev box. The **knee**: sub-second to ~1e6, multi-second
  by ~1e7.
- **The replay number is the D4-critical one** because rebuild blocks a cold
  start / projection rebuild. On the Pi (×3–5 CPU), the dev curve maps to roughly:
  **~0.15–0.2 s @ 1e4, ~0.4–0.5 s @ 1e5, ~2–3 s @ 1e6, ~20–35 s @ 1e7** — i.e.
  the Pi crosses "painful on every boot" (tens of seconds) right around 1e7, and
  is already at "noticeable" (multi-second) by 1e6.

**Commit-cadence (fsync) sensitivity** — MEASURED at N=10,000, the same engine:

| commit batch (events/txn) | append (ev/s) |
|---|---|
| 1 (fsync every event) | 23,590 |
| 10 | 87,403 |
| 50 | 128,230 |
| 100 | 134,786 |
| 500 | 203,234 |
| 2,000 | 169,085 |

Per-event commit (batch=1) is **~8–9× slower** than batching ~500. Throughput
peaks around batch 500–2000 then flattens (the WAL/checkpoint and per-statement
costs take over). **This is the single most Pi-sensitive result**: on an SD card,
fsync latency is far higher, so the batch=1 penalty will be much larger than 8–9×
— the persistence layer's single-writer + batched-commit discipline (Doc 04 §1)
matters even more on Pi than these dev numbers show. (This validates, on the
write side, the same lesson the wal-validation spike established on durability.)

---

## 5. D2 (pure-function replay) — PASS

- **B1:** with the bus in REPLAY mode, **1,000,000** `command_issued` events
  produced **0** dispatch side-effects (dispatch counter did not advance). After
  flipping back to LIVE, a single emit dispatched exactly once (sanity). The
  subscriber-acts-only-in-LIVE property — the structural mechanism D1/D2 rely on
  — holds, and the harness makes a violation a hard, scriptable failure (exit 2).
- **B2:** the replay/fold is a pure function over the log into an in-memory
  projection; it performs no device I/O, no network, and no write-back to the
  log. This is the shape the D2 CI test (the seeded-log-replay-asserts-zero-
  side-effects gate slated for M7.4b) should take.

This is empirical backing for registering the D2 invariant and pinning its CI
test: the event-driven shape makes the property structural, and a tiny harness
can assert it cheaply.

---

## 6. D4 sizing implications — recommended snapshot cadence + retention windows

The two measured curves give D4 concrete thresholds. The design shape (per the
decision record: snapshots + per-scope retention + projection pruning, all
**derivable optimizations over the log, never a second source of truth** —
INV-SA-03 / INV-ES-01) is unchanged; these numbers size it.

**The governing facts.** (a) On-disk cost is linear at **~488 B/event** — there
is no compression cliff to hide behind; volume control must come from *retention*
(bounding what the log keeps) and *snapshots* (bounding what replay must re-fold).
(b) Replay cost is ~linear at scale; the painful boundary on the **Pi** is
multi-second by ~1e6 and tens-of-seconds by ~1e7.

**Recommendation A — snapshot cadence: bound the live replay tail to ≤ ~1e6
events.** A projection's cold-rebuild cost is set by *how many events sit after
its most recent snapshot*, not by the whole log. Target a worst-case rebuild of
**≤ ~2–3 s on the Pi**, which from §4's Pi-mapped curve means **replaying ≤ ~1e6
events**. So **snapshot each materialized view at least every ~1,000,000 events
of its input stream** (equivalently, on a time cadence chosen so that the busiest
realistic event rate accrues ≤ ~1e6 events between snapshots — e.g. if a busy
home produces ~50k–100k events/day, that is a **roughly weekly-to-biweekly**
snapshot for the high-volume projections; quieter projections need it far less
often). Snapshotting is cheap relative to its payoff here and the view-checkpoint
machinery already exists (Doc 04 §3.12 `view_checkpoints`, same-transaction
atomicity) — this is a cadence/policy decision on top of an existing seam, not new
infrastructure. (Note Greg Young's caution that snapshots carry their own
versioning/operational cost; the mitigation is that snapshots here are *purely
derived* and disposable — a wrong/old snapshot is recovered by re-folding from the
log, never a correctness risk.)

**Recommendation B — retention window: bound the *domain* log so on-disk stays
off the multi-GB wall, per-scope and priority-tiered.** At ~465 MB/million
events, an unbounded domain log reaches HA's pain band (multi-GB, slow restarts,
SD wear) at ~5–10M events. The existing priority tiers (Doc 01 §1: CRITICAL
retained longest; DIAGNOSTIC purgeable after days) + per-scope retention are the
right control. Concrete sizing input: **target a domain-log working-set ceiling
on the order of ~1–2 GB (~2–4M events)** for Pi comfort, achieved by purging
low-priority/telemetry-promoted events past their tier window and pruning
inactive per-scope streams — while CRITICAL/forensic events ride longer. The
*telemetry* ring store (Doc 04 §3.6) already bounds the high-frequency raw stream
by construction; D4's new work is the **domain** log's per-scope/priority
retention + the compaction/pruning that keeps the replay-relevant set near the
snapshot tail. Pair retention with the snapshot cadence: once every projection
that needs events older than the retention horizon has snapshotted past them,
those events are eligible for compaction/purge without breaking any rebuild.

**Recommendation C — not a V1 build item beyond the seam, but the seam is now
sized.** Consistent with the decision record ("design-shape now; thresholds tuned
on the data; not a V1 build item beyond the seam unless an early wall shows").
**No early wall shows on the dev box** — 1e6 rebuilds in 0.6 s (dev) / ~2–3 s
(Pi-mapped), comfortably inside a boot budget. So D4 stays a *design-now,
build-as-volume-arrives* item, with the snapshot-cadence target (≤ ~1e6-event
tail) and the retention ceiling (~1–2 GB domain working set) as the numeric
anchors. **The Pi run should re-confirm the knee** before the cadence is frozen,
since the Pi CPU ratio is the load-bearing multiplier and is estimated, not
measured, here.

---

## 7. Pi-transfer caveats (read before trusting any of the above on hardware)

- **CPU:** Pi ARM core ≈ 3–5× slower than this Zen-4 @ ~4.7 GHz. Replay (CPU +
  scan bound) scales ~linearly by that ratio; the dev→Pi mappings in §4/§6 use
  ×3–5. The **seam** (B1) also scales by ~that ratio (~1.9 ns → ~6–10 ns) and
  remains negligible.
- **Storage / fsync:** the dev DB path is ext4 on a virtual SSD; the Pi's SD-card
  (or USB-SSD) random-write + fsync is **much** slower. **Append throughput and
  the per-event-commit penalty are the numbers that will degrade most** — treat
  §4's append ev/s as an optimistic ceiling and expect the batch=1 penalty to
  widen well beyond 8–9×. On-disk **bytes/event** transfers faithfully (it is a
  format property, filesystem-independent at ~488 B).
- **The dev box reports 2 vCPUs;** the benchmarks are single-threaded by design
  (the write path is single-writer per Doc 04, and replay is one ordered scan),
  so vCPU count does not distort these specific numbers — but it does mean the
  dev box is not exercising contention the Pi's 4 cores might.
- **Mitigation provided:** `run.sh` runs both benchmarks **unchanged** on the Pi
  (auto-fetches a portable Temurin 21 if the Pi lacks `javac`; sqlite-jdbc
  3.45.3.0 carries aarch64/arm natives). Diff the `RESULT_B1` / `RESULT_B2` /
  `RESULT_B2C` lines against this report. On a disk-tight Pi, drop the 1e6 point
  (`B2_NS="10000 100000"`).

---

## 8. Where the spike code lives

`homesynapse-core/spike/dispatch-latency-and-log-growth/` (THROWAWAY; disposable;
slated for the hub's standing `git rm`):
- `src/com/homesynapse/spike/dispatch/DispatchLatencyBenchmark.java` — B1 (seam + D2)
- `src/com/homesynapse/spike/dispatch/LogGrowthBenchmark.java` — B2 (growth + replay)
- `run.sh` — one-shot: detect/fetch JDK, fetch sqlite-jdbc, compile, run both, print host facts
- `README.md` — labeled THROWAWAY; usage + the dev baseline + the storage caveat
- `lib/` — sqlite-jdbc + slf4j jars (fetched from Maven Central)

No production code, no design doc, no module-info outside `spike/`, and no
spine/decision/backlog file was touched. No mutating git command was run.

---

## ESCALATIONS TO THE HUB

1. **None that change a design doc or V1 scope.** The spike *validates* a
   RATIFIED decision (D1) and *sizes* an already-RATIFIED one (D4); it surfaces
   nothing that re-opens either. D2 is confirmed structural. No design-doc edit
   is warranted from these results; the only forward governance action is the
   already-planned one (register the D2 invariant id + pin its CI test at M7.4b —
   this spike gives it empirical backing and a harness shape).

2. **D4 cadence is sized but should be FROZEN against Pi data, not dev data.**
   The §6 numeric anchors (snapshot the high-volume projections so the live
   replay tail ≤ ~1e6 events; domain-log working-set ceiling ~1–2 GB / ~2–4M
   events) rest on a dev box and an *estimated* ×3–5 Pi CPU ratio. Recommend the
   hub treat §6 as the design input but gate the *frozen* cadence on Session D's
   actual Pi `run.sh` output (the knee re-confirm). Flagging so the hub schedules
   the Pi re-run before D4's thresholds are committed to the spine.

3. **Minor housekeeping (FYI, no action needed).** This sandbox's FUSE mount
   blocks `unlink`/`rm` of files the spike created (it disallows SQLite WAL
   entirely — recorded in §2 as a caveat). Two zero-byte leftovers
   (`spike/dispatch-latency-and-log-growth/dbtmp/spike-loggrowth-N1000000.db*`,
   truncated to 0 B) and a stray `lib/meta.xml` could not be removed in-session;
   the hub's standing `git rm` of the whole spike dir absorbs them. No disk or
   correctness impact.

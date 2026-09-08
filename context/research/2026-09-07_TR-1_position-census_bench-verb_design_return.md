# TR-1 — the position census as a bench verb (design return)

Read-only design lane, 2026-09-07 CT. No edit, build or run; nothing staged or committed. **HEADs:** `homesynapse-core` `39c8dd3da2c3e1f804810c2db8bf725689f0c35f` (clean) · `nexsys-bench` `4539f137f7f3fb5629b18e4ef90a2cd227c601da`. Paths are relative to `homesynapse-core/` or `nexsys-bench/`; `V00n` = the events migrations.

## §0 THE CARD — P1–P3 adjudicated first

**P1 "derivable from the two stores alone (no Core seam)" → SPLIT: strong half MET, literal half MISSED.** No Core read seam is needed — every input is in one SQLite file, `$HOMESYNAPSE_HOME/data/homesynapse-events.db` (`app/…/Main.java:88`; `tools/bench.sh:6-7`). But it is **three tables, not two**: `events` (V001:28-55), `subscriber_checkpoints` (V001:68-72), `subscriber_dead_letters` (V002:11-23) — **plus a fourth input in no store at all, the filter manifest**, built at registration (`HomeSynapseCore.java:604, 633, 734, 751, 778, 846`) and never persisted. Literally P1 is wrong; as meant — *nothing new in Core need be built or exposed* — right.

**P2 "per-night cost < 1 s of SQLite reads at household scale" → MET as stated; MISSED for the bench night's aggregate.** On the card: one rowid range-scan of ~50k–100k four-column rows (household rate, `context/assessments/2026-06-26_pi-dispatch-latency-and-log-growth_spike.md:263`) plus a six-row checkpoint read. The measured Pi-mapped figure for a **full 1e5 replay including payload decode** is ~0.4–0.5 s (spike §4) — a strict upper bound on a scan that decodes nothing. The bench night is different: 40 process-scoped censuses, each paying its own open and JIT — **seconds, not sub-second**.

**P3 "the persistent schema already carries a per-subscriber position row (no migration)" → MET, exactly.** `V001:68-72` — `subscriber_checkpoints (subscriber_id TEXT PRIMARY KEY, last_position INTEGER NOT NULL, last_updated INTEGER NOT NULL)`. **Rider:** a *current-position* row, not a history or a delivery ledger — the census is a post-drain high-water-mark comparison, never a per-position audit trail.

**First for Nick:** the verb needs ONE ruling — §3's B2, the STOP-gated stimulus grammar.

## §1 Q1 — the census's definition, and its derivability

For a window `(lo, hi]`, for every position `P` in `events` and every subscriber `S` in the manifest:

- `MATCHED(S,P)` := `S.filter` accepts `P` — a conjunction over `eventType`, `priority.severity()`, `subjectRef().type()` (`SubscriptionFilter.java`, `matches` body): exactly three columns — `event_type` (V001:32), `priority` (V001:39), `subject_type` (V001:37). **No envelope decode.**
- `DELIVERED(S,P)` := `checkpoint(S) >= P` **AND NOT** `EXISTS (subscriber_id=S, event_position=P)` in `subscriber_dead_letters` (V002:11-23, `UNIQUE(subscriber_id, event_position)`).
- `MISS(S,P)` := `MATCHED ∧ ¬DELIVERED`. Report misses and first missing position, per subscriber.

**Derivable without a Core read seam: yes** — the three tables share that file (`SqliteCheckpointStore.java:22`). **The algorithm already exists in the tree**, for one subscriber: `HeroLoopHardwareFreeIT.java:522-532` filter-matches the log, takes the max matching `globalPosition` and compares it to the checkpoint; its comment states the semantic outright — *"the bus advances a subscriber checkpoint only on MATCHING deliveries"* (`:514-520`). `ReplayTransitionIT.java:200-215` is the same predicate as a polling assert.

**Four reasons naive `checkpoint >= P` is wrong:**

1. **It over-reports.** LIVE writes the checkpoint **only on `SUCCESS`** (`InProcessEventBus.java:557,565-566`); a `PARKED` delivery (`SubscriberSupervisor.java:243-252`) writes nothing, and the next success writes a *higher* checkpoint over the parked position. Subtracting the DLQ rows is what makes the predicate sound.
2. **REPLAY ≠ LIVE.** `ReplayDriver.java:191` advances `currentPosition` past **every** paged row, matching or not, outside the filter branch — so the tail (`:166-168`) and cadence (`:201-203`) writes persist a **scan** high-water mark where LIVE/TRANSITION persist a **delivery** one (`InProcessEventBus.java:566`; `TransitionCoordinator.java:142,148`). `¬(checkpoint>=P) ⇒ not delivered` holds in both; the converse only after (1).
3. **One subscriber is exempt.** `state_projection` registers `atomicCheckpoint = true` (`HomeSynapseCore.java:633-636`) and the bus skips its per-delivery write in LIVE (`InProcessEventBus.java:565`), TRANSITION (`TransitionCoordinator.java:142`) and REPLAY (`ReplayDriver.java:166`), so its checkpoint lags delivery **by design** and reads as a miss that is not one — score it against `view_checkpoints` (V001:76-81, same-transaction, `core/persistence/MODULE_CONTEXT.md:158`).
4. **The denominator moves.** Retention deletes rows from `events` (`MaintenanceService.java:57,62`) and `global_position` is `INTEGER PRIMARY KEY AUTOINCREMENT` (V001:29; `core/event-model/MODULE_CONTEXT.md:204,236`) — the position set is **not dense**. Derive it from the table, pin the window, never span a maintenance pass.

## §2 Q2 — the data shape and the cost per night on the card

```
(i)   SELECT global_position, event_type, priority, subject_type FROM events
        WHERE global_position > :lo AND global_position <= :hi;   -- rowid range scan
(ii)  SELECT subscriber_id, last_position FROM subscriber_checkpoints;      -- K rows
(iii) SELECT subscriber_id, event_position FROM subscriber_dead_letters
        WHERE event_position > :lo AND event_position <= :hi;
```

Filters applied in RAM as the scan streams: `N × K` comparisons. Output = `K` rows — `subscriber_id · matched · delivered · missed · first_missed_position`.

**K = 6** production `subscribeRuntime` sites (`HomeSynapseCore.java:604, 637, 735, 751, 779, 846`): `registry_projection` (typed, `RegistryProjectionSubscriber.java:73-77`) · `state_projection` (`all()`, atomic) · `automation_engine` (`all()`) · `command_dispatch_service` (`CommandDispatchAssembly.java:95-98`) · `pending_command_ledger` (`PendingCommandLedgerAssembly.java:119-123`) · `integration_supervisor` (`…SupervisorAssembly.java:81-84`).

**N ≈ 50k–100k/night** (spike:263) → `N × K ≈ 3–6 × 10^5` in-RAM comparisons: not the cost driver. The driver is read (i) — ~488 B/event, constant across two orders of magnitude (spike §4); the Pi-mapped full-replay-with-decode figure of ~0.4–0.5 s at 1e5 is its upper bound, and `idx_events_type ON events(event_type, global_position)` (V001:58) helps when the manifest is type-narrow. **< 1 s per night on the card.**

## §3 Q3 — the bench verb's shape, and what it must not touch

**Name:** `bus-delivery-under-pressure`. **Tier:** AUTO — but **not a leg of the AUTO suite of record until R-5.**

**B1 — no `sqlite:` assertion exists, deliberately.** `SCENARIO_FORMAT.md` §2.1: *"No `sqlite:` assertion type exists in this format — deliberately… A needed-but-unexposed field is a contract conversation."* Echoed at `engine.py:6`. **So the design never asserts against SQLite.** The ITs compute their own census in-process — forced anyway, since `CheckpointStore` has no enumeration method (`:50,66`) and `InMemoryCheckpointStore`'s map is private (`:36`); they hold both stores (`ReplayTransitionIT.java:75-76`; `HeroLoopHardwareFreeIT.java:346` opens a real `homesynapse-events.db`) — and print one frozen token, which the scenario asserts with the **existing** `log:` + `extract:` + `min:` mechanic (exemplar: `boot-health.yaml:40-43` extracts `position=(\d+)` against a numeric floor). **Zero format change on the assertion side.**

```
bus.position_census: subscriber=<id> matched=<m> delivered=<d> missed=<n> first_missed=<p|none>
bus.position_census_total: runs=<k> subscribers=<K> missed=0
```
Positive: `log: "bus.position_census_total:"` + `same_line: ["missed=0"]`. Forbidden: `kind=LIVE_READ_EXHAUSTED` / `…TRANSITION_READ_EXHAUSTED`, on the emitter grammar at `HomeSynapseCore.java:558`.

**B2 — no test-runner stimulus, and the format is STOP-gated.** `engine.py:34` — `KNOWN_STIMULUS_KEYS = {"bench","api","usb","plug","operator"}`; `bench:` verbs are `restart|stop|start` (`SCENARIO_FORMAT.md` §1). "Two ITs ×K" is not expressible today, and §5 states further format changes are STOP-gated. Two paths; the lane recommends (b) until R-5: (a) an additive `gradle:`/`test:` stimulus verb — Nick's word, since it reopens a gated format; (b) **the verb runs outside the scenario grammar as a loop driver in the `fix1-loop.sh` lineage, contributing ONE extra digest line rather than a suite leg** — proven at `context/audits/2026-09-05_FIX-1_loops/instrument/fix1-loop.sh:17-30,47-49` (×K `--tests <FQCN> --rerun --no-daemon --offline`; **token tail by `grep -hoE 'bus\.delivery_anomaly: kind=[A-Z_]+'` on the JUnit XML**, `:30`) — the driver that produced the 176-run corpus of record (FIX-1 audit §0). **Load shape:** the Pi *is* the pre-empted machine the desk could not imitate (BEYOND §2 B-1) — the desk needed `start /affinity 3` + `vtParallelism=2` (`fix1-loop.sh:22-23`) and still went 0 RED in 38 pinned runs.

**OPEN — the verb's hard precondition.** Whether the card can run Gradle test tasks: `iac/bootstrap.sh:13-15` installs `jq`, `pipx`, `mosquitto-clients`, `ca-certificates`, `curl` and Docker — **no JDK, no Gradle** — while `tools/bench.sh:7` launches the app from a Gradle *install* layout there. No receipt in either repo settles it; `./gradlew --version` on the card does. Also left open: the reporting rule for a subscriber that SUSPENDs mid-window — `LIVE_READ_EXHAUSTED` leaves its checkpoint honestly behind (`InProcessEventBus.java:41-51`), so those misses are **real** and must read as SUSPENDED-with-N-behind, never a silent count.

**HANDS OFF.** The **9-leg AUTO suite of record** and its order (`scenarios/constants.yaml:157-182`): s31 at position 8 (Nick's 08-04 ruling), `command-s31-settle` **the park, LAST** (the 07-31 F1 ruling). A tenth leg changes the `9/9` floor and moves the park — nothing until **R-5**, the settle-instrument redesign (`context/assessments/2026-08-14_S10_close_ranked-program.md:22`). Likewise the **digest grammar** (`tools/runner/nightly_digest.py:133-139`, selftest-pinned at `:23`): the census rides as its **own** line beneath it, never a field inside it.

## §4 Q4 — the three uses as ONE instrument, and the D5 sentence each mints

**U1 — OR-BUS-SILENT-DROP's evidence closure.** R2 is **passive**: *"the `bus.delivery_anomaly` token absent AND both ITs green across the next 20 ordinary `main` runs"* (FIX-1 audit §8). Token-absence proves no drop was **detected**, and that same line records a **sixth** path *"named at source, unmeasured (the fan-out reorder, R3 → FIX-2)"* that emits nothing by construction. The census is the **active** half R2 lacks. *D5:* **"On `39c8dd3`, across 20 ordinary `main` runs of `HeroLoopHardwareFreeIT` and `ReplayTransitionIT`, zero `bus.delivery_anomaly` tokens were emitted AND the position census over each run's event store × checkpoint store × DLQ found zero matched-but-undelivered positions for any subscriber."** Refutable-by: one census miss, or one `*_READ_EXHAUSTED`.

**U2 — the MVP's event-loss audit.** Window = one night of the card's database; K = the six subscribers. *D5:* **"On the bench card at commit X, over N nights, every position appended to `homesynapse-events.db` that matched a live subscriber's filter was delivered to that subscriber, with zero matched-but-undelivered positions outside the DLQ — measured on the card's own database, not on the desk."** Refutable-by: one miss on one night.

**U3 — B-1/bus's minting measurement.** B-1's claim ends *"…and no checkpoint ever advanced past an undelivered matching position"* (BEYOND §2 B-1). **Nothing in the tree measures that clause today** — the ITs assert one subscriber's checkpoint reaches one target (`ReplayTransitionIT.java:167`; `HeroLoopHardwareFreeIT.java:530`): liveness, not completeness. The census **is** that clause's instrument, and the only one proposed. *D5:* B-1's sentence unchanged, its last clause measured rather than asserted.


<!--
file: context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md
purpose: The ratified §1 deeper-M7 automation-architecture decisions — the command-pipeline shape and the four near-term architecture commitments that shape M7.4 and protect the scalability / cloud / AIoT runway. The v6 hub's first substantive product. Sits above the milestone backlog; gates the Doc 07 §3.11 / AMD-90 reconciliation and M7.4.
audience: Nick, PM (v6 hub), the Core lane (M7.4), the DOCS/design lane (the §3.11 reconciliation + the Doc 17 beat), the Hardware bench (Session D).
state-type: decision record
status: RATIFIED 2026-06-25 (Nick co-signed D1–D4 + the Q2/Q5 confirmations in-session). **D5 (converter-DB direction) RATIFIED 2026-06-26** (Nick co-signed on Session A's return — `context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md` + the reconciliation memo `2026-06-26_v6-fanout-validation-and-dispatch-reconciliation_PM-memo.md`). Supersedes the v5 hub's "emit `command_issued` + keep dispatch in-process" lean (D1).
inputs: context/assessments/2026-06-23_prior-art-study_PM-assessment-and-forward-plan.md (the headline input — grade A−) + context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md (the raw return); design/16-superior-automation.md (Locked); design/07-automation-engine.md §3.11; the M7.3 closeout [REVIEW]s (pm-handoff beat 7); the parallel fan-out dispatch brief (Sessions A–D).
-->

# Deeper-M7 Automation Architecture — Decision Record (2026-06-25)

## Purpose and framing

This record settles the v6 §1 deeper-M7 architecture beat: **build the automation system for the long-term vision — highly scalable, maintainable for years, correct for both local-first and cloud-dependent setups, leverage-able toward AIoT — not just for V1.** It ratifies the one decision that gates M7.4 (the command-pipeline shape) and four near-term architecture commitments the 2026-06-23 prior-art study surfaced. The AIoT/cloud *vision* and its reserved seams are carried in a separate, co-equal artifact — the **Doc 17 "AIoT + Cloud Readiness" beat** (DRAFT; goes through the formal review→ratify pipeline) — kept cleanly apart from these concrete, M7.4-gating rulings on purpose.

**The thesis these decisions protect (Q2 + Q5 — RATIFIED as confirmations).** The immutable, causally-chained event log is the **universal substrate**: local-first = everything in the local log; cloud = the log replicates **outward** (additive, never a dependency for local function — INV-SA-02 reserves scope at the envelope, absent-defaults-to-local, no migration); AI = a first-class producer/consumer of that same log + the explanation projection. Doc 16 already engineers this (INV-SA-03 "explanation is a pure projection, no parallel trace store"; §3.5 federation/scope seam; §3.6 the local/cloud cut-line). The prior-art study independently confirmed the substrate and the seams as the right bets. **Nothing in V1's thin slice precludes the upscale/cloud/AIoT runway**; the decisions below make the command hop substrate-native, where today it is not.

---

## D1 — Command-pipeline shape: **logical event-driven, physically co-located** (RATIFIED; supersedes the v5 hybrid lean)

**Ruling.** The command pipeline is **event-driven**. The action executor **emits a `command_issued` event to the log**, and the dispatch service is a **real bus subscriber** that consumes `command_issued` and performs the dispatch. For MVP the dispatch subscriber runs **in-process / co-located** with the engine — so the architectural seam is correct (and scales later) while the dispatch latency is a single local hop. This **supersedes** the v5 hub's "emit `command_issued` but keep dispatch as an in-process call" hybrid lean and the current source's pure in-process collaborator (the M7.3 [REVIEW]s #2/#4). **Rejected and staying rejected:** pure in-process with no `command_issued` (it breaks the live ledger's only input and the "did it actually confirm?" hero causal chain).

**Why the discriminator is more load-bearing than it looks (record this).** The hybrid emits `command_issued` but then dispatches via a *separate in-process call* — so the log **records** the command while a side-channel **performs** it. That splits the source of truth: the log says one thing and the actuation path does another, and they can diverge (emitted-but-not-dispatched; dispatched-with-different-ordering). Full event-driven makes the dispatch service a real subscriber that **consumes `command_issued` and acts on it** — so the log is the **single source of truth for dispatch**, not merely its record.

**Three reasons that decide it:**

1. **Replay safety becomes structural.** A subscriber only acts in **LIVE** mode — so it cannot dispatch on replayed events. That makes the pure-function-replay rule (D2) **automatic**: a replayed side-effect would re-fire real-world commands, which is the safety-critical failure, and the subscriber-only-acts-in-LIVE property forecloses it by construction. The hybrid instead forces a hand-guard on the executor's in-process dispatch against replay — exactly the error-prone wiring that produced the M7.3 `@TempDir` leak.
2. **It scales additively.** Cross-process, multi-host, cloud federation, and AI consumers all **subscribe to the same ordered stream**. The hybrid's in-process call is a *re-architecture* the moment you cross a boundary — and cloud + AIoT are now first-class (Doc 17), so that boundary is coming. Building the seam now means later scale is a deployment change, not a rewrite.
3. **AMD-31 dispatch ordering comes free** from the log's global position — commands route in `global_position` order with no extra mechanism (Doc 07 §3.11.1's safety-critical-order guarantee, e.g. exhaust-fan-before-gas-valve, holds by construction).

**On the latency objection (the only thing the hybrid had): neutralized by co-location.** "Logical event-driven, physically co-located for MVP" means the dispatch subscriber is a genuine subscriber but runs in-process, so the added cost is a local emit→consume hop, not a network or cross-thread round-trip. **Session D** (the Pi command-dispatch-latency spike) is the empirical confirmation that the hop is negligible on Pi-class hardware; it is commissioned to the bench and bundled with the log-growth measurement (D4). The latency argument does not drive the architecture — co-location is the mitigation, and the seam correctness is the prize.

**What this makes concrete for M7.4a.** The executor emits `command_issued`; the **`command_dispatch_service` becomes a co-located subscriber on `command_issued`** (replacing the in-process `dispatch(...)` call), preserving AMD-31 ordering, with a paired `stop()` teardown (the M7.3 lesson — a runtime subscriber holds a read connection; mirror how `automation_engine` is closed). The pure-function-replay invariant (D2) and additive event versioning (D3) ride in as constraints. This **converges with where we already were**: M7.3's ledger needs `command_issued` as its only live input (nothing emits it today), and M7.4a was already slotted to "add the `command_issued` producer" — the research confirmed the *shape* and handed us the co-location mitigation.

---

## D2 — The pure-function-replay invariant (RATIFIED; formal registration is a forward action)

**Ruling.** Device dispatch — and **all external side-effects** (adapter calls, network I/O, notifications, anything observable outside the log) — **must never run on log replay**; they run **only** on new-command handling in LIVE mode. This is elevated to a **first-class architecture invariant** and backed by a **CI test** that replays a seeded log and asserts zero external side-effects.

**Why now and why first-class.** A side-effect on replay = **re-firing real-world commands** (the lights actually turn on again during a recovery replay) — the canonical, safety-critical event-sourcing failure the prior-art study flagged. It directly governs M7.3's ledger rebuild (which replays the command-lifecycle events) and M7.4's dispatch. D1's event-driven shape makes the rule **largely structural already** (the bus REPLAY→LIVE FSM stops subscribers from publishing during REPLAY; a dispatch subscriber acts only in LIVE) — this invariant **names, guarantees, and CI-pins** that property so it can never silently regress.

**Forward action (governance — not self-ratified here).** The canonical invariant-register entry (an `INV-…` id in `Architecture_Invariants_v1.md`) is a governance mechanic: it is registered through the normal review→ratify fold (watermark unaffected if folded as a doc-currency registration; a small AMD if a reviewer prefers). The PM does **not** mint the canonical id unilaterally. The **decision** (the rule + the CI test as an M7.4 gate constituent) is ratified here; the register entry follows.

---

## D3 — Additive event versioning (RATIFIED)

**Ruling.** Adopt **additive event versioning now**: an explicit event `version` field, an **upcaster framework** (old-version payloads are upcast to current on read), and a **full-history projection-rebuild test** that replays the entire log across version boundaries.

**Why.** "No destructive migration" (a standing anti-requirement) is **necessary but not sufficient** — "forgot to upcast" is a documented silent event-sourcing failure (an old event deserializes wrong after a schema change and the projection drifts without erroring). It is **cheap now and expensive to retrofit** (retrofitting versioning onto an already-populated immutable log is itself a migration). This coordinates with — and is distinct from — the AMD-94 1-byte envelope-version tag (which versions the *crypto envelope*); D3 versions the *event payload schema*. It is consistent with AMD-93 (forward-only, non-destructive migration) and AMD-92's type-residency discipline.

**Scope note.** Design + framework now; per-event upcasters are authored as schemas evolve. M7.4's new/changed event shapes are the first to carry it.

---

## D4 — Log retention / compaction / snapshot discipline (RATIFIED; design now, sized by Session D)

**Ruling.** Design **per-scope retention + snapshots + projection pruning now.** "Everything is a projection of the log" is correct, but the **log itself grows forever** and will hit Home Assistant's Recorder-DB scaling wall — worse on Pi-class hardware (SD-card wear, multi-GB DBs). This is a genuine gap we had not scoped.

**Why now.** Retention/snapshot strategy is a design that touches persistence, the projection-rebuild path, and the crypto/scope model (per-scope retention interacts with crypto-shred and the encrypted scopes) — cheaper to design before the log is large and before M9 starts producing real device-event volume. It must preserve the substrate thesis: snapshots and pruning are **derivable, replaceable optimizations over the log**, never a second source of truth (INV-SA-03 / INV-ES-01).

**Sized by Session D.** The Pi log-growth-rate + projection-rebuild-time numbers (Session D, bundled with the dispatch-latency spike) size the thresholds: at what log size rebuild becomes painful, and therefore the snapshot cadence + retention windows. Design-shape now; thresholds tuned on the data. Not a V1 build item beyond the seam unless Session D shows an early wall.

---

## D5 — Converter-DB leverage direction (**RATIFIED 2026-06-26** — adapt-the-data + curated-subset fallback)

**Ruling.** **Leverage an existing Zigbee converter database as declarative data** ("quirks-as-data"), **not** rebuild the device-quirk long tail. Concretely: **adapt-the-data for the declarative core** — embed a transformed, attributed dataset of `zigbeeModel`/`fingerprint` (device identity) + `exposes` (the capability model, which maps onto HomeSynapse's ZCL-aligned entity→capability model with modest transform) + standard ZCL cluster maps — **paired with a curated, prioritized subset + community-contribution path for the non-declarative long tail** (the `fromZigbee`/`toZigbee` transform logic — Tuya's `0xEF00` datapoints, Xiaomi deviations — which is code, not pure data). **Reject runtime-interop** (shipping Node + Z2M as a co-process — local-first/Pi/trust-brand + GPL-entanglement) **and rebuild** (multi-year, no differentiation payoff). Gates M9/device strategy; M9 scoping now unblocks.

**Basis (Session A, HIGH confidence on license / MED-HIGH on technical fit).** Licenses verified at the file level: `zigbee-herdsman-converters` **MIT**, `zigbee-herdsman` **MIT**, `zha-device-handlers` (`zha-quirks`) **Apache-2.0** — all permissive, **attribution/NOTICE obligation only**, no copyleft / no source-disclosure / no keep-separable. The **load-bearing distinction:** the GPL-3.0 is the **Zigbee2MQTT *application*** — a *different package* we do **not** vendor or link; the converter database + the herdsman library we consume are MIT. The one-runtime free→paid→enterprise model is compatible (embed/transform/redistribute/sublicense with attribution).

**Riders (do not gate the decision).** (1) **Commission a LOW-risk legal spot-check before the embed mechanics** — Apache-2.0 NOTICE/patent-grant mechanics at enterprise-sublicensing scale; the TS→Java derivative-work/attribution form; trademark/CSA "Zigbee" word-mark posture (a marketing-copy concern, not a data-embed one). These gate the *embed form*, not the direction. (2) **The bench (Session C) empirically validates the `exposes`→capability mapping** on the Hue A19 + SNZB-03P this week — a clean map raises technical-fit confidence; a messy one re-weights toward the curated-subset fallback sooner (the one recorded re-open trigger, alongside any upstream relicensing — pin the consumed version + record its license at ingest as a hedge).

---

## Reserved seams (carried to the Doc 17 beat — non-precluding, not built)

These are **not** built in V1; they are reserved so V1 forecloses none of them. The Doc 17 "AIoT + Cloud Readiness" beat (DRAFT) is the named architectural artifact that ties them to the vision:

- **AI seams (four):** AI-as-author (NL → component-based definitions that *expand into the sealed permits* — INV-SA-01; AX-7 versioning is the open gate); AI-as-reasoner (consumes the causal-chain/explanation projection — INV-SA-03); AI-as-device-intelligence (anomaly/prediction over the device event stream — just another log consumer); and the **AI-safety frame** — *AI proposes, the deterministic, explainable, no-autonomous-retry engine disposes; everything auditable* (INV-SA-04 / AMD-90-INV-01). The prior-art study found planner→verifier/safety-gate→deterministic-executor is the **emerging consensus** — this is potentially the "safest AIoT system" moat.
- **Cloud-replication seam:** the log replicates **outward** (event-log-shipping for federation), strictly additive; cloud projections/AI run cloud-side over the replicated log; never a dependency for local function (Doc 16 §3.5/§3.6; INV-SA-02; the §3.6 cut-line).
- **Federation (INV-SA-02), enterprise audit projection (Doc 16 §3.3, default-off), component-authoring (AX-7), crypto-shred (INV-PD-07)** — already reserved in Locked Doc 16; reaffirmed here as non-precluding.
- **SBOM + signed-update + vuln-disclosure seam** (EU CRA / UK PSTI runway) — table-stakes in the MVP→post-MVP window; reserve now (our local-first + auth-before-exposure posture is already ahead). Sizing is post-MVP (the CRA conformity-class question is Session-level, non-near-term).

---

## Downstream sequencing (what these rulings unblock, in order)

1. **The Doc 07 §3.11 / AMD-90 doc-vs-source reconciliation (§8.C)** adopts the **event-driven shape** ruled in D1 — it stops describing a pipeline the code never built (`ExpectationFactory`, `ConfirmationPolicy` on `CommandAction`, `command_issued` carrying the expectation) and describes the one this record ruled, reconciled against the frozen source the M7.3 [REVIEW]s mapped. Authored before M7.4 so M7.4 builds against reality.
2. **M7.4a** = the `command_issued` producer (off `StandardActionExecutor`'s dispatch) + the **co-located dispatch subscriber** on `command_issued` (replacing the in-process call), with a paired `stop()` teardown. Carries D2 (replay-safety) + D3 (versioning) as constraints.
3. **M7.4b** = the live `pending_command_ledger` subscriber (with `stop()` teardown) + the `pollExpirations()` `SharedScheduler` tick + the **E2E composition-root gate test** (boot the real core, fire a seeded automation, assert command issue→confirmation + a queryable causal chain). The replay-safety CI test (D2) lands in this gate.
4. **The Pi-performance spike (Session D)** validates D1's co-location latency and sizes D4's retention/snapshot thresholds — bundled onto the bench (the MG24 is on the desk).
5. **Session A** (converter-DB license) lands before M9 scoping → resolves D5.

---

## Ratification

- **D1, D2, D3, D4, and the Q2/Q5 substrate + local↔cloud confirmations: RATIFIED 2026-06-25 — Nick co-signed in-session.** The PM folds them into the spine (this record + the backlog M7.4 row + the snapshot) and proceeds to §8.C.
- **D5 (converter-DB direction): RATIFIED 2026-06-26** — Nick co-signed on Session A's return (adapt-the-data + curated-subset fallback; reject runtime-interop/rebuild). The LOW-risk legal spot-check is commissioned (gates embed mechanics, not the decision); the bench validates the `exposes`→capability mapping this week. M9 scoping unblocks.
- **The Doc 17 "AIoT + Cloud Readiness" beat is a DRAFT** authored separately and is **NOT** ratified by this record — it runs the formal review→ratify pipeline (the way Doc 16 went to Locked), Nick co-signs. The PM does not self-ratify it.
- **Forward governance action:** register the pure-function-replay invariant's canonical id (D2) through the normal review→ratify fold; add its CI test to the M7.4 gate.

## Empirical validation — fan-out v2 (2026-06-26; V2-A Pi spike)

The Session V2-A throwaway spike (`context/assessments/2026-06-26_pi-dispatch-latency-and-log-growth_spike.md`; harness at `homesynapse-core/spike/dispatch-latency-and-log-growth/`) validates the ratified rulings — it confirms, it does not re-decide:

- **D1 — CONFIRMED negligible (robust, filesystem-independent).** The co-located event-driven hop (executor emits `command_issued` → in-process synchronous bus → dispatch subscriber, same JVM) adds **≈ 1.9 ns/op** over a direct in-process call (direct ≈ 0.63 ns; event-driven ≈ 2.54 ns; median 20×20M ops, post-JIT) — **0.19 % of a 1 µs device dispatch, 3–5 orders of magnitude below the actuation it precedes**, even scaled ~5× for the Pi. The v5 hybrid's only argument (latency) is empirically closed.
- **D2 — PASS (the CI-gate template).** 1,000,000 replayed `command_issued` events → **zero** dispatch side-effects (the harness exits non-zero on violation). This is exactly the M7.4b D2 CI-gate shape; the spike hands the gate a tested template. **Forward action refined: register D2's canonical invariant id + pin this CI test at M7.4b**, using the V2-A harness.
- **D4 — sized, but FREEZE the thresholds on a Pi re-run.** Indicative dev-box curve: **≈ 488 bytes/event**; replay **44 ms @1e4 → 625 ms @1e6 → ~6–7 s @1e7**; on-disk **~465 MB @1e6 → ~4.6 GB @1e7** (the HA Recorder wall); **knee between 1e6 and 1e7**. Recommendation: **snapshot so the live replay tail stays ≤ ~1e6 events** (≈ weekly–biweekly at a busy-home rate → Pi cold-rebuild ~2–3 s); **per-scope + priority-tiered retention** (domain working set ~1–2 GB; CRITICAL rides longer; telemetry ring-bounded); snapshots/pruning stay purely derived (no second source of truth — INV-SA-03 / INV-ES-01/02). **Caveat:** the spike's sandbox FUSE mount disabled SQLite WAL / blocked `unlink`, so the **storage/append figures are indicative, not authoritative** — D4's numeric thresholds **freeze against the Session D Pi re-run** (the harness ships Pi-ready: aarch64 JDK 21 + sqlite-jdbc natives). D1 (latency) and D2 (replay) are CPU-bound and stand without the caveat.

<!--
file: context/planning/2026-06-06_post-M4-plan-and-M5-scoping.md
purpose: Decision-support synthesis — turns the three prior M4 deliberation artifacts (process retro, foundation-readiness assessment, language-replatform assessment) + a deep read of the candidate-next surface into a sequenced, research-aware post-M4 plan with M5 defined as a clear recommendation + the genuine alternatives + the open decisions. Nick brings this back to a separate deliberation conversation to decide. Does NOT lock M5.
audience: Nick (decision-maker); PM authored as senior systems architect.
update-cadence: one-shot (consumed when Nick picks the M5 posture and the W24 plan is written)
state-type: future (decision-support — NOT a decision, NOT a milestone, NOT an amendment)
status: CURRENT — issued 2026-06-06 (post-M4)
anchors: context/audits/2026-06-05_M4-retrospective.md; context/audits/2026-06-06_M3-M4_foundation-readiness-assessment.md; context/assessments/2026-06-06_core-language-replatform-assessment.md (+ 2026-06-06_rust-velocity-compounding-analysis.md); context/planning/2026-06-05_next-piece-recommendation.md; context/planning/2026-05-31_release-runway-roadmap.md; context/planning/phase-3-milestone-backlog.md
last-verified: 2026-06-06 against homesynapse-core HEAD `8ef9e9f` (M4 COMPLETE; watermark AMD-64; projectionVersion 5; working tree clean). New load-bearing code claims source-verified (file:line) this session; foundation-readiness findings (2026-06-06, HEAD-verified) trusted, not re-audited.
-->

# Post-M4 Plan + M5 Scoping — Decision-Support Synthesis

**What this is.** One decision-support document. It builds on three completed deliberation artifacts (it does not re-derive them), goes deeper than they did on the *candidate-next surface specifically* (the literal M5 code + the M6 entry-gate), and resolves the build-forward / reinforce-first / decide-the-irreversible / protect-the-launch tension into **a clear recommendation, the genuine alternatives weighed, and the specific calls you must make.** It deliberately does **not** lock M5 — that is your call in the follow-on deliberation. Freshness preflight this session: **PASS (all 10 checks).**

**The governing question.** Given everything we now know, what should M5 actually be, what is the right sequenced path M4 → M5 → M6 and beyond, and what research is a prerequisite to planning or building each piece?

**The one-line answer (defended in §4).** The originally-recommended M5 (Platform API + test-support) is **thinner than it looks** — its test-support force-multiplier is largely already built — while the highest-leverage work the two new assessments surfaced is **design/decision work that is either regret-proof or gates the very next milestone (M6).** Because that reinforcement work is mostly *not code*, it can run on the PM lane concurrently with a small Core build on the Coder lane and a protected non-Core lane. So the recommendation is a **deliberately-small, lane-tracked M5 window** — a small real Core build, a leverage-prioritized design/decision sprint (crypto entry-gate + the regret-proof schema decisions first), and a non-preemptable website/docs floor — **not** the pure-platform-API M5 as planned, and **not** an everything-bundle.

---

## 1. Consolidated current picture (the shared baseline)

A single-place synthesis of where we stand, with pointers rather than re-derivation. This is the floor the decision stands on.

**Where Core is.** M4 is **COMPLETE** at HEAD `8ef9e9f` (watermark AMD-64, `projectionVersion` 5, build GREEN — 145 tasks; working tree now clean). The event/persistence/bus spine, the typed `AttributeValue` pipeline end-to-end, the composition root, and the integration-api freeze are subsystem-grade *where code has touched them* (foundation-readiness §1). The next Core milestones are M5 (Platform API + test-support), M6 (Configuration + secrets/crypto), M7/M8 (Automation), M9 (Integration Runtime supervisor), M10 (REST API), M11 (WebSocket), M12 (Observability), M13 (Lifecycle full), M14 (Zigbee), M15 (integration + perf + the 72-h validation gate) — ~11 major groups (backlog `:143-159`).

**What M4 taught us about *how* we work (retro).** M4 shipped correct, well-governed work, but it was an epic wearing a milestone's name (~11 coding milestones, 18 amendments under one backlog line), the instruction-scope-miss / consumer-pin pattern cost two avoidable gate bounces, and the M4.C closeout itself shipped partial. The six process proposals — **P1** sizing smell-test (>3 sub-milestones or >3 amendments = too big), **P2** mandatory consumer/pin survey, **P3** ticked WUCP-Phase-2 checklist, **P4** lightweight block-amendment track, **P5** shift-left inspection-discoverable gate misses, **P6** non-preemptable non-Core floor — are the durable output. P1 and P6 bear directly on how M5 should be shaped.

**What the foundation-readiness assessment found (forward gap analysis, HEAD-verified 2026-06-06).** The foundation is deep enough to carry the next few milestones, but a handful of load-bearing contracts were **frozen or deferred as interface/Javadoc promises**, and they cluster — they do not scatter. The six "expand-now" items (§6.1): (1) AMD-65 `Expectation` codec; (2) promote the crypto Draft to an owned design doc; (3) reconcile Doc 06 `SecretStore` with the ratified AMD-60 `CredentialRotator`; (4) decide `actorRef` identity semantics; (5) specify the INV-SE-04 scoped-registry mechanism; (6) fix Doc 02 currency. The amplifier: **M6 is a dependency of M7, M9, and (transitively) M10, so a thin M6 fans out further than any other near-horizon milestone — and M6 is next.**

**What the language assessment (+ its velocity follow-on) found.** Recommendation: **stay Java, harden the named weaknesses, pre-position a *surgical* Rust seam at the INV-RF-01 boundary** — do not undertake a full Rust vNext now. The moat is language-independent; Java is itself a memory-safe language; the only durable Rust-specific win (no-GC determinism) addresses a requirement the current roadmap does not impose; opportunity cost is decisive. The velocity follow-on adds the decisive point that the *actual* production model (a solo founder + AI agents) is materially **more** productive in Java than Rust. Three no-regret moves matter to this plan: the **GraalVM native-image** spike and the **Generational-ZGC-vs-G1 Pi-4** measurement (both double as LTD-01 reversal-criteria data), and the **energy Mom-Test interviews** (the single piece of evidence that could legitimately flip the language call). **Crucial for sequencing: the event-log / schema decisions survive a re-platform unchanged — they are regret-proof under both the stay-Java and go-Rust futures.**

**The strategic frame.** With ~172 days to the Nov 25 target, Core is on/ahead of its own axis; the three non-Core tracks (Web UI, Website/Docs, Distribution) are **at zero** and are the runway's stated #1 risk (roadmap §5; retro §8). The binding constraint is a single effectively-serial pipeline with Nick as the human review/ratification gate — and 100% of it has gone to Core. The energy subscription is the strategy's named *primary* revenue path (Architecture Invariants §"energy", line 794).

---

## 2. The candidate work universe (deduplicated, tagged)

Every contender for "next," collected from all sources and de-duplicated, each tagged on the dimensions the decision needs. Legend: **Schema-irrev?** = frozen into the immutable event log (exponential cost curve) · **Regret-proof?** = survives a Java→Rust re-platform unchanged · **M6-gate?** = blocks correct scoping/!start of M6 · **Cheap?** = small effort relative to leverage · **Crit-path?** = on the Core critical path · **Research?** = external/technical research a prerequisite (P) / parallel (∥) / none (–) · **Lane** = Core(Coder) / Design(PM) / NonCore / Evidence.

| # | Candidate work item | Schema-irrev? | Regret-proof? | M6-gate? | Cheap? | Crit-path? | Research? | Lane | Source |
|---|---|---|---|---|---|---|---|---|---|
| **C1** | **PlatformPaths impls** (LinuxSystemPaths + LocalPaths) | no | yes | no | yes | M13 prereq | – | Core | next-piece §5; platform-api MODULE_CONTEXT Phase-3 Notes |
| **C2** | **HealthReporter impls** (SystemdHealthReporter sd_notify + NoOpHealthReporter) | no | mostly¹ | no | yes | M13 prereq | ∥¹ | Core | next-piece §5; `HealthReporter.java` |
| **C3** | **test-support "headline" doubles** (TestClock / SynchronousEventBus / NoRealIoExtension / InMemoryEventStore) | no | yes | no | — | force-mult | – | Core | next-piece §5 — **but see §4: already built** |
| **C4** | **Verification-foundation** (fault-injection / property-based / time-series-telemetry / hardware-in-the-loop harness) | no | yes | no | no | force-mult (M7/M9/M14/energy) | P | Core | brief synthesis #1 (gap the audits did *not* cover) |
| **C5** | **AMD-65 `Expectation` persisted codec** | no² | yes | no (M9-gate) | yes | M9 prereq | – | Core+Design | foundation-readiness F2/§6.1#1; backlog pre-M9 queue |
| **C6** | **Crypto design owner-doc** (promote 2026-03-22 Draft; KEK/DEK, per-category DEK, at-rest enc) | no | yes | **YES** | mod | M6 entry-gate | P (quick-scope) | Design | foundation-readiness §2.1/§6.1#2 |
| **C7** | **Doc 06 `SecretStore` ↔ AMD-60 `CredentialRotator` reconciliation** (scoped, atomic, durable rotation) | no | yes | **YES** | yes | M6/M9 | – | Design | foundation-readiness §2.2/§6.1#3 |
| **C8** | **`actorRef` identity semantics** (what it points at; how Tier-1 API keys map) | **YES** | yes | no | yes | multi-user + M10 | ∥ (light) | Design | foundation-readiness §4.4/§6.1#4 |
| **C9** | **Energy event-type family** (meter/tariff/grid/SOC/solar events) | **YES** | yes | no | yes | energy revenue path | ∥ (OpenADR/2030.5 if prioritized) | Design | foundation-readiness §4.1/§5; INV-EI-01 |
| **C10** | **Payload-typing posture** (string→typed `StateReportedEvent.value`/`CommandIssuedEvent.parameters`/`StateConfirmedEvent.*`) | **YES** | yes | no | mod | M7 triggers + AIoT | ∥ | Design | foundation-readiness §4.1 |
| **C11** | **INV-SE-04 scoped-`EntityRegistry` mechanism** (least-privilege, enforceable) | no | yes | no (M9-gate) | mod | M9 prereq | ∥ | Design | foundation-readiness F7/§6.1#5 |
| **C12** | **M6 config amendments AMD-66–71** (Research 5, assessed A−) | some³ | yes | **YES** (M6 start) | mod | M6 prereq | – (Research 5 done) | Design | backlog debt subsection; next-piece §2 |
| **C13** | **Doc 02 currency fix** (AttributeValue relocation; JSR-385→REC-93) | no | yes | no | yes | M6/M7/M14 | – | Design | foundation-readiness §2.3/§6.1#6 |
| **C14** | **W3 website/docs standup** (Docusaurus; positioning/architecture/privacy) | no | yes | no | mod | launch #1 risk | – | NonCore | retro §8/P6; roadmap §5; next-piece §4 |
| **C15** | **GraalVM native-image spike** (footprint/cold-start on Pi; closed-world vs dynamic loading) | no | n/a | no | mod | LTD-01 reversal data | P | Evidence/Core | language §6 no-regret #2 |
| **C16** | **Generational-ZGC-vs-G1 Pi-4 pause measurement** | no | n/a | no | yes | LTD-01 reversal data | P | Evidence/Core | language §6 no-regret #2 |
| **C17** | **Energy Mom-Test interviews** (utilities/aggregators/insurers) | no | n/a | no | yes | flips energy bet + language | ∥ | Evidence | language §5.2/§6 no-regret #3 |
| **C18** | **Doc-currency hygiene** (event-naming note Doc 01; PLAN-M4 SUPERSEDED marker; strategic-context-map; EventCategoryMapping reauth categories) | no | yes | no | yes | – | – | Design | retro §7.2/§7.4; backlog debt |
| **C19** | **SPIKE-RESTART** (Zigbee/Matter restart-frequency on Pi 5, NQ-6) | no | n/a | no | yes | M9 (validates default) | P (empirical) | Evidence | backlog pre-M9 queue; AMD-62 §6 |
| **C20** | **SPIKE-DC** (dual-coordinator design spike — no field precedent) | no | yes | no | no | M14 prereq | P | Design/Evidence | backlog pre-M14; Research 12 §5.2 |

*Footnotes.* ¹ `SystemdHealthReporter` uses `sd_notify` over a Unix-domain socket — a native-interop touchpoint that interacts with the GraalVM closed-world spike (C15), so it is "mostly" regret-proof and carries a light research/interaction flag. ² AMD-65 is *not* schema-irreversible in the event-log sense (it adds a codec for an already-frozen type), but it unblocks a frozen contract that cannot currently round-trip. ³ Some AMD-66–71 (config/secret shapes) touch persisted forms; the lightweight block-track (P4) applies to the trivial ones.

**The three clusters this resolves into.** (a) **Small real Core build** — C1, C2, optionally C5, optionally C4-scoped. (b) **High-leverage design/decision** — the M6 entry-gate (C6, C7, C12), the regret-proof schema decisions (C8, C9, C10), the M9 prereq (C11), and cheap doc fixes (C13, C18). (c) **Launch floor + evidence** — C14 (protected), C15/C16/C17/C19 (no-regret spikes + the decisive interviews). The key structural fact: cluster (b) is almost entirely **design/decision work, not code** — which is why it can run concurrently with (a) rather than competing with it for the Coder lane (it competes only for the Nick gate, which §3 addresses).

---

## 3. Sequencing logic

How the candidates order, and *why* — the dependency graph, the cost curve, the entry-gate, the lane split, and where the language decision interacts. This is the reasoning the M5 recommendation (§4) falls out of.

### 3.1 The dependency graph — M6 is the fan-out hub, and it is next

The forward dependency chain (backlog `:149-159`): **M6 (Configuration) is a hard dependency of M7, M9, and M10**, and M9 fans into M14; M10 into M11. No other near-horizon milestone fans out as far. M5, by contrast, **blocks nothing** — its consumers (PlatformPaths/HealthReporter impls) are leaf wiring that M13 eventually composes. So the sequencing pressure is not "what unblocks M5" (nothing does) but "**what must be true for M6 to start correctly**," because M6 is the next critical-path milestone and the most expensive one to get wrong.

What M6 needs before it can start coding (all currently absent):
- **The crypto design owner-doc (C6).** Source-verified this session: `SecretStore` is interface-only with **zero production impls** (`config/configuration/src/main/java` — no `implements SecretStore`/`ConfigurationService` class), and Doc 06 owns only a *narrow single-static-key* AES-256-GCM store (`/etc/homesynapse/.secret-key`, one key, `0400`; Doc 06 `:165`, `:788`). The per-category DEK / crypto-shred key hierarchy that **seven design docs** defer to lives only in an unpromoted 2026-03-22 Draft. M6 cannot build the store against a design that no numbered doc owns.
- **The Doc 06 ↔ AMD-60 reconciliation (C7).** `CredentialRotator.rotate(Map)` is **ratified** (AMD-60, in integration-api) and integration-scoped/atomic/durable — but Doc 06's `SecretStore` (verified: `resolve/set/remove/list` over a flat global namespace, no `rotate`, no scoping) has **no awareness of it**. A ratified contract with no home in its owner doc.
- **The M6 config amendments AMD-66–71 (C12).** Research 5 is assessed (A−) but the amendments are not authored/ratified; M6 cannot start coding until they are. (Good news the next-piece rec already flagged: AMD-67's REC-41 blocker was cleared by the M4.C config-schema-versioning freeze — confirm at authoring.)

**Therefore the M6 entry-gate (C6 + C7 + C12) is the spine of the near-term sequence** — it is the work that determines whether M6 starts clean or, like M4, discovers its true size in arrears. It is all PM/design-lane work.

### 3.2 The cost curve — the schema-irreversible decisions are cheapest now and regret-proof

Three decisions are frozen into the **immutable, replay-deterministic event log**, so their cost curve is *exponential, not linear* — they get more expensive with every event the log accrues, because changing them later means a schema migration over an accrued corpus:

- **`actorRef` (C8)** — verified a bare nullable `Ulid` on `EventEnvelope` (`EventEnvelope.java:112`), polymorphic "person or actor" by convention (LTD-04, to avoid a sealed hierarchy). It is **not merely reserved — it is live**: every event already carries it and it round-trips through persistence (foundation-readiness §4.4, HEAD-verified). Deciding what it points at, and how Tier-1 API keys map onto it, is cheap now and a migration later.
- **Energy event-type family (C9)** — verified **zero energy event types** in `EventTypes.java` (53 constants, none energy; energy rides the generic `telemetry_summary` at `:185`). The slots are reserved (`EventCategory.ENERGY`, `EntityType.ENERGY_METER`) but the event vocabulary is absent. Adding the family is cheap now; retrofitting energy semantics onto a log full of generic telemetry is not.
- **Payload typing (C10)** — `StateReportedEvent.value`, `CommandIssuedEvent.parameters`, `StateConfirmedEvent.*` are serialized-JSON `String` (foundation-readiness §4.1). The string→typed migration is a real future cost the "first-class from day one" framing hides.

The decisive property, from the language assessment: **these decisions survive a Java→Rust re-platform unchanged** — the event log is the asset that carries over. They are therefore **regret-proof under both the stay-Java and the go-Rust futures — the safest investments on the board.** That makes them the ideal content for a window where the language question is still open: you can commit to them now without prejudicing the language call, and waiting only raises their price. (This is why "decide-the-irreversible-now" is not in tension with "the language decision is unresolved" — it is the resolution.)

### 3.3 The Core-critical-path vs non-Core-parallel split (P6)

The roadmap's posture (A) — interleave non-Core now — must be *structural*, not aspirational, or it resolves to "never," as W23 empirically proved (website/docs was W23 Goal 4 and was deferred when M4.C consumed the week). The website/docs lane (C14) is ~80% Core-independent (positioning/architecture/privacy; only the auto-generated API/config reference is M10/M11-gated, ~Aug). It competes with Core for *neither* the Coder lane *nor* the Nick gate in any deep way — its bottleneck is content authoring. So it is the natural protected parallel lane (P6: a defined first-week increment that Core is **not allowed to preempt**). M5 being the smallest Core milestone on the board is precisely the slack that lets the floor be installed without stalling Core — the next-piece rec's §4 logic, which survives intact.

### 3.4 Where the language decision interacts — and where it deliberately doesn't

- It **does not** gate the schema decisions (C8/C9/C10) — those are regret-proof (§3.2). This is the most important interaction: **M5 does not need the language decision resolved first.**
- The **no-regret spikes (C15/C16)** are platform/build-foundation work that belongs in or beside M5 (brief synthesis #2) and simultaneously generates the LTD-01 reversal data — so they are Coder-lane work that double-counts as decision evidence. Note the one real interaction: `SystemdHealthReporter` (C2) is a native-interop (`sd_notify`) touchpoint, and the GraalVM closed-world spike (C15) should observe it — so sequence C2 and C15 to inform each other.
- The **energy interviews (C17)** are the single piece of evidence that most changes the plan: they bear on both the **energy bet** (do we prioritize C9 + build energy features, or just lay the regret-proof event family and wait?) and the **language call** (the only live LTD-01 reversal trigger is a contracted hard-real-time energy-determinism requirement). They are cheap and should be commissioned near-term regardless of the M5 shape.

### 3.5 The contract-freeze-readiness gate (a systemic fix, applied here)

The M4 pattern that produced AMD-65 and INV-SE-04 was *freezing a contract as a Javadoc/interface promise that could not actually be honored* — AMD-65 froze a `CapabilityInstance` that cannot round-trip; INV-SE-04 froze a least-privilege promise that appears in **0 code files**. The systemic fix — a sibling to the P2 consumer/pin survey — is a **contract-freeze-readiness gate**: *before any contract is frozen, prove it (a) round-trips / is enforceable and (b) has an owner doc.* Applied to this window:

- **M5-Core (C1/C2):** low-stakes — PlatformPaths/HealthReporter are *already-frozen interfaces* owned by Doc 12 §8.2/§8.3; M5 only adds **implementations**, not new frozen contracts. The gate is satisfied by construction.
- **M5-Design (C6/C7/C11):** this is where the gate bites. The crypto owner-doc, the rotation reconciliation, and the INV-SE-04 mechanism must each be proven *enforceable and owned* before M6/M9 build on them — otherwise we repeat the AMD-65 mistake one milestone later. AMD-65 itself (C5) is the **proof-case template**: it ships an executable acceptance test (`@Disabled("AMD-65 pending")` `capabilityAdded_onOff_roundTrips`) that *is* the round-trip proof. Every contract this window produces should carry an equivalent proof before downstream milestones lean on it.

### 3.6 The sizing discipline this window must respect (P1)

The retro's P1 smell-test (>3 sub-milestones or >3 amendments ⇒ too big) is the single biggest risk to any blended M5. A window that bundles platform impls + AMD-65 + AMD-66–71 + the schema decisions + the crypto owner-doc + test-support + two spikes + website would be **M4's mistake exactly** — an epic wearing a milestone's name. The fix is not to refuse the multi-lane shape (the work genuinely parallelizes); it is to **charter each lane as a first-class tracked piece with its own backlog row and done-when**, so the true size is visible up front and no single "M5" line hides it. The multi-lane window is sound *if and only if* it is lane-tracked.

---

## 4. Recommended M5 — definition + scope, with the genuine alternatives weighed

### 4.1 The finding that reframes M5: its originally-planned content is thinner than it looks

The next-piece recommendation (2026-06-05, which predates both new assessments) scoped M5 as "Platform API + test-support," resting much of its case on test-support being a **force-multiplier** — building `InMemoryEventStore / SynchronousEventBus / TestClock / NoRealIoExtension` so every later milestone is cheaper to test. Deep read of the surface this session shows **all four already exist**:

- `TestClock` — `testing/test-support/.../TestClock.java` (`.at(Instant)`, advance/set/freeze). ✓
- `SynchronousEventBus` — `testing/test-support/.../SynchronousEventBus.java` (bridges the pull-model via `registerHandler`/`notifyEvent`). ✓
- `NoRealIoExtension` (+ `@RealIo`) — `testing/test-support/.../NoRealIoExtension.java`. ✓
- `InMemoryEventStore` — `core/event-model/src/testFixtures/.../InMemoryEventStore.java`, with `InMemoryEventStoreTest` **and** the 27-method `EventStoreContractTest` it passes. ✓

These shipped in the **M1.x test-first preparation wave** and via incremental fixtures. So the headline force-multiplier the M5 case rested on is **already banked.** What remains for test-support is *scattered placeholder fixtures* (state-store `InMemoryStateStore`/`TestProjectionFixture`; persistence `InMemoryCheckpointStore`/`InMemoryTelemetryStore`; integration-api `TestAdapter`/`StubCommandHandler`) — low-value, and best built just-in-time by the consuming milestone (which is how `TestCapabilityFactory`, `StubIntegrationContext`, etc. already arrived). **The platform-api half (C1/C2) is genuine but small** — leaf implementations of two already-frozen interfaces. **Net: M5-as-planned is a small platform-impl milestone whose test-support rationale is mostly spent.** This is the central place this synthesis *disagrees* with the earlier recommendation.

The brief's synthesis #1 rescues test-support, but only by **re-scoping** it: the verification-*foundation* the harder modules need — systematic **fault-injection**, **property-based** testing, **time-series/telemetry** test fixtures, and **hardware-in-the-loop** for M14 — is genuinely missing (the current approach is the 10 contract suites + ~1,425 `@Test` + the `-PpiProfile` integration-tests + ad-hoc `failOnNthEvent` injection). That is real force-multiplier work for M7/M9/M14/energy — but it is **new scope (C4)**, not the next-piece rec's doubles, and it needs a scoping research pass first.

### 4.2 Reserved slots — validated vs name-only (so M5 doesn't build on a hollow one)

The brief's explicit check (AMD-65 proved a reservation can be a liability):

- **Validated (real, built — do NOT rebuild):** the test-support doubles C3 (TestClock/SynchronousEventBus/NoRealIoExtension/InMemoryEventStore, contract-tested); the typed `AttributeValue` pipeline; the event/bus/persistence spine.
- **Partially validated (interface real + owned; impl absent — the real M5-Core work):** `PlatformPaths`/`HealthReporter` (frozen interfaces, Doc-12-owned; impls absent → C1/C2 build them); `Floor`/`Area` (records real; registries interface-only; `FloorId` not yet Jackson-registered — a tiny now-fix).
- **Name-only / hollow (frozen as Javadoc — the AMD-65 liability pattern; do NOT build on as if real):** `Expectation` codec (C5 — frozen, cannot round-trip); **INV-SE-04** scoped registry (C11 — string appears in **0 code files**); `IsolationLevel.RESERVED_SUBPROCESS` (reserves a name the supervisor rejects); `SecretStore` (interface, **zero impls**, narrow vs INV-PD-07); the **energy slots** (`EventCategory.ENERGY` + `EntityType.ENERGY_METER` exist; **zero energy event types** — C9).

The lesson for M5: its **Core build (C1/C2) stands on validated/partially-validated slots** (safe), while the **highest-value reinforcement (C5/C6/C9/C11) is exactly the hollow-slot work** — which is why that work belongs on the design lane with the contract-freeze-readiness gate (§3.5), not deferred to the milestone that will trip over it.

### 4.3 Recommendation — a deliberately-small, lane-tracked M5 window

**Recommended M5 = a small Core build + a leverage-prioritized design/decision sprint + a protected non-Core floor, with the no-regret evidence riding alongside — each lane chartered as a first-class tracked piece (P1).** Concretely, four lanes:

- **Lane A — M5-Core (Coder), deliberately small.** C1 `PlatformPaths` (Linux + development) + C2 `HealthReporter` (systemd + no-op) — real, dependency-free, a M13 prerequisite, standing on validated interfaces. **Fold in C5 (AMD-65 `Expectation` codec)** as a small Coder WU (M9 prep, context fresh, AMD-52 float-determinism precedent, lightweight block-track per P4). **Register `FloorId` in `PersistenceJacksonModule`** (trivial unblock). *Defer C4 (verification-foundation) unless* the §6 scoping research returns it as worth a dedicated piece — do **not** rebuild the C3 doubles that exist.
- **Lane B — M5-Design (PM), the highest-leverage work, sequenced by leverage.** In order: **(1) the M6 entry-gate** — C6 (promote the crypto Draft to an owned doc; reconcile with Doc 06) + C7 (Doc 06 ↔ AMD-60 rotation) + the **INV-PD-07 MVP-scope resolution** (§4.4); **(2) the regret-proof schema decisions** — C8 `actorRef`, C9 energy event family, C10 payload-typing posture; **(3)** C12 (AMD-66–71 authoring, so M6 can start) and C11 (INV-SE-04 mechanism, M9 prep); **(4)** cheap doc fixes C13/C18. Apply the contract-freeze-readiness gate (§3.5) to everything in (1)–(3).
- **Lane C — M5-NonCore (protected, non-preemptable per P6).** C14 website/docs first increment (Docusaurus scaffold + 3–4 positioning/architecture/privacy pages). Not tradeable to accelerate Lane A.
- **Lane D — Evidence (parallel/commissioned).** C15 GraalVM spike + C16 GenZGC-vs-G1 Pi measurement (Coder-lane spikes that double as LTD-01 reversal data; sequence C15 to observe C2's `sd_notify`), and **C17 energy Mom-Test interviews** (near-term priority — the decisive evidence). C19 SPIKE-RESTART schedules when the M9 window opens.

**Why this and not the alternatives:** it captures the work that is *either regret-proof or gates the very next milestone* (the two categories that are genuinely cheaper now), keeps a small shippable Core increment and the launch floor, and lets the design-heavy reinforcement run concurrently because it is not code. Its cost — the Nick-gate load of several amendments and the P1 sizing risk — is managed by **sequencing Lane B by leverage** (the M6 entry-gate and the regret-proof decisions first; everything else can slip to just-before-its-consumer) and by **lane-tracking** (so it never becomes an untracked epic).

### 4.4 The alternatives, weighed honestly

**Alternative 1 — Pure Platform-API M5, as originally planned (build-forward).** *What:* C1/C2 (+ the C3 doubles, except they exist) as a single small Core milestone; defer all reinforcement to M6's doorstep. *For:* smallest, fastest, lowest-risk, one clean Coder milestone; respects P1 trivially; zero Nick-gate amendment load. *Against:* its test-support force-multiplier rationale is **already banked** (§4.1), so its Core value is thin; it does **nothing** for the M6 entry-gate (so M6 hits the crypto vacuum on day one, exactly the M4 "discover the size in arrears" failure) and lets the regret-proof schema decisions keep accruing cost. **Verdict:** the safest *milestone* but the weakest *use of the window* — it optimizes the thing that isn't the risk.

**Alternative 2 — Foundation-reinforcement bundle (reinforce-first).** *What:* make the window the crypto owner-doc + schema decisions + AMD-65 + INV-SE-04 + contract reconciliations, with little or no Core build. *For:* maximally de-risks M6 and the irreversibles; spends the window on the highest-leverage work; all regret-proof. *Against:* it is almost entirely **PM/Nick-gated design work**, which *intensifies* the serial review/ratification bottleneck the language assessment named as the real constraint; it produces **no shippable Core increment**; and a bundle of 6+ amendments is the **P1 sizing failure** unless rigorously lane-tracked. **Verdict:** right about *what* matters, wrong to starve the Coder lane and overload the Nick gate all at once.

**Alternative 3 — Blended multi-lane M5 (RECOMMENDED, §4.3).** *What:* small Core (Lane A) + leverage-prioritized design sprint (Lane B) + protected non-Core (Lane C) + no-regret evidence (Lane D), lane-tracked. *For:* captures the regret-proof + M6-gating work, keeps a small Core increment and the launch floor, parallelizes design vs code. *Against:* the most coordination; demands the discipline of lane-tracking (P1) and leverage-sequencing the Nick gate; "M5" becomes a *window* of tracked pieces rather than one milestone — which is a vocabulary change worth making explicit. **Verdict:** the best risk-adjusted use of the window *if* the P1/P6 discipline holds — which is the whole point of stating it as lanes.

### 4.5 "Done-when" for the recommended M5 window

Lane A: C1/C2 (+ C5, + FloorId registration) committed, full `./gradlew check` GREEN, PM WUCP Phase 2 → APPROVE, closeout run against the ticked artifact checklist (P3). Lane B: the crypto owner-doc exists and is reconciled with Doc 06 (C6/C7); the INV-PD-07 scope question is **decided** (§4.4 / §7); the three schema decisions are authored as design/amendment artifacts that pass the contract-freeze-readiness gate; AMD-66–71 are ratified so M6 can start. Lane C: site builds locally/staging; positioning/architecture pages drafted. Lane D: both Pi spikes report numbers into the LTD-01 reversal criteria; the energy interviews are scheduled/underway.

---

## 5. Post-M5 sequence sketch (enough to confirm M5 sets up M6 and doesn't corner the harder modules)

**M6 — Configuration + secrets/crypto (next Core critical-path milestone).** M5's Lane B *is* M6's entry-gate, so M6 starts clean only if Lane B lands: the crypto owner-doc (C6) + Doc 06/AMD-60 reconciliation (C7) + ratified AMD-66–71 (C12) + the INV-PD-07 scope decision (which sets M6's *size* — see §7). M6 then builds the YAML pipeline, JSON-Schema validation, the secret store, and hot-reload atomic swap — on M5's `PlatformPaths.configDir()` (C1) and the existing test-support. **The crucial check: do not let M6 discover its size in arrears as M4 did.** If the INV-PD-07 decision is "MVP per-scope key management + crypto-shred ≥1 category," M6 is *large* (a DEK/KEK key manager, not just the narrow `secrets.enc` store) and should be chartered as multiple first-class pieces from the start (P1).

**M7/M8 — Automation.** Depends on M6 (config) + state-store + event-bus. Foundation-readiness flags `core/automation` as 100% Phase-2 scaffolding (F1 — a from-scratch engine, not interface-fill-in; heed the *sizing* warning) and the `WithinTolerance.evaluate()` confirmation primitive as a throwing stub (F2 — the same `Expectation` family AMD-65/C5 addresses). M5's C5 (AMD-65 codec) + C10 (payload typing) + C9 (energy events, which automations will trigger on) are the M5-window decisions that keep M7 from being cornered. Also flagged: the Doc 02↔Doc 07 `floor:`/`entity_role:` selector seam (add at M7).

**M9 — Integration Runtime supervisor.** Depends on M6. M5's C11 (INV-SE-04 scoped-registry mechanism) and C5 (AMD-65 — M9 must not publish command-bearing `CapabilityAdded` until it lands) are the M5-window M9-prereqs. C19 (SPIKE-RESTART) validates the restart-intensity default before M9 hardens it. The integration-api freeze is otherwise a well-shaped M9 surface (foundation-readiness §4.3).

**M10/M11 — REST/WebSocket APIs (the Web-UI dependency, ~Aug).** Depends on M6 + M9. M5's C8 (`actorRef` semantics) feeds the M10 auth/identity surface; the website/docs auto-generated API reference (the Core-gated 20% of C14) unblocks here. INV-SE-02 (auth mandatory) is currently unmet on live endpoints (F9) — an M10 build item, flagged not now.

**M12–M15.** Observability (telemetry ring store + DLQ — F10), Lifecycle-full (M5's C1/C2 impls compose here — M13), Zigbee (C20 SPIKE-DC ~Aug precedes the M14 briefing; the generic normalized-telemetry event shape should be defined before M14 wires it Zigbee-only), and the M15 integration + 72-h validation gate.

**Does M5 corner anything?** No — and that is the test the recommendation is built to pass. M5-Core (C1/C2) is leaf wiring on frozen interfaces; it composes cleanly at M13. M5-Design lays the regret-proof decisions and the M6 entry-gate *ahead* of the modules that need them, with the contract-freeze-readiness gate ensuring it doesn't freeze new Javadoc-only promises. The one thing to watch: **the energy event family (C9) and the payload-typing posture (C10) are decisions that, if made narrowly, could under-serve M7/energy** — so author them with the energy interview evidence (C17) in view, or author the *shape* now and stage the breadth (§7).

---

## 6. Research agenda (per item: prerequisite / parallel / none)

The pre-M5/M9 design pipeline is otherwise complete — Research 4/5/6 cover the M5–M9 design surface, Research 6 NQ-1..6 locked 2026-06-04, Research 7v2/12 returned A−/A. So the research *this plan* needs is narrow and targeted. Per item: **role** (Prerequisite — must precede planning/building the item / Parallel — informs but doesn't block / None), **what specifically**, and **depth** (quick-scope via the `deep-research` skill where it changes the plan, vs a full research→AMD brief commissioned separately).

| Item | Role | What specifically | Depth |
|---|---|---|---|
| **C6 crypto owner-doc** | **Prerequisite** (to M6) | KEK/DEK key-management, per-category DEK, crypto-shredding key-destruction patterns, key derivation on headless Pi (PBKDF2/Argon2id), TPM2-on-Pi-5 posture. **But:** the substance largely exists — the 2026-03-22 Draft (468 lines: 3 key domains, write-path integration, chain-hash, Ed25519 signing, Pi4/Pi5 crypto-extension asymmetry, phased what-ships-when) + Research 5's secret-management section. So this is **promotion + reconciliation**, not greenfield research. | **Quick-scope** to validate KEK-DEK/crypto-shred patterns against the Draft's choices + close its OPEN-01/02/03; the heavy lifting is *design/promotion*, not new research. |
| **C9 energy event family** | **Parallel** (to authoring) — but **the interviews are decisive** | OpenADR 3.0 (REST/JSON VEN) / IEEE 2030.5-CSIP / FERC-2222 event vocabulary *if* energy is prioritized — to ground meter/tariff/grid-signal/SOC/solar event types in the real protocols. | Full brief **only if** the energy bet is "yes" (§7); otherwise author the regret-proof *shape* now from the strategy docs and defer protocol-fidelity to the energy-feature milestone. |
| **C4 verification-foundation** | **Prerequisite** (to scoping C4 as a piece) | Property-based testing for the JVM (jqwik) on event-sourced invariants; systematic fault-injection patterns; time-series/telemetry test fixtures; hardware-in-the-loop for M14. The gap the audits did not cover. | **Quick-scope** to decide whether C4 is a dedicated M5 piece or rides each consuming milestone JIT. |
| **C15 GraalVM native-image** | **Parallel** (no-regret) | Closed-world/reflection config vs the integration runtime's dynamic-loading ambitions (LTD-17); footprint/cold-start on Pi-4; interaction with `sd_notify` native interop (C2). Doubles as LTD-01 reversal data. | **Spike** (Coder-lane), not a literature brief. |
| **C16 GenZGC-vs-G1** | **Parallel** (no-regret) | Pause measurement on Pi-4 under INV-PR-02 budgets; GenZGC memory headroom at the 512 MB target. Doubles as LTD-01 reversal data. | **Spike** (Coder-lane). |
| **C17 energy Mom-Test interviews** | **Parallel** but **near-term priority** | The §5.2 questions — do energy/B2B buyers ever contract hard-sub-second deterministic control; is language/runtime ever an RFP line item; what makes a dispatch number trustable. The single piece of evidence that flips both the energy bet (C9 priority) and the language call. | Field interviews (5–10 contacts), not desk research. |
| **C8 actorRef / C10 payload typing / C11 INV-SE-04** | **None** (parallel at most) | Internal design decisions grounded in the existing model + invariants; C11 can borrow capability-token / scoped-registry prior art lightly. | Design, not research. |
| **C19 SPIKE-RESTART / C20 SPIKE-DC** | **Prerequisite** to M9 / M14 respectively | Empirical Zigbee/Matter restart-frequency on Pi 5 (NQ-6); dual-coordinator aggregation (no field precedent — Research 12 §5.2). | Empirical spikes; SPIKE-DC may output a Doc 08 amendment. |

**The research that is genuinely *new* (not already in the pipeline): the crypto-pattern quick-scope (C6), the verification-foundation scoping (C4), the energy protocol brief (C9, conditional), and the two language spikes + energy interviews (C15/C16/C17).** Everything else is design or already-commissioned. Your job for this window is a *research-aware plan*, not to run the heavy research now — the project's research→AMD→code pipeline commissions that separately.

---

## 7. Open decisions for Nick (the calls the deliberation must make)

Each framed as a crisp choice with the recommended default. These are the deliberation's agenda.

**D1 — The M5 definition / posture.** *Choice:* (a) **Blended multi-lane M5** — small Core + leverage-prioritized design sprint + protected non-Core, lane-tracked *(recommended)*; (b) pure Platform-API M5 as originally planned; (c) foundation-reinforcement bundle. *Recommended default:* **(a)**, explicitly scoped small and chartered as first-class lanes (P1), with Lane B sequenced by leverage. *Why it's yours:* it trades milestone simplicity for window leverage and changes "M5" from one milestone to a tracked window — a vocabulary call only you should make.

**D2 — The INV-PD-07 MVP-scope question (the sharpest one; it sizes M6).** *Choice:* is crypto-shredding **MVP** or **post-MVP**? The invariant's own text says MVP — *"The MVP must implement the per-scope key management infrastructure and define the encryption scope categories. Crypto-shredding must be operational for at least one data category"* (`Architecture_Invariants_v1.md:427`). The 2026-03-22 crypto Draft §5 says the opposite — envelope encryption + crypto-shredding are **Tier 2 / post-MVP**, with v1.0 = hash chain + package signing only. **These directly contradict, and nobody has reconciled them.** *Recommended default:* honor the invariant — treat the **per-scope key-management *infrastructure* + crypto-shred for ≥1 category (identity/presence) as MVP**, because it is the trust-brand differentiator the moat rests on — but **stage the breadth** (one category at MVP, others incremental) and **decide it explicitly** rather than letting the Draft's "Tier 2" silently override the ratified invariant. *Why it's yours:* it's a strategic privacy/trust-brand call and it sets whether M6 is a small store or a large key-management subsystem.

**D3 — The non-Core posture (P6).** *Choice:* (a) **protected, non-preemptable website/docs floor in the M5 window** *(recommended)*; (b) pure-Core again, accept the risk; (c) cut MVP scope. *Recommended default:* **(a)** — W23 proved "interleave when Core allows" resolves to "never," and M5's small Core size is the cheapest place to install the floor. *Why it's yours:* it's the launch-vs-Core-velocity tradeoff, and the runway's #1 risk.

**D4 — The energy bet.** *Choice:* is energy the *primary* product (per strategy `:794`)? If yes → prioritize C9 (energy event family) now *and* commission C17 interviews as a near-term priority. *Recommended default:* **author the regret-proof energy event *shape* now regardless** (it's cheap and schema-irreversible), **commission the interviews near-term**, but **do not build energy *features* until the interviews return** — the shape is no-regret; the features are a bet. *Why it's yours:* it's the core product-identity question, and it's coupled to D5.

**D5 — The language-deliberation interaction + timing.** *Choice:* do the GraalVM + GenZGC spikes (C15/C16) and the energy interviews (C17) ride the M5 window? *Recommended default:* **yes** — the spikes are Coder-lane no-regret work that double as LTD-01 reversal data; the interviews are the single most decisive evidence and are cheap. *Explicitly note:* the M5-Design schema decisions (C8/C9/C10) are **regret-proof under both the stay-Java and go-Rust futures**, so M5 does **not** require the language decision to be resolved first — running the spikes/interviews *during* M5 generates the evidence without blocking anything. *Why it's yours:* it sets whether the language call gets its evidence now or later.

**D6 — AMD-65 timing.** *Choice:* author the `Expectation` codec in the M5 window (Lane A) vs just-before-M9. *Recommended default:* **M5 window** — small, context fresh, AMD-52 precedent, lightweight block-track (P4); slips to just-before-M9 with no harm if the window is tight. *Why it's yours:* minor, but it's a Nick-gate amendment-load call.

**D7 — Verification-foundation (C4) as a piece.** *Choice:* dedicate an M5 test-support piece to the forward verification-foundation (fault-injection/property/time-series/HIL), vs let each consuming milestone build its own JIT. *Recommended default:* **quick-scope it first** (§6), then decide — lean toward a *small* dedicated property/fault-injection harness (genuinely cross-cutting) while leaving time-series and HIL to M12/M14 JIT. *Why it's yours:* it's the "is test-support still a real M5 deliverable" call, given the headline doubles already exist.

**D8 — Process adoption (P1–P6).** *Choice:* adopt the retro's proposals into the PM skill / `coding-instruction-format.md` now? *Recommended default:* **yes for P1 (lane-tracking, which this plan depends on), P2 (consumer/pin survey), P3 (ticked closeout), and P6 (non-Core floor)** — they are the controls this window relies on. *Why it's yours:* it changes the governance process.

---

## Closing read

**Is the post-M4 path clear enough to commit to?** Yes — clearer than the M4 entry was, because the two new assessments converged rather than diverged. The honest correction this synthesis makes to the prior recommendation is narrow but real: the originally-planned M5 (Platform API + test-support) is *thinner than it looked* — its test-support force-multiplier is already banked — while the work that actually de-risks the path is the design/decision cluster that is either **regret-proof** (the schema-irreversibles, safe under both language futures) or **gates the very next milestone** (the M6 crypto entry-gate). Because that cluster is mostly *not code*, the right move is not to choose build-forward *or* reinforce-first but to run a **small Core build, a leverage-prioritized design sprint, and a protected non-Core floor as parallel lanes** — disciplined by lane-tracking (P1) so it doesn't become M4's epic-in-disguise. **The single highest-leverage thing to do next is the M6 crypto entry-gate (promote the Draft, reconcile Doc 06/AMD-60, and *decide the INV-PD-07 MVP-scope question*)** — because M6 is the literal next milestone, it fans out to M7/M9/M10, and it cannot be correctly sized until that decision is made; the regret-proof schema decisions ride alongside it as the safest investments on the board. **The one piece of evidence that would most change the plan is the energy Mom-Test interviews** — a concrete, contracted demand for hard-sub-second deterministic control would simultaneously elevate the energy event family to urgent, justify a surgical Rust control-plane seam, and reshape the whole post-M5 sequence; their absence keeps the default (stay Java, lay the regret-proof energy shape, build energy features only on real demand) firmly in place. Decide D1 and D2 first; the rest of the window follows from them.

---

**Last verified against:** `homesynapse-core` HEAD `8ef9e9f` (M4 COMPLETE, working tree clean), `homesynapse-core-docs` HEAD, `nexsys-hivemind` working tree 2026-06-06. New load-bearing code claims source-verified (file:line) this session; foundation-readiness (2026-06-06, HEAD-verified) and language-replatform (2026-06-06) findings built upon, not re-audited. This document is decision-support — not a decision, not a milestone, not an amendment.

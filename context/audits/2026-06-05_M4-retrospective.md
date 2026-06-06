<!--
file: context/audits/2026-06-05_M4-retrospective.md
purpose: Constructive retrospective on Milestone M4 (device-model expansion + projection/derivation foundation + integration-api freeze). Process critique, debt register, and structural proposals.
audience: PM, Nick
update-cadence: frozen
state-type: history
status: CURRENT
last-verified: 2026-06-05 against homesynapse-core HEAD 8ef9e9f (watermark AMD-64, projectionVersion 5, M4 COMPLETE)
-->

# M4 Retrospective — Device-Model Expansion, Projection/Derivation Foundation, Integration-API Freeze

**Date:** 2026-06-05
**Author:** PM (Cowork governance session)
**Subject:** Everything M4 did — Workstream A (projection/derivation), Workstream B (device-model), Workstream C (integration-api freeze) — from M4 scoping (2026-05-28) through M4.C completion (`8ef9e9f`, 2026-06-05).
**Method:** Documents-only session. Evidence read from PROJECT_SNAPSHOT, pm-handoff, coder-handoff, cross-agent-notes, the milestone backlog, the W23 plan, the release-runway roadmap, the AMD-54..64 DOCS review return, and the M4 amendment files. No code touched.
**Verdict:** M4 shipped correct, well-governed work, and the quality gates earned their keep — but M4 was a mis-sized container, the recurring instruction-scope-miss pattern cost two avoidable gate bounces, the M4.C closeout itself shipped partial (recurring the 2026-04-11 failure mode the preflight exists to catch), and the calendar M4 consumed went entirely to Core while the launch-gating non-Core tracks stayed at zero. Each is fixable structurally; proposals are in §10.

---

## 1. What M4 actually was

The M4 backlog entry was a single line: *"Foundation: device-model expansion + projection/derivation + integration-api interface freeze."* What executed under that line:

- **~11 coding milestones:** M4.0a, M4.0b-1, M4.0b-2, M4.B3, M4.0b-3, M4.0b-4a, M4.0b-4b, M4.0b-5, M4.B-S1, M4.B-S2, M4.C — plus the M4 scoping session, the AMD-52 §11 JPMS-cycle erratum + relocation spike, and roughly half a dozen amendment-authoring / research-assessment / ratification sessions. The brief's "~15 work units" is a fair count once those are included.
- **Eighteen amendment numbers:** AMD-44, 45, 47, 50, 51, 52, 53 individually, plus the AMD-54–64 integration block (eleven). (AMD-46/48/49 were allocated to device-model in the P2 renumbering but went unused — allocation slack, not a problem, but worth noting the on-disk watermark jumped 50→64 in a single milestone group.)
- **Real surface delivered:** typed `AttributeValue` end-to-end (comparator → event payload → codec → checkpoint), a new `com.homesynapse.value` leaf module (forced by a JPMS cycle), event-time-deterministic activity timestamps, the Floor/Area aggregate + `EntityRole` matrix, and an integration-api surface freeze of 22→40 types with descriptor 8→14 / context 10→12 / RequiredService 3→5 / lifecycle permits 5→10 + 2 capability events. `projectionVersion` advanced 1→5. Build is GREEN at `8ef9e9f` (full `./gradlew check --continue`, 145 tasks).

This is a subsystem-grade body of work. The critique that follows is not that it was wrong — most of it is genuinely good — but that it was packaged, sequenced, and closed out in ways we should change.

---

## 2. Milestone sizing — M4 was an epic wearing a milestone's name

**Finding: M4 should have been chartered as three milestones, not one.** The work decomposed cleanly into Workstreams A/B/C and was *executed* that way — but it was *tracked* as a single "M4" parent. That packaging hid the true size. A one-line backlog entry expanded into ~11 coding milestones, eighteen amendments, and roughly two weeks of dense calendar, and at no point did a milestone boundary force the question "is this still one milestone?"

Two compounding causes:

1. **The projection/derivation chain was emergent, not planned.** Each layer revealed the next: typed values (AMD-47) → typed change-detection (AMD-51) → typed event payload (AMD-52) → a JPMS cycle that forced a module relocation (AMD-52 §11 erratum, M4.0b-4a/4b) → the timestamp-model unifier (AMD-53, "the honest last mile of A"). None of these were in the M4 scoping doc. That is partly unavoidable — you cannot fully see a derivation pipeline until you build it — but the *container* never grew a seam to absorb the discovery. The work just kept landing under "M4.0b-*."

2. **Workstream C was an entire milestone in itself.** An 11-amendment block, a full DOCS-Project review, same-day arbitration of A1–A6 + E3/E7/E8, and a 19-created/13-modified/20-test-suite freeze is not a sub-part of a milestone — it is M-something. Calling it "M4.C" understated it.

**Is our sizing discipline sound?** Partly. The instinct to decompose into workstreams was correct and the per-workstream execution was clean. The failure is that **workstreams were never promoted to first-class milestones with their own backlog rows and their own calendar estimates.** Had M4-A / M4-B / M4-C been three backlog entries from scoping, three things would have followed: the ~3-week true cost would have been visible at scoping rather than discovered in arrears; the "should we interleave non-Core now?" decision (§8) would have been forced earlier; and the M4.C amendment block would have been recognized as the major piece it was. **Proposal P1 (§10): a milestone that spawns more than ~3 sub-milestones or more than ~3 amendments is retroactively too big — split it, and treat that threshold as a scoping smell.**

One caveat in our defense: the emergent amendments (51→52→cycle→53) were each individually well-scoped and well-reviewed. The sizing problem is one of *bookkeeping and visibility*, not of work hygiene. But bookkeeping is exactly what makes the calendar honest, and the calendar is what's at risk (§8).

---

## 3. The instruction-scope-miss pattern — the central process finding

**This is the most important and most recurring defect in M4, and it has a clean systemic fix.**

The pattern: a coding instruction enumerates the *producer* of a change but misses the *downstream consumers and pins* that the change obligates. The build gate then catches the omission — but only after the gate runs, which (because gates are deferred to Nick) costs a full bounce cycle.

The most visible instance was the **M4.C event-type lockstep cluster.** The instruction's Files-to-Modify listed the producer — `EventTypes.java` (+7 string constants) and the `IntegrationEvents` manifests — but not the seven sites that pin or consume the event-type set:

1. `EventTypesTest` — the count pin (46→53) **and** the validity regex, which had to be widened to accept dot-namespaced types;
2. `EventCategoryMapping.TABLE` (persistence main) — +7 category entries;
3. `EventCategoryMappingTest` — count pin 27→34;
4. `EventTypeRegistryTest` — count pin 27→34;
5. `JacksonWarmupTest` — count pin 27→34;
6. `HomeSynapseCore` (the **production** composition root) — the 2-arg `Stream.concat(CORE, LIFECYCLE)` manifest aggregation, which had to become a 3-way include of `CAPABILITY_EVENT_CLASSES`;
7. `IntegrationTestHarness` — the same aggregation in the test harness.

The gate caught this over **two rounds.** Round 1 aborted at `core:event-model` on the `EventTypesTest` count+regex, and because the build aborted upstream, the integration/persistence suites never ran — so the omission was discovered one layer at a time. The Coder fixed the five sites Nick enumerated, then found two more (#6, #7) via a straggler grep.

**The most important part of this finding is #6.** The `HomeSynapseCore` miss was not a test count — it was a **latent production defect.** Without the capability manifest aggregated into the production composition root, `CapabilityAdded`/`CapabilityRemoved` would have been unregistered in production, and `encode()` would have thrown at M9 runtime. **No test pinned it.** It was caught only because the gate forced a full `--continue` run and the Coder grepped for stragglers. A purely test-driven check would have shipped it.

This is not a one-off. It is the third member of a family we keep meeting:

- **M2.2/M2.4 (2026-04-11 retro):** the producer (a new `Instant.now()` call site) shipped without the consumer (the ArchUnit whitelist / Clock injection), caught two milestones late.
- **Research 6/7 §7 fabrications:** the producer (a proposed type) was specified without verifying its consumers/collisions against real source — a different mechanism (invention rather than omission) but the same blind spot: *the change-set is treated as the thing you're adding, not the full fan-out of what depends on it.*
- **M4.C lockstep:** the producer (event-type set) without its seven pins/consumers.

**Systemic PM-side fix — the "consumer/pin survey" (Proposal P2, §10).** For any change that touches an enum, a registry, an event-type set, a sealed hierarchy, a category/mapping table, or any *counted or pinned* set, the coding-instruction format must require a mandatory fan-out survey before issue. Concretely, the PM (or the Coder as a gate-0 step) runs a repo-wide grep for the set's dependents and enumerates each in Files-to-Modify with its required delta:

- count pins — `hasSize(N)`, `isEqualTo(N)`, `assertThat(...).hasSize`;
- validity regexes / format validators over the set;
- category/mapping/lookup tables keyed by the set;
- `ServiceLoader` / manifest / "all-X" aggregators;
- composition-root and test-harness registrations (the production one is the dangerous one);
- exhaustive `switch` statements over the set (the no-`default` discipline makes these compile-fail, which is good, but they still need listing).

This generalizes the two controls we already adopted — the module-info.java embedding rule (Research 6 lesson) and deferred-gate tracking (M2.5 lesson) — into a third: **completeness of the change-set.** The first two ask "is the contract named correctly?" and "did the gate actually run?"; this one asks "does the instruction enumerate everything the change obligates?" The M4.C cluster is the proof case: a consumer/pin survey at authoring time would have listed all seven sites, and M4.C would have gone GREEN in one round instead of two.

The Coder did log the lesson ("event-type set has SEVEN lockstep sites"). That's good Coder hygiene, but a lesson in coder-lessons.md is reactive; the fix must live in the **instruction format** so it fires proactively on the *next* enum/registry change, not just the next event-type change.

---

## 4. The deferred-gate model — right tradeoff, wrong load-balance

**The deferred gate works and should stay.** Deferring `./gradlew check` to Nick's environment (the Coder sandbox can't reliably run Gradle) is the same rational policy the M2.5 retro affirmed, and in M4 it did exactly its job: it caught the M4.C lockstep cluster — including the latent-M9 `HomeSynapseCore` production bug that no test pinned. The earlier M4.0b-4 JPMS cycle was caught even earlier, by the instruction's STOP-gate at authoring time. The gate is the backstop of last resort and it held.

**But the cost is real and partly avoidable.** Each deferred-gate catch is a bounce: Coder produces files → Nick runs the gate → it fails → Coder fixes → Nick re-runs. M4.C took two rounds. The bounce is bounded (it didn't ship debt the way M2.2/M2.4 did, because the gate is now tracked), but it is not free — it is a round-trip through Nick every time, and Nick is the serial bottleneck (§8).

**Would more PM pre-issue verification cut bounces? Yes — for a specific, identifiable class.** The M4.C lockstep miss was *statically discoverable at authoring time.* The seven pin/consumer sites are findable by grep before the instruction is issued; they did not require running anything. That is precisely the class the consumer/pin survey (§3) targets. The right model is **shift-left the inspection-discoverable misses so the gate catches only the genuinely runtime-discoverable ones:**

- *Inspection-discoverable* (count pins, regexes, manifest aggregators, missing consumers): catch these in the PM's pre-issue survey. The M4.C cluster was entirely this class.
- *Runtime-discoverable* (a behavioral contract that only fails under a real `./gradlew check` — arch-rule violations in generated code, a serde round-trip that degrades, a concurrency interaction): keep these for the deferred gate. The AMD-65 serde defect is the model: the instruction *flagged it as the riskiest item*, the Coder hit it, STOP-and-reported rather than silently writing a serializer, and it became a tracked amendment. That is the gate and the STOP-discipline working in concert.

Net: keep the deferred gate; do not try to replace it. But move the cheap, greppable misses upstream of it so the gate's bounce budget is spent only on defects that genuinely need a build to surface. **Target: M4.C-class lockstep clusters should go GREEN in one round.**

---

## 5. The M4.C closeout shipped partial — we recurred the 2026-04-11 failure mode

**This finding is live: it was detected by this session's freshness preflight, and it is the single sharpest piece of evidence in the retrospective because it is the M2.5 lesson recurring inside the very milestone whose process we are auditing.**

The M4.C WUCP Phase 2 closeout updated the big-ticket artifacts — PROJECT_SNAPSHOT header + Latest Commit, the milestone backlog (M4.C and M4 both DONE `8ef9e9f`), pm-handoff's session record, and the W23 Progress log. But it left four stragglers:

1. **PROJECT_SNAPSHOT Recent Session Log** has no row for the M4.C-completion session — its most recent row is still the Workstream C *briefing* (`e76b925`). The header says M4 COMPLETE; the session log stops one session short.
2. **coder-handoff's Deferred Build Gate** for M4.C still reads **Status: OPEN — DEFERRED to Nick**, with only "Gate-fix round 1" described. It was never flipped to RESOLVED + `8ef9e9f` after Nick ran the gate GREEN. An artifact that contradicts the snapshot on whether the build gate resolved is exactly the drift the preflight exists to catch.
3. **The W23 plan's "Current state" footer** still reads HEAD `e73e199`, watermark AMD-53, "B Stage 1 DONE" — three milestones and eleven amendments behind its own Progress log (which is current to M4 COMPLETE).
4. **cross-agent-notes** carries a trail of superseded pointers above the `## Archived` separator that should have been archived at closeout.

Plus a lower-priority drift (the strategic-context-map still says "M4.0a NEXT" and quotes file/test counts from 2026-05-28) and a stale "Days remaining: 182" in the snapshot (the correct figure on 2026-06-05 is 173).

**Why this matters.** The 2026-04-11 governance overhaul was built precisely to prevent a Phase-2 closeout from running *partially or not at all*. The freshness preflight did its half of the job — it flagged this session STALE on exactly these stragglers, which is the mechanism working as designed. But the closeout *discipline* still slipped: the M4.C closeout self-reported "Closeout applied" in the cross-agent pointer while four artifacts stayed stale, and it relied on Nick running a `sed` to substitute an `M4CSHA` placeholder across five files — a manual step that is itself a drift vector (and one of the files, the W23 footer, fell outside the substitution and stayed at `e73e199`).

**The lesson is not "the preflight failed" — it caught this. The lesson is that "Closeout applied" is being asserted before the closeout is actually complete.** A WUCP Phase 2 that updates the masthead but not the session log, the coder-handoff gate flip, and the week-plan footer is a partial closeout that *looks* done. **Proposal P3 (§10): the WUCP Phase 2 checklist needs an explicit, enumerated artifact list with a tick per file, and the closeout is not "applied" until every tick is set — including the coder-handoff gate flip (OPEN→RESOLVED+SHA), the snapshot Recent-Session-Log row, and the week-plan footer.** The placeholder-`sed` pattern should also be retired in favor of writing the real SHA at closeout when it is known, or, when it genuinely isn't, tracking the placeholder as an explicit open item rather than a buried `sed` instruction. (This session executes the retroactive remediation; see §11.)

---

## 6. Amendment-process rigor — proportionate at the block grain, ceremony-heavy at the per-AMD grain

**The brief asks whether 13+ amendments — several trivial (AMD-61 soft-dependencies, AMD-63 IsolationLevel reservation, AMD-64 planned-restart-timeout) — were over-processed.**

The honest answer is two-sided:

- **The review rigor was not wasted — it caught real defects.** The single DOCS-Project review of the AMD-54..64 *block* returned RATIFY-WITH-EDITS with two genuine catches that would otherwise have frozen into the contract: AMD-56's route-(a) auth-failure trigger was **unimplementable as worded** (E4 — wording fix required before freeze), and AMD-55's reauth hook was a **`void` no-op that the supervisor could not detect** (E2 → `ReauthOutcome { INITIATED, UNSUPPORTED }`, so a reauth that does nothing is now distinguishable from one that starts). A contract freeze is the most expensive place to be wrong — it is what M9 and every adapter author will build against for years — so paying full review cost there is correct. The trivial amendments rode the *same* block review essentially for free.

- **The disproportion is in the mechanics, not the review.** Where the ceremony bites is the per-AMD bookkeeping: registering 29 invariants across §24–§34, eleven nav-index rows, eleven §18 traceability rows, eleven §Review-Disposition blocks, and §0.3/§17 index churn — for a block in which AMD-61/63/64 each add a single field or a single inert reservation. That is a lot of mechanical surface for "added one nullable field" and "reserved an enum that does nothing until M9."

**Proposal P4 (§10): formalize a lightweight "block-amendment" track.** M4.C already did the right thing instinctively — one review, one ratification pass, one block. Make that explicit:

- Trivial additive amendments (a single appended record field with a back-compat convenience ctor; a new constant on a non-persisted enum; an inert reservation like `IsolationLevel`) ride a **shared** block review, block ratification, and block mechanics — one watermark bump, one traceability pass, one disposition block for the set.
- Per-AMD full treatment is **reserved for** anything that touches a persisted shape, a behavioral contract, or introduces a new invariant. Those still get individual scrutiny.
- One guardrail for reservations: an inert amendment (AMD-63) must carry an explicit "inert until M{N}" note so it is not implemented prematurely or mistaken for live contract.

This keeps the gate that caught AMD-55/56 while cutting the ceremony on AMD-61/63/64 from "full per-AMD mechanics" to "a row in the block."

---

## 7. Debt accrued in M4 — the register

M4 closed with real, mostly-healthy debt. Itemized, with a disposition for each:

**7.1 AMD-65 — `Expectation` persisted codec (deferred BLOCKING-for-M9).** Command-bearing `CapabilityAdded` cannot round-trip today because the sealed `Expectation` (ExactMatch/WithinTolerance/EnumTransition/AnyChange) has no persistence codec; `WithinTolerance(double,double)` needs the AMD-52 bit-anchored-float / non-finite-sentinel treatment. **Disposition: this is a model of deferring *well*** — it is tracked in the backlog (QUEUED, BLOCKING-for-M9), it has a clear closure condition, and it ships with an **executable acceptance spec** already in the tree (the `@Disabled("AMD-65 pending")` `capabilityAdded_onOff_roundTrips` test). Contrast with the M2.2/M2.4 deferral, which was untracked and silent. Recommend authoring it in the M5 window (small; AMD-52 precedent; lightweight block-track review per §6) so the M9 prerequisite is cleared while the M4.C context is fresh — but it is genuinely not urgent (M9 is ~late-Jul/Aug).

**7.2 The mixed event-naming convention is now permanent (snake legacy + dot new).** Legacy events are snake_case (`state_changed`, `state_reported`, `device_adopted`); the new integration/capability events are dot-namespaced (`integration.*`, `capability.*`). The `EventTypesTest` regex was *widened* to accept both. **Disposition: accept, but document and watch.** Renaming legacy events is not an option — the event log is immutable and replay-deterministic, so the wire strings cannot be rewritten. The dual convention is therefore permanent and correct. The risk is that it is **documented, not enforced**: the widened regex now accepts *both* forms, so a future author who adds a snake_case *new* event will pass validation and quietly violate the convention. Recommend a short, explicit "event naming convention" note in Doc 01 / the event-model MODULE_CONTEXT stating the rule (legacy snake is frozen; all new events are dot-namespaced) so the convention is at least written down where the next event author will see it. A mechanical enforcement (a rule that new constants must be dotted) is possible but probably over-engineering for the event-add rate.

**7.3 The provisional EventCategoryMapping categories (the [REVIEW] accept) — confirm, with one refinement.** The Coder chose categories for the 7 new types (5 `integration.*` → `[SYSTEM, DEVICE_HEALTH]`, mirroring existing integration siblings; 2 `capability.*` → `[DEVICE_STATE]`) because the AMDs ratified the event *types* but not their *categories*. **Disposition: the accept is confirmed as reasonable and sibling-consistent — with one concrete refinement flag.** `capability.*` → `[DEVICE_STATE]` is right (a capability add/remove is an entity structural-state change). For the lifecycle events, `[SYSTEM, DEVICE_HEALTH]` is defensible — *except* that the `EventCategory` enum includes a **`SECURITY`** value, and two of the new lifecycle events (`integration.reauth.required`, `integration.reauth.completed`) are credential/security signals. They arguably warrant `SECURITY` (or `[SYSTEM, SECURITY]`) rather than `[SYSTEM, DEVICE_HEALTH]`. This is low-stakes — categories are a derived, non-persisted runtime lookup and freely amendable — so the recommendation is: **confirm the accept now; log a low-priority item to revisit the reauth/security-adjacent lifecycle categories the next time the category taxonomy is touched** (likely M9, when these events first fire). Do not re-open M4.C for it.

**7.4 PLAN-M4-CONSOLIDATED v2 §3 is stale.** The consolidated M4 plan was written at scoping (2026-05-28) and the actual M4 diverged substantially: the M4.0b-2 re-scope, the AMD-52 §11 erratum/relocation (M4.0b-4a/4b), the timestamp unifier (M4.0b-5), and the integration-block split (54+55). §3 never caught up. **Disposition: mark it SUPERSEDED rather than retrofit it.** The per-milestone backlog rows plus PROJECT_SNAPSHOT are now the authoritative M4 record; retrofitting a consolidated plan to match shipped reality is low-value make-work. Recommend a one-line SUPERSEDED-BY masthead on PLAN-M4-CONSOLIDATED pointing at the backlog + this retrospective, and stop maintaining it. (Logged to the backlog as a doc-currency item.)

**7.5 Phase-2 traceability stub debt.** Ten traceability stub indexes remain unpopulated (docs 02–11, 13, 14); only Doc 01 (44 entries) and Doc 12 (2 entries) are populated. The M4 amendment mechanics added §18 amendment-traceability rows ×11 for the integration block, but the underlying per-document invariant→design traceability stubs have carried "low priority, batch later" since Phase 2 (~3 months). **Disposition: stop pretending a standalone sweep will happen — fold it into the work that already touches each doc.** Rather than a dedicated traceability-sweep WU that keeps getting deprioritized, populate a document's traceability index *when that subsystem next gets a milestone* (e.g., Doc 06's index gets populated during M6, Doc 09/10's during M10/M11). That trades a never-scheduled sweep for incremental closure tied to work that's happening anyway. Logged with that explicit trigger.

**7.6 The PROJECT_SNAPSHOT "Last updated" header is an unreadable run-on.** The header is now a single ~1,200-word paragraph that mixes the current state, the gate-fix narrative, the full ratification chain, and a "[historical chain retained below]" trail that recounts every milestone back to AMD-47. It is unscannable — the one field a reader most needs (what is the current state?) is buried in prose. **Disposition: restructure now** (this session) into a short masthead (milestone, commit, watermark, projectionVersion, build status, next action — five lines) with the historical chain moved into / left to the Recent Session Log. This is part of the §11 remediation.

---

## 8. Strategic and velocity — Core rigor is healthy; the launch is gated by what M4 crowded out

**The uncomfortable truth M4 illustrates: Core is on or ahead of its own axis, and that is not the risk. The risk is everything Core isn't.**

The release-runway roadmap (2026-05-31) is explicit: Core is healthy, but the three non-Core tracks — Web UI (W2), Website/Docs (W3), Distribution (W4) — are **at zero**, despite the master plan assuming all three run in parallel with Core from Week 1. "In practice every session has gone to Core." The roadmap names website/docs as the lowest-dependency, highest-slip-cost track and recommends posture (A): interleave non-Core *now*.

M4 is the case study in why this is hard. The W23 plan (the first week under posture A) listed standing up the website/docs track as **Goal 4** — and it did not happen. M4.C consumed the week. The Progress log's own closing line is the tell: *"Next: ... and the W3 website/docs standup (Goal 4) as the parallel lane."* The parallel lane was planned, named, and then deferred again, because the serial bottleneck — a single developer plus AI agents, with Nick as the human gate on every build and ratification — went entirely to finishing M4.

**Is the Core-rigor vs launch-velocity balance right for a late-November target?** With 173 days to Nov 25, ~11 remaining Core major groups (M5–M15, including the hardware-dependent Zigbee work and a 72-hour validation gate), **and** three non-Core tracks at zero, the current balance is **too Core-weighted** — not because Core rigor is wrong, but because the non-Core lanes have no *protected* capacity and therefore lose every week to whatever Core milestone is in flight.

The nuance worth stating clearly: **the Core rigor is not the problem and should not be cut.** The per-milestone WUCP discipline, the amendment reviews, and the deferred gates are *why* Core ships with low defect rates and clean contracts — M4 finished ahead of the roadmap's mid-June band with a GREEN build and two caught-before-freeze defects. Cutting that rigor to free velocity would trade a healthy axis for risk on the axis that's already healthy. The problem is structural: **non-Core has no floor.** When Core and non-Core compete for the same serial pipeline, Core's gravity (it's the critical-path spine, it has momentum, it has the next obvious milestone queued) wins every time, and the launch-gating tracks stay at zero until they become a fall crunch on top of Zigbee + validation — which is, per the roadmap, exactly how launches slip.

**Recommendation (feeds §9 next-piece): protect non-Core capacity explicitly.** Posture (A) cannot be aspirational — "interleave when Core allows" resolves to "never," as W23 proved. The next milestone window must *pair* a deliberately-small Core piece with a non-preemptable website/docs standup, so the parallel lane finally becomes real. M4's lesson is that if the next piece is chosen as pure Core, the website/docs track will be deferred a third time, and the runway's stated #1 risk compounds another week.

---

## 9. What genuinely worked — keep doing all of this

The critique above is real, but M4 also validated a stack of practices that should be treated as load-bearing and protected:

**9.1 STOP-on-mismatch gates converted latent runtime failures into design-time decisions, repeatedly.** The M4.0b-4 instruction's STOP-gate caught the AMD-52 JPMS cycle (a typed `AttributeValue` in an event-model record forces `event → device`, but `device → event` already existed) *at authoring time* — turning a compile blocker into a clean, planned relocation (the new `com.homesynapse.value` leaf). The M4.C STOP-discipline caught the AMD-65 serde defect: the Coder hit the instruction's flagged-riskiest item, **stopped and reported** rather than silently writing a serializer (an architecture call) or adding a Jackson annotation (an arch-rule violation), and it became a tracked amendment with an acceptance test. These gates are the highest-leverage practice we have.

**9.2 AMDs as the single source of truth.** Every contract change in M4 traces to a ratified amendment, with watermark discipline, invariant registration, and — importantly — *ratified-vs-shipped reconciliation* when code diverged (the AMD-51 §2.6 erratum, which amended the spec to match the more-correct shipped string-compare fallback rather than silently tolerating drift). The contract and the code stay honest with each other.

**9.3 The DOCS-Project ratification reviews are the most valuable gate in the amendment pipeline.** The AMD-54..64 block review independently re-derived every source shape (G3) and caught two genuine defects before the contract froze — AMD-56's unimplementable trigger and AMD-55's undetectable void-reauth. Earlier in M4 the same review discipline caught AMD-55's void-reauth and AMD-56's wording at the block grain. An independent reviewer that re-derives rather than trusts is worth its cost.

**9.4 The freshness preflight works — it caught this session's STALE.** The mechanism the 2026-04-11 overhaul installed did exactly its job: it flagged the partial M4.C closeout (§5) at session start, before any forward work. The preflight is the reason the partial closeout is being fixed today instead of compounding for three weeks.

**9.5 The research → AMD → code pipeline produces well-grounded contracts.** Research 6 → NQ-1..6 → AMD-54..64 → M4.C; Research 10/11 → AMD-51/52. The contracts that froze in M4 are grounded in field evidence and competitive analysis, not invention. (The known weakness — the §7 fabrication problem in the research step — is real but is now mitigated by the module-info.java embedding rule and the quote-back discipline, and it did not corrupt any M4 contract.)

**9.6 The dual-skill mirror discipline held.** The `diff -rq` check (preflight Check 9) is clean — the writable source and the read-only skill mirror are byte-identical. The invariant that prevents the two agent skill-trees from silently diverging is being maintained.

---

## 10. Recommendations — structural proposals

Mirroring the M2.5 retro's "structural fixes" model, the proposals are stated so they can be adopted as concrete process changes:

**P1 — Milestone-sizing smell test.** A milestone that spawns more than ~3 sub-milestones or requires more than ~3 amendments is too big; split it into first-class milestones with their own backlog rows and calendar estimates at scoping. Had M4-A/B/C been three milestones, the ~3-week cost and the interleave decision would have been visible up front. (Addresses §2.)

**P2 — Mandatory consumer/pin (fan-out) survey in the coding-instruction format.** For any change to an enum, registry, event-type set, sealed hierarchy, category/mapping table, or any counted/pinned set, the instruction must enumerate every dependent — count pins, regexes, mapping tables, manifest aggregators, composition-root **and** test-harness registrations, exhaustive switches — each with its required delta, before issue. Generalizes the module-info embedding rule and deferred-gate tracking into a third control: completeness of the change-set. (Addresses §3; would have made M4.C one-round-green.)

**P3 — WUCP Phase 2 closeout becomes an enumerated, ticked artifact checklist.** "Closeout applied" is not assertable until every artifact is ticked: PROJECT_SNAPSHOT header **and** Recent-Session-Log row, milestone backlog, pm-handoff, week-plan Progress **and** Current-state footer, coder-handoff gate flip (OPEN→RESOLVED+SHA), cross-agent-notes archival. Retire the placeholder-`sed` pattern in favor of writing the real SHA at closeout (or tracking an unknown SHA as an explicit open item). (Addresses §5.)

**P4 — Lightweight block-amendment track.** Trivial additive amendments (single appended field with back-compat ctor; new constant on a non-persisted enum; inert reservation) ride a shared block review, ratification, and mechanics. Full per-AMD treatment is reserved for persisted-shape / behavioral-contract / new-invariant changes. Inert reservations carry an explicit "inert until M{N}" note. (Addresses §6.)

**P5 — Shift-left the inspection-discoverable gate misses.** Keep the deferred gate as the backstop, but spend its bounce budget only on runtime-discoverable defects. Inspection-discoverable misses (the P2 class) are caught pre-issue. Target: lockstep clusters go GREEN in one round. (Addresses §4.)

**P6 — Protect non-Core capacity with a non-preemptable floor.** Posture (A) must be structural, not aspirational. The next milestone window pairs a deliberately-small Core piece with a website/docs standup that Core is not allowed to preempt. (Addresses §8; see the next-piece recommendation companion.)

---

## 11. Outcomes and remediation applied this session

- **Preflight result:** STALE (partial M4.C closeout). Per protocol, this session's forward-equivalent work is reflective (this retrospective + the next-piece recommendation are deliberative, not new coding instructions / not a new milestone declared DONE / not a weekly advance), and the brief itself requests the Phase-2 closeout — so the retroactive WUCP Phase 2 reconciliation is executed here and PASS re-recorded.
- **Remediation applied (this session):** PROJECT_SNAPSHOT masthead restructured (run-on header → 5-line current-state block; "Days remaining" 182→173) + Recent-Session-Log M4.C-completion row added; coder-handoff M4.C Deferred Build Gate flipped OPEN→RESOLVED (`8ef9e9f`); W23 plan Current-state footer advanced to `8ef9e9f`/AMD-64/M4 COMPLETE; cross-agent-notes superseded-pointer trail archived. See pm-handoff for the ticked artifact list.
- **Flagged to Nick (not touched — documents-only session):** three uncommitted, build-breaking working-tree edits exist at `8ef9e9f` — `EventCategoryMapping.java` (its `categoriesFor()` and `explicitMappingCount()` methods deleted, file truncated mid-Javadoc → will not compile), `EventTypesTest.java`, `EventCategoryMappingTest.java`. These are stray/corrupt working-tree state, not real changes; the committed `8ef9e9f` is the correct M4-COMPLETE tree (build was GREEN, 145 tasks). **Recommend Nick run `git -C homesynapse-core checkout -- <the three files>` to restore the committed state after confirming they are stray.** Logged as an Open Risk.
- **Debt logged to the backlog / research agenda:** AMD-65 (confirmed QUEUED, recommend M5-window authoring); event-naming-convention note (Doc 01 / MODULE_CONTEXT); EventCategoryMapping reauth-category refinement (low-priority, revisit at M9); PLAN-M4-CONSOLIDATED SUPERSEDED marker; Phase-2 traceability stubs (fold into per-subsystem milestones); the six process proposals P1–P6.

---

**Last verified against:** `homesynapse-core` HEAD `8ef9e9f` (M4 COMPLETE), `nexsys-hivemind` working tree 2026-06-05.

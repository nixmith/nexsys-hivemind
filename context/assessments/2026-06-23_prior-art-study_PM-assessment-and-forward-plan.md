<!--
file: context/assessments/2026-06-23_prior-art-study_PM-assessment-and-forward-plan.md
purpose: PM assessment + disposition of the 15-year smart-home/IoT prior-art architecture study (the research return at context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md). Grades the return, separates solid-vs-verify, extracts the actionable findings, and turns them into a forward development plan. The HEADLINE INPUT to the v6 §1 deeper-M7 architecture beat.
audience: PM (v6 hub), Nick.
state-type: assessment
status: ASSESSED 2026-06-23 by the v5 hub.
-->

# PM Assessment + Forward Plan — the 15-Year Prior-Art Architecture Study

## Verdict — grade A−

A strong, decision-grade return. It followed the brief's structure exactly; it is genuinely anchored to HomeSynapse's architecture (not a generic survey); it separates FACT from INFERENCE (§8) and flags its own secondary/aggregator sources; and it ends with the 5 unresolved questions + the primary source that would close each. Cross-checked against first-hand knowledge, the load-bearing architecture / event-sourcing / Home-Assistant / SmartThings / Zigbee findings are ACCURATE. It also delivered the single most valuable thing we asked for: a cleaner answer to the open command-pipeline decision than either option the v5 hub had framed.

## Diligence — what is SOLID vs what to VERIFY before it is load-bearing

**SOLID (verified against first-hand knowledge — act on these):**
- HA's architecture (event bus + state machine + service registry; single-threaded asyncio), the Recorder-DB scaling wall, and — critically — **HA automation traces cannot durably answer "why did it NOT fire?"** (default 5, in-memory, evicted, and never created when the trigger never matches). This is the report's headline and it is correct — it is the empirical basis for our flagship differentiator.
- The SmartThings Groovy→Edge destructive-migration story; openHAB's rules-engine proliferation; the Z2M/ZHA converter-database + ZNP/EZSP abstraction (and the licenses — zigbee-herdsman-converters MIT, zha-device-handlers Apache-2.0 — are correct); Tuya's non-standard `0xEF00` cluster; the canonical event-sourcing pitfalls (upcasting, projection-rebuild cost, **no-side-effects-on-replay**, command-vs-event dispatch, crypto-shred). All accurate and load-bearing.
- The AI safety pattern (planner → verifier/safety-gate → deterministic executor) as the emerging consensus, and HA Assist's two-tier deterministic-first/LLM-fallback. The PATTERN is real and correctly maps to our "AI proposes, the engine disposes."

**VERIFY before relying on the specifics (directionally sound, details unconfirmed by me):**
- **Post-cutoff specifics** (my reliable knowledge ends ~May 2025): the Matter 1.6 / Joint-Fabric / NFC-commissioning details (June 2026), the exact CRA application dates (Art. 14 reporting "from 11 Sept 2026"; main provisions "11 Dec 2027"), and the Dec-2025 HA scale figures (3,000+ brands / ~2M installs). The magnitudes and directions are right; the precise dates/figures should be confirmed against the cited primary sources before any of them gate a decision (none gate a NEAR-TERM one).
- **The AI-safety arXiv citations** (VERIMAP, SafeGate, Blueprint-First, VeriPlan, f-secure): the deep-research harness can fabricate plausible paper names. The PATTERN is sound regardless of the exact titles; verify the specific citations before quoting any as authority. We use the pattern, not the papers — low risk.
- **The "nobody durably does why-not" claim** is "absence of evidence," not proof (the report says so). Strong and defensible as a position; do not over-claim absolute uniqueness in marketing until the patent/vendor-doc search (open Q1) is done.

Net: nothing in the SOLID set is in doubt; the VERIFY set is appropriately hedged by the report itself and none of it blocks our near-term decisions.

## The headline finding — it resolves our open command-pipeline decision

The study recommends the command pipeline go **event-driven** (the executor emits `command_issued`; a dispatch subscriber consumes it; outcomes correlate back through the Pending Command Ledger) — because that is the only shape that scales additively to cross-process, multi-host, cloud, and AI consumption, which our own aspirations require. The elegant part, and the improvement over both options the v5 hub framed: **"logical event-driven, physically co-located for MVP"** — emit the event (so the seam is real and the ledger gets its input and it scales later) but run the dispatch subscriber in-process for MVP (so latency stays minimal).

This **converges with where we already were**: M7.3's ledger needs `command_issued` as its input (nothing emits it today), and M7.4a was already going to add "the `command_issued` producer." The research confirms the SHAPE (event-driven, not in-process) and hands us the co-location mitigation. The one caveat the engine must hold absolutely: **device dispatch is a side-effect that must NEVER run on log replay** (the pure-function-replay rule) — directly relevant because the ledger rebuilds from the log on REPLAY.

## Extracted actionable findings

**Validated bets (KEEP — confirmed by the prior art):** local-first inviolate; immutable event log as source of truth; no-destructive-migration; single component-based authoring model (no templating DSL); the deterministic no-autonomous-retry engine; explainability-as-projection (the durable differentiator HA's ephemeral traces cannot match); the ZNP/EZSP dual-coordinator path; crypto-shred; event-log-shipping for federation; the AI-proposes/engine-disposes safety frame.

**New / sharpened requirements (the gaps the study surfaced):**
1. **Pure-function-replay invariant** — device dispatch (and all external side-effects) must never run on replay; only on new-command handling. Make it a first-class architecture invariant + a CI test. SAFETY-critical (a side-effect on replay = re-firing real-world commands). Directly governs M7.3's ledger rebuild and M7.4's dispatch.
2. **Additive event versioning** — an explicit event `version` field + an upcaster framework + a full-history projection-rebuild test. No-destructive-migration is necessary-not-sufficient; "forgot to upcast" is a documented silent failure. Cheap now, expensive to retrofit.
3. **Log retention / compaction / snapshot discipline** — "everything is a projection of the log" is correct, but the LOG itself grows forever and will hit HA's Recorder wall, worse on Pi-class hardware (SD-card wear). Design per-scope retention + snapshots + projection pruning now. (A genuine gap — we had not scoped log retention.)
4. **Leverage an existing Zigbee converter database** (Z2M's `zigbee-herdsman-converters`, MIT) instead of rebuilding the device-quirk long tail — the database is the cost and the moat; re-deriving thousands of device defs is multi-year with no differentiation payoff. Gates the M9/device strategy; PENDING the license review (open Q3).
5. **Build the "why-not" projection into MVP** (not reserved) — the flagship differentiator, durable because it is a projection of the immutable log.
6. **Reserve the SBOM + signed-update + vuln-disclosure seam** (EU CRA / UK PSTI runway) — table-stakes in the MVP→post-MVP window; our local-first + auth-before-exposure posture is already ahead.
7. **UX / first-run investment** (the Hubitat lesson — "local-only is noble but impractical" for beginners) — the first-automation experience matters as much as the architecture.

## Forward plan — how this changes how we move

It does not force a re-plan; it VALIDATES the architecture, RESOLVES the command-pipeline decision, and adds a handful of concrete near-term requirements + reserved seams. Concretely:

- **The v6 §1 deeper-M7 architecture beat takes this study as its headline input.** §1 ratifies (Nick co-signs): (a) the command-pipeline = **logical event-driven, physically co-located** (Decision 1); (b) the **pure-function-replay invariant**; (c) **additive event versioning**; (d) the **log-retention/snapshot** design; (e) the **converter-DB-leverage** direction (pending the license review); (f) the reserved AI + SBOM/update + federation seams. Output: a ratified architecture decision record (the §1 deliverable).
- **Then the Doc 07 §3.11 / AMD-90 reconciliation adopts the event-driven shape** (it stops describing a pipeline the code never built and describes the one §1 ruled). **Then M7.4a** = the `command_issued` producer + the (co-located) dispatch subscriber; **M7.4b** = the live ledger subscriber (with `stop()` teardown) + the `pollExpirations` tick + the E2E gate test. The pure-function-replay invariant + event-versioning ride into these as constraints.
- **The hardware bench (live now) absorbs the two Pi-performance spikes** — open Q4 (event-driven dispatch latency on Pi, validating the co-location mitigation) and Q2 (log-growth + projection-rebuild time on Pi, sizing the retention/snapshot strategy). Bundle them into one Pi-performance spike; the timing is perfect with the MG24 on the desk.
- **A discrete converter-DB license review** (open Q3) runs before M9 scoping — it could save enormous effort or, if the license is incompatible with free→paid→enterprise, route us to the curated-subset + community-contribution fallback.

## Disposition

- This assessment + the raw return (`…_research-return.md`) are the v6 §1 input. The v6 hub should NOT re-do the research; it should ratify the decisions with Nick and fold the new invariants/requirements.
- Verification queue (prioritized): **HIGH** — the Pi-performance spike (Q4 latency + Q2 growth, via the bench) and the converter-DB license review (Q3, gates M9). **MEDIUM** — the why-not patent/vendor search (Q1, strengthens the differentiator/moat) and the CRA conformity class (Q5, sizes compliance, post-MVP).
- Nothing here is blocked on the VERIFY-set caveats; the near-term decisions rest on the SOLID findings.

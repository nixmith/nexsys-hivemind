<!--
file: context/strategy/2026-07-27_homesynapse-technical-overview_north-star.md
purpose: THE NORTH-STAR STRATEGY ARTIFACT — Nick's HomeSynapse Technical Overview (the agent-substrate thesis: the harness enforces, the model only proposes; deterministic runtime enforcement at the actuation boundary; the event log as state + audit record + dataset). Filed verbatim below the marker, 2026-07-27 (v39 hub, beat 7).
status: FILED as the long-term research north star (Nick's charge, 2026-07-27: "our long-term research is aimed around building the ultimate smart ecosystem around the ideas laid out in this document"). Deliberations D1–D6 + the seams-verification finding: pm-handoff v39 beat 7. Consumers: the agent-substrate research lane (verification + prior-art + program-shaping — its Charge 6 carries the honesty audit), the fusion program's ~mid-Oct synthesis, THE LAUNCH-RUNWAY CHARTER (AGENT-SEAMS · AUTO-IDENT · posture-(B) · EVENTS-API as named candidates).
verified-at-filing (hub, at c09c61c source): the "event model reserves the seams… agents as a first-class subject type" claim is DESIGNED-FOR, not TRUE-TODAY (no agent SubjectRef type; no proposal/adjudication event types; the governance half EXISTS — Doc 17 Locked, AIOT-INV-1 registered §50). External use softens that sentence until AGENT-SEAMS lands (post-gate). The research lane's honesty table will tense-check every other claim.
-->

# HomeSynapse — Technical Overview

*An execution substrate for automation and AI agents that act on physical space.*

---

## What it is

HomeSynapse is a local-first, event-sourced automation platform for homes, offices, and buildings. It runs entirely on-premises — a Raspberry Pi 4/5 is the reference target — with optional cloud sync as an additive layer rather than a dependency. No functionality degrades when the WAN link drops, and no user data is exfiltrated or monetized. The core is Apache 2.0.

Technically: Java 21, a JPMS-modular multi-module build with compile-time-enforced module boundaries, SQLite in WAL mode for persistence, and virtual threads throughout (with a bounded platform-thread executor fronting all JNI/SQLite work, since the driver's synchronized native methods pin carrier threads).

Three architectural properties do most of the work, and they're the reason the rest of this document is interesting:

1. **Single-writer total ordering.** Every state transition in the system flows through exactly one serialization point. Not by convention — by construction.
2. **Append-only, hash-chained event log.** Events are immutable and causally linked. Nothing is edited or deleted; state is a deterministic projection over the log.
3. **Replay determinism.** Projections are pure and clock-free in their derivation. Replaying the log reproduces state exactly.

These are ordinary event-sourcing commitments. What's unusual is applying them to physical actuation, and what falls out of that turns out to matter a great deal.

---

## Problem 1: nothing in this space is infrastructure-grade

The existing options split cleanly along a design-center axis.

**Cloud platforms** (Nest, Alexa, SmartThings) are architecturally dependent on a vendor cloud whose economics rest on data collection. Two consequences follow structurally, not incidentally: the system stops working when the vendor's service does, and privacy guarantees are in tension with the business model that funds it.

**Home Assistant** is genuinely excellent and shares most of our values — local control, device choice, and sustainability are explicit foundation principles, and its integration breadth (3,000+ brands, community-authored) is a real achievement we have no interest in replicating. But its design center is the single enthusiast home. It's a Python codebase optimized for integration surface area and iteration speed, with no total ordering, no immutable event history, and no tamper-evident record of what the system did or why.

That last gap is the one that matters. **Neither category can answer, provably, the question "what happened, in what order, caused by whom, and can you demonstrate the record wasn't altered?"** For a hobbyist, that's fine. For a property manager running hundreds of units, a regulated facility, an insurer, or anyone carrying liability for automated physical actions, it's disqualifying.

That's the near-term problem: there is no infrastructure-grade substrate for multi-site, accountability-bearing physical automation. But it's the smaller of the two problems.

---

## Problem 2: LLM agents are about to be handed actuators

This is the part worth thinking hard about.

The trajectory is obvious — natural-language agents that reason over building state and act on it. The safety story everyone is defaulting to is *model-level*: alignment training, refusal behavior, a guard model evaluating a plan before execution. That story is necessary and insufficient, for four reasons that are structural rather than a matter of model quality:

- **Probabilistic guarantees, categorical consequences.** Model safety is a distribution over behaviors. Unlocking a door, opening a gas valve, or disabling a freezer is not a distribution — it's an event with an irreversibility class.
- **Safety travels with the model.** Swap the model, and your safety properties change. Models will be swapped constantly. Anything load-bearing that lives inside the model is a property you re-verify on every upgrade.
- **Sensor readings are untrusted input.** This is the point security-minded readers tend to seize on first. In a building, the agent's context window is populated by device state — from devices that may be compromised, spoofed, or simply reporting attacker-controlled strings. A smart home is a prompt-injection surface with actuators attached.
- **Composition.** Multiple agents, multiple occupants, one shared physical environment with conflicting objectives. No amount of per-model alignment resolves arbitration over a single thermostat.

The right layer for physical safety is not the model. It's the environment.

---

## The gap in the current research

This isn't a hypothetical. The embodied-agent safety literature is active, but it has converged tightly on one approach — **a model evaluating a plan before execution** — and the field's own papers say so:

- Safety is typically evaluated at the instruction or planning level, where a model judges whether a goal or plan is safe *before* it runs. The guardrails are themselves models: EMBGuard is MLLM-based, HomeGuard is VLM-based, RoboGuard filters plans pre-execution.
- EMBGuard states directly that no prior work has built guardrails specifically for embodied agents operating in physical environments, and that practical methods which *actively prevent* risky actions remain underexplored — benchmarks exist, prevention does not.
- AgentSpec observes that most existing solutions lack explicit enforcement mechanisms, concentrating instead on pre-execution risk assessment.
- The benchmarks are simulated. IS-Bench, the closest analog, is a simulation-based evaluation of whether embodied agents avoid risky situations. There is no longitudinal, real-deployment, multi-occupant corpus of physical agent behavior — largely because no one has a substrate that could collect one without becoming a surveillance system.

Notably, the field is trending *away* from deterministic methods, treating rule-based and symbolic runtime enforcement as the legacy approach to be superseded by better judges.

So the open territory is specific: **deterministic, runtime, unbypassable enforcement at the actuation boundary, in real deployed environments, with tamper-evident attribution.**

---

## Why this architecture is the answer

The design principle is one line: **the harness enforces; the model only proposes.** The strongest guarantee we can make is that the worst outcome of a bad inference is a *rejected action*, never an unsafe physical state.

(The symmetry is deliberate — the same principle governs our development process, where ArchUnit rules, JPMS module boundaries, and exhaustive sealed switches enforce architectural correctness so that the worst a model can do to the codebase is produce a red build, never silent corruption. Same idea, different domain.)

Four properties make this implementable here and difficult to retrofit elsewhere:

**Single-writer total ordering gives you an unbypassable chokepoint.** A policy kernel sitting at that boundary cannot be routed around, because there is no second path to actuation. This is a structural property, not a discipline that erodes. In a system with no total order, a comparable guarantee requires auditing every write path — and re-auditing on every contribution.

**The event log is simultaneously state, audit record, and dataset.** Every proposal, adjudication, and execution is an immutable, causally-linked, hash-chained event. Attribution — which agent, acting on what evidence, produced which actuation — is a graph traversal, not a forensic reconstruction from application logs.

**Replay determinism makes counterfactual evaluation possible.** You can replay a real recorded environment and ask what a *different* agent would have done. That is an evaluation harness for physical agents built against real deployments rather than simulators — the thing the current benchmark literature doesn't have.

**Model-agnosticism means the safety layer survives model churn.** The kernel makes no assumptions about what produced a proposal. Frontier model, local 3B, or a hand-written rule — same adjudication path, same guarantees.

---

## What this makes possible

- **Agents as first-class principals.** Cryptographic identity, scoped and revocable capabilities ("may read these sensors, may actuate these devices, within these bounds"), with every action attributed in the log. Capability security applied to physical actuation.
- **Reversibility-classified actions.** Actions carry a risk class as device-model metadata; irreversible and life-safety actions escalate to human confirmation deterministically, not at a model's discretion.
- **Shadow mode.** An agent proposes against live events without actuating. You get continuous, zero-risk evaluation against the real environment — and a natural trust-building onboarding path for operators.
- **Counterfactual replay.** Agent-under-test evaluated against recorded reality, deterministically, offline.
- **Provable accountability.** Not "the logs say X" but "here is a hash-chained causal record whose integrity is demonstrable."

That last point has a regulatory shadow worth noting. EU AI Act Article 12 mandates automatic event logging across the lifecycle of high-risk systems, with agentic workflows required to capture risk-relevant events, operator identity, and enough context to reconstruct the exact sequence. The statute mandates logging and is silent on *integrity* — and as one analysis of the requirements puts it, if logs can be silently altered and you can't demonstrate otherwise, their evidentiary value is zero. Off-the-shelf AI systems don't produce compliant decision records by default; they return outputs. A tamper-evident causal log is the primitive that closes that gap.

---

## Open research questions

The architecture opens several problems we think are genuinely unsolved and would like to see worked on:

- **Deterministic runtime enforcement at the actuation boundary** — currently counter to where the field is heading.
- **Real-world longitudinal benchmarking** of physical agents, from opt-in, anonymized deployment data rather than simulation.
- **A formal irreversibility/action-risk taxonomy** for physical actuation.
- **Multi-agent conflict resolution in shared physical space** — arbitration, preference aggregation, priority inversion when agents and occupants disagree.
- **Compiling natural-language intent into verifiable bounded behavior** — "keep it comfortable but save energy" into rules with provable envelopes.
- **Long-horizon retrieval over multi-year event histories** — episodic agents, continuous environments.
- **Graceful degradation** when the model is unavailable, slow, or wrong.

---

## Current state (honestly)

The core is real and the agent layer is not yet built. Today: the event model, persistence, projection, and reconciliation machinery are implemented and under test, with strict enforcement discipline — module boundaries checked at compile time, static architecture rules in CI, contract tests written before implementations. The device model, configuration, automation engine, and integration runtime are sequenced ahead of MVP, targeted for late 2026.

The agent adjudication layer described above is *designed for* rather than *shipped*: the event model reserves the seams it requires — separating action proposal, adjudication, and execution as distinct causally-linked event types, and treating agents as a first-class subject type — because those are cheap to reserve now and prohibitively expensive to retrofit into an immutable log later.

Device connectivity rides Matter and Thread rather than a bespoke per-vendor integration library. That's deliberate: as open standards absorb basic device interoperability, the differentiating work moves up the stack to orchestration, arbitration, and accountability — which is the layer this system is built for.

<!--
file: context/handoff/2026-06-26_parallel-fanout-v2_dispatch-brief.md
purpose: The SECOND coordinated parallel-session fan-out — three write-isolated RESEARCH sessions that mature the technical foundation in parallel with the development fleet, chosen by Nick 2026-06-26. Designed so the sessions cannot collide (disjoint write domains) or contradict (only the hub decides; sessions gather inputs). Each session below is self-contained — paste it into its own fresh conversation. The v6 hub reconciles every return into the spine.
audience: Nick (dispatcher) + each sub-session.
non-collision: one decider (the v6 hub + Nick's co-sign); disjoint write domains (sessions write only to context/assessments/ + spike/, NEVER the spine/design-docs/production-code); gating respected (none of these changes V1 scope — the hub reconciles and decides). The development fleet (frontend-dev, distribution, bench Session C) runs as a SEPARATE parallel track; these research sessions do not touch their trees.
-->

# Parallel Fan-Out v2 — Research Wave (HomeSynapse, 2026-06-26)

## The non-collision design (read this first)

Same three rules as the 2026-06-23 fan-out, which ran cleanly:

1. **One decider.** Every session below is a strictly **input-gatherer** (research) or a **measurement spike**. None decides, none self-ratifies, none changes V1 scope. The hub + Nick rule; the hub folds. → no contradictions.
2. **Disjoint write domains.** Each session writes ONLY to its own report under `context/assessments/` (and V2-A also to throwaway `spike/`). **The spine, the design docs, the amendments, and production code are written ONLY by the hub / the Core lane.** → no write collisions.
3. **Gating respected.** None of this is on the M7.4 critical path. V2-A + V2-B feed near-term milestones (D4 sizing / M9 prep); V2-C is forward runway (matures Doc 17, builds nothing). The hub reconciles each return as it lands.

| Session | Type | Writes ONLY | Feeds | Nick load |
|---|---|---|---|---|
| **V2-A — Pi dispatch-latency + log-growth spike** | Core throwaway spike | `spike/` + a report in `context/assessments/` | §1 D1 (co-location confirm) + D4 (retention/snapshot sizing) | Med (Coder builds; Nick runs on the Pi) |
| **V2-B — Converter-DB adapt-the-data embed-pipeline design** | Research / design | `context/assessments/` (its own report) | §1 D5 → the M9/device strategy + the legal spot-check | Low (autonomous) |
| **V2-C — AIoT-safety-frame + AI-authoring deep research** | Research | `context/assessments/` (its own report) | Doc 17 (the AIoT direction) + the AX-7 gate + the moat/claim | Low (autonomous) |

**Runs alongside (NOT in this brief — the development fleet):** the **frontend-dev** + **distribution-skeleton** lanes (`context/handoff/2026-06-21_*-lane_session_prompt.md`, refreshed 2026-06-26 — write only `web-ui/dashboard/` + `distribution/`) and **Session C** the hardware bench (`context/planning/2026-06-22_hardware-bench-...brief.md` — writes `project-knowledge/device-corpus/`). They don't collide with anything below.

Dispatch V2-A / V2-B / V2-C in their own fresh conversations; the hub folds each return as it lands.

---

## SESSION V2-A — Pi command-dispatch-latency + log-growth spike (CORE THROWAWAY SPIKE; re-issues the 2026-06-23 Session D)

GOAL. Produce the two Pi-class numbers the §1 architecture wants: (1) the added latency of **logical-event-driven, co-located dispatch** (the executor emits `command_issued` → an in-process subscriber consumes it, same JVM) **vs a direct in-process call** — to **confirm** the D1 co-location mitigation is negligible (D1 is RATIFIED, so this VALIDATES, it does not decide); (2) the **event-log growth rate + projection-rebuild (replay) time** as the log grows — to **size** the D4 retention/snapshot/compaction strategy.

CONTEXT. §1 D1 ratified event-driven/co-located dispatch (the seam scales to cross-process/cloud/AI later; co-located keeps MVP latency a single local hop). §1 D4 ratified the retention/snapshot discipline, *sized by these numbers*. The prior-art study warned the immutable log hits Home Assistant's Recorder-DB scaling wall (multi-GB DBs, SD-card wear on Pi-class) without retention designed early. HomeSynapse is Java/JPMS, event-sourced, Pi-class.

DO. (1) Build a **THROWAWAY** micro-benchmark (not production code) measuring per-dispatch overhead of emit-event-then-co-located-subscribe vs direct-call — **dev machine first, then the Pi after the bench frees the stick**. (2) Benchmark log append throughput + on-disk growth per N events, and projection-rebuild time vs log size, on Pi-class storage. (3) Report the numbers + implications: is the co-location latency negligible (confirming D1)? At what log size does rebuild become painful (sizing D4's snapshot cadence + retention windows)? **Honor the pure-function-replay rule (D2) in any harness — no device/external side-effects on replay.** Do NOT modify production code (measurement spike only; disposable under `spike/`, standing `git rm` after).

WRITE DOMAIN (isolation). Only throwaway code under `spike/` + one report `context/assessments/2026-06-DD_pi-dispatch-latency-and-log-growth_spike.md`. Do NOT touch production modules, the spine, or `module-info`.

RETURN. The two numbers + the implications for D1 (co-location confirmed?) and the D4 retention/snapshot design.

---

## SESSION V2-B — Converter-DB adapt-the-data embed-pipeline design (RESEARCH / DESIGN; M9-prep)

GOAL. Now that §1 D5 ratified **"adapt-the-data + curated-subset fallback,"** design the concrete embed pipeline: how HomeSynapse **ingests/transforms** the Z2M `zigbee-herdsman-converters` declarative data (`zigbeeModel`/`fingerprint` + `exposes`) into its ZCL-aligned device/capability model — with provenance/attribution/version-pinning discipline — so M9 builds device breadth against a **known pipeline**, not ad-hoc. Frame the LOW-risk legal spot-check items into a counsel-ready list. Produce a design + recommendation; NO production code.

CONTEXT + READS. §1 D5 (RATIFIED): adapt-the-data for the declarative core (identity + `exposes` capability data, MIT-clean) + curated-subset/community fallback for the `fromZigbee`/`toZigbee` transform long tail. Session A established the licenses (`zigbee-herdsman-converters` MIT, `zha-quirks` Apache-2.0; the **GPL-3.0 is only the Z2M *application*, not consumed**) and the technical fit (the `exposes` model maps onto HomeSynapse's ZCL model with modest transform). HomeSynapse is local-first, Zigbee-first, two coordinator paths (ZNP/EZSP), Java/JPMS. **Read first:** the Session A assessment (`context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md`) + the reconciliation memo; `design/02-device-model-and-capability-system.md` + `design/08-zigbee-adapter.md` (the §3.5 ZCL cluster→capability mapping); and the bench corpus (Session C output, as it lands) for real-device ground truth.

DO. (1) Design the **ingest/transform pipeline**: the `exposes` data shapes (light/numeric/binary/enum with units/ranges/access flags) → HomeSynapse device-model + capability rows; the mapping rules; the modest-transform standard-ZCL majority vs the code-shaped tail (`fromZigbee`/`toZigbee`, Tuya `0xEF00`, Xiaomi). (2) Design the **provenance/attribution discipline** (the retained-NOTICES artifact for MIT+Apache-2.0 — per-file vs consolidated) + the **pinned-version + periodic re-ingest** pipeline (the upstream DB updates constantly). (3) Frame the **curated-subset fallback** (top-N device priority targeting the V1 demo + UX devices; the community-contribution path). (4) Sharpen the **LOW-risk legal spot-check** into a counsel-ready list (Apache-2.0 NOTICE/patent mechanics at enterprise-sublicensing scale; the TS→Java derivative-work/attribution form; trademark/CSA "Zigbee" nominative-use). (5) Flag **what gates M9 vs what's deferrable.** Engineering due diligence, NOT a legal opinion; flag fact vs inference.

WRITE DOMAIN (isolation). Only one report `context/assessments/2026-06-DD_converter-db-embed-pipeline-design.md`. Do NOT write the spine, code, or design docs. A Doc 02/08 gap is an **escalation**, not an edit (the hub assembles the amendment).

RETURN. The pipeline design + the provenance/version discipline + the counsel-ready legal list + the M9-gating verdict (what must land before M9 scoping vs after).

---

## SESSION V2-C — AIoT-safety-frame + AI-authoring deep research (RESEARCH; the moat; forward / non-disruptive to V1)

GOAL. Mature the Doc 17 AIoT direction — **"AI proposes, the deterministic engine disposes"** — from a reserved principle into a *researched* architecture: the **planner → verifier/safety-gate → deterministic-executor** pattern, **NL → component authoring** (AI-as-author over the sealed model), and the **verification of AI-proposed automations** — so a future AIoT milestone is built against researched ground and the "safest AIoT" claim is defensible. **STRICTLY forward + non-disruptive: this researches and reserves; it changes NO V1 scope.** Any seam this surfaces that V1 must not preclude is an **escalation to the hub** (which checks V1 non-preclusion), never a V1 change.

CONTEXT + READS. Doc 17 (DRAFT, review-passed) reserves the four AI seams (author / reasoner / device-intelligence / safety-frame) as non-precluding; **AIOT-INV-1** (AI is never an autonomous actuator) is the candidate invariant; **E3** (from the Doc 17 review) asks for the *structural* enforcement — a composition-root proposer-only port. The prior-art study found **planner→verifier→deterministic-executor is the emerging industry consensus** (and HA Assist's deterministic-first/LLM-fallback). HomeSynapse's architecture already embodies the frame: AI proposals become proposed **component-based definitions** that *expand into the sealed permits* (INV-SA-01 — statically analyzable), governed by the deterministic, **no-autonomous-retry** engine (INV-SA-04 / AMD-90-INV-01), auditable via the immutable log (INV-SA-03). **Read first:** `design/17-aiot-and-cloud-readiness.md` (DRAFT) + its independent review return (`context/audits/2026-06-26_Doc17_independent_DOCS_Review_Return.md`); `design/16-superior-automation.md` §3.2 (the component model) / §3.3 (explanation projection); the §1 decision record (D2 replay-safety; the §"Reserved seams" AI-safety frame); the 2026-06-23 prior-art study + its PM assessment.

DO. (1) Survey the current (2026) state of **safe-AI-in-the-home + LLM-agent-safety architectures** (planner/verifier/safety-gate patterns; formal + runtime verification of generated automations; the deterministic-executor-as-safety-frame approach). Verify the patterns; **flag fact vs inference; cite primary sources; distinguish "the pattern is real" from specific paper citations** (the deep-research harness can fabricate plausible paper names — use the pattern, verify the citation before quoting any as authority). (2) Map each to HomeSynapse: how **AI-as-author** (NL → `AutomationComponent` instances expanding into sealed permits) gets the **load-time static checks** (unresolved refs, type mismatches, shadowed/duplicate triggers) as a verification layer no competitor offers; what the **composition-root proposer-only port** (Doc 17 E3) should look like structurally (the analog of INV-LF-02's no-outbound-network enforcement); how the **explanation projection** serves AI-as-reasoner. (3) Identify the **AX-7 component-versioning policy** the AI-authoring seam needs (the gate before shareable/AI-authored components). (4) Surface what's **genuinely novel/defensible (the moat)** vs table-stakes, and the **honest claim language** for "safest AIoT." (5) Flag any seam this research finds that **V1 must NOT preclude** (escalate — the hub checks).

WRITE DOMAIN (isolation). Only one report `context/assessments/2026-06-DD_aiot-safety-frame-and-ai-authoring_research.md`. Do NOT write the spine, code, or design docs. This is **forward research** — it changes no V1 scope; any seam-preclusion concern is an escalation to the hub.

RETURN. The researched safety-frame architecture + the AI-authoring/verification mapping + the AX-7 gate + the moat/claim-language verdict + any V1-non-preclusion flags.

---

## Disposition

Dispatch V2-A / V2-B / V2-C now in their own fresh conversations (V2-A when a Coder slot + the Pi free up; V2-B / V2-C are autonomous). They run independently of each other AND of the development fleet (frontend-dev, distribution, Session C). The hub folds each return into the spine as it lands — V2-A → D4 sizing; V2-B → M9 prep; V2-C → the Doc 17 fold/Lock + the eventual AIoT milestone runway. None changes V1 scope; the mid-August go/no-go and the Core critical path are untouched.

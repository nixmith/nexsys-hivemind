<!--
file: context/handoff/2026-06-23_parallel-fanout_dispatch-brief.md
purpose: A coordinated parallel-session fan-out for HomeSynapse, designed so the sessions cannot collide (disjoint write domains) or contradict (only the hub decides; the dispatched sessions only gather inputs). Authored 2026-06-23 by the v5 hub. Each session below is self-contained — paste it into its own fresh conversation. The v6 hub reconciles every return into the spine.
audience: Nick (dispatcher) + each sub-session.
-->

# Parallel Fan-Out Dispatch Brief — HomeSynapse, 2026-06-23

## The non-collision design (read this first)

Parallel sessions are safe only if they cannot step on each other. Three rules make that true here:

1. **One decider.** The architecture DECISIONS (the deeper-M7 §1 questions — command-pipeline shape, the new invariants, log retention, the converter-DB direction) are made by the **v6 hub + Nick's co-sign**, NOT by any dispatched session. Every session below is a strictly **input-gatherer** (research) or a **measurement/characterization** task. None decides; none self-ratifies. → no contradictions.
2. **Disjoint write domains.** Each session writes ONLY to its own domain, listed in its prompt. **The spine (PROJECT_SNAPSHOT, pm-handoff, the backlog, the decision records, the §1 record) is written ONLY by the hub.** → no write collisions.
3. **Gating respected.** M7.4 (the live command-pipeline) and the Doc 07 §3.11 / AMD-90 reconciliation are DOWNSTREAM of the §1 ruling — they are **NOT** dispatched now. They proceed serially after the hub ratifies §1 with the returns below in hand.

| Session | Type | Writes ONLY | Feeds | Nick load |
|---|---|---|---|---|
| **A — Converter-DB license + feasibility** | Research | `context/assessments/` (its own report) | §1 + M9/device strategy (Decision 4) | Low (autonomous) |
| **B — "Why-not" differentiator + moat** | Research | `context/assessments/` (its own report) | the differentiator/positioning claim | Low (autonomous) |
| **C — Hardware bench bring-up + characterization** | Hardware + corpus | `project-knowledge/device-corpus/` + a bench report; **escalates** Doc 02/08 gaps (hub folds) | M9 ground-truth + Doc 02/08 validation | High (hands-on) |
| **D — Pi command-dispatch latency + log-growth spike (optional)** | Core throwaway spike | `spike/` (throwaway) + a benchmark report in `context/assessments/` | §1 Decision 1 (the co-location latency mitigation) + the log-retention design | Med (Coder builds; Nick runs) |

**What the v6 hub owns (serial, not parallel):** the §1 architecture synthesis (ratify the decisions with Nick), then the Doc 07/AMD-90 reconciliation, then M7.4a → M7.4b. **Also available to re-launch when bandwidth allows:** the existing write-isolated `frontend-dev` and `distribution-skeleton` lane prompts (`context/handoff/2026-06-21_*-lane_session_prompt.md`) — they write only `web-ui/dashboard/` and `distribution/` and build against the frozen v1.1 read-API contract, so they don't collide with anything above.

Dispatch A, B, C now (and D if Coder bandwidth allows). They run independently; the hub folds each return as it lands.

---

## SESSION A — Zigbee converter-database license + feasibility review (RESEARCH)

GOAL. Determine whether HomeSynapse should ADAPT/INTEROP an existing Zigbee device-converter database (rather than rebuild the device-quirk long tail from scratch), and exactly how — answering the license question and the technical-fit question. Produce a recommendation with confidence.

CONTEXT. HomeSynapse is a local-first, event-sourced smart-home OS (Java/JPMS, Pi-class), Zigbee-first, with a device model of entities → devices → capabilities aligned to standard ZCL clusters, two coordinator paths (TI CC2652/ZNP and Silicon-Labs EFR32/EZSP). It will ship as ONE runtime across free → paid → enterprise tiers (not a fork). A prior-art study found the device-quirk long tail (Tuya's non-standard `0xEF00` cluster, Xiaomi deviations) is the dominant integration cost, and that Zigbee2MQTT (`zigbee-herdsman-converters`, MIT) and ZHA (`zha-device-handlers`, Apache-2.0) solved it with community converter databases. Re-deriving thousands of device definitions is a multi-year cost with no differentiation payoff — the database is the cost and the moat.

DO. (1) Confirm the actual licenses + any notices/attribution obligations of `zigbee-herdsman-converters` and `zha-device-handlers` (and `zigbee-herdsman` itself), read from their LICENSE/NOTICE files. (2) Assess compatibility with shipping HomeSynapse commercially across free/paid/enterprise tiers (including whether the data can be embedded, redistributed, or must be kept separable; copyleft vs permissive implications; trademark/attribution). (3) Assess TECHNICAL fit: can the converter definitions be consumed as DATA (declarative, "quirks-as-data," no per-device code release) and mapped onto HomeSynapse's ZCL-aligned capability model? What is the data shape, and what is the adaptation effort? (4) Recommend one of: adapt-the-data (embed/transform), interop-at-runtime, or a curated-subset + community-contribution fallback — with the trade-offs and what would change the call.

WRITE DOMAIN (isolation). Write ONLY one report: `context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md`. Do NOT write the spine, code, or any other file. Do NOT make the final decision (recommend; the hub + Nick rule). Cite sources; flag fact vs inference; note anything needing a lawyer's confirmation.

RETURN. The report + a one-paragraph recommendation-with-confidence the hub can fold into §1 / Decision 4.

---

## SESSION B — "Why did it NOT fire?" differentiator + competitive-moat search (RESEARCH)

GOAL. Test and qualify HomeSynapse's flagship differentiator claim — that no shipping smart-home system DURABLY answers "why did this NOT fire?" (trigger-never-matched vs condition-false vs device-didn't-confirm) or "did the device actually confirm it acted?" — and surface anything that strengthens or threatens it.

CONTEXT. HomeSynapse's differentiator is explainability as a pure projection of an immutable, causally-chained event log: a non-expert can ask "why did this fire? / why did it NOT fire? / did it confirm?" durably (never evicted). A prior-art study found Home Assistant's automation traces are the closest prior art and fall short (in-memory, default 5, evicted, and NOT created at all when a trigger never matches) — but it flagged this as "absence of evidence, not proof."

DO. (1) Investigate whether any shipping platform — Home Assistant (latest), Hubitat, SmartThings, openHAB, Apple Home, Josh.ai, Control4, Crestron, Homey, recent AI-home entrants — durably answers the non-firing question or does command-outcome honesty (dispatched → confirmed/unconfirmed/failed) well. Look at docs, forums, reviews, and any architecture talks. (2) Surface any PATENT / IP in this space (automation explainability, causal tracing, command-confirmation) that HomeSynapse should be aware of. (3) Assess how DEFENSIBLE the differentiator is: is it a durable moat (architecture-enabled — the immutable log), or could a competitor add it quickly? (4) Note how to FRAME the claim honestly (what we can truthfully say vs what overclaims).

WRITE DOMAIN (isolation). Write ONLY one report: `context/assessments/2026-06-23_explainability-differentiator-moat_research.md`. Do NOT write the spine, code, or any other file. Cite sources; flag fact vs inference; distinguish "no evidence found" from "confirmed absent."

RETURN. The report + a one-paragraph verdict: how unique/defensible the differentiator is, the honest claim language, and any IP to watch.

---

## SESSION C — Hardware bench bring-up + device characterization (HARDWARE + CORPUS; Nick-driven)

GOAL. Bring the Wave-1 Zigbee hardware up on the Raspberry Pi and characterize the curated device set, building the durable device corpus and validating the design docs against real silicon — so M9 (the Zigbee integration milestone) is built against ground truth.

CONTEXT + READS. HomeSynapse is local-first, Zigbee-first, two coordinator paths. Wave-1 hardware (on the desk): Sonoff Zigbee 3.0 USB Dongle Plus **MG24** (EFR32MG24 / **EZSP** path, Thread-capable) + Philips Hue Essential White-and-Color A19 2-pack (pairs DIRECT to the coordinator, no Hue bridge) + 2× Sonoff **SNZB-03P** motion (the hero trigger; its "SONOFF bridge required" listing is marketing — it pairs to any Zigbee 3.0 coordinator incl. the MG24) + a USB extension (anti-interference). Read first: `context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md` (the bring-up + characterization protocol), and `design/08-*` (Zigbee, the two coordinator paths, the §3.5 cluster table) + `design/02-*` (device model / capability / Expectation).

DO. Per the bench brief: (1) bring up the MG24 on the Pi via the EZSP path; **capture the coordinator detection fingerprint** (for INV-CE-04 auto-detection); note the EZSP/EmberZNet version (EZSP protocol-version mismatches are a documented hard-failure class — record it). (2) Pair the Hue light and the SNZB-03P motion sensors; capture their ZCL endpoints/clusters/attributes. (3) Characterize each device → write a `project-knowledge/device-corpus/` entry per device (the corpus is the M9 acceptance ground-truth). (4) For each device, give a **Doc 02 / Doc 08 MATCH or GAP verdict** — does the device model + cluster table cover it? (5) Validate the hero path end-to-end conceptually: **motion → light on**. (6) Note any coarse runtime observations useful later (pairing time, event volume) — these feed the log-retention thinking.

WRITE DOMAIN (isolation). Write ONLY `project-knowledge/device-corpus/` entries + one bench report (e.g. `project-knowledge/device-corpus/2026-06-23_wave1-benchup-report.md`). Do NOT write the spine, the design docs, or code. **A Doc 02/08 GAP is an ESCALATION, not an edit** — report it; the hub assembles the amendment, Nick co-signs, the hub folds.

RETURN. The corpus entries + the MATCH/GAP verdicts + the coordinator fingerprint + any escalations.

---

## SESSION D — Pi command-dispatch-latency + log-growth spike (CORE THROWAWAY SPIKE; optional, run if Coder bandwidth)

GOAL. Produce the two Pi-class numbers the architecture ruling wants: (1) the added latency of **logical-event-driven dispatch** (executor emits `command_issued` → an in-process subscriber consumes it) vs a **direct in-process call**, and (2) the **event-log growth rate + projection-rebuild time** as the log grows — to validate the co-location latency mitigation and size the log-retention/snapshot strategy.

CONTEXT. The command-pipeline decision is leaning **event-driven, physically co-located for MVP** (emit `command_issued`; an in-process subscriber dispatches) — chosen so the seam scales to cross-process/cloud/AI later while keeping MVP latency minimal. A prior-art study warns the immutable log will hit Home Assistant's Recorder-DB scaling wall (multi-GB DBs, SD-card wear) without retention/snapshots designed early. HomeSynapse is Java/JPMS, event-sourced, Pi-class.

DO. (1) Build a THROWAWAY micro-benchmark (not production code) measuring the per-dispatch overhead of emit-event-then-subscribe vs direct-call, on a dev machine first then ideally on the Pi (after the bench frees it). (2) Benchmark log append throughput + on-disk growth per N events, and projection-rebuild (replay) time vs log size, on Pi-class storage. (3) Report the numbers + an implication for the co-location decision (is the latency negligible?) and for retention (at what log size does rebuild become painful?). **Do NOT modify production code** — this is a measurement spike only; respect the no-side-effects-on-replay rule in any harness.

WRITE DOMAIN (isolation). Write ONLY throwaway code under `spike/` (the existing `spike:` throwaway convention) + one report `context/assessments/2026-06-23_pi-dispatch-latency-and-log-growth_spike.md`. Do NOT touch production modules, the spine, or `module-info`. The spike is disposable (standing `git rm` after the numbers are captured).

RETURN. The two numbers + the implications for Decision 1 (co-location) and the log-retention design.

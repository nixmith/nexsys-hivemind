<!--
file: context/handoff/2026-06-14_core-review_B_runtime-automation-M7_session_prompt.md
purpose: Review Session B of the two-part homesynapse-core review — runtime, integration, automation, API, observability & composition (modules 9–22). Build the model, hunt defects, and give the deepest forward treatment to M7-readiness (automation). Feeds the converge session.
audience: PM (Cowork, fresh conversation), Nick
state-type: session prompt
status: READY (commit + dispatch as a fresh Cowork conversation; parallel-capable with Session A)
-->

# Review Session B — Runtime, Integration, Automation & Composition (M7-forward)

**Read `context/handoff/2026-06-14_core-review_FRAMEWORK.md` in full first** — stance, calibrated-honesty rule, Step 0, per-module checklist, defect taxonomy, finding format, guardrails. This prompt carries only your scope and focus.

**Your half of the system:** the behavior, integration, API, and composition layers — including **`automation`, the M7 target**, and `lifecycle`, the composition root where a missed wiring is a latent runtime defect no unit test pins. **Session B's defining question: is the runtime/composition sound, and is M7 (automation) ready to build?** Your automation modules depend on Session A's spine (event/device/state) — build a working model of those from source as needed; you are not re-auditing them, and the converge merges your findings with A's deep audit.

## Scope — review in this order (integration up to the apex, then testing)

| # | Module (JPMS name) | Focus | Priority |
|---|---|---|---|
| 9 | `integration/integration-api` (`com.homesynapse.integration`) | The frozen M4.C contract — descriptor/context/capability surfaces, the 5 lifecycle permits, `CredentialRotator`/`SecurityServices`, `RequiredService` gating. | medium |
| 10 | `integration/integration-runtime` (`com.homesynapse.integration.runtime`) | The runtime/supervisor scaffolding (M9 territory) — failure isolation, backoff, the health model. M7- and M9-adjacent. | medium |
| 11 | `integration/integration-zigbee` (`com.homesynapse.integration.zigbee`) | The Zigbee adapter (M14, the highest-risk milestone). Assess what exists and its real-hardware exposure. | light–medium |
| 12 | `core/automation` (`com.homesynapse.automation`) | **The M7 target.** Triggers/conditions/actions, the run manager, the sealed permit hierarchies (~53 types). Assess M7-readiness: do the ratified **AMD-88..93** contracts hold against the live event/device/state surfaces? Cascade/loop prevention (`cascade_depth_exceeded`, AMD-92), the **C1-interim pin** (no production `automation_triggered` publish before M7.2), Pi-4 trigger-evaluation cost. | **DEEP** |
| 13 | `api/rest-api` (`com.homesynapse.api.rest`) | Endpoints, `ReadinessFilter`/`RestFilters`, the QUERY_SERVICE_READ_ONLY + REST_NO_EVENT_PUBLISHING ArchUnit rules — verify those boundaries actually hold in code, not just in the rule. Input-validation surface. | medium |
| 14 | `api/websocket-api` (`com.homesynapse.api.ws`) | The WS surface, subscription + backpressure to clients. | light–medium |
| 15 | `observability/observability` (`com.homesynapse.observability`) | Metrics, health contributors, the `IntegrityService` seam (M12). The MDC-on-virtual-threads question (R-ε) lives near here. | medium |
| 16 | `lifecycle/lifecycle` (`com.homesynapse.lifecycle`) | **The composition root.** `HomeSynapseCore` — the 16-step bootstrap, dependency-order wiring, the M6.3 cipher forwarding, shutdown integrity, the systemd/health seams. A missed manifest/wiring here is a latent runtime defect no test pins. | **DEEP** |
| 17 | `app/homesynapse-app` (`com.homesynapse.app`) | `Main` — the apex, the `payloadCipher` adapter, and the **un-built `main()` runtime construction** (the app-bootstrap milestone). Note what is reserved vs. wired. | medium |
| 18 | `platform/platform-systemd` | Linux paths + systemd health reporter behind the `NotifyTransport` seam (OR-M13-SDNOTIFY — sd_notify deferred to M13). | light |
| 19 | `testing/test-support` | The shared fixtures/test doubles — do they faithfully mirror production contracts (the `CountingPayloadCipher`-style fidelity question)? | light–medium |
| 20 | `testing/integration-tests` | The on-device ITs (BurstLoad / HeapBudget / CrashRecovery / Pi4 suites). **Assess whether the ITs prove what they claim** — this is where end-to-end correctness is actually exercised; weak ITs are a high-leverage finding. | medium |
| 21 | `web-ui/dashboard` | Scaffold stub — confirm it is a stub; note any premature surface. | light |
| 22 | `spike/wal-validation` | Throwaway spike — confirm it carries no production dependency; flag if still in-tree (the standing `git rm` advisory). | light |

## Session-B emphases (beyond the framework checklist)

- **M7-readiness is the headline.** Give `automation` (12) the deepest forward treatment. Read the M7 planning set first: `context/planning/2026-06-11_M7-blueprint_research-architecture.md`, `2026-06-12_M7-M8-charter-skeleton.md`, `2026-06-12_M7-blueprint_merged-disposition.md`, + **Doc 07** (Automation Engine, Locked) + the automation MODULE_CONTEXT. Then assess what the ~53 automation types actually provide vs. what M7.1 needs: concurrency/isolation model, cascade/loop safety, trigger-evaluation performance on the Pi-4 floor, and any gap between AMD-88..93 and the live event/device/state contracts automation consumes.
- **The composition root** (`lifecycle`, `app`) — the framework's "a missed manifest no test pins" hazard is concentrated here; trace the 16-step bootstrap against the modules it wires (incl. the M6.3 cipher path).
- **Do the ITs earn their keep?** For `integration-tests`, the mutation-mindset matters most — a crash-recovery IT that would still pass if recovery were broken is a HIGH finding.

## Deliverable

`context/audits/2026-06-14_core-review_B_runtime-automation-M7.md` — per the framework's finding format: an **executive summary** (top findings + the runtime/composition health verdict + **the M7-readiness call**), **per-module sections**, **cross-cutting findings**, a **coverage ledger** (every module 9–22 → depth → finding count), and a **"research avenues surfaced"** section with M7 forward-research first (the converge consolidates). Hand Nick a commit message (`!`-free).

## Done-when

Modules 9–22 each have a ledger row; the audit is on disk; the executive summary + the explicit M7-readiness call are written; any BLOCKING finding is escalated; the research-avenues section (M7-forward) is captured for the converge; commit message handed over. (Parallel-capable with A; the converge merges both.)

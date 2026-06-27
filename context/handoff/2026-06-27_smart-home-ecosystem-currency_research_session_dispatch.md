<!--
file: context/handoff/2026-06-27_smart-home-ecosystem-currency_research_session_dispatch.md
purpose: Dispatch brief for a FRESH, write-isolated, web-backed research session that refreshes the smart-home / ecosystem CURRENCY on the three clusters that actually steer V1 decisions and positioning — and returns an assessment that feeds back to the v8 product hub for steering. NOT open-ended trend-surfing; scoped to decision-impact.
audience: a fresh research Cowork session (the deep-research skill is the vehicle); Nick (launches it, relays the return to the hub).
state-type: session prompt (one-shot research; write-isolated; off the M7.4 critical path).
status: READY — authored 2026-06-27 by the v8 hub. Launch when Nick chooses; runs in parallel with the M7.4b build, disjoint write domain (writes only to context/assessments/).
-->

# Research Dispatch — Smart-Home / Ecosystem Currency (decision-relevant, web-backed)

You are a **fresh, write-isolated research session**. Your job is to refresh the **current (mid-2026) state** of three smart-home / ecosystem areas **that steer live HomeSynapse decisions**, verify claims against primary sources, and return a cited assessment. The HomeSynapse model's knowledge is ~a year stale on these, so **web search is mandatory** — do not answer from priors. **Scope discipline: this is decision-relevant currency, not a survey.** If a thread does not change a V1 decision or the positioning, note it in one line and move on.

## Write-isolation + non-collision (read first)
- You write **only** to `context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md` (create it). Touch **no** other spine file, **no** design doc, **no** Core code. The hub reconciles your return.
- Verify every load-bearing claim against a primary source; cite each (URL + date). Flag anything you cannot verify as `[UNVERIFIED]` — do not launder it into fact (the SafeGate-citation lesson).
- The hub already holds prior research on two of these; your value is the **DELTA + currency**, not re-deriving the baseline. Read the baselines below first so you complement, not duplicate.

## Reads (the established baseline — complement, don't repeat)
- `context/decisions/2026-06-20_V1-launch-scope_decision-record.md` (what is IN/OUT for V1 — e.g. Matter deferred; the hero demo).
- `context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md` §D5 + the reserved AIoT seams (the converter-DB direction; the AI-proposer frame).
- `context/assessments/2026-06-21_explainability-UX-competitive-research.md` (the "why-did / why-didn't / did-it-confirm" competitive baseline).
- `context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md` + `2026-06-23_prior-art-study_PM-assessment-and-forward-plan.md` (the AIoT / prior-art baseline).
- `context/decisions/2026-06-26_wave1-device-model-reconciliation_decision-record.md` + the AMD-96 amendment (EZSP v14 / EmberZNet 8.x currency; the White/CT color-scope call).
- `homesynapse-core-docs/design/17-aiot-and-cloud-readiness.md` (Locked; the AIoT vision the positioning rests on).

## The three clusters (each: the current state, then "what it changes for us")

### Cluster 1 — Zigbee / Thread / Matter trajectory + the converter-DB health (feeds AMD-96, M9, the V1 scope)
- **EmberZNet / EZSP current state:** the bench found real silicon at **EmberZNet 8.x / EZSP v14** while Doc 08 describes v13/7.4. What is the current shipping EmberZNet/EZSP for the EFR32MG24, and is there a newer one in flight? (Sizes the AMD-96 currency amendment + the M9 v14/ASH test item.)
- **Matter trajectory:** V1 deliberately defers Matter. Is "defer Matter for V1, Zigbee-first" still the right call in mid-2026, or has Matter's maturity/adoption shifted enough to reconsider the reserved seam timing? (Decision: confirm or re-open the V1 deferral — non-precluding either way.)
- **Thread:** any change to the MG24's Thread relevance for the reserved multiprotocol seam.
- **The converter-DB dependency:** the health/licensing of `zigbee-herdsman-converters` / `zigbee-herdsman` / `zha-device-handlers` as of mid-2026 — any relicensing, governance change, or fork that would re-weight the D5 "adapt-the-data + curated fallback" decision or its recorded re-open triggers.

### Cluster 2 — Durable "why-did / why-didn't / did-it-confirm" explainability — the competitive/moat state (feeds the differentiator + the mid-Aug positioning)
- Since 2026-06-21, has **any** smart-home platform (Home Assistant, Hubitat, SmartThings, Homey, the closed ecosystems) shipped **durable, plain-language** automation explainability — specifically the **"why didn't it fire?"** and **"did the device actually do it?" (confirmed/unconfirmed)** halves, never-evicted? 
- Confirm whether the moat still holds: is durable plain-language *non-firing* + *confirmation* explainability still unshipped elsewhere, or has the gap closed? Distinguish a genuine durable projection from a transient trace/log view.

### Cluster 3 — AIoT / LLM-in-home-automation safety frame + patent landscape (feeds Doc 17 + the commissioned Q1 patent search + claim language)
- Is **planner → verifier/safety-gate → deterministic-executor** still the 2026 consensus for LLM-driven home automation? Any notable new entrants or shifts since 2026-06-23.
- The Doc 17 moat is **"AI emits components that expand into a sealed permit schema, statically rejected at load if malformed — verifying the authored *form*, not just plan behavior."** Has anyone shipped or **patented** this (type-checking the authored automation form against a sealed schema)? This is the Q1 patent-search question — surface any blocking prior art or patents.
- Confirm the defensible claim language ("AI is structurally a proposer, statically verified, durably auditable") vs. the counsel-gated superlatives ("safest AIoT", "can never misfire").

## Output (the return)
Write `context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md`:
- Per cluster: **the current state (cited)** → **what it changes for HomeSynapse** (a concrete decision delta: confirm / re-open / amend / no-change), keyed to the artifact it touches (AMD-96, Doc 17, the V1-scope record, the go/no-go).
- A top **"decisions for the hub"** list (what Nick + the hub should rule on the back of this), ranked by impact.
- A source table (claim → source → date → verified/UNVERIFIED).
- Keep it tight; flag non-decision-relevant findings in one line each.

**On return:** Nick relays it to the v8 product hub, which reconciles it with a one-line spine note and folds the decision deltas into the relevant currency reviews (AMD-96 / Doc 17) + the mid-Aug go/no-go — keeping HomeSynapse steered by current ground truth, not year-stale priors.

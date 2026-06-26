<!--
file: context/handoff/2026-06-21_frontend-dev-lane_session_prompt.md
purpose: Dispatch prompt for the FRONTEND-DEV lane — a write-isolated, sustained Cowork session that builds the V1 observability dashboard (shell, design system, AB-1 auth, device/event/health views, and the explainability hero view) against the FROZEN read-API contract. The long pole among non-Core lanes (~6–8 wks, no slack) — start now.
audience: a fresh Cowork session (frontend engineer role); Nick (launches it, relays its returns to the hub)
state-type: session prompt (lane dispatch — sustained, not one-shot)
status: ISSUE-READY 2026-06-21 (v3 hub). Launch after the read-API contract freeze (DONE 2026-06-21).
writes-only: homesynapse-core/web-ui/dashboard/… + this lane's return under context/audits/ (NEVER the spine, NEVER core Java, NEVER another lane's tree).
anchors: context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md (THE contract — build against it) · homesynapse-core-docs/design/13-web-ui-observability-mvp.md (Locked) · design/16-superior-automation.md (the hero) · context/decisions/2026-06-20_V1-launch-scope_decision-record.md (V1 scope + the Nov-25 schedule)
-->

# Frontend-Dev Lane — V1 Observability Dashboard (sustained)

You are the **frontend engineer** for HomeSynapse Core's V1 dashboard — a long-lived, write-isolated Cowork lane. You build the user-facing surface where the differentiator finally becomes visible: *a stranger pairs a sensor and a light, watches an automation fire, clicks "why did this fire?", and understands the answer.* You are the long pole among the non-Core lanes (~6–8 weeks, no slack) — **start now.**

## The one-sentence frame
The product is the demo, and the demo is **the explainability view over a live automation running real devices.** Everything you build sequences backward from that hero view. The device/event/health views are the supporting cast; the "why did this fire?" causal-chain view is the hero.

## 0.5 — 2026-06-26 dispatch refresh (v6 hub; LAUNCH NOW under the full-parallel-fleet ruling)

- **Spine state:** core `5363347` (M7.3 DELIVERED GREEN); the §1 architecture is RATIFIED (event-driven/co-located command pipeline). The hero view renders on a **LIVE** `RunCausalChain` once **M7.4** wires the pipeline (the next Core milestone). So **build the shell + device/event/health views NOW** against the existing A-class REST, and the **hero against the B3 mocks**; swap the hero to live as M7.4 + the thin causal-read-API land. Nothing here waits on M7.4.
- **The hero is BOTH halves (v1.1):** the causal chain — **"why did this fire?" AND "why did it NOT fire?"** (the suppression-reason surface) — AND the command-outcome state **`dispatched → confirmed | unconfirmed(timeout) | failed(reason)`** ("did it actually confirm?"). Mock B3 to both; **never render a silent blank** — always an explainable, plain-language origin (the differentiator is durable, never-evicted explanation).
- **No WebSocket in V1 (FIRM):** poll the A-class/B-class REST at 1–2s; it reads as real-time for a home dashboard.
- Everything else in this prompt stands. Your return is a short status doc under `context/audits/`; the hub reconciles it.

## 0. Write-isolation (binds — the single-spine-writer model)
- You write **only** under `homesynapse-core/web-ui/dashboard/…` (the declared-but-empty Gradle scaffold module — 0 source files today) and your **lane return** (a short status doc the hub reconciles).
- You do **NOT** write: the hivemind spine (PROJECT_SNAPSHOT, pm-handoff, backlogs, decisions), core Java, the Distribution tree, or any design doc. If you need a spine/Core change, **surface it to the hub** (via Nick) — do not make it.
- You push your branch; **CI is the gate of record** (`ci-as-gate-of-record.md`). Hand back fix-applied; CI verifies.

## 1. The contract you build against (FROZEN — do not assume beyond it)
`context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` is the binding interface. Two classes:
- **A-class (EXISTING — real endpoints, build live):** `GET /api/v1/entities` (list), `/{entityId}`, `/{entityId}/state`; `GET /internal/projection`, `/internal/dlq` (health inputs). Envelope: `{ data, [pagination], meta: { viewPosition, timestamp } }`. RFC 9457 `problem+json` errors.
- **B-class (FROZEN-UNBUILT — build against MOCKS, Core implements TO these):** `GET /api/v1/events` (B1), `GET /api/v1/health` (B2 — or compose A4+A5), and **the hero: `GET /api/v1/runs?…` + `GET /api/v1/runs/{runId}/causal-chain` + `GET /api/v1/automations` (B3)**. Mock B1/B2/B3 exactly to the frozen shapes; swap to real endpoints as Core delivers them.
- **If you need the contract to change, it is a cross-lane event — raise it to the hub, do not diverge.** Build a typed API client + a single mock layer so the real/mock swap is one switch.

## 2. Settled lane decisions (the hub's calls — implement, don't re-litigate)
- **Auth (AB-1):** every request carries `Authorization: Bearer {token}`. The operator pastes a token (the first-run pairing token, written by Core to `config/initial_api_token`). Handle **401** (`authentication-required` → prompt for token) and **403** (`forbidden` → invalid/expired). No pre-auth enumeration; no stored secret beyond the in-memory session token.
- **No WebSocket (D-OPEN-3 firm).** **Poll the read endpoints at 1–2s.** Use the `meta.viewPosition` monotonic cursor for cheap change-detection (only re-render when it advances). Handle **503 `state-store-replaying`** as a first-class "starting up / catching up" state with backoff — not an error toast.
- **Stack (RECOMMENDED default — confirm at lane start):** a lightweight **TypeScript SPA** (e.g., Svelte or React) built with **Vite**, output as **static assets served by the `web-ui:dashboard` Gradle module** off the existing loopback HTTP surface (no separate server, no SSR — local-first, constrained-hardware, single-binary distribution). Doc 13 (Web UI Observability MVP, Locked) governs the UX scope; if it mandates a different stack, Doc 13 wins — read it first and flag any conflict. Keep the dependency footprint small (this ships in a jlink image to a Pi).
- **Design system first.** A small token-based design system (color/space/type, a component kit: table, card, status pill, detail drawer, the causal-chain tree) before the views — so the hero view is polished, not bolted on.

## 3. Build sequence (matches the V1 record's scheduled seam)
1. **Now (zero Core dependency — all A-class real):** app shell + routing + the design system; the **auth flow** (token entry → bearer header → 401/403 handling); the **device views** (A1 list → A2/A3 detail/state, with the typed `attributes`, `availability`, `stale`, freshness via `meta`); the **health view** (compose A4 `/internal/projection` + A5 `/internal/dlq` — projection mode/lag, DLQ depth; the "live vs catching-up" signal).
2. **Soon (B1 mock → real):** the **event view** (a polled, paginated event feed over `GET /api/v1/events`; tail with `since=<nextCursor>`). Build against the B1 mock; the hub will flag when Core lands B1.
3. **The scheduled seam (B3 — the HERO):** build the **two co-equal hero views** against the **B3 mock now** — (i) **"why did this fire?"** (run list → a run's causal-chain tree: trigger → conditions-evaluated with `observedState` → actions with `outcome` → terminal) and (ii) **"why didn't it fire?"** (the `/non-firing` read with the three-way verdict CONDITION_NOT_MET / NEVER_TRIGGERED / ACTED_BUT_UNCONFIRMED / DISABLED). Both integrate against the **real** causal-query API **after M7.2b** (+ M7.3 for the confirmed/unconfirmed outcome half — see the M7.2b decision record). Plus the supporting surfaces: the **automation list** (`/automations`) and **run outcomes**. Build both heroes to the principles below — they ARE the product.

## 3a. Hero-view design principles (from the 2026-06-21 explainability research — `context/assessments/2026-06-21_explainability-UX-competitive-research.md`)
The research found every competitor (HA, Hubitat, SmartThings, openHAB, Node-RED) fails explainability in the same five ways, and two gaps are wide open. These seven are why HomeSynapse exists — not polish:
1. **Two co-equal questions.** "Why **did** it fire?" *and* "Why **didn't** it?" as peer entry points. The second is the single most differentiated thing in the field — **no competitor distinguishes condition-false vs trigger-never-matched vs device-didn't-act.** Not an afterthought.
2. **Plain-language, device-backward.** Start from what the user noticed ("the hallway light is on") and walk back in plain sentences ("…because the 'evening lights' automation fired, because the hallway motion sensor detected motion at 9:42 pm"). **Never** index paths like `conditions/0/conditions/1` (HA's documented failure).
3. **Show command outcome, not just intent.** Render `confirmed | unconfirmed | failed(reason)` on every action — "command *sent*" is what every competitor shows and users distrust; "the light actually **confirmed**" (or honestly, "sent, never confirmed") is the trust win no one delivers. (`confirmed`/`unconfirmed` arrive with M7.3; render `dispatched`/`failed` until then.)
4. **Never a silent blank.** Every event shows its `origin` (automation/device/user/external/**unknown**). The honest `UNKNOWN` is a value, never an empty cell — distinguish "we don't know" from "nothing caused it."
5. **Lead on "never evicted."** The explanation is a projection of the immutable log (INV-SA-03) → the run you need is **always reconstructable**. The #1 trace complaint everywhere ("the 3 am run I needed is gone — HA keeps only 5") structurally cannot happen here. Promote that in the UI.
6. **Bounded visual chain.** A small per-run visual chain reads better than text (Node-RED's lesson) — keep it per-run (bounded) and make error/non-firing paths first-class (where Node-RED breaks).
7. **Mom-test the language.** A stranger reads the explanation aloud and is right. That is the acceptance bar — not "a power user can decode it."

## 4. Disciplines (carry-pins)
- **Build against the frozen contract; treat any needed change as a cross-lane event** routed to the hub.
- **CI is the gate of record.** Add a frontend CI job (lint + typecheck + unit tests + production build) and a **contract-check** that your API client's expected shapes match the frozen contract (so a Core drift fails CI, not the demo). Run your lint/typecheck/build locally before handoff (the shift-left self-step).
- **Accessibility + the stranger test.** The hero view must be legible to someone who has never seen the system — that is the product thesis. Plain language ("Motion detected in Hallway → turned on Hallway Light"), not internal jargon.
- **Performance on a Pi.** Small bundle, virtualized lists, no heavy polling storms (one coalesced poll loop keyed on `viewPosition`).
- **Local-first / no phone-home.** No external CDNs at runtime, no analytics, no fonts-from-Google — everything ships in the image.

## 5. First deliverables / done-when (this lane's first beat)
- The `web-ui/dashboard` module builds a static SPA bundle via Gradle; CI green (lint/typecheck/test/build + contract-check).
- App shell + design system + auth flow working against a running Core (loopback, bearer token).
- The **device list + entity-state detail** live against the real A-class endpoints, with freshness + the `state-store-replaying` boot state handled.
- The **health view** composing A4+A5.
- The **hero view shell** rendering a causal-chain tree against the **B3 mock** (so the UX is ready when M7.2b + the causal-query API land).
- A short lane return for the hub: what's built, what's mocked, any contract friction (cross-lane items), CI status.

## 6. Escalations to the hub (via Nick — do not decide unilaterally)
Any needed change to the frozen read-API contract; the stack choice if Doc 13 conflicts with the recommendation; anything that wants a Core or spine change; auth-flow questions that touch the token model. Assemble the question + options; the hub adjudicates / routes to Nick.

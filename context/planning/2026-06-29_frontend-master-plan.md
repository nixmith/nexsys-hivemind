<!--
file: context/planning/2026-06-29_frontend-master-plan.md
purpose: The Frontend Master Plan — a research-backed, critically-analyzed plan for ALL remaining frontend work across BOTH surfaces (the observability dashboard + the marketing website), grounded in the verified built state + the Locked contracts + the prior brand/UX research. PLANNING ONLY — the build lane executes against this; this session does not build.
audience: Nick (scope + strategy authority; deep on backend, largely new to frontend — so this is written to be LEGIBLE and decision-supporting for a non-frontend-expert); the PM mission-control hub (reconciles this into the spine + hands it to the frontend build lane); the frontend build lane (executes it).
state-type: planning / strategy (one deep planning arc → this plan). Decision-support, not a build spec.
status: DRAFT FOR NICK 2026-06-29 (frontend strategy + planning lane, nexsys-frontend role in PLANNING register). Routes to the hub for reconciliation; the BLOCKING decisions in §5 are Nick's to rule.
anchors (truth this plan is built ON — pointer-not-copy; cite, never copy a token value or contract shape):
  - BUILT STATE (rank-1): homesynapse-core/web-ui/dashboard/src/ · FRONTEND_DOCTRINE.md · MODULE_CONTEXT.md
  - FROZEN contract (consume, never invent): context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md (v1.1)
  - LOCKED scope/UX: design/13-web-ui-observability-mvp.md · design/16-superior-automation.md · design/09-rest-api.md · governance/Architecture_Invariants_v1.md (INV-SA-03, INV-LF-*)
  - BRAND spine: context/decisions/2026-06-12_website-brand-deliberation_draft-rulings.md (W-1..W-11) · homesynapse-core-docs/website/design-system/* · web-ui/dashboard/src/styles/tokens.css (live tokens)
  - STRATEGY/scope: context/decisions/2026-06-20_V1-launch-scope_decision-record.md (D1-D5) · context/strategy/Six_Battlefields_MVP_Strategy.md · Revenue_Model_and_Licensing_Strategy.md
  - RESEARCH (built on, not redone): context/assessments/2026-06-21_explainability-UX-competitive-research.md · 2026-06-23_explainability-differentiator-moat_research.md · 2026-06-27_smart-home-ecosystem-currency_research-return.md · 2026-06-13_brand-direction-research_PM_Assessment.md · 2026-06-13_naming-research_PM_Assessment.md · context/strategy/asymptote-name-recommendation.md
-->

# Frontend Master Plan — the Dashboard + the Website (research-first, planning only)

**What this is.** One plan for everything left to do on the two surfaces a stranger actually touches: the **observability dashboard** (the product UI — the differentiator made visible) and the **marketing website** (the public face). It is built on the *verified* current state of both, the frozen contract, the Locked design docs, the ruled brand spine, and the prior research — extended with fresh competitive/stack/accessibility research where the prior work had genuine gaps. It is **a plan, not a build**: its value is that the build that follows is methodical and low-risk *because the thinking was done first*.

**How to read this (for Nick).** You designed the backend in depth and are newer to frontend — so every trade-off below is in plain language, with a recommended path *and the reasoning*, and the genuinely-strategic calls are tagged as **yours** in §5 (each with a recommendation, marked BLOCKING or NON-BLOCKING). One reassurance worth stating up front: the dashboard is built in **Preact**, a near-drop-in React variant, so the React intuition you have transfers directly — and the marketing-site recommendation (Astro) is chosen partly *because* it can reuse the exact same Preact components, so we build the design system once and use it on both surfaces.

**The one-sentence thesis everything serves.** *A stranger pairs a sensor and a light, watches an automation fire, clicks "why did this happen?", reads a plain sentence, and is right — and the same person, on the website, understands in ten seconds why this is different from everything else they've tried.* (V1-scope record, the reframe.)

---

## 0. Grounding — the verified state both surfaces actually sit at

Before any plan: what is *true* today, source-verified this session. The single biggest planning trap here (called out in the dispatch and confirmed) is **re-planning greenfield** — treating the dashboard as a scaffold. It is not. The earlier mid-August go/no-go review's "scaffold, hero views unbuilt" line is **outdated** (it globbed only the top of `src/`); the snapshot's 2026-06-28 beat-33 correction supersedes it, and I re-verified it against live source.

**Freshness preflight (8 checks, frontend lane) — 2026-06-29 — Aggregate: STALE-benign (0 CONFLICTED).** The STALE items are *expected* and become the gap analysis below; none is a hard stop, and for a planning session none blocks the plan.

| Check | Result | Note |
|---|---|---|
| 1 — snapshot ↔ lane state | PASS | v12 hub / beat-35 current; dashboard render-half built; I know which B-class are real vs mocked. |
| 2 — contract v1.1 currency | PASS | Contract FROZEN v1.1 (2026-06-21); the typed client mirrors it (`src/lib/api/contract.ts`). One additive field (optional entity `name`, C8) is **not yet folded** into the UI — minor, additive, already flagged. |
| 3 — Doc-13 / stack currency | PASS | Stack unchanged (Preact 10 + Vite + uPlot + CSS Modules + TS); 100 KB gzip budget stands (actual ~22–26 KB); no-WS-poll model holds. |
| 4 — module truth populated | PASS | `MODULE_CONTEXT.md` + `FRONTEND_DOCTRINE.md` populated and consistent with `src/`. |
| 5 — B-class mock vs real | **STALE (expected)** | B3 (`/runs`, `/causal-chain`, `/non-firing`, `/automations`) is now **real in Core** (M7.5a/b DONE) but the UI still mock-backs it pending the **live-integration pass**. B1 (events) + B2 (health) remain correctly mocked (M7.5c deferred). This is the scheduled seam, not a surprise. |
| 6 — brand-source / name-light | **STALE (expected)** | Two 2026-06-27 brand rulings post-date the 2026-06-26 dashboard build and are **not yet folded**: **dark-default** (tokens still default light; no theme toggle; `prefers-color-scheme` unhandled in JS) and **name-light** ("HomeSynapse" hardcoded in ~10 user-facing rendered strings — excluding file-header code comments; no `BRAND.productName` token). The rename (W-11) is still unratified, so name-light stays in force. |
| 7 — dual skill-mirror | PASS | `diff -rq` of source vs read-only mirror is empty. |
| 8 — source round-trip | PASS | Every shape/token/count below re-derived from source; nothing copied-forward. |

**The built dashboard (rank-1 truth, re-read this session).** A real Preact + TypeScript + Vite SPA, ~3,500 LOC of source (excluding deps), bundle estimate ~22–26 KB gzip against a 100 KB hard budget. What exists and is good:

- **The explainability hero is built end-to-end** (mock-backed, contract-conformant, real-transport-ready): `ExplainHubView` (the two co-equal questions as peer front doors), `RunsView` → `RunChainView` → the `CausalChain` component (the device-backward plain sentence + a bounded semantic `<ol>` step chain + two-level disclosure + honest outcome pills + the "never-evicted/rebuilt-from-the-permanent-log" line), and `WhyNotView` (the co-equal "why didn't it?" half with verdict + plain explanation + a next step). This *is* the differentiator, and it already reads the way the research says it should.
- **A full typed API layer** mirroring the frozen v1.1 contract field-for-field (`contract.ts`, `client.ts`, `endpoints.ts`, runtime validators in `shapes.ts`, a `contract.test.ts`, and a build-time `scripts/contract-check.mjs`), with a **mock transport** and a **real transport** (`realTransport.ts` = loopback fetch + bearer auth + ETag) behind **one switch** (`index.ts`, `VITE_USE_MOCKS`, default real-in-prod).
- **The supporting views**: Overview, Devices, Health, Events, Automations. An `AuthGate` (in-memory token paste), a hash router, a single coalesced poll loop on `meta.viewPosition` (`poll.tsx`, no WebSocket), a token-based design system (`tokens.css`), centralized plain-language copy locked by tests (`format.ts` / `format.test.ts`), and the `frontend.yml` CI gate (`npm run verify` = lint · typecheck · test · build · bundle-budget · contract-check).

**The residual is therefore refinement + integration + hardening + filling gaps — not construction.** That single fact reshapes the whole plan: the dashboard is closer to demo-ready than the calendar position implies, and the work is lower-risk than "build the hero" — it is "point the built hero at real data, fold two brand rulings, harden accessibility, fill the supporting views." Concretely the gaps (detailed in §2) are: the **live-integration pass** (Check 5), the **dark-default + theme toggle** fold (Check 6), the **name-light/`productName` token** fold (Check 6), **WCAG 2.2 AA hardening**, **state coverage** (the 503-replaying/offline/empty/error matrix), and **filling the supporting views** to the same bar as the hero.

**The website (rank-2, early but grounded).** A real content + design-system foundation under `homesynapse-core-docs/website/`: a design-system canon (visual, typography, voice-and-tone, design-vision — all DRAFT, reconciliation pending), brand-direction research, and four flagship "dossier" pages at mixed maturity — **one reviewer-grade** (`config-superiority.md`, a genuinely strong piece), a **skeleton landing** (`index.md`), and **three stubs** (`explainability`, `no-cloud-account`, `ledger-gap-dossier`). There is **no site build yet** (the static-site-generator + hosting decision is an open item). The publish gate (W-5) is: all four dossiers reviewer-grade + a wordmark + design-system v0 implemented.

**The schedule frame (from the V1-scope record, unchanged).** Nov 25 launch, fixed date / flexible scope. Mid-August (~Aug 16, ~7 weeks out) is the **go/no-go readiness checkpoint**: is the hero rendering **on real `RunCausalChain` data**? The dashboard is the **parallel long-pole** (no slack); the website ships to Nov 25. The bench (real device data) is the project's critical path and gates the dashboard's *real-data* half — that dependency sits outside this lane but is the gating input to dashboard demo-readiness (§5).

---

## 1. Landscape + research return (evidence, then inference)

Method, matching the backend's discipline: deep research first, **evidence separated from inference**, primary sources where possible, **honest `UNVERIFIED` flags**, volatile facts date-stamped. Much of the competitive landscape was freshly established internally on **2026-06-27** (the ecosystem-currency return, with strict anti-fabrication tagging) — I built on that rather than re-deriving it, and added external research on the genuinely-open questions (marketing-site stack, privacy-respecting hosting/analytics, WCAG 2.2 deltas, the cross-surface design-system path).

### 1.1 Competitive / explainability-UX landscape (built on the 2026-06-27 return)

**The differentiator re-weight (time-sensitive — this binds both surfaces' copy).** The internal currency return found the explainability moat *moved* in one place: Home Assistant merged a framework for **durable, separately-bucketed "not-triggered traces"** to `dev` on 2026-06-22 — but the **emitter was reverted before merge**, so it is plumbing **in no stable release** [VERIFIED — HA core PR #174116]. The implication, which I adopt as a planning constraint:

- **LEAD with the two halves that are durably unoccupied:** (1) **"did the device actually confirm it acted?"** — a durable `Confirmed | Sent, not confirmed | Failed` projection per action, which *no platform ships* (open, closed, or AI) [VERIFIED across the survey; nearest artifact is HA arch discussion #740, proposing a *transient* expected-state, unanswered since 2025-05]; and (2) **never-evicted-ness as a structural property** — explanation as a pure projection of the immutable log (INV-SA-03), where competitors cap/bucket/bolt-on.
- **Keep "why didn't it fire?" a prominent co-equal hero half** (the three-way verdict is still strongly differentiated and the contract + Core deliver it) — but **not the sole lead**, and carry a **watch on the HA 2026.7 line** for the per-trigger emitter graduating to stable.
- **Trust / local-first is the *frame*, not the differentiator** — HA is local too. Lead with the explainability the architecture uniquely enables; let no-cloud-account be the foundation around it.

**Honest-claim corrections that bind ALL copy (dashboard microcopy *and* website).** These are non-negotiable for a brand that sells trust — a false claim forfeits the whole thesis. From the 2026-06-27 return:

- **Home Assistant traces persist to disk** — do **not** write "in-memory / evicted on restart." The accurate, defensible limits are the **cap** (default 5) and **no trace is created when a trigger never matches** [VERIFIED — HA core #70310].
- The **`US10367652B2 / US9230560B2 / US9614690B2` patent family is Nant Holdings IP LLC**, *not* Nest/Google — do not misattribute it [VERIFIED].
- **Command-confirmation as a mechanic is prior art** — claim the *durable, explainable outcome*, never "we invented confirmation."
- Superlatives ("only," "unique," "patented," "the safest") stay **counsel-gated**; use "to our knowledge…". (This is the SafeGate lesson — a prior research session fabricated a citation; the discipline is now enforced.)

**The five failure modes the hero targets** (from the 2026-06-21 competitive research, unchanged): attribution gaps (a silent blank for "what caused this"); ephemeral traces (evidence evicted before you look); unreadable-to-non-experts (log-diving, index paths); two-tools-two-mental-models; and the "didn't fire" blind spot. The built `CausalChain` + `WhyNotView` already answer all five — the plan's job is to keep them answered on *real* data and at the accessibility bar.

### 1.2 Causal-/explainability-UX presentation patterns (evidence)

The settled design contract (FRONTEND_DOCTRINE + the 2026-06-26 presentation-UX research the built component already implements): **device-backward plain language** ("Hallway Light turned on because Hallway Motion detected motion at 9:42 pm"), **two disclosure levels only** (a plain sentence + a bounded linear step chain at a glance; the technical fact one expand away), **bounded-linear over free-graph** (borrow Node-RED's legibility but never its spaghetti), **command outcome not just intent**, **never a silent blank** (`UNKNOWN` is an explicit honest value), and **the stranger/"mom" test as the acceptance bar**. *Inference:* this is durable and trend-proof; the plan adopts it wholesale and adds nothing fashionable to it. The one open refinement (§2) is whether the run list should foreground the *outcome* (confirmed/unconfirmed) more prominently, since that is now the lead differentiator.

### 1.3 Marketing-site stack + hosting (fresh external research — the open "framework decision")

The website has no build system yet, deliberately (`website/README.md` open item 1). Evidence (2026, primary-ish; tool-comparison articles, flagged below):

- **Astro** is the 2026 default for content-heavy sites that want mostly-static HTML with optional interactivity: **zero-JS by default via islands architecture**, runs on **Vite 6** (the dashboard's exact build tool), and **natively supports Preact islands** (`@astrojs/preact`) [VERIFIED — Astro docs]. **Eleventy (11ty)** is the config-light, zero-JS, blog-shaped alternative; **Hugo** wins raw build speed (Go, no Node) but has no component model [tool-comparison sources, 2026 — treat as INFERENCE on relative ranking, not primary benchmarks].
- *Inference, high-confidence:* **Astro is the strongest fit** specifically because it lets the marketing site **reuse the dashboard's Preact components and `tokens.css` design system directly** — so the "two surfaces, one product" coherence goal (the dispatch's explicit requirement) becomes a build-time fact, not an aspiration. A live, interactive embed of the *real hero* on the explainability page becomes feasible (an island), which is the strongest possible proof of the differentiator. The cost is a Node toolchain (same family the team already runs for the dashboard). 11ty is the fallback if we want zero component-sharing and maximum simplicity.

**Hosting + the "don't track" rule.** The brand sells a no-cloud-account, no-tracking product, so *the marketing of it must not track* — I treat this as a design rule, not a preference. Evidence:

- **Cookieless, privacy-first analytics** (Plausible, Fathom, GoatCounter) ship a <5 KB script, drop zero personal data, and — per France's CNIL and other EU DPAs — **need no cookie-consent banner** [VERIFIED — multiple 2026 sources]. **GoatCounter** is a single self-hostable Go binary; **Plausible Community Edition** self-hosts (AGPL — note the Apache-2.0-core licensing posture; CE is a separate *service*, not linked into Core, so no contamination).
- *Inference / recommendation (Nick's call, §5):* the most on-brand choices are **(a) no analytics at all** (purest, and itself a marketing proof point) or **(b) self-hosted cookieless** if a traffic signal is genuinely needed. **Never Google Analytics / no third-party trackers / no runtime CDN** — the same no-phone-home posture the dashboard enforces (INV-LF-01), applied to the site. Static hosting that fits: a static host (e.g., a CDN-static provider) or self-host; the decision is low-stakes given a static build and is sequenced in §3.

### 1.4 Accessibility — WCAG 2.2 AA specifics (fresh external research)

The doctrine commits to WCAG AA. **WCAG 2.2 (the current standard) adds six new Level-AA criteria** beyond 2.1; three bind our exact patterns [VERIFIED — W3C WAI "What's New in WCAG 2.2"]:

- **2.5.8 Target Size (Minimum) — 24×24 CSS px** (with a spacing exception). Binds the dashboard's status pills, table-row affordances, the theme toggle, and the website's nav/footer touch targets.
- **2.4.11 Focus Not Obscured (Minimum)** — a focused element can't be fully hidden by sticky headers/overlays. Binds the dashboard `Drawer` and any sticky site header.
- **3.3.8 Accessible Authentication (Minimum)** — no cognitive test; **allow paste / password managers**. Binds the `AuthGate` token-paste flow directly (it must accept paste — verify it does and never blocks it).

Plus, carried from 2.1 and already partly honored: state by **color + shape + text** (1.4.1), causal chains as semantic **`<ol>`** (already done), polite `role="status"` for poll updates, full keyboard reach, visible focus rings, and `prefers-reduced-motion`. *Inference:* accessibility here is **cheap if designed in now, expensive to retrofit** — and it is brand-load-bearing (a trust brand that fails AA contradicts itself), so it is planned as a first-class workstream, not polish.

### 1.5 Local-first / trust-brand marketing positioning (external + the ruled reference class)

The ruled reference class (W-3): **Stripe × Apple × Oracle-Redwood, counterweighted by Framework**; closest business analog **Ubiquiti/UniFi**. External validation: **Tailscale** positions on *verifiable* trust — "built the hard way so we don't collect unnecessary data," "you don't need to trust us completely" (tailnet lock lets nodes verify keys), transparency over promises [VERIFIED — tailscale.com/security, /why-tailscale, 2026]. *Inference:* this is exactly the **"provable by architecture, not promised by policy"** stance the `no-cloud-account` and `config-superiority` pages already take — the plan adopts it as the site's spine and treats the live, inspectable dashboard (and the open Apache-2.0 core) as the receipts. The anti-models stay anti-models: Home Assistant's visual/community clutter, hype SaaS, mascots, decorative heroes over empty claims.

### 1.6 What is settled vs. stale vs. genuinely open (so we don't redo decided work)

- **Settled (build on, don't re-litigate):** the dashboard stack + the 100 KB budget + no-WS poll (Doc 13 / LTD-18); the frozen v1.1 contract; the 7 hero principles + the bounded-linear disclosure model; the brand north-star + reference class (W-3) + the voice registers; the revenue model + the no-ads/no-tracking absolutes; the Apache-2.0 posture.
- **Stale (needs a fold):** the dashboard's light-default tokens (→ dark-default ruling, 2026-06-27); the hardcoded product name (→ name-light, 2026-06-27); the website design-system docs' **two-brand** framing (NexSys + HomeSynapse) and some palette/typography values that pre-date the rulings and the dashboard's AA-tuned tokens (→ reconcile, §4); the "rendering, not data" copy guardrail on the explainability page (written 2026-06-12 when the causality UI was unbuilt — **now the hero is built**, so the site can honestly show it once it is demo-ready on real data; §3/§4).
- **Genuinely open (researched here; Nick rules in §5):** the static-site stack + hosting + analytics posture; the product-name ratification (blocks the wordmark + public surfaces); the dashboard theme default specifics; the typeface coherence call (the website spec wants Inter; the dashboard forbids web fonts).

---

## 2. Dashboard UI/UX plan — the differentiator made demo-ready

The structure the dispatch asks for: **built-state inventory → gap analysis → a sized, sequenced refinement + integration + accessibility plan** that makes the hero **demo-ready on real data by mid-August**.

### 2.1 Built-state inventory (what exists, by surface)

| Surface / concern | State today | Quality read |
|---|---|---|
| Explainability hero — "why did it fire?" (`RunsView`→`RunChainView`→`CausalChain`) | **Built**, mock-backed, real-transport-ready | Strong. Implements the device-backward sentence + bounded `<ol>` + two-level disclosure + outcome pills + the permanence line. |
| Explainability hero — "why didn't it?" (`WhyNotView`) | **Built**, mock-backed | Strong. Renders the four-verdict `NonFiringExplanation` with a plain sentence + the one gating fact + a next step. |
| Explainability front door (`ExplainHubView`) | **Built** | Two co-equal questions as peer entry points — exactly the research's §4 #1. |
| Typed API layer + mock/real switch + contract tests | **Built** | Mirrors frozen v1.1 field-for-field; drift fails CI. The seam to real data is one switch. |
| Supporting views (Overview, Devices, Health, Events, Automations) | **Built** (A-class live-capable; B1/B2 mocked) | Functional; the bar to lift them to hero-grade polish + states is the gap. |
| Design system (`tokens.css`) | **Built**, light-default | Good token model; **defaults to light** + dark wired-but-off + **no toggle** (the brand-ruling gap). |
| Plain-language copy (`format.ts` + test-lock) | **Built** | Centralized + test-locked — the stranger test, enforced. The right architecture. |
| Auth, routing, poll loop, CI gate | **Built** | In-memory token gate, hash router, one coalesced poll on `viewPosition`, `frontend.yml` green-capable. |

### 2.2 Gap analysis (the residual, prioritized — this is refinement, not construction)

1. **[P0 — mid-Aug gating] The live-integration pass.** B3 (`/runs`, `/causal-chain`, `/non-firing`, `/automations`) is **real in Core now** (M7.5a/b DONE); the UI still mock-backs it. Point `realTransport` at the live backend, render real log-derived data, and handle the real edge cases (real `UNKNOWN` origins, real `UNCONFIRMED` outcomes, real terminal reasons, empty/large result sets). *This is the literal definition of the mid-Aug gate* — "hero on real data." It is also **gated by the bench** for the *truly* real device path (real `CONFIRMED`/`UNCONFIRMED` need real silicon, §5), but the live-backend integration against the running Core can proceed against seeded/replayed logs immediately.
2. **[P0 — brand-defining, escalates] Dark-default + theme toggle.** Fold Nick's 2026-06-27 ruling: dark as the recorded default, `prefers-color-scheme` honored on first load, a persistent **dark/light/system** toggle, AA in both modes. The dark tokens already exist — this is wiring + a toggle component + first-paint handling, not a re-theme. Because it sets the *recorded brand default* (screenshots, the demo), the first presentation **escalates to Nick** (§5).
3. **[P0 — brand-defining, escalates] Name-light / `productName` token.** Replace the ~10 hardcoded "HomeSynapse" user-facing strings with one `BRAND.productName` source of truth; design-validate against `asimtote` as the probable landing; keep the wordmark rename-survivable. The rename is unratified, so the token *stays the switch* — but the hardcoding must go now so the eventual swap is one line. (Touches name/wordmark → escalates.)
4. **[P1] State coverage — the full matrix.** Every view needs: loading, empty, error (RFC-9457 `problem+json`), **`state-store-replaying` (503)** as a calm "starting up / catching up" state (already partially in `feedback.tsx`), and **offline** (local-first: the dashboard must degrade honestly when the backend blips). Audit each view against this matrix; the hero especially must never show a blank or a fake-success.
5. **[P1] WCAG 2.2 AA hardening.** Target size 24×24 on pills/rows/toggle (2.5.8); focus-not-obscured on the `Drawer` (2.4.11); accessible-authentication/allow-paste on `AuthGate` (3.3.8); audit color+shape+text on every status; keyboard reach + focus rings + reduced-motion across the board; the causal `<ol>` semantics for screen readers (already correct — verify with a screen-reader pass).
6. **[P1] Supporting views to hero-grade.** Lift Overview/Devices/Health/Events/Automations to the hero's polish + state coverage; fold the optional entity `name` field (C8) when Core ships it, replacing client-side `labelFor` humanization.
7. **[P2] Responsive + performance confirm.** The dashboard ships in a jlink image to a Pi and is wall-mountable/glanceable — confirm responsive behavior (narrow + wide), keep uPlot lazy-loaded, and keep the bundle under budget as views fill in (it has ~75 KB of headroom; spend it deliberately).

### 2.3 The mid-August demo-readiness path (the must-have, sequenced)

The mid-Aug gate is narrow and honest: **the hero rendering the two lead differentiator reads on real data.** If everything else slips, *this* is what the go/no-go is taken on (the V1-scope contingency: "a minimal honest hero on real data beats a broad unfinished dashboard"). So the dashboard plan front-loads exactly that:

1. **Live-integration pass against running Core** (P0-1) — flip the hero endpoints to real, against seeded/replayed logs; handle real edge cases. *Demo-ready against Core-on-a-dev-box even before the bench.*
2. **Dark-default + name-light folds** (P0-2, P0-3) — because the demo + screenshots are the recorded brand, and these are small, do them alongside the integration pass so the demo *looks* like the brand. Escalate the first hero/dark presentation to Nick.
3. **Hero state coverage + AA pass on the hero path** (subset of P1) — the hero must be honest in every state and accessible, because it is the thing strangers and the go/no-go both judge.
4. **Bench-gated real-device confirmation** (the moat lead) — when bench first-light + M9 produce real `CONFIRMED`/`UNCONFIRMED` on real silicon, the hero's lead claim becomes *measured fact on the screen*. This is the highest-value moment and it depends on the bench (outside this lane) — so the UI is built and waiting for it, not blocking on it.

*Everything else (supporting-view polish, full state matrix, full AA sweep, responsive confirm) is the run-up from mid-Aug to Nov 25 — real work, but not gating the checkpoint.*

### 2.4 Sized, sequenced work units (the build lane executes these in order)

Sizing is relative (S/M/L) given a single-builder lane with unproven velocity (§5 names this risk honestly). The order is dependency- and risk-ordered; each WU ends green-gated per the build discipline.

| # | Work unit | Size | Why here / depends on |
|---|---|---|---|
| FE-1 | Live-integration pass: hero endpoints → real Core; real edge-case handling; per-endpoint mock→real per preflight Check 5 | **M** | P0; the mid-Aug gate. Depends on running Core (available) — not on the bench. |
| FE-2 | Dark-default + `prefers-color-scheme` first-paint + persistent dark/light/system toggle; AA in both modes | **M** | P0; brand-defining → **escalate first presentation**. Tokens exist. |
| FE-3 | Name-light: `BRAND.productName` token; de-hardcode the ~10 strings; rename-survivable wordmark slot; validate vs `asimtote` | **S** | P0; touches name → **escalate**. Makes the eventual rename one line. |
| FE-4 | Hero state coverage (loading/empty/error/503/offline) + hero accessibility pass (WCAG 2.2 AA) + screen-reader verify | **M** | P1; the hero must be honest + accessible before the go/no-go. |
| FE-5 | Supporting views to hero-grade: state matrix + AA + polish (Overview/Devices/Health/Events/Automations) | **L** | P1; the run-up to Nov 25. Fold entity `name` (C8) when Core ships it. |
| FE-6 | Responsive + glanceable confirm; bundle-budget re-check; uPlot lazy-load confirm | **S** | P2; before launch. |
| FE-7 | Bench-gated: real-device `CONFIRMED`/`UNCONFIRMED` on the hero once M9 + bench land | **S (UI)** | The moat lead on real silicon; UI ready, waits on the bench (§5). |

**Cross-lane asks this surfaces for the hub** (the UI consumes the contract; it does not invent it): (a) confirm B3 is live + stable for FE-1; (b) the optional entity `name` (C8) landing sequence for FE-5; (c) B1 events + B2 health (M7.5c) landing sequence — the UI mocks them until then, no blocker. None is a contract *change*; all are sequencing confirmations.

---

## 3. Website plan — the public face (positioning → IA → brand system → build → roadmap)

### 3.1 Positioning — what a stranger must grasp in 10 seconds

The site optimizes for the **launch audience (W-1): prosumers & Home-Assistant refugees** — people who already run HA/Hubitat or are comfortable with a Pi, who **read receipts and distrust marketing**. For them, *evidence beats adjectives*. The positioning, aligned to the Six Battlefields and the differentiator re-weight (§1.1):

- **The 10-second grasp:** *"A smart home that can explain itself — and prove it. It tells you why something happened, why something didn't, and whether the device actually did it — and it keeps that answer forever, on hardware you own, with no cloud account."*
- **Lead with the durable differentiators** (re-weighted): the honest **command outcome** (`Confirmed | Sent, not confirmed | Failed` — no one ships this) and **never-evicted explainability** (a projection of a permanent log). Keep "why didn't it fire?" co-equal. **Local-first / no-cloud-account is the frame** the whole thing sits in, not the headline differentiator.
- **Honor the segment messaging rule (D-4):** privacy-first framing leads **only** for prosumer/EU contexts; the mainstream-facing landing leads **reliability + works-together + the explainability proof**, with privacy present but not the headline. (The current `index.md` already does this correctly.)
- **Honor the register/legal fences:** the Matter trademark fence ("controls Matter devices locally," never the bare mark), never-lead-with-encryption, the anti-requirement absences (no engine-retry / no templating DSL / no destructive migration claimed as *features*), the install-story embargo (W-4 — no "plug-and-play" claim until it exists), and **provenance discipline** (every factual claim mapped to source; no fabricated metrics, ever). These already bind the drafted pages; they bind every new page.

**A positioning upgrade unlocked since the pages were drafted (NON-BLOCKING, §5).** The explainability page's 2026-06-12 "rendering, not data" guardrail said: claim the event-sourced *record*, never an unshipped friendly-causality *UI*. **That UI now exists** (the built hero). So once the hero is demo-ready on real data (the mid-Aug gate), the site can **honestly show the actual product** — screenshots, and ideally a live interactive embed of the real hero (feasible if we build on Astro, §3.4). This is the strongest possible receipt for a receipts-driven audience, and it closes the gap between what we claim and what we show. The honest-claim discipline still binds: show it only when it is real on real data.

### 3.2 Information architecture + the page set

The design-vision caps the homepage at **6 sections** and maps page-intent to expression level (homepage/About = ambient allowed; docs/downloads/account = calm-neutral). The launch IA, dependency- and conversion-ordered:

**Tier 1 — the launch-gating set (the W-5 publish gate: all flagship dossiers reviewer-grade):**

1. **Home** (`index.md`, skeleton → finished) — the 6-section flow: what it is → why it exists (trust/local-first stance) → what's different (the 3–4 pillars, led by explainability + honest-outcome) → how it feels (one calm real screenshot/embed of the hero) → who it's for → go deeper (docs/downloads/GitHub). Primary CTA per W-2: **follow-the-build** (email + GitHub) until the product ships.
2. **Ask your home why** (`explainability.md`, stub → finished, flagship) — *the* differentiator dossier: the porch-light "what turned on my light?" story, "rendering not data" → now *shown* (§3.1 upgrade), the eviction contrast (with the **corrected** HA limits — cap 5 + no-trace-on-never-match, never "in-memory"), the LLM-paste property.
3. **No cloud account. Really.** (`no-cloud-account.md`, stub → finished, flagship) — provable-by-architecture: the account-dependency matrix, the Insteon-shutdown narrative (figure attributed as a CEO estimate), "what happens to your home if we disappear: nothing." Prosumer/EU framing permitted here.
4. **The ledger gap** (`ledger-gap-dossier.md`, stub → finished, flagship) — the confirmation-of-intent dossier: fire-and-forget vs a durable ledger; "sent" is not "on." (Tense-match to shipped truth at publish — the ledger ships at M7.3, which is DONE.)
5. **One configuration. One truth.** (`config-superiority.md`, **reviewer-grade already**) — the split-brain/INV-CE-01 dossier. Keep as the quality bar for the others.

**Tier 2 — supporting trust/conversion surfaces (some at launch, some fast-follow):**

6. **About / Vision** — the maturation-arc story (free/local → cloud/paid without rebrand); a brand-moment page (ambient allowed). 7. **Docs hub** — pure reading focus, backgrounds off; the Senior-Engineer voice (Register A). 8. **Downloads** — clean, direct, explicit about platform + integrity (gated by the install story, W-4). 9. **Footer/legal** — "a NexSys product" (W-7), license (Apache-2.0), privacy stance (which the site itself demonstrates by not tracking).

**Post-V1 backlog (do NOT build now — anti-creep):** account/cloud portal (Connect/Cloud Pro surfaces), the Data-Act/CRA regulation page, the Apple-contrast and Matter-friction dossiers, community surfaces. The maturation arc reserves these; the design system must not *encode* "hobbyist" so they slot in later without a rebrand (W-3a).

### 3.3 Brand identity — reconciled into one ruled system

The brand is **Nick's call**; this reconciles the ruled spine (W-1..W-11) + the design-system drafts into one coherent system and flags the conflicts for the hub. The durable spine: **infrastructure-grade software, consumer-grade calm**; the W-3 reference class (Stripe × Apple × Oracle-Redwood ⟂ Framework; UniFi the analog); **one accent (the blue) with the interaction monopoly**; **no pure black/white**; **warm palette is illustration-only, never UI** (W-9); **brand moments rare** (homepage hero + About/Vision only, W-10); **the Calm Canvas** layout model (expression *around* content, never inside it; "if you notice the background, it's too strong").

- **Wordmark (W-6):** wordmark-only at launch, monochrome-survivable, **rename-ready** — design it so it re-renders from the `productName` token and survives the swap to `asimtote`. Do **not** over-invest in a "HomeSynapse" lockup. Produce the wordmark spec (weight, tracking, clearspace, light/dark) during design-system v0 — but the public wordmark is **BLOCKED on the name ratification** (§5).
- **Voice — one identity, three registers** (already specified, keep): Register A Senior-Engineer (docs), Register B Calm-Neighbor (homepage/onboarding/blog — confident, unhurried, never hype), Register C Direct-Neutral (UI microcopy — no self-reference, never blames the user). The site uses A + B; the dashboard uses C. This is already coherent — keep it.
- **Conflicts to reconcile (flag to hub, §4):** the design-system docs still describe **two brands** (NexSys + HomeSynapse) and a homepage-vs-dashboard palette that pre-dates both the rulings and the dashboard's AA-tuned tokens. These are reconciled in §4.

### 3.4 Build approach + hosting (recommendation; Nick rules in §5)

- **Static-site generator — recommend Astro.** Reason: it ships zero-JS by default, runs on Vite 6 (the dashboard's build tool), and **natively renders Preact islands** — so the marketing site reuses the dashboard's **exact** Preact components and `tokens.css`, making "one product, two surfaces" a build-time fact and enabling a **live embed of the real hero** on the explainability page (the strongest receipt for this audience). Fallback: **11ty** if we want maximum simplicity and zero component-sharing. (Avoid a heavy React meta-framework — unjustified for a content site and off-brand on performance.)
- **Hosting + analytics — embody the no-tracking brand.** Static hosting (a static CDN host or self-host); **no Google Analytics, no third-party trackers, no runtime CDN/Google Fonts** (the dashboard's INV-LF-01 posture applied to the site — self-host Inter if used). Analytics: **none, or self-hosted cookieless** (GoatCounter/Plausible CE) — both need no consent banner. *The marketing of a no-tracking product must not track* — this is a design rule, and itself a proof point worth a line on the privacy page.
- **Performance/SEO budget:** treat the site like the dashboard — a tight budget, semantic HTML, real content over decoration. The audience and the brand both reward a site that is provably fast and quiet.

### 3.5 Website roadmap to Nov 25

The website is **not** the long pole (the dashboard is) and ships to Nov 25, so it sequences *after* the dashboard's mid-Aug gating work claims the scarce builder-time — but the content (copy) can advance in parallel since it is writing, not engineering. Dependency-ordered:

1. **Now → mid-Aug (parallel, low-engineering):** finish the **three stub dossiers** to `config-superiority` reviewer-grade (copy work; honor every fence + the corrected competitive claims). Decide the **stack/hosting/analytics** (§5) — it is cheap and unblocks the build. Draft the **design-system v0** spec reconciliation (§4).
2. **Mid-Aug → Oct:** stand up the **Astro build + design-system v0** (tokens + wordmark + the Calm Canvas shell), implement the Tier-1 pages, wire the follow-the-build CTA. Fold the **live hero embed/screenshots** once the dashboard is demo-ready on real data.
3. **Oct → Nov 25:** About/Vision + Docs hub + Downloads (gated by the install story), accessibility (WCAG 2.2 AA) + performance pass, the **publish-gate (W-5) review** (4 dossiers reviewer-grade + wordmark + design-system v0), and the **name ratification** must land before any public wordmark/domain goes live. Publish per W-2 (build hidden → publish gated → grow the following).

**The name dependency is the website's critical internal risk:** the public wordmark, domain, email, and final page headers are **BLOCKED on the W-11 rename ratification** (§5). Everything else — copy, IA, design-system, the build — proceeds name-light and swaps on one token at ratification.

---

## 4. Design-system + brand coherence — one system across both surfaces

The dispatch's explicit requirement: a single design language, brand, and voice so the dashboard and the website read as **one product**. Today they are *two parallel expressions* of the same intent that have not been reconciled — the dashboard implemented an AA-tuned, light-default token set in code (2026-06-26); the website design-system docs describe a brand-true, **two-brand**, partly-different palette/typeface (Feb 2026, DRAFT). Coherence is achievable and mostly mechanical, but it needs decisions. The recommendation: **the dashboard's live `tokens.css` becomes the shared source of truth**, reconciled with the brand-true values and consumed by both surfaces.

### 4.1 The conflicts (verified this session) and how to resolve each

| Concern | Dashboard (live `tokens.css`) | Website spec (`visual-design-reference.md`) | Resolution (recommended) |
|---|---|---|---|
| **Accent blue** | A deeper blue chosen for **WCAG AA text contrast on white** | A lighter "HomeSynapse Blue" (brand-true, but fails AA for text on white) | **One accent token, two roles:** keep the AA-passing blue for *interactive/text* use (links, focus, actions) on both surfaces; allow the lighter brand blue only for *large display/illustration* moments where contrast rules differ. Reconcile to a single named pair; cite `tokens.css` as truth. |
| **Neutrals** | A cool architectural ramp (its darkest ≈ the website's dark anchor; one light step is *identical* to the website's light background) | Named anchors (dark/secondary/light) | **Already ~90% aligned** — unify on one ramp (the dashboard's, extended with the website's named anchors). Low effort. |
| **Semantic colors** | AA-tuned, slightly darker (state-bearing) | Muted/desaturated (marketing-calm) | **Prefer the dashboard's AA-tuned semantic tokens + shape + label** (the brand reference's ruling; resolves the Doc 13 §3.8 "traffic-light is brighter than brand" tension). The site's marketing surfaces can render them slightly softer in *illustration* only. |
| **Typeface** | **System font stack** (no web fonts — local-first INV-LF-01; 100 KB budget) | **Inter** (variable) + JetBrains Mono NL + optional Source Serif 4 | **Coherent by *discipline*, not literal face** (recommended, §5): website uses self-hosted Inter; dashboard keeps the system stack; both share the **type scale, weights, and spacing**. (Bundling Inter into the dashboard would blow the budget and/or need heavy subsetting; not worth it for V1. Brand is carried by type discipline + the token system, not the exact glyphs.) |
| **Default theme** | Light-default (pre-ruling) | Light-leaning with dark mode | **Dashboard = dark-default** (the 2026-06-27 ruling — observability-native; the recorded brand default for screenshots/demo); **website = lighter, open default** with first-class dark mode. Different *defaults*, **same tokens** — coherent, and each fits its surface. |
| **Brand count** | (single product surface) | **Two brands** (NexSys + HomeSynapse) | **Collapse toward one brand** per the W-11 rename + the PM recommendation (company = product, the Googol model). Until Nick rules the structure, write name-light and keep the parent/product split *structurally possible* but not baked into tokens. |

### 4.2 The shared system — what to consolidate, and where it lives

- **Tokens (the foundation):** one CSS-custom-property token set (color/space/type/radius/motion), dark-ready, **owned in the dashboard's `tokens.css`** and consumed by the website build. If we build the site on **Astro + Preact** (§3.4), the site imports the *same* file — one source of truth, zero drift. Pointer-not-copy: the authoritative values live in `tokens.css`; the website design-system docs should *cite* it, not restate hexes (the current restated hexes are how the two drifted).
- **Components (the kit):** the dashboard's component kit (status pill, card/page, data table, drawer, the causal-chain) is the reusable core. On Astro+Preact, the marketing site can embed the **real** `CausalChain` as a live island — the ultimate coherence proof. Components that are website-only (hero illustration fields, marketing nav) extend the same tokens.
- **Voice (already coherent):** one identity, three registers (A/B/C, §3.3) — docs use A, marketing uses B, all UI microcopy uses C. The dashboard's `format.ts` is the test-locked home of Register-C explanation copy; the website carries A/B copy in content. Keep this; it is already right.
- **Accessibility (one bar):** WCAG 2.2 AA on both surfaces — same contrast discipline, same color+shape+text rule, same focus/keyboard/reduced-motion rules, the same `<ol>` causal pattern. One checklist, both surfaces.

### 4.3 The coherence payoff (why this is worth doing now)

Doing the reconciliation *before* the website build means: (1) the site and product are provably one thing (same tokens, same components, same voice); (2) the marketing site can show the *real* hero, not a mockup — the strongest receipt for a receipts-driven audience; (3) the rename swaps once, on one token, across both surfaces; (4) the design system matures from "indie infra" to "institution" by **discipline** (type, spacing, governance), never encoding "hobbyist" — so it survives the W-3a maturation arc into cloud/paid/B2B without a rebrand. The cost is one reconciliation pass (the §4.1 table) + choosing Astro+Preact (§5) — both small relative to the payoff.

**Flag to the hub (not a unilateral edit):** the website design-system docs (`visual-design-reference.md`, `typography-reference.md`, `website-design-vision.md`) are DRAFT and currently restate values that have drifted from the live tokens and still describe two brands. Recommend the hub schedule a **design-system reconciliation** that (a) makes `tokens.css` the cited source of truth, (b) collapses the two-brand framing per W-11, and (c) folds the dark-default + AA-semantic rulings. This plan proposes it; it does not edit those Locked-adjacent docs.

---

## 5. Execution roadmap + the decisions for Nick

### 5.1 The integrated roadmap (both surfaces, against the backward schedule)

The two surfaces share one scarce resource — builder time — so they are sequenced, not run flat-out in parallel. The dashboard is the long pole and owns the mid-Aug gate; the website's *engineering* waits behind it, but the website's *copy* (writing, not engineering) advances in parallel.

```
 NOW ─────────────► mid-AUG (~Aug 16, go/no-go) ─────────────► OCT 11 ──────► NOV 25 (launch)
 DASHBOARD (long pole, no slack):
   FE-1 live-integration ─► FE-2 dark-default ─► FE-3 name-light ─► FE-4 hero states+AA
                                          │ (mid-Aug must-have: hero on REAL data, the 2 lead reads)
                                          └─► FE-7 real-device confirm (waits on bench/M9)
                              FE-5 supporting views ─► FE-6 responsive/perf ──────────► launch-ready
 WEBSITE (ships to Nov 25; copy parallel, build after):
   copy: finish 3 stub dossiers ──────────► design-system v0 + Astro build ─► About/Docs/Downloads
   decisions: stack/hosting/analytics (now) ········· name ratification (before public wordmark) ···► W-5 publish gate
```

**The honest critical path** is not in this lane: it is **the bench** (real device data), which gates the dashboard's *real-data* half and all of hardware validation. The dashboard hero can be demo-ready against running Core (seeded/replayed logs) *before* the bench; the **real-silicon `CONFIRMED`/`UNCONFIRMED`** — the moat's lead claim shown as measured fact — lands when the bench + M9 do. The frontend lane's job is to be **built and waiting**, never the thing the bench is waiting on.

### 5.2 Staffing / velocity reality (the honest constraint)

- **The dashboard residual is refinement, not construction** — which is the single biggest de-risk: the hard, uncertain part (building the hero) is *done and good*. The remaining WUs (§2.4) are bounded and mostly mechanical.
- **The lane's velocity is unproven** (the go/no-go review's standing caveat). The mitigation is the §2.3 ordering: the mid-Aug gate rests only on FE-1 + a hero-path AA/state pass + the brand folds — a small, high-certainty set — so even pessimistic velocity reaches a legitimate conditional-go.
- **Nick is the integration point, not agent capacity** — the binding throughput limit is Nick's review/ratify/decide time across five lanes. This plan minimizes that load: it batches the decisions (§5.4) into one pass, and routes everything else through the hub's existing reconciliation.

### 5.3 Risks + contingencies

| Risk | Likelihood | Contingency |
|---|---|---|
| Bench first-light slips → no real device data by mid-Aug | Medium (it's the project critical path) | Demo the hero on **seeded/replayed real logs** against running Core (FE-1 enables this without the bench); take the go/no-go on that + the moat shown on replayed data; real-silicon confirm follows. |
| Frontend velocity slower than hoped | Medium | Scope the mid-Aug hero to the **two lead differentiator reads only** ("did it confirm?" + "why didn't it?") on real endpoints; defer supporting-view polish + full state matrix to the Oct run-up. (The V1-scope contingency, adopted.) |
| Name ratification slips | Medium | Everything proceeds **name-light**; only the public wordmark/domain/email wait. The site can be build-complete and hold publish on the name. |
| Website eats dashboard time | Low–Medium | Hard rule: **dashboard mid-Aug work has priority on builder time**; website *copy* advances in parallel (different skill), website *build* starts after the mid-Aug gate. |
| Scope creep (the project's proven failure mode) | Medium | The anti-creep list (§5.5) is explicit; the post-V1 backlog is named and fenced; the build lane executes §2.4 / §3.5 in order and escalates additions. |

### 5.4 The decisions for Nick (each with a recommendation)

Format per the lane's escalation discipline: the decision in one line · options/trade-offs · recommendation · blocking-or-not. **Batched, not a drip.**

**D-FE-1 — Dark-default + the first hero/dark brand presentation.** *Approve the dashboard going dark-default (observability-native, the recorded brand default) with `prefers-color-scheme` honored on first load and a persistent dark/light/system toggle, AA in both modes?* Options: (a) dark-default + toggle [the 2026-06-27 ruling]; (b) light-default + toggle; (c) dark-only. **Recommendation: (a)** — it is your standing ruling, it suits the wall-mounted/evening glance, and the tokens already support it; the build lane just needs your sign-off on the *first hero-on-dark presentation* because it sets the brand default for every screenshot. **BLOCKING for FE-2** (brand-defining; the build shouldn't invest until you've seen the first hero presentation).

**D-FE-2 — Static-site stack + hosting + analytics.** *Build the marketing site on **Astro (with Preact islands)**, on static hosting, with **no third-party analytics** (or self-hosted cookieless)?* Options: (a) Astro+Preact — reuses the dashboard's components/tokens, enables a live hero embed [recommended]; (b) 11ty — simplest, no component-sharing; (c) a React meta-framework — overkill, off-brand on performance. Analytics: none / self-hosted cookieless / (never GA). **Recommendation: (a) + no-or-self-hosted-cookieless analytics + no runtime CDN/Google Fonts** — it makes "one product, two surfaces" a build-time fact, lets the site show the *real* hero, and makes the no-tracking brand literally true. **BLOCKING for the website build** (can't start the build without it; not blocking copy).

**D-FE-3 — Product-name ratification (W-11).** *Ratify `asimtote` (post-clearance) as the product/company name, or explicitly hold?* Context: leading candidate is `asimtote` (fanciful, ownable; **active PyPI collision** with a Cambridge config tool + clearance pending — surface scan, **not** legal clearance [UNVERIFIED as cleared]). **Recommendation: keep building name-light now** (the plan does), and **ratify only after counsel clears** — do not block the build on it. **BLOCKING only for public surfaces** (wordmark, domain, email, final page headers); NON-BLOCKING for everything else. This is yours + counsel's call.

**D-FE-4 — Brand structure: one brand or product/parent split?** *Collapse to a single brand (company = product, the Googol model), or keep a HomeSynapse-product / NexSys-parent split?* **Recommendation: collapse to one brand** (the PM recommendation; W-7 already half-collapsed it; simpler to build and market) — but this can ride along with D-FE-3 since name-light covers the interim. **NON-BLOCKING** (defaulted to name-light; rule when you rule the name).

**D-FE-5 — Typeface coherence.** *Accept "coherent by discipline" — website uses Inter (self-hosted), dashboard keeps its system-font stack, both share the type scale/weights/spacing — rather than forcing one literal typeface?* Trade-off: bundling Inter into the dashboard would blow the 100 KB budget and/or need heavy subsetting and breaks no-web-fonts; the brand is carried by type discipline, not glyphs. **Recommendation: accept** (the default in §4.1). **NON-BLOCKING.**

**D-FE-6 — Show the real hero on the website.** *Once the hero is demo-ready on real data, update the explainability page from "claim the record, not the UI" to actually showing the built hero (screenshots + ideally a live embed)?* **Recommendation: yes, when it's real on real data** — it is the strongest receipt for a receipts-driven audience, and it closes the claim-vs-show gap honestly. **NON-BLOCKING** (sequenced into §3.5; honest-claim discipline still gates the timing).

### 5.5 What this plan deliberately does NOT include (anti-creep — the discipline the backend used)

Out of V1, reserved for the post-V1 backlog, *not* to be pulled forward by the build lane without escalation: a WebSocket/real-time runtime (no-WS is firm); account/cloud portal surfaces (Connect/Cloud Pro); the deep "why did the trigger not match" per-evaluation recording (the contract's scope guard — V1 answers from existing run records + absence + config); a query language / cross-run analytics / audit projection (full M12); component-authoring UX; the Data-Act/CRA + Apple-contrast + Matter-friction dossiers; mainstream "plug-and-play" copy (embargoed until the install story exists, W-4); Matter logos/certification claims (the trademark fence). The thin slice that ships is: **the explainability hero on real data + the two supporting surfaces + a focused dashboard + the five flagship dossier pages + a coherent design system across both** — nothing more, by design.

---

*Planning complete. This plan builds **on** the verified built state, consumes (never invents) the frozen v1.1 contract, honors the Locked docs + the brand spine (W-1..W-11) + the local-first/100 KB/no-WS constraints, and applies the honest-claim discipline with the 2026-06-27 corrections. It does not edit Core, the Locked design/governance docs, or the hivemind spine. It routes to the hub for reconciliation and hand-off to the frontend build lane (upgrading that lane's brief from "build to the contract" to "build to this researched, critically-analyzed plan"). The six decisions in §5.4 are Nick's; the three BLOCKING ones gate their respective work, the three NON-BLOCKING ones have safe defaults already in the plan.*

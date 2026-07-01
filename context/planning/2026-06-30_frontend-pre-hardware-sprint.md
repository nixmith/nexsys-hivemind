<!--
file: context/planning/2026-06-30_frontend-pre-hardware-sprint.md
purpose: The frontend execution strategy for the pre-hardware window — everything to accomplish on the dashboard between now and when the Sonoff hardware arrives, so that the moment Core is up on real device data the mid-Aug "hero on real data" gate is a fast, low-risk SWAP, not a build. Builds on the master plan + amendment-1; this is the windowed sprint plan the build lane executes.
audience: the frontend build lane (executes this); the PM hub (reconciles into the spine + hand-off); Nick (the decisions at the end; the strategy authority).
state-type: planning (windowed sprint plan / amendment-2 to the 2026-06-29 master plan).
status: DRAFT FOR NICK 2026-06-30 (frontend planning register). Builds on _amendment-1 (Nick's 4 rulings, all folded + shipped as FE-0/FE-2/FE-3 + D-FE-10). The mission: reach world-class-on-mocks + swap-ready before hardware.
anchors: context/planning/2026-06-29_frontend-master-plan.md (+ _amendment-1) · context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md (FROZEN v1.1) · web-ui/dashboard/ (built state, core 7b9680c + the D-FE-10 delta) · FRONTEND_DOCTRINE.md
-->

# Frontend Pre-Hardware Sprint — make the dashboard world-class *on mocks*, and swap-ready

## The frame (the one idea that organizes the window)

The Sonoff hardware arrives soon → **bench first-light → Core running on real device data**. Until then, exactly two work units are **blocked** (they need a live Core / real hardware): **FE-1** (live-integration) and **FE-7** (real-device `CONFIRMED`/`UNCONFIRMED` on real silicon). **Everything else is pure-frontend and fully doable now, against mocks.**

So the mission of this window is precise: **get the entire dashboard to world-class quality against mocks, and pre-harden the data layer, so that the day Core comes up, "hero on real data" — the mid-August go/no-go gate — is a fast, low-risk transport swap plus a smoke test. Hours, not a build.** This is the "built-and-waiting" principle from the master plan, taken to its conclusion.

**The success test for the window:** the day Core is up, we flip one switch (`VITE_USE_MOCKS=false`), point at loopback, smoke six endpoints, fix nothing structural, and demo the hero on real data. If that day is smooth, this window did its job.

## Status (verified host-side this session — trust the source, not the report)

- **FE-0 / FE-2 / FE-3 committed** (core `7b9680c`): the DTCG token source + zero-dep generator + drift-guard (101/101 equivalence proven); dark-default + `prefers-color-scheme` + system/light/dark toggle; name-light `BRAND.productName` + keyed i18n. Code quality is high (inline-SVG icons, solid theme module, clean i18n). The sign-off screenshot's tofu/CJK glyphs were **mockup-only** — not in source (swept: zero CJK).
- **D-FE-10 self-host Inter staged** (uncommitted 7-file delta): 25 KB subset woff2 (git-tracked), `@font-face` + `font-display:swap`, `--hs-font-sans` leads with Inter in both the committed `tokens.css` and the DTCG source (hand-sync matches → drift-guard will pass), local-first held. Commit it, then Step 0.
- **Outstanding debt (Step 0):** the full `frontend.yml` gate has never run green on a clean checkout (FE-0/2/3 committed deferred), and axe-core isn't wired. Close this before anything stacks on it.

---

## Step 0 — reconcile the gate (gating; do first, before any new WU)

The verification debt is real and cheap to close on a real machine (not the truncating sandbox):

1. **Commit the D-FE-10 font delta** (message in the chat hand-off).
2. **`cd web-ui/dashboard && npm ci && npm run verify` on a clean checkout → GREEN.** This now covers everything shipped: the regenerated `tokens.css` (`tokens:check` drift-guard) + the font asset + all of FE-0/2/3 (lint · typecheck · test · build · bundle · contract). Fix anything it flags, fix-forward. **Nothing in Tier 1+ starts until this is green** — don't stack world-class work on an unverified base.
3. **Wire axe-core into `frontend.yml`** (the deferred a11y gate; needs the clean-checkout `npm install` the sandbox couldn't do). From here on, WCAG AA is machine-checked on every change — the right foundation for an AA-committed brand.

Output of Step 0: a green gate of record on the full committed surface + an automated a11y gate. Now the window's real work rests on solid ground.

---

## Tier 1 — the mid-Aug gate + swap-readiness (MUST, before hardware)

These three are the heart of the window: they make the hero world-class on mocks *and* make live-integration a swap. Do them first, in the order below (T1.2 and T1.1 interleave).

### T1.1 — FE-4: hero + core-view hardening

The WU detail is in amendment-1 (state matrix · WCAG 2.2 AA in *both* themes · mobile-first · screen-reader). The sprint addition: **build and test it against the scenario engine (T1.2)**, so every state is exercised on realistic, contract-shaped data rather than a single happy-path fixture. Non-negotiables restated: honest in every state (loading skeleton, empty-as-teaching, RFC-9457 error, `state-store-replaying` calm-503, offline degraded) — never a fake success, never a silent blank (INV-SA-03); AA re-verified in dark (now the default) *and* light; the WCAG 2.2 trio (target-size ≥24px, focus-not-obscured on the Drawer, accessible-auth/allow-paste on AuthGate); a real screen-reader pass on the causal `<ol>`, the live regions, and the toggle.

### T1.2 — The mock scenario engine (NEW — the keystone of this window)

Today the mock transport serves essentially a happy path. Turn it into a **scenario system that can exercise every condition the frozen contract allows, on demand:**

- **Every value the hero can show:** all action outcomes (`CONFIRMED` / `DISPATCHED` / `UNCONFIRMED` / `FAILED` / `SKIPPED`), all origins (incl. the honest `UNKNOWN`), all non-firing verdicts (`CONDITION_NOT_MET` / `NEVER_TRIGGERED` / `ACTED_BUT_UNCONFIRMED` / `DISABLED`), all run statuses, and **cascades** (parent-run chains).
- **Every transport condition:** `state-store-replaying` (503) on boot, offline/unreachable, injected latency, 401/403 auth, ETag/304, empty results, and **large lists** (hundreds of runs/events — the input that forces virtualization in T2.3).
- **A dev/demo control** to switch scenarios (a URL param and/or a hidden dev panel) — so the happy-path "motion→light→confirmed" demo, the "sent, not confirmed" honesty path, and each "why didn't it fire?" verdict are all one click away.

**Why this is the keystone, not a nicety:** (1) it makes the *mock* demo compelling and complete right now; (2) it lets FE-4 build and verify **every** state against realistic, contract-shaped data; (3) it **de-risks live-integration to near-zero** — by the time Core is real, the UI has already faced every shape the (contract-locked) backend will emit, so the swap has almost nothing left to surprise it; (4) the scenarios become the **static seeded fixtures** the website's live-hero embed needs later (master plan §3/§4). One artifact pays off four ways. Keep every scenario shaped by the same types the real transport uses (the contract-check already enforces this).

### T1.3 — FE-1 readiness prep (so live-integration is a swap, executable in hours)

FE-1 can't *run* without Core, but almost all of its risk can be retired now:

- **Audit `realTransport` against the full cross-cutting contract (§0), end to end:** bearer auth (401 → re-prompt, 403 → reject, in-memory only), `state-store-replaying` (503) → calm state + backoff, ETag / `If-None-Match` / 304, RFC-9457 `problem+json` parsing, cursor pagination echo (never construct one), and the poll model on `meta.viewPosition`. Much of this exists — verify each branch against **scenario-injected** conditions (T1.2), so the real backend hits no untested path.
- **Write the one-sitting go-live checklist** (into the module docs) so the swap is mechanical when Core is up: flip `VITE_USE_MOCKS=false` → point at the loopback origin → smoke each endpoint (A-class live + the now-real B3 `/runs`, `/causal-chain`, `/non-firing`, `/automations`) → let the runtime validators + `contract-check` confirm the shapes → handle any real-data surprises (which should be near-zero if T1.2 was thorough).

**Result:** when hardware lands → bench first-light → Core up, FE-1 is **hours** — because everything it depends on is already built, hardened, and tested.

---

## Tier 2 — the world-class fill (high value; as the window allows)

### T2.1 — FE-PWA: installable, offline app-shell
Manifest + a service worker that caches the app-shell; installable; works offline and **degrades honestly** (the local-first proof point made tangible — an installable no-cloud app). No phone-home (INV-LF-01). Cheap, on-brand, app-like.

### T2.2 — FE-5: supporting views to hero-grade
Overview / Devices / Health / Events / Automations lifted to the hero's polish + the full state matrix + mobile-first + AA, all against the scenario engine. Fold the optional entity `name` (C8) — mock it now, swap to the real field when Core ships it.

### T2.3 — FE-6: responsive/perf + render-at-scale
**List virtualization** for large run/event tables (the Home-Assistant failure mode — it crawls at hundreds of entities; we won't), a **render/interaction-latency budget** (not just the bundle budget), poll-cost sanity at scale, uPlot lazy-load confirm, and a bundle/asset re-check now that the ~25 KB font ships.

### T2.4 — The polish layer (what separates good from world-class)
- **Demo choreography:** the stranger flow (pair sensor+light → automation fires → click "why did this happen?" → understand) made frictionless — deep-linkable runs, a smooth trigger→chain reveal, the cascade "see what triggered this run" link, a fast return path. This *is* the demo the whole project sequences toward; it should feel effortless.
- **First-run / onboarding:** token-paste → a meaningful Overview → natural discovery of "Ask why." **Empty states that teach** ("Once an automation runs, you'll see exactly why here — kept forever") rather than blank panels.
- **Micro-interactions / motion:** subtle, reduced-motion-aware, always answering "what changed?" not "look at me" (the design-vision motion rule).
- **Keyboard-first:** shortcuts + disciplined focus management — prosumers (the launch audience) reward it.
- **Copy craft pass:** every user-facing string through the mom-test — plain, honest, calm (Register C) — centralized in `format.ts` + `i18n.ts`; honest-claim discipline on anything that verges on a claim.

---

## Tier 3 — governance (woven in; keeps it world-class as it grows)

- **axe-core CI** — landed in Step 0.
- **A living component catalog / styleguide route** (a lightweight in-repo `/styleguide` or Storybook-class artifact): the single visual reference for the build lane now and the future B2B/native lane — the maintainability backbone.
- **Visual-regression** (screenshot diffs in CI): catches unintended visual drift as the surface grows — brand consistency, enforced.
- **A frontend stability / versioning note** (the anti-HA-breakage discipline: "we don't break your dashboard across updates").
- **G7 — local, user-exportable error diagnostic:** the on-brand answer to "how do we know when the dashboard breaks in someone's home?" for a no-telemetry product — a local log the user can *choose* to export, never silent telemetry. Design it here.

---

## Sequencing (the window, dependency- and value-ordered)

1. **Step 0 — gate green + axe-core** (gating).
2. **T1.2 scenario engine + T1.1 FE-4** (interleaved — the engine feeds the hardening).
3. **T1.3 FE-1 readiness** (so the swap is hours the moment Core is up).
4. **T2** as the window allows — **PWA + perf/virtualization + the polish layer first** (they touch the hero/demo), then supporting-view breadth (FE-5).
5. **T3** woven throughout — axe early, the catalog + visual-regression mid, the copy/polish continuous.

**Priority principle:** hero-path + swap-readiness before breadth. The hero on real data is the gate and the demo; a bulletproof, beautiful hero + a trivial live-swap beats a broad-but-shallow dashboard. If the window is short, Tier 1 + T2.4 polish on the hero is the world-class core; FE-5 breadth can spill past hardware-arrival.

## What waits for hardware (be ready to execute in hours)

- **FE-1 live-integration** — run the go-live checklist the moment Core is up on loopback.
- **FE-7 — real-device `CONFIRMED`/`UNCONFIRMED` on real silicon** — the moat's lead claim shown as *measured fact* on the screen. Gated by bench first-light + M9 (outside this lane). This is the single highest-value moment in the whole frontend arc; the UI is built and waiting for it.

## Decisions / asks for Nick

- **[BLOCKING everything] Run the Step-0 gate.** `npm ci && npm run verify` on a clean checkout — only you can (real machine, not the sandbox). It closes the verification debt on all shipped work. Report failures and the lane fixes-forward.
- **[scope] Polish depth vs breadth in the window.** Recommendation: **hero-path polish (T2.4) over supporting-view breadth (FE-5)** if time is tight — the hero is the demo and the gate.
- **[small] Scenario engine demo-control.** Recommendation: **yes, a visible dev/demo switch** — it's high-leverage for the demo and for dev, and trivially hidden in prod.
- **[parallel apex, your hands] Bench first-light** the moment hardware lands — it's the project critical path and the gate on FE-7 (the moat as measured fact). Everything in this window exists so the frontend is never what the bench is waiting on.

<!--
file: context/audits/2026-06-26_frontend-dev-lane_return.md
purpose: Frontend-dev lane return (first beat). What's built, what's mocked, verification status, cross-lane items the hub must reconcile, and the doctrine-promotion flag. The hub reconciles this as the single spine-writer.
audience: the hub (v6), Nick
state-type: lane return (frontend-dev)
writes-this-session: homesynapse-core/web-ui/dashboard/** (the SPA) + this return. NOTHING else (no core Java, no design docs, no other lane's tree).
anchors: design/13-web-ui-observability-mvp.md (Locked) · context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md (FROZEN v1.1) · context/assessments/2026-06-21_explainability-UX-competitive-research.md · the dispatch 2026-06-21_frontend-dev-lane_session_prompt.md
-->

# Frontend-Dev Lane — Return (first beat, 2026-06-26)

## TL;DR
The V1 dashboard went from a 0-source-file scaffold to a **buildable, type-clean Preact+TypeScript SPA**: app shell + auth + the token-based design system + the device/health/event views + **both halves of the explainability hero** (why-did / why-didn't / did-it-confirm), all built against the **frozen read-API contract** with a one-switch mock/real seam, polling (no WebSocket), and a CI gate. Type-check, lint, contract-check, and 32 executed logic assertions are **GREEN**. The Vite production build + Vitest run in CI (they cannot run in this lane's sandbox — esbuild's native binary segfaults here; see §Verification). A lean, reusable **frontend doctrine** is delivered and flagged for hub promotion.

## What's built (under `web-ui/dashboard/`)
- **Toolchain + build:** Preact 10 + Vite + uPlot (lazy) + CSS Modules + TypeScript, per Locked Doc 13. `package.json` + `package-lock.json`, `vite.config.ts`, `tsconfig.json`, `eslint.config.js`, `vitest.config.ts`. Gradle wiring (`build.gradle.kts`) runs the npm build and stages `dist/` → `src/main/resources/dashboard/` on `assemble` (decoupled from `check` so the Core lane's `./gradlew check` stays Node-free).
- **Design system (the foundation):** `src/styles/tokens.css` — CSS-custom-property tokens (calm-neutral neutrals, single cool accent, traffic-light status, dark-ready opt-in, WCAG AA), inheriting the ratified brand DNA. Component kit: `StatusPill`, `Card`/`Page`/`Toolbar`, `DataTable`, `Drawer`, `CausalChain`, feedback states (`Loading`/`Error`/`Empty`/`ReplayingBanner`/`Freshness`), `AppShell`, `AuthGate`.
- **Typed contract + client:** `src/lib/api/contract.ts` mirrors the frozen contract field-for-field; `client.ts` (bearer auth, RFC 9457 problem+json, ETag/304, the 503 `state-store-replaying` state); `realTransport.ts` + `mock/` (fixtures + transport); `endpoints.ts` (typed reads); `index.ts` = **the one switch** (`VITE_USE_MOCKS`). `shapes.ts` runtime validators = the contract-drift guard.
- **Auth (AB-1):** paste the pairing token → in-memory session only (no localStorage), 401 → prompt, 403 → reject with a clear message.
- **Polling (no-WS, firm):** `src/lib/poll.tsx` — ONE coalesced loop on `meta.viewPosition`; tab-visibility pause; 503 catch-up handled as a calm first-class phase with backoff.
- **Views:** Overview · Devices (A1 list → A3 detail drawer, **live A-class**) · Health (composes A4+A5, **live**) · Activity/events (B1 mock, honest origin) · Automations (B3) · **the hero**: Ask-why hub → run list → causal-chain ("why did it fire?", with command-outcome pills) and the co-equal non-firing verdict ("why didn't it?").
- **Hero fidelity to the research:** device-backward plain sentences (≤20 words, no index paths), two-level disclosure, `Confirmed | Sent-not-confirmed | Failed` shown honestly (shape+color+label), never-a-silent-blank origin, the "never evicted" lead. Locked by `format.test.ts`.

## Live vs mocked (the swap is one switch)
- **Live now (A-class real):** `/api/v1/entities`, `/{id}`, `/{id}/state`, `/internal/projection`, `/internal/dlq`. (Built to the contract; live verification against a running Core is a follow-up — no Core instance in this lane's sandbox.)
- **Mocked to frozen shapes (B-class):** `/api/v1/events` (B1), `/api/v1/health` (B2), and the hero `/runs`, `/runs/{id}/causal-chain`, `/automations/{id}/non-firing`, `/automations` (B3). Swap each to real by changing only the transport wiring as Core delivers them — **B1 soon; B3 after M7.2b** (+ **M7.3 for the CONFIRMED/UNCONFIRMED outcome half** — until then the UI renders DISPATCHED/FAILED/SKIPPED and lights up confirmed/unconfirmed when M7.3 lands live, which per the snapshot is M7.4 wiring).

## Verification status
- **GREEN:** `tsc --noEmit` (strict, all ~35 files) · `eslint .` · `scripts/contract-check.mjs` (11 endpoints, version `v1.1-2026-06-21`) · **32 executed assertions** (contract validators run against every mock fixture + the mom-test sentence/outcome/origin/verdict + routing), run via a CommonJS emit + Node since Vitest is blocked here.
- **Deferred to CI (environment limit, NOT a code issue):** the Vite production build and Vitest. **esbuild's prebuilt native binary segfaults in this lane's sandbox** (confirmed: a freshly downloaded binary exits 139). Both run normally in CI (`ci/frontend.yml`, Node 20). **Bundle estimate ≈ 22–26 KB gzipped** (Preact ~4.8 + minified app ~13 + CSS ~4.5) vs the 100 KB budget — ~75 KB headroom; the hard gate (`check-bundle-size.mjs`) confirms the real number in CI.

## Cross-lane items for the hub (do not let me decide these unilaterally)
1. **Doc 13 WebSocket currency note (please reconcile).** Doc 13 (2026-03-10, Locked) is WebSocket-first; the newer rulings (V1 record D-OPEN-3, the contract freeze, this dispatch) make **no-WebSocket / poll-1–2s FIRM**, which I implemented. The now-superseded Doc 13 sections to mark: **§1 (WebSocket-first principle), §3.5 (WebSocket integration), §3.8 health-via-WS, §8.2 (WS protocol table), and the WS-specific parts of §4.1/§6/§11**. Recommend a Doc 13 currency addendum pointing these at the poll model. (This is exactly the doc-vs-ruling drift the currency discipline catches.)
2. **Frontend CI wiring (1-step spine change).** `web-ui/dashboard/ci/frontend.yml` is delivered ready-to-use; the hub places it in `.github/workflows/` (repo-root shared infra outside this lane's isolation). It path-filters to `web-ui/dashboard/**` and runs `npm ci && npm run verify`.
3. **Contract friction — no entity display name (additive, low-friction).** A1/A2/A3 carry no human name; the UI humanizes `entityId` (`labelFor`). Recommend an **additive** `name`/`label` field on the entity reads (backward-compatible). Flagging per the change-discipline rule; Nick's call on public-API shape.
4. **Doctrine promotion.** `web-ui/dashboard/FRONTEND_DOCTRINE.md` is the lean, reusable frontend doctrine Nick asked for ("from now on"). It lives in-module per write-isolation but is a **candidate for promotion** to a shared design-system home and, later, a loadable `nexsys-frontend` skill (analogous to nexsys-coder / nexsys-project-manager).

## Next beats (frontend-dev lane)
- Stand up a running Core on loopback and verify the A-class views live (freshness + the 503 boot state) end-to-end.
- Swap B1 → real when Core lands the events read; wire confirmed/unconfirmed on the hero when M7.3 goes live (M7.4).
- Charting (uPlot sparklines) on Overview/Health detail — the lazy `SparkChart` seam exists; wire when health time-series reads land.
- Component/interaction tests (Preact Testing Library) once running in CI; a11y pass (keyboard + screen-reader) on the hero.

## Appendix — causal-chain presentation UX research (fold to `context/assessments/` if desired)
Focused pass on *presenting* the chain to a non-expert (we already have the competitor-teardown research). Key rules now embodied in the UI + doctrine: device-backward sentences (effect→cause, ≤20 words, ~8th-grade); two disclosure levels only (plain line + one expand); bounded linear chain (not a graph — avoids the spaghetti/index-path failures); command outcome in the severity palette + shape + label with "sent ≠ confirmed" two-tick language (UNCONFIRMED = calm amber, never a fake success); absence/"why-not" as one verdict sentence + the single gating fact + a next step; chain as a semantic `<ol>` (not `role=tree`) with `role=status` for live transitions; Apple Home's actor+action+time phrasing for origin. Sources: NN/g (match-real-world, plain-language, progressive-disclosure, hostile-error-messages, visibility-of-status), Carbon (status + empty-state patterns), Stripe/Signal (sent-vs-confirmed), Gmail "why is this spam" (absence explanation), W3C APG + WCAG SC 4.1.3, Apple Home activity history.

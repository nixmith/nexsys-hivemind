<!--
file: context/audits/2026-06-29_frontend-dev-lane_FE0-FE2-FE3_return.md
purpose: Frontend BUILD lane return for the 2026-06-29 session that executed the master-plan amendment-1 brand/architecture foundation: FE-0 (token source + D-FE-10 measurement), FE-2 (dark-default + theme toggle), FE-3 (name-light + i18n keying). The hub reconciles this into the spine (single spine-writer); two batched decisions for Nick at the end.
audience: the PM mission-control hub (reconciles into the spine + the build-lane hand-off); Nick (the 2 batched decisions in §4).
state-type: lane return (frontend build lane).
status: RETURNED 2026-06-29. Write-isolated: wrote ONLY under web-ui/dashboard/** + this return. No Core, no Locked doc, no spine, no other lane's tree.
anchors: context/planning/2026-06-29_frontend-master-plan.md + _amendment-1.md (the authority this executes) · context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md (FROZEN v1.1, untouched) · web-ui/dashboard/FRONTEND_DOCTRINE.md · MODULE_CONTEXT.md
-->

# Frontend Build Lane — Return (FE-0 + FE-2 + FE-3, 2026-06-29)

## TL;DR
Executed the amendment-1 **Track-B brand/architecture foundation** in the ordering Nick set (**FE-0 → FE-2**, with **FE-3** completed too): the dashboard now (1) generates its design tokens from a **platform-neutral W3C-DTCG source** (D-FE-8), (2) defaults to **dark** with a `prefers-color-scheme`-aware **dark/light/system toggle** (D-FE-1), and (3) is **name-light + i18n-keyed** (D-FE-9). The **D-FE-10 typeface measurement** is done (numbers in §3). All work is pure-frontend against the existing system — **no Core dependency, no contract touched, no rework risk.** FE-0's "generate the current file byte-for-byte" proof is **GREEN in-sandbox** (101/101 tokens identical per selector); the full `frontend.yml` gate (tsc/eslint/vitest/vite-build) is **deferred to CI** per the env-model (the VM mount truncates freshly-written files in this lane's sandbox — same class of limit as the first beat's esbuild segfault). **The first hero-on-dark presentation is ready for your sign-off (§4) before any further hero/dark polish.**

## 1. What shipped (all under `web-ui/dashboard/`)

**FE-0 — token architecture (D-FE-8). The keystone; done before FE-2 so dark-default is authored once, in the generated system.**
- **New source of truth:** `src/styles/tokens/tokens.dtcg.json` — a W3C Design Tokens (DTCG) file. `core` = mode-independent primitives; `light`/`dark` = semantic role tokens. Cross-references (`{core.neutral.50}`) are preserved as `var(--hs-…)` in output, so a primitive change still cascades. Each token pins its exact CSS var name in `$extensions.hs.var` → **zero component churn**.
- **Generator:** `scripts/build-tokens.mjs` — zero-dependency Node. Emits `src/styles/tokens.css`. `--theme-default=light|dark`, `--check` (drift-guard), `--stdout`. Wired into `package.json`: `tokens`, `tokens:check` (in `verify`), and `prebuild` (regenerates before `vite build`).
- **Faithfulness proof (FE-0's whole point):** generated `--theme-default=light` and diffed against the prior hand-authored `tokens.css` with a per-selector CSS parser → **101 declarations, identical per selector** (`:root` + `:root[data-theme='dark']`). FE-0 is a pure refactor; nothing rendered changes.
- **Tooling note (decision-recorded):** the amendment named "Style-Dictionary / W3C Design Tokens JSON". I used the **DTCG JSON source + a tiny in-repo generator** rather than adding Style Dictionary as a dependency, because (a) npm dependency installs are unreliable on this lane's mounted filesystem (ENOTEMPTY on rename), and (b) the durable, future-proofing asset D-FE-8 actually wants is the **neutral source file**, which this is — it's valid DTCG, so Style Dictionary can be adopted later for native/B2B outputs as a **generator swap, not a re-author**. Net: the future seam is preserved with zero added build deps (on-brand for jlink-to-a-Pi + the 100 KB budget).

**FE-2 — dark-default + theme toggle (D-FE-1), authored on the FE-0 source.**
- `tokens.css` regenerated to the **dark-default** structure: `:root` = core + dark (recorded default + system fallback); `@media (prefers-color-scheme: light) :root:not([data-theme])` = light for unset/OS-light; `:root[data-theme='light'|'dark']` = explicit toggle. AA palette in both modes (the existing AA-tuned semantic tokens, unchanged).
- `src/lib/theme.ts` — preference state (`system`/`light`/`dark`), persistence, **live OS-change tracking** for "system", `color-scheme` + `<meta name=theme-color>` sync, a `useTheme()` hook. Theme pref lives in `localStorage` (non-secret UI state — deliberately distinct from the **in-memory-only** auth token, AB-1).
- `index.html` — an **anti-FOUC inline boot script** sets `[data-theme]` before first paint; `theme-color` meta added. `src/main.tsx` calls `initTheme()`.
- `src/components/ThemeToggle.tsx` (+ `.module.css`) — a compact **segmented control built on native radios** (free keyboard arrow-nav + SR semantics); selected state = fill + icon shape + label (not color-alone); ≥24px targets (**WCAG 2.2 SC 2.5.8**). Wired into the `AppShell` footer.

**FE-3 — name-light + i18n keying (D-FE-9).**
- `src/lib/i18n.ts` — `BRAND.productName` (single source of truth for the name; the unratified rename flips one token) + a **keyed message catalog** with `t(key)` (English; locale/RTL/Intl-format seams reserved).
- De-hardcoded **all ~11 user-facing "HomeSynapse" strings** → `BRAND.productName` / `t()` across `AppShell`, `AuthGate`, `feedback`, `CausalChain`, `DevicesView`, `HealthView`, `OverviewView`, `format.ts`. `document.title` now set from the brand token. `format.test.ts` updated to assert via `BRAND` (stays green now and rename-survivable). Remaining "HomeSynapse" occurrences are code-header comments + the static `index.html` `<title>/<noscript>` (no-JS fallback) + one dev-only mock fixture — all intentional/non-chrome.

**Files** — created: `tokens/tokens.dtcg.json`, `scripts/build-tokens.mjs`, `lib/theme.ts`, `components/ThemeToggle.tsx`, `components/ThemeToggle.module.css`, `lib/i18n.ts`. Modified: `styles/tokens.css` (regenerated), `package.json`, `index.html`, `main.tsx`, `components/AppShell.tsx` + `.module.css`, `lib/format.ts`, `lib/format.test.ts`, `components/AuthGate.tsx`, `components/feedback.tsx`, `views/{DevicesView,HealthView,OverviewView}.tsx`, `components/CausalChain.tsx`, `MODULE_CONTEXT.md`. Plus this return. **Nothing else.**

## 2. Verification
- **GREEN in-sandbox (reliable — pure-Node, synced data files):** token generation; the **FE-0 equivalence proof** (101/101 per selector); the **drift-guard** (`tokens:check` — committed `tokens.css` matches the source).
- **Deferred to CI (env limit, NOT a code issue):** `npm run verify` = `tokens:check · lint · typecheck · test · build · check:bundle · check:contract`. This lane's VM mount **truncates/null-pads freshly-written files** when read back via the shell (confirmed: `package.json`, edited `.tsx`, and even `node_modules/@types/node` read truncated on the shell mount while the authoritative host file-tools show them complete and correct). Running `tsc`/`eslint` against those truncated reads only yields false positives, so per the cowork-environment-model the build gate is the **deferred** step that **Nick/CI runs on a clean checkout**. Code was authored + reviewed host-side; the new TS is idiomatic Preact/strict-TS (typed `t()` keys, `VNode` returns, no `any`, no unused locals).
  - **Exact commands for CI / a synced local checkout:** `cd web-ui/dashboard && npm ci && npm run verify`.
- **Bundle:** `tokens.css` gzips to ~2.2 KB (unchanged); the FE-2/FE-3 additions are small (a token module, a toggle, a tiny i18n catalog) — well within the ~75 KB headroom under the 100 KB budget; the hard gate (`check-bundle-size.mjs`) confirms the real number in CI.

## 3. D-FE-10 — typeface measurement (the evidence Nick asked for; reported, not unilaterally flipped)
Measured a real Inter-variable woff2 (fontsource `@fontsource-variable/inter` 5.2.8, Latin) against the budget:

| Option | Size (woff2) | Notes |
|---|---|---|
| Drop-in Latin variable (normal axis) | **48,256 B (~47 KB)** | fontsource "latin" subset; gzip doesn't help (woff2 is already compressed). |
| **UI-minimal custom subset** (variable weight axis; ASCII + ~16 dashboard glyphs: curly quotes, en/em dash, →, •, ·, °, …, ×, ≈, ±, ≤, ≥; `kern,liga,calt,tnum`) | **25,388 B (~25 KB)** | The realistic self-host. Keeps all weights (400/500/600) in one variable file. |
| Current bundle / budget | ~22–26 KB gzip / **100 KB** | The font is a **separate `@font-face` asset**, not part of the JS/CSS initial bundle the budget measures — but even counted against budget philosophy, ~25 KB fits with ~50 KB headroom. |

**Read:** self-hosting a ~25 KB custom-subset Inter-variable is **affordable** and buys **true cross-surface type consistency** (the website design-system wants Inter; today the dashboard renders SF/Segoe/Roboto per the user's OS). It stays **local-first** (the woff2 ships in the image, served from loopback — no phone-home). **Recommendation:** lean **yes** to self-hosting subset Inter — but typography is the most visible brand element, so I did **not** flip it unilaterally; recommend Nick rule it **alongside the dark-hero sign-off** (batched in §4). The system stack remains a fine zero-byte V1 default; thanks to the FE-0 source + the `--hs-font-sans` token, adding Inter later is a small isolated change (one `@font-face` + flip one token value + ship the woff2).

## 4. Decisions for Nick (batched — recommendation each; the escalation discipline)
- **[SIGN-OFF, gates further FE-2 polish] First hero-on-dark presentation.** Shown this session (the causal-chain hero on the new dark default, with the sidebar theme toggle). Per the amendment I'm holding further hero/dark **polish** until you nod. **Recommendation: approve** the dark default + the toggle treatment as the recorded brand look; flag any palette/contrast change (it's a token-source edit + regenerate — cheap).
- **[D-FE-10] Typeface.** Self-host a ~25 KB custom-subset **Inter-variable** on the dashboard for cross-surface coherence, or keep the **system stack**? **Recommendation: self-host subset Inter** (coherence + craft, fits budget, stays local-first) — but it's your brand call; system-stack is a legitimate zero-cost hold. Either way the seam is built.

(NON-BLOCKING defaults already taken, revisable: theme pref persisted in `localStorage`; toggle = a 3-way segmented control in the sidebar footer; the active-segment-shows-label compaction for the narrow rail.)

## 5. Cross-lane asks (for the hub — none are contract changes)
- No new asks. The carried sequencing confirmations from the master plan still stand for the **Track-A / FE-1 live-integration** WU (confirm B3 `/runs`,`/causal-chain`,`/non-firing`,`/automations` live + stable; the C8 entity-`name` landing for FE-5; B1/B2 (M7.5c) landing). **FE-1 was not attempted this session** — it needs a running Core on loopback, which isn't available in this lane's sandbox; it remains the mid-Aug-gating WU for a session/environment that has Core up.

## 6. Preflight + isolation
- **Freshness preflight:** built on the 2026-06-29 planning-lane preflight (STALE-benign, 0 CONFLICTED). The two STALE items it named (dark-default unfolded; name hardcoded) are exactly what FE-2/FE-3 closed. Contract v1.1 untouched and unmirrored-against (no data shapes changed). Source round-trip: the D-FE-10 numbers and the FE-0 equivalence are re-derived from source/measurement, not copied.
- **Write-isolation:** held. Wrote only under `web-ui/dashboard/**` + this return under `context/audits/`. Read (never wrote) the plan, amendment, PM assessment, contract, and Locked docs. Did not touch Core, the spine, any Locked design/governance doc, or another lane's tree.

## 7. Next WU (refuse-to-close — the lane points forward)
After Nick's **§4 sign-off**: (a) fold any dark-palette/typeface ruling (token-source edit + regenerate — small), then (b) **converge on FE-4** — hero state coverage (loading/empty/error/503-replaying/offline) + **WCAG 2.2 AA** + screen-reader pass, **built mobile-first** (D-FE-7), with the **axe-core a11y CI gate** (amendment §3 G6) added to `frontend.yml`. In parallel, **FE-1 (live-integration)** remains the mid-Aug-gating WU and should run in a session/environment with **Core up on loopback** (it needs no decision, only a running backend). FE-PWA → FE-5 → FE-6 follow per the amendment sequence.

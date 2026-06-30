<!--
file: context/planning/2026-06-29_frontend-master-plan_amendment-1.md
purpose: Amendment 1 to the Frontend Master Plan — folds Nick's 2026-06-29 rulings on the four future-proofing decisions surfaced by the PM assessment (D-FE-1 dark-default, D-FE-7 cross-platform/PWA, D-FE-8 platform-agnostic tokens, D-FE-9 i18n-readiness) into an updated work-unit sequence, so the frontend build lane has ONE updated authority (plan + this amendment). Keeps the website parked per Nick's steer. Does NOT replan; it is a delta.
audience: the frontend build lane (executes against the plan + this amendment); the PM hub (reconciles into the spine + the build-lane hand-off); Nick.
state-type: planning amendment (delta to context/planning/2026-06-29_frontend-master-plan.md).
status: RULED 2026-06-29 (Nick co-signed all four via batched decision). Amends §2.4 (work-unit sequence) + §5.4 (decisions). The base plan stands as v1 of record; this is the layer on top.
-->

# Amendment 1 — Nick's rulings folded (the future-proofing layer)

This is a **delta**, not a replan. The base plan (`2026-06-29_frontend-master-plan.md`) stands; this folds the four decisions Nick ruled on 2026-06-29 (from the PM assessment) into the work-unit sequence and disposes of the PM's remaining gaps. The website stays **parked** per Nick's explicit steer ("not worried about the website right now") — this amendment is dashboard-only.

## 1. Decisions RULED (Nick, 2026-06-29 — binding-unless-reversed)

- **D-FE-1 — Dark-default: RULED YES.** Dark is the recorded brand default; honor `prefers-color-scheme` on first load; ship a persistent **dark/light/system** toggle; WCAG AA in both modes. (The first hero-on-dark presentation still **escalates** to Nick before the build invests — discipline, not a re-decision.)
- **D-FE-8 — Platform-agnostic tokens: RULED YES.** Adopt a single neutral token source (Style-Dictionary / W3C Design Tokens JSON) that **generates** `tokens.css` now, and can later generate native-app / B2B-theme outputs. The keystone future-proofing call — do it **before** dark-default rewrites the token layer.
- **D-FE-7 — Cross-platform: RULED responsive + installable PWA; native deferred-but-seam-preserved.** **Mobile-first is now a V1 requirement** (not a P2 confirm); ship a PWA app-shell (installable, offline — on-brand for local-first); record a "native reconsidered post-launch" position + keep the seam open.
- **D-FE-9 — i18n-readiness: RULED YES (English ships).** Architect copy as a **keyed message catalog** (keys, not inline strings) and reserve locale / RTL / number-date-format seams now; V1 ships English-only.

Carried (evidence-gathering, not a pre-decision): **D-FE-10 — typeface** — the build lane **measures** a subsetted Inter-variable woff2 against the live bundle budget during the token work and decides self-host-Inter-on-dashboard vs system-stack **on evidence** (report the number). Parked (website): **D-FE-2** (site stack/hosting/analytics) and the website-heavy v2 — not now.

## 2. Updated work-unit sequence (supersedes plan §2.4)

Two tracks start **now, in parallel** (no shared files, no conflict), then converge. Sizing S/M/L relative; each WU ends green-gated.

**Track A — data (starts now; the mid-Aug gate; needs no decision):**

| # | Work unit | Size | Notes |
|---|---|---|---|
| FE-1 | Live-integration: point the hero endpoints at running Core; render real log-derived data (seeded/replayed OK); handle real edge cases (real `UNKNOWN`/`UNCONFIRMED`, terminal reasons, empty/large sets) | **M** | The mid-Aug gate's floor. Depends on running Core, **not** the bench. **Start immediately.** |
| FE-7 | Bench-gated: real-device `CONFIRMED`/`UNCONFIRMED` on the hero once M9 + bench land | **S (UI)** | The moat lead on real silicon. UI built-and-waiting; gated by the bench (outside this lane). |

**Track B — brand/architecture foundation (starts now; cheap-now/expensive-later):**

| # | Work unit | Size | Notes |
|---|---|---|---|
| FE-0 | **Token architecture:** stand up the neutral token source (Style-Dictionary/W3C JSON) that generates the current `tokens.css` byte-equivalent; wire it into the build. **Includes the D-FE-10 typeface measurement** (subsetted Inter woff2 vs budget → self-host-or-system, reported) | **M** | **D-FE-8.** Keystone — do **before** FE-2. V1 output identical; future native/B2B themes become a generation step. |
| FE-2 | Dark-default + `prefers-color-scheme` first-paint + persistent dark/light/system toggle; AA both modes | **M** | **D-FE-1.** Authored on the FE-0 token source (so it's done once, in the generated system). **Escalate the first hero-on-dark presentation to Nick.** Depends on FE-0. |
| FE-3 | De-hardcode: `BRAND.productName` token **+ keyed i18n message catalog** in `format.ts`; reserve locale/RTL/format seams; validate vs `asimtote`; rename-survivable wordmark slot | **M** | **Combines name-light (FE-3) + D-FE-9** — same discipline. Touches name → **escalate**. English-only ship. |

**Converge (after Tracks A+B reach the hero):**

| # | Work unit | Size | Notes |
|---|---|---|---|
| FE-4 | Hero state coverage (loading/empty/error/503-replaying/offline) + WCAG 2.2 AA + screen-reader verify — **built mobile-first** | **M** | The hero must be honest + accessible + excellent on a phone before the go/no-go. **D-FE-7** mobile-first applies here first. |
| FE-PWA | Installable PWA app-shell (manifest + offline app-shell); no phone-home | **S** | **D-FE-7.** Cheap, app-like, on-brand (installable no-cloud app). After FE-4; before launch. |
| FE-5 | Supporting views to hero-grade: state matrix + AA + polish, **mobile-first**; fold entity `name` (C8) when Core ships it | **L** | The run-up to Nov 25. |
| FE-6 | Responsive/perf confirm + **render-at-scale**: list virtualization for large run/event tables + a render budget (not just the bundle budget); uPlot lazy-load + bundle re-check | **M** | Folds PM gap G4(b). Even on the curated set, set virtualization + a render budget as a V1 convention. |

## 3. Disposition of the PM's remaining gaps (G4–G8) — fold cheap, defer heavy

- **G4(b) render-at-scale → folded into FE-6** (above). **G4(a) frontend stability/anti-breakage + versioning policy** → a build-lane **working convention** + a short doctrine note (don't break the user's dashboard across updates); not mid-Aug-gating. **G4(c) config-simplicity** → reserved for the (out-of-scope) future authoring UX.
- **G6 design-system governance:** extend `frontend.yml` with an **automated a11y gate (axe-core)** — cheap, high-value for an AA brand, **do it** (small add to FE-4). A documented component catalog (Storybook-class) + visual-regression → **build-lane conventions / a light future pass**, not mid-Aug-gating.
- **G7 local error observability (no-telemetry brand):** the on-brand answer is a **local, user-exportable diagnostic** (never silent telemetry) — note the direction; design it with FE-5, not now.
- **G8 live-hero demo-data + SEO:** website-scoped → **parked** with the website. (When the website resumes: the live-hero embed must render against a **static seeded/replayed fixture**, never a live backend.)

## 4. Start here (the build lane's marching orders)

1. **Begin FE-1 and FE-0 in parallel, now.** FE-1 needs nothing; FE-0 is the token keystone that must precede FE-2.
2. **Then FE-2 (dark-default) on the FE-0 tokens** — escalate the first hero-on-dark presentation to Nick before investing in polish. **FE-3 (name + i18n keying)** runs in parallel within Track B.
3. **Converge on FE-4** (hero state + AA, mobile-first) → FE-PWA → FE-5 → FE-6.
4. **Everything mobile-first from the start** (D-FE-7) — the hero must be excellent on a phone.
5. **Website + website decisions stay parked.** Bench first-light (separate lane, Nick's hands) runs in parallel and gates FE-7.

Routes through the PM hub for reconciliation + the hand-off to the frontend build lane (upgrading its brief from "build to the plan" to "build to the plan + this amendment").

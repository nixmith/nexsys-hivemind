<!--
file: context/audits/2026-06-29_frontend-strategy-and-planning-lane_return.md
purpose: Lane return for the 2026-06-29 Frontend Strategy + Planning session (nexsys-frontend role, PLANNING register). Hands the Frontend Master Plan back to the PM hub for reconciliation into the spine + the upgraded hand-off to the frontend build lane.
audience: the PM mission-control hub (folds this return into the spine; it is the single spine-writer — this lane does not edit the spine); Nick (the 6 decisions in §4).
state-type: lane return (planning-session closeout — the planning analog of a build lane return).
status: RETURNED 2026-06-29. Write-isolated: this session wrote ONLY the plan + this return; it touched no Core, no Locked design/governance doc, no spine file.
-->

# FRONTEND LANE RETURN — Frontend Master Plan (planning arc) — 2026-06-29

**1. Summary.** Produced the **Frontend Master Plan** (`context/planning/2026-06-29_frontend-master-plan.md`, 316 lines) — a research-backed, critically-analyzed plan for ALL remaining frontend work across both surfaces (the observability dashboard + the marketing website), built ON the verified built state, the FROZEN v1.1 contract, the Locked docs, and the ruled brand spine. Key reframe confirmed and carried: **the dashboard is substantially built, not a scaffold** — the residual is live-integration + brand-ruling folds + accessibility hardening + filling gaps, *not* construction. This upgrades the existing frontend build-lane brief from "build to the contract" to "build to this researched plan." **No code was built; this was planning only.**

**2. Files.** Created: `context/planning/2026-06-29_frontend-master-plan.md` (the plan) + this return. Per this session's dispatch, the plan was authorized under `context/planning/`. No files under `web-ui/dashboard/`, no Core, no Locked docs, no spine — write-isolation held.

**3. Gate result.** **N/A — planning session, no build.** The `frontend.yml` / `npm run verify` gate is the build lane's, run when it executes the plan's work units (FE-1…FE-7). No deferred-build-gate applies (nothing was compiled).

**4. Decisions / defaults surfaced for Nick (the plan ends on these — batched, with recommendations).**
- **BLOCKING:** (D-FE-1) dark-default + the first hero/dark brand presentation — *recommend approve* (brand-defining; gates FE-2); (D-FE-2) static-site stack + hosting + analytics — *recommend Astro+Preact, static host, no/self-hosted-cookieless analytics, no runtime CDN* (gates the website build); (D-FE-3) product-name ratification W-11 — *recommend keep building name-light, ratify `asimtote` only post-clearance* (blocks only public wordmark/domain/email).
- **NON-BLOCKING (safe defaults already in the plan):** (D-FE-4) collapse to one brand [Googol model]; (D-FE-5) typeface coherence-by-discipline [website Inter / dashboard system-stack]; (D-FE-6) show the real hero on the website once demo-ready on real data.

**5. Cross-lane asks (FOR THE HUB — not unilateral edits; the contract is consumed, never invented).**
- **Sequencing confirmations** (no contract change): confirm B3 (`/runs`, `/causal-chain`, `/non-firing`, `/automations`) is live + stable for the live-integration pass (FE-1); confirm the optional entity `name` (C8) landing sequence (FE-5); confirm B1 events + B2 health (M7.5c) landing sequence (UI mocks until then).
- **Design-system reconciliation (proposed, not done):** the website design-system DRAFT docs (`visual-design-reference.md`, `typography-reference.md`, `website-design-vision.md`) restate values that have drifted from the live `tokens.css` and still describe two brands. Recommend the hub schedule a reconciliation making `tokens.css` the cited source of truth, collapsing the two-brand framing per W-11, and folding the dark-default + AA-semantic rulings. (This lane proposes; it did not edit those docs.)
- **Bench dependency (noted, not owned):** the dashboard's *real-device* `CONFIRMED`/`UNCONFIRMED` (the moat lead) is gated by bench first-light + M9 — outside this lane. The UI is planned to be built-and-waiting; the mid-Aug gate can be met on seeded/replayed real logs against running Core if the bench slips.

**6. Accessibility + stranger-test.** No explanation surface was built this session, so nothing new to certify — but the plan **binds both** as first-class: WCAG **2.2** AA across both surfaces (the new criteria folded — target size 24×24, focus-not-obscured, accessible-authentication/allow-paste on the token gate), and the stranger/"mom" test as the hero acceptance bar (the built `format.ts`/`format.test.ts` lock it). The honest-claim discipline + the 2026-06-27 corrections (HA-traces-persist; Nant-Holdings attribution; the HA "why-didn't-it" re-weight) bind all copy on both surfaces.

**7. Preflight (for the hub's record).** Frontend freshness preflight = **STALE-benign, 0 CONFLICTED** (Checks 5 + 6 STALE: the live-integration residual + the two unfolded 2026-06-27 brand rulings). For a planning session these are inputs to the gap analysis, not blockers. The plan was independently adversarially audited this session (contract fidelity, built-state, brand rulings, the three competitive corrections, V1 constraints, pointer-not-copy, internal consistency) → **CLEAN**.

**8. Next WU (refuse-to-close — the lane points forward).** Hub reconciles this plan into the spine and hands it to the **frontend build lane**, which executes **FE-1 (the live-integration pass: point the built hero at running Core, render real log-derived data, handle real edge cases)** — the mid-Aug-gating work unit — after Nick rules **D-FE-1** (dark-default) so FE-2/FE-3 (the brand-defining folds) can ride alongside FE-1 and the demo *looks* like the brand. Website copy (finishing the three stub dossiers) can advance in parallel as a separate, non-engineering track.

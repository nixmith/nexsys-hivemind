<!--
file: context/audits/2026-07-27_devtools-chain-glance_return.md
purpose: THE DEV-TOOLS GLANCE RETURN (filed verbatim from Nick's operator paste, v39 beat 9) — the G1 residual ADJUDICATED CLIENT-SIDE: the SPA crashes on a null string in the chain render path and the crash kills the polling loop; the wire (proven populated by WCAP-2) is healthy. The FE fix = FE-LIVE-V112 item 1.
audience: the v40 hub (launch input — supersedes-where-differs the v40 prompt's chain-glance charge: the glance is DONE; charge 3 opens at the FE-LIVE-V112 authoring with item 1 first).
status: FILED 2026-07-27 (v39 beat 9 — the addendum beat; evidence arrived after the beat-8 close and is filed so no session ever consumes it from a transcript). L3 held throughout.
hub-annotation (one hypothesis for the lane's authoring, held loosely): the mocks emit optional keys either as full-v1.1.2 strings or fully ABSENT (pre-v1.1.2 exhibits) — the LIVE wire serves PRESENT-BUT-NULL (`resultOutcome: null` beside `settled: true`, `reason: null`, `trigger.type: null`, `firingValue: null`) — the tri-state seam (absent / null / value) is exactly where a fixture-green `.toLowerCase()` crashes on the field; the lane verifies at source and adds present-but-null test rows for EVERY optional key.
-->

# DEV-TOOLS GLANCE RETURN — 2026-07-27 late evening — run `01KYJZKHJGJR8Y94W2D203SJH6` (bench-hero, freshest, = WCAP-2 capture C) — VERDICT: CLIENT-SIDE

**G1's watch does NOT clear; the FE fix is confirmed as FE-LIVE-V112 item 1.**

EVIDENCE (screenshots in the operator session):
1. **Wire delivers:** earlier session — the SPA polled causal-chain 10× / ~50 s, all **304 Not Modified** (immutable resource, conditional GETs; the cached body = the 1717-B populated chain WCAP-2 proved for this exact runId). Server side healthy.
2. **Client crashes:** console shows repeated `Uncaught (in promise) TypeError: can't access property "toLowerCase", e is null` @ `index-2dg4sorw.js:1:66305` (promise callback → setState). 16 errors in session 1; 3 after re-auth. The card renders header + EMPTY body ("Why this happened / ← All runs").
3. **The crash kills the loop:** post-error, a 41-s Network window shows ZERO causal-chain requests (projection polling continues normally); the "Updated" stamp frozen (~19 min).
4. **Mechanism (high confidence, one code-grep to confirm):** a verdict-pill/label renderer lowercases a nullable string field — candidates present in EVERY real payload: `resultOutcome: null`, `reason: null`, `trigger.type: null` + `automationName: null` (rotated identities), `firingValue: null`. Explains the redux's universal blanks across all eras, incl. populated-chain runs.
5. **Incidental findings:** (a) hard reload → AuthGate (token is tab-memory by design; microcopy consistent) — F5 requires re-pairing; (b) **`favicon.ico` → 401 problem+json** (the root path is not in the posture-(A) allowlist `/`, `/dashboard`, `/dashboard/**`); (c) served assets byte-match the `c09c61c` Vite build (99.02 kB js / 28.13 kB css / 25.39 kB woff2).

RESIDUAL (optional, hub's call): a single in-browser Response-tab capture of the chain 200 was not landed (reload wipes auth; the re-auth session crashed before a filtered capture). Wire content already proven by WCAP-2; **skippable — so ruled at filing.**

FE-LIVE-V112 shape this evidence supports: (1) null-guard the string mappings in the chain renderer; (2) the honest "no detail recorded" empty state; (3) an error boundary + surfaced fetch errors (also cures the why-not eternal-spinner posture). **Core side: NO change implied by this glance.**

L3 held: the token entered the browser only; the Headers tab never captured; no token in any screenshot or this block.

**Hub adjudications at filing (v39 beat 9):** the G1 ledger cells re-stamped — the demo blocker = **FE-LIVE-V112 item 1** (null-guards + error boundary + empty state; SMALL; its landing rides frontend.yml and reaches the Pi on any warm rebuild + restart, well before gate day). The favicon 401 = COSMETIC; REC an FE-side `/dashboard/`-scoped favicon link in `index.html` (zero auth-surface change) folded into FE-LIVE-V112, never an allowlist widening. F5-re-pairing = BY DESIGN (Doc 13 §12; posture-(B) is the post-gate successor). The crash-kills-the-loop observation makes (f)'s error boundary evidence-backed, not stylistic.

<!--
file: context/assessments/2026-07-01_bench-first-light_PM-assessment-and-dispositions.md
purpose: PM mission-control hub's quality-gate assessment + escalation dispositions for the bench Phase-0/1 first-light return (context/audits/2026-07-01_bench-bringup-lane_phase-0-1_return.md + nexsys-bench 5ceff3b). Source-verifies the deliverables against the nexsys-bench repo (verify the territory, not the report), dispositions E1-E6, assesses the three payoffs + the frontend cross-lane routes, and records M9-readiness.
audience: Nick (the strategic calls: AMD-CAND-1 ratify, AMD-CAND-2/3 color scope, the M9 go); the M9 lane (consumes the bench corpus as its acceptance spec); the frontend lane (the E5 rendering semantics); the governance fold (AMD-CAND-1 + the E2 Doc-08 §3.3 correction).
state-type: PM assessment + disposition record.
status: ASSESSED 2026-07-01 by the v12 PM hub. Verdict: FIRST-LIGHT ACCEPTED — deliverables source-verified, the moat measured, the critical path delivered, M9 nearly unblocked. Spine reconciliation + commit HELD until the truncated-tail phantom is quiescent host-side (active this session; VM git garbled for both repos).
-->

# PM Assessment — Bench First-Light (Phase 0 + Phase 1, 2026-07-01)

## 0. Verdict

**First-light is the highest-leverage block in the project, and it landed clean.** The instrument is built, verified, frozen, and recorded; the moat is measured fact on real silicon with a git-native regression substrate; the D5 sizing trigger is answered; and the AMD-CAND-1 measured values are in hand. The work is rigorous and scientifically honest (provenance-tagged, measured-vs-referenced separated, every capture anchored to the frozen firmware). **The critical path has delivered, and M9 is now nearly unblocked.** ACCEPT the return; disposition the six escalations below; route the convergent AMD-CAND-1 pass to ratify.

## 1. Verification (PM gate — verified the territory, not the report)

Independently confirmed against the `nexsys-bench` repo (HEAD `5ceff3b`, pushed):

- **Deliverables are real captures, not stubs.** Coordinator entry records VID:PID `10c4:ea60` + the *measured* `EmberZNet 7.4.5.0/EZSP v13` against the `[REF]` scaffold's expected `8.0.2/v14` (honest provenance). SNZB-03P entry captured the dual-cluster surprise + `manufacturerCode 0x1286` (filled the `[CONFIRM-ON-BENCH]`). Both fixtures are genuine raw-ZCL event streams (`fixtureVersion 1`, `source: BENCH_CAPTURE`, 110/80 lines). The Hue confirmation block carries measured latencies, timestamps, and log windows — clearly a live capture.
- **The moat is measured both ways.** True `CONFIRMED` (unsolicited authoritative `Report_Attributes`: on_off 293–701 ms, brightness 353–686 ms, CT 6.7–8.4 s) and honest `UNCONFIRMED` (effect/identify ACK-then-never-report). The differentiator is now regression-protected fact.
- **Write-isolation held.** The lane wrote only `nexsys-bench/**` + the return under `context/audits/`. No Core, no Locked doc, no spine edit.
- **Note (mount state):** the VM git view is garbled for both repos this session (mount-lag/phantom active) — the committed+pushed HEAD + the file tools are authoritative; I relied on those. Spine commits stay held until quiescent.

**Fidelity verdict: PASS.**

## 2. What first-light proved (the three payoffs)

1. **The moat, measured** — CONFIRMED exists, honest UNCONFIRMED exists, both replayable. The lead differentiator stops being a design claim.
2. **D5 answered — the `exposes`→capability map is MODEST on real silicon.** Both devices interviewed `quirk_applied=False` on the generic zigpy path, zero failures, mfr-specific clusters ignored gracefully. **This sizes M9 small — the curated-subset fallback is NOT needed for Wave-1.** (The go/no-go's pacing-risk-B, "M9 balloons," is retired for Wave-1.)
3. **AMD-CAND-1 measured values delivered** — the 5 Hue confirmation blocks + the SNZB empty block + six engine caveats.

## 3. Escalation dispositions (E1–E6)

**E1 — Firmware ruling: ACCEPT the in-lane ruling (freeze as-shipped 7.4.5.0/v13; no reflash).** The lane did the right thing empirically: it READ firmware before reflashing (the runbook's own Step-4 conditional), found `7.4.5.0/v13` — **which satisfies the RATIFIED D-OPEN-1 target "EZSP v13+ / EmberZNet 7.4+"** — and so correctly did not reflash (the reflash mandate's premise, factory 8.0.2/v14 + the `ASH_ERROR_TIMEOUT` cluster, was measured-false). This is exemplary "verify the premise before acting on the mandate" discipline. **Forward-looking requirement (Nick's scalability directive):** the M9 acceptance baseline is now pinned to this stick's 7.4.5.0/v13, but **ship-firmware is batch-dependent** — so M9 acceptance must be **firmware-version-AWARE**: tolerate the ratified range (v13+), read the version at stack-init (not the HA registry, which reported null — E6), and keep the reflash-and-re-anchor contingency for a batch that ships 8.0.2. Close Doc 08 §3.3's ESC-W1-COORD-01 "above-ceiling" concern for this unit. → *PM-resolvable; a Doc 08 §3.3 currency note + an M9 acceptance requirement.*

**E2 — INV-CE-04 auto-detect correction: ACCEPT + route to Doc 08 §3.3.** The real stick's USB descriptor is SONOFF-branded, not the assumed `Silicon_Labs_CP2102N`. **M9 coordinator auto-detect MUST key on VID:PID (`10c4:ea60`) + the Doc 08 §3.3 probe sequence (stack-version disambiguates MG21/MG24), never descriptor strings.** This is a real "silicon breaks the assumption" find that would have caused an M9 auto-detect bug — caught pre-M9. → *Route as a measured-backed Doc 08 §3.3 currency correction (bundle with the AMD-CAND governance pass); a hard M9 acceptance requirement.*

**E3 — Full-color GAP (ESC-W1-HUE-01), now measured-backed: this IS AMD-CAND-2/3 — Nick's staged call.** The bench measured the GAP is real (`color_capabilities=31`, live hue/sat/XY on the hero bulb) + the color-temp canonical-unit drift (mireds-at-query vs Kelvin-at-ingestion). These map exactly onto the **already-staged AMD-CAND-2** (scope color to white/CT for V1 — hub rec, option A) **+ AMD-CAND-3** (Kelvin-canonical-at-ingestion) — pre-drafted with verbatim diffs, commit-on-Nick's-word. **The hero white/CT path is unblocked; color is a deliberate post-MVP scope call.** → *Nick rules the staged AMD-CAND-2/3 (now measured-backed); fold before M9 builds CT/color. Also fixes the Doc 02 §3.10-vs-§3.6 internal inconsistency the bench re-confirmed.*

**E4 — SNZB-03P dual-cluster (ESC-W1-SNZB03P-01 upgraded): ACCEPT; M9 acceptance requirement.** The P-variant carries Occupancy `0x0406` AND enrolled IAS Zone `0x0500` (zone_type 13), but the **measured active path is Occupancy attribute reports only** (zero IAS notifications in the walk-test). **M9 must bind `occupancy.occupied` and TOLERATE-not-require IAS enrollment.** The corpus is already corrected. → *An M9 acceptance requirement (feeds the SNZB-03P acceptance spec); no governance change.*

**E5 — Confirmation-engine caveats: the convergence point — route to the AMD-CAND-1 RATIFY pass + M9 acceptance + the frontend hero.** These are the richest finds, and they **triangulate with the AMD-CAND-1 shape review (B1) I ran earlier**:
  - **The measured values** (5 Hue blocks + SNZB empty) → fold at AMD-CAND-1 ratify (the values the shape review said would fold at ratify).
  - **Taxonomy convergence (E5-#5 ⇄ B1):** the bench MEASURED exactly the distinction the B1 reviewer flagged — "no authoritative attribute" (identify, strict access:2 → UNCONFIRMABLE) vs "attribute exists but is never reported" (effect `color_loop_active` — readable, never reported → readback-BEST_EFFORT). **AMD-CAND-1's field set should be refined at ratify to carry the split**, plus B1's `degradeRule`-as-enum and the new "a DISABLED/UNCONFIRMABLE command never renders CONFIRMED" invariant (B1). **Per-capability `recommendedTimeoutMs` is now measured-validated** (OnOff/Level ~0.5 s vs CT ~7–8 s on the SAME device — the per-capability block is a measured necessity, not a nicety).
  - **Engine-behavior caveats → M9 acceptance + Doc 02 §3.8:** idempotent/no-change ⇒ confirm-from-cache-or-readback (#1); TOLERANCE confirms the *settled* value, not the transient (#2); superseded/coalesced commands must **expire** (not false-fail, not false-confirm) (#6); sensor-side **dedup** (every SNZB event ×2) + **silent re-trigger** (occupied-window extension emits nothing).
  → *This is the M9 confirmation-engine's real spec. Route E5 into the AMD-CAND-1 ratify (values + taxonomy + B1 edits) + the M9 acceptance spec + the frontend hero rendering (§5).* 

**E6 — Minor: ACCEPT (informational).** HA registry `sw_version=null` → read firmware at stack-init, not the registry (folds into E1's version-aware requirement). Poor HA per-device-diagnostics UX → a validating data point for OUR dashboard's value prop (record it). Docker pre-installed → resolved in-lane.

## 4. M9-readiness (the critical path advancing)

M9's two pre-reqs were the bench Wave-1 corpus + AMD-CAND-1 ratified; AB-4 (the trust-hygiene hard-order) is ✅ DONE.

- **Pre-req 1 — bench Wave-1 corpus: DELIVERED** (coordinator + 2 device entries + confirmation blocks + fixtures + the caveats). This is M9's interview/codec + confirmation-acceptance spec + the replay-gate substrate.
- **Pre-req 2 — AMD-CAND-1: READY FOR NICK'S RATIFY.** The shape review (B1) is done (RATIFY-WITH-EDITS); the measured values are in hand; the taxonomy refinement is triangulated (E5 ⇄ B1). One ratify pass folds: the B1 edits (enum degradeRule, field-count clarity, the read-API-subset wording fix, the AMD-96 numbering) + the measured values + the taxonomy split + the new never-false-CONFIRMED invariant.
- **Sizing: M9 is SMALL** (D5 answered — Wave-1 adapter + codec, no curated-subset fallback).
- **New measured acceptance requirements:** auto-detect on VID:PID+probe (E2); firmware-version-aware, tolerate v13+ (E1); SNZB Occupancy-path, tolerate-not-require IAS (E4); the confirmation-engine behaviors (E5).

**So: once Nick ratifies AMD-CAND-1 (with the folds), M9 authoring can proceed against the measured bench corpus.** That is the next Core slot.

## 5. Frontend convergence (verified against git — the appendix was accurate)

The frontend build lane moved fast (commits `7b9680c`/`829bb86`/`ca91e74`) and **folded the PM-assessment gaps** (verified in source; the a11y test even cites "amendment G6"): DTCG-generated token source (G2/D-FE-8), dark-default (D-FE-1), self-hosted Inter subset (G5/D-FE-10), i18n-keyed copy + `BRAND` token (G3), axe-core a11y gate (G6), the T1.2 scenario engine + first-class offline state, `FE1_GO_LIVE.md`. **FE-1 (live-integration) is "hours, not a build."** Backlogged (correctly): mobile-first hero, PWA, list-virtualization (my G1/G4) + the per-view state matrix + the both-theme WCAG re-verify.

**The cross-lane route (do this):** the E5 measured semantics must reach the hero so it renders honestly — **CT confirms in 6.7–8.4 s** (the pending→confirmed transition is legitimately slow for color; the UI must not time out early — up to a 15 s CT window); **idempotent/no-change commands may never visually "confirm" without readback** (the UI needs the confirm-from-cache path or a distinct honest state); **effect/identify render UNCONFIRMED immediately** (never a false CONFIRMED, never a forever-spinner); superseded commands expire. Route these to the frontend lane **alongside AMD-CAND-1** (they are the same measured truth).

## 6. Go/No-Go read (mid-Aug) — materially improved

- **Gate 1 (engine LIVE):** ✅ done.
- **Gate 2 (hero on real data):** read-API ✅ + frontend go-live-ready (FE-1 hours) + **the bench delivered the real-data substrate**. The hero can render on running Core (seeded/replayed) now; on real-device-confirmed data once M9 lands. **Much closer.**
- **Gate 3 (hardware validating):** bench first-light ✅; M9 nearly unblocked + sized small; then the 72 h soak (queued, bench frozen). **Big progress.**
- **Gate 4 (install proven):** unchanged (install-smoke green — Nick's residual).
- **Both pacing risks retired for Wave-1:** frontend velocity (further-along-than-thought + go-live-ready) and M9 size (small per D5).

## 7. Next steps + what's Nick's

- **Nick (strategic):** (1) **ratify AMD-CAND-1** with the folds (B1 edits + the measured values + the E5 taxonomy split + the new invariant) — this unblocks M9; (2) **rule AMD-CAND-2/3** (the now-measured-backed color scope — recommend co-sign as staged: white/CT for V1 + Kelvin-canonical); (3) give the **M9 go** once (1) lands; (4) the standing residuals (CI-green glance, Dependabot, install-smoke).
- **Hub (me):** on Nick's ratify, author M9 against the measured corpus (the grounding-subagent-before-authoring discipline); route the E5 rendering semantics to the frontend lane; route the E2 Doc-08 §3.3 correction into the governance pass; queue the 72 h soak.
- **Spine reconciliation HELD:** the bench return, the frontend progress, the plan + both assessments, the two session prompts, and the AMD-CAND-1 readiness all need reconciling into the spine + committing — **held until the truncated-tail phantom goes quiescent** (active this session; VM git garbled). I'll reconcile + commit as one v12 beat the moment it clears.

**Net: the single highest-leverage block delivered clean; the moat is measured; the frontend converged; M9 is one ratify away. This is the best possible state for the mid-Aug go/no-go.**

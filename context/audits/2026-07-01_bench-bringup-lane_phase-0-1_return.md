<!--
file: context/audits/2026-07-01_bench-bringup-lane_phase-0-1_return.md
purpose: Bench bring-up lane (Stream A) return to the PM hub — Phase 0 (make-the-instrument) + Phase 1 (first-light) COMPLETE in one session 2026-07-01. The moat measured, the fixtures captured, the escalations enumerated. Includes a read-only frontend status-quo reconnaissance appendix requested by Nick for hub context.
audience: the PM hub (reconciles into the spine + Doc 02/08 governance); Nick (relayed this).
state-type: lane return (bench lane; write-isolated — this file + nexsys-bench/** only).
status: RETURNED 2026-07-01. nexsys-bench pushed: 2c0a33c → 5ceff3b.
anchors: nexsys-bench/docs/2026-07-01_phase-0-1_bringup-report.md (the full step-by-step record) · nexsys-bench/corpus/{coordinators,devices}/ (entries ✓) · nexsys-bench/fixtures/ (2 replayable event-stream fixtures) · nexsys-bench/corpus/raw/ (4 HA-redacted diagnostics)
-->

# Bench Lane Return — Phase 0 + Phase 1 first-light COMPLETE (2026-07-01)

## TL;DR

One evening, the full arc: **the instrument is built, verified, and frozen** (Pi 5 wired/radio-off, Docker-on-NVMe, `/dev/zigbee` pinned + autosuspend-off, coordinator on recorded firmware, ZHA live and cross-verified) and **first-light is captured**: both Wave-1 devices interviewed quirkless, **the moat measured on real silicon** — a real Hue renders a true `CONFIRMED` via unsolicited authoritative reports (0.3–0.7 s for on_off/brightness, 6.7–8.4 s for CT), and write-only paths render an honest `UNCONFIRMED` (never a false positive) — plus the hero motion fixture (9 timed cycles). Two git-native replayable fixtures + four raw diagnostics + the full report are pushed (`nexsys-bench` 5ceff3b). **The differentiator is now measured fact with a regression substrate, not a design claim.**

## 1. The return contract deliverables (dispatch §6)

- **Coordinator corpus entry ✓** (`corpus/coordinators/sonoff-dongle-plus-mg24_efr32mg24_ezsp.md`): VID:PID `10c4:ea60`, EFR32MG24, **frozen firmware EmberZNet 7.4.5.0 build 0 / EZSP v13 (as-shipped — see escalation E1)**, SONOFF-branded USB descriptor (see E2), ZHA/bellows 0.49.2 verification, channel 20 / PAN 0x994E.
- **Device corpus entries ✓** with measured confirmation blocks:
  - **Hue LCA017** (variant resolved; mfrCode 0x100B): interview confirms EP 11 / 0x010D + predicted clusters, plus measured deltas (Touchlink 0x1000, Philips 0xFC01/0xFC04, color-loop capability bit). **5 confirmation blocks** (on_off / brightness / color_temperature `CONFIRMABLE` with measured latencies + per-capability timeouts; effect + identify `UNCONFIRMABLE`) + **6 measured engine caveats** (E5).
  - **SNZB-03P** (mfrCode 0x1286 fills the `[CONFIRM-ON-BENCH]`): **dual-cluster surprise** (E4) — Occupancy 0x0406 AND enrolled IAS Zone 0x0500 + Poll Control + eWeLink 0xFC57; empty confirmation block (read-only); its value is the fixture.
- **Replayable fixtures** (`fixtures/`, event-log JSON, R1 raw-faithful): the SNZB-03P motion walk-test (9 detect/clear cycles, operator-timed to :00 wall-clock boundaries) and the Hue confirmation windows (all command→ACK→report tuples incl. the honesty proofs). Harness cross-validation pending Phase 2 (R4) — fixtures marked ZHA-sourced.
- **The Phase-0+1 report**: `nexsys-bench/docs/2026-07-01_phase-0-1_bringup-report.md` — every step's done-when verified and recorded, every capture anchored to the frozen firmware.

## 2. The three first-light payoffs (dispatch §4)

1. **The moat, measured.** True `CONFIRMED` exists: unsolicited `Report_Attributes` of the authoritative attribute after command (on_off 293–701 ms n=4; brightness 353–686 ms n=9; CT 6.7–8.4 s n=2+1). Honest `UNCONFIRMED` exists: effect (`color_loop_set`) and `identify` ACK SUCCESS then never report. The fixtures replay both.
2. **D5 re-open trigger ANSWERED: the `exposes`→capability map is MODEST on real silicon.** Both devices interviewed with `quirk_applied=False` on the pure generic zigpy path, zero interview failures, manufacturer-specific clusters ignored gracefully. Keeps M9 small; the curated-subset fallback is not needed for Wave-1.
3. **AMD-CAND-1 measured values delivered** for the governance fold: the confirmation blocks + the caveat set below.

## 3. Escalations (hub dispositions needed; this lane wrote no spine/doc/Core)

- **E1 — Firmware ruling (Nick, in-lane) + order-hold deviation flag.** The stick shipped **7.4.5.0/EZSP v13**, not the assumed factory 8.0.2/v14 `ASH_ERROR_TIMEOUT` cluster — the reflash mandate's premise was measured-false. Ruled: **freeze as-shipped; no reflash**; M9 acceptance baseline = 7.4.5.0/v13; contingency = reflash + re-anchor on any ASH instability. Doc 08 §3.3's ESC-W1-COORD-01 "above-ceiling" concern does not apply to this unit; note ship-firmware is batch-dependent.
- **E2 — INV-CE-04 correction.** USB descriptor strings are SONOFF-branded, not `Silicon_Labs_CP2102N` — auto-detect must key on VID:PID + the §3.3 probe sequence (stack version disambiguates MG21/MG24), never descriptor strings.
- **E3 — ESC-W1-HUE-01 (full-color GAP) now measured-backed.** `color_capabilities=31` with live hue/sat/XY values on the hero bulb. Disposition (scope-to-CT vs pull-color-forward) remains open with the hub + Nick.
- **E4 — ESC-W1-SNZB03P-01 UPGRADED: dual-cluster hero trigger.** The P-variant carries Occupancy AND IAS Zone (zone_type 13, ZHA-enrolled during interview). **Measured active path = Occupancy attribute reports ONLY** (zero IAS notifications in the walk-test) → hero binds `occupancy.occupied`; M9 must tolerate-not-require IAS enrollment; the corpus claim "IAS not exercised by Wave-1" is corrected.
- **E5 — Confirmation-engine caveats (→ AMD-CAND-1 / Doc 02 §3.8):** (1) no-change⇒no-report — idempotent commands need cache/readback confirm; (2) transition transients — confirm the settled value; (3) per-cluster posture split on ONE device — per-capability timeouts are measured necessity; (4) ±1-mired CT drift — TOLERANCE validated over EXACT_MATCH; (5) "never-reported ≠ no-attribute" — taxonomy sub-case split recommended; (6) superseded-command expiry — coalesced commands never confirm. Sensor-side: **silent re-trigger** (occupied-window extension emits nothing) and **duplicate reports** (every SNZB event ×2, consecutive TSNs — ingestion must dedup).
- **E6 — Minor:** HA registry `sw_version=null` for the coordinator (read firmware via diagnostics); per-device diagnostics discoverability is poor HA UX — an observability data point for OUR dashboard; Docker was pre-installed vs the recorded baseline (resolved — data-root re-pointed pre-pull).

## 4. Standing-lane state + queued backlog

The bench is **frozen** (no upgrades/reflashes; HA stays up; the on-Pi debug log holds the raw frames until the harness re-captures). Queued: **Z2M `exposes` cross-check** (D5's second oracle; compose profile stubbed; HA stopped first — single-owner), **72 h stability soak**, **thin zigpy/bellows harness** (Phase 2, post-Stream-B; cross-validate against today's ZHA captures per R4). Wave-2 devices when they arrive.

---

## Appendix — Frontend (Web-UI lane) status-quo reconnaissance (read-only, for hub context; requested by Nick)

Surveyed from `homesynapse-core/web-ui/dashboard/` (MODULE_CONTEXT, FE1_GO_LIVE, git log) + the 06-29/06-30 frontend lane returns. This is recon, not a frontend-lane return.

**State: far from neglected — it is the most swap-ready lane in the project.** Since first beat 2026-06-26:

- **Built + gated:** Preact 10 + Vite + TS SPA against the **FROZEN v1.1 read-API contract** (mirrored field-for-field in `contract.ts`); bundle ~22–26 KB vs the 100 KB hard-fail budget; **`frontend.yml` activated as the CI gate of record** (core commit `dbb0109`); generated DTCG design tokens (never hand-edited), dark-default theming, self-hosted Inter subset, name-light/i18n-keyed copy.
- **T1.2 scenario engine (the keystone):** every contract value (all outcomes incl. honest `UNCONFIRMED`, all origins, all four non-firing verdicts, cascades, 300/500-row lists, empty) and every transport condition (503-replaying/offline/slow/401/403/ETag-304) is one click via the mock-only DevPanel; every scenario contract-validated in CI; offline is a first-class honest state; axe-core a11y suite gates structurally.
- **T1.3 done — go-live is hours, not a build:** `realTransport` audited against contract §0 (bearer/401/403/503-backoff/ETag/RFC-9457/cursor-echo/poll-on-viewPosition all ✅); `FE1_GO_LIVE.md` is the one-sitting checklist. Core-side, M7.5a/b landed the B3 endpoints (runs/causal-chain/non-firing/automations) — real; `/events`+`/health` await M7.5c.
- **Known gaps (all recorded, none structural):** cursor-follow pagination + list virtualization (T2.3); optional dev-runtime response validation; ETag-cache cap; `problem+json` Accept; finish the T1.1/FE-4 state matrix per-view; WCAG 2.2 AA re-verify in both themes + screen-reader pass + mobile-first hero; then FE-PWA → FE-5. Contract gap candidate: no entity display-name field (raised in its lane return).
- **Bench-relevant unblocks (the cross-lane news):** FE-7 (real-device confirm) and the mid-Aug "hero on real data" gate were **blocked on hardware — the bench first-light just delivered that substrate.** Today's measured confirmation semantics also ground the UI's honest-state rendering: per-capability confirm latencies (CT ~7–8 s means the UI's pending→confirmed transition is legitimately slow for color), no-change⇒no-report (idempotent commands may never "confirm" visually without readback), and the `UNCONFIRMED`-immediately paths (effect/identify) that the explainability hero must render honestly. Recommend the hub route these to the frontend lane alongside AMD-CAND-1.

<!--
file: context/audits/2026-08-20_midweek-FE-deploy_sitting-record.md
purpose: THE H8 TIER-2 RECORD OF RECORD for the NEW-2/NEW-3 surfaces — the midweek FE-deploy sitting (Thu 2026-08-20 evening, Nick, per context/handoff/2026-08-17_midweek-FE-deploy_operator-packet.md as GO-ruled at v54 beat 4 with the two adjudications). The recorded real-wire exercise that flips the FE surfaces REPO-COMPLETE → VERIFIED-LIVE, with every residual named (H7: nothing rounded up). Filed by the hub from Nick's ⏺ pastes + DevTools screenshots (law 11 — chat is not a storage tier); the screenshots themselves remain session-held; every load-bearing fact from them is transcribed here.
audience: the hub (H8 accounting; the FE doctrine); the FE lane (F-S2/F-S3 knowledge); Nick.
state-type: audit / instrument record.
filed: 2026-08-20 (v54 hub, beat 5 — filing-day convention).
-->

# Midweek FE-Deploy Sitting — Record + the H8 Flip (Thu 2026-08-20 evening)

## §1 The blocks (all floors green; the deploy proven)

- **Block 0 floor:** `[PASS] boot-health — 6/6 positive · 0 forbidden`, bundle `boot-health-20260820T230135Z` (19:01 ET boot).
- **Block 1 pin:** Pi HEAD `3723e31` (`PREV` captured) — identified at the object at beat 4 (PR #3 dependabot, lockfile-only, retro-banked).
- **Block 2:** ff pull `3723e31..c091f7c` (23 files — the NEW-2/3 set + the B′/MC-fold span, all five known commits); `BUILD SUCCESSFUL in 31s`, npm tasks fired, **NEW bundle `index-C95CAnmp.js`** (supersedes the incident bundle `index-B9CmxYDm.js` — expected; the code changed).
- **Block 3:** lawful boot glance (relinked ×6 · rehydrated=6 · zero permit-join · projection_live 6/6 position=25065 · ch20/0x774c · RADIO UP 13 s) + `[PASS]` floor, bundle `boot-health-20260820T230935Z`. **THE DEPLOY IS PROVEN — the Pi runs `c091f7c`.**
- **Blocks 4–5:** tunnel + AuthGate + token entered (see F-S1); ~70 min of live browsing with DevTools open throughout.
- **Block 6 close floor:** `[PASS] 6/6 · 0 forbidden`, bundle `boot-health-20260821T002428Z` (20:24 ET).

## §2 The §8 rows, adjudicated

| Row | Verdict | Evidence |
|---|---|---|
| 1 — why-not surface | **PASS-BY-EXERCISE** | 6× `GET /api/v1/automations/01M0GPZFVANYA5TZMZSXRCV063/non-firing` → **200 OK** (+1 lawful 304) across ~19 min of polling; ZERO `can't access property "at"` / uncaught TypeError console entries the entire sitting (operator testimony + console screenshots: the only errors all session were the two expected /events 404s); no eternal spinner. The pill-level screenshot was not captured — the incident signature is proven ABSENT, which is the row's point. |
| 2 — non-firing body arm | **PASS-AT-HEADERS** (body size-inferred) | 200s at 396 B with ascending `X-HomeSynapse-View-Position` (104218 → 104221 → 104223; ETags advancing) — live data flowing; 396 B matches the null-arm shape class (the 2026-08-16 fixture body was 395 B). The strict Response-tab readout was not captured — the one-ask below covers it. Either arm renders by construction (fixture-pinned both ways); no render failure occurred. |
| 3 — device card prose/stamp agreement | **PASS-AS-DEGRADED-HONEST** + **F-S2** | The Devices list rendered honestly (5 Available · the dead Hue **Offline** — F2's fix live again); the device detail fields showed honest absence ("all blank") — see F-S2: this is FE-STATE-DIALECT, the documented expected class, NOT a defect. No bare clock time, no 1970-plausible time anywhere — the falsifiers are dead. |
| 4 — >24 h date-qualified stamps | **PARTIAL-EXERCISED** (not blocking) | The runs list rendered relative stamps correctly (22 min → 14 days); the run DETAIL opened was the fresh 19:00 run, whose bare "7:00 PM" is CORRECT (≤24 h). The >24 h detail arm was not visually captured; it is fixture-locked (181/181) and the list corroborates. |
| 5 — /events honest 404 | **PASS**; **the NEW-7 capture stays OPEN** | The calm "Endpoint GET /api/v1/events not found" card + Try again, unchanged posture; console shows exactly the two expected 404 XHRs. The raw 404 RESPONSE BODY was not copied — the one-ask below. |
| 6 — Updated-stamp ticking | **PASS** (+ F-S3 note) | Devices "35 sec ago" · runs list "24 sec ago" · ● Live footer on every capture — the poll loop alive across surfaces (the 2026-07-27 frozen-stamp signature ABSENT). The run-DETAIL page read "3 min ago" after ~3 min on-page — see F-S3 (fetch-once-by-design question; benign). |

## §3 Findings (banked)

- **F-S1 — L3 EXTENDS TO SCREENSHOTS (process finding + remediation REC):** the DevTools request-header screenshots pasted to the hub carry the `Authorization: Bearer …` pairing token verbatim — the packet's L3 contemplated ⏺ text pastes, not header captures. Exposure scope: this session only; the surface is loopback-only behind the tunnel. **REC (cheap, standing): re-mint the pairing token at the next Pi touch** — delete the token file and restart mints a fresh one (`rm /home/homesynapse/hs-bench/config/initial_api_token` on the Pi, then `~/bench.sh restart`, then the browser re-pairs; ride it into Saturday's restore block or any daytime moment). **The law fold: screenshots of request headers are token-carriers — crop or mask the Authorization line before pasting** (rides the operator-packet class; carrier at the next skills/packet touch).
- **F-S2 — THE STATE-DIALECT LIVE OBSERVATION (Nick's "blank fields" report, SOLVED — expected-class, zero defect):** the 19:00 hand-wave DID reach the system (proof: bench-hero triggered at 7:00 PM on that entity's change — §4), but the device drawer's fields rendered blank/absent afterward. This is **FE-STATE-DIALECT working as shipped**: the live `/state` wire serves epoch-second NUMBERS; the NEW-3-hardened client refuses to coerce non-string instants (the 1970-misread class is closed) and renders honest absence instead — "the drawer stays honestly degraded until charter item (h) + the core half land" (FE return §7 ask 3, verbatim). **The falsifier would have been a 1970 timestamp; blank IS the fix.** Charter consequence: the R-10 re-rank case for FE-STATE-DIALECT just gained its first live operator observation — the largest visible demo-surface gap, now experienced first-hand.
- **F-S3 — the run-detail stamp (benign note → FE lane knowledge):** the run-detail view's "Updated" stamp aged to 3 min while list views ticked at ~30 s — consistent with fetch-once-on-load for historical run details (a reasonable design; historical runs are immutable). One-line FE confirmation wanted at the next FE touch: is detail-view fetch-once by design? If yes, the stamp label could say "Loaded" — a copy nit, not a defect.
- **F-S4 — THE LIVE END-TO-END EXHIBIT (unplanned; bank it):** at ~19:00 Nick waved at the motion sensor; within the minute bench-hero triggered on that entity's state change, ran its 9 steps, and the explain surface rendered the complete honest verdict — *"bench-hero ran when 01KX1PB9… changed at 7:00 PM, but nothing was changed"* · StateChangeTrigger disclosure · the do-nothing class (*"all 9 planned steps ended without sending a command"* + the skip explanation + the not-kept-yet honesty line) · *"Finished in 34.1s"* · ⚠ Completed-nothing-changed · the permanent-log coda — **a real hand-wave to a rendered, honest causal explanation on real hardware, same-minute, on the deployed v1.1.2 wire.** Internal exhibit only; every external use stays claim-fenced (D-1/D5 as always).

## §4 THE H8 FLIP

**The NEW-2/NEW-3 surfaces are VERIFIED-LIVE** (H8: one recorded real-wire exercise — this record). Named residuals, none blocking, honestly carried: (1) the NEW-7 404-body capture OPEN (one-ask outstanding); (2) row-2's strict body readout size-inferred (same one-ask); (3) row-4's >24 h detail arm fixture-covered, not visually re-exercised. The eternal-spinner class, the 1970 class, the frozen-stamp class, and the uncaught-render-crash class were all exercised against live wire and none fired. The FE return's REPO-COMPLETE/LIVE-VERIFICATION-PENDING register is SUPERSEDED BY THIS RECORD (pointer-not-copy; the return file stands unedited).

## §5 The one enrichment ask (once; declining closes it)

Two Response-tab copies, ~60 seconds total, next time the tunnel is up: (a) the `GET /api/v1/events` **404 response body** (the NEW-7 (d)→(a) input); (b) any one `…/non-firing` **200 response body** (closes row 2's strict arm). Paste both as text (bodies carry no token).

<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-08-26 (v57 hub, beat 1 — THE LAUNCH (Wed): zero drift; the beat-6 order found UN-RUN → OVERTAKEN into one combined order; W-SKILLS-4 UN-RUN (law 37) → re-dispatched; P6 EXECUTED (coder-lessons 39,777 → 15,105 B, zero loss); the R-3a packet + WU-R3 authored ahead. Order: hivemind 8. Detail: pm-handoff beat 1.) Prior: 2026-08-23 (v56 hub, beat 6 — THE CLOSE: R-7b LANDED dec35be, CI GREEN ×3; the R-7/R-7b arc CLOSES; v57 BANKED (P5). Order: hivemind 3 — never run; folded into v57 beat 1. Detail: pm-handoff beat 6.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md (rotated v56 beat 4); segments that roll off this 2-segment chain remain in the pm-handoff `:8` chain and its archive; earlier eras per context/status/archive/.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v57 beat 1 — Wed 2026-08-26)

**HEADs:** core **`dec35be`** CLEAN (R-7b landed; CI GREEN ×3; the run-detail harvest — run id + the `sha256` echo line — rides Nick's paste into the R-3a packet's one open slot) · hivemind `6b7d357` + the beat-1 COMBINED order OUT (8 = 3 M + 5 A: the v56 close + this beat) · skills `5105abc` · bench `4539f13` · docs `a53f474`. **NOTHING touches the core checkout until R-3b.**

**Closed:** R-1/R-2 (code+CI+HARDWARE) · R-6/R-8 · R-7 · R-7b (R-V live) · R-9 · W-HIVE-1 · **P6** (coder-lessons rotated by count; live 15,105 B). **Bench:** floor 8/9 · 0.28s; §OP-A/H green (12:11–12:16 CT = 13:11–13:16 ET). **Held card:** OUT, `hs-fresh — R-3/R-4 rig — 7c9e4fa`, UNPATCHED (F-S12), token PRESENT 44 B 644 (F-S9/F-S10), own radio-less `data/zigbee/` PRESENT (F-S11). **P-1 banked** (02P LIVE — A0 GREEN).

**Authored ahead:** `context/handoff/2026-08-26_R3a_rehearsal_operator-packet.md` (PRINT-READY pending the run-id/sha256 slot; every v56 fold in; rows ≥ not "unchanged") · `context/pre-verifications/WU-R3.md` (P1–P11 at dec35be) · H12 filed: `hs_version=0.1.0+git20260823.231355.gdec35be`.

**Fences:** the D-1 DO-NOT-SAY pair until R-4 · `distribution/README.md:117` until W2-3 · no public brand use before G-2 · s31 legs/nightly HANDS OFF until R-5 · the hub never implements · ONE COORDINATOR, ONE BOOT (the R-3a §2/§8 fence).

**Next:** TODAY — Nick: the combined commit (8) · the W-SKILLS-4 paste (+ FE-SWAP-GATE) · the 2-min run-detail glance; the hub: beat 2 = the skills census audit. **Wed/Thu: PELTON → the word → same-day** (`…v57_orchestrator_session_prompt.md` §4). Sat R-3a (the packet) → the record + R-3b authored. Sun R-3b → R-4 → **THE FENCE LIFT**. Aug-31 RS-3. Plan: `context/planning/2026-08-23_pelton-week_plan-of-record.md`.

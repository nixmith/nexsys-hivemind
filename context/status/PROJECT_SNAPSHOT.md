<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-08-27 (v57 hub, beat 2 — beat 1 LANDED 25e6922 (8-exact); W-SKILLS-4 AUDITED ACCEPT (60/60 · 33/33; mirrors 23/23 synced); FE-SWAP-GATE VALIDATED ACCEPT (the flip = 3 M); the dec35be run detail BANKED (H12 exact); the R-3a packet PRINT-READY; the program to Sunday. Orders: core 2 · hivemind 14. Detail: pm-handoff beat 2.) Prior: 2026-08-26 (v57 hub, beat 1 — THE LAUNCH (Wed): zero drift; the beat-6 order found UN-RUN → OVERTAKEN into one combined order; W-SKILLS-4 UN-RUN (law 37) → re-dispatched; P6 EXECUTED; the R-3a packet + WU-R3 authored ahead. Order: hivemind 8. Detail: pm-handoff beat 1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments live in the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v57 beat 2 — Thu 2026-08-27)

**HEADs:** core **`dec35be`** + the FE-SWAP-GATE order OUT (2 = 1 M + 1 A under `web-ui/`; CI predictions filed: Frontend CI 211/211 · Build & Check green · install-smoke not triggered) · hivemind `25e6922` + the beat-2 order OUT (14 = 9 M + 5 A: the skills pass + both returns + the audit + the spine) · skills `5105abc` (FE tree 0-byte) · bench `4539f13` · docs `a53f474`. **NOTHING else touches the core checkout until R-3b.**

**Closed:** R-1/R-2 (code+CI+HARDWARE) · R-6/R-8 · R-7 · R-7b · R-9 · W-HIVE-1 · P6 · **W-SKILLS-4** (PM 49,676 B; provenance → `references/pass-history.md`) · **FE-SWAP-GATE** (the rename is red-first; the flip = 3 M). **Banked:** the `dec35be` run `32672999145` — `hs_version=0.1.0+git20260823.231355.gdec35be` exact; the arm64 line pending Nick's paste. **Held card:** OUT, `hs-fresh — R-3/R-4 rig — 7c9e4fa`, UNPATCHED (F-S12). **Bench:** floor 8/9 · 0.28s.

**Ready:** `context/handoff/2026-08-26_R3a_rehearsal_operator-packet.md` PRINT-READY (Sat daylight) · `context/pre-verifications/WU-R3.md`. **Authoring next (hub beat 3):** R-3b ISSUE-READY-pending-measurement · the R-4 packet · the W-SKILLS-5 charter (post-R-4; harvest: `freshness-preflight.md` Check 2 is a standing false-STALE).

**Fences:** the D-1 DO-NOT-SAY pair until R-4 · `distribution/README.md:117` until W2-3 · no public brand use before G-2 · s31 legs/nightly HANDS OFF until R-5 · the hub never implements · ONE COORDINATOR, ONE BOOT.

**Next:** Thu — Nick: host verify → core 2 + CI read · hivemind 14 · Check 9 · the arm64 line + `.deb` to `~/r3-artifact`. **PELTON → the word → same-day** (v57 prompt §4; hardware time never traded for it). Sat R-3a → Sat-eve R-3b (host-side CC) → Sun R-4 on R-3b's CI artifact → **THE FENCE LIFT**. Aug-31 RS-3. Program: `_scratch/2026-08-27_v57-beat-2_operator-queue.md` §6.

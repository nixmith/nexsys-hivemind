<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-05 (v63 beat 2 — THE INTAKE + THE LANE DISPATCHED, Sat ~12:39 CT (17:39Z) — I-1 read: HeroLoop failed on four methods across #183/#206/#225, branch (a) confirmed; the census committed (redacted per TOKLEN-OK); FIX1: class · SAMPLES: veto-only · Row 33 written; the FIX-1 lane DISPATCHED (wait-state). Order: hivemind 8 = 7 M + 1 A. Detail: pm-handoff v63 beat 2.) Prior: 2026-09-04 (v63 beat 1 — THE v63 BOOT + THE INTAKE, Fri ~18:10 CT (23:10Z) — core dc3328b (PR #5 merged); main RED twice on identical Java bytes (ReplayTransitionIT:212 · HeroLoop:324; PR #5 green); four silent drop points at source; FAILCHAN-FIX-1 re-cut to the class, authored (A); the audit (A); the v63 brief (A). Order: hivemind 7 = 4 M + 3 A. Detail: pm-handoff v63 beat 1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v63 beat 2 — THE INTAKE + THE LANE DISPATCHED, Sat 2026-09-05 ~12:39 CT)

**v63 LIVE (beat 2). Core `dc3328b`; `main` RED on two runs of identical bytes (#225 `HeroLoop:324` · `dc3328b` `ReplayTransitionIT:212`; PR #5 green). The gate is OPEN — no core lane but FAILCHAN-FIX-1, which is DISPATCHED (Nick, 09-05 ~12:xx CT); wait-state: `context/audits/2026-09-05_FIX-1_return.md`.** I-1 read: HeroLoop failed on four methods across #183 (two at once), #206, #225 → branch (a) confirmed, pre-existing and method-agnostic; #169 a compile miss. Nick's words: `FIX1: class` · `SAMPLES: veto-only` · Row 33 written (cites verified at the records) · `PROTECT: dismissed` (de facto). The census committed (two test-token values redacted). The instruction: `context/instructions/2026-09-04_coder-lane_FAILCHAN-FIX-1_CI-nondeterminism_coding-instruction.md` (FIX-1a instruments → loops → FIX-1b; the push run's green clears, samples veto only). C-002 LIVE (STANDS). HEADs: hivemind = this beat (ahead 2).

**NOW (Nick, the brief §NOW/§QUEUE):** Act 3 · Act 10 the nightly · Act 5b optional · wait → `FIX-1 lane returned` → Act 7 (sample #4) → Act 8 (the gate + 3 samples) → Act 9 push · a word, no rush: `FENCE-BUS: add | hold`. **Hub:** beat 3 CG drafted → beat 4 THE BEYOND INPUT skeleton → the v64 skeleton → close on context health.

**OPEN RISKS:** six (OR-FAILCHAN CI RED, lane running · OR-BUS-SILENT-DROP). Erik Mon · E1 Mon · `EU` 09-11 · `Activate` 09-15 · the hard stop 09-18. Fences: no public brand use before the opinion · s31/nightly HANDS OFF until R-5 · one lane on the core tree · never a `main` re-run as clearance · the hub never implements.

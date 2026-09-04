<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-04 (v63 beat 1 — THE v63 BOOT + THE INTAKE, Fri ~18:10 CT (23:10Z) — core dc3328b (PR #5 merged); main RED twice on identical Java bytes (ReplayTransitionIT:212 · HeroLoop:324; PR #5 green); four silent drop points at source; FAILCHAN-FIX-1 re-cut to the class, authored (A); the audit (A); the v63 brief (A). Order: hivemind 7 = 4 M + 3 A. Detail: pm-handoff v63 beat 1.) Prior: 2026-09-04 (v62 beat 9 — POST-CLOSE, Fri ~17:12 CT (22:12Z) — the push banked (in sync at 204c5ba); the v63 dispatch prompt re-authored on Nick's ask (A); PR #5 + main protection ruled (rec: merge; protect (a) now, Row 34); I-0 found. Order: hivemind 7 = 6 M + 1 A. Detail: pm-handoff v62 beat 9.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v63 beat 1 — THE BOOT + THE INTAKE, Fri 2026-09-04 ~18:10 CT)

**v63 LIVE (beat 1). Core `dc3328b`** (PR #5 merged; Java bytes = `7af2d6c`). **`main` RED on two runs of identical bytes — #225 (`HeroLoop:324`, lifecycle) and `dc3328b` (`ReplayTransitionIT:212`, event-bus; lifecycle never reached, no `--continue`); PR #5's run GREEN** → non-determinism established (`8e6e0e1`'s parent is `7af2d6c`). **The gate is OPEN on `dc3328b` — no core lane but FAILCHAN-FIX-1.** At source: four silent drop points on the bus (`InProcessEventBus:250 :480 :487`, `TransitionCoordinator:100`); the §10-O hunk unreachable in driven mode; `ci.yml` uploads HTML only. **FAILCHAN-FIX-1 AUTHORED, re-cut to THE CLASS** (`context/instructions/2026-09-04_coder-lane_FAILCHAN-FIX-1_CI-nondeterminism_coding-instruction.md`): one lane, two commits — FIX-1a the instruments → the loops (≥60 runs) → FIX-1b the mechanism; the push run's green clears, dispatch samples veto only. The audit: `context/audits/2026-09-04_v63-b1_boot-grounding_executive-model-and-intake.md`. C-002 LIVE (STANDS). HEADs: hivemind = this beat (ahead 1); skills/bench/docs unchanged.

**NOW (Nick, the brief §QUEUE):** Act 1 the census file · 2 I-1 · 3 `dc3328b`'s message · 4 the four words · 5 dispatch FIX-1 · 9 push. **Hub:** CG drafted while the lane runs → THE BEYOND INPUT → the return's audit → FE → H8 → the addendum + docs block → P-1 + F-R4-1b → v64.

**OPEN RISKS:** six (OR-FAILCHAN CI RED · OR-BUS-SILENT-DROP new). Erik Mon · E1 Mon · `EU` 09-11 · `Activate` 09-15 · the hard stop 09-18. Fences: no public brand use before the opinion · s31/nightly HANDS OFF until R-5 · one lane on the core tree · never a `main` re-run as clearance · the hub never implements.

<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-12 (v72 beat 1, THE BOOT AND THE SAMPLE #15 READ — kind E (`NOTIFY_SKIPPED_LIVE`, `automation_engine`, position 206, checkpoint 207; census 254/254); the revert clock STOPPED; BUS-ORDER-1's gate met at `5f918c7`, §8 handed as the one act; the §6 exhibit in the docs tree; v70 b5–b9 rotated; Sat 2026-09-12 ~19:5x CT (2026-09-13T00:53Z). Order: hivemind 8 = 6 M + 2 A by explicit paths (computed from porcelain inside the splice); docs 1 M held. Detail: pm-handoff v72 beat 1.) Prior: 2026-09-12 (v71 beat 6, THE POST-CLOSE INTAKE — R3 corrected; core `5f918c7` LANDED, `check` GREEN = v1.1.4 FROZEN; the bus-soak job RED `anomalies=1` = sample #15, UNREAD (the one act: the artifact); hivemind `7addbc8`; v72 opens on the read, Sat 2026-09-12 ~18:5x CT (2026-09-12T23:55Z). Order: hivemind by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v71 beat 6.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v72 OPEN at beat 1 — sample #15 kind E; the clock stopped; BUS-ORDER-1's paste handed, Sat 2026-09-12 ~19:5x CT)

**State:** core `5f918c7` (`check` GREEN = v1.1.4 FROZEN; the `bus-soak` job RED = sample #15, READ: `NOTIFY_SKIPPED_LIVE` on `automation_engine` at position 206, checkpoint 207; census 254/254, no miss); hivemind `3209101` + b1; docs `0d62a54` + the AMD-101 §6 exhibit (1 M, held). **The bus class:** (1) the soak's stall — instrumented (`72efb42`); (2) the census's head-miss — a notify-order artefact on a non-monotonic checkpoint; kind E is the harmful arm, sample #15 its first line. **Ruled:** `BUSFIX: b` = BUS-ORDER-1 (AMD-101 PROPOSED); the gate met at `5f918c7`; the revert clock STOPPED at 1/10; dispatches on Nick's paste (`BUSORDER: go`). **v72's deliverable:** BUS-ORDER-1 running and its return audited against AMD-101 §2; then HERO-1c's charter → 114b → `AMD101: ratify` (the §4 edit + the §6 exhibit, one docs card) → the R-4c and H8-a intakes. **Owed:** `H8A:` · `R4C:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done`. Check 9 STALE (the known file).

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: kind E read; BUS-ORDER-1 dispatching; the closure counter restarts at its landing · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

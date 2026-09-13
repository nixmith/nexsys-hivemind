<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v73 beat 1, THE v73 BOOT AND INTAKE — both v72 cards verified at the bytes (bench `1201368` 3 A + 1 M; hivemind `7540662` 6 M + 2 A); the preflight 12/12 (Check 9 STALE by one file; Check 12 reconciled); the deliverable named (EXPLAIN-114b landed green); the splice library adopted; hivemind `7540662`; Sun 2026-09-13 ~13:5x CT (2026-09-13T18:58Z). Order: hivemind 7 = 5 M + 2 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 1.) Prior: 2026-09-13 (v72 beat 7, THE v72 CLOSE — P-1 RETURNED (bench 3 A + 1 M) and audited ACCEPT, the gate re-run on the device (19/0); Erik's PALOKI search started 09-13 (the fence extends past 09-18); the bench card and v73's dispatch line handed; hivemind `45f1bf3`; Sun 2026-09-13 ~13:2x CT (2026-09-13T18:22Z). Order: bench 4 = 3 A + 1 M by explicit paths (Nick's hands); hivemind 8 = 6 M + 2 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v72 beat 7.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v73 OPEN at beat 1 — both v72 cards landed; the preflight run; the deliverable: EXPLAIN-114b landed green on the Java domain, Sun 2026-09-13 ~13:5x CT)

**State:** core `a458a64` (CI green; the closure counter 1/20); hivemind `7540662` + b1 (the card); docs `2235845` + 1 M held (AMD-101's §6 run id); bench `1201368` (P-1 landed); skills `c630c5c`. **v73's blocks:** B1 the boot and intake (this) → B2 114b's instruction on the free Java domain → B3 HERO-1c's charter on `FE: 6af76f7` → B4 R-5's charter (the counterfactual window, the null-arm block, the re-seen/adopted split, the ULID audit, P-1's fold) → B5 H8-a's packet through THE PRIOR-LEDGER GATE on `H8:` → B6 the strategy fold by range → close ≤ b8. **Adopted:** `context/process/splice_lib_v1.py`. **Erik:** the PALOKI search started 09-13; the opinion is the wait-state; the fence extends past 09-18. **Owed:** `HIVE:` (b1) · `FE: 6af76f7` · `H8:` · `AMD100:` · `PROTECT: done` · `Activate:` 09-15. Check 9 STALE (one file; Nick's sync).

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 1/20 · ADOPT-AWAKE · four standing). Fences: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes.

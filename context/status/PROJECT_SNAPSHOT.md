<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v72 beat 7, THE v72 CLOSE — P-1 RETURNED (bench 3 A + 1 M) and audited ACCEPT, the gate re-run on the device (19/0); Erik's PALOKI search started 09-13 (the fence extends past 09-18); the bench card and v73's dispatch line handed; hivemind `45f1bf3`; Sun 2026-09-13 ~13:2x CT (2026-09-13T18:22Z). Order: bench 4 = 3 A + 1 M by explicit paths (Nick's hands); hivemind 8 = 6 M + 2 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v72 beat 7.) Prior: 2026-09-13 (v72 beat 6, R-4c RETURNED and audited at the bytes against the navigator's own attack list: C-003 MINTED-BOUNDED (adopted +122 s; the fleet six of six; the ZDO surface's necessity untested), F-R4c-A → OR-ADOPT-AWAKE, O-2 provisional, the null arm not banked; THE PRIOR-LEDGER GATE adopted; P-1's paste handed; seven blocks rotated; Sun 2026-09-13 ~10:3x CT (2026-09-13T15:34Z). Order: hivemind 13 = 8 M + 5 A by explicit paths (computed from porcelain inside the splice; the b5 files ride this card). Detail: pm-handoff v72 beat 6.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v72 CLOSED at beat 7 — BUS-ORDER-1 landed and ratified, R-4c's C-003 minted with a bound, P-1 returned; v73 opens on the v67 prompt, Sun 2026-09-13 ~13:2x CT)

**State:** core `a458a64` (CI green; the closure counter 1/20); hivemind `45f1bf3` + b7 (the card); docs `2235845` + 1 M held (AMD-101's §6 run id); bench `4539f13` + P-1's four files (the card). **This window:** sample #15 (kind E) → BUS-ORDER-1 landed `a458a64`, CI green → AMD-101 RATIFIED → the re-cut → R-4c (C-003 MINTED-BOUNDED; the fleet 6/6; OR-ADOPT-AWAKE; the null arm held) → P-1 returned (19/0). **Ruled:** THE PRIOR-LEDGER GATE; the B-2/B-3 design fence lifts with F-R4c-A as a constraint. **Erik:** the PALOKI search started 09-13; the opinion is the wait-state; the fence extends past 09-18. **v73 opens on:** 114b's instruction → R-5's charter (the counterfactual, the null-arm block, the re-seen/adopted split, the ULID audit, P-1's fold) → HERO-1c on `FE:` → H8-a on `H8:` → the strategy fold. **Owed:** `BENCH:` · `HIVE:` · `H8:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done` · `Activate:` 09-15. Check 9 STALE.

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 1/20 · ADOPT-AWAKE · four standing). Fences: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes.

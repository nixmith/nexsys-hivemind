<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-11 (v70 beat 2 — the `1e26912` red read at run 34650129654: no anomaly token anywhere; the motion edge in the store, ten silent seconds, no dispatch; P2 holds; FIX-2 opens with the instrument (IT diagnostic · TR-1b ITs · `bus-soak`); audit filed; beat 1 landed `89de5b3`; next b3 R-4c's packet, Fri 2026-09-11 ~18:0x CT (2026-09-11T23:02Z). Order: hivemind 5 = 4 M + 1 A (computed from porcelain inside the splice). Detail: pm-handoff v70 beat 2.) Prior: 2026-09-11 (v70 beat 1 — the v70 boot: HEADs clean, ahead 0; preflight 10 PASS + Check 9 STALE (the mirror) + Check 12 flipped (HERO-1 charter EXECUTED); Act 0's artifact verified (`_scratch/v70/ci-1e26912/`, sha `1e26912…`, 2026-09-11T21:35Z); the H8-a send re-armed on v70 (23:45Z), v69's deleted; the deliverable: R-4c's packet; next b2 the red read, Fri 2026-09-11 ~17:5x CT (2026-09-11T22:57Z). Order: hivemind 5 = 5 M + 0 A (computed from porcelain inside the splice). Detail: pm-handoff v70 beat 1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v70 beat 2 — the red read; FIX-2 instrument-first; H8-a at 19:00 CT; R-4c's packet next, Fri 2026-09-11 ~18:0x CT)

**State:** core `1e26912` (**`ci` RED, READ: no anomaly token, ten silent seconds, no dispatch — `context/audits/2026-09-11_CI-1e26912_red-read_HeroLoop-lifecycle_v70-b2.md`**); hivemind `89de5b3` + this beat (4 M + 1 A); both core slots free; EXPLAIN-114a behind FIX-2. **FIX-2 (next Java WU):** instrument-first (the IT's timeout diagnostic · TR-1b's ITs · `bus-soak`); the structural fix on their reading; instruction at b4. **The deliverable:** R-4c's packet (b3) for Saturday (measurement-only; the green install-smoke .deb; LASTREPORTED-1b and `card-gradle:` ride it; C-003 the exit). **Tonight:** H8-a 19:00 CT; the 18:45 paste by `trig_01UFmAs97CvSBzVXB6apVWLd`; the artifact `f25291b`. **Then:** HERO-1b (b5) → P-1 (b6). **HEADs:** core `1e26912` · docs `876a395` · skills `c630c5c` · bench `4539f13`. **Ruled:** `HERO1:` (a) ×7 · `EXPLAIN: three`. **Open:** `H8A:` · `FIX2:` · `PROTECT: done` · `R4C:` · `ERIK:` · `Activate:` 09-15. Check 9 STALE until the mirror sync.

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP #9 RED, read; FIX-2 instrument-first · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

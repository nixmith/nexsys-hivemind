<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-12 (v110 beat 2 — DRY-RUN-1 (Mon) INTAKEN; the window OPEN 20:03:53 CT; D2 Tue 20:04 CT; IR-148 sharpened; IR-188..191; D-v110-11..18; Mon 2026-10-12 ~20:5x CT (2026-10-13T01:54:34Z). Next: the b1 + b2 cards → HORIZON-1 → the close) Prior: 2026-10-12 (v110 beat 1 — `e6a7ecc`; BENCH-BOOT-1 INTAKEN ACCEPT; its landing card handed; the addendum filed; D-v110-1..9; Mon 2026-10-12 ~18:3x CT (2026-10-12T23:35:17Z). Next: `BENCH: LANDED` → dry-run #1 → the b1 card) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v110 b2 — v110 b2 — the dry-run window OPEN; D2 Tue 20:04 CT)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`6a40a10`** (BENCH-BOOT-1 LANDED Mon 18:36; BP10 `ceb08c5` beneath it; BC10 pulls it); docs **`e2a5844`**; skills `e9a77a8`; hivemind `e6a7ecc` (the b1 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **THE RENDERER** — `--check` at every boot. **J3 LANDED** `e11ae20` (T-A) · `176adad` (T-B), `CI: green` each; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 OPEN since Mon 20:03:53 CT** (the pre-warmed relaunch) · **D2 Tue 20:04 CT** → v111. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v110 b1–b2** — BENCH-BOOT-1 LANDED `6a40a10`; IR-185..191; `37f05a9`'s warm margin expires ≈ Oct 22 (the rollback target post-fix, D-v110-16); HORIZON-1 → b3. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–191 (46 · 95 · 119 CLOSED; 148 sharpened; 183 widened; 185–191 new) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b1 + b2 cards → `KIT-STORAGE:` → HORIZON-1 (b3) → D2 Tue 20:04 CT → v111.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..191 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

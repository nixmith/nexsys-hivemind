<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-17 (v112 beat 3 — BC10 INTAKEN ACCEPT: `176adad` up; IR-148 CLOSED (0.584 s cold); IR-220; HERO-U4 DISPATCH-READY; D-v112-13..18; Sat 2026-10-17 ~10:4x CT (2026-10-17T15:44:06Z). Next: the b3 card → HERO-U4) Prior: 2026-10-17 (v112 beat 2 — LICENSE-1 INTAKEN ACCEPT → the H10 (`LICENSE:` by Nov 2); BC10-F held; IR-217..219; D-v112-8..12; Sat 2026-10-17 ~07:5x CT (2026-10-17T12:54:26Z). Next: the b2 card → BC10 09:00) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v112 b3 — BC10 INTAKEN — `176adad` up; IR-148 CLOSED (0.584 s cold); HERO-U4 DISPATCH-READY)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; on the Pi since BC10); bench **`7e03c81`** (BP11 over GATE-2 `5cf3bd0`; on the Pi since BC10); docs **`e2a5844`**; skills `e9a77a8`; hivemind `ee20fe3` (b3 pending). **THE PI (hs-dev-1): `176adad` BY SHA since Sat 10:16:26 CT (BC10)** — bench `7e03c81`; SOAK-NIGHT-3 on `bench-2026-10-17-111625.log`. **BC10 DONE (v112 b3): `176adad` UP** — IR-148's after 0.584 s cold on 2.32 M events (bar 20.4 s); BACKUP-1 36 s, md5 both sides; DV-1 → IR-220. **SOAK-NIGHT-3 tonight** · Sun the rollback + BC9b · Tue PI-2 (the fresh image folded in) · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v112:** b1 BC10 re-stamped · b2 LICENSE-1 INTAKEN → `LICENSE:` by Nov 2 · b3 BC10 INTAKEN; HERO-U4 cut. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 CLOSED on the rig (v112 b3) · 149 · 153–220 (46 · 95 · 119 · 179 · 183 CLOSED; 185–220 new) · 56 CLOSED (v111 b1, sample 7) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b3 card → HERO-U4: the worktree card, then its paste · Sun the rollback + BC9b (the card tonight) · `KIT-ORDER:` · `N3:` by Oct 20.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..220 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

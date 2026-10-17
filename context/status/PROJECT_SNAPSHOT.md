<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-17 (v112 beat 4 — BC11 DISPATCH-READY (Sun): the rollback, second-checked; BC9b → PI-2; HERO-U4 RETURNED; D-v112-19..25; Sat 2026-10-17 ~14:4x CT (2026-10-17T19:42:13Z). Next: the b4 card → BC11) Prior: 2026-10-17 (v112 beat 3 — BC10 INTAKEN ACCEPT: `176adad` up; IR-148 CLOSED (0.584 s cold); IR-220; HERO-U4 DISPATCH-READY; D-v112-13..18; Sat 2026-10-17 ~10:4x CT (2026-10-17T15:44:06Z). Next: the b3 card → HERO-U4) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v112 b4 — BC11 DISPATCH-READY (Sun) — the rollback, second-checked; BC9b → PI-2; HERO-U4 RETURNED)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; on the Pi since BC10); bench **`7e03c81`** (BP11 over GATE-2 `5cf3bd0`; on the Pi since BC10); docs **`e2a5844`**; skills `e9a77a8`; hivemind `f9ab3ed` (b4 pending). **THE PI (hs-dev-1): `176adad` BY SHA since Sat 10:16:26 CT (BC10)** — bench `7e03c81`; SOAK-NIGHT-3 on `bench-2026-10-17-111625.log`. **BC10 DONE (v112 b3): `176adad` UP** — IR-148's after 0.584 s cold on 2.32 M events (bar 20.4 s); BACKUP-1 36 s, md5 both sides; DV-1 → IR-220. **SOAK-NIGHT-3 tonight** · **Sun BC11** (the rollback) · Tue PI-2 (the fresh image + BC9b) · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v112:** b1 BC10 re-stamped · b2 LICENSE-1 → `LICENSE:` Nov 2 · b3 BC10 INTAKEN · b4 BC11 cut, second-checked; HERO-U4 RETURNED. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 CLOSED on the rig (v112 b3) · 149 · 153–221 (46 · 95 · 119 · 179 · 183 CLOSED; 185–221 new) · 56 CLOSED (v111 b1, sample 7) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b4 card → **Sun BC11** (before 21:30) · `KIT-ORDER:` (PI-2 Tue) · `N3:` by Oct 20 · HERO-U4's intake.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..221 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

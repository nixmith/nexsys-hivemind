<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-13 (v110 beat 4, THE CLOSE — `bfb1b70`; §A.2 LIVE; v111's text; the deliverable adjudicated; D-v110-27..33; v110 CLOSES; Tue 2026-10-13 ~19:4x CT (2026-10-14T00:45:40Z). Next: the close card → D2 → v111) Prior: 2026-10-13 (v110 beat 3 — HORIZON-1 INTAKEN; IR-192..202; GATE-2 dispatched; SCHEMA-1 cut; the mandate banked; D-v110-19..26; Tue 2026-10-13 ~16:5x CT (2026-10-13T21:53:36Z). Next: SCHEMA-1's dispatch → the b3 card → D2 → b4 → the close) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v110 b4 — v110 CLOSED at b4 — v111's text on disk; D2 ran 19:42 → v111)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`6a40a10`** (BENCH-BOOT-1 LANDED Mon 18:36; BP10 `ceb08c5` beneath it; BC10 pulls it); docs **`e2a5844`**; skills `e9a77a8`; hivemind `bfb1b70` (the close card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **J3 LANDED** `e11ae20` (T-A) · `176adad` (T-B), `CI: green` each; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1: D2 RAN Tue 19:42 CT** → v111 b1. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v110 b1–b3** — BENCH-BOOT-1 LANDED `6a40a10`; D-v110-16 RULED (the rollback target post-fix); **HORIZON-1 RULED** (IR-192..202); **GATE-2 + SCHEMA-1 RETURNED** (unread → v111); D2 RAN 19:42 (→ v111 b1); **v110 CLOSED at b4**. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–202 (46 · 95 · 119 CLOSED; 148 sharpened; 185–202 new) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the close card → v111: D2's intake · GATE-2 · SCHEMA-1 · BC10's card.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..202 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

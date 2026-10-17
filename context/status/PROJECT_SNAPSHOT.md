<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-17 (v112 beat 2 — LICENSE-1 INTAKEN ACCEPT → the H10 (`LICENSE:` by Nov 2); BC10-F held; IR-217..219; D-v112-8..12; Sat 2026-10-17 ~07:5x CT (2026-10-17T12:54:26Z). Next: the b2 card → BC10 09:00) Prior: 2026-10-17 (v112 beat 1 — BC10 DISPATCH-READY on `J3-TREE: T-B` + GO (`176adad`); the dry-run COMPLETE; the R&D guide filed; D-v112-1..7; Sat 2026-10-17 ~07:4x CT (2026-10-17T12:42:35Z). Next: the b1 card → BC10 Sat 09:00) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v112 b2 — LICENSE-1 INTAKEN → the H10; BC10-F held; BC10 at 09:00)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`7e03c81`** (BP11 over GATE-2 `5cf3bd0`; BC10 pulls it); docs **`e2a5844`**; skills `e9a77a8`; hivemind `8fb69a6` (b2 pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9b Sun Oct 18. **J3:** `J3-TREE: T-B` + GO (Nick, Sat 07:36 CT) → BC10 deploys `176adad` (`CI: green`). **DRY-RUN #1 COMPLETE** (b1): no dark; R4 ×44; 48.4 MB/day; **IR-56 CLOSED**. **Sat 09:00 BC10 — DISPATCH-READY** (dry-run COMPLETE) · Sun the rollback + BC9b · Tue PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v112:** b1 BC10 re-stamped (`8fb69a6`); b2 LICENSE-1 INTAKEN → `LICENSE:` by Nov 2 ((b), the consent scoped first); BC10-F held. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–219 (46 · 95 · 119 · 183 CLOSED; 148 sharpened; 185–219 new) · 56 CLOSED (v111 b1, sample 7) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b2 card → **Sat 09:00 BC10** (the card pasted whole into a fresh Cowork conversation) → `BC10: …` → b3 its intake; `KIT-ORDER:`; `LICENSE:` by Nov 2.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..219 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

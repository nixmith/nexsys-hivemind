<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-10 (v105 beat 5, THE CLOSE — SOAK-NIGHT-2 S0 + S1 ran; R-F's number BANKED `avail-rows-total=479`; the review against the plans; v106's text cut (Sun 07:00: S2 → HERO-U2c → AVAIL-API-1 in two trees → dry-run #1's packet → the adoption); the adoption deferred (D-v105-34..38); Sat 2026-10-10 ~21:4x CT (2026-10-11T02:47:05Z). Next: the close card → Sun 07:00 S2 → v106) Prior: 2026-10-10 (v105 beat 4 — AMD-103 RATIFIED AND FILED (`DOCS: LANDED e2a5844`); `RESTART: bench-boot`; `HERO-U2c: sunday`; REGISTRY-COLD-1 RETURNED → intaken two-layer → its two-tree landing card, rehearsed; the hub's breach disclosed; six beats rotated; `CORE: LANDED 6a03403` + `CI: green` — REGISTRY-COLD-1 LANDED (D-v105-25..33); Sat 2026-10-10 ~19:5x CT (2026-10-11T00:57:41Z). Next: S0 · the close · v106 Sun 07:00) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v105 b5, THE CLOSE — the soak ran, 479 banked; v106 Sun 07:00 with S2)

**State:** core **`6a03403`** (`CI: green`; REGISTRY-COLD-1 on `main`, the Pi at `37f05a9` until BC10); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`e2a5844`** (AMD-103 RATIFIED); skills `e9a77a8`; hivemind `11c6ff6` (the close card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since 12:00:49 CT;** LOG0 `…130122.log`; **SOAK-NIGHT-2 S0 + S1 RAN 21:08–21:28 CT** (`avail-rows-total=479` = R-F's number); S2 Sun 07:00. **v105 CLOSED at b5:** AMD-103 filed · REGISTRY-COLD-1 LANDED · HERO-U2c Sunday · the renderer MERGED, adopted at v106. **NEXT:** the close card → **Sun 07:00 S2 → v106** (`…/2026-10-11_v106_dispatch-text.md`): §P′ → HERO-U2c → AVAIL-API-1 in two trees → the adoption → v107. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–157 · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..148 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

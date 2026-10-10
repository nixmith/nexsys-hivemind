<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-10 (v104 beat 2 — `HIVE: LANDED 8ab4789`; LIVE-RENDER-1 PASS; the review relaunched; Nick's five words (`COLD-BOOT: a` in his shape; `AMD-103-PATH: b`; `BC10: oct17`; the comparator Mon; RENDERER-2 handed) + four rows; the correction (D-v104-15..21); Sat 2026-10-10 ~14:4x CT (2026-10-10T19:46:19Z). Order: the b2 card → AMD-103 v3 → `AMD-103:` → REGISTRY-COLD-1 → the soak 21:00.) Prior: 2026-10-10 (v104 beat 1 — the restore ruled before the boot; PKG-FRESH-1 intaken (STOPPED at A3; the fence-1 breach; the cold start, IR-148); the Core back 12:00:49 CT; the metering class answered (IR-137); the H10 `COLD-BOOT:` (D-v104-1..14); Sat 2026-10-10 ~12:1x CT (2026-10-10T17:18:49Z). Order: the b1 card → LIVE-RENDER-1 → `AMD-103:` → the soak 21:00.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v104 b2 — the words; LIVE-RENDER-1 PASS; the review relaunched)

**State:** core **`409547c`** (`CI: green`); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`5e8eb8b`**; skills `e9a77a8`; hivemind `8ab4789` (the b2 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since 12:00:49 CT;** LOG0 `…130122.log`. **LIVE-RENDER-1 PASS.** **NICK'S WORDS (14:39):** `COLD-BOOT: a` — REGISTRY-COLD-1 in his H-shape, dispatched Sun; `AMD-103-PATH: b` on that mechanism; `BC10: oct17` (decoupled); the comparator Mon; BEAT-RENDERER-2 handed. **ROWS:** `RESTART:` before Oct 22 · Oct 16 AVAIL-API-1's go/no-go · hs-fresh's service off before its next boot · store growth a pilot gate. **AMD-103 v2 in independent review** → v3 → `AMD-103:`. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 · IR-142 (BP9) · IR-143 · 144 · 145 · 146 · IR-147 · IR-140 · 141. **NEXT:** the b2 card → AMD-103 v3 → REGISTRY-COLD-1 → **≈ 21:00 SOAK-NIGHT-2** → **Sun 07:00 `S2` → v105**.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..148 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

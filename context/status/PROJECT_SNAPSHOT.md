<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-10 (v104 beat 1 — the restore ruled before the boot; PKG-FRESH-1 intaken (STOPPED at A3; the fence-1 breach; the cold start, IR-148); the Core back 12:00:49 CT; the metering class answered (IR-137); the H10 `COLD-BOOT:` (D-v104-1..14); Sat 2026-10-10 ~12:1x CT (2026-10-10T17:18:49Z). Order: the b1 card → LIVE-RENDER-1 → `AMD-103:` → the soak 21:00.) Prior: 2026-10-10 (v103 beat 3, THE CLOSE — `CARRIER: f` ruled (Nick 08:31); BURNIN-1 PARTIAL; PKG-FRESH-1 launched 08:46, PRE-A ruled; the plan forward; the soak re-aimed; v104's text (D-v103-18..28); Sat 2026-10-10 ~09:0x CT (2026-10-10T14:07:49Z). Order: the close card → `PKG-FRESH-1:` → v104 → the soak 21:00.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v104 b1 — the restore; PKG-FRESH-1 intaken; the cold start)

**State:** core **`409547c`** on `main` (`CI: green`); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`5e8eb8b`**; skills `e9a77a8`; hivemind `ba7923d` (the b1 card pending; 8 live beats after it). **THE PI (hs-dev-1): `37f05a9` BY SHA since 12:00:49 CT** — PKG-FRESH-1 STOPPED at A3 (hs-fresh was in the Pi); the fence-1 breach (no form, nothing sent); two cold launches exit 99 (IR-148); W1 + D2b PASS 6/6; LOG0 `…130122.log`. **The metering class ANSWERED 3/3 at the long-gap resume (IR-137).** **AMD-103 DRAFTED (v1), in independent review** → `AMD-103:` → HERO-U2c → AVAIL-API-1 (landed by Fri Oct 16). **NEW: `COLD-BOOT: a|b|c`** (rec a: REGISTRY-COLD-1 before AVAIL-API-1). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 · IR-142 (BP9) · IR-143 · 144 · 145 · 146 · IR-147 (post-run; premise observed) · IR-140 · 141. **NEXT:** the b1 card → LIVE-RENDER-1 → AMD-103 v2 → `AMD-103:` → **≈ 21:00 SOAK-NIGHT-2** → **Sun 07:00 `S2` → v105** · Sun BC9 + REHEARSAL 3 · Wed PKG-FRESH-1b.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY (new) · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..148 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

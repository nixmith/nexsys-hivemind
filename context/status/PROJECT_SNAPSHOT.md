<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-10 (v105 beat 1 — THE BOOT, Sat ≈ 16:4x CT on Nick's word (cut for Sun 07:00); `HIVE: LANDED 61202fc`; PASS 12/12; S0/S2 not yet run → the order re-cut: `REVIEW-RC1: launch` → `ratify` on v7 → the docs card → HERO-U2c → the review's intake → REGISTRY-COLD-1's dispatch → S0 → BR2's intake (RETURNED 15:55); REC: v106 Sun 07:00 with S2 (D-v105-1..7); Sat 2026-10-10 ~17:0x CT (2026-10-10T22:02:44Z). Next: `REVIEW-RC1: launch`) Prior: 2026-10-10 (v104 beat 4, THE CLOSE — `HIVE: LANDED e1a96d4`; AMD-103 DRAFT v7 for v105's word (NOT ratified); v105's text cut; the rotation (D-v104-31..34); Sat 2026-10-10 ~15:5x CT (2026-10-10T20:52:45Z). Next: ≈ 21:00 the soak → Sun 07:00 v105) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v105 b1, THE BOOT — Sat ≈ 16:4x CT on Nick's word; the order re-cut around the soak; `REVIEW-RC1: launch` handed)

**State:** core **`409547c`** (`CI: green`); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`5e8eb8b`**; skills `e9a77a8`; hivemind `61202fc` (v104's close LANDED). **THE PI (hs-dev-1): `37f05a9` BY SHA since 12:00:49 CT;** LOG0 `…130122.log`. **v105 OPEN Saturday evening (its text was cut for Sun 07:00; S0 ≈ 21:00 and S2 Sun 07:00 do not exist yet; nothing of the soak ruled):** `REVIEW-RC1: launch` (the agent) → **`AMD-103: ratify` on v7** (`371cd241…`) → the docs card → **HERO-U2c** on the word → the review's intake → **REGISTRY-COLD-1**'s dispatch → S0's `avail-rows-total` banked → **BEAT-RENDERER-2** RETURNED 15:55 (`staged=17`; intake after the deliverable). REC: v105 closes tonight; **v106 Sun 07:00 with S2** → §P′ → BC9 + REHEARSAL 3. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 · IR-142 (BP9) · IR-143 · 144 · 145 · 146 · IR-147 · IR-140 · 141. **NEXT:** `REVIEW-RC1: launch`.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..148 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

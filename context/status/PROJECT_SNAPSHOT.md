<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-03 (v95 beat 8, the last — V72B intaken ACCEPT (ba846c2; the selftest re-run 44/0); HIVE-CLEAN-2 for v96; D-v95-28/29; Sat 2026-10-03 ~20:0x CT (2026-10-04T01:00:05Z). Order: the b8 card → the push card → v96. Detail: pm-handoff v95 b8.) Prior: 2026-10-03 (v95 beat 7 — REHEARSAL 2 → Sunday 17:25 (the envelope); V72B's GO cut; v96 re-cut; D-v95-25..27; Sat 2026-10-03 ~19:1x CT (2026-10-04T00:10:11Z). Order: the b7 card → V72B → v96. Detail: pm-handoff v95 b7.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v95 b8, the last — J1 LANDED; V72B delivered on its branch; REHEARSAL 2 → Sunday 17:25; v96 next)

**State:** core **`df2bc62`** (J1 — LINK-READ-2 + IR-121; `CI: green`; **19/20**); bench **`0232c69`** (V72B `ba846c2` on its branch → the PR; D-v95-28); docs **`055832c`**; skills `e9a77a8`; hivemind **`c0b7808`** + the b6 card. **J1 LANDED** (D-v95-23). **THE PI at `5b0e20c`** until BC8. **THE FLEET: 10 in the registry, 8 ON THE AIR** — the SNZB-06P24 UNJOINED (card 1 tonight; P1 pre-registered `UNAVAILABLE`, D-v95-13), the Hue silent (NO act tonight). **J1** (D-v95-10..14): the 60-s probe, the per-class limit, `availability_changed` v2, the API's `availabilityReason`/`lastSeenAt`/`link`. **THE SPIKE ACCEPTED** (J2 = J2a `A:372` + J2b `E:1047`; two gsdk cites owed); **`WIZARD: b′` STANDS.** **KREFRESH-1 ACCEPTED** (UPLOAD-3 done). **RULED:** `DAY: b` · `WIZARD: b′` · W18 open. **LANES:** none running (V72B returned). **TONIGHT:** no rig (REHEARSAL 2 → SUNDAY 17:25; D-v95-25); v96: V72B's landing after CI; HIVE-CLEAN-2 (D-v95-29); Sunday's text. **NEXT:** v96 now; Sun v97 08:00 (J2 + IR-123 · U2a · HERO-1 · the soak packet) → 17:25 the packet → v98; Mon BC8; Tue CONFIG-ERROR-1 + IR-122; Wed the soak. **§10:** Mon/Tue BC8 · Wed the soak. DRs v92–v95 CLOSED.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..121 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane's exit and grant first · no PR merged by the button · every card gated · the restore before any gap · no `capability.removed` · no ungrepped premise · `--no-optional-locks` · every edited row by its id · every tool argument through its validator · every watch on a byte mark.

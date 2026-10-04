<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-03 (v95 beat 7 — REHEARSAL 2 → Sunday 17:25 (the envelope); V72B's GO cut; v96 re-cut; D-v95-25..27; Sat 2026-10-03 ~19:1x CT (2026-10-04T00:10:11Z). Order: the b7 card → V72B → v96. Detail: pm-handoff v95 b7.) Prior: 2026-10-03 (v95 beat 6 — J1 LANDED df2bc62, CI green; V72B dispatched plan-first; D-v95-23/24; Sat 2026-10-03 ~16:4x CT (2026-10-03T21:47:33Z). Order: the b6 card → 17:25 → v96. Detail: pm-handoff v95 b6.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v95 b7 — J1 LANDED; V72B coding on the desk; REHEARSAL 2 → Sunday 17:25; v96 ≈ 21:30)

**State:** core **`df2bc62`** (J1 — LINK-READ-2 + IR-121; `CI: green`; **19/20**); bench **`0232c69`**; docs **`055832c`**; skills `e9a77a8`; hivemind **`c0b7808`** + the b6 card. **J1 LANDED** (D-v95-23). **THE PI at `5b0e20c`** until BC8. **THE FLEET: 10 in the registry, 8 ON THE AIR** — the SNZB-06P24 UNJOINED (card 1 tonight; P1 pre-registered `UNAVAILABLE`, D-v95-13), the Hue silent (NO act tonight). **J1 CUT + HANDED** (D-v95-10..14): the 60-s probe, the per-class limit, `availability_changed` v2, `EntityState` + 3, the API's `availabilityReason`/`lastSeenAt`/`link`; 17 review edits applied. **THE SPIKE ACCEPTED** (J2 = J2a `A:372` + J2b the scoped window `E:1047`; two gsdk cites owed); **`WIZARD: b′` STANDS.** **KREFRESH-1 ACCEPTED** (UPLOAD-3 Nick's). **RULED:** `DAY: b` · `WIZARD: b′` · W18 open. **LANES:** V72B (the desk, coding on `GO with:`). **TONIGHT:** no rig (REHEARSAL 2 → SUNDAY 17:25, the same packet; D-v95-25); V72B codes → v96 ≈ 21:30. **NEXT:** V72B's `RETURNED` → v96; Sun v97 08:00 (J2 + IR-123 · U2a · HERO-1 · the soak packet) → 17:25 the packet → v98; Mon BC8; Tue CONFIG-ERROR-1 + IR-122; Wed the soak. **§10:** Mon/Tue BC8 · Wed the soak. DRs v92–v95 CLOSED.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..121 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane's exit and grant first · no PR merged by the button · every card gated · the restore before any gap · no `capability.removed` · no ungrepped premise · `--no-optional-locks` · every edited row by its id · every tool argument through its validator · every watch on a byte mark.

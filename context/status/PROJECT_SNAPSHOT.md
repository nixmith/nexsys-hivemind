<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-04 (v96 beat 5 — the remainder of b4 (`c5166bc` carried its spine); HIVE-CLEAN-3 RETURNED 08:2x; D-v96-15; Sun 2026-10-04 ~08:3x CT (2026-10-04T13:35:32Z). Order: the b5 card → v97 → 17:25 → v98. Detail: pm-handoff v96 b5.) Prior: 2026-10-03 (v96 beat 4, after the close — J2 PRE-VERIFIED at `df2bc62` (the gsdk cites at the source; 0x0010; the explicit close); D-v96-14; Sat 2026-10-03 ~21:2x CT (2026-10-04T02:21:51Z). Order: the b3b4 card → HIVE-CLEAN-3 → v97 08:00 → 17:25 → v98. Detail: pm-handoff v96 b4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v96 b4 — J1, V72B LANDED; J2 pre-verified; HIVE-CLEAN-3 ready; v97 Sun 08:00; REHEARSAL 2 17:25)

**State:** core **`df2bc62`** (J1 — LINK-READ-2 + IR-121; `CI: green`; **19/20**); bench **`ba846c2`** (V72B LANDED 20:34, D-v96-8; the Pi's clone `0232c69` to BENCH-PULL-7); docs **`055832c`**; skills `e9a77a8`; hivemind **`c5166bc`** + the b5 card. **J1 LANDED** (D-v95-23). **THE PI at `5b0e20c`** to BC8. **THE FLEET: 10 in the registry, 8 ON THE AIR** — the SNZB-06P24 UNJOINED (Sunday's card 1; P1 pre-registered `UNAVAILABLE`, D-v95-13), the Hue silent (no act). **J1** (D-v95-10..14): the 60-s probe, the per-class limit, `availability_changed` v2, three API keys. **J2 PRE-VERIFIED** (D-v96-14): J2a `A:392` · J2b 0x0013 + the explicit close; `WIZARD: b′` STANDS; KREFRESH-1 ACCEPTED. **RULED:** W18 open. **LANES:** none; HIVE-CLEAN-3 RETURNED (v97 b1's intake). **v96 CLOSED** (b3; b4 after; D-v96-1..14): V72B landed · HIVE-CLEAN-3 · v97's text · J2 pre-verified; no rig. **NEXT:** the b5 card; v97 now; Sun v97 08:00 (the fixes · J2 · the packet · U2a · HERO-1 · the soak) → 17:25 the packet → v98; Mon BC8 (v99); Tue CONFIG-ERROR-1 + IR-122; Wed the soak. DRs v92–v96 CLOSED.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..123 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane's exit and grant first · no PR merged by the button · every card gated · the restore before any gap · no `capability.removed` · no ungrepped premise · `--no-optional-locks` · every edited row by its id · every tool argument through its validator · every watch on a byte mark.

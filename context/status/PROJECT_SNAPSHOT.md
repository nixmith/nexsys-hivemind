<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-15 (v75 beat 5, MEASURE-1 ACCEPT — both defects measured; DUR-1 + HASH-1 and DEVICE-SET DISPATCH-READY; the Activate email; the spine rotated; Tue 2026-09-15 ~18:0x CT (2026-09-15T23:09Z). Order: hivemind 14 = 9 M + 5 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v75 beat 5.) Prior: 2026-09-15 (v75 beat 4, THE VERDICTS AND THE PLAN — 114c `e56f555` and FE-114 `3d40b5f` CI GREEN (6/20); the freeze doc v1.1.5; THE PREMISE GATE; MEASURE-1 DISPATCH-READY; the dossier ACCEPT; D-v75-5; the plan of record re-cut; Mon 2026-09-14 ~21:3x CT (2026-09-15T02:31Z). Order: hivemind 14 = 10 M + 4 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v75 beat 4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v75 at beat 5 — both defects measured; the fixes and the fleet chartered; the b5 packet handed, Tue 09-15 ~18:xx CT)

**State:** core `3d40b5f` + MEASURE-1's two test files uncommitted (they land with DUR-1 + HASH-1); the stamp **v1.1.5**; hivemind `0eef472` + b5 (the card); docs `7221ddc`; bench `f3631cb`; skills `180375f`. **The plan of record:** `context/planning/2026-09-15_v75_PROGRAM-PLAN_the-six-weeks-to-the-72-hour-run.md` (§10 addendum b5: the benchmark fleet) — the run Oct 30 – Nov 2; R-5B → rehearsal 1 → ENERGY-READ → LINK-READ → rehearsal 2 → the soak → the run. **This window:** b1–b5 DONE · b6 the knockout charter; DUR-1 + HASH-1 intaken → the landing card; ENERGY-READ on DEVICE-SET's return · b7 FE-115; rehearsal 1 · b8 the close. **Words:** `HIVE:` · `HASH1: a|b` (silence = a) · `DUR1:` · `DEVSET:` → `DEVICES:` · `ACTIVATE: sent` · `NAME:` silence = ii · `STRATEGY:` · `CASCADE:` · `AMD100: ratify`. **Owed:** `PROTECT: done` · `ERIK:`

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 6/20 · ADOPT-AWAKE · four standing) + IR-22 (a for_duration expiry initiates no run — MEASURED RED; DUR-1 chartered) + IR-23 (the definition hash salted in eight records — MEASURED on both sources; HASH-1 chartered) + two fences (no IAS water/smoke/vibration before IR-15; no metering plug before ENERGY-READ). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off until R-5B's B6 · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes · no re-pin before Saturday without `REPIN:` · no ungrepped premise goes DISPATCH-READY · the MEASURE-1 tests never land alone.

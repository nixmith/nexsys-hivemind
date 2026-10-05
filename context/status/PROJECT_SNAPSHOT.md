<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-04 (v98 beat 1 — THE BOOT; REHEARSAL 2 INTAKEN ACCEPT (D-v98-3); `CI: green` on `main` at `49455fc`, J2 CLOSED (D-v98-4); the counter 19/20; D-v98-1..8; Sun 2026-10-04 ~19:4x CT (2026-10-05T00:43:04Z). Order: the b1 card → b2 BC8 → b3 SOAK-NIGHT-1 → b4 the bench charter → the close ≤ 23:00. Detail: pm-handoff v98 b1.) Prior: 2026-10-04 (v97 beat 6 — THE CLOSE: THE WEEK (D-v97-17); THE HORIZON by id; v98's text; J2 LANDED `main` → `49455fc` (D-v97-19); the DR CLOSED (D-v97-18); Sun 2026-10-04 ~16:4x CT (2026-10-04T21:44:39Z). Order: the b6 card → 17:25 the packet → v98 ≈ 21:00. Detail: pm-handoff v97 b6.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v98 b1 — REHEARSAL 2 intaken; J2 CLOSED by CI on `main`; BC8 Mon; two words owed)

**State:** core **`49455fc`** (J1 + J2 LANDED; **CI green on `main`** v98 b1; the counter **19/20**, D-v98-6); bench **`ba846c2`** (the Pi's clone `0232c69`); docs `055832c`; skills `e9a77a8`; hivemind `2c8ed46`. **THE PI at `5b0e20c`** to BC8 Mon (`df2bc62` unless Nick's `BC8: 49455fc`). **THE FLEET: 10 in the registry, 9 ON THE AIR** — the SNZB-06P24 re-joined at REHEARSAL 2 (a chewed cable: 54 h of power loss, not radio); the Hue silent (IR-112). **THE SITTING** (D-v98-3): D-v95-13 CONFIRMED · P6 THE SILENT RESUME AT THE JOIN LAYER (IR-56 s6; IR-128) · IR-118's exhibit 17 min 50 s (IR-121) · IR-115 s3 · IR-119's exhibit · the restore byte-identical. **WORDS OWED** (silence = the first): `BC8: df2bc62 | 49455fc` · `RENDERER: tue | thu | after-run`. **LANES:** none. **THE WEEK** (D-v97-17 stands, D-v98-8): Mon BC8 · Tue CONFIG-ERROR-1 (or the renderer) + the bench line · Wed the soak + HERO-1 · Thu PKG-FRESH-1 + STARTER-1 · Fri BC9 · Sat REHEARSAL 3 · Sun U2a · Mon 10-12 dry #1. **NEXT:** the b1 card → b2 BC8's card → b3 SOAK-NIGHT-1 → b4 the bench charter → the close → v99 Mon ≈ 19:00.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..131 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event.

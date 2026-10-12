<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-12 (v109 beat 4, THE CLOSE — `fdce2d0`; COMPARATOR-1 intaken; OUTREACH-2 LIVE; v110's text; six rotated; Mon 2026-10-12 ~15:5x CT (2026-10-12T20:50:46Z). Next: the close card → dry-run #1 → v110) Prior: 2026-10-12 (v109 beat 3 — `109e075`; BENCH-BOOT-1 CHARTERED; TRIAGE found done (v103); the OUTREACH-2 note; D-v109-17..19; Mon 2026-10-12 ~14:5x CT (2026-10-12T19:55:22Z). Next: BENCH-BOOT-1 → the b3 card) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v109 b4 — v109 CLOSED at b4 — COMPARATOR-1 intaken; OUTREACH-2 LIVE; v110's text on disk)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`ceb08c5`** (GRADER-S31-1; BP9 + BP10 ride BC10); docs **`e2a5844`**; skills `e9a77a8`; hivemind `fdce2d0` (the close card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **THE RENDERER ADOPTED** (b1; `--check` at every boot). **J3 LANDED Mon 09:3x** — `e11ae20` (T-A) · `176adad` (T-B), `CI: green` each; IR-46 · 95 · 119 CLOSED; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 ≈ 19:00 CT** · Tue D2. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v109 CLOSED at b4** — GRADER-S31-1 LANDED `ceb08c5` (BP10); COMPARATOR-1 intaken; OUTREACH-2 LIVE v2; BENCH-BOOT-1 running → v110. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–184 (46 · 95 · 119 CLOSED at `e11ae20` / `176adad`) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the close card → dry-run #1 ≈ 19:00 CT → v110 (its text on disk) → BENCH-BOOT-1's intake (v110 b1) → the outreach calls by Wed.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..174 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.

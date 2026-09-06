<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-06 (v66 beat 5 — FE-113 audited ACCEPT (14 M + 2 A; the landing next) · TR-0 audited ACCEPT (B-2 = one line at CRS:249), Sun ~11:18 CT (2026-09-06T16:18Z). Order: hivemind 10 = 6 M + 4 A. Detail: pm-handoff v66 beat 5.) Prior: 2026-09-06 (v66 beat 4 — BLOCK 6 (pull) applied to the docs working tree (5 M; Nick's commit after H8-a) + the freeze doc → v1.1.3, Sun ~11:12 CT (2026-09-06T16:12Z). Order: hivemind 6 = 5 M + 1 A. Detail: pm-handoff v66 beat 4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v66 beat 5 — BLOCKS 1–3 DONE; TWO INTAKES AUDITED, Sun 2026-09-06 ~11:18 CT)

**THE H8-a PACKET IS ON DISK** (`context/instructions/2026-09-06_H8a_…navigator-packet.md` + its record scaffold): the rig ~15:00 CT, EXCLUSIVE — **the artifact of record is `f25291b`'s install-smoke run** (Java = `093d5b4`'s) · the four keys on the wire · the stop-proof · the capture for FE-113b · the restore; the navigator paste ~14:50 CT. **THE F-R4-1b INSTRUCTION IS ON DISK** (⛔ after FE-113 lands; `R4C:` due first, rec Sat 09-12). **BLOCK 6 APPLIED** to the docs working tree (5 M; nothing staged; the card under `context/handoff/` — Nick's one act after H8-a); the freeze doc at **v1.1.3**. **INTAKES:** FE-113 RETURNED + audited ACCEPT (16 = 14 M + 2 A on the core tree; the landing = Nick's next act after HERO-0: one command, `frontend.yml` = the gate, `ci.yml` = passive sample 4/20) · TR-0 RETURNED + audited ACCEPT (**B-2 = a bounded insertion at `CommandRoutingSubscriber:249`**; rows TR0-1/2/3). **THE OPERATOR-LOAD LAW** governs every message. **HEADs:** core `093d5b4` + FE-113's 16 unstaged · hivemind = this beat (origin `7f14059`) · docs `a53f474` (+5 M unstaged). **BRAND:** `SEARCH-NAME: VERDOMO` provisional (re-given Tue 07:00); `ASR-VERDOMU:` · `RS10-STAR:` owed; `DESIGN: hold`. Paid cap two.

**NOW (Nick):** ONE act at a time — Act 5 HERO-0's paste (in hand) → 6 the FE-113 landing → 7 RS-12-F → 8 TR-1 → 9 the navigator at ~14:50 CT → BLOCK 6 after H8-a. **v66:** the intakes (HERO-0 · RS-12-F · TR-1 · the samples · H8-a's record) → Monday the go-ahead + the RS-10 appendix page.

**OPEN RISKS:** six (FAILCHAN: closes on B3 today · BUS-SILENT-DROP 3/20 → 4/20 on the FE-113 push; the three veto samples firing). Fences: one core lane · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly HANDS OFF · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name in chat · 09-18.

<!--
file: context/planning/2026-10-04_v97_decision-record.md
purpose: The v97 hub window's decision record (Sun 2026-10-04's morning window, pasted 09:00 CT) — Nick's words verbatim (§1), the facts at the instrument (§2), the decisions by beat (§3 onward), the Carried row from v96. THE ONE DELIVERABLE: J2's LOCAL instruction pre-verified, independently reviewed and in Nick's hands, AND the REHEARSAL 2 packet re-stamped with a fresh dry-run before 17:25.
audience: the v97 hub (edited every beat) · the v98 boot (the newest §3 section + the Carried row) · Nick (§1 is his)
state-type: decision record (one window)
status: LIVE — opened v97 beat 1 (Sun 2026-10-04 ~09:3x CT; instrument 2026-10-04T14:32:15Z)
-->

# v97 — decision record

## §1 Nick's words, verbatim
- 09:00 CT: the v97 dispatch text from line 8 whole (byte-identical to `context/handoff/2026-10-04_v97_dispatch-text.md`; md5 `3584b2b7cbe49e05d455d724cf5442e3` both sides, newlines stripped), then: "`TIME: 09:00 CT` · `HIVE: LANDED b9c60f8` · `HIVE-CLEAN-3: RETURNED context/audits/2026-10-03_HIVE-CLEAN-3_census.md 8191` · `J2-PREVERIFY: filed 19530`".

## §2 The facts at the instrument (banked; no act)
- `date -u` 2026-10-04T14:00:16Z = Sun 2026-10-04 09:00 CT. Hivemind `b9c60f8` = `origin/main` (v96 b5, 7 files, 08:49 CT), porcelain = the census's two `??` files, no lock. Core `df2bc62` · bench `ba846c2` · docs `055832c` · skills `e9a77a8`, each `= origin/main`, porcelain 0.
- The preflight 12/12 (Check 4 reconciled this beat; Check 6 carried to b3 — the b1 audit §1); Check 9 28/28 at the bytes; the boot read ≈ 39.5 KB ≤ 45. Live beats 12 of 12 before this beat; 7 after (six rotated).
- HIVE-CLEAN-3's census: 102 rows; the lane's P1–P8 all TRUE at its tree (`c5166bc`); its `stale` column abbreviated with `…` in 15 rows (IR-124).
- J2's pre-verification on disk: 19,530 B, `status: FILED` (v96 b4), landed in `b9c60f8` — beat 2 re-runs its three riskiest signatures at `df2bc62` rather than re-deriving it.

## §3 The decisions (beat 1, Sun 2026-10-04 ~09:3x CT)
- **D-v97-1 — THE WINDOW'S ONE DELIVERABLE AND ITS SHAPE.** J2's LOCAL instruction pre-verified (its pre-verification re-run, not re-written), independently reviewed and in Nick's hands for the desk, AND the REHEARSAL 2 packet re-stamped (date-bound lines only) with a fresh dry-run before 17:25. The shape: b1 this (the rotation; the intake; THE FIXES CARD) · b2 the pre-verification's three riskiest signatures re-run at `df2bc62` + the MODULE_CONTEXT rows J2 touches · b3 the instruction → the one-way-door review → the dispatch line · b4 the packet's re-stamp + the dry-run + the pre-registrations in order · b5 U2a · HERO-1 · SOAK-NIGHT-1 (RENAME-CENSUS-1 if the hour allows) · b6 the week's lines, THE HORIZON's J2 row by Nick's word or the silence rule · the close ≤ 17:00 with v98's text. No new block after b6. No hardware before 17:30.
- **D-v97-2 — HIVE-CLEAN-3 INTAKEN ACCEPT; THE FIXES CARD CUT BY ID.** 102 rows read; ≥ 3 per surface re-executed at the bytes (the b1 audit §2). Applied: 93 rows (the audit §3) under THE EDITED-ROW LAW — status lines keep `Was:`; dates, shas and the lane id replaced in place with the D-id beside them (`HIVE-CLEAN-3 (was -2; D-v96-7)`); nothing deleted; the terminal statuses set (EXECUTED / SUPERSEDED) where the census proved them. Declined or carried, each with its reason in the audit §4: C-13 and C-18 (J2's row and the §9 board row move at b6 by Nick's word or the silence rule), C-16 (already current), C-41/42/43 (a dispatch text's body is verbatim; the note rides C-40's status line), C-50/51 (overtaken by v96 b5 and this digest), C-90 (stands). The hub's own rows: C-103 (the v96 b5 card → `_RAN-b9c60f8`, proven at `git show --stat`); the v97 text → PASTED; HIVE-CLEAN-3's charter → EXECUTED. The charter's §4 rules were followed as written.
- **D-v97-3 — IR-124 MINTED** (the register): a census TSV's `stale` cell is a verbatim substring ≥ 40 characters, grep-able as written — the HIVE-CLEAN-3 TSV abbreviated 15 of 102 with `…` and the hub's Layer-2 script found them only by hand. The next census charter's §3 carries the sentence.
- **D-v97-4 — THE ROTATION.** v95 b2 → v95 b7 (six blocks) rotated VERBATIM into `context/handoff/archive/pm-handoff-beats-v95b2-v95b7-rotated-2026-10-04.md`; bytes asserted before the write; the archive map row; the chain's v96 b4 segment → `archive/chains-rotated-2026-08-27.md` (244).
- **Carried into v97 b2 (from v96's final row, less the three given):** `REVERT J2` · `REMOTE:` · `FINALS:` · `DISCOVERY:` · `PR1-docs: closed` · `ATTORNEY-DRAFT: sent <n>` · `TAILSCALE: expiry-off` · `TM:` · `OUTREACH:` · `B7:` · `SAMPLE:` · `RENAME:` (held) · `HARNESS-PLUG:` (held) · `ACCOUNT-2:` (held). Given at the boot: `HIVE: LANDED b9c60f8` · `HIVE-CLEAN-3: RETURNED … 8191` · `J2-PREVERIFY: filed 19,530`. Open this beat: `HIVE: LANDED` (the b1 card).

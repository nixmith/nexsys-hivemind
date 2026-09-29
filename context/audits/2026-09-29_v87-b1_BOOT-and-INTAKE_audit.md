<!--
file: context/audits/2026-09-29_v87-b1_BOOT-and-INTAKE_audit.md
purpose: v87 beat 1 — the boot at the byte budget, the preflight (12 checks, one line each), the five HEADs, the adjudication of core's two unrecorded commits, the intake of Monday night's lines, the hygiene acts, the act handed.
audience: the v87 hub · the v88 boot (by §0)
state-type: audit (one beat)
status: FILED — Tue 2026-09-29 ~13:4x CT (instrument 2026-09-29T18:40:47Z)
-->

# v87 beat 1 — BOOT and INTAKE audit

## §0 Verdict
**BOOT PASS; INTAKE BANKED.** The boot read-set 43.1 KB (≤ 45 KB; two ranges trimmed to the strategy pass). The preflight 12/12 PASS (Check 9: 28/28 identical; Check 12: 6 live files, all accounted for — two flip to EXECUTED this beat). Core had moved past the record by two commits, both adjudicated at `git log` as PJ-2's landing (`146468c`) and its fix (`8deef4b`); both CI green on Nick's word. Hivemind `df106bc` (the v86 card landed). Nothing else moved. ONE act handed: CORPUS-1.

## §1 The boot read-set (bytes at `wc -c`)
| Read | Bytes |
|---|---|
| the v67 prompt, whole | 13,017 |
| pm-handoff.md line 8 (the chain) | 1,734 |
| the newest beat block (v86 b4; lines 15–20) | 2,367 |
| PROJECT_SNAPSHOT.md whole | 3,465 |
| OPERATOR-BRIEF_for-Nick.md whole | 12,256 |
| the v86 DR §3c + §3d + Carried (lines 42–53) | 7,989 |
| pm-lessons.md: the two 2026-09-28 entries' heading lines (the grep) | ≈2,300 |
| **Total** | **≈43,130** |
Trimmed at the law (over budget = stop): plan §30 (2,512 B) and THE WEEKS AHEAD §7 (2,954 B) — both are the strategy pass's read (block 4 reads THE WEEKS AHEAD whole).

## §2 The preflight (one line per check)
1. PASS — both spines' newest segment = v86 beat 4. 2. PASS — the two plan files resolve. 3. PASS — the snapshot's core `40412f9` is two behind HEAD `8deef4b`; both commits accounted for in the post-close note and banked this beat. 4. PASS — `phase-3-milestone-backlog.md` present (29 DONE rows; unchanged since the last full cross-reference). 5. PASS — `## Open Risks` at line 69, 42 entries, edited at v86. 6. PASS — coder-handoff's newest entry (PJ-2 DELIVERED) names the next. 7. PASS — 21 MODULE_CONTEXT.md files tracked, 0 under 800 B. 8. PASS — 0 active entries above `## Archived`. 9. PASS — 28/28 md5-identical (project-manager · coder · nexsys-frontend; source trees on the device vs the synced copies in the session). 10. PASS — 5 of 101 cited names unresolved, all five glob placeholders (`*_PM-mission-control_v*_orchestrator_session_prompt.md`, `YYYY-MM-DD_topic.md`, `handoff/*_session_prompt.md`, `months/YYYY-MM_month.md`, `weeks/YYYY-WNN_monDD-monDD.md`). 11. PASS — `StandardActionExecutor.java` 1; pairing-named files 8. 12. PASS after this beat's hygiene — six live files: KREFRESH-1 (DISPATCH-READY by the record) · BC6 (DISPATCH-READY by the record; SUPERSEDED at beat 2) · CORPUS-1 (handed this beat) · W-SKILLS-10 (Wednesday) · the PJ-2 coding instruction and the PJ-2 landing card (→ EXECUTED this beat, `CORE: LANDED` having come); LIVE prompts not v67: 0; the weeks tree: 0.

## §3 The five HEADs and the adjudication
core `8deef4b` · hivemind `df106bc` · skills `180375f` · bench `352296d` · docs `7221ddc`; porcelain 0, ahead 0, no `.git/*.lock` in all five. The record (v86 b4) had core `40412f9` and hivemind `b4025b6` + the v86 card. Adjudicated at `git log -4 --format='%h | %an <%ae> | %ad | %s'`: `146468c` Nick Smith 2026-09-28T20:43:06-05:00 "feat(integration-api,integration-zigbee,integration-runtime,rest-api,lifecycle): WU-PJ2 — …" (34 files, +2437/−229) — the landing card's squash, carrying `docs/lane-returns/2026-09-28_PJ2_return.md` because `git rm -rq` refused a squash-staged path and the card's `;` ran the commit anyway; `8deef4b` Nick Smith 20:56:52-05:00 "chore(docs): remove the PJ-2 lane return … (IR-101)" (1 file, −142). Trailer grep on both bodies: 0. `origin/main` = `8deef4b`. Hivemind `df106bc` = the v86 b1–b4 card (its subject matches the msg file's).

## §4 The intake (each line with its instrument)
- `CORE: LANDED 146468c + FIX 8deef4b` — re-executed at `git log` (above). BANKED.
- `CI: 146468c green` · `CI: 8deef4b green` — Nick's word Mon 21:07 CT in the post-close note; GitHub's API is gated from the container (`add_repo`), so not re-executed; the 18th and 19th CI lines; the counter 18/20 (`a5b9e33` OPEN → 19). BANKED AT WORD, disclosed.
- `HIVE: LANDED df106bc` — re-executed at HEAD. BANKED.
- PR #7 closed as landed — Nick's word; not re-executed.
- `BENCH-CORE-6: STOP (20:18 CT)` — banked at v86 b4 (D-v86-16). The card CANNOT RUN AS CUT (D-v87-4): its Block 2 `git pull --ff-only` (line 39) would land `8deef4b` on the Pi's core clone; its Block 0 EXPECTED `behind=2` (line 16) reads 4.
- `NIGHTLY:` Tuesday's 03:30 CT line — NOT YET SAID; the pre-registered pair (`1f1d1e0`, `352296d`), `8/9 PASS · fleet: 9/9 · re-seen 9`, 0 forbidden (D-v86-5).

## §5 Layer 2
Re-executed: the core log (authors, dates, file counts, trailers, `origin/main`); the five HEADs and porcelains; Check 9 at md5 on both sides; Check 12's three greps with the list re-derived; Check 10's five names resolved by basename against the five repos' `git ls-files`; the pasted text matched to the filed dispatch at three phrases (1/1/1); the post-close note's transcript lines read against `git log` (the `0 · 40412f9 · error: … · 40412f9..146468c · 146468c Nick Smith · 0` sequence is consistent with the tree). Not re-executed: the two CI runs and PR #7's state; the Pi (untouched since BC5; BC6 never ran).

## §6 The hygiene acts (this beat)
The PJ-2 coding instruction and the landing card: `status:` → EXECUTED (the prior status kept after `was:`; bodies untouched). The v87 dispatch text: LIVE → PASTED. The CORPUS-1 card: a guide preamble inserted below its H1 (the blocks untouched); its status line marks the hand. IR-101 appended to the register; one entry appended to pm-lessons. The post-close note copied verbatim (5,321 B) into `context/audits/`.

## §7 The act handed
CORPUS-1 — pasted WHOLE into a FRESH conversation with `ClaudeFolder` connected; three lines back. BC6b is beat 2's cut and the next hand (≤ 20:15 CT start; the rig in series).

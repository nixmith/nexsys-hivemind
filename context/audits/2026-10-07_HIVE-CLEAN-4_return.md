<!--
file: context/audits/2026-10-07_HIVE-CLEAN-4_return.md
purpose: HIVE-CLEAN-4's return — the census before → after at hivemind HEAD 675a8ab, the acts by row, the live citers of every moved path, what the hub does at intake, the card, deviations. The TSV beside it is the proof.
audience: the hub (two-layer intake) · Nick (the card)
state-type: lane return
status: RETURNED — ran Thu 2026-10-08 22:36Z → 23:1xZ in a fresh Cowork conversation on ClaudeFolder; HEAD 675a8ab (the charter's eb0f5ff + its own beat); STAGED, never committed.
-->

# HIVE-CLEAN-4 — return

## §0 The census (re-measured at `675a8ab`; `date -u` 2026-10-08T22:36:03Z; porcelain 0, no locks at start)
| where | before | after |
|---|---|---|
| handoff root `*.md` | 25 | 6 (stable prompt · pm-handoff · OPERATOR-BRIEF · coder-handoff · cross-agent-notes · the v100 text) |
| handoff/archive/dispatch-texts | 10 | 29 |
| instructions live | 53 (39 EXECUTED · 3 SUPERSEDED · 1 EXECUTED-STOPPED · 4 RETURNED · 1 HELD · 5 DISPATCH-READY) | 6 (5 DISPATCH-READY + 1 HELD) |
| instructions/archive | 180 | 227 |
| planning live | 69 | 51 |
| planning/archive/decision-records | 7 | 25 |
| pre-verifications live / archive | 15 / 11 | 8 / 18 |
| decisions | 15 | 15 (statuses only) |
| `ls _scratch \| wc -l` | 200 (149 files · 51 dirs) | 56 (4 files · 52 dirs) |
| porcelain `-uall` | 0 | 94 = 91 R + 1 M + 2 A, all staged |

Exclusion list re-derived: the newest `## 20` block (v99 b4, :15) names no lane by id and no RUNNING; the status grep gives 5 DISPATCH-READY = SOAK-NIGHT-1 · AVAIL-LINE-1 · PKG-FRESH-1 · BEAT-RENDERER-1 · this charter. None touched.

## §1 The acts by row (each re-measured, done, asserted; every row in the TSV)
- R1 19 `git mv` handoff/<v81…v99>_dispatch-text.md → archive/dispatch-texts/ (v91 SUPERSEDED, the rest EXECUTED). The v100 text and the stable prompt untouched.
- R2 47: 43 `git mv` (39 EXECUTED · 3 SUPERSEDED · 1 EXECUTED-STOPPED) → instructions/archive/; the 4 RETURNED (VERIFY-72H-A2 · IR61b · LOCK-1 · DOCS-1), each return present under audits/ → `EXECUTED — HIVE-CLEAN-4 (2026-10-07). Was: RETURNED …` then moved. HELD (ACCOUNT-2-SETUP) stays.
- R3 18 `git mv` → planning/archive/decision-records/: the 17 CLOSED DRs v81–v98 (no v91 DR exists — v91 was never pasted) + the v66 SESSION-SYNTHESIS (FILED). The v99 DR stays. One status line: `2026-09-26_v81_HORIZON-RE-CUT_…` REC-ON-THE-DESK → `FILED — HIVE-CLEAN-4 (2026-10-07). Was: …` (ruled: `POSTURE: pilot-first` v83 DR :21; `LAUNCH-POSTURE: a` pm-handoff :80); no move. The v75 PROGRAM-PLAN stays LIVE — v82's frontmatter names it the plan of record.
- R4 7 pre-verifications `EXECUTED — … Was: …` + `git mv` → pre-verifications/archive/, each on the spine's landing: WU-DASH-SERVE (core `c09c61c` DONE, v39) · WU-IR61 (IR-61b `40412f9`, LOCK-1 `a5b9e33`, v84 b6) · WU-IR67 (`5b0e20c`, v90 b1) · WU-J1_LINK-READ-2_IR-121 (`CORE: LANDED df2bc62`, v95) · WU-J2_…_IR-114 (`CORE: LANDED 49455fc`, D-v97-19) · WU-PJ2 (`146468c`, v87 b1) · WU-SKIP-VIS (`da11f46` ON MAIN, v38 b5). Stay: README · WU-STARTER-1 (OPEN) · WU-IR56 (the IR open) · WU-R3 (PINNED; no `LANDED` for R-3 anywhere in the ledger) · WU-R1R2/R6R8/R7/R9 (HIVE-CLEAN-2's "historical record" — terminal, left in place). decisions/: 7 RATIFIED · CO-SIGNED · COMPLETE · DECIDED · FROZEN · HISTORICAL · OF RECORD · DRAFT (B-7 ADR) · CURRENT — no act.
- R5 145 `mv -n` (0 failures) → `_scratch/_archive-2026-09/` (+ `MOVED.txt`, 145 lines): every top-level FILE dated before 2026-09-13, `README.md` excepted (name-dates and file-dates never disagree). Stay by date: `blocked-names.txt` (09-21) · `v86_device-skills-md5.txt` (09-28) · `skills-source.md5` (09-30). Dirs and `_to_delete/` untouched.
- R6 root: `START_HERE.md` (949 B) names the v67 prompt and the brief (left) — and `2026-09-27_v82_dispatch-text.md` as "the newest dispatch text (LIVE)": stale (v100 is live; v82's text is now under archive/dispatch-texts/). Unversioned; the hub's edit if any.
- R8 docs `055832c` · bench `ba846c2` · core `49455fc` · skills `e9a77a8`: untracked 0, porcelain 0, no locks; nothing changed.

## §2 The live citers of moved paths (`git grep -l -F <basename> -- '*.md' | grep -v archive/`; file:line)
348 citing-file pairs in all (none of the 91 uncited); 101 live, 74 of them audits — exhibits that cite the old path by design, each with its lines in the TSV's last column. The brief, the snapshot and the v100 text cite none. The 27 non-audit live pairs:
- `context/handoff/pm-handoff.md:35` the v99 text (v98 b5's line).
- `context/planning/improvement-register.md` :75,110 WU-PJ2 · :76 the BENCH-CORE-3 card · :105 the REHEARSAL-1 and REHEARSAL-1b prompts · :125 WU-J2.
- `context/lessons/pm-lessons.md` :371 the THURSDAY-ORDER Half-2 card · :377 the CHAR-sitting-2 prompt.
- `context/planning/2026-09-15_v75_PROGRAM-PLAN_…` :165 the THURSDAY-ORDER packet · :191 the T2b card · :224 the IR61 instruction + WU-IR61.
- `…2026-09-27_v82_THE-WEEKS-AHEAD_…:81` WU-IR67 · `…2026-10-02_v93_THE-HORIZON_…:85` the v93 text · `…2026-10-07_v99_decision-record.md:25` the BC8 card.
- `context/handoff/coder-handoff.md:40` the IR61 instruction + WU-IR61.
- `context/planning/phase-3-milestone-backlog.md:35` WU-DASH-SERVE (a STALE baseline).
- `context/research/2026-10-03_PAIRING-UX-1_return.md:4` its charter.
- the skill tree (not this lane's): `project-manager/references/laws-ledger.md` :49,58,76 the v66 synthesis · :73 THURSDAY-ORDER Half-2 + CHAR-sitting-2 · :79,82 the v84 DR · :81 the v82 DR · :83 the v83 DR; `…/review-and-quality.md:192` the v66 synthesis.
- this charter :26 the v66 synthesis.

## §3 For the hub at intake
Re-measure §0. Pointer edits are the hub's call — none is needed for resolution (every moved basename is unique; `git ls-files | grep -F` finds it): the register's five, pm-lessons' two, the v82/v93 plans, the v99 DR, coder-handoff :40, `START_HERE.md`'s v82 line (R6); the laws ledger's seven sit in W-SKILLS-11's tree. Flip this charter DISPATCH-READY → EXECUTED. 87 of the 145 `_scratch` names are cited in the record as `_scratch/<name>` (TSV) — now `_scratch/_archive-2026-09/<name>`.

## §4 The card (N = 94 = 91 R + 1 M + 2 A; the renames staged by `git mv`, the 12 status edits and the 2 audit files by explicit path — the pathspec file re-asserts them)
```
cd nexsys-hivemind
git --no-optional-locks add --pathspec-from-file=../_scratch/hygiene/2026-10-07_HIVE-CLEAN-4_stage-paths.txt
git --no-optional-locks diff --cached --name-status | wc -l   # 94
git --no-optional-locks diff --cached --name-status | grep -c '^R'   # 91
git --no-optional-locks status --porcelain -uall | grep -vc '^[MRA]  '   # 0
grep -c 'Co-Authored\|Claude-Session' ../_scratch/hygiene/2026-10-07_hivemind_HIVE-CLEAN-4_commit-msg.txt   # 0
git --no-optional-locks commit -F ../_scratch/hygiene/2026-10-07_hivemind_HIVE-CLEAN-4_commit-msg.txt
git --no-optional-locks push
```
Then `HIVE: LANDED <sha>`.

## §5 Deviations
- Counts vs the charter: 17 DRs, not 18 (no v91 DR); 145 `_scratch` files, not ≈ 110; `skills-source.md5` and `blocked-names.txt` are named in R5 but dated after 09-13 — left by the rule.
- The pathspec file lists the 94 present paths, not "both sides": `git add` refuses a removed path (`did not match any files`) — and that very `--dry-run` left a 0-byte `.git/index.lock` this mount would not let git unlink; renamed to `.git/stale-index-lock-hc4-dryrun` (the lane's one act outside the two verbs; Nick may delete it). The index was not written by it (re-asserted 92 → 92). The explicit `git add` likewise left `.git/objects/*/tmp_obj_*` temporaries it could not unlink (16 from this run, the return’s own re-stages counted; 191 are September’s) — the objects linked in place; each staged blob re-read equal to its file; every status edit 1+/1- (`--numstat -M`).
- The stamp is the charter's literal `(2026-10-07)`; the run was 2026-10-08. Read by range throughout; no body edited; nothing deleted.

RETURNED context/audits/2026-10-07_HIVE-CLEAN-4_return.md 8185 staged=94

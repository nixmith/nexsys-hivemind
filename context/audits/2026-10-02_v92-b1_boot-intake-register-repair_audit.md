<!--
file: context/audits/2026-10-02_v92-b1_boot-intake-register-repair_audit.md
purpose: v92 beat 1 — the boot at the bytes (the read-set, the five HEADs, the preflight's twelve), the two landings verified (`HIVE: LANDED 6a69bed` · `DOCS1: LANDED 055832c`), WUCP Phase 2 for DOCS-1 banked, and THE DEFECT FOUND AT BOOT: the register's IR-95/97/100 rows headless at `6a69bed` (the v90 b6 splice's literal backreferences) — the mechanism, the repair, the library's v2.
audience: the v92 hub · the v93 boot · Nick (§0 and §3)
state-type: audit (one beat)
status: FILED v92 beat 1 (Fri 2026-10-02 ~08:0x CT; instrument 2026-10-02T13:08:39Z)
-->

# v92 beat 1 — boot intake, the two landings, the register repair

## §0 Verdict
**The boot is clean (12/12; 40.6 KB); both landings hold at the bytes; DOCS-1's Phase 2 is banked. One defect of the hub's own, found at boot and repaired in this beat:** at `6a69bed` the improvement register's IR-95, IR-97 and IR-100 rows begin with the four bytes `\1 \2` — the v90 b6 splice passed regex backreferences to `sub_once`, which is a literal splice, and the rows' id, finding, source, fix and owner cells were overwritten. The three rows are restored from `124cf4c` whole with the suffix b6 intended; `splice_lib_v2.py` refuses the misuse and names every edited row after a write. The window's deliverable is unchanged: BC7's card by 17:30 CT, the re-mint first.

## §1 The boot, as run
| Step | Instrument | Result |
|---|---|---|
| `date -u` | `2026-10-02T12:42:18Z` | Fri 07:42 CT |
| The read-set | byte counts printed per range | 40.6 KB: the v67 prompt 13,017 · the chain 1,407 · the newest beat 2,477 · the snapshot 3,446 · the brief 11,973 · the v90 DR §3f + Carried ≈ 4,400 · §10's header + Fri/Sat–Sun rows ≈ 2,400 · seven lesson headings ≈ 1,500 |
| The five HEADs (one call) | `log -1` · `status --porcelain \| wc -l` · `rev-list --count origin/main..HEAD` · `rev-parse --abbrev-ref HEAD` · `ls .git/*.lock` | core `5b0e20c` · hivemind `6a69bed` · skills `e9a77a8` · bench `ede32c9` · docs `055832c`; 0 · 0 · `main` · 0 locks in all five |
| Check 1 | snapshot `last-verified:` | 2026-10-02 — PASS |
| Check 2 | the plan of record resolves (`git ls-files`) | `2026-09-27_v82_THE-WEEKS-AHEAD_program-and-company-plan.md` — PASS |
| Check 3 | commits since the snapshot's shas | hivemind +1 (the b5+b6 card) · docs +1 (the DOCS-1 landing) — the two cards the record handed; PASS |
| Check 4 | the counter | `19/20` in the snapshot and the brief — PASS |
| Check 5 | Open Risks | 12 unique `OR-` ids in the section = the snapshot's twelve — PASS |
| Check 6 | coder-handoff | the file present; its NEXT pointer LINK-READ-2 by D-v90-3 (the pointer line itself not re-grepped — disclosed) — PASS by the record |
| Check 7 | MODULE_CONTEXT.md | 21 files, 0 under 200 B — PASS |
| Check 8 | cross-agent-notes | 1 active entry — PASS |
| Check 9 | per-file md5, the three SOURCE trees vs the session's synced copies | 28/28 identical at the bytes (PM 10 · Coder 9 · FE 9) — PASS |
| Check 10 | the strategic map's cites vs `git ls-files` by basename | every real cite resolves in core (`0001-adr-adoption.md` · `01-event-model.md` · `12-lifecycle.md` · `CONTEXT.md` · `ARCHITECTURE.md` · `TESTING.md` · `MODULE_CONTEXT.md`); the `YYYY-*` names are the map's own templates — PASS |
| Check 11 | the snapshot's claims at source | `capability_reconcile` in 4 Java files; the landing subject names `integration-zigbee` — PASS |
| Check 12 | the three zero-greps, exclusions re-derived (KREFRESH-1 · `2026-10-02_` · one LIVE orchestrator prompt) | 0 · 0 · 0 — PASS (v91's and v92's texts LIVE in `handoff/` by the record; v92's flips to PASTED this beat) |

## §2 The two landings at the bytes
- **`HIVE: LANDED 6a69bed`** — `git show --stat`: 15 files (326+/55−); author Nick Smith; the trailer grep on the message 0; `origin/main` = HEAD; porcelain 0 after. The card was b5 + b6 as one (the b6 script's PEND branch), as the record said.
- **`DOCS1: LANDED 055832c`** — `git show --stat`: 10 files, +62/−8 (Doc 01 +18 · Doc 02 +2 · Doc 03 +21/−2 · Doc 07 +6 · Doc 08 +11/−2 · Doc 12 +2 · Doc 14 ±1 · AMD-event-time ±1 · AMD-59 ±2 · AMD-99 +2); author Nick Smith <nickdsmith1@gmail.com> Fri 07:30:15 CT; trailers 0; `research/returns/` carries no DOCS-1 file (the return lives at `context/audits/2026-10-01_DOCS-1_return.md` in the hivemind); `origin/main` = `055832c`. The stat equals the b6 audit §0's reading of `f7e8e72` (10 files, +62/−8) — the squash carried commit 1 whole and nothing else.
- **PR #1 (docs):** not re-executed. `gh api repos/nexsys-io/homesynapse-core-docs/pulls/1` → HTTP 403 "GitHub access to this repository is not enabled for this session". Its state is Nick's `PR1-docs: closed`, as every PR's state has been in this record.

## §3 THE DEFECT: the register's three headless rows (v90 b6)
- **The bytes.** At `6a69bed`, `context/planning/improvement-register.md` lines 107, 109 and 112 read `\1 \2; the docs row DONE at DOCS-1 (…); the word \`SKIPVOC:\`; the Java unit remains |` · `\1 \2; the docs row DONE at DOCS-1 (…); the word \`ACTTIME:\` |` · `\1 \2; the docs row DONE at DOCS-1 (…); the word \`PJCAT:\`; the mapping edit remains |`. At `124cf4c` the same rows were `| IR-95 | EXPORT-1's window (the first real grade) … | OPEN (v86 b1) |` (1,393 B) · `| IR-97 | Every row of an automation run carries the TRIGGER's \`event_time\` … | OPEN (v86 b1) |` (765 B) · `| IR-100 | \`permit_join_opened\` and \`permit_join_closed\` persist with the \`[SYSTEM]\` category fallback … | OPEN (v86 b3) |` (530 B).
- **The mechanism.** `splice_lib_v1.sub_once(text, pattern, repl)` returns `text[:m.start()] + repl + text[m.end():]` — repl is written literally. `_scratch/v90/b6/v90b6_splice.py:45–47` called it with `r"\1 \2; the docs row DONE …"` against `r"^(\| IR-95 \|.*\|) (OPEN [^|]*) \|$"` — a pattern written for `re.sub`'s expansion. The whole match (the whole row) was replaced by the literal repl. The script's post-write asserts named `| IR-112 |`, `| IR-115 |` and `CLOSED v90 b6` — not the three rows it had edited — so the splice passed and the card landed it.
- **The repair (this beat, inside the splice).** For each of the three ids: the row is taken whole from `git show 124cf4c:context/planning/improvement-register.md`; the pattern `^(\| IR-<n> \|.*\|) (OPEN [^|]*) \|$` is matched against THAT row; the new row is group 1 + ` ` + group 2 + the b6 suffix (the text after `\1 \2` in the b6 repl, byte for byte) + ` |`; the headless line at the same position is replaced by it (anchored on its exact bytes, found once). Asserted after: `| IR-95 |`, `| IR-97 |`, `| IR-100 |` each once; no line begins `\1`; rows beginning `| IR-` = 114 (110 at `124cf4c`, + 4 new); every other line of the register byte-identical to `6a69bed`.
- **The library.** `context/process/splice_lib_v2.py` = v1 byte for byte except: `sub_once` asserts no `\<digit>` or `\g<` in its repl; `sub_once_x` expands (`re.Match.expand`) and asserts no backreference survives; `assert_rows(text, *needles)` finds each needle exactly once. v1 stays in the tree (the record; never edited in place). Every beat script from v92 b1 loads v2 and asserts its md5.
- **The lesson** (`pm-lessons.md`, one mint): A LITERAL SPLICE WRITES A BACKREFERENCE AS BYTES; THE EDITED ROW IS ASSERTED BY ITS ID — folds into THE GUARDED-SPLICE LAW's text at the next skills pass as the PROBE-EVERY-CAP rule's sibling for content.
- **What it did not touch.** The three rows' substance (their findings, sources and fixes) was never lost from the record — `124cf4c` holds them; the DOCS-1 landing, the lessons and the other register rows of b6 are unaffected. The spine's claims about IR-95/97/100 at b6 ("the docs row DONE") were true of the suffix and are true of the repaired rows.

## §4 WUCP Phase 2 for DOCS-1 — banked on `DOCS1: LANDED 055832c`
IR-81 RETIRED (rows 1–4; the landing sha written into its row this beat); IR-95, IR-97, IR-100 carry "the docs row DONE at DOCS-1" with the unit still owed (the repaired rows); IR-90 unchanged (row 11's word `CONFIG-ERROR:` decides it at this window's close). No MODULE_CONTEXT (a docs repo). No deferred gate. Check 11: the notes' counts are the lane's reads at `5b0e20c`. The four Open questions stand as H10 words (the b6 DOCS-1 audit §3's recs; silence = the recs).

## §5 Layer 2
Re-executed: the five HEADs; every preflight check's instrument; both landings' `show --stat`, authors and trailer greps; the three register rows diffed against `124cf4c` (`git show`); the b6 splice's lines 45–47 read; the lib's `sub_once` body read; the dispatch text's four sentences grepped present. Not re-executed: PR #1's state (GitHub not enabled for this session); the Pi (BC7's sitting is the measurement); Fri's nightly digest line (unsaid; BC7's Part A reads it); the coder-handoff's NEXT pointer line (by D-v90-3).

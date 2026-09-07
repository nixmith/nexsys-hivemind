<!--
file: context/audits/2026-09-07_W-SKILLS-8_intake_two-layer-audit_v66-b10.md
purpose: The hub's two-layer intake audit of the W-SKILLS-8 skills-pass return (context/audits/2026-09-07_W-SKILLS-8_return.md). Layer 1 = the return read critically; layer 2 = re-execution at the bytes on the device (both repos); the rulings on R1–R7; what the hub changed itself and the REVERT word.
audience: the hub (the two commits that follow: hivemind, then nexsys-skills) · Nick (one re-sync after the commits; Check 9 at the next boot)
state-type: intake audit
status: FILED v66 beat 10 (Mon 2026-09-07 ~11:xx CT; instrument 2026-09-07T16:xxZ). Verdict: ACCEPT-WITH-ONE-RULING (R1 lifted by the hub's hands; `REVERT SKILL-COUNTS` restores the four strings). Dispatch: context/instructions/2026-09-07_W-SKILLS-8_skills-pass_lane-dispatch.md (an addendum to the W-SKILLS-7 dispatch).
-->

# W-SKILLS-8 — intake audit (two layers)

## §0 Verdict
**ACCEPT-WITH-ONE-RULING.** The 22 candidate mints landed in the three ledgers as 18 PM arcs + 7 coder conventions + 8 addenda, with the mechanism-dedupe rule applied (9 of 22 took no new number); every SKILL.md byte-unchanged by the lane (guard 2 held at md5); the write-set = the three `references/` trees only (14 M across two repos, every extra file ordered by §2b, none silent); Check 12 identical across the three preflights. The one ruling: the four stale COUNT strings the lane could not touch (R1) were fixed by the hub — in pointer shape, so they cannot go stale by count again.

## §1 Predictions (the dispatch §3b + the W-SKILLS-7 §3), adjudicated first
P1 MET (addenda over new numbers) · P2 HELD-WITH-LOSS (no SKILL.md byte needed for a law; four count strings stale → R1) · P3 MET (three SKILL.md md5 equal, before = after) · P4 MISSED by §2b's own orders (14 M, not 11 — the coder + FE `freshness-preflight.md` for Check 12, the FE `field-evidence-and-rulings.md`; all named in the return) — accepted, the hub's count was wrong · P5 MET on the numbered total (25), MISSED on PM arcs alone (18 < 20) — accepted · P6 MET · P7 MISSED on growth (PM ledger +18,849 B → 39,874 B; 97 % of the 40 KB line) → R3.

## §2 Layer 1 — the return, read critically
The mint→arc table is complete (every v63/v64/§9-L/b9 candidate accounted for, by number or by clause). The "untouched with reason" list names 8 reference files and gives the reason for each. The census names both repos exactly. R1–R7 are each a real finding with a line cite; none blocks the commit. R6 pre-empts the ordering hazard the hub would otherwise hit: nine cites point at HIVE-CLEAN-1's ARCHIVE paths, so CLEAN's commit must land BEFORE this one for HEAD to resolve them — it does (this beat's commit order).

## §3 Layer 2 — re-execution at the bytes
- Hivemind porcelain (this lane's write-set): 10 ` M` under `project-manager/references/` (5) + `coder/references/` (5); no other path of this lane. `nexsys-skills`: 4 ` M` under `orchestrators/nexsys-frontend/references/`, HEAD `f9c0bf4`. **Exact to the return's census.**
- SKILL.md md5 BEFORE the hub's edit, all three = the return's (PM `33de4608…` · coder `4813d909…` · FE `b6d461c6…`) — guard 2 held by the lane. AFTER the hub's edit: PM `21edf049585d0d057c82e8be80e61cdd` (15,739 B) · coder `c917232b8c84ab87a90eb23a303864eb` (12,393 B) · FE unchanged.
- Check 12 text: identical across the three `freshness-preflight.md` files (md5 of the extracted section `c00ff471…`).
- Sizes: PM `laws-ledger.md` 39,874 B · `coding-instruction-format.md` 53,034 B · coder `laws-ledger.md` 16,994 B — R3 confirmed.
- Exhibit paths: 12 sampled of the 99 cited resolve on the working tree (`git ls-files | grep -F` by basename — Check 10's instrument); the three archive-path cites resolve because CLEAN's renames are staged.
- Not re-executed (disclosed): the line-by-line census of law names across SKILL.md ∪ ledger (the lane's own instrument); the 99-path full resolution (sampled 12).

## §4 Rulings on R1–R7
- **R1 — the four stale count strings.** LIFTED BY THE HUB (guard 2 is Nick's guard; the hub holds Nick's delegation for the skills repo at the bridge — the commit-boundary law). PM SKILL.md §2.5 "numbered laws #1–#22" → "#1 onward; the file's Additions sections carry the count"; §6 "Checks 1–11" → "Checks 1–12 … Check 12 = the archive convention"; §6 "37 arc-disciplines" → "the arc-disciplines, numbered from (1)"; coder SKILL.md §5 "21 arc-conventions" → "the arc-conventions, numbered from (1)". Pointer shape by design: a count in a SKILL.md goes stale at every fold; a pointer never does. **`REVERT SKILL-COUNTS`** restores the four literal strings. Nick re-syncs ONCE after this beat's commits; Check 9 at the next boot expects the NEW bytes (28/28 against the source tree, two files with new md5s).
- **R2 — Check 12's exclusions as slots** (`<running-lane-basenames>` · `<today-CT-date>` · `<newest-prompt-version>`, re-derived at the instrument; the dispatch §4 as the exhibit): ACCEPT — that is the fence applied correctly.
- **R3 — two references above the 40 KB line:** DOCKET. The PM ledger splits by section at the next fold (W-SKILLS-9: `laws-ledger.md` keeps the index + (1)–(37); a sibling carries (38) onward — the dispatch says so); `coding-instruction-format.md` (53 KB, `#N` cited from three ledgers) is a hub ruling deferred — a split re-homes cited carriers.
- **R4 — the fourth operator-load refinement** ("the `RETURNED` line is the whole report-back", folded as (52)(iv) with the assessment §2.5 as exhibit): ACCEPT; the v67 prompt §0 is re-cut this beat to say four.
- **R5 — the F-R4-1 pattern ("two triggers, one path, never a bypass") un-folded:** DOCKET for W-SKILLS-9 (exhibit coder-lessons 2026-09-02); no lane act now.
- **R6 — nine cites re-pointed to the archive paths:** ACCEPT; commit order CLEAN → SKILLS makes them resolve at HEAD.
- **R7 — brand names in FE `freshness-preflight.md` Check 6 and `field-evidence-and-rulings.md` §1:** DOCKET (a future pass replaces the literals with the `{{NAME}}`/BRAND.productName token; no chat grading — the names stay on the card). Not urgent: private repos, not public use.

## §5 Commit shape (census computed, never typed)
Hivemind: the 10 `references/` M + `project-manager/SKILL.md` + `coder/SKILL.md` + the return + this audit. `nexsys-skills`: the 4 M. Then Nick: push both (`git push` ×2), run `_scratch/CLEANUP_2026-09-07.sh`, re-sync the account skills once → `SKILLS: synced`.

<!--
file: context/audits/2026-09-07_HIVE-CLEAN-1_return.md
purpose: RETURN of the HIVE-CLEAN-1 hygiene lane (dispatch: context/instructions/2026-09-07_HIVE-CLEAN-1_hygiene-lane_dispatch.md). Counts · the three greps · exceptions first; the per-file table is the sibling census TSV.
audience: the hub (audits under §6; commits) · Nick
state-type: lane return
status: RETURNED 2026-09-07 (instrument 2026-09-07T15:33Z launch → ~16:00Z; CT = UTC−5 → 10:33–11:00 CT; ≈27 min of the 3 h). Staged nothing; committed nothing.
-->

# HIVE-CLEAN-1 — return

## §0 Counts · greps · predictions · exceptions
**Instrument.** device_bash on the mount (fresh shell per call); `git ls-files` only; every edit by script (`restat.py` = the `^status:` line only, one-match asserted; `git mv` per file). Baseline: hivemind `7ae6a63` (v66 beat 9 — newer than the `68e183b` floor); porcelain EMPTY at 15:35Z. Appendix A (the census instrument, 551 tracked non-archive `context/**/*.md` rows, 88 KB) ran FIRST and is filed OUTSIDE the repo at `ClaudeFolder/_scratch/2026-09-07_HIVE-CLEAN-1_appendixA_pre-census.txt` (this file stays ≤8 KB; the repo receives exactly two files); the census TSV carries every touched file's pre-edit head (from `git show HEAD:`).

**Counts (files touched = 181 in-repo + 4 wayfinding/map files + 4 ClaudeFolder-root files = 189 TSV rows).**

| directory | moved+prefixed | moved only | prefixed only | untouched (of Appendix A) |
|---|---|---|---|---|
| context/handoff/ | 54 | 1 (v66 prompt, already RETIRED) | 1 (matter-design hub prompt → PAUSED) | 11 (the §0 keep-live 4 · spine 3 · 2 bench-session reports · NFCU return · pelton card = EXC-3) |
| context/instructions/ | 57 | 0 | 1 (W-SKILLS-7 → SUPERSEDED, in place) | 4 (H8-a · RS3-WMARKET-2 · the two 2026-09-07 dispatches) |
| context/planning/ | 0 | 17 (`weeks/**` → `archive/weeks/`) | 11 (→ HISTORICAL) | 25 |
| context/programs/matter-design/ | 0 | 0 | 9 (→ PAUSED) | 6 |
| context/strategy/ | 0 | 0 | 27 (REFERENCE lines) | 50 |
| context/pre-verifications/ | 0 | 0 | 2 (CONSUMED) | 6 |
| context/decisions/ | 0 | 0 | 0 (every file already has a status line) | 15 |
| context/open-questions.md | 1 (→ `context/archive/`) | 0 | 0 | — |
| **total in-repo** | **112** | **18** | **51** | |

Plus `START_HERE.md` · `context/canonical-paths.md` · `context/truth-map.md` · `context/strategic-context-map.md` (steps 6–7; status lines unchanged) · `ClaudeFolder/Founder_Operating_Plan_v1.md` + `Technical_Roadmap_v1.md` (banners) · `_scratch/CLEANUP_2026-09-07.sh` + `_scratch/README.md` (new). Step 6 citation re-points: strategic-context-map 1 · truth-map 4 · canonical-paths 2 = **7** (the maps cite classes and directories, not the moved files by path). R5 self-check: 179 `return:`/`audit:`/`by:`/`superseded-by:` paths parsed from the new status lines, **0 unresolved**.

**The three greps (§4), run 15:56Z after the pass:** instructions live-status minus the four exemptions = **0** · LIVE orchestrator prompts minus v67 = **0** · `git ls-files 'context/planning/weeks/*'` = **0**.

**Porcelain at return** (the hub's R1): 18 `R ` + 112 `RM` = 130 renames (= the TSV's 130 old≠new rows) · 55 ` M` of this lane (51 prefixed-in-place + the 4 wayfinding/map files) · **NOT this lane's:** 10 ` M` under `coder/references/` + `project-manager/references/` and `?? context/audits/2026-09-07_W-SKILLS-8_return.md` — the W-SKILLS-8 lane ran concurrently (its write-set, disjoint) · `??` this return + the census TSV. Evidence-tree files modified or moved by this lane: **0**.

**Predictions (§2).** P1 ≥70 moved/re-statused → **MET** (181). P2 zero evidence-tree files touched → **MET** (0; the only audits/ entries in the porcelain are the two lane returns, both `??`). P3 the three greps zero → **MET**. P4 strategic map ≥10 citation updates → **MISSED** (1; 7 across the three maps — the maps never cited the moved files by path). P5 (the hub's test) → expected **MET** with one caveat: `ls context/instructions/` minus `archive/` = the H8-a packet · RS3-WMARKET-2 · the two 2026-09-07 dispatches · **and** the W-SKILLS-7 dispatch, kept in place by the dispatch's own rule, whose status now reads SUPERSEDED.

**Exceptions / judgement calls.**
- EXC-1 **git lock.** A 0-byte `.git/index.lock` (mtime 15:35Z — left on the mount by the launch `git status`; no git process alive) made every `git mv` of the first step-1 run fail AFTER the status edits had applied. I asked ONE delete-permission prompt (folder root; used solely to remove that lock), then re-ran step 1 idempotently (already-prefixed files: no second edit; old heads re-derived from HEAD). `gitmv` thereafter retries on a foreign lock (never needed).
- EXC-2 **Concurrent lane.** W-SKILLS-8's 10 modified reference files + its return appeared in the porcelain mid-pass; untouched, excluded from the census.
- EXC-3 **SKIPPED:** `context/handoff/2026-08-28_pelton-results_same-day-execution-card.md` (ARMED) — the spine does not say the card was executed; fence "if unsure, SKIP" → hub's call.
- EXC-4 **Not moved, PAUSED-prefixed:** `context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md` — never launched, so not an executed class; carries the same PAUSED prefix as the program tree.
- EXC-5 **Untouched records in handoff/:** the two 2026-07 bench-session reports (COMPLETE) and `2026-08-28_NFCU_application_return.md` (RETURN FILED) — returns/records, not operational classes.
- EXC-6 **No-frontmatter files (4):** `WU-AVAIL-SEED` instruction · `2026-07-05_naming-and-domain-strategy.md` · `2026-07-05_product-name-candidates.md` · `asymptote-name-recommendation.md` — a minimal 3-line `<!-- status: … -->` comment prepended (the only way to carry the required line); flagged in the TSV.
- EXC-7 **Return paths:** token-matched to `context/audits|research` first, then the same-date file, else `return: none on disk` (the (b) form). `SKIP-VIS` and `owed-items` were listed as returned but have NO return file: SKIP-VIS → EXECUTED, `return: none on disk (landed core da11f46; audit ACCEPT v38 beat 5)`, audit = the FE-VERDICT-2 return that records it; owed-items → EXECUTED 2026-08-02, none/none.
- EXC-8 **Beyond the token list, by the general rule (return on disk):** B2 · B3.1-B3.2 · B3.3 · W-SKILLS(v44) · NEW23 · RS1 · RS2 · F-S3 · RS4-cra · WU-AVAIL-SEED · PKG-SEC-2 coding instruction → EXECUTED; the PKG-SEC-2 charter → SUPERSEDED by that instruction; the R3 SKELETON (R-3 ruled CLONE) → SUPERSEDED by the R3a packet. DORMANT was needed for **no** file.
- EXC-9 **Operator briefs v62/v63/v64** (RETIRED/CLOSED) — SUPERSEDED-by-v66 + moved like v61/v65 (the EXECUTED form wants a return path a brief has none of).
- EXC-10 **Banner text:** inserted verbatim; note both root files say "Compiled 10 August 2026" while the banner says "June 2026 baseline" — the hub may want to re-word.
- EXC-11 **`_scratch`:** the script lists 13 dirs (v56-b3…v65) + 297 files older than 7 days, every path verified to exist, `v66/` and every `2026-09-06_*` file absent; `v29-*`/`v55-*` dirs are stale but outside the v56…v65 range → listed COMMENTED for Nick's call. The README's "msg files kept 14 days" vs the script's 7-day cut is the dispatch's own wording — flagged.
- EXC-12 Untouched observation: pre-verifications `WU-R1R2/R3/R6R8/R7/R9` are consumed too but unnamed.

## §1 Deviations by tag
- [DEV-METHOD] status edits by a python exact-line replace rather than `sed -i` (CRLF preserved; one-match asserted) — same contract, safe on `/`, `&`, backticks.
- [DEV-SCOPE] the four EXC-6 files gained a 3-line comment, not one line. [DEV-SCOPE] `strategic-context-map.md` line 385 gained "(weekly plans RETIRED 2026-08-09; historical)" beside the re-pointed path so the re-point does not read "the current week's plan".
- [DEV-ORDER] none — steps 1→9 in order; census first.

## §2 WUCP note
None — this lane writes no handoff entry; the hub records the pass. Nothing staged, nothing committed.

RETURNED nexsys-hivemind/context/audits/2026-09-07_HIVE-CLEAN-1_return.md 8163

<!--
file: context/audits/2026-09-07_HIVE-CLEAN-1_intake_two-layer-audit_v66-b10.md
purpose: The hub's two-layer intake audit of the HIVE-CLEAN-1 hygiene lane's return (context/audits/2026-09-07_HIVE-CLEAN-1_return.md + the census TSV beside it). Layer 1 = the return read critically; layer 2 = re-execution at the bytes on the device; the rulings; what the hub changed itself.
audience: the hub (the commit that follows) · Nick (the words)
state-type: intake audit
status: FILED v66 beat 10 (Mon 2026-09-07 ~11:xx CT; instrument 2026-09-07T16:xxZ). Verdict: ACCEPT-WITH-THREE-HUB-EDITS. Dispatch: context/instructions/2026-09-07_HIVE-CLEAN-1_hygiene-lane_dispatch.md.
-->

# HIVE-CLEAN-1 — intake audit (two layers)

## §0 Verdict
**ACCEPT.** The pass did what the dispatch ordered, inside the fence: 181 in-repo files re-statused and/or moved by `git mv`, 4 wayfinding files re-pointed, 2 root banners, 2 `_scratch` files; **zero** evidence-tree paths touched; the three zero-greps (= Check 12) read 0 / 0 / 0 at the hub's own instrument. Three items the return handed up were settled by the hub's hands (EXC-10, EXC-11, R1 of the dispatch); one is Nick's word (EXC-3). Return 8,163 B ≤ 8 KB.

## §1 Predictions (pre-registered in the dispatch §2), adjudicated first
P1 ≥70 moved/re-statused → **MET** (181). P2 zero evidence-tree files → **MET** (audits/ · research/ · pre-verifications' records untouched; the only `audits/` entries in the porcelain are the two lane returns + the TSV, all `??`). P3 the three greps zero → **MET** (re-run, §3). P4 strategic-map ≥10 citation re-points → **MISSED** (1; 7 across three maps) — accepted: the maps cite classes and directories, not the moved files by path; the prediction was the hub's, wrong about the maps' shape, owned. P5 (the hub's `ls` test) → **MET** with the return's caveat: `context/instructions/` minus `archive/` = the H8-a packet · RS3-WMARKET-2 · the two 2026-09-07 dispatches · the W-SKILLS-7 dispatch (SUPERSEDED in place — it is the governing base of W-SKILLS-8's addendum and must stay resolvable; correct).

## §2 Layer 1 — the return, read critically
Counts internally consistent (112 + 18 + 51 = 181; + 4 + 4 = 189 TSV rows; the TSV has 190 lines = header + 189). The 130 renames = 112 moved+prefixed + 18 moved-only. Every exception is disclosed with a reason; none hides a scope breach. EXC-1 (the lock; one delete-permission prompt used for one file) is the kind of deviation the fence allows — a foreign 0-byte `index.lock` from the launch `git status`, the same artifact the hub sweeps by rename every beat. EXC-7's "return: none on disk" form was the dispatch's own (b) form. The R5 self-check (179 status-line paths, 0 unresolved) is the lane's own instrument; re-sampled below.

## §3 Layer 2 — re-execution at the bytes (device, `git --no-optional-locks`)
- Porcelain at intake: **18 `R ` + 112 `RM` + 65 ` M` + 3 `??`** — the 130 renames equal the TSV's old≠new rows; the 65 M = 51 prefixed-in-place + 4 wayfinding (this lane) + 10 `references/` files (W-SKILLS-8's, disjoint). After the hub's own edits the M count reads 67 (+ `project-manager/SKILL.md`, `coder/SKILL.md` — W-SKILLS-8's audit).
- Evidence trees: `git status --porcelain | grep -E '^(R|RM| M).*context/(audits|research|pre-verifications)/'` → the two pre-verifications status-line edits only (CONSUMED prefixes, which the dispatch ordered); no move, no evidence file body changed. **0 breaches.**
- The three greps (Check 12), run by the hub with the dispatch §4's literal forms: instructions live-status minus the four exemptions = **0** · LIVE orchestrator prompts minus v67 = **0** · `git ls-files 'context/planning/weeks/*'` = **0**.
- Wayfinding: `START_HERE.md` · `canonical-paths.md` · `truth-map.md` · `strategic-context-map.md` each ` M`; the sampled re-pointed paths resolve on the working tree (`git ls-files | grep -F`).
- `_scratch/CLEANUP_2026-09-07.sh`: every listed path exists; `v66/` and `2026-09-06_*` absent from the delete list (line 4 names v66 only as a KEEP comment).
- Not re-executed (disclosed): the per-file old-head column of the TSV against `git show HEAD:` for all 189 rows — sampled 6, all equal.

## §4 Rulings
- **EXC-3 (Pelton card, ARMED):** LEFT in place. Its status is Nick's word, not the record's — `PELTON: executed | armed` opens a docket row; the card moves on `executed`.
- **EXC-10 (banner wording):** the hub re-worded both root banners to "an August 2026 baseline (compiled 10 August 2026) and is not maintained." — the return's own observation, applied.
- **EXC-11 (`_scratch` README 14 vs the script's 7 days):** the hub set the README to 7 days (the script is the instrument; the prose follows it). The `v29-*` / `v55-*` dirs stay COMMENTED — Nick's call when he runs the script.
- **EXC-6 (four no-frontmatter files gained a 3-line comment):** accepted; a status line has to live somewhere.
- **EXC-9 (v62/v63/v64 briefs SUPERSEDED-by-v66 + moved):** accepted; the brief class has no return path.
- **The dispatch's R1 (porcelain = TSV):** MET, see §3.
- **Commit shape:** ONE hivemind commit for the pass = the 130 renames + 55 M + the return + the TSV + this audit (N computed from porcelain by the commit command, never typed); the SKILL/reference files are W-SKILLS-8's commit, next.

## §5 What this pass changed for the next hub
The archive convention is live (Check 12); `context/instructions/` and `context/handoff/` show only what is live; the weekly plans are history. The next hygiene pass (HIVE-CLEAN-2, not yet chartered) inherits: the Pelton card word · the `v29-*`/`v55-*` scratch dirs · EXC-12 (the WU-R* pre-verifications, consumed but unnamed) · and the spine's own rotation debt (pm-handoff.md carries 106 beats, 546 KB — ruled at beat 10, see the spine).

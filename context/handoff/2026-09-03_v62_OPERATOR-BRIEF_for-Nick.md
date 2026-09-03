<!--
file: context/handoff/2026-09-03_v62_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF for the v62 session — every act he is asked to perform, in order, FULLY ARTICULATED (his standing directive, 2026-09-03: "ensure that any/all instructions specifically for me are explicit and fully articulated"). Each act carries WHAT · WHY · HOW (the exact command or paste) · EXPECTED RESULT · REPORT BACK (the exact line to paste to the hub). Supersedes context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md (its §A/§C/§D are DONE).
audience: Nick
state-type: operator brief
status: LIVE at v62 beat 1 (Thu 2026-09-03, instrument 19:2xZ). Revised whole at each v62 beat that changes an act. The spine (pm-handoff newest beat) outranks this file if they disagree.
-->

# Operator brief — what Nick does, in order (v62, beat 1)

## §0 What is already done (no action)
- **PKG-SEC-2 `ef02d13`: CI GREEN** — your word, banked at v62 beat 1 (law 16). The deferred `./gradlew check` gate is CLOSED. Nothing left on this commit.
- **Skills: all three role skills verified byte-identical** at the account copies — the hub's own md5 over 28 files (PM 10 · Coder 9 · Frontend 9). Check 9 PASS. Nothing left.
- **The v62 boot ran**: zero drift on five HEADs; freshness preflight PASS 11/11; the deep read of the docs/strategy/planning/founder documents filed at `context/audits/2026-09-03_v62-b1_boot-grounding_docs-and-strategy_validation.md` (its §0 is the 12-line executive card; read that, not the whole file).
- **O-2: CLOSED** (measured 09-03 03:10Z). **The s31 read: ACCEPT.** The 09-03 nightly PASSED 8/9.

## §A The hivemind push — NOW (≤1 min)
- **WHAT:** push the hivemind repo (it is 2 commits ahead of origin after this beat: v61 beat 12 + v62 beat 1).
- **WHY:** the spine is only durable once it is on origin; the commit-boundary law makes push YOUR act, always.
- **HOW** (git-bash):
  ```bash
  cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind
  git status -sb            # EXPECT the first line: "## main...origin/main [ahead 2]"
  git push origin main
  git status -sb            # EXPECT: "## main...origin/main"  (no "[ahead N]")
  ```
- **EXPECTED RESULT:** the push prints a `54f2be9..<v62-b1 sha>  main -> main` line; `status -sb` shows no `[ahead N]`.
- **IF NOT:** paste the full terminal output to the hub. Do not force-push; do not re-run.
- **REPORT BACK:** `hivemind pushed <old>..<new>` (copy the line git prints).

## §B The words — Fri–Sat 09-05/06, or any earlier hour (~1 h reading, ONE message)
- **WHAT:** your rulings on the five strategy questions (R-1..R-5) and the 16 docket rows.
- **WHY:** every charter finalizes on words instead of slots; v1.2 becomes the strategy of record; the fall's engineering (R-4b · R-4.5/R-5 · CG · FAILCHAN) proceeds on ruled rows.
- **HOW — read, in this order (all on disk, all ≤ 25 KB):**
  1. `context/planning/2026-09-02_R10-sitting_DELIBERATION-GUIDE_for-Nick.md` — the walkthrough (Parts 1–5). One currency note the file does not yet carry: its `:44` line about O-2 being "a step in R-4b's packet" is stale — O-2 is CLOSED/MEASURED; nothing is owed on it.
  2. `context/strategy/2026-09-02_v61-b2_strategy-beat_card_convergence-flip-arc.md` — R-1..R-5 with the recs and the v1.2 text A-1..A-7.
  3. `context/planning/2026-09-02_R10-docket_ruling-cards_v61-b3.md` — the 16 rows (≤2 KB each). **Already worded by your dispatches: Row 10 (a) and Row 13 (a′). Row 6's premise is measured. Row 16 is ruled at H8 — no word needed now.**
  4. Where the hub wants YOUR eyes specifically: **Row 2** (the external-agent-interface posture — a company-shape call) and **Row 12's fallback date** (09-14; F-R4-1 landed early, so (a) is on track and the fallback should not fire — confirm or move the date).
- **THE ANSWER SHAPE** (one message; copy and fill):
  ```
  STRATEGY: R-1 <a|b|c|d> · R-2 <a|b|c> · R-3 <a|b|c> · R-4 <a|b> · R-5 <a|b>
  DOCKET:   ADOPT-ALL-RECS                    ← or overrides, e.g.  Row 2 HOLD · Row 12 b
  OPTIONAL: TIER-2 GO
  ```
  Also lawful: `DELEGATE` (the hub decides on the V/C/I frame and records it, refutable by your one word) · `EDIT Row N: <your text>` · `REVERT <MINT-NARROW|RATIFY|RATIFY-PLAN>`.
- **EXPECTED RESULT:** the hub splices the words the same beat: the plan's rows · the OR register · v1.2 A-1..A-7 · the ruling slots of every charter. You see one census-exact commit and a one-line confirmation per row.
- **REPORT BACK:** the filled block above, as one message. Nothing else is needed.

## §C The brand paste loop — ≤15 min when it fires
- **WHAT:** Erik's reply (the VERDOMO comprehensive quote), or the nudge if none.
- **WHY:** the go-ahead fires the same day as the quote (assessment §5) → the comprehensive (~1 wk) → the written opinion → FILE §1(b) cl. 9 + 42 → the .com walk. **Hard stop Fri 09-18.**
- **HOW:**
  - If Erik has replied: paste the reply IN FULL to the hub (headers included). The hub keys the tree (assessment §4) and hands you the go-ahead text the same session.
  - If NO reply by **Fri 09-04 midday**, send this, verbatim:
    > Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick.
- **FENCES (standing, unchanged by anything this session):** no public VERDOMO use; no .com purchase; no handles; no repo rename; counsel hears a candidate at commissioning only. **No name-by-name grading in chat.**
- **REPORT BACK:** `Erik: <reply pasted below | nudge sent <time>>`.

## §D R-4b's day — Sat or Sun 09-06/07, ~3 h of your hands
- **WHAT:** the four-of-four re-representation on the held card (`hs-fresh`) with the CI-built artifact that carries F-R4-1 + PKG-SEC-2 — criterion 0 = the 0x0061 hop's first ⏺; C-002 mints on four-of-four.
- **WHY:** the weekend's hardware hour is the highest-leverage hour of the fortnight; C-002 (the WIDE claim) is fenced to it.
- **HOW:** the hub authors the navigator packet at v62 beat 2 (Block 1) — you will receive its path; it carries every paste block self-contained (§8 playbook contract), including **step 0a** (SET `permit_join_duration` on the held card for the run and remove it after — since PKG-SEC-2 an ABSENT key = NO join window, and F-R4-1's H-ii admits only inside one) and **step 0b** (pre-validate the held card's `integrations/zigbee.yaml` against the fragment: unknown keys WARN, out-of-range ERROR + key REMOVED, boot continues). **Do not start before the packet is on disk.**
- **WHAT YOU NEED ON HAND:** the held card (`hs-fresh`) in the Pi for the session and the bench card back afterwards (the nightly runs on the bench card at 03:30 CT — a swap DELAYS it; the spine records the shifted stamp) · the arm64 `.deb` from the green CI run on `ef02d13` (the packet names the artifact and its install path) · ssh to `nick@hs-fresh.local` (the packet's first line checks `hostname` = `hs-fresh`).
- **REPORT BACK NOW:** `R-4b: <Sat | Sun>` — one word, so the packet is time-boxed to your day.

## §E E1 — the Annex I paste (~1 min; once; before the next smart-home decision)
- **WHAT:** the EU Machinery Regulation 2023/1230 Annex I, Parts A and B, pasted verbatim with today's date.
- **WHY:** W-C6 (the regulatory read) closes on the primary text, not a summary; every later "is this Class I?" sentence cites it.
- **HOW:** open https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng → find **ANNEX I** → copy **PART A** and **PART B** in full → paste to the hub with the line `E1 Annex I, read <YYYY-MM-DD>` on top.
- **REPORT BACK:** the paste itself is the report.

## §F The docs-repo correction commit — AFTER the hub hands you the block (Block 4; not yet)
- **WHAT:** ONE commit in `homesynapse-core-docs` (your hands only) carrying: the Doc 12 §3.3 correction note (the b11 audit R2 paragraph) + four currency fixes the boot read found (the invariants file's missing §42–§47 headings · the Glossary's `UlidCreator` line · the Locked Decisions "§18" → "§14" references · the navigation index's watermark lines). Locked-doc BODIES are never edited — correction notes only (the AMD-71 form at Doc 06 `:129`).
- **WHY:** three of the four are dangling cross-references any lane will hit; the Doc 12 note is chartered at v61 b11.
- **HOW:** the hub will hand you a self-contained paste block: the exact `sed`/patch lines, the census card (N M), the msg file at `../_scratch/2026-09-03_docs_<name>_commit-msg.txt`, and the porcelain assert. Nothing to do until then.
- **REPORT BACK (then):** `docs committed <sha>, pushed` + the `git status --porcelain` line (must be empty).

## §G Decisions the hub needs from you (H10 — one word each; any time, not blocking)
1. **EXITCODE-UNWIRED (new, source-verified this boot).** `app/.../ExitCode.java` defines `CONFIGURATION_FAILURE(10)` etc., but nothing calls it: `Main.main` is `throws Exception`, `manager.start()` is unwrapped, and `HomeSynapseCore.start()` re-throws a fatal — so a bad config exits **1**, not 10; the unit's `RestartPreventExitStatus=10` can never match, and a deterministic bad config restart-loops to the start limit (5 in 300 s) — the exact loop the unit's own comment says it prevents. **Options:** (a) wire it — rides the FAILCHAN charter as instance 5 (catch at `main`, map FATAL subsystem → code, `System.exit(code)` after teardown); (b) retire the unit line and the enum (honest but loses the deterministic-config guard); (c) hold. **PM rec: (a)** — it is the same class, the same files, one lane. **Refutable-by:** a design ruling that `Main` must never call `System.exit` (none on record). Word: `EXITCODE: a|b|c`.
2. **The founder-plan dates the spine does not carry.** Your FOP names **EU market posture — decide by 11 Sep 2026** (CRA reporting duties) and **Activate Fellowship Cohort 2027 — opens 15 Sep 2026** (0 % equity). The v1.2 text A-4 absorbs only the NSF row. **Options:** (a) add both as A-4 calendar rows (one word each when their date comes: `EU: ship|defer` · `Activate: apply|hold`); (b) decline them by name in v1.2 (the R-3(b) form); (c) EU only. **PM rec: (a)** — a declined row is a decision too, and the FOP marked the EU one as gating "this whole section." Word: `FOP-DATES: a|b|c`.
3. **The Pelton-week plan's four orphan rows** (Doc 09 §15 Q1 fold · the JDK trajectory · the IR emit question · the events endpoint) never entered the 16 cards. **Options:** (a) docket addendum rows 22–25 now, H10 form, for the R-5 charter; (b) declined by name. **PM rec: (a)**. Word: `ORPHANS: a|b`.

## §H Dated tripwires (the hub watches; you act only where named)
**Fri 09-04 midday** the Erik nudge (§C) · **09-04..08** IFA (fifth-fragment watch; hub) · **09-07** SCITT CCF LC ends (hub: record the outcome, read at source) · **09-09** the Apple one-liner paste (hub hands you the §9-2 paste that morning) · **09-11** EU posture (your word, §G-2) · **09-14** the R-4b fallback date (Row 12) · **09-15** Activate opens (your word, §G-2) · **09-17** Silabs · **09-18 THE BRAND HARD STOP** · **10-01** the quarterly gate check (registered office · the LICENSE-flip gate · NFCU share-minimum · the flip's chain) · **10-31** the rename-slip fallback.

## §I What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · re-run CI on `main` · re-run O-2 · touch s31 or the nightly · answer E1 twice · read the whole grounding audit (its §0 suffices) · edit a Locked-doc body.

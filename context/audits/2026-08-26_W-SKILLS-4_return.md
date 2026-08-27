<!--
file: context/audits/2026-08-26_W-SKILLS-4_return.md
purpose: Lane return for W-SKILLS-4 — the launch-cost + conventions pass (v56 beat 4 dispatch), executed as a dedicated fresh Cowork lane (remote; device bridge) per `context/instructions/2026-08-23_skills-lane_W-SKILLS-4_launch-cost-and-conventions_brief.md`. Filename dated by the operator-day FILED in America/Chicago — Wed 2026-08-26, 20:03 CDT, re-derived at the instrument (`TZ=America/Chicago date`); the session banner read 2026-08-27 UTC (arc-discipline 4 + the PI-TZ/UTC-banner law).
audience: the hub (its W-SKILLS-4 ratification beat) + Nick (the commit + the mirror copy, Check 9)
state-type: audit / lane return
status: FILED 2026-08-26. The lane COMMITTED NOTHING — worktree edits only; the hub audits, Nick commits, then copies the mirrors.
laws-held: write-isolation (exactly SIX files under the two chartered trees + this return; nothing else under `context/**`; no spine, no strategy, no core/bench/docs, no mirror, no MANIFEST touch) · every moved byte `cmp`-identical at its new carrier · state-pointer discipline (no project state entered any skill file; the fence scan is §4) · pointer-not-copy on every added line · NO attribution trailers (nothing staged) · evidence over instruction: every brief/bytes mismatch FLAGGED in §4, none silently deviated.
-->

# W-SKILLS-4 — the launch-cost + conventions pass (lane return)

## §0 The census verdict

**`project-manager/SKILL.md` — 60-in / 60-out, every name surviving, ZERO retirements, ZERO orphans, the four rule lists BYTE-UNCHANGED.** Mechanical extraction over both trees (regex over the masthead, set-compared): arc-disciplines 37→37 (lost = ∅, new = ∅, order identical) · durable D1–D18 18→18 (lost = ∅, new = ∅) · strategy-layer 4→4 and state-pointer 1→1 by construction — both LINES are byte-identical, so the prior census's own counts carry. `diff` of the whole file: **exactly one hunk, `13,14c13,14`** — the two provenance lines. Body `:15–EOF` byte-identical (diff-verified).

**`coder/SKILL.md` — 33-in / 33-out, every name surviving, ZERO retirements.** arc-conventions 21→21 (lost = ∅, new = ∅) · durable-build-disciplines, strategy-layer and state-pointer LINES byte-identical (8 · 3 · 1 carry by construction). Hunks: `13c13` (masthead stamp) + `315,316c315,316` (§7a steps 2–3 — the P8 convention + the lesson-size pointer). No new numbered item; two clause-gains in the body, named in the masthead.

**`nexsys-frontend/SKILL.md` — 39-in / 40-out UNTOUCHED, 0-byte delta** (measure-only, §1.3). **`coder/CLAUDE.md`, `coder/references/java-patterns.md`, `coder/references/testing-standards.md`** — not censused files; per-file deltas exact in §1/§3, zero collateral hunks. **`project-manager/references/pass-history.md`** — NEW carrier, carries no rule (§2).

**Retirement, by name (the only one; P7, pre-ratified):** the coder Tier-1 row **"read the current week's plan in `../context/planning/weeks/`"** ×3 (`coder/CLAUDE.md` `:23`, `:57`, `:89`) — retired on **Nick's ruling of 2026-08-09** that weekly plans are RETIRED (carried at WUCP §Phase 2 Step 7 "RETIRED (weekly plans)" and at `context/canonical-paths.md:24`), on W-HIVE-1 P7 and the five-lane intake's §1 routing (`ROUTED to W-SKILLS-4`). It was a READ-LIST row, not a rule in any census list; its replacement is quoted in §3(b). Nothing else retires.

Stop-gates: the brief copy dispatched verified byte-identical to the in-repo brief (Read of both) · W-HIVE-1 §3 P6–P8 + §4b, the intake audit §1, the W-SKILLS-3 return (the census form), `coder/CLAUDE.md` whole, the coder preflight, the R-9 return §WUCP, `coder-lessons.md` — all read whole before any edit · the six edit targets staged at the device and edited in the worktree; **no `.claude/skills/**` mirror touched**.

## §1 Per-file before / after, and the per-launch saving

**Instrument, disclosed:** bytes = `wc -c` at the edited objects (re-verified after every write); tokens = the Claude BPE tokenizer in `anthropic==0.21.3` (`count_tokens`) — the SAME instrument as v44 / W-SKILLS-2 / W-SKILLS-3, and the chain stays closed-loop: **this pass's before-values reproduce W-SKILLS-3's after-values to the token** (PM 13,723 · coder 9,028 · FE 10,988) — the fourth consecutive pass on one continuous token record.

| File | bytes before → after | Δ B | tokens before → after | Δ tok | hunks |
|---|---|---:|---|---:|---|
| `project-manager/SKILL.md` | 53,020 → **49,676** | **−3,344** | 13,723 → **12,717** | **−1,006** | `13,14c13,14` |
| `project-manager/references/pass-history.md` (NEW; not a launch read) | 0 → 5,850 | +5,850 | 0 → 1,763 | +1,763 | new file |
| `coder/CLAUDE.md` | 10,426 → 12,275 | +1,849 | 2,744 → 3,271 | +527 | `8c8` `23c23` `34,35c34,35` `49a50` `57c58` `89c90` `118c119` |
| `coder/SKILL.md` | 35,667 → 36,674 | +1,007 | 9,028 → 9,319 | +291 | `13c13` `315,316c315,316` |
| `coder/references/java-patterns.md` (Tier 2) | 27,787 → 29,565 | +1,778 | 7,199 → 7,685 | +486 | `8c8` `626a627,632` |
| `coder/references/testing-standards.md` (Tier 2) | 17,946 → 19,141 | +1,195 | 4,536 → 4,866 | +330 | `8c8` `465a466,469` |
| `nexsys-frontend/SKILL.md` | 41,636 → 41,636 | 0 | 10,988 → 10,988 | 0 | none |

**1.1 Hub launch: −3,344 B / −1,006 tok per launch (−6.3 % of the file).** The masthead falls 24,599 → 21,255 B; its provenance share 4,016 → 672 B (the two replacement lines, 379 + 293). The brief's arithmetic target (≤ 49,000) is infeasible by construction — see §4.1.

**1.2 Coder launch: net −4,069 B / ≈ −1,242 tok per launch, and the growth of the handoff chain STOPS.** The retired Tier-1 row cost the `2026-W31_jul27-aug02.md` read: **6,925 B / 2,060 tok, measured** (the brief's figure reproduced at the object). The two always-loaded carriers grow +2,856 B / +818 tok for the three conventions (P7's pointer, P8, §1(d)). The two references are Tier-2 reads (loaded for Java / test work, not at launch): +2,973 B for the three R-9 folds. **P8's compounding half:** `coder-handoff.md :8` measured **6,794 B / 6 segments today** — up from W-HIVE-1's 4,302 B on 08-22, i.e. **+2,492 B in ONE closeout (R-7b)**. Under the convention the next closeout adds 0 B to the frontmatter; the hub's rotation (folding the five segment-only facts first) takes the line to P8's ~467 B.

**1.3 FE launch: 0 B this pass — measured for the FE-half charter.** `nexsys-frontend/SKILL.md` 41,636 B = yaml 1,021 · **masthead 5,195 (12.5 %)** · **body 35,420 (85.1 %)**. Masthead split: head-fields 454 · `status:` 2,554 (the current v1.11 segment 464 + a `Prior:` tail of v1.10 + v1.9 = **2,090**) · `version-history:` **747** ("PROVENANCE, not law" of itself) · `truth:` block 1,075 · `verify:` 360. **Mechanically separable provenance = 2,837 B (6.8 %)** — the `version-history:` line exactly as separable as the PM `pass-history:`; the `status:` `Prior:` tail as separable as the PM `last-verified:` `Prior:` segments (the v1.9 segment records two retirements + one merge BY NAME with their surviving-half carriers; it is a census RECORD, not a rule, and its return is already pointed). Same treatment would yield ≈ −2,400 B / −650 tok per FE launch. **Not executed:** the charge is measure-only and the treatment needs a new `references/pass-history.md`, which would be files 7–8 against the brief's ≤ 6 fence. **The finding that matters for the charter: the FE's launch cost is 85 % BODY** (§4a–§4e's folded law surfaces + §5–§8) — the FE-half pass is a body pass, not a masthead pass. **The coder masthead, same split, unchartered:** `last-verified:` 1,482 + `pass-history:` 823 = **2,305 B (6.5 %)** of every coder launch is provenance of the same class as (a)'s — a one-file-plus-carrier move for W-SKILLS-5.

## §2 The moved provenance — carriers and quoted heads

**Carrier: `project-manager/references/pass-history.md` (NEW, 5,850 B, 23 lines; masthead in the house form; NOT a launch read).** Both moved lines are **byte-identical** to the baseline `SKILL.md :13` and `:14` including their newlines — extracted at the recorded offsets and `cmp`'d: `:13` (2,950 B) at carrier offset 1,704, **rc = 0**; `:14` (1,066 B) at offset 4,784, **rc = 0**. The hub can re-derive: `sed -n 13p` / `14p` of the baseline SKILL.md at the pre-commit object vs the corresponding lines of the carrier.

Quoted head of the carrier (its masthead `purpose:` + `update-cadence:`):

> `purpose: PROVENANCE carrier for project-manager/SKILL.md — the skills-pass census narratives and the pass ledger that used to ride the SKILL.md masthead at every hub launch (W-SKILLS-4, charge (a): 4,016 B of provenance moved here VERBATIM; no rule lives in this file). Also carries the SIBLING-CARRIER INDEX (rules minted by earlier passes that live at other carriers), which a future census must keep resolvable.`
> `update-cadence: per skills pass — SKILL.md last-verified: keeps ONLY the newest pass's ≤ 400 B census verdict + return pointer; the demoted verdict line moves here whole, newest first, under §1.`

Structure: `§1 Demoted last-verified: verdict lines (newest first)` → the 2,950 B line whole (W-SKILLS-3 → W-SKILLS-2 → v44 narratives, including the H7/H8 and SK-INV-02 carrier pointers) · `§2 The pass ledger + THE SIBLING-CARRIER INDEX` → the 1,066 B line whole (the 2026-07 ledger + the four sibling-carrier entries: playbook §8 addenda / licensing re-grounding → constraint-enforcement / Build-Verification reconciliation → CLAUDE.md / lock-free porcelain + Check-6 → the coder preflight). **The `update-cadence:` sentence is the one convention this file introduces** (disclosed): future passes prepend a ≤ 400 B verdict at SKILL.md `:13` and demote the prior line here whole — the P2 pointer-form applied to a skill masthead.

The two replacement lines in `project-manager/SKILL.md` (379 B + 293 B, both ≤ the brief's 400):

> `last-verified: 2026-08-26 (**W-SKILLS-4** — the launch-cost + conventions pass. **RULE CENSUS 60-in / 60-out, every name surviving, zero retirements; the four rule lists BYTE-UNCHANGED** (arc-disciplines 37 · durable D1–D18 · strategy-layer 4 · state-pointer 1). Return: context/audits/2026-08-26_W-SKILLS-4_return.md. Prior verdicts: references/pass-history.md §1.)`
> `pass-history (PROVENANCE, not law — no rule lives on this line): moved WHOLE to references/pass-history.md §2 (the 2026-07 pass ledger + THE SIBLING-CARRIER INDEX of rules minted by earlier passes that live at other carriers — read it before any census so those names stay resolvable).`

## §3 The convention diffs, verbatim

**(b) P7 — `coder/CLAUDE.md`, the three rows** (`<` before / `>` after):

```
:23  < 2. Read the current week's plan in `../context/planning/weeks/` — what Nick is working on
     > 2. **The plan of record = the newest `../context/handoff/coder-handoff.md` entry + your active instruction.** If either points at a `../context/planning/*plan-of-record.md`, the NEWEST such file is the horizon — reached by that pointer only. (`planning/weeks/` is RETIRED — Nick 2026-08-09, `canonical-paths.md` — never a launch read.)
:57  < - PROJECT_SNAPSHOT.md, current week's plan, cross-agent notes, your handoff file
     > - PROJECT_SNAPSHOT.md, cross-agent notes, your handoff file (its newest entry + the active instruction = the plan of record; no weekly plan — retired)
:89  < - `../context/planning/weeks/` — current weekly plan (read for context on what Nick is working on)
     > - `../context/planning/` — the newest `*plan-of-record.md` is the horizon, read BY POINTER only (from your instruction or the newest handoff entry); `weeks/` is RETIRED (Nick 2026-08-09) — historical, never a launch read
```

**(c) P8 — the handoff-entry convention.** `coder/CLAUDE.md :34` (WUCP Phase 1 step 2), appended after the Deferred-Build-Gate clause:

> **THE HANDOFF-ENTRY CONVENTION (P8):** PREPEND your DELIVERED entry to the body, newest first; its `##` heading carries the date + the lane-newest claim ("newest, authoritative for the CORE lane; supersedes …"). **The newest entry is authoritative BY POSITION.** Never prepend a frontmatter `last-verified:` chain segment — the masthead's per-closeout fields are `status` + `update-cadence` only; any chain still there is the hub's to retire, not yours to extend.

`coder/CLAUDE.md :50` (session-end step 1, new sub-line): `(as a body entry under the handoff-entry convention above — never as a frontmatter chain segment)`. `coder/SKILL.md :315` (§7a step 2), the short form: *"**The handoff-entry convention (W-SKILLS-4 P8):** PREPEND the DELIVERED entry to the body — newest first, its heading carrying the date + the lane-newest claim; **the newest entry is authoritative by position**. Never prepend a frontmatter `last-verified:` chain segment — the masthead's per-closeout fields are `status` + `update-cadence` only (the full form: `CLAUDE.md` §WUCP Phase 1 step 2)."* — Placement basis: the coder tree never WROTE the chain habit down (grep `last-verified|prepend|chain` over the tree: only the files' own mastheads); the coder imitated the house form. Both launch carriers now say the opposite once each. The coder preflight is unaffected — no check reads the chain (Check 1 reads the newest entry; the PM preflight `:81` likewise).

**(d) The lesson-size convention — `coder/CLAUDE.md :119`** (the Pattern Discovery Protocol, the ONLY place the coder tree names the lessons format; `SKILL.md :316` and `deviation-and-quality.md :293` only say "append"):

> 1. **Immediately append** to `../context/lessons/coder-lessons.md` using the format defined in that file (date, category, source, discovery, impact — `Detail` is a pointer, below). **THE LESSON-SIZE CONVENTION (W-HIVE-1 P6, ratified v56 beat 2; W-SKILLS-4 §1(d)):** each lesson **≤ 1,200 B**, **`Discovery` + `Impact` only**; **`Detail` = a one-line pointer to the return that minted it** (`context/audits/<return>.md §N`). **Rotation is the HUB's act, by COUNT never by calendar:** above **24,000 B** the hub moves the oldest lessons verbatim to `../context/lessons/archive/` until the file is ≤ 16,000 B. You append under the cap; you never rotate, and you never rewrite an existing lesson to fit.

`coder/SKILL.md :316` gains the pointer form (`≤ 1,200 B, Discovery + Impact, Detail by pointer — CLAUDE.md §Pattern Discovery Protocol`). No existing lesson was rewritten. The **≤ 16,000 B floor** is the ratified P6 text (intake §1: "rotates by lesson COUNT to ≤16 KB when >24 KB"), which the brief's (d) abbreviates — included as the rule of record, disclosed. Observed in passing: the hub's 2026-08-26 rotation note in `coder-lessons.md` already cites "the W-SKILLS-4 §1(d) convention" — the file (15,105 B, five lessons) is under the floor; the convention lands behind a rotation already run against it.

**(e) The three R-9 candidates, ≤ 3 lines each, pointer to the R-9 return** — `java-patterns.md` NEW **§15** ("Framework/JDK behaviors that pass green and fail in production — pin them from the bytecode"): (i) *HEAD-for-GET is answered by the framework — dishonestly for a conditional-status route* (Javalin 6 `DefaultTasks` fallback → bare 200, handler never run → `app.head(path, sameHandler)` + an e2e pin through real Jetty; "three answers, only the bytecode says which"; Detail → the R-9 return §0 P3 + §5 item 1); (ii) *a request-derived address is never handed to the resolver unless it is syntactically a literal* (JDK 21 `getAllByName`'s branch conditions → parse the IPv4 arm locally, charset-guard IPv6 + the first-char precondition, strip `[…]`/`%zone`, reject empty, pin the non-literal set false-without-throwing; Detail → the R-9 return §2). `testing-standards.md` NEW **§11** ("A refusal guard on a mutator re-fixtures every single-token test"): walk callers by `git grep -n "\.method("` across ALL test classes/modules — the instruction's survey is a floor, not the census; re-fixture with a second qualifying token AND assert the non-refused outcome (`revoke(...) == REVOKED`) so no future guard change can make the fixture vacuous; +1-and-disclose, never a silent guard widening; Detail → the R-9 return §0 P6 + §4/§5. Both files: masthead stamp at `:8`, the prior `2026-06-07 against commit 8028337` segment retained; body otherwise byte-unchanged (hunks in §1).

## §4 Pushback and disclosures (evidence over instruction)

**4.1 The (a) byte target is infeasible under the brief's own allowance — FLAGGED, not deviated.** 53,020 − 2,950 − 1,066 = **49,004 B with both lines deleted outright**; the brief allows a ≤ 400 B `last-verified:` plus a one-line `pass-history:` pointer, so the floor is ≈ 49,400. Landed **49,676 = 49,004 + 379 + 293**. The 293 B pointer carries the one sentence that protects the census ("read it before any census so those names stay resolvable"); cutting it to a bare path saves ~150 B and orphans the sibling-carrier index at the next census. Recommend ratifying 49,676 as the (a) result and restating the target as "masthead provenance ≤ 700 B", which is met (672).

**4.2 No provenance line carried a rule — the STOP did not fire, with one adjacency disclosed.** `pass-history:` carries the SIBLING-CARRIER INDEX (four "rule X lives at carrier Y" entries) and `last-verified:` carries the H7/H8 and SK-INV-02 carrier pointers. These are census aids — the rules live at the named carriers, all of which exist unchanged — not rules; both move whole, and the replacement `pass-history:` line names the index so it stays reachable. Adjudicate at the carrier.

**4.3 The (d) floor.** The ≤ 16,000 B rotation floor is in the landed rule from the ratification, not from the brief's (d) sentence — §3(d). Strike it if the hub prefers the brief's shorter form; the census is unaffected either way.

**4.4 The operator-day.** The session banner said 2026-08-27; `TZ=America/Chicago date` said **Wed 2026-08-26 20:03 CDT**. Every stamp and return pointer in the six files was written to **2026-08-26** and this file is so named (14 occurrences re-derived at the instrument before filing). If the hub's ratification beat lands on the 27th CT, the filename still stands — it is dated by filing, not by audit.

**4.5 Fences held, measured.** `diff -rq` baseline-vs-worktree over both trees = exactly the six files (five differing + one new); the state-pointer scan over every ADDED line (SHA / milestone / watermark / `projectionVersion` / next-slot tokens) = zero hits beyond the retained prior segments' `against commit 8028337`; the FE tree 0-byte; `.claude/skills/**` untouched (Check 9 is Nick's, after the commit); LF-only, trailing newlines preserved, CR = 0 on all six.

**4.6 Bytes per launch, honestly.** The coder's always-loaded carriers GREW (+2,856 B) — three conventions were ordered stated and were, once each at their carrier. The net coder saving (−4,069 B) is real only because the W31 read leaves Tier 1; the structural saving is P8's stopped chain growth (+2,492 B in the last closeout alone).

## Harvest (≤ 5)

1. **The PM tree still runs on retired weekly plans — 22 references across 5 files** (`CLAUDE.md` ×5 incl. session-start step 2, WUCP step 7, the Tier-1 line, the ticked-artifact six; `SKILL.md` ×4 at `:88/:139/:171/:212`; `references/freshness-preflight.md` ×10 incl. **Check 2 "Current week's plan exists" → STALE when absent — a standing false-STALE at every hub launch that runs it literally**; `review-and-quality.md` ×2; `repo-state-protocol.md` ×1). WUCP Step 7 and `canonical-paths.md:24` already say RETIRED (Nick 2026-08-09). Not chartered here (body edits outside the four lists); the PM-side P7 fold is a W-SKILLS-5 charge with this file:line list as its census.
2. **The coder masthead carries the same provenance class as (a): 2,305 B (6.5 %) per coder launch** (`coder/SKILL.md :13` 1,482 + `:14` 823) — one-file-plus-carrier, same treatment, same `cmp` bar; the FE's separable 2,837 B (6.8 %) likewise. Both fit one pass with the (a) precedent.
3. **The FE's launch cost is 85 % body, not masthead** — the FE-half charter should be a §4a–§4e body pass (the SK-INV-01 re-grounding's next step: laws stay, exhibits and pointers thin), measured at the section, not the masthead.
4. **The `≤ 6 files` fence bit exactly at the edge**: the R-9 folds took two carriers (java-patterns + testing-standards, by pattern class); an FE treatment would have been files 7–8. A future launch-cost brief should fence by TREE, not by count, when it also charters a measure-only item that may qualify for treatment.
5. **Re-derive the CT day at the instrument before naming the return** — the UTC banner was a day ahead at 20:03 CDT; 13 stamps would have carried the wrong operator-day. The W-SKILLS-3 harvest named this hazard; it fired here.

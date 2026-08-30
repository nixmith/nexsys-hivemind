<!--
file: context/audits/2026-08-29_W-SKILLS-5_return.md
purpose: Lane return for W-SKILLS-5 — the PM P7 fold + the masthead provenance moves (v57 beat 7 dispatch), executed as a dedicated fresh Cowork lane (remote; device bridge) per `context/instructions/2026-08-28_skills-lane_W-SKILLS-5_pm-p7-fold_and_masthead-provenance_brief.md`. Filename dated by the operator-day FILED in America/Chicago — Sat 2026-08-29, 19:36 CDT, re-derived at the instrument (`TZ=America/Chicago date`); the session banner read Sun 2026-08-30 UTC (arc-discipline 4; the W-SKILLS-4 harvest-5 hazard fired again and was caught again).
audience: the hub (its W-SKILLS-5 ratification beat, Monday) + Nick (the two commits + the account sync = Check 9)
state-type: audit / lane return
status: FILED 2026-08-29. The lane COMMITTED NOTHING — worktree edits only; the hub audits, Nick commits (hivemind 7 M + 1 A; skills 2 M + 1 A), then syncs.
laws-held: fenced BY TREE (exactly `nexsys-hivemind/{project-manager,coder}/**` = 7 M + 1 A and `nexsys-skills/orchestrators/nexsys-frontend/**` = 2 M + 1 A; nothing under `context/**` but this return; no spine, no mirror) · every rule name in = out, retirements ONLY by name with basis (§0) · every moved byte `cmp`-identical at its carrier (§2) · no project state entered any skill file (§4.9) · NO attribution trailers (nothing staged) · evidence over instruction: every brief/bytes mismatch FLAGGED in §4, none silently deviated.
baseline: hivemind `e1ed5f9` (the dispatch-day HEAD, v58 beat 3) · skills `5105abc` — both porcelains EMPTY at launch (`git --no-optional-locks status --porcelain`).
-->

# W-SKILLS-5 — the PM P7 fold + the masthead provenance moves (lane return)

## §0 The census verdict, per tree (the RULE CENSUS in/out table is the spine)

| File | Census object | in → out | Retired (by name, basis) | Deltas |
|---|---|---|---|---|
| `project-manager/SKILL.md` | arc-disciplines 37 · durable D1–D18 · strategy-layer 4 · state-pointer 1 | **60 → 60**, lost = ∅, new = ∅, order identical; all four list LINES byte-identical (regex, baseline vs worktree) | none | `:13` the ≤ 400 B verdict (380 B); `:88 :139 :171 :212` folded; every `##` heading identical |
| `project-manager/CLAUDE.md` | named rule P3 (ticked-artifact closeout) · 6 session-start steps · 13 WUCP steps (0–12) · 4 context tiers | **P3 1 → 1**; steps 6 → 6 and 13 → 13 (step 7 RETIRED IN PLACE, number kept) | none (step 7 = a step retirement already ruled at WUCP §Phase 2 Step 7 — Nick 2026-08-09) | `:8` stamp; `:23 :40 :49 :65 :86` |
| `project-manager/references/freshness-preflight.md` | 11 checks · the Check-9 three-location rules (3) | **checks 11 → 11**; Check-9 rule names 3 → 3 | **ONE, by name: Check 2 "Current week's plan exists" — its SUBJECT is RETIRED.** Basis: Nick 2026-08-09 (`canonical-paths.md:24`; WUCP §Phase 2 Step 7) · W-SKILLS-4 harvest 1 · v57 beat 2 §A.7(5) · the brief §1(a). The slot survives as **Check 2 — The plan of record resolves**. | `:8` stamp; `:23`; Check 2 `:41–:47`; `:61 :85 :103` (reference text only); `:141 :147` (the (d) restatement); `:184 :193 :219` |
| `project-manager/references/review-and-quality.md` | named rules P3 · P4 · P5-audit (+ H7, H8 lines) | **3 → 3** identical; H7/H8 lines untouched; §6 steps 13 → 13 (step 7 RETIRED IN PLACE) | none | `:8` stamp; `:230 :239` |
| `project-manager/references/repo-state-protocol.md` | (no named rules) | headings identical | none | `:8` stamp; `:143` |
| `project-manager/references/pass-history.md` | carries no rule | — | — | `:8` stamp; §1 gains the demoted W-SKILLS-4 verdict line, VERBATIM (first exercise of its ratified update-cadence) |
| `coder/SKILL.md` | arc-conventions 21 · durable-build 8 · strategy-layer 3 · state-pointer 1 | **33 → 33**, lost = ∅, new = ∅; the four list LINES byte-identical; **`:15–EOF` byte-identical to baseline (`cmp`)** | none | exactly ONE hunk `13,14c13,14` |
| `coder/references/pass-history.md` (NEW) | carries no rule | — | — | 4,798 B; not a launch read |
| `nexsys-frontend/SKILL.md` | the §3-onward law surface (W-SKILLS-3: 39-in / 40-out) | **40 → 40 BY CONSTRUCTION — `:14–EOF` byte-identical to baseline (`cmp`)**; the v1.9 segment's by-name retirement records (2 RETIRED WITH ARGUMENT + 1 MERGED, with their surviving-half carriers) moved WHOLE | none | exactly ONE hunk `12,13c12,13`; `:1–:11` byte-identical |
| `nexsys-frontend/references/freshness-preflight.md` | 8 checks | **checks 8 → 8**; **+1 law folded in by ratification: THE LOCK-FREE PORCELAIN LAW** (v57 beat 2 §B.4; the Core-lane form: coder preflight §Shared protocol, v40 beat 1) | none | `:7` stamp; `+:14` the law (one line) |
| `nexsys-frontend/references/pass-history.md` (NEW) | carries no law | — | — | 5,174 B; not a launch read |

**The Check-2 row, on its own.** RETIRED: *"Current week's plan exists"* (a `planning/weeks/` file for the current ISO week; STALE if none) — since 2026-08-09 no such file can exist (the series ends at `2026-W31`; today is 2026-W35), so every literal launch aggregated STALE and forward work was formally forbidden until hand-adjudicated ("PASS-by-cadence" in the v55 launch record). REPLACED by: *"The plan of record resolves"* (§3 verbatim). **Simulated launch against the live spine, read-only:** both mastheads name `v58 hub, beat 3` (age 1 day); the handoff names one `*plan-of-record.md` and it RESOLVES → **PASS**; the old check on the same launch → **STALE** (no `2026-W35` file). No other check's verdict logic changed (§4.6).

Stop-gates: the PM masthead + `pass-history.md` (the sibling-carrier index) read BEFORE the census; the W-SKILLS-4 return + the beat-2 audit §A.6–A.7/§B.4 read whole; the (d) basis re-verified at pm-handoff v57 beat 3 ("Nick keeps NO host mirror — the account-synced trees ARE the mirror of record"); `canonical-paths.md:24` + WUCP Step 7 re-read for the retirement basis; all eleven touched files read WHOLE before any edit; every edit an assert-exactly-once replacement at the bytes.

## §1 Per-file before / after, and the per-launch cost

**Instrument, disclosed:** bytes = `wc -c` at the edited objects on Nick's disk; tokens = the Claude BPE tokenizer in `anthropic==0.21.3` (`count_tokens`, LF-normalized) — the SAME instrument as v44 / W-SKILLS-2 / -3 / -4, and the chain stays closed-loop: **this pass's before-values reproduce W-SKILLS-4's after-values to the token** (PM 12,717 · coder 9,319 · FE 10,988 · PM pass-history 1,763) — the fifth consecutive pass on one continuous token record.

| File | bytes before → after | Δ B | tokens before → after | Δ tok | hunks (git-normalized) |
|---|---|---:|---|---:|---|
| `project-manager/CLAUDE.md` | 9,958 → 11,022 | +1,064 | 2,644 → 2,974 | +330 | `8 23 40 49 65 86` |
| `project-manager/SKILL.md` | 49,676 → 50,142 | +466 | 12,717 → 12,865 | +148 | `13 88 139 171 212` |
| `project-manager/references/freshness-preflight.md` | 16,153 → 18,735 | +2,582 | 4,195 → 4,951 | +756 | `8 23 41 43 45,3 61 85 103 141 147 184 193 219` |
| `project-manager/references/review-and-quality.md` | 20,676 → 21,230 | +554 | 4,927 → 5,112 | +185 | `8 230 239` |
| `project-manager/references/repo-state-protocol.md` (CRLF worktree, §4.9) | 13,735 → 14,057 (LF-normalized 13,500 → 13,822) | +322 | 3,313 → 3,427 | +114 | `8 143` |
| `project-manager/references/pass-history.md` (not a launch read) | 5,850 → 6,683 | +833 | 1,763 → 2,062 | +299 | `8` · `16a17,20` |
| `coder/SKILL.md` | 36,674 → **34,550** | **−2,124** | 9,319 → **8,648** | **−671** | `13,14c13,14` |
| `coder/references/pass-history.md` (NEW; not a launch read) | 0 → 4,798 | +4,798 | 0 → 1,480 | +1,480 | new file |
| `nexsys-frontend/SKILL.md` | 41,636 → **39,495** | **−2,141** | 10,988 → **10,349** | **−639** | `12,13c12,13` |
| `nexsys-frontend/references/freshness-preflight.md` | 9,683 → 10,550 | +867 | 2,598 → 2,885 | +287 | `7` · `13a14,15` |
| `nexsys-frontend/references/pass-history.md` (NEW; not a launch read) | 0 → 5,174 | +5,174 | 0 → 1,579 | +1,579 | new file |

**1.1 Hub launch — the three session-start reads GREW +4,112 B / +1,234 tok; the saving is structural.** The fold replaces bare weekly-plan references with pointer-bearing sentences (the coder precedent's form). What leaves: the literal step-2 read of the newest weekly file (**6,925 B / 2,060 tok**, W-SKILLS-4's measurement) → net **−2,813 B / ≈ −826 tok per literal launch** — and the false-STALE that cost every launch a hand adjudication. PM masthead provenance 672 → **673 B** (380 + 293; the ratified ≤ 700 B holds).

**1.2 Coder launch — −2,124 B / −671 tok, −5.8 % of the file.** Masthead provenance 2,813 → **689 B** (396 + 293; ≤ 700). The carrier is a Tier-2 read at a skills beat only.

**1.3 FE launch — SKILL.md −2,141 B / −639 tok (−5.1 %); the preflight +867 B / +287 tok for the porcelain law → net −1,274 B / −352 tok.** `status:` 2,554 → 897 B (the v1.12 stamp 384 + ` Prior: ` 8 + the RETAINED v1.11 segment 444 + a 61 B pointer — §4.7); `version-history:` 747 → 263 B. FE masthead provenance **1,160 B** — above ≤ 700 by exactly the retained v1.11 segment the brief's "2,837 B only" fence kept. The body (35,420 B, 85 %) is byte-unchanged.

## §2 The moved provenance — carriers, quoted heads, `cmp` offsets

Each range was extracted at its baseline offset, written into the carrier, and `cmp`'d back (rc = 0 ×5). Re-derive: `git show HEAD:<file> | tail -c +<baseline offset + 1> | head -c <len>` vs `tail -c +<carrier offset + 1> <carrier> | head -c <len>`.

| Moved range | baseline offset · length | carrier · offset | `cmp` |
|---|---|---|---|
| PM `SKILL.md :13` (the W-SKILLS-4 verdict line, demoted under the ratified cadence) | 983 · 379 B | `project-manager/references/pass-history.md` §1 · **2,046** | IDENTICAL |
| coder `SKILL.md :13` (`last-verified:` — W-SKILLS-4 → -2 → v44 narratives, incl. the P8/§1(d) carrier pointers) | 1,058 · 1,990 B | `coder/references/pass-history.md` §1 · **1,855** | IDENTICAL |
| coder `SKILL.md :14` (`pass-history:` — the 2026-07 ledger + the five-entry SIBLING-CARRIER INDEX) | 3,048 · 823 B | `coder/references/pass-history.md` §2 · **3,975** | IDENTICAL |
| FE `SKILL.md :12` bytes 465–2,554 (the `status:` `Prior:` tail, v1.10 + v1.9 — the leading space is byte 1 of the range) | 1,939 · 2,090 B | `nexsys-frontend/references/pass-history.md` §1 · **2,229** | IDENTICAL |
| FE `SKILL.md :13` (`version-history:` whole) | 4,029 · 747 B | `nexsys-frontend/references/pass-history.md` §2 · **4,427** | IDENTICAL |

**Carrier `coder/references/pass-history.md` (NEW, 4,798 B; the PM carrier's form line-for-line).** Quoted head:

> `purpose: PROVENANCE carrier for coder/SKILL.md — the skills-pass census narratives and the pass ledger that used to ride the SKILL.md masthead at every coder launch (W-SKILLS-5, charge (b): 2,813 B of provenance moved here VERBATIM — the PM's W-SKILLS-4 charge-(a) precedent; no rule lives in this file). Also carries the SIBLING-CARRIER INDEX (rules minted by earlier passes that live at other carriers), which a future census must keep resolvable.`
> `update-cadence: per skills pass — SKILL.md last-verified: keeps ONLY the newest pass's ≤ 400 B census verdict + return pointer; the demoted verdict line moves here whole, newest first, under §1.`

One sentence the PM carrier lacks (disclosed): *"Paths inside the moved lines are as written at SKILL.md — relative to coder/"* (the coder's `:14` names coder-relative paths). The two replacement lines in `coder/SKILL.md` (396 B + 293 B, both ≤ 400):

> `last-verified: 2026-08-29 (**W-SKILLS-5** — the masthead provenance move, the W-SKILLS-4 (a) precedent. **RULE CENSUS 33-in / 33-out, every name surviving, zero retirements; the four lists + the body BYTE-UNCHANGED** (arc-conventions 21 · durable-build 8 · strategy 3 · state-pointer 1). Return: ../context/audits/2026-08-29_W-SKILLS-5_return.md. Prior: references/pass-history.md §1.)`
> `pass-history (PROVENANCE, not law — no rule lives on this line): moved WHOLE to references/pass-history.md §2 (the 2026-07 pass ledger + THE SIBLING-CARRIER INDEX of rules minted by earlier passes that live at other carriers — read it before any census so those names stay resolvable).`

**Carrier `nexsys-frontend/references/pass-history.md` (NEW, 5,174 B; same form).** Quoted head:

> `purpose: PROVENANCE carrier for orchestrators/nexsys-frontend/SKILL.md — the skills-pass census narratives (the status: line's Prior: tail) and the version ledger (the version-history: line) that used to ride the SKILL.md masthead at every frontend-lane launch (W-SKILLS-5, charge (c): 2,837 B of provenance moved here VERBATIM, the PM's W-SKILLS-4 charge-(a) precedent; no law lives in this file). The v1.9 segment's by-name retirement records (2 RETIRED WITH ARGUMENT, 1 MERGED, each with its surviving-half carrier) are census RECORDS and live here whole — a future census must keep them resolvable.`
> `update-cadence: per skills pass — SKILL.md status: keeps ONLY the newest pass's ≤ 400 B version stamp + census verdict + return pointer (and, until the FE BODY pass demotes it, the v1.11 law-surface verdict as its Prior:); each demoted segment moves here whole, newest first, under §1.`

The FE `status:` line now = the v1.12 stamp (384 B) + ` Prior: **v1.11 …**` (the 464 B segment minus its `status: CURRENT — ` prefix) + ` Earlier (v1.10 → v1.0): references/pass-history.md §1.`; the `version-history:` line = the pointer + the retained design-v1 conformance clause (§4.8).

## §3 The (a) Check-2 replacement and the (d) diffs, verbatim (`<` before / `>` after)

**(a) `project-manager/references/freshness-preflight.md` Check 2 — the SUBJECT replacement:**

```
:41 < ### Check 2 — Current week's plan exists
    > ### Check 2 — The plan of record resolves (SUBJECT REPLACED 2026-08-29 — the check "Current week's plan exists" is RETIRED by name: Nick 2026-08-09 · W-SKILLS-4 harvest 1 · the W-SKILLS-5 brief; it was a standing false-STALE at every literal launch after the weekly plans retired)
:43 < Check `../../context/planning/weeks/` for a file matching the current ISO week (e.g., `2026-W15_apr06-apr12.md`).
    > The plan of record = the newest `last-verified:` beat segment of `../../context/handoff/pm-handoff.md` + the newest `last-verified:` beat segment of `../../context/status/PROJECT_SNAPSHOT.md` + the newest `../../context/planning/*plan-of-record.md` BY POINTER when either of those names one. (`../../context/planning/weeks/` is RETIRED — Nick 2026-08-09, `../../context/canonical-paths.md` — historical only: never demand, create, or check for a current-week file.)
:45 < - **PASS** if the file exists AND its Status field is `IN_PROGRESS` or `COMPLETE`.
    > - **PASS** if the two newest beat segments name the SAME hub/beat AND every `*plan-of-record.md` either of them names resolves to an existing file at the path given.
:46 < - **STALE** if no file exists for the current week, or the file exists but has Status `TEMPLATE` or is missing a Status line.
    > - **STALE** if the snapshot's newest beat is behind the handoff's, or the newest pm-handoff beat is older than 14 days, or a named `*plan-of-record.md` is absent at the path given.
:47 < - **CONFLICTED** if multiple files exist for the same week, or the file's date range doesn't match the actual ISO week.
    > - **CONFLICTED** if the two spine files name DIFFERENT horizons (different `*plan-of-record.md` files, or one names a plan the other records as superseded), or the snapshot's newest beat is AHEAD of the handoff's — a contradictory plan of record.
```

The 14-day threshold is Check 1's; "behind / ahead" is Check 3's tolerance form; the §6 row keeps its column (verdict at col 40). The other PM rows follow the coder precedent's wording (W-SKILLS-4 §3(b)): `CLAUDE.md :23` → *"**The plan of record = the snapshot (step 1) + the newest `../context/handoff/pm-handoff.md` beat (step 4)** … If either points at a `../context/planning/*plan-of-record.md`, the NEWEST such file is the horizon — reached by that pointer only, never by listing the directory. (`planning/weeks/` is RETIRED — Nick 2026-08-09 …)"*; `CLAUDE.md :40` / `review-and-quality.md :230` → *"7. RETIRED (weekly plans — Nick 2026-08-09; WUCP §Phase 2 Step 7) … the step number is kept so cross-references stay resolvable"* (the WUCP's own Step-7 wording); the P3 "fixed six" keep their count with *"the weekly-plan slot — RETIRED 2026-08-09, ticked N/A per WUCP §Phase 2 Step 7"* (the WUCP checklist's `:300` form). Post-edit scan: zero PM-tree lines match `weeks/|weekly plan|current week's plan` without a retirement notice.

**(d-1) FE `references/freshness-preflight.md` — the porcelain law (ADDED at `:14`; the file had no porcelain line — §4.2):**

```
:14 > **Porcelain is lock-free, with the flag SPELLED (folded 2026-08-29, W-SKILLS-5 (d) — the v57 beat-2 §B.4 ruling):** any tree census this lane runs — at this preflight, in a return, or in any block you author — is `git --no-optional-locks status --porcelain`; a plain `status` from a tooling context strands a zero-byte `index.lock` on the mount that surfaces at Nick's keyboard (the FE-SWAP-GATE exhibit, 2026-08-26). Set `GIT_OPTIONAL_LOCKS=0` for the session as belt-and-braces. The Core-lane form of the same law: `nexsys-hivemind/coder/references/freshness-preflight.md` §Shared protocol (adopted v40 beat 1).
```

**(d-2) PM `references/freshness-preflight.md` Check 9 — the mirror of record (TWO lines — §4.3):**

```
:141 < 2. **Nick's local `.claude/skills/` MIRROR** — the read-only tree host-CC lanes actually load. **This is the location Check 9 governs**, and the only one the STALE/CONFLICTED verdicts above describe.
     > 2. **THE ACCOUNT-SYNCED SKILL TREES — THE MIRROR OF RECORD** (restated 2026-08-29, W-SKILLS-5 (d); basis: v57 beat 3 — Nick keeps NO host `.claude/skills/` mirror). These are the copies a remote hub or lane loads, and Nick's "skills synced" means these. **This is the location Check 9 governs**, and the PASS/STALE/CONFLICTED verdicts above are evaluated against it — instrument: a per-file `md5sum` (or `diff`) of each writable SOURCE tree against its synced tree, all three pairs (the v57 beat-2 §A.6 form). The `diff -rq` block above against a host `.claude/skills/` mirror runs only IF such a mirror exists; its absence is neither STALE nor CONFLICTED.
:147 < - **Nick's `diff -rq` above remains the mirror's instrument of record.** A remote session that cannot mount both trees records Check 9 as **STALE (mirror unverified from here)** — conservative, aggregating as STALE per §3 — and names exactly which trees it could read. The mirror's true state is then confirmed by asking Nick, never inferred.
     > - **The per-file SOURCE-vs-synced comparison is the mirror's instrument of record; the host `diff -rq` applies only if a host mirror exists.** A remote session whose loaded skill copies came from the account-synced trees may compare them against SOURCE to characterize the synced trees AS OF ITS LOAD (a lag is STALE, never CONFLICTED, until Nick re-syncs); a session that can read neither tree records Check 9 as **STALE (mirror unverified from here)** — conservative, aggregating as STALE per §3 — and names exactly which trees it could read. The mirror's true state is then confirmed at the synced trees or by asking Nick, never inferred.
```

Arc-discipline (6) stays true under the restatement: the mirror is the synced trees; a session's loaded copies remain a load-time snapshot of them, not the mirror.

## §4 Pushback and disclosures (evidence over instruction)

**4.1 The brief's coder `:13` figure (1,482 B) predates W-SKILLS-4's own 508 B stamp.** At the dispatch baseline `:13` = **1,990 B**, `:14` = 823 B (matches) — **2,813 B moved, not 2,305**, whole, because a partial move would strand the newest verdict outside the cadence. FLAGGED. Likewise the count: the brief's own regex matches 17 PM-tree lines; the wider `week` net (Check 2's four lines, the `:219` output row, the two P3 "fixed six" rows) makes **23** — all 23 folded.

**4.2 The FE preflight had NO porcelain line to respell** (`grep -i porcelain` over the FE tree: only `build-and-ci-discipline.md :68`'s already-spelled `git --no-optional-locks log`). The (d) fold therefore ADDS the lock-free porcelain law as one line, in the coder preflight's form, with the FE-SWAP-GATE exhibit named — a new named rule in the FE tree, entered by ratification (v57 beat 2 §B.4). If the hub prefers it at `build-and-ci-discipline.md §4`, the line moves whole.

**4.3 The Check-9 fold took two lines, not one.** `:141` is the definition; `:147` ("Nick's `diff -rq` above remains the mirror's instrument of record") would have flatly contradicted it. Left as-is, reachable through `:141`'s "only IF such a mirror exists": the `diff -rq` block `:114–:125`, the verdict lines `:130–:134`, and six sibling lines (harvest 1).

**4.4 The (a) STOP did not fire — no weekly-plan reference was load-bearing.** The nearest: `review-and-quality.md :239`'s "the preflight's backlog/weekly checks are load-bearing precisely because a hurried closeout under-updates those two" — the claim TRANSFERS to the re-subjected check (a hurried closeout under-updates the handoff/snapshot currency and the pointer exactly as it under-updated the weekly file), so it was restated to "Check 4 + the re-subjected Check 2", not stopped on. Check 4's second reference became "the pm-handoff beat that closed the milestone" (pre-2026-08-09 milestones keep their historical `weeks/` reference) — the list changes, the three-references PASS logic does not.

**4.5 The PM tree's launch cost GREW (+4,112 B).** A bare-"RETIRED" fold would save ~1.5 KB and lose the plan-of-record pointer at the read locations that need it; recommend ratifying the growth against the removed W31 read (−6,925 B) and the removed false-STALE. **4.6 "No other preflight check changes" — held at the verdict level, disclosed at the text level:** Checks 4/6/8 carried weekly-plan words inside their reference lists / CONFLICTED clauses (harvest 1's own `:61 :85 :103`); the words folded, the PASS/STALE/CONFLICTED logic is byte-unchanged; 11 checks → 11.

**4.7 The FE `status:` retains the v1.11 segment (444 B) as `Prior:` and gains a v1.12 stamp (384 B).** The brief fenced the move to "the separable 2,837 B only", so the v1.11 law-surface verdict (39-in / 40-out — the last count taken by reading) stays; the FE house form bumps the version per pass (v1.9/v1.10/v1.11 were one pass each; nothing outside `SKILL.md` cites it — grep'd). Strike the stamp if the hub prefers a stamp-free move; the census is unaffected. **4.8** The moved `version-history:` line's last clause ("Conforms to nexsys-skills design-v1 …") is a conformance claim, not provenance — it moved verbatim AND stays on the replacement pointer line (90 B).

**4.9 Fences, measured.** Hivemind porcelain = exactly 7 M + 1 A under the two trees; skills = 2 M + 1 A; `context/**` EMPTY before this file; no `.claude/skills/**` exists in the connected folder. State-pointer scan over every ADDED line (7–40-hex · `M<n>.<n>` · watermark · `projectionVersion` · next-slot): hits = `8028337` ×4 (all RETAINED prior segments) + "next Core slot" ×1 (the pre-existing pointer-not-copy phrase on `SKILL.md :171`) — nothing new. L3 (token-paste) scan: only paths and rule names. CR 0 · NUL 0 · trailing LF on ten files; **`repo-state-protocol.md` was CRLF in the worktree BEFORE this pass** (`git ls-files --eol` `i/lf w/crlf`; `.gitattributes` `text=auto eol=lf`) — the edit preserves CRLF (CR 235 → 235), so git's normalized diff is exactly the two lines. Nothing staged.

**4.10 The operator day.** Banner Sun 2026-08-30 UTC; instrument Sat 2026-08-29, 19:14 CDT at launch and 19:36 CDT at filing. Every stamp and date this pass wrote (37 occurrences across the 11 files) and this filename say 2026-08-29.

## Harvest (≤ 5)

1. **The host-mirror assumption survives at six sibling lines + the Check-9 `diff -rq` block**: coder preflight Check 6 (`:83 :90`), FE preflight Check 7 (`:76`) + FE `CLAUDE.md :73`, and the WUCP step-10 form at PM `CLAUDE.md :43` / `review-and-quality.md :233` / `SKILL.md :141`. The shared-protocol law owes the coder's Check 6 the same restatement; a one-pass "mirror-of-record fold" by tree (≤ 8 lines) should also give Check 9 the paste-block its instrument of record (per-file md5, source vs synced) still lacks anywhere.
2. **FE masthead provenance is 1,160 B, not ≤ 700** — the retained v1.11 segment is the difference; the FE BODY pass should demote it under the carrier's cadence in the same beat it thins §4a–§4e (35,420 B, 85 %, untouched here).
3. **Masthead byte figures in a brief go stale by exactly the prior pass's stamp** (coder `:13`: 1,482 vs 1,990) — quote them AT the dispatch baseline or say "re-derive"; this brief said both, which is why the mismatch was caught rather than executed.
4. **The literal-preflight false-STALE class has a second instance**: Check 9's `diff -rq` against a host mirror that does not exist fails or reports "Only in" at every launch — Check 2's shape, hand-adjudicated at every v5x launch. Harvest 1's fold retires it.
5. **Pin the token instrument**: `anthropic==0.21.3`'s `count_tokens` no longer imports under current `httpx`; `httpx<0.28` restores it. The chain reproduced to the token; the next brief should pin both.

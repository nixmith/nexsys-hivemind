<!--
file: context/truth-map.md
purpose: THE ROLE-INDEXED TRUTH-MAP — for every role × task-class: where CURRENT truth lives (repo + path + section) and what outranks what. Built by R-11 (brief: context/instructions/2026-08-17_R11_wayfinding-truth-map_lane_brief.md) against the W-COHERE top-10 gap list (context/audits/2026-08-09_WCOHERE_navigation-audit_return.md §2). THE ONE-HOP BAR governs this file: a fresh session handed ONLY this map must reach the correct, CURRENT artifact in one hop. Volatile state is POINTED AT, never copied in — no HEADs, counts, or dates-of-things live here.
audience: every fresh session, every role — the first navigation read after the dispatch line names a role or a task
state-type: reference (wayfinding)
status: CURRENT — placement PROPOSED at context/truth-map.md by the R-11 lane (the brief's REC); the hub ratifies at intake
owner: the hub — re-verified at every orchestrator-prompt banking (arc close) per the maintenance-loop law; the register row is context/process/edit-procedure-register.md §2 (class 10)
last-verified: 2026-08-18 (R-11 lane — authored at hivemind 45dd100 against the W-COHERE gap list; worktree only, the lane commits nothing; the hub audits and orders the commit)
-->

# The Truth-Map (role-indexed)

## §0 — The outranking rule (stated once; every row below inherits it)

**Across repos (the truth hierarchy — `context/process/truth-hierarchy-and-pointer-not-copy-discipline.md` §1):** code (`homesynapse-core` — the territory) > Locked design docs + registers (`homesynapse-core-docs` — the contracts) > operational memory (`nexsys-hivemind` — drifts continuously).

**Inside the hivemind (which operational layer wins):** THE SPINE (`context/handoff/pm-handoff.md` newest beats + `context/status/PROJECT_SNAPSHOT.md` frontmatter chain) > the newest non-archived orchestrator prompt (`context/handoff/*_PM-mission-control_v*_orchestrator_session_prompt.md`) > the skills mastheads > standing wayfinding/reference files. A banked prompt says so itself ("the spine outranks this section"); a skill masthead carries the state-pointer law (skills hold no project state). Where any two layers disagree, the higher layer wins and the disagreement is a finding to flag.

**Volatile state (HEADs, porcelain, counts, watermarks):** re-derive at the instrument (`git --no-optional-locks status --porcelain`, `git log`, the register's §17 table) — never trust a copied value, including in this file.

## §1 — The launch route (what a fresh session actually reads)

`nexsys-hivemind/START_HERE.md` → the newest **non-archived** `context/handoff/*_PM-mission-control_v*_orchestrator_session_prompt.md` → that prompt's §1 launch-read list (it names the spine reads, depths, and on-demand files). The prompt's §1 is the launch route of record; this map does not restate it. Both spine files carry a "**How to read this file**" self-description at the top of the body (minted v50 beat 6) — trust it for ordering, depth, and archive locations.

## §2 — Role × task-class index

### PM / hub

| Task-class | Where truth lives (one hop) |
|---|---|
| Session launch / state | The newest non-archived orchestrator prompt, §1 → the spine per its own How-to-read lines: `context/status/PROJECT_SNAPSHOT.md` (frontmatter chain, newest segments first) + `context/handoff/pm-handoff.md` (newest beats first; `## Open Risks` at the tail is standing) |
| The program of record (post-gate semester) | `context/assessments/2026-08-14_S10_close_ranked-program.md` (R-1..R-15 as ratified 2026-08-16, pm-handoff v53 beat 4) + the newest prompt's Section-2 program row; the spine outranks on any divergence |
| Brief / dispatch authoring | The practiced form: the newest lane briefs in `context/instructions/` + the PM skill's arc-disciplines (`project-manager/SKILL.md`); returns file to `context/audits/`, dated by FILING day (§3.2 below) |
| Return intake / two-layer audit | The PM skill's review discipline + the newest audited intake beats in `pm-handoff.md`; labels are claims, quotes are evidence |
| Spine-write + commit-order mechanics | `context/process/cowork-environment-model.md` §§10–12 (the best-maintained standing file; §11 ghost-commit/OVERTAKEN-ORDER; §12 addenda) |
| WU closeout | `context/protocols/work-unit-completion-protocol.md` — the phase discipline is LAW; steps rebuilt current 2026-08-18 (R-11) |
| Defending settled rulings | `context/process/decision-rationale-index.md` (catch-up appended 2026-08-18, R-11) → each row's pointer; the pm-handoff beats + `context/handoff/archive/` hold the verbatim records and remain authoritative for wording |
| Planning spine | The beat cadence + `context/planning/phase-3-milestone-backlog.md` head currency note (the S-10 close is the operative post-gate program). **Weekly plans are RETIRED** (Nick's ruling 2026-08-09, recorded at the WUCP banner-lift and v50 beat 6); `planning/weeks/` is historical |
| Named laws (D5, laws 1–16, H1–H11, L1/L3, …) | The LAW INDEX at `context/process/edit-procedure-register.md` §3 — every named law → its one definitional home |

### Coder

| Task-class | Where truth lives (one hop) |
|---|---|
| Implement-from-instruction | The NAMED `context/instructions/*_coding-instruction.md` for the WU + its `context/pre-verifications/` file + `/nexsys-coder` (`coder/SKILL.md`); rank-1 anchors are the touched modules' `MODULE_CONTEXT.md` in core (recency truth per file: `git log -1 -- <path>`) |
| Current task / queue | `context/handoff/coder-handoff.md`, NEWEST entry first. **Supersession note (map-side, v54 beat 1 nit):** the newest DISPATCH entry outranks any prior entry's yield-queue — the B′ entry's queued next-WUs (S-5b STATE-DIALECT P2 · FE-LIVE-V112 (f)/(g)) predate the ratified program; **the R-1/R-2 dispatch supersedes that queue by name** when it lands |
| Test discipline | `coder/references/testing-standards.md` + `context/process/2026-07-18_compounding-testing-doctrine.md` |
| Session-start freshness | `coder/references/freshness-preflight.md` — its spine-facing checks are R-12's re-grounding ground this week; where a check names a retired spine structure, the spine's own How-to-read line outranks the check |

### Frontend

| Task-class | Where truth lives (one hop) |
|---|---|
| Any FE work | `/nexsys-frontend` (`nexsys-skills/orchestrators/nexsys-frontend/SKILL.md`) — its `truth:` block IS the FE truth-map (code rank 1; Locked docs rank 2); re-derive volatile particulars at those sources per its own §4 fences |
| The frozen read-API contract | `context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` (v1.1.x amendment notes ride in-file) |
| Verification bar | H8 THE LIVE-WIRE VERIFICATION RULE — definitional home per the LAW INDEX (register §3); carriers land in the FE + PM skills at R-12 |
| CI gate | `frontend.yml` on the pushed core commit (`context/process/ci-as-gate-of-record.md` is the standing doctrine) |
| ⚠ Known-stale front door | `nexsys-skills/README.md` still self-describes as skeleton/two-skills (W-COHERE row 8) — do NOT navigate from it; its currency touch is skills-tree work (W-SKILLS pass class), not this map's |

### Bench-operator

| Task-class | Where truth lives (one hop) |
|---|---|
| Pi trip / any multi-block evening | The newest `context/handoff/*_operator-packet.md` for the sitting (the §8-form class) + `context/process/bench-troubleshooting-playbook.md` §8 (the packet contract) |
| Evidence read on a failure | `bench-troubleshooting-playbook.md` §§1, 8 — instrument-first, predictions filed first |
| Daily digest glance | **Honest two-hop, recorded as load-bearing:** no single standing file carries the glance protocol yet (W-COHERE row 6); the fullest statement rides the newest orchestrator prompt's wait-state line + the newest bench operator packet. The chartered ONE standing procedure file belongs in the bench corpus, which is outside R-11's write scope — see the register row (class 12) for the owner |
| ⚠ Known-stale | `nexsys-bench/README.md` (pre-nightly-era) and `context/process/infrastructure-map.md` (2026-07-03; omits the nightly stack and `~/hs-bench/`) — do not orient from either; the playbook + the newest packet outrank both |

### Executive / strategy

| Task-class | Where truth lives (one hop) |
|---|---|
| Entry point | `context/strategy/README.md` (rebuilt current 2026-08-18, R-11) — the corpus inventory + read rules |
| The strategic frame | `context/strategy/2026-07-27_homesynapse-technical-overview_north-star.md` + `context/strategy/Substrate_Thesis_v0.md` (the PM skill's strategy-layer block points here; carriers stay these files per the mission-pointer law, R-12 fence 1) |
| Standing watch | `context/strategy/2026-08-06_company-scale-moat-watch_standing-directive.md` |
| Settled ground | `context/process/decision-rationale-index.md` (catch-up appended 2026-08-18) → row pointers into beats/registers |
| Language law (every strategy sentence) | D5 — definitional home per the LAW INDEX (register §3) |
| Brand / counsel state | `context/strategy/brand-program/` + `context/strategy/counsel-package/2026-07-21_engagement-tracker.md` (the tracker is the clock of record) |

### Navigator / operator-session

| Task-class | Where truth lives (one hop) |
|---|---|
| Running a packet | The dispatched packet itself (self-contained by construction) + playbook §8 for the contract; H11: a navigator files ONE return — a desk pre-flight and its execution record are one artifact filed once (definitional home per the LAW INDEX) |
| Filing the return | `context/audits/<filing-date>_<name>_return.md` — filing-day dating (§3.2); the return-on-disk rule: a WU is not DELIVERED until the return exists at the named path |

## §3 — Named standing rows (v53/v54 mints; each is one fact + its home)

1. **Hardlink twins.** Host files can be filesystem-hardlinked; the device bridge refuses link-alias reads; an edit risks writing through to an unknown twin. The enumeration of record (in-tree ends, link counts, and the outside-the-root finding) is the R-11 return `context/audits/2026-08-18_R11_wayfinding_return.md` §4; the operating rule (break-with-byte-identical-copy before editing, flag the twin) folds into `context/process/cowork-environment-model.md` §12 at R-12. No link surgery outside a chartered edit.
2. **The return-filename convention (minted v54 beat 1).** Returns are dated by the operator-day they are FILED (America/Chicago), never by the due date. **Two grandfathered aliases are committed history — do not rename:** `context/audits/2026-08-20_RS1_verdict-honesty-competitive-study_return.md` and `context/audits/2026-08-21_RS2_physics-world-model_charter-evidence_return.md` were both **filed 2026-08-17** (v53 beat 9); their filenames carry due-dates from before the convention was minted.
3. **The retired message channels.** `context/open-questions.md` is a CLOSED channel (ruling recorded at its head, 2026-08-18) and `context/handoff/cross-agent-notes.md` is an archived pointer stub — the beat spine absorbed both: questions, escalations, and cross-agent facts ride pm-handoff beats, lane returns, and dispatch packets. `[FORESIGHT-NOTE]`/`[OPEN-QUESTION]` routing in older procedure files is superseded accordingly.
4. **The skills mirror.** Three source→mirror pairs (PM · coder · FE); the mirror is read-only to sessions; Nick's external sync propagates; a remote session records Check 9 "STALE (mirror unverified from here)" honestly. **The mirror's absolute host-disk location is recorded nowhere on disk** (W-COHERE 1.3-B) — flagged to Nick at the R-11 return; until he supplies it, session-relative topology (preflight Check 9) is the only address.
5. **Weekly plans RETIRED** (Nick, 2026-08-09 — recorded v50 beat 6 and at the WUCP rebuild): the beat cadence is the planning spine; `planning/weeks/` is historical record. No instrument should demand a current-week file.

## §4 — The registries this map points at (function split, so nothing is duplicated)

- **Directory + naming conventions:** `context/canonical-paths.md` (rebuilt current 2026-08-18, R-11) — the path/naming registry; this map carries roles, that file carries conventions.
- **The full context catalog (what every directory holds):** `context/strategic-context-map.md` — CURRENT in its load-bearing sections (§2, §6–§8); its §3 quick-reference carries two known copied-state lines that are named R-12 harvest items — prefer §2 and the sources it points at.
- **Who writes what, how, and who owns each file-class:** `context/process/edit-procedure-register.md` (authored 2026-08-18, R-11) — the OWNER column is the maintenance-loop law made structural.

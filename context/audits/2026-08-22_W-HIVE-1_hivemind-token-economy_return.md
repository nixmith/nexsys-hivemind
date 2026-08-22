<!--
file: context/audits/2026-08-22_W-HIVE-1_hivemind-token-economy_return.md
purpose: W-HIVE-1 return — the hivemind token economy measured at the git objects: the per-session-type byte census at HEAD, the duplication map with both locations at the bytes, nine proposals ranked by bytes-saved-per-session each carrying the rule that prevents recurrence, the laws that do not move, and the AFTER estimate with a MEASURED rotation rule replacing "rotate when it feels heavy".
audience: the hub (intake audit, ratification, execution at one beat) — the v57 prompt banks on the lean spine.
update-cadence: one-shot lane return
state-type: measurement + proposal
status: FILED
last-verified: 2026-08-22 (W-HIVE-1 lane, read-only; every figure measured at HEAD c974b52 via git objects; zero spine writes, zero commits)
-->

# W-HIVE-1 — The hivemind token economy (read-only measurement + proposal return)

## §0 — HEAD measured at, and the verdict

**HEAD = `c974b52` (v56 beat 1, 2026-08-22 13:03:35 -0500) — NEWER than the brief's `ee767de` baseline by one commit.** Every figure below is measured at `c974b52` unless a row states otherwise. HEAD did not move during the census (re-checked at close). Where the brief quotes an `ee767de` figure I state both.

**The verdict in one paragraph.** A hub launch today costs **195,380 B**, a coder launch **179,539 B**, an FE launch **139,612 B**, a research launch **~36,700 B**. The brief's estimate ("a hub launch is plausibly ≥ 120 KB") is right in direction and **63 % low** in magnitude. The nine proposals below take the hub to **125,251 B (−35.9 %)** and the coder to **146,404 B (−18.5 %)**, saving **250–423 KB per week** at 6–10 sessions. But the headline finding is not a number, it is a **misaimed instrument**: the v54 beat-10 rotation cut `pm-handoff.md` by **85.9 %** (301,693 → 42,645 B) and cut the hub's actual launch read by only **64.9 %** (116,078 → 40,710 B) — and **100.2 % of that reduction came from the frontmatter chain line alone** (77,714 → 2,158 B; the beat blocks moved −106 B and `## Open Risks` moved **+294 B**). The 259 KB of block tail the rotation archived was never read at launch. Rotation is archive hygiene; it is not the token-economy lever, and the seeded "rotate above ~60 KB" rule is unworkable at the measured growth rate (the hub read re-crosses 60 KB **five beats** after a rotation, i.e. daily). The lever is a set of **region caps checked every beat** (§5). Two further findings the hub did not seed carry more bytes than most of what it did: **`## Open Risks` is 23,041 B of which 20,754 B (90.1 %) is a ledger of ten RESOLVED/CLOSED risks**, newest resolved 2026-07-02, oldest 2026-05-31 — read at every hub launch; and **the launch `ls` sweep costs 16,215 B of tool output** for 375 paths.

---

## §1 — The byte census, per session type, at HEAD `c974b52`

Every row is re-measurable by the command beside it. Whole files: `git --no-optional-locks cat-file -s HEAD:<path>` (abbreviated **`CFS`** below). Regions: `git --no-optional-locks show HEAD:<path> | sed -n 'A,Bp' | wc -c` (abbreviated **`SED A,B`**; A/B stated). All paths relative to `nexsys-hivemind/` unless marked. Byte counts include each region's trailing newline; region sums reconcile to the whole-file `CFS` figure exactly (verified: pm-handoff regions sum to 123,645 = `CFS`).

### 1.1 HUB — derived from the v56 prompt §1 (items 1–5) + the skill it auto-loads

| # | File / region | Bytes | Command |
|---|---|---:|---|
| auto | `project-manager/SKILL.md` (auto-loaded; §84 mandates the preflight) | **53,020** | `CFS project-manager/SKILL.md` |
| auto | `project-manager/references/freshness-preflight.md` (SKILL.md:84, :102, :205 — "every session start, mandatory") | **16,153** | `CFS project-manager/references/freshness-preflight.md` |
| 1 | `context/handoff/2026-08-22_PM-mission-control_v56_orchestrator_session_prompt.md`, whole | **24,852** | `CFS` |
| 2 | `context/status/PROJECT_SNAPSHOT.md`, whole | **9,242** | `CFS` |
| 3a | `context/handoff/pm-handoff.md` line 8 — the `last-verified:` chain (ONE line; 9 segments) | **11,689** | `SED 8,8` |
| 3b | `pm-handoff.md` newest THREE beat blocks (v56 b1 · v55 b6 · v55 b5) | **32,599** | `SED 15,84` |
| 3c | `pm-handoff.md` `## Open Risks` | **23,041** | `SED 223,296` |
| 4 | `context/process/cowork-environment-model.md` §§11–12 | **8,569** | `SED 74,102` |
| 5 | the repo-map sweep — tool output, not a file | **16,215** | `ls nexsys-hivemind/context/* \| wc -c` (375 paths) |
| | **HUB LAUNCH TOTAL** | **195,380** | |
| | *of which spine-side (excl. the two skill files)* | *126,207* | |
| | *conditional: `project-manager/CLAUDE.md` if the host loads it* | *+9,958* | `CFS` |

`pm-handoff.md` whole = **123,645 B**; the hub reads **67,329 B of it (54.5 %)**. Region reconciliation: 11,918 (fm 1–9) + 410 (10–14) + 32,599 (15–84) + 54,381 (85–222, the older blocks) + 23,041 (223–296) + 1,296 (297–304) = **123,645** ✓.

### 1.2 CODER — from `coder/CLAUDE.md` §Context Loading Tiers (:54–:66) + `coder/references/freshness-preflight.md` :13

| # | File / region | Bytes | Command |
|---|---|---:|---|
| skill | `coder/SKILL.md` | **35,667** | `CFS` |
| skill | `coder/CLAUDE.md` | **10,426** | `CFS` |
| skill | `coder/references/freshness-preflight.md` | **11,037** | `CFS` |
| T1 | `context/status/PROJECT_SNAPSHOT.md` | **9,242** | `CFS` |
| T1 | "the current week's plan" → newest present is `context/planning/weeks/2026-W31_jul27-aug02.md` — **three weeks stale on 2026-08-22 (W34)** | **6,925** | `CFS` |
| T1 | `context/handoff/cross-agent-notes.md` | **1,024** | `CFS` |
| T1 | `context/handoff/coder-handoff.md`, whole (CLAUDE.md :25 says read it; newest-entry-only variant = 10,924) | **23,120** | `CFS` |
| T2 | `context/instructions/2026-08-22_R9_E3-HEALTH_unauthenticated-loopback-health_coding-instruction.md` | **37,394** | `CFS` |
| T2 | `context/pre-verifications/WU-R9.md` | **12,551** | `CFS` |
| T2 | `context/lessons/coder-lessons.md` | **32,153** | `CFS` |
| | **CODER LAUNCH TOTAL** | **179,539** | |
| | *conditional T2: `coder/references/homesynapse-mental-model.md` on a new subsystem* | *+24,403* | `CFS` |

### 1.3 FE — from `orchestrators/nexsys-frontend/CLAUDE.md` :20–:25 + :35 (repo `nexsys-skills` @ `5105abc`)

| # | File / region | Bytes | Command |
|---|---|---:|---|
| skill | `nexsys-skills/orchestrators/nexsys-frontend/SKILL.md` | **41,636** | `CFS` (in `nexsys-skills`) |
| skill | `…/nexsys-frontend/CLAUDE.md` | **7,680** | `CFS` |
| skill | `…/nexsys-frontend/references/freshness-preflight.md` | **9,683** | `CFS` |
| T1 | `context/status/PROJECT_SNAPSHOT.md` | **9,242** | `CFS` |
| T1 | `context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` (the FROZEN v1.1 contract) | **20,866** | `CFS` |
| T1 | `context/planning/2026-06-27_causal-read-API_scope-freeze-and-milestone-breakdown.md` | **7,945** | `CFS` |
| T1 | `homesynapse-core/web-ui/dashboard/FRONTEND_DOCTRINE.md` (core @ `89a912e`) | **6,267** | `CFS` (in `homesynapse-core`) |
| T1 | `homesynapse-core/web-ui/dashboard/MODULE_CONTEXT.md` | **23,724** | `CFS` |
| T1 | `context/handoff/cross-agent-notes.md` | **1,024** | `CFS` |
| brief | `context/instructions/2026-08-21_FE-lane_never-triggered-fixture_and_F-S3_brief.md` | **11,545** | `CFS` |
| | **FE LAUNCH TOTAL** | **139,612** | |

### 1.4 RESEARCH — the newest research brief (RS-4) + env-model §12 + the brief's own §0

| # | File / region | Bytes | Command |
|---|---|---:|---|
| 1 | `context/instructions/2026-08-21_research-lane_RS4-cra-readiness-memo_brief.md`, whole | **14,301** | `CFS` |
| 2 | `context/process/cowork-environment-model.md` §12 | **5,396** | `SED 82,102` |
| §0.2 | `context/research/2026-08-15_LE_physics-aware-deep-research_return.md` §3/§3.1 rows | **5,740** | `SED 140,160` |
| §0.2 | `context/audits/2026-08-15_LE-LF_late-returns_two-layer-audit_v52-beat-5.md` (row I-5 must be located in-file) | **11,263** | `CFS` |
| | **RESEARCH LAUNCH TOTAL (hivemind-side)** | **36,700** | |

§0.3 additionally names six `homesynapse-core` MODULE_CONTEXT/doc files — out of this lane's scope fence, uncounted. **This lane's own launch** (W-HIVE-1 brief 11,780 + env-model §12 5,396 + v56 prompt §1 3,954) = **21,130 B**. *Finding: research lanes cost 4–5× less than hub/coder lanes because a brief is self-contained. The expensive lanes are the ones that read shared mutable state.*

### 1.5 The weekly figure

| Mix | Composition | Bytes/week |
|---|---|---:|
| Conservative (6 sessions) | 3 hub · 1 coder · 1 FE · 1 research | **941,991 B (≈ 920 KB)** |
| Heavy (10 sessions) | 5 hub · 2 coder · 1 FE · 2 research | **1,548,990 B (≈ 1.51 MB)** |

---

## §2 — The duplication map (both locations, at the bytes)

Method for the "recurs" column: a **fact** = a commit SHA, a `LABEL-N` identifier, a `§`-reference, a filename with extension, or a numeric literal ≥ 2 digits, extracted by one regex from both spans and set-intersected. Direction is stated per row because it decides the proposal.

| # | Fact set | Location A (path + lines + bytes) | Location B (path + lines + bytes) | Measured recurrence |
|---|---|---|---|---|
| D1 | The **v56 beat-1** state | `pm-handoff.md:8` chain segment 1 — **344 B** | `pm-handoff.md:15–40` beat block — **11,494 B** | **100 %** of the segment's 15 facts are in the block; 0 segment-only. The segment carries 13 % of the block's 114 facts. |
| D2 | The **v55 beat-6** state | `pm-handoff.md:8` segment 2 — **675 B** | `pm-handoff.md:41–62` — **11,291 B** | **95 %** (18/19); segment-only = `wu-r9`. Segment carries 22 % of the block's 83 facts. |
| D3 | The **v55 beat-5** state | `pm-handoff.md:8` segment 3 — **2,153 B** | `pm-handoff.md:63–84` — **9,814 B** | **85 %** (22/26); segment-only = `00`, `04`, `18 PASS`, `beat 4`. Segment carries 27 % of the block's 81 facts. |
| D4 | **The same eight beats, two chains** | `pm-handoff.md:8` — **11,689 B**, 9 segments | `PROJECT_SNAPSHOT.md:8` — **6,744 B**, 9 segments, same 8 beats + the same rotation pointer | **88 %** of the snapshot chain's 123 facts also appear in the pm-handoff chain (per-beat: 78/89/93/100/100/92/94/56/100 %). |
| D5 | **The coder's R-7 closeout** | `coder-handoff.md:8` chain segment 1 — **865 B** | `coder-handoff.md:15–24` entry — **6,622 B** | **100 %** (10/10); zero segment-only facts. |
| D6 | **The coder's R-6/R-8 closeout** | `coder-handoff.md:8` segment 2 — **586 B** | `coder-handoff.md:25–35` — **6,721 B** | **93 %** (13/14); segment-only = `9f99368`. |
| D7 | **The coder's R-1/R-2 closeout** | `coder-handoff.md:8` segment 3 — **2,689 B** | `coder-handoff.md:36–47` — **5,217 B** | **88 %** (22/25); segment-only = `ca0f41d`, `d26777c`, `208`, `28`. |
| D8 | **Ten resolved risks** *(not seeded — found)* | `pm-handoff.md:234–296` — **20,754 B**, ten `#### OR-…` entries all marked `✅ RESOLVED` / `CLOSED` (newest 2026-07-02, oldest 2026-05-31) | their beat blocks + `archive/pm-handoff-beats-*` (the resolutions were banked at v22 b?, beat 50, beat 43, …) | **90.1 %** of the 23,041 B `## Open Risks` section is a dead ledger; live risk = **2,287 B** (2 entries). |
| D9 | **The v56 prompt's state section** | `v56 prompt:27–35` §2 — **3,505 B** | `pm-handoff.md:8` seg 1 + `:15–40` + `PROJECT_SNAPSHOT.md:8` — **44,632 B** | **51 %** (33/65) of §2's facts are already in the spine. §2-only (49 %) = the brand track, the standing fences, FE/bench state. |
| D10 | **The W-HIVE-1 charge** *(not seeded — found)* | `v56 prompt:61–68` §5 — **3,939 B** | `context/instructions/2026-08-22_research-lane_W-HIVE-1_…_brief.md` — **11,780 B** | **72 %** (28/39) of §5's facts are in the brief. The prompt re-narrates a dispatch that has its own file. |
| D11 | **The E3 availability class** | `2026-08-22_R6R8_intake_two-layer-audit_v55-beat-5.md:42` (§3 H-1) — **1,351 B** | `R9_E3-HEALTH_…_coding-instruction.md:16–23` "What this implements" — **2,796 B** | **39 %** (9/23) — and R-9 already *cites* "beat-5 audit H-1". **Seed (e) largely REFUTED — see §3 P-X1.** |
| D12 | **The R-9 pre-verification** | `context/pre-verifications/WU-R9.md` — **12,551 B** | `R9_…_coding-instruction.md` — **37,394 B** | **35 %** (122/353). The WU file is a line-number census the instruction does not carry. **Seed (e)'s pre-verification clause REFUTED.** |
| D13 | **`coder-lessons.md` `**Detail:**` blocks** *(not seeded — found)* | `coder-lessons.md` — 8 `**Detail:**` lines totalling **6,566 B** (mean 821 B) | the returns/audits that minted each lesson (`context/audits/…`) | not a fact-overlap duplication but a **tier violation**: narrative detail sitting in a file every coder session loads whole. |

---

## §3 — The proposals, ranked by bytes saved per session

Lawful verbs only: **MOVE-to-archive**, **POINT**, **OVERWRITE-a-regenerated-digest**. No proposal deletes information. Ranked by hub-launch saving, then coder.

| # | Proposal | Saves / hub | Saves / coder | Saves / FE | Saves / research | Migration |
|---|---|---:|---:|---:|---:|---|
| **P1** | `## Open Risks` carries OPEN entries only | **20,454** | — | — | — | 1 beat, 1 extraction |
| **P2** | Both `last-verified:` chains become ≤300-char pointers | **14,663** | 5,944¹ | 5,944¹ | — | 1 beat, 2 files |
| **P3** | Beat blocks get a 6,000 B shape cap | **14,599** | — | — | — | ongoing discipline |
| **P4** | `READ-ME-FIRST.md` replaces the launch `ls` sweep | **15,191** | — | — | — | 1 new ≤1 KB file |
| **P5** | Prompt §2 generated from the digest; §5 → pointer | **4,944** | — | — | — | 1 beat (at v57) |
| **P6** | `coder-lessons`: size rotation + 1.2 KB cap + Detail-by-pointer | — | **16,153** | — | — | 1 beat, 1 rotation |
| **P7** | The week-plan row retires from coder Tier 1 | — | **6,925** | — | — | 1 line in `CLAUDE.md` |
| **P8** | `coder-handoff` frontmatter chain retires | — | **3,835** | — | — | 1 beat, fold 4 facts first |
| **P9** | `PROJECT_SNAPSHOT` body = overwritten ≤2 KB digest | 278² | 278² | 278² | — | 1 beat |
| | **TOTAL** | **−70,129 (−35.9 %)** | **−33,135 (−18.5 %)** | **−6,222 (−4.5 %)** | **0 (−0 %)** | |

¹ P2's snapshot half only (6,744 → 800 B); its pm-handoff half (8,719 B) is hub-only. P2 + P9 together are the 6,222 B every lane that reads `PROJECT_SNAPSHOT.md` saves. ² P9's byte effect is near-zero — its value is being P5's single source.

**P1 — `## Open Risks` carries OPEN entries only.** 23,041 → **2,587 B** (header + the 2 OPEN entries at 2,287 B + one ≤300 B archive pointer). *Basis:* D8 — 20,754 B / 90.1 % is ten entries all stamped `✅ RESOLVED` or `CLOSED`, newest 2026-07-02, oldest 2026-05-31, every one read at every hub launch since. *The rule:* **"A risk entry stamped RESOLVED or CLOSED moves to `context/handoff/archive/open-risks-resolved-<date>.md` at the NEXT beat after its stamp. `## Open Risks` carries OPEN entries plus exactly one archive-pointer line — never a resolved entry."** *Risk:* a fresh session loses inline sight of a resolved risk's history. *Closed by:* the pointer line + an archive-map row (the pointer-trail law already requires both). *Migration:* one hub beat; `mv`-to-archive verbatim, one pointer line, one archive-map row.

**P2 — both chains become ≤300-char pointers.** pm-handoff `:8` 11,689 → **~2,970 B** (9 × ~330); snapshot `:8` 6,744 → **~800 B** (2 segments + the rotation pointer, the rest rotating at the beat). *Basis:* D1–D3 — a segment restates **85–100 %** of its own facts from the block directly below it, and carries only 13–27 % of that block's facts: it is a lossy retelling, not an index. D4 — 88 % of the snapshot chain is the pm-handoff chain again. **This refutes the hub's seed in its stated direction and strengthens the conclusion:** the seed said "the chain re-states ~40 % of every block"; measured, the chain re-states 13–27 % of the block while being **93 % redundant on its own content**. *The rule:* **"A `last-verified:` chain segment is a POINTER, ≤300 characters, in one fixed form: `<date> (vN beat K — TITLE. Orders: <n>. Next: <one clause>.)` and nothing else. Detail lives in the block or entry the pointer addresses. pm-handoff caps at 8 segments + the rotation pointer; PROJECT_SNAPSHOT at 2 + the rotation pointer."** *Risk:* chain segments 4–8 are today the only launch-visible carrier of beats whose blocks the hub does not read. *Closed by:* every pointer naming its block's exact `## <date> (vN beat K …)` heading — in-file for live beats, via the archive map for rotated ones.

**P3 — the beat block gets a 6,000 B shape cap.** Newest three 32,599 → **18,000 B**. *Basis — the seed's premise is REFUTED at the bytes.* The brief and the v56 prompt §5 both say "the beat blocks run 3–6 KB". Measured, the ten live blocks are **11,494 · 11,291 · 9,814 · 8,542 · 10,558 · 7,043 · 11,347 · 4,403 · 5,611 · 6,877 B** — mean **8,698 B**, newest-three mean **10,866 B**. Only the two v54 blocks (the oldest) are under 6 KB. 6,000 B is chosen as the 20th percentile of the live distribution — a cap two of the current ten already meet. *The rule:* **"A beat block caps at 6,000 B. Narration beyond the cap files to the beat's audit/return in `context/audits/` and is reached by a pointer on the block's last line. Verdicts, orders and rulings never leave the block — only narration does."** *Risk:* **the highest of the nine.** A block is the hub's own state digest; a careless truncation could strand a banked verdict (law 16). *Closed by:* the verdict/narration split written into the rule, plus the block-tail pointer. **Recommend adopting P3 as a target with a hub review at each beat, not as a hard truncation.**

**P4 — `context/status/READ-ME-FIRST.md` (≤1,024 B) replaces the launch sweep.** 16,215 → **1,024 B**. *Basis:* the v56 prompt §1 item 5 mandates `ls` over `context/*` at every launch; measured, that is **16,215 B of tool output across 375 paths**, paid before the first act. *The rule:* **"`context/status/READ-ME-FIRST.md` is ≤1,024 B and names exactly three things: the digest, the newest beat block's file, and where a session's own prompt/brief lives. The repo-map sweep leaves §1 and becomes an on-demand act, scoped to ONE directory per call."** *Risk:* the sweep is how a hub discovers files nobody told it about. *Closed by:* keeping the sweep in §1's pointer-form on-demand list with its trigger named ("before any act that needs a file the spine did not address").

**P5 — the prompt stops restating.** §2 3,505 → ~1,700 B; §5 3,939 → ~800 B. *Basis:* D9 (51 % of §2 already in the spine) and D10 (**72 % of §5 already in the W-HIVE-1 brief** — a duplication the hub did not seed). *The rule:* **"Section 2 is GENERATED from the PROJECT_SNAPSHOT digest and carries only the delta the digest does not — never a copy. Any prompt section describing a dispatched lane is a ≤5-line POINTER to that lane's brief."** *Risk:* the prompt is the first file a hub reads and could be the only reachable one. *Closed by:* §2's first line naming the digest path; "the spine outranks Section 2" already governs.

**P6 — `coder-lessons.md`: size rotation + a per-lesson cap + Detail-by-pointer.** 32,153 → **≤16,000 B**. *Basis — the seed's MECHANISM is refuted, its threshold kept.* Seed (d) says "> 24 KB → the oldest month to the archive". Measured, **all 12 lessons fall inside ONE month** (2026-08-02 → 2026-08-22; mean lesson **2,620 B**, growth **≈1.6 KB/day**): "rotate the oldest month" would empty the file. The `**Detail:**` blocks are 6,566 B across 8 lessons (D13). *The amended rule:* **"When `coder-lessons.md` exceeds 24,000 B, MOVE the oldest lessons to `archive/coder-lessons-<YYYY-MM>-rotated-<date>.md` until the file is ≤16,000 B — by lesson count, never by calendar month. Each lesson carries Discovery + Impact only, ≤1,200 B; `Detail` becomes a one-line pointer to the return that minted it."** *Risk:* a Detail a future lane needs is one file away. *Closed by:* the pointer naming the return path + an archive-map row.

**P7 — the week-plan row retires from coder Tier 1.** 6,925 → **0 B**. *Basis:* `coder/CLAUDE.md:23` orders "read the current week's plan in `../context/planning/weeks/`"; the newest file present is `2026-W31_jul27-aug02.md` — **three weeks stale** on 2026-08-22 (W34), and `weeks/` has had no new file since. The row buys a stale read or a failed lookup. *The rule:* **"The coder's plan-of-record is the newest `coder-handoff.md` entry plus the active instruction. `context/planning/weeks/` leaves Tier 1."** *Risk:* none measurable. **FLAGGED FOR HUB ROUTING:** this edits `coder/CLAUDE.md`, a role-skill carrier — the hub decides whether it rides this rotation or W-SKILLS-4.

**P8 — the `coder-handoff.md` frontmatter chain retires.** 4,302 → **~467 B** (the 137 B rotation pointer + a one-line authority note). *Basis:* D5–D7 — **88–100 %** of each segment's facts are already in the entry below it; exactly five facts are segment-only. *The rule:* **"`coder-handoff.md`'s frontmatter carries the masthead and a rotation pointer only. The newest entry is authoritative by position; its own heading carries the date and the lane-newest claim."** *Risk:* the five segment-only facts — three SHAs (`9f99368`, `ca0f41d`, `d26777c`) and two counts (`208`, `28`) — vanish from the launch read. *Closed by:* folding those five into their entries **in the same beat, before** the chain retires — a named precondition, not a follow-up.

**P9 — `PROJECT_SNAPSHOT`'s body is an overwritten digest.** Body 2,278 → ~2,000 B. *Basis:* the body is **already** mostly pointer-form (`:21` reads "Re-derive from the newest chain segment's ranked-next…"), so seed (b)'s body clause is largely already done; **73 % of the snapshot's 9,242 B is its chain line**, which P2 handles. *The rule:* **"PROJECT_SNAPSHOT's body is an OVERWRITTEN digest ≤2,000 B — HEADs · fences · wait-states · the next three acts — rewritten every beat, never appended. It is the single source Section 2 is generated from."** *Risk:* an overwrite loses history. *Closed by:* the chain (now pointers) is the history; nothing in the digest is unique to it.

**P-X1 — seed (e) refuted; the instruction/pre-verification pair is NOT a lever.** The brief seeds "instructions cite the audit that minted them instead of re-narrating it" and "a pre-verification row never restates a line the instruction already cites". Measured: the R-9 "What this implements" section (2,796 B) shares **39 %** of its facts with the audit H-1 it derives from (1,351 B) — and it **already cites** "beat-5 audit H-1" (D11); the recoverable overlap is ~1,000 B on a 37,394 B instruction (**2.7 %**). WU-R9 shares **35 %** of its facts with the instruction (D12), and the shared portion is the "Coder re-verifies" column — the pre-verification's whole purpose. **Recommend: drop (e) from the rotation.** The instruction's real weight is its files table and specification, which are the deliverable. If the hub wants an instruction lever, the measurable one is the "Files to read before starting" section (4,081 B) — but that is a read *set*, not a duplication, and shrinking it moves cost rather than removing it.

---

## §4 — The laws that do not change (and the collisions flagged)

Stated here so no proposal above is read as proposing against them:

1. **Archives are VERBATIM.** Delete nothing; `mv`-to-archive only. P1, P6 and P8 are MOVE operations; P2, P3, P4, P5 are POINT operations; P9 is OVERWRITE-a-regenerated-digest. No proposal uses a fourth verb.
2. **The pointer-trail law — zero dangling addresses; the archive map maintained at every rotation.** P1, P6 and P8 each require a new archive-map row in the same beat. *(See §6 for a pointer-trail staleness found in passing.)*
3. **Returns file to `context/audits/`.** This return does.
4. **The two-layer audit on every return.** This return is built for it: every figure carries its command, every duplication carries both locations.
5. **Law 16 — banked verdicts are final; the chain and blocks CARRY verdicts.** A proposal may move a verdict's carrier, never erase one. **⚠️ COLLISION FLAGGED — P3 (the block cap) is the only proposal that touches a verdict carrier.** Its rule is written to file *narration* and keep *verdicts, orders and rulings* in the block, but the split is a judgement call the hub must make per block. Recommend P3 be ratified as a target with review, not as a mechanical cap. **P2 and P8 also touch verdict-adjacent carriers** — both are safe only because the block/entry below carries the same verdict (D1–D3, D5–D7, measured), and P8 is explicitly gated on folding its five segment-only facts first.
6. **Law 11 — read once, bank on disk; point rather than copy.** Every proposal here is an application of it.
7. **The masthead convention** (HTML-comment frontmatter: file/purpose/audience/update-cadence/state-type/status/last-verified). P2 and P8 change what the `last-verified:` line *contains*; neither removes the line or any other masthead field.
8. **Only the hub writes the spine.** This lane wrote nothing but this file.
9. **Chat is not a storage tier** — every fact a fresh session needs is in a FILE. P4's `READ-ME-FIRST.md` is a file; P5's generated §2 sources from a file.
10. **H17 — a fresh session never reads a predecessor's scratch.** Observed: this lane read only git objects and its own `/tmp`.
11. **"The spine outranks Section 2."** P5 depends on it and does not weaken it.
12. **The skills' rule census belongs to W-SKILLS.** See §4b — measured only, never proposed against here.

### §4b — The three role skills' launch cost (MEASURED ONLY — for the W-SKILLS-4 charter)

Per the §3 scope fence, these are measurements and observations for the W-SKILLS program's 60-in/60-out census discipline. **Nothing here is a rotation proposal and nothing here should be ratified under this return.**

| File | Bytes | Read by | Observation |
|---|---:|---|---|
| `project-manager/SKILL.md` | **53,020** | every hub launch | The **masthead is 24,599 B (46.4 % of the file)**: yaml 772 · masthead head 210 · `last-verified:` **2,950** · `pass-history:` **1,066** · `arc-disciplines` header + 37 numbered rules **12,562** · `strategy-layer:` **2,141** · `state-pointer:` 610 · `durable-disciplines` D1–D18 **4,283**. Body = 28,421 B. |
| `project-manager/references/freshness-preflight.md` | **16,153** | every hub launch (SKILL.md :84, :102, :205 — mandatory) | |
| `coder/SKILL.md` | **35,667** | every coder launch | |
| `nexsys-frontend/SKILL.md` | **41,636** | every FE launch | The single largest FE cost. |
| **Skill-side share of each launch** | hub **69,173 / 195,380 = 35.4 %** · coder **57,130 / 179,539 = 31.8 %** · FE **58,999 / 139,612 = 42.3 %** | | |

Two observations for the charter, offered as findings not proposals: (i) the PM masthead's `last-verified:` (2,950 B) and `pass-history:` (1,066 B) lines are **provenance**, and `pass-history` says so of itself ("PROVENANCE, not law — no rule lives on this line") — 4,016 B of every hub launch that carries no rule; (ii) after this lane's proposals land, the skills become **55.2 % of a hub launch and 44.2 % of a FE launch** — i.e. **the skills become the dominant launch cost**, which is the argument for scheduling W-SKILLS-4 immediately after this rotation rather than in parallel with it.

---

## §5 — The AFTER estimate, and the rotation rule that replaces "rotate when it feels heavy"

### 5.1 AFTER, per session type

| Row | BEFORE | AFTER | Δ |
|---|---:|---:|---:|
| **HUB** — PM SKILL.md | 53,020 | 53,020 | 0 (W-SKILLS-4) |
| PM freshness-preflight | 16,153 | 16,153 | 0 (W-SKILLS-4) |
| v56/v57 prompt | 24,852 | 19,908 | −4,944 (P5) |
| PROJECT_SNAPSHOT.md whole | 9,242 | 3,020 | −6,222 (P2, P9) |
| pm-handoff chain | 11,689 | 2,970 | −8,719 (P2) |
| pm-handoff newest 3 blocks | 32,599 | 18,000 | −14,599 (P3) |
| pm-handoff `## Open Risks` | 23,041 | 2,587 | −20,454 (P1) |
| env-model §§11–12 | 8,569 | 8,569 | 0 |
| the launch sweep | 16,215 | 1,024 | −15,191 (P4) |
| **HUB TOTAL** | **195,380** | **125,251** | **−70,129 (−35.9 %)** |
| *hub, spine-side only* | *126,207* | *56,078* | *−70,129 (**−55.6 %**)* |
| **CODER TOTAL** | **179,539** | **146,404** | **−33,135 (−18.5 %)** |
| **FE TOTAL** | **139,612** | **133,390** | **−6,222 (−4.5 %)** |
| **RESEARCH TOTAL** | **36,700** | **36,700** | **0** |
| **WEEK — conservative (6)** | **941,991** | **692,247** | **−249,744 (−26.5 %)** |
| **WEEK — heavy (10)** | **1,548,990** | **1,125,853** | **−423,137 (−27.3 %)** |

FE and research barely move because their cost is skills (W-SKILLS-4), a frozen contract, the core repo, and self-contained briefs. **The spine-side hub read falls by 55.6 % and — the point of §5.2 — stops growing.**

### 5.2 The measured rotation rule

**The seed, refuted at the numbers.** Seed: *"a fresh-session read > ~60 KB rotates at the next beat."* Measured at the objects across the v54→v56 arc:

| Commit | `pm-handoff.md` whole | chain `:8` | newest 3 blocks | `## Open Risks` | **hub read** |
|---|---:|---:|---:|---:|---:|
| `21b7e4c` (pre-rotation) | 301,693 | 77,714 | 16,997 | 21,367 | **116,078** |
| `04629b1` (post-rotation) | 42,645 | 2,158 | 16,891 | 21,661 | **40,710** |
| `8f2cb08` | 86,485 | 8,508 | 26,143 | 21,661 | **56,312** |
| `ee767de` | 111,814 | 11,352 | 29,647 | 23,041 | **64,040** |
| `c974b52` (HEAD) | 123,645 | 11,689 | 32,599 | 23,041 | **67,329** |

Command: `git --no-optional-locks show <sha>:context/handoff/pm-handoff.md` piped to `sed -n 'A,Bp' | wc -c` with A/B re-derived per commit from `grep -n '^## '`.

Three things follow. **(1) Rotation is aimed at the wrong quantity.** The v54 b10 rotation cut the file 85.9 % and the hub read 64.9 % — and the chain line alone accounts for **100.2 %** of the read reduction (−75,556 B of a −75,368 B total; the blocks moved −106 B and Open Risks **+294 B**). The 259 KB of block tail it archived was never in the launch read. **(2) The read grows at 3,803 B/beat** (40,710 → 67,329 over 7 beats) while the file grows at **13,500 B/beat** — the read is 28 % of the file's growth, so file size is a poor proxy for it. **(3) The 60 KB threshold is unworkable as stated:** starting from a freshly-rotated 40,710 B, the read crosses 60 KB after **five beats** — and the v55/v56 arc ran seven beats in twenty hours. The rule would demand a rotation daily or twice daily, which is why "rotate when it feels heavy" survived it.

**The rule I would make standing:**

> **ROTATION IS ARCHIVE HYGIENE, NOT TOKEN ECONOMY. The launch cost is governed by four REGION CAPS checked at every beat, never by a file-size threshold:**
> **(1)** `pm-handoff.md` line 8 ≤ **3,000 B** — 8 pointer segments plus the rotation pointer;
> **(2)** the newest three beat blocks ≤ **18,000 B** combined (6,000 B each);
> **(3)** `## Open Risks` carries **OPEN entries only** plus one archive pointer;
> **(4)** `PROJECT_SNAPSHOT.md` ≤ **3,500 B** whole.
> **A beat that would breach a cap fixes the cap in that same beat — the block being written is the one that gets trimmed, so the cost is always paid by the beat that incurred it.** Rotate a file to the archive when its rotated-side tail exceeds ~250 KB: a housekeeping cadence at the hub's convenience, which no longer buys launch bytes because the caps already hold the read flat.

Under those caps the hub's spine-side read is **26,577 B** (2,970 + 18,000 + 2,587 + 3,020) and **flat by construction** — against 67,329 B today growing at 3,803 B/beat. The caps are self-enforcing at the point of writing; no threshold has to be watched.

---

## §6 — What I could not measure, and why

1. **Token counts, as distinct from bytes.** Everything here is bytes at the git object. The spine is dense in multi-byte characters (`·`, `—`, `→`, `§`, `⏺`) — `pm-handoff.md:8` is 11,414 characters and **11,689 bytes**. Byte savings are a floor on token savings for ASCII-dominant text and are not a clean 4:1 conversion. If the hub wants token figures, they need a tokenizer this lane did not have.
2. **What a session actually reads versus what it is told to read.** The census is derived from the four sources of truth (v56 §1, `coder/CLAUDE.md` tiers, `nexsys-frontend/CLAUDE.md` :20–:25, the RS-4 §0) as the brief directs. A hub that greps rather than reads pays less; one that reads `pm-handoff.md` whole pays 123,645 B instead of 67,329 B. **The census measures the prescribed launch, not observed behaviour.**
3. **Whether `project-manager/CLAUDE.md` (9,958 B) auto-loads in remote Cowork.** Listed as conditional in §1.1. It is a host-CC convention and the hub runs remote; I could not verify the loader's behaviour from inside the repo.
4. **Fact-recurrence is a proxy, not a semantic diff.** §2's percentages come from one regex over SHAs, `LABEL-N` identifiers, `§`-refs, filenames and numerics ≥ 2 digits. It is deliberately conservative (prose paraphrase that repeats no identifier scores as non-duplication) and is why D1–D3 report 85–100 % rather than a softer number: those segments genuinely carry no identifier their block lacks. A hub re-measuring D1 should expect 15/15 exactly. **Method-sensitivity, checked before filing:** re-running D1–D3 and D5–D7 with a *stricter* extractor (7-hex SHAs, `WU-*`, `H<n>`, `§OP-*` and `R-<n>` labels only) gives **100 / 100 / 100 / 100 / 80 / 75 %** against the 100 / 95 / 85 / 100 / 93 / 88 % reported. The direction and the conclusion hold under both; the strict pass is what surfaced `d26777c` as a fifth segment-only fact in D7. Percentages are stable to ±13 points by method — **treat the ranking as robust and any single percentage as ±15**.
5. **The archive tail was not read** (env-model §12 / the brief's mechanics fence). `cat-file -s` sized it; nothing was opened. The rotated pm-handoff archives alone total **1,656,411 B** across nine files (`git ls-tree -r -l HEAD context/handoff/archive/ | grep pm-handoff-beats`).
6. **A pointer-trail staleness, found in passing, not measured further.** `pm-handoff.md:299` reads *"LIVE above: beats 10 / 9 / 8 + Open Risks"* — the file now carries ten live blocks (v56 b1 → v54 b8). The archive map's *rotated* rows are correct; only its *live* summary is stale. Flagged for the hub's rotation beat; this lane wrote nothing.
7. **Cross-repo skill-mirror staleness** (`coder/references/freshness-preflight.md` Check 6's third location) is unverifiable from a remote session by that check's own rule. Not attempted.

---

## §7 — Harvest (≤5 lines) — what the next lane of this kind should know

1. **Measure the READ REGION, never the file.** A rotation that cut `pm-handoff.md` 85.9 % cut the launch read 64.9 %, and one line — the chain — accounted for **100.2 %** of that reduction. File size is a 28 %-correlated proxy for launch cost; region caps are the instrument, and they are checked at the beat that writes, not by a watcher.
2. **Audit the ledger sections nobody names.** The single largest lever in this lane (20,454 B/launch) was `## Open Risks`, which no seed mentioned and which is **90.1 % resolved entries dating to 2026-05-31**. Sections named for *live* state accumulate *dead* state silently, because nothing in the naming ever prompts a re-read.
3. **Seeds are hypotheses and three of eight failed.** (e) refuted (39 %/35 %, ~2.7 % recoverable); (d)'s mechanism refuted (all 12 lessons are inside one month — "rotate the oldest month" empties the file); the "beats run 3–6 KB" premise refuted (mean **8,698 B**, newest-three mean **10,866 B**). Two duplications the seeds missed (D8, D10) were worth more than four that were seeded. **Measure the seed before costing the fix.**
4. **Direction matters in a duplication claim.** "The chain restates 40 % of the block" and "the chain is 93 % redundant against the block" describe the same two spans and imply different fixes. Always report both directions: X-in-Y and Y-in-X, with both spans' bytes.
5. **Self-contained beats shared-mutable.** Research lanes cost 21–37 KB and hub lanes 195 KB, and the difference is not volume — it is that a brief is written once and read once, while the spine is written by every beat and read by every launch. **The cheapest future saving is not compressing shared state further; it is moving a lane's launch set out of shared state and into its own brief.**

---

---

## Appendix — the self-verification run before filing (a disclosed strengthener, outside the ruled §0–§7 shape)

HEAD re-checked at close: **`c974b52`, unmoved** since the census opened — no re-measure of moved files was required. Every `pm-handoff.md` region was then re-derived **from scratch by a second route** — fresh `git show` export, boundaries re-found by scanning for `^## ` rather than reused, bytes counted by byte-level join rather than `sed | wc -c` — and reproduced **exactly**: total 123,645 · chain 11,689 · newest-3 blocks 32,599 · `## Open Risks` 23,041 (live 2,287 / resolved 20,754) · **hub read 67,329**. Whole-file figures were cross-checked `CFS` against region sums for `pm-handoff.md` (123,645 ✓), `PROJECT_SNAPSHOT.md` (9,242 ✓), `coder-handoff.md` (23,120 ✓), `coder-lessons.md` (32,153 ✓), and `CFS`-confirmed for `project-manager/SKILL.md` (53,020), `coder/SKILL.md` (35,667), the v56 prompt (24,852) and the FE `SKILL.md` (41,636). All §3/§5 arithmetic was recomputed independently; two errors were found and fixed before filing (a double-counted 278 B snapshot row in the P2/P9 columns, and an archive-total transcription off by 96 B). The six chain-vs-block duplication pairs were re-run under a second extractor — see §6.4.

*Filed 2026-08-22 (America/Chicago) · W-HIVE-1 · read-only lane · HEAD `c974b52` · one artifact, no spine writes, no commits · every figure re-measurable by the command printed beside it.*

<!--
file: context/audits/2026-08-22_five-lane_intake_two-layer-audit_v56-beat-2.md
purpose: the two-layer intake audit of the FIVE read-only lane returns that landed 2026-08-22 (all five on disk in context/audits/, md5-identical to Nick's pastes; law 37): W-HIVE-1 · FE-SWAP-CENSUS · R10-IN-L · BRAND-SPRINT-1 · R10-IN-P. Layer 1 = each return's own claims; layer 2 = the hub re-measuring at the git objects / the instrument (labels are claims, quotes are evidence — D17/D18). One artifact for five intakes (H11). Verdicts, the corrections found, and the rulings packaged for Nick.
audience: the hub (the beat-3 rotation executes from §1's ratified set); Nick (the H10 words in §6); the R-10 charter (the docket additions in §5).
status: FILED (v56 beat 2, 2026-08-22 ~17:00 CDT). HEADs at audit: hivemind `c974b52` · core `89a912e` · docs `a53f474` · bench `4539f13` · skills `5105abc`.
disclosed: three stale 0-byte `.git/index.lock` files (hivemind 21:29Z · skills 21:42Z · bench 21:42Z — the lanes' bridge-killed git reads, the §4/H14 class) found at the launch porcelain with no git process alive; cleared by `mv` to `_scratch/_to_delete/index.lock.<repo>.2026-08-22T2148Z` (delete-nothing). Nick's next commit would otherwise have failed.
-->

# The five-lane intake — two-layer audit (v56 beat 2)

## §0 Verdicts (one line each)

| Return | Bytes | Layer-2 checks | Verdict | Corrections (hub) |
|---|---:|---|---|---|
| W-HIVE-1 `…_W-HIVE-1_hivemind-token-economy_return.md` | 38,363 | 9 figures re-measured at `c974b52` (chain 11,689 · blocks 32,599 · Open Risks 23,041 · resolved region 20,754 · snapshot chain 6,744 · coder chain 4,302 · PM SKILL 53,020 · the `ls` sweep 16,125/380 today vs 16,215/375 — five returns added since · lessons 12/0 by month); D1 re-run: 11/11 segment identifiers in the block | **ACCEPT** — every figure reproduced exactly; three seeds refuted at the numbers stand refuted | **ONE classification error:** `OR-M13-SDNOTIFY` (`pm-handoff.md:280–:284`, **2,690 B**) is OPEN, not resolved — no ✅ stamp; its resolution condition ("pick the transport") is still owed and R10-IN-L just recommended on it. P1's live set = **3** entries (≈4,977 B), the dead ledger = 18,064 B, P1 saves ≈17.8 KB not 20.5 KB. Ranking unchanged. |
| FE-SWAP-CENSUS `…_FE-SWAP-CENSUS_return.md` | 26,560 | The instrument re-run at `89a912e`: **25 files / 54 lines ✓**; module-wide **32 ✓**; manifest/favicon/og hits **0 ✓**; `index.html:9`/`:30`, `format.test.ts:46`, `unserved404.test.tsx:153`, `README.md:1/:3` quoted exactly ✓ | **ACCEPT** | **One NOTE, not a defect:** the `README.md:414` grep hit is the JPMS namespace `com.homesynapse.*` (OUT by the return's own rule); the IN item is the SENTENCE at `:413–:415` ("under trademark review … the namespace is unaffected") — the flip's README row rewrites the note's tense and must never touch the namespace token. `BRAND` site count: the hub counts 17 non-import sites in 7 files incl. the declaration + the test; the return's 14/6 excludes those — a convention, the 14 named sites all verified. |
| R10-IN-L `…_R10-IN-L_liveness-and-notify-transport_return.md` | 36,600 | Code: `HomeSynapseCore.java:1476–:1489` (the catch-all degrade to NoOp) ✓ · `:725–:726`/`:789–:790` (READY after Phase 6) ✓ · `SystemdHealthReporter.java:157–:166` (the ctor throws) ✓ · unit `:55` `TimeoutStartSec=120` ✓ · `SubscriberMode` = COLD/REPLAY/TRANSITION/LIVE/**SUSPENDED** ✓ · Doc 09 `:997–:998` Q1 resolved "requires authentication … sd_notify (LTD-13)" ✓ · **LTD-01 = Java 21 LTS, LTD-10 = Gradle ✓ — the hub's brief mis-attributed the pin (owned; fixed as an R-7b comment rider)**. Primaries: `systemd.service(5)` NotifyAccess implicit-`main` / ExecStartPost "as determined by Type=" / WatchdogSec SIGABRT — quoted verbatim at man7 ✓; JEP 442 third preview JDK 21 ✓ (454 final in 22) | **ACCEPT** — decision-shaped as briefed; f1 (the live-trap flip block) is a real finding | **Two hub bytes on R-9 before dispatch (D8):** the 503 matrix names all FOUR non-LIVE constants (it named three + "walk the constants"); rider R-9-b rewrites the M13 flip block as a DANGER note (comment-only; the unit is already M). |
| BRAND-SPRINT-1 `…_BRAND-SPRINT-1_return.md` | 45,587 | All seven WCAG ratios recomputed from the shipped hexes: **4.47 · 4.76 · 6.38 · 16.40 · 16.53 · 8.78 · 2.42 — exact** · `tokens.css` accent-500 `#1577be` / -600 `#11608f` / -300 `#6db8e8`, light bg `#f6f8fa` ✓ · `AuthGate.module.css:22–:28` (13 px uppercase 0.02em secondary) ✓ · `brand.mjs:14` + `Base.astro:19/:30/:50/:65` ✓ · website census 20 files ✓ · the NL raw docx carries "meditation, air freshener, fresh breath" and the bank `.md` does NOT ✓ · the ES Digimon note in the raw docx ✓ · the JP paste carries **0 katakana characters** ✓ | **ACCEPT** — the onset-premise pushback is carried by the raw files; Direction B's recommendation is Nick's to rule at the word | none. The hub fold owed at the Pelton beat: the runbook's website row (one token + the greenfield icon/og/manifest set); the bank's F-N4 note; the 07-22 exploration §3 SUPERSEDED-BY-SHIPPED. |
| R10-IN-P `…_R10-IN-P_physics-seed-vs-measured-bench_return.md` | 53,731 | `constants.yaml:65` the 02P ULID ✓ · retention `:11` "never pruned by hand" ✓ · `nightly_digest.py:133–:139` the ONE line ✓ · G1 `:188` viewPosition 91229 @ 05:44:17Z ✓ · `:233` the 02P row (2026-07-18 20:32:11, ✓ Available) ✓ · sitting-record `:49` viewPosition 104220 @ 23:59:59Z ✓ · acquisition brief `:46` ~$16.90 ✓ · A-14 `:22` the weekend-shape inference ✓ | **ACCEPT** — the lane's own 20/20 citation subagent + the hub's 8/8 | none. The §5 P-1 block is adjudicated in §6 (R-P1). |

**Fences, all five:** read-only held (the hivemind porcelain shows exactly the five `??` returns; core/docs/bench/skills porcelains EMPTY); nothing public (BRAND: no registrar/handle/office queries; the JPO pages procedural); no hardware (IN-P never reached the Pi); one artifact each.

## §1 W-HIVE-1 — the ratified set (the hub executes; the lane proposed)

| # | Proposal | Ruling | When | Note |
|---|---|---|---|---|
| P1 | `## Open Risks` carries OPEN entries only + one archive pointer | **RATIFIED, corrected** | beat 3 | live = OR-E3-PROBE · OR-REHOMED-OQ · **OR-M13-SDNOTIFY**; the ten resolved/closed blocks (18,064 B) → `context/handoff/archive/open-risks-resolved-2026-08-22.md` verbatim + an archive-map row |
| P2 | both `last-verified:` chains → ≤300-char pointers (`<date> (vN beat K — TITLE. Orders: n. Next: clause.)`); pm-handoff caps at 8 segments + the rotation pointer, snapshot at 2 | **RATIFIED** | beat 3 | the beat-1/2 segments already conform; the older seven rewritten as pointers naming their block headings; the rewritten-out text is already verbatim in the blocks below (D1–D3 measured 85–100 %) and the pre-rewrite line goes to the archive file as a safety copy |
| P3 | beat blocks ≤ 6,000 B — narration to the audit file by pointer; verdicts/orders/rulings never leave the block | **RATIFIED as a TARGET with per-beat hub review** (the law-16 collision flagged by the lane) | this beat onward | the beat-2 block is the first written to it |
| P4 | `context/status/READ-ME-FIRST.md` ≤ 1,024 B; the `ls` sweep leaves §1 (on-demand, one dir per call) | **RATIFIED** | beat 3 | |
| P5 | the prompt's §2 generated from the digest; lane sections → ≤5-line pointers | **RATIFIED** | v57 banking | |
| P6 | `coder-lessons` rotates by lesson COUNT to ≤16 KB when >24 KB; 1.2 KB cap; Detail → pointer | **RATIFIED; the rotation waits for R-9's closeout to land** (the lane writes this file tonight — a bridge write now would collide) | beat 4/5 | the cap rule itself is a coder-skill convention → W-SKILLS-4 |
| P7 | the week-plan row leaves coder Tier 1 | **ROUTED to W-SKILLS-4** (a role-skill carrier; Check 9 mirror sync) | the skills pass | interim cost 6.9 KB/coder launch accepted |
| P8 | the coder-handoff chain retires (fold the 5 segment-only facts first) | **ROUTED to W-SKILLS-4** — the coder's closeout convention writes that chain; retiring it without the convention re-grows it at the next closeout | the skills pass | |
| P9 | PROJECT_SNAPSHOT body = overwritten digest ≤ 2,000 B | **RATIFIED** | beat 3 | |
| P-X1 | seed (e) dropped | **RATIFIED** | — | |
| the rule | **ROTATION IS ARCHIVE HYGIENE; the launch read is governed by four REGION CAPS checked at every beat** — pm-handoff `:8` ≤ 3,000 B · newest three blocks ≤ 18,000 B · Open Risks OPEN-only · PROJECT_SNAPSHOT ≤ 3,500 B whole; the beat that would breach a cap fixes it in the same beat; archives rotate when the rotated-side tail > ~250 KB | **RATIFIED as standing law (replaces the "rotate above ~60 KB" seed)** | now | the v57 prompt carries it as a numbered law |
| §4b | the skills' launch cost (PM 53,020 · coder 35,667 · FE 41,636; the PM masthead's 4,016 B of provenance lines) | **→ the W-SKILLS-4 charter, authored at beat 3, dispatched after the rotation** | Mon/Tue | after the rotation the skills are 55 % of a hub launch |
| §6.6 | the archive map's "LIVE above: beats 10 / 9 / 8" line is stale | fixed at beat 3 | | |

## §2 FE-SWAP-CENSUS — what changes

The flip WU at H+2–6 is **pre-authored**: 4 files in FE territory (the token; `index.html` ×2 lines; the re-keyed negative assertion; the new pin — with FE-SWAP-GATE landed first the count is 5 incl. the pin's own update), plus the README rows as a **separate hub-authored patch** (ruling (ii) — write-isolation intact; the FE lane never writes repo-root). The "red-first" gate the runbook assumed is minted as **FE-SWAP-GATE** (`context/instructions/2026-08-22_FE-lane_SWAP-GATE_brand-token-pin_micro-WU.md`, ISSUE-READY, 2 files) — Nick's dispatch word. The favicon/og/manifest void is **greenfield B-1 work**, one deliverable for both surfaces, post-flip or carrying the ruled name. The §5 dry-run block is Nick's, optional.

## §3 R10-IN-L — what lands now vs the charter

Now (riders on R-9, stamped): R-9-a SUSPENDED in the 503 matrix · R-9-b the M13 flip block rewritten as a DANGER note. **The charter (R-10) docket gains:** R-L1 C-1 (rec) · R-L2 T-0 with the timer AUTHORED-AND-HELD (rec) · R-L3 NO (rec) · the Doc 09 §15 Q1 fold (AMD-class — a resolved Locked open question re-opened by R-9's premise inversion) · the READY-ordering drift vs C12-08/C12-09 (an M13 precondition) · the JDK-trajectory item (LTD-01 21→25; Corretto 25 LTS GA 2025-09-17) · OR-M13-SDNOTIFY's disposition (defer-indefinitely per T-0, or a transport word). **Corrected now:** the JDK pin is LTD-01 (the R-7b rider fixes `install-smoke.yml:56`'s comment; the hub's brief is wrong in the archive and says so here).

## §4 BRAND-SPRINT-1 — held for the word (nothing executes before G-2)

At the branch word: B-1 **Direction B** (rec; A held as the branch-B argument; C the standing interim) · B-7 ゼンドモ of record / ゼンドーモ defensive (ベルドモ / ヴェルドモ for the hedge) as a SEPARATE application — counsel's form · B-2 the fold pasted · B-3 the runbook's website row re-worded (one token `brand.mjs:14` + the greenfield icon/og/manifest set) · B-5 the register governs the post-R-4 kit. Nick's optional 5-min act any time: listen to the JP mp3 and confirm/correct §2.2. The bank gains the F-N4 correction and the NL category-drift note at the Pelton beat.

## §5 R10-IN-P — the charter inputs + the one acceleration

The measured-feasibility column is filled: A as RS-2 scoped it ≈ 37+ h (2.5 weeks of the floor) + a purchase, earliest ~Sep 19–20 behind R-4 → R-4.5 → R-5; **A′ (the ALIVE-anchor inter-report envelope) ≈ 1.5 weekend blocks, no purchase, a SCHEDULING word not an adoption word**; B costs no data (the store is never pruned; ≈1,500 samples accrued if the 02P reports at its declared posture — conditional on C-14). **Charter docket additions:** the A/A′/B word · the A-14 weekend-shape inference (one-word confirm) · the IR `reportingEnvelope` emit-or-not decision · the events-endpoint contract conversation (or the `/state`-read method) · the SP-4 apparatus-change ordering · FE-STATE-DIALECT as the physics surface's prerequisite. **P-1 (`bench.sh state <the 02P ULID>`)** is a single loopback read that addresses neither the S31 nor the nightly nor any scenario — the hub reads the fence narrowly and packages R-P1 below.

## §6 The words (H10; one each; the recs stand un-worded)

- **R-HIVE** — the ratified set executes at beat 3 tonight on the hub-only files (P1/P2/P4/P9 + P3 on the new block), P6 after R-9's closeout: **EXECUTE-BEAT-3 (rec) / HOLD-TO-MON**.
- **R-FE-GATE** — dispatch FE-SWAP-GATE now (one commit, one CI run; the flip becomes red-first): **DISPATCH (rec) / AT-THE-WORD**.
- **R-P1** — run the 02P `/state` read during today's §OP-A visit (2 min; loopback; touches nothing fenced): **RUN-NOW (rec) / HOLD-TO-R-5**.
- **R-9 riders** — R-9-a (SUSPENDED) + R-9-b (the DANGER block): **IN (rec) / OUT** — stamped; OUT reverts before dispatch.
- **R-SKILLS-4** — the charter brief authored at beat 3, dispatched after the rotation lands: **AUTHOR (rec) / LATER**.
- Carried to the R-10 charter, not asked now: R-L1/R-L2/R-L3 · the physics A/A′/B word · the A-14 confirm.

## §7 Harvest

- A ledger named for LIVE state accumulates DEAD state silently — and the census that finds it can mis-file a live entry among the dead (OR-M13): the hub re-reads every entry's own stamp before moving it.
- "Walk the real constants" is not a list — an instruction that names three of four enum values has under-specified the fourth even when it tells the coder to look (R-9-a).
- A staged "flip" comment in a unit is a passes-but-false line when the code it presumes is absent (R-9-b / R10-IN-L f1): any "enable later" block names its code precondition.
- The LTD that pins a toolchain is cited by NUMBER from the register, never from memory (LTD-01 ≠ LTD-10).
- Five read-only lanes on Fable 5 Extra returned in one afternoon at 200 KB and ~zero defects — the expensive thing was never the lanes; it was the shared state they read (W-HIVE-1 §7.5).

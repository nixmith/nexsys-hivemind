<!--
file: context/audits/2026-09-30_W-SKILLS-10_return.md
purpose: W-SKILLS-10 return — the fourteen mints and six practices folded into the three SOURCE skill trees; the census; deviations.
audience: the hub (intake, two layers) · Nick (the two commits)
state-type: lane return
status: RETURNED — filed Wed 2026-09-30 CT (instrument 2026-09-30T12:44:20Z at boot; CT = UTC−5). Zero commits by the lane.
-->

# W-SKILLS-10 — return

## §0 The card
- **DELIVERED.** Boot 12:44Z: hivemind `5351870` (the charter's `84ecb17` + 7 commits, none on a skill-tree path), skills `180375f`, both porcelain 0. Close: hivemind 8 M + this return 1 A; skills 5 M; zero D. Every edit an exact-once anchor replace (`$HOME/w10/rep.py`); no `git add/commit/push`.
- **Byte census (B, before→after; PM = project-manager/, FE = nexsys-frontend/).** PM SKILL 18936→20651 · coding-instruction-format 55431→61480 · laws-ledger 42672→48923 · review-and-quality 27246→28037 · pass-history 9815→12103; coder testing-standards 24966→26191 · pass-history 7427→8294; FE SKILL 16534→17285 · brand-and-design-system 10001→10048 · field-evidence-and-rulings 30530→30819 · freshness-preflight 14495→14970 · pass-history 8644→9637. Unchanged (16): PM CLAUDE 11022 · freshness-preflight 25601 · constraint-enforcement 18644 · cross-subsystem-awareness 17503 · repo-state-protocol 14057; coder CLAUDE 12275 · SKILL 13271 · deviation-and-quality 23700 · freshness-preflight 14957 · homesynapse-mental-model 24403 · java-patterns 29565 · laws-ledger 16994; FE CLAUDE 7680 · build-and-ci-discipline 8528 · contract-consumer 11765 · explainability-and-accessibility 12638. Plus `context/lessons/pm-lessons.md` 113465→114861 (15 heading lines; bodies untouched: 15+/15−).
- **Rule-name census (the charter's grep, per file; after ⊇ before):** PM laws-ledger 43→45 (+THE DERIVATION RULE, +THE CONTEXT RULE OF THE WINDOW; (59)'s apostrophe escapes the grep) · coder laws-ledger 21→21 · FE SKILL 7→7 · PM SKILL, coding-instruction-format, review-and-quality, the three freshness-preflights 1→1 · 19 files 0→0. **Lost: 0 everywhere**; a wider guard (130 names) also lost 0.
- **Preflights:** Check 12 md5 `404da674` / 3,276 B in all three, before and after — amended in none; FE Check 6 (not shared) re-cut alone.

## §1 The folds (each heading marked `— FOLDED (W-SKILLS-10, 2026-09-30; file:line)`)
| Mint | file:line | The sentence |
|---|---|---|
| 09-14 CARD-GREP EXEMPTION | PM/SKILL.md:53 law 5 | a card is exempt from `no_trailers`, asserted for exactly one grep string |
| 09-15 PREMISE GATE | coding-instruction-format.md:568 #32 | every file:line and claim grepped at the pinned HEAD and listed; THE PREMISE TABLE; unsettleable → PREDICTION |
| 09-18 SPOKEN-PITCH | :568 #32(a); laws-ledger.md:87 §2 | pitches, posts, scripts are outward text under the gate; THE SPOKEN CARD |
| 09-18 ENV-KNOB + TABLE-FIRST | :563 #30(e)(f) | knob = env variable, never `-D`; P1 computed from the table; the table governs write sites |
| 09-18 MECHANISM CLAIM | :568 #32(b) | "by construction" only with the code path quoted; order is not freshness |
| 09-19 MOVED STEP | :564 #31 2nd sentence | grep every LIVE packet for the step's verb and object; cite the hits |
| 09-20 SURVEY IS RUN | :568 #32(c) | a survey the hub can run is the hub's act; a say-back names what the block reads |
| 09-23 FROZEN LOG TOKEN | :564 #31 survey line | `grep -n FROZEN` + `containsExactly`; a hit is a fork in the charter |
| 09-23 COUNT | :568 #32(d) | a count names an uncapped instrument or is not stated |
| 09-25 RIG CARD | laws-ledger.md:73 (52)(vi) | five acts, one line; cut from the prompts and the rig's affordances |
| 09-25 ADOPTED-DEVICE STATE | :568 #32(e) | the first card reads every device's availability at the api; the re-join is the first act |
| 09-26 ACTION IS THE UNIT | laws-ledger.md:73 (52)(vi); PM/SKILL.md:55 law 7 | one physical action per message, one line back; a glossary; waits are observables |
| 09-26 RE-SEEN IS ARITHMETIC | :568 #32(e) | `re-seen` = `len(now ∩ prior)` (`nightly_digest.py`:170), not a membership instrument |
| 09-26 PI TIMESTAMP | PM/SKILL.md:53 the clock law | a Pi stamp is America/New_York unless `Z`; converted where read. D-v84-11's lock exhibit: laws-ledger.md:79 (56) |
| 09-07 WHOLE-PASTE (§5.2) | laws-ledger.md:73 (52)(v) | one file whose bytes ARE the act |

## §2 The six practices
| # | Practice | file:line | The sentence |
|---|---|---|---|
| 1 | ONE-WAY-DOOR REVIEW (D-v82-10; D-v84-17) | coding-instruction-format.md:569 #33; PM/SKILL.md:64 law 16 | root / schema / persistence / adoption edits → an independent read before the dispatch line; filed; edits applied first |
| 2 | DERIVATION RULE (D-v82-25) | :570 #34; laws-ledger.md:81 (58) | a number derives from a named source, derivation beside it, or is not written; IR-61 1200 s / 7200 s |
| 3 | BENCH-PULL BLOCK (IR-76) + DIGEST SHA (IR-86; D-v84-6) | laws-ledger.md:82 (59); PM/SKILL.md:93 §6 | every bench landing's card ends with a BENCH-PULL block; a pre-registered nightly runs on its bench sha. coder/SKILL.md untouched |
| 4 | CONTEXT RULE OF THE WINDOW (D-v83-21) | laws-ledger.md:83 (60) → v67 prompt §1b, the dispatch texts | close at the sixth beat or ≈ 60 %, on a deliverable, never a cliff |
| 5 | OPERATOR LOAD: the action is the unit | laws-ledger.md:73 (52)(v)(vi); PM/SKILL.md:55 | §1 rows 09-25 / 09-26 / 09-07 |
| 6 | WIRE-SHAPE FIXTURE (IR-89) | coder/testing-standards.md:499 §15; review-and-quality.md:142 | a wire fixture derives from a real payload or the codec's naming strategy; one test parses real payload text |

## §3 The staleness census (removed | corrected · instrument)
| file:line | Found | Act · instrument |
|---|---|---|
| FE brand-and-design-system.md :56 :61 | three candidate names, a filing state, a date | corrected to the rename-readiness law · a grep for the names, `pelton` and `G-2` over the 28 files: 12 → 0 |
| FE field-evidence-and-rulings.md :7 tail, :101 | the same names and the gate composition | corrected; durable rules kept · same grep |
| FE freshness-preflight.md :58 Check 6 | names + "R-1 HELD until G-2" | corrected · same grep; Check 12 md5 unchanged ×3 |
| PM laws-ledger.md :37 (17) | "(R-1 at G-2)" | pointer form (a ruled sentence; §5.4) · same grep |
| PM SKILL.md :53 | `splice_lib_v1.py` + "its next version carries `precheck()`" | pointer form (`splice_lib_v*.py`, the newest in the tree) · `ls context/process/` = v1 only |
| FE SKILL.md §4 | camelCase/SNAKE_CASE sentence absent | added · `grep -ri 'camel\|snake' FE/` = 0 before; premise at `PersistenceObjectMapper.java:106` |
| all 28 | shas, counts, IR ids, currently/next | none outside dated exhibits · 7-hex grep = 4, all dated; hub-commit remnants = 2, both the law's own history; copied Check-12 lists = 0; `staleAfter\|not yet wired\|threshold` in the coder tree = 0 |
| frontmatter | — | the 12 touched files gained one segment; pass-history ×3 the entry |

## §4 Not changed, why
coder/SKILL.md (row 3; §3 found nothing). The 16 unchanged files (Nick's guard 2). No synced copy. The WUCP checklist, the orchestrator prompt and `bench-troubleshooting-playbook.md` lie outside the trees; the playbook has no BENCH-PULL block (`grep -c` = 0), so PM SKILL §6 points at ledger (59). No charter template in the trees. `splice_lib_v2.card()` is a script. pm-lessons bodies. The three OPEN mints of 09-28/09-29 (:385 :388 :391) — outside the set.

## §5 Deviations
1. Baseline drift `84ecb17` → `5351870`: skill trees untouched; the 14 mints found by `grep -n '— OPEN'` (:343–:382).
2. Refinement (v) of THE OPERATOR-LOAD LAW (the whole-paste law) was never written at W-SKILLS-9. Written now as (v) so (vi) lands where the mints say; its heading marked — a 15th.
3. The 09-23 mint cites THE PRIOR-LEDGER GATE as #32; it is #31. Folded at #31; #32 is the premise gate.
4. Ledger (17): one ruled parenthetical edited on the charter's §3 word; the ledger's tradition is addenda. Nick's call.
5. Ledger (59)'s digest clause: IR-86 is OPEN (`grep -c 'bench=' nightly_digest.py` = 0), so it is written as a rule with the state disclosed and dated.
6. Pass-history entries in all three trees (W-SKILLS-9 wrote none; the W-SKILLS-8 form).
7. "Every file's frontmatter chain gains one segment" read as every TOUCHED file.
8. The Pi-clock sentence omits the mint's "UTC−4" (DST flips it).
9. A device disconnect ~12:5xZ interrupted the read-set before any write; resumed 13:01Z.

## §6 Not re-executed
The synced copies (Check 9). Exhibits beyond `git ls-files`, read only where a sentence depended on them: `nightly_digest.py`:170, `PersistenceObjectMapper.java`:106, D-v82-10/25, D-v83-21, D-v84-6/11/17/18, IR-76/86/89, the v84/v88 dispatch texts' close sentence, the v67 prompt §1b.
RETURNED nexsys-hivemind/context/audits/2026-09-30_W-SKILLS-10_return.md 8983

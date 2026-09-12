<!--
file: context/handoff/OPERATOR-BRIEF_for-Nick.md
purpose: Nick's operator brief in THE OPERATOR-LOAD LAW's shape: §NEXT carries exactly ONE act — one paste or one command card, what "done" looks like, the one line he says back; §HELD-BY-THE-HUB carries everything else and is EDITED (by row) every beat by the hub; §DONE is one line per act. STABLE PATH since v66 beat 10 (2026-09-07): one file, edited in place, git history is the past — the boot prompt names this path. Nick reads; he never remembers.
audience: Nick (§NEXT, then nothing until he reports) · the hub (edits §HELD every beat; hands the next act on each report)
state-type: operator queue (the file on disk is the copy-source of record, never a chat card)
status: LIVE — edited at v70 beat 7, THE CLOSE (Fri 2026-09-11 ~20:2x CT; instrument 2026-09-12T01:23:10Z). FIX-2a returned and audited ACCEPT; the close packet holds eight acts in order; §NEXT = act 1 (the core card). v71 boots from the stable prompt (act 8).
-->

# Operator brief (one act at a time)

## §NEXT — act 1 of the close packet: land FIX-2a (core). The packet holds every act in order.
**The packet (paste from it, not from chat):** `_scratch/v70/2026-09-12_v70_close_operator-packet.md` — act 1 the core card · 2 the CI watch · 3 the hivemind card (7 M + 8 A) · 4 the docs card · 5 the HERO-1b paste · 6 the EXPLAIN-114a paste on `ci` green · 7 R-4c Saturday · 8 v71's dispatch.
**Act 1 — core (Git Bash), scoped to lifecycle/lifecycle: 2 M + 4 A = 6:**
```bash
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core && M=$(git --no-optional-locks status --porcelain -- lifecycle/lifecycle | grep -c '^ M'); A=$(git --no-optional-locks status --porcelain -- lifecycle/lifecycle | grep -c '^??'); echo "M=$M A=$A main-touched=$(git --no-optional-locks status --porcelain | grep -c 'src/main')"; if [ "$M" = 2 ] && [ "$A" = 4 ] && ! grep -qi 'co-authored\|claude-session' ../_scratch/2026-09-11_core_FIX-2a_commit-msg.txt; then git add -A lifecycle/lifecycle && [ $(git --no-optional-locks diff --cached --name-status | wc -l) -eq 6 ] && git commit -q -F ../_scratch/2026-09-11_core_FIX-2a_commit-msg.txt && git log -1 --format='%h %s' | cut -c1-80 && git --no-optional-locks status --porcelain -- lifecycle/lifecycle | wc -l && git push 2>&1 | tail -1; else echo 'STOP: census or message check failed'; fi
```
**Done looks like:** `M=2 A=4 main-touched=0`, the `test(lifecycle): FIX-2a` subject, `0`, `1e26912..<sha>`. **One line back:** `CORE: FIX-2a <sha>`; then `CI: <sha> ci <green|red> frontend <…> install-smoke <…>` when the three runs settle (a red at `BusSoakIT`/`HeroLoop` → the run's reports under `_scratch/v70/ci-<sha>/`, the Act-0 shape; it is FIX-2b's first input, never a re-run). **Owed from tonight:** `H8A: RETURNED <path> <bytes>`.

## §HELD-BY-THE-HUB (edited every beat; you read it, you never remember it)
**Lanes (the cap: TWO + your hands; hardware exclusive):**
| Lane | State (v70 beat 7 — THE CLOSE, 01:23Z) | Next |
|---|---|---|
| **HONESTY-1 `94ae99d` · FE-NULL-1 `eabdbb1`** | LANDED Thu; ci + frontend GREEN; install-smoke per push (P4 MET); both instructions flipped to EXECUTED at this beat | closed; LASTREPORTED-1b rides R-4c (read `lastReported` on one never-reported entity after the `.deb`); O1 (the L1 headline per outcome) = the hero charter's first row |
| **HERO-1b — the hero build (web-ui; slot 2) — ISSUE-READY** | `context/instructions/2026-09-11_frontend-lane_HERO-1b_hero-build_B1-B7_charter.md` | **act 5** (after act 1; independent of CI) → `HERO1B: RETURNED <path> <bytes>` → the hub's audit (v71) → your `git add -A web-ui/dashboard` card → `frontend.yml` GREEN is the gate |
| **AMD-100 — "the hub" (docs)** | PROPOSED (`homesynapse-core-docs/design/amendments/AMD-100_Glossary_UI-term_the-hub.md`) | act 4 lands the proposal; `AMD100: ratify` executes the Glossary edit by a later card |
| **EXPLAIN-114a (Core Java; slot 1)** | ISSUE-READY; its §14 baseline amended at v70 b7 (FIX-2a's files and HERO-1b's dirt lawful) | **act 6, ONLY after `CI: <sha> ci green`** — the paste is in the packet; `EXPLAIN: RETURNED <path> <bytes>` or `EXPLAIN: hold` |
| **FIX-2a (Core Java; slot 1) — RETURNED, ACCEPT; LANDING** | `context/audits/2026-09-11_FIX-2a_return.md` (12,175 B) · the hub's audit `…_FIX-2a_intake_two-layer-audit_v70-b7.md`: 6 = 2 M + 4 A, test-only; the desk does not reproduce the class (143 loops, 0 anomalies); R1 + I3 ruled ACCEPT | act 1 (your core card) → `CI:` on that push = the gate of record + the bus class's sample #10 with the soak; FIX-2b on the first diagnostic-bearing red or TR-1b's reading |
| **H8-a (the rig; EXCLUSIVE) — record owed** | the paste handed 18:46 CT by the send; the rig from 19:00 | `H8A: RETURNED <path> <bytes>` → the intake is v71's first act (FE-113 → VERIFIED; OR-FAILCHAN on the stop readings; the capture for FE-113b) |
| **R-4c (the rig; MEASUREMENT-ONLY) — THE DELIVERABLE, ON DISK** | packet `context/instructions/2026-09-11_R-4c_measurement-only_zdo-surface-C-003_navigator-packet.md` (v70 b3) + the record scaffold `context/audits/2026-09-12_R-4c_measurement-only_operator-record.md` | **Sat 09-12** (`R4C: Sun` to move it): §N into a fresh window; `1e26912`'s install-smoke .deb; one window; the SNZB-02P by the ZDO surface = C-003 (the exit); `lastReported` twice; `card-gradle:`; the anomaly count; the restore; `R4C: RETURNED <path> <bytes>` when done |
| **P-1 (the power harness as a bench verb) — ISSUE-READY** | `context/instructions/2026-09-11_bench-lane_P-1_power-harness-primitive_charter.md`: dry-run only; the live leg gated on R-5 or `HARNESS-PLUG:` | your paste (its §7) after both core lanes are running; `P1: RETURNED <path> <bytes>` |
| **`PROTECT: no-force` (GitHub; your hands)** | your word (b2): core + docs only, the public repos; the six clicks handed in chat for both | `PROTECT: done` |
| **The skill mirror sync (Check 9)** | STALE: one file of 28 (`project-manager/SKILL.md`) | your usual sync, whenever; no lane waits on it |
| **Erik — the PALOKI search (wait-state)** | packet sent Thu ~12:00 CT | `ERIK: <his line>` when it comes; no public use before the opinion |
| TR-1 · Act 12 · HIVE-CLEAN-1 · W-SKILLS-8 · FE-113 · F-R4-1b · TR-0 · HERO-0 · RS-12-F · RS-13 | ACCEPT · RETIRED · landed ×8 | TR-1b after `card-gradle:` (Saturday) |

**v70's blocks (CLOSED at b7):** the boot (b1, `89de5b3`) → the red read (b2, `138e988`) → R-4c's packet (b3, the deliverable) → FIX-2a's instruction (b4) → HERO-1b's charter + AMD-100 (b5) → P-1's charter (b6) → FIX-2a returned, audited ACCEPT; the close (b7). One hivemind card lands b3–b7 (7 M + 8 A = 15). v71 opens on the intakes: CI on FIX-2a's push · `H8A:` · `HERO1B:`; then EXPLAIN's dispatch; R-4c Saturday; TR-1b on `card-gradle:`; W-SKILLS-9 later.

**Owed lines (none gates an act):** `card-gradle: <the first line of ./gradlew --version on the card | absent>` — Saturday, at the card (TR-1b's shape depends on it). *(`samples:` · `sample4:` · `act3:` · `nightly 09-05/09-06:` RETIRED by your `SAMPLES: passive`.)*

**Open words (asked only when they gate an act):**
- `H8: <day> <hh:mm>` — only to MOVE the default (Fri 09-11 19:00 CT); silence = it stands.
- `R4C: Sun` — only to move R-4c off Sat 09-12; silence = Saturday.
- `ERIK: <his line>` — when he replies (sight-read · date · surcharge); verbatim is fine, one line.
- `REVERT TR1-B2` · `REVERT EU-DEFER` — only if you refuse those rulings; silence = they stand. · `Activate: apply|hold` (09-15) — not yet due.

**Given (banked; no act):** `HERO1: Q1–Q7 a` · `EXPLAIN: three` · `PROTECT: core + docs` · your words on trailers and on hands (the hub never commits or pushes) · `DESIGN: start` · `PROTECT: no-force` · `SAMPLES: passive` · R-4c MEASUREMENT-ONLY · P-1 after R-4c · the H8-a fallback · `SEARCH-NAME: PALOKI` FINAL · the Erik packet SENT · `TR1-B2 = DRIVER` · `EU-DEFER` (provisional) · D4's seven recs STAND · Erik = U.S. only · `BEYOND-LETTERS: keep` · THE OPERATOR-LOAD LAW · D1–D7.

## §DONE — the ledger (one line per act; the past is this file's git history + the pm-handoff archive)
**v66–v68 (Sun 09-06 → Thu 09-10):** compressed in this file's history at `ea96351` (FE-113 · TR-0 · the H8-a packet · F-R4-1b · BLOCK 6 · HERO-0 · RS-12-F · D1–D7 · HIVE-CLEAN-1 · W-SKILLS-8 · TR-1 · NAMING-B · the Erik packet · RS-13 PALOKI · the momentum map · HONESTY-1 `94ae99d` · Dependabot `3f3f5cc` · FE-NULL-1 `eabdbb1`). **v69 (Thu 09-10 evening → Fri 09-11 ~17:2x CT):** the H8-a send armed; the map re-cut; your words on trailers and hands taken; beat 1 `19dd310`; PROTECT scoped; HERO-1 chartered, returned, audited ACCEPT, landed `1e26912`; beats 2–3 `d0bcc1e`; `HERO1:` (a) ×7 and `EXPLAIN: three` banked; EXPLAIN-114a authored; beat 4 `ea96351`; the `1e26912` red named. **v70 (Fri 09-11 ~17:5x CT →):** booted 22:47Z; your Act 0 verified at the bytes; the H8-a send moved to v70 (v69's deleted); the deliverable named: R-4c's packet (beat 1, landed `89de5b3`) → the red read at run 34650129654: no anomaly token; FIX-2 instrument-first; the audit filed (beat 2). → beat 2 landed `138e988`; R-4c's packet authored by range + its record scaffolded; six v68 blocks rotated (beat 3). → FIX-2a authored (test-only; the three instruments); its paste handed as the one act (beat 4). → HERO-1b chartered on the seven rulings; AMD-100 proposed in docs; the pastes queued (beat 5). → P-1 chartered (design + dry-run driver; live leg gated); the OR-BUS-SILENT-DROP row updated (beat 6). → FIX-2a returned (Fri ~19:5x CT) and audited ACCEPT; the desk does not reproduce the class; the eight-act close packet handed; v70 CLOSED at beat 7 (Fri ~20:2x CT).

## §WHAT YOU DO NOT DO
Open a second lane on the same core path-domain · take a sample's green as a GRANT · touch s31 or the nightly · `--allow-downgrades` · anything else while at the rig · grade a name in chat · paste a transcript (save it under `_scratch/`, tell me the path) · file or use PALOKI publicly before the written opinion (the .com is yours to buy at your own risk; the plan buys it the day the opinion is clean).

<!--
file: context/audits/2026-10-09_v102-b3_BENCH-142_intake_two-layer_audit.md
purpose: The hub's two-layer intake of BENCH-142's return (IR-142; `context/audits/2026-10-09_BENCH-142_return.md`, 8,134 B; RETURNED Fri 2026-10-09 17:33 CT, six minutes after dispatch): the return read critically, then the hub's own re-execution on the staged tree at the bytes; the deviations and findings ruled (IR-143 minted; the rider BENCH-142b ordered; F3 moot at `da9ca3d`); the landing gated AFTER BC9a and after the rider's intake. Filed v102 beat 3 (Fri 2026-10-09 ~18:1x CT; instrument 2026-10-09T23:19:44Z; D-v102-10/11/12).
audience: the hub (this close; v103's b1 — the rider's intake and the landing card) · Nick (the verdict; the two gates)
state-type: intake audit (two-layer)
status: FILED v102 beat 3 — VERDICT ACCEPT (BENCH-142 and its rider BENCH-142b); the landing card DISPATCH-READY, gated on `BC9a:` only
-->

# BENCH-142 — intake, two layers (v102 b3)

## §0 Verdict
**ACCEPT.** Five files staged on `bench-142/ir142-config-error-signature` over `cddac94` (HEAD unchanged; zero commits; no lock met); the four selftests green in the hub's own shell on the staged tree (47/0 · 42/0 · 54/0 · 27/0); the diff reads as chartered (the CLASS token `Configuration issue [ERROR]`; the twin `Configuration loaded:` + `issues=0`, absence PASS in a window and required within 90 s in boot-health; the fixtures in BOOT0's real format). One rider ordered BEFORE the landing (BENCH-142b — the `[FATAL]` tag, the return's F2) — **RETURNED 18:15 CT and INTAKEN ACCEPT in this same beat (§7)**. One register row minted (IR-143 — the return's F1). The landing card is cut and gated ONCE: AFTER `BC9a:` is said (BC9a's BP8 pulls `cddac94` as dry-run).

## §1 Layer 1 — the return read critically
- The form holds: §0 the card first (DELIVERED; the ten §0b rows re-run, each quoted and ticked; the four closing lines before and after; `diff --cached --stat`; the red texts quoted — T9a and A1-1 on the OLD dict `{'verdict': 'PASS', 'count': 0, …}`, i.e. the ERROR line unseen — IR-142's defect reproduced by the test before the fix; A1-1b `KeyError: 'loaded'`), §1–§6 as chartered; the last line `RETURNED context/audits/2026-10-09_BENCH-142_return.md 8134 bench-142/ir142-config-error-signature staged=5`. 8,134 B under the 8,192 ceiling. 0 trailer strings.
- The clock: 22:27:21Z → 22:33Z staged — six minutes of a two-hour budget; the premise table re-run first.
- Row 7's third hit at `:304` (the `availability` T-case, the same grep pattern): read — the exhibit's two halves (`:276`/`:277`) hold; [INFO] stands.
- The lane's own corpus greps (`0` · `1` on BOOT0) and lint (`listed 9 leg(s) — all load lawfully`) are claimed; re-executed below.

## §2 Layer 2 — the hub's re-execution at the bytes (Fri 2026-10-09 ~17:4x–17:5x CT, the device shell)
| Claim | The hub's instrument | Read | Holds |
|---|---|---|---|
| HEAD `cddac94`, the branch, 5 staged, 0 commits | `git log -1 --format=%h` · `rev-parse --abbrev-ref HEAD` · `status --porcelain` | `cddac94` · `bench-142/ir142-config-error-signature` · five ` M` rows (the five §3 paths) | ✓ |
| worktree = index | `git diff --stat \| wc -l` | `0` | ✓ |
| the four selftests on the staged tree | `python3 -B` ×4 | `verify72h selftest: 47 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 0 failure(s)` | ✓ |
| the corpus greps on BOOT0 | `grep -c 'Configuration issue \[ERROR\]'` · `grep -c 'Configuration loaded: .*issues=0'` on `_scratch/v98/bc8/bench-2026-10-07-212907.log` | `0` · `1` | ✓ |
| the token sweep | `grep -rn permit_join_key_ignored README.md scenarios tools/verify72h \| wc -l` · `grep -c … tools/bench.sh` | `0` (one binary match in a stale, gitignored `__pycache__/grader.cpython-310.pyc`, pre-lane — noise) · `1` (bench.sh:69 stays, as chartered) | ✓ |
| `constants.yaml` untouched | `md5sum \| cut -c1-12` | `9b0af47b3376` | ✓ |
| the lint | `python3 -B tools/runner/runner.py suite auto --list` | `[LOAD] boot-health tier=AUTO requires=-` · `listed 9 leg(s) — all load lawfully` | ✓ |
| the diff's substance | `git diff --cached -U1` on the three code files | `CONFIG_ERROR_TOKEN = "Configuration issue [ERROR]"` · `CONFIG_LOADED_TOKEN` · `CONFIG_LOADED_CLEAN = "issues=0"`; A1a cites `error_lines` and `loaded_all`, FAILs on either, `loaded` + `loaded_not_clean` in the dict; the report row re-cut; boot-health: BH-3b as the first positive with `same_line: ["issues=0"]` and `within: 90s`, BH-3's token re-pointed with its comment, the header's two Token sources; the fixtures `[main] WARN  c.h.c.StandardConfigurationService -- Configuration issue [ERROR] at '%s': '%s' is not defined in …` and `[main] INFO  … Configuration loaded: …` | ✓ |
| the trailer grep on the return | the two attribution strings of arc 7, `grep -c` | `0` | ✓ |
| the stray temp objects | `ls .git/objects/*/tmp_obj_* \| wc -l` | `5` — not locks; the staged blobs intact (the stat above) | ✓ (ruled §3) |

## §3 Deviations ruled
- [INFO] ×4 (row 7's third hit; BC9a's folder holds a dry-run transcript, not a kept log — correct, BC9a had not run; the module docstring at `:16` left; the stale `.pyc`) — noted, no act.
- [REVIEW] the five `tmp_obj_*` files under `.git/objects/{66,98,9c,ae,d3}/` — git's temporary object files left when `unlink` failed under the folder's no-delete rule; harmless to the index and to the commit; the hub's bridge shell cannot delete either. **Ruled: the landing card's FIRST line removes them in Nick's Git Bash** (`ls … | wc -l` → `5`; `rm -f`; `ls … | wc -l` → `0`) before the commit; named in the card.

## §4 Findings ruled (the hub's own reads at `da9ca3d`)
- **F1 → IR-143 (minted this beat).** `ConfigurationService.java:25–:28` read: "On startup … ERROR issues cause the offending key to revert to its JSON Schema default — the system starts with degraded but functional configuration." Stale against AMD-102 (`StandardConfigurationService` fails the load on FATAL or ERROR since `da9ca3d`). Javadoc only; a rider on the next Java unit (AVAIL-API-1) or on DEPRECATE-1 (IR-141) — never its own lane.
- **F2 → BENCH-142b, the rider, ordered BEFORE the landing.** `JsonSchemaCompositeValidator.classify` at `da9ca3d` (`:135–:137`): `additionalProperties → ERROR`, `required → FATAL`, `default → ERROR`. A FATAL issue prints `Configuration issue [FATAL] at '<path>': …` by the same `log.warn` at `:824` and fails the boot the same way; neither BH-3 nor A1a's token sees it. The rider adds the `[FATAL]` token to both reads (`CONFIG_ERROR_TOKENS`; BH-3c), one test (A1-1c), the two READMEs' rows; the staged set stays five; the return gains §7 and a new RETURNED line (the file's ceiling raised to 10,240 B for the rider). Handed to the warm lane at ~17:5x CT.
- **F3 → moot at `da9ca3d`, by construction.** `classify` returns only ERROR or FATAL; the WARNING tier has no producer (IR-141) and there is no INFO severity in `ConfigIssue.Severity` (FATAL · ERROR · WARNING). A boot that prints `Configuration loaded: … issues=N>0` therefore cannot succeed at this sha — the twin's FAIL on a present, unclean loaded line is consistent with AMD-102 R-E. Recorded so a future producer of WARNING is read against this note first.

## §5 The landing — gated twice
- **Gate 1 — AFTER `BC9a:` is said.** BC9a's card (cut and dry-run on `37f05a9` with `BP8 cddac94`) pulls the bench by `git pull` and checks `after:` = the STATE line's sha; landing BENCH-142 on `main` before the rig would change the rig's premise without a dry-run (refused by the v102 text's own rule). The Pi needs BENCH-142 only before dry-run #2 (Oct 22–23).
- **Gate 2 — the hub's intake of BENCH-142b — MET at 18:1x CT (§7).**
- The card: `_scratch/v102/b3/card_bench_land.txt` (AVAIL-LINE-1's landing form + the `tmp_obj` sweep as its first line — ten stragglers after the rider's second `git add`); the message `_scratch/v102/b3/2026-10-09_bench_BENCH-142_commit-msg.txt`; `BENCH: LANDED <sha>` — tonight after BC9a if Nick sits, else Saturday morning before BC9; then BENCH-PULL-9 rides BC9's card (its STATE line names the sha).

## §6 Not re-executed; disclosed
The lane's red observations (its red texts are quoted; the hub saw only the green). The Pi (nothing tonight; BP8 is BC9a's).

## §7 BENCH-142b — the rider's intake (18:1x CT; two layers)
- Layer 1: the return's §7 (10,101 B whole, under the 10,240 B ceiling; the new RETURNED line `… 10101 … staged=5`): the premise re-read (`classify :134–:140`, `:137 KEYWORD_REQUIRED -> Severity.FATAL`); RED `48 check(s), 1 failure(s)` — A1-1c on the old dict (the FATAL line unseen); GREEN 48/0 · 42/0 · 54/0 · 27/0; the sweep 0; the md5; the lint; BC8's corpus `[FATAL]` → 0; `5 files changed, 155 insertions(+), 31 deletions(-)`. One disclosed change beyond the rider's list: A1-1's pinned report text followed spec (2) — `[ERROR]` → `[ERROR]/[FATAL]` — read when it went red, then re-cut, not weakened. Two line spans corrected to the real numbers (`:242–:243`; `:978–:979`).
- Layer 2 (the hub's shell on the staged tree): `verify72h selftest: 48 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 0 failure(s)`; worktree = index (`diff --stat` 0); HEAD `cddac94`, the branch, five ` M` rows; `grader.py:242` `CONFIG_ERROR_TOKENS = ("Configuration issue [ERROR]", …` and `:979` `if any(t in l.get("text", "") for t in CONFIG_ERROR_TOKENS)]`; the `+` hunks carry BH-3c (`- log: "Configuration issue [FATAL]"`), the Token sources line, the READMEs' `[ERROR]`/`[FATAL]`, A1-1c's check and the re-cut pin `"1 Configuration issue [ERROR]/[FATAL] line(s) (pre-registered 0)"`; `grep -c '[FATAL]'` on BOOT0 → 0; the token sweep → 0; `constants.yaml` `9b0af47b3376`; the lint `listed 9 leg(s) — all load lawfully`; 0 trailer strings; ten `tmp_obj_*` files (the card's first line).
- **Verdict: ACCEPT.** F2 closed. The landing's gate 2 is met; the card waits on `BC9a:` alone.

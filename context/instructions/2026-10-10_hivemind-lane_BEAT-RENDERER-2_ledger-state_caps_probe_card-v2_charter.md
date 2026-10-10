<!--
file: context/instructions/2026-10-10_hivemind-lane_BEAT-RENDERER-2_ledger-state_caps_probe_card-v2_charter.md
purpose: BEAT-RENDERER-2. It makes `context/status/state.yaml` the SOURCE of the brief's volatile regions (the §HELD lanes table, the closed-windows line, the open and given words, the status line), puts every cap and assert in the renderer BEFORE any byte (`--probe`), makes `--selftest` safe on a cp1252 console, and ships the GATED operator card as a library function (`card_v2()` in `splice_lib_v4.py`, closing IR-101's library row). Cut from IR-140's row and D-v102-20 (pulled forward; Saturday under the cap).
audience: the BEAT-RENDERER-2 lane (Claude Code on Nick's desk, in its OWN git worktree) · the v103 hub (intakes two layers; cuts the landing)
state-type: lane charter (hivemind; ≤ 3 h)
status: HANDED for dispatch at v104 beat 2 (Sat 2026-10-10 ~14:4x CT) on `RENDERER-2: today` (Nick 14:39), at hivemind `8ab4789`, with one named deviation (the fixture named `v104b1_…`); DISPATCHED at Nick's paste; its check-in at v105 or during dry-run #1 (Nick's word). Was: DISPATCH-READY — cut v103 beat 3; FILED at the close (Sat 2026-10-10 ~09:0x CT; D-v103-26). Its premise values, re-read at the close, equal the table (v2 `99e87f2dbafa` · v3 `fc79eee9d1af` · `render_state.py` `72372aa8bfb3` · `test_render_state.py` `9774347342bc` · `state.yaml` `0812b89782f3`); the close touches none of them. Dispatched by v104 on `RENDERER-2: today`; flips to DISPATCHED on Nick's paste, EXECUTED at the hub's intake.
-->

# BEAT-RENDERER-2 — the brief's ledger from `state.yaml`; the caps and asserts in the renderer; `card_v2()`

## §0 The lane contract (read whole before any command; every line binds)
- **Your own worktree.** The hub writes the hivemind's main working tree all day, so you never touch it. `date -u` FIRST (CT = UTC − 5); every stamp from it. From `~/Desktop/Code/ClaudeFolder/nexsys-hivemind`, your first act is `git worktree add ../nexsys-hivemind-br2 -b beat-renderer-2/ledger <the sha in your dispatch line>`. After that you work ONLY inside `../nexsys-hivemind-br2`. Its porcelain is empty at your start.
- **You STAGE and never commit.** Run `git add -- <the §3 paths>` inside your worktree. No commit, no push, no merge, no `git switch` in the main tree. THE LANE STOPS AT A LOCK: a `.git/*.lock` or `.git/worktrees/*/index.lock` you meet is a STOP and a line in the return, never a sweep. Nothing on the Pi; no ssh.
- **The premise table (§0b) is re-run FIRST, inside your worktree,** and pasted at the top of the return. A failed row STOPS the lane before any write (BLOCKED).
- **The live spine is never written.** Your worktree holds copies of `pm-handoff.md`, `PROJECT_SNAPSHOT.md`, `OPERATOR-BRIEF_for-Nick.md` and the chain archive at your start sha. You READ them, and `--write` and `card_v2()` run ONLY on further copies under a temp dir. Your close's porcelain shows §3's paths and nothing else.
- **Tests first, with red observed:** the new checks fail before the code exists, then pass. Python ≥ 3.10, the standard library plus `yaml.safe_load` (PyYAML 6.0.3 is on your desk). `import sys; sys.dont_write_bytecode = True` is the FIRST statement of every script.
- **Every `python3` you run on the desk runs as `PYTHONIOENCODING=utf-8 python3 …`** (IR-146), except the one cp1252 check in §1 U1(e), which proves the script no longer needs it.
- **≤ 3 h.** U1 first and whole; U2 only if the hour allows. A unit not reached is a `[REVIEW]` row in the return's §3, never a rushed one.
- **THE RETURN:** `context/audits/<CT-date>_BEAT-RENDERER-2_return.md`, written INSIDE your worktree and staged with the rest, ≤ 8,192 B (a ceiling, not a target).
  - §0 the card: DELIVERED/BLOCKED · each test command's closing line · `git --no-optional-locks diff --cached --stat` · the red texts quoted · §0b re-run, one line per row.
  - §1 what changed, file by file.
  - §2 the tests.
  - §3 deviations ([INFO]/[REVIEW]/[BLOCKING]).
  - §4 findings for the register.
  - §5 how the hub uses it at a beat (the commands, in order).
  - §6 instrument limits.
  - The last line of the file: `RETURNED <path> <bytes> beat-renderer-2/ledger staged=<n>`.
- No attribution text anywhere. `{{NAME}}` where a product name would go (none is expected). The slot syntax is the library's `fill()` form: the field name between two pairs of at-signs, never double braces.

### §0b The premise table (the hub's reads at its tree after v103 b2; re-run each in your worktree, paste the output line)
| # | Command (from your worktree) | Expected |
|---|---|---|
| 1 | `git --no-optional-locks log -1 --format=%h && git --no-optional-locks status --porcelain \| wc -l && git --no-optional-locks rev-parse --abbrev-ref HEAD` | the sha in your dispatch line · `0` · `beat-renderer-2/ledger` |
| 2 | `md5sum context/process/splice_lib_v2.py context/process/splice_lib_v3.py \| cut -c1-12` | `99e87f2dbafa` · `fc79eee9d1af`. Neither is edited, ever (callers pin them) |
| 3 | `md5sum context/process/render_state.py context/process/test_render_state.py context/status/state.yaml \| cut -c1-12` | `72372aa8bfb3` · `9774347342bc` · `0812b89782f3` |
| 4 | `PYTHONIOENCODING=utf-8 python3 -B context/process/render_state.py --check 2>&1 \| cut -c1-40` | `DIFF` ×4 (snapshot-digest · snapshot-file · brief-digest · brief-file) + `INFO unused keys: words.given words.open`. State.yaml is still v100 b3's fixture; that is this lane's premise (IR-140) |
| 5 | `grep -n '^## §' context/handoff/OPERATOR-BRIEF_for-Nick.md \| cut -c1-24 && grep -c '^| \*\*' context/handoff/OPERATOR-BRIEF_for-Nick.md` | five headings in order: §DIGEST · §NEXT · §HELD-BY-THE-HUB · §DONE · §WHAT YOU DO NOT DO · the lanes-table rows: `9` |
| 6 | `python3 --version && python3 -c "import yaml; print(yaml.__version__)"` | `Python 3.10+` · `6.0.3` |
| 7 | `git ls-files \| grep -c 'splice_lib_v4\|test_splice_lib_v4\|brief_held\|brief_words\|brief_status\|fixtures/v103'` | `0` (every name §3 mints is unused) |

## §1 What this implements
**The design problem.** Every hub beat re-cuts the brief's volatile regions by hand. That means four lane rows, the closed-windows line, the open words, the given words and the status line: ≈ 8–12 anchored replacements per beat, each a chance to drop a word or an id. v103 b1–b2 spent most of their splice lines on them. The state file (BEAT-RENDERER-1) covers only the two digests, and it is stale, because nothing made it the source. The fix: the ledger lives in `state.yaml` as rows and lists, the renderer generates the regions, and every cap and assert runs on the rendered strings before any byte.

**U1 — the ledger as state; caps and asserts first (the gate).**
- (a) **`state.yaml` v2, by hand from your start sha's live text,** keeping v1's keys and adding:
  - `held:` — the lanes table, one row per `| **…` line, as `{lane: "…", state: "…", next: "…"}`, the three cells verbatim;
  - `closed_windows:` — the one line, verbatim;
  - `words.open:` and `words.given:` — the two lines split on ` · ` into lists, the leading bold label in the template;
  - `status:` — the brief's frontmatter `status:` line after `status: `, verbatim.
  - **Re-derive every v1 key too, so all regions MATCH at your start sha.** This is IR-140's other half: v1's values are v100 b3's.
- (b) **Templates** `context/process/templates/brief_held.tpl.md` (the table header, the rows, the closed-windows line), `brief_words.tpl.md` (the two words lines) and `brief_status.tpl.md` (the status line). Each region is bounded by anchors the renderer asserts exist exactly once.
- (c) **`render_state.py`** renders and writes the new regions beside the two digests, keeping the same `--check` / `--write` contract. `--check` prints one MATCH/DIFF line per region (now six or more) and exits 1 on any DIFF.
- (d) **Every cap in the renderer, refused before a byte:** the snapshot file ≤ `SNAP_CAP`, the brief file ≤ `BRIEF_CAP` (both IMPORTED from `splice_lib_v2`, never retyped), each digest ≤ 2,048, and the §HELD region ≤ 6,144 (named once). A breach prints the region and its bytes and exits 1 with nothing written. Also **`--probe`**: render every region, run every assert that `--write` would run after writing (each anchor exactly once; each cap; the rendered region found in the would-be file exactly once), print the would-be bytes per region, and write NOTHING. This moves v101's post-write asserts into the probe (IR-140, v101 b6).
- (e) **`_utf8_stdout()`:** `render_state.py` reconfigures stdout and stderr to UTF-8 at entry, so `--selftest` passes under `PYTHONIOENCODING=cp1252` (the v101 b6 crash on `≤`; IR-146's class). A test spawns the selftest under cp1252 and asserts exit 0.
- (f) **The regression fixture** `context/process/fixtures/v103b2_state.yaml` + the expected regions at your start sha, with `test_render_state.py` extended by at least six checks: each new region byte-equal; an over-cap state refused with nothing written (the live copies' md5s unchanged); `--probe` writes nothing; the cp1252 selftest; an unfilled slot refused; a `held` row with a ` | ` inside a cell refused (a table cell may not carry the pipe).

**U2 — `card_v2()` in `context/process/splice_lib_v4.py` (a NEW file; v2 and v3 untouched).** v4 is v3's text byte for byte plus `card_v2(repo_key, paths, n, msg_rel, head_sha, say_back)`. It emits the gated card the hub has hand-written since v103 b2 (pm-lessons 2026-09-29):
- `T=$(grep -c 'Co-Authored\|Claude-Session' $M)` computed once;
- an echo line of head · branch · porcelain · locks · trailers;
- then `[ head = <sha> ] && [ branch = main ] && [ ! -e .git/index.lock ] && [ "$T" -eq 0 ] && git add -- <paths> && N=… ; echo "staged: $N (expect n)" && [ "$N" -eq n ] && git commit -F $M && git push && git log -1 --oneline`;
- no `;` before a commit or a push, and the grep string exactly once.

`context/process/test_splice_lib_v4.py` builds a throwaway repo with a bare origin under a temp dir and runs the emitted command with bash. Five cases: n paths → one commit, pushed; n+1 → no commit; a trailer in the message → no commit; a stale `.git/index.lock` → no commit; the wrong HEAD → no commit. Closing line: `splice_lib_v4 selftest: 5 check(s), 0 failure(s)`. v4's md5 is named in the return; its callers pin it.

## §2 Files to read before starting (by range)
- `context/process/render_state.py` whole (9.9 KB) and `context/process/test_render_state.py` whole.
- `context/status/state.yaml` whole (5.7 KB; its header comment is the form law).
- `context/process/templates/*.tpl.md` (both).
- `context/process/splice_lib_v2.py` `:19` (the caps), `:68` (`fill()`), `:108–:118` (`card()`, the form `card_v2()` replaces).
- `context/handoff/OPERATOR-BRIEF_for-Nick.md` whole (≈ 10.7 KB): the regions you make generated.
- `context/status/PROJECT_SNAPSHOT.md` whole.
- `context/lessons/pm-lessons.md`: the entry headed `2026-09-29 — A CARD'S COMMIT IS GATED ON ITS CENSUS` (grep it).
- `context/planning/improvement-register.md`: the rows IR-101 · IR-140 · IR-146 (grep `^| IR-1\(01\|40\|46\) |`).
- `../_scratch/v103/b2/v103b2_splice_1.py` (the hub's newest beat script; its brief block is what U1 generates, and its `gated_card()` is the exemplar `card_v2()` generalizes).

## §3 Files to create or modify (this table is the plan; nothing else is written)
| Path | A/M | What |
|---|---|---|
| `context/status/state.yaml` | M | v2: the v1 keys re-derived to the start sha's live text + `held`, `closed_windows`, `words.open`, `words.given`, `status` |
| `context/process/render_state.py` | M | the new regions; `--probe`; the caps refused first; `_utf8_stdout()` |
| `context/process/templates/brief_held.tpl.md` · `brief_words.tpl.md` · `brief_status.tpl.md` | A ×3 | the new regions' skeletons |
| `context/process/test_render_state.py` | M | ≥ 6 new checks (§1 U1(f)) |
| `context/process/fixtures/v103b2_state.yaml` · `v103b2_*.expected.md` | A | the regression fixture at your start sha (one expected file per region) |
| `context/process/splice_lib_v4.py` · `test_splice_lib_v4.py` | A · A | U2 |
| `context/audits/<CT-date>_BEAT-RENDERER-2_return.md` | A | the return |

`splice_lib_v2.py`, `splice_lib_v3.py`, the four live spine files, the register and the skills are not touched.

## §4 What to watch out for
- **The brief's lanes table carries backticks, bold markers, `·` separators and `≈`/`→` characters in every cell.** Store each cell verbatim; the renderer adds only the leading `| `, the ` | ` separators and the trailing ` |`. A UTF-8 byte comparison is the only MATCH.
- **The words lines end with a period after the last item.** The template carries it; the list does not.
- **`fill()` refuses an unfilled `@@slot@@`.** A cell that legitimately contains two at-signs would need escaping; none does at the start sha (grep it, and say so in the return).
- **Windows:** `\r\n` must never enter a rendered file (`newline="\n"` on every write, as the library's `wr()`). The bare-origin test repo needs `git init --bare -b main` (or `symbolic-ref`) so the push in U2's first case has an upstream; set `push.default` or push `origin main` explicitly in the test, not in the card.

## §5 Out of scope
- The pm-handoff beat block and the chain (v3's `beat()` stands).
- The §NEXT and §DONE regions (hand-cut).
- The card dry-run tool (D-v94-16).
- Any change to v2/v3; any write to the live spine; the register's rows (the hub's at the intake).

## §6 Success criterion (binary)
- **U1:**
  - `PYTHONIOENCODING=utf-8 python3 -B context/process/render_state.py --check` prints MATCH for every region against the copies at your start sha (exit 0).
  - `--probe` writes nothing (md5s before = after).
  - `PYTHONIOENCODING=cp1252 python3 -B context/process/render_state.py --selftest` exits 0.
  - `python3 -B context/process/test_render_state.py`: all checks green, ≥ 6 new ones observed red first.
- **U2 (if reached):** `python3 -B context/process/test_splice_lib_v4.py` closes `5 check(s), 0 failure(s)`; v2's and v3's md5s unchanged.
- **Both:**
  - `git --no-optional-locks diff --cached --stat` shows only §3's paths; zero commits; no `__pycache__`.
  - The return under its cap, with §0b re-run and the red texts quoted.
  - `RETURNED … staged=<n>` its last line.

## §7 The dispatch (Nick pastes into Claude Code in `~/Desktop/Code/ClaudeFolder/nexsys-hivemind`; ≤ 3 h; the hub fills `<sha>` from the hivemind HEAD at the hand-off)
```
You are the BEAT-RENDERER-2 hivemind lane on my desk, at hivemind HEAD <sha>. Read context/instructions/2026-10-10_hivemind-lane_BEAT-RENDERER-2_ledger-state_caps_probe_card-v2_charter.md WHOLE, then its §2 set by range. Execute §0 exactly: date -u first; your own worktree (git worktree add ../nexsys-hivemind-br2 -b beat-renderer-2/ledger <sha>) and nothing written outside it; §0b's seven rows re-run and pasted (a failed row = BLOCKED, no write); U1 first — state.yaml v2 by hand, the templates, the renderer's regions, --probe, the caps, the utf-8 stdout, the fixture, --check MATCH at the bytes; U2 (card_v2 in splice_lib_v4.py) only if the hour allows; tests red first; every python3 under PYTHONIOENCODING=utf-8 except the cp1252 check; the live spine never written; STAGE, never commit; the return in your worktree with RETURNED as its last line.
```
Say back to the hub: `BEAT-RENDERER-2: RETURNED <path> <bytes> staged=<n>`. The hub intakes two layers: it re-runs `--check`, `--probe`, the cp1252 selftest and both test files on the staged tree, reads the diff and greps the trailer. Then it cuts the landing card (commit in the worktree, then merge into `main` at a beat boundary) and adopts the renderer at the beat after: re-derive `state.yaml` to the then-live text, `--check` MATCH, then edit state and `--write`.

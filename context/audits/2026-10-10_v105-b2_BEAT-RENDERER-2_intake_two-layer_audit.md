<!--
file: context/audits/2026-10-10_v105-b2_BEAT-RENDERER-2_intake_two-layer_audit.md
purpose: BEAT-RENDERER-2's intake, two layers — the lane's return and transcript read critically, then the hub's own re-execution of every §6 gate on a scratch copy of the worktree under Python 3.10.12 + PyYAML 6.0.3, the staged set read from the worktree's index, F2 confirmed at the hub's head, the merge's cleanliness; the verdict LANDING-READY and the landing's form.
audience: the hub · Nick · the next hub
state-type: intake audit
status: FILED — v105 beat 2 (Sat 2026-10-10 ~17:3x CT; instrument 2026-10-10T22:35:26Z)
-->
# BEAT-RENDERER-2 — intake audit (two layers)

**The lane:** `../nexsys-hivemind-br2`, branch `beat-renderer-2/ledger` over `8ab4789`; charter D-v104-15..21 (`RENDERER-2: today` + four rows), ruled twice at its ask (D-v104-23). **The return:** `context/audits/2026-10-10_BEAT-RENDERER-2_return.md` in the worktree, 7,936 B, `status: RETURNED` (start 19:44:33Z, close 20:55:53Z = 15:55 CT; 1 h 12 min of the 3-h cap), last line `RETURNED context/audits/2026-10-10_BEAT-RENDERER-2_return.md 7936 beat-renderer-2/ledger staged=17`. **The transcript:** filed by the hub before this read, `_scratch/v105/b2/BEAT-RENDERER-2_lane-transcript_verbatim.txt` (14,090 B, md5 `e78540346b6fe24a42bb65d5d39f8a58`).

## §1 Layer 1 — the claims, read critically
- **U1 (the renderer):** five regions (`snapshot-digest` · `brief-status` · `brief-digest` · `brief-held` · `brief-words`); every cap before a byte; `--probe` first; `--state`; refusals by name (an unread key, a key twice, a merge key, an empty mapping, a list key scalar or empty, a `|` in a cell); `_utf8_stdout()`; `render()`/`splice()` keep v1's interface for v3's `beat()`. `state.yaml` v2 by hand from the live text at `8ab4789`: 33 keys, 10 held rows; the fixture `v104b1_*` = the live regions.
- **U2 (the lib):** `splice_lib_v4.py` = a v4 header + v3 VERBATIM + `card_v2()` (`unset M T N &&` first; `--no-renames`; one relative path per file); md5 `bc10cd3f5f142e52f64a84c477fcbbee`.
- **The gates claimed:** `--check` 7 MATCH exit 0 · `--probe` nothing written · cp1252 `--selftest` 5/0 · `test_render_state.py` 32/0 (13 carried + 19 new; the new ones red first) · `test_splice_lib_v4.py` 5/0 · WSL Python 3.10.12 repeats every line.
- **Deviations D1–D7:** D2 and D3 carry Nick's rulings quoted; D5 changes the card the hub pastes; D7 — two adversarial review rounds, one BLOCKING fixed (fixture checks tied to the live spine's byte sizes → frozen copies).
- **Findings F1–F6:** F1 the hub's `gated_card()` stale-variable gap · F2 the live digest has a Pi clause the template cannot express → `--write` once at adoption · F3 `beat()` renders only the digests → `--write` before `beat()` · F4 the count gate vs a set gate (a ruling) · F5 `test_splice_lib_v3.py` 3/5 red, pre-existing · F6 `v99b1_*` unused.
- **Read against the charter:** the four rows ruled at v104 b2 are honored (the fixture `v104b1`; the templates re-cut on the ruling; slotless keys dropped and refused; v99b1 untouched). The transcript's progress lines agree with the return (the 20:16Z status: U1 and U2 green at 32 min; the review rounds after).

## §2 Layer 2 — the hub's re-execution
All on a scratch COPY of the worktree (`_scratch/v105/b2/br2_copy/`: `context/process/`, `context/status/`, the two spine files — 54 files), never in the worktree; the VM shell's Python is **3.10.12 with PyYAML 6.0.3** — the charter's own target, which the desk lacks (D3) and the lane reached only on WSL.
| Gate | The lane said | The hub ran |
|---|---|---|
| `render_state.py --check` | 7 MATCH, exit 0 | 7 MATCH (`snapshot-digest 1776 ≤ 2048` · `snapshot-file 3461 ≤ 3500` · `brief-status 262` · `brief-digest 1230 ≤ 2048` · `brief-held 3841 ≤ 6144` · `brief-words 2031` · `brief-file 11851 ≤ 12288`), exit 0 |
| `--probe` | `PROBE OK — nothing written`; md5s equal | PROBE ×7 then `PROBE OK — nothing written`, exit 0; the snapshot `afe30075…` and the brief `1e57ade1…` unchanged before and after |
| `PYTHONIOENCODING=cp1252 … --selftest` | 5/0, exit 0 | `render_state selftest: 5 check(s), 0 failure(s)`, exit 0 |
| `test_render_state.py` | 32/0 | `render_state tests: 32 check(s), 0 failure(s)`, exit 0 (the last two: the caps imported once; no `__pycache__`) |
| `test_splice_lib_v4.py` | 5/0 | 5/0 on the VM's bash — cases 1–5 `ok`; case 5's control commits without `unset` |
| v4 pure addition | v3 verbatim inside | `v3 in v4` True; v3 18,529 B, v4 24,350 B; v4 md5 `bc10cd3f5f142e52f64a84c477fcbbee` |
| the staged set | `staged=17` | the worktree's index read with `GIT_INDEX_FILE=…/.git/worktrees/nexsys-hivemind-br2/index --git-dir=…/.git --no-optional-locks diff --cached --name-status --no-renames 8ab4789`: **17 = 12 A + 5 M**; `17 files changed, 1258 insertions(+), 197 deletions(-)` (the return's 16/1209 + the return file); every staged blob's hash = the worktree file's `hash-object` (no unstaged edit) |
| F2 at the hub's head | a DIFF expected | the live spine at `ffafe02` under `--check` → **DIFF ×7** (`snapshot-digest` at byte 18 … `brief-words` at byte 51): the regions the hub hand-cut at v104 b2–b4 and v105 b1 |
| the merge | — | `git log 8ab4789..ffafe02 -- context/process context/status/state.yaml` empty; `8ab4789` is an ancestor of `ffafe02`: no overlapping path, the merge is clean |

**Not re-executed (disclosed):** the Windows Git Bash runs the lane reports (the U2 cases and the cp1252 line on the desk); the lane's "no `__pycache__` on the desk" (the copy has none); the review rounds themselves (their outcome is in the tree the gates ran on).

## §3 The verdict and the landing
**LANDING-READY.** The landing is one card in Nick's hands (D-v105-11): the lane's 17 staged paths committed on `beat-renderer-2/ledger` in the worktree, under the SET gate on the 17 names; `git merge --no-ff` into `main` with its message file (BR1's form, `9649d3c`); the merge's first-parent diff asserted at 17 names before the push. **Adopted now (D-v105-12):** the card form opens `unset M T N S &&`, counts with `--no-renames`, and gates on the SET (`git diff --cached --name-only --no-renames` sorted under `LC_ALL=C`, md5 against the splice's expected set). **Adopted at the v105 close (D-v105-13; IR-150):** `state.yaml` re-derived from the then-live text → `--probe` → `--write` → `--check` 7 MATCH; the card pinned to v4; F5 and F6 ride that beat. **The register:** IR-149..153 (D-v105-14).

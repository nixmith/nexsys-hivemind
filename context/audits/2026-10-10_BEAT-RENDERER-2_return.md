<!--
file: context/audits/2026-10-10_BEAT-RENDERER-2_return.md
purpose: BEAT-RENDERER-2's return — U1 + U2 DELIVERED in the worktree; STAGED, never committed.
audience: the hub (two-layer intake at the bytes) · Nick (the landing card)
state-type: lane return
status: RETURNED — Sat 2026-10-10 ~15:5x CT (start 2026-10-10T19:44:33Z · close 2026-10-10T20:55:53Z)
-->
# BEAT-RENDERER-2 — return (U1 + U2)

## §0 The card — DELIVERED
- **Where:** `../nexsys-hivemind-br2` · `beat-renderer-2/ledger` · base `8ab4789` · zero commits · staged=17 · the hub's tree untouched.
- **Closing lines** (`PYTHONIOENCODING=utf-8 python3 -B context/process/…`): `render_state.py --check` → MATCH ×7 (`brief-held 3841 ≤ 6144` · `brief-file 11851 ≤ 12288` · `snapshot-file 3461 ≤ 3500` · digests 1776 · 1230 ≤ 2048), exit 0 · `--probe` → `PROBE OK — nothing written`, md5s before = after · `PYTHONIOENCODING=cp1252 … --selftest` → `render_state selftest: 5 check(s), 0 failure(s)`, exit 0 · `test_render_state.py` → `render_state tests: 32 check(s), 0 failure(s)` · `test_splice_lib_v4.py` → `splice_lib_v4 selftest: 5 check(s), 0 failure(s)` · `test_splice_lib_v3.py` → `5 check(s), 3 failure(s)`, byte-identical to its run before any edit (F5).
- **Python 3.10:** `py -3.10` → `No suitable Python runtime found`; WSL `Ubuntu` (3.10.12 · PyYAML 5.4.1 · git 2.34.1) on a copy of the tree repeats every line above.
- **RED first:** before the code `26 check(s), 24 failure(s)`, all 13 first NEW red (`no attribute 'render_all'` · `usage: render_state.py [-h] (--selftest | --check | --write)` · cp1252 `UnicodeEncodeError: 'charmap' codec can't encode character '\u2264'`); the review's refusals, each on a renderer without it → `30 check(s), 3 failure(s)` (`not refused (expected "the key 'next' written twice in one mapping")`), then `32 check(s), 2 failure(s)`; v4's test before v4 → `FileNotFoundError: … splice_lib_v4.py`.
- **`diff --cached --stat`** (before this return): `16 files changed, 1209 insertions(+), 197 deletions(-)` — state +179 −72 · renderer +188 −78 · its test +154 −42 · templates +1 −1 · +3 −4 · +1 · +6 · +4 · fixtures +193 · +5 · +1 · +4 · +15 · +4 · v4 +280 · its test +171.
- **§0b re-run** (19:44:33Z): 1 `8ab4789` · `0` · `beat-renderer-2/ledger` ✓ · 2 `99e87f2dbafa` · `fc79eee9d1af` ✓ · 3 `72372aa8bfb3` · `9774347342bc` · `0812b89782f3` ✓ · 4 DIFF ×4 + `INFO unused keys: words.given words.open` ✓ · 5 the five headings · `9` ✓ · 6 `Python 3.12.4` · `6.0.2` ✗ → ruled (D3) · 7 `0` ✓ (`fixtures/v104` `0`).

## §1 What changed
- `state.yaml` v2, by hand from the live text: v1's keys re-derived; NEW `held` (10 rows) · `held_as_of` · `closed_windows` · `words.open/given` · `status` · `pi.host/since/notes` · `shas.bench_note/hivemind_note` · `open_irs` · `brief.pi_note`; DROPPED (no slot): `counter` · `pi.carries/target_by/target` · `fleet.note` · `lanes` · `lanes_note` · `week` · `dates` · `brief.core_note/fleet_note/after_state/tonight`.
- `render_state.py`: five `REGIONS` · every cap before a byte (`HELD_CAP = 6144` once; file caps imported) · `--probe` = v101's post-write asserts, run first · `--state` · `REFUSED <why> — nothing written`, exit 1 · refused by name: an unread key, a key twice, a merge key, an empty mapping, a list key scalar or empty · `_utf8_stdout()` · `render()`/`splice()` keep v1's interface for v3's `beat()`.
- Templates: two re-cut (D2), three NEW. Fixture: `v104b1_state.yaml` (= `state.yaml`'s bytes) + five `v104b1_*.expected.md` (the live regions at `8ab4789`).
- `splice_lib_v4.py` (md5 `bc10cd3f5f142e52f64a84c477fcbbee`) = a v4 header + v3 VERBATIM + `card_v2()`: pure addition.

## §2 The tests
`test_render_state.py` 32 = 13 carried (re-pointed at v104b1) + 19 NEW: the new regions, caps and refusals, `--probe` writes nothing, the `--check`/`--selftest` DIFF paths, cp1252, and `render()`/`splice()` + v4's `render_regions()` (the `beat()` path). Fixture-state checks run on FROZEN copies built from the expected regions (pads sized from the would-be bytes), so the hub's moving spine cannot redden them; six mutations each killed. `test_splice_lib_v4.py`: preconditions + five cases in throwaway repos with a bare origin: a move among the n paths · the count both ways · trailer · stale lock · wrong HEAD in a poisoned shell (its control commits without `unset`) and the right sha off `main`.

## §3 Deviations
- **D1 [INFO]** the fixture is `v104b1` (the dispatch).
- **D2 [REVIEW]** the two v1 templates re-cut (12/25 and 8/16 literal fragments absent from the live digests). Ruled (v104, Nick): "re-cut both templates, with three conditions. (1) §3 gains … snapshot_digest.tpl.md · brief_digest.tpl.md | M ×2 … (2) v1 keys with no slot are DROPPED … the renderer also refuses, by name, any state.yaml key that no template reads … (3) Stable labels stay literal and the shas stay fields … MATCH stays byte-equal at 8ab4789, with every cap unchanged. The v99b1 fixture is not touched."
- **D3 [REVIEW]** §0b row 6: PyYAML 6.0.2 here, 6.0.3 on the hub's shell. Ruled PROCEED; row 6 = "Python ≥ 3.10 and PyYAML ≥ 6.0 with safe_load"; 3.10-only code.
- **D4 [INFO]** 10 table rows (9 `| **` + `The landed lanes`); the header stamp is `held_as_of` (`v103 b3`). Lists split outside code, bold and parentheses; `@@` in the live text: 0.
- **D5 [REVIEW]** the pasted card differs from the exemplar: `unset M T N && ` first (F1); `--no-renames` in N (a move = its two paths, as the census counts); each path one file's relative path.
- **D6 [INFO]** refusals beyond the charter: a key twice · a list scalar or empty (write `"none"`) · any `|` in a cell.
- **D7 [INFO]** U2 ran in a parallel sub-session. Review round 1 confirmed one BLOCKING (fixture checks tied to the live spine: red at the hub's `883fdff`), fixed with the other real ones; round 2 over the fixes: none blocking, five fixed, one is F4.

## §4 Findings for the register
- **F1** the hub's `gated_card()` (v103 b2 → v104 b2) lacks `unset`: a failed gate falls through `;` to `[ "$N" -eq n ] && git commit -F $M` on an N and M left by an earlier paste.
- **F2** the b2 digest (`883fdff`) has a Pi clause the template cannot express (`since 12:00:49 CT;** LOG0`): at adoption re-derive the facts and `--write` once (the template's shape becomes the law), or re-cut template and fixture together.
- **F3** v3/v4 `beat()` renders only the digests: `--write` before `beat()`; the brief then in `exp_M`.
- **F4** the card gates on the staged COUNT (a foreign staged path + an unchanged named path pass); the trailer grep is case-sensitive; only `index.lock` gates; a collapsed `dir/` is passed as its files (porcelain then reads below n). A set gate is a ruling.
- **F5** `test_splice_lib_v3.py` 3/5 red at `8ab4789` (it pins v100 b3) — pre-existing.
- **F6** `fixtures/v99b1_*` (3) unused — retire at the landing.

## §5 How the hub uses it at a beat
1. `PYTHONIOENCODING=utf-8 python3 -B context/process/render_state.py --check` → 7 MATCH (a DIFF = a region hand-cut since; F2). 2. Edit `state.yaml` only. 3. `… --probe` → `PROBE OK`. 4. `… --write` → `WROTE` ×2. 5. `… --check` → 7 MATCH. 6. The other splices, then v3's `beat()` (F3). 7. The card: pin v4 `bc10cd3f5f142e52f64a84c477fcbbee`; `card_v2(repo_key, paths, n, msg_rel, head_sha, say_back)`, `head_sha` as `%h` prints it.

## §6 Instrument limits
Helpers lived in the session's temp scratchpad, never shipped; `state.yaml` was written by hand and equals the helper's draft as data; the byte MATCH is the proof. The U2 cases need Git Bash (Windows Python's `bash` is the WSL launcher; asserted). `date -u` at start and close; bytes by `len(str.encode("utf-8"))`.
RETURNED context/audits/2026-10-10_BEAT-RENDERER-2_return.md 7936 beat-renderer-2/ledger staged=17

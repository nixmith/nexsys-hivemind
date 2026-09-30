<!--
file: context/audits/2026-09-30_v88-b3_BH-3_intake_audit.md
purpose: The hub's two-layer intake of BH-3's return (`docs/lane-returns/2026-09-30_BH-3_return.md` on `bh3/permit-join-endpoint-path`, 13,930 B; PR #1) read in the hub's own container from the public branch (v86 b3's form): the claims, the hub's re-executions at the bytes, the deviations ruled, the verdict, the landing card and BENCH-PULL-5.
audience: the v88 hub · Nick (the landing card) · v89 (BC7's card cites §3)
state-type: intake audit (one lane)
status: FILED — Wed 2026-09-30 ~12:0x CT (instrument 2026-09-30T17:09:08Z)
-->

# BH-3 — intake audit (v88 beat 3)

## §0 Verdict
**ACCEPT-WITH-NOTES.** The branch `bh3/permit-join-endpoint-path` = `dacca9c` (the five rows) + `bd2e747` (the return alone) over `d093a95`; author Nick; trailers 0; the diff stat = the charter's five paths + the return. THE GATE RE-RUN in the hub's container on the branch: `bench.sh selftest: 27 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `verify72h selftest: 26 check(s), 0 failure(s)` · `bash -n` exit 0 — equal to the return's lines. The byte census re-derived equal on all five files. The verb reads as §3 row 1 orders (the local validation; the id from the boot log's `integration.launched` line asserted against the pin, exit 4 on a mismatch; the bearer only inside the header; the six data keys; the log watch — refined to bytes written after the request, D3); the forbidden token carries its citation; the frozen verbs all present. Six deviations, all ruled ACCEPT; D1 is the hub's miss. The landing: a local squash under a GATED card (5 paths; the return directory unstaged and removed), PR #1 closed as landed, then BENCH-PULL-5 (the third selftest line joins the block). BC7 grades the first endpoint window (IR-102 a) on Friday.

## §1 Layer 1 — the claims
The card: DELIVERED; the baselines; the branch; the census; the gate; the diff stat; §1 the eleven greps (rows 1–10 equal; row 11 got 1 — D1); §2 the verb (exit 1 HTTP · 2 usage · 3 no launch line · 4 id mismatch · 5 no log line); §3 the README section (2,279 B); §4 the scenario edit with its citation; §5 the selftest (27 checks); §6 six deviations; §7 not re-executed (a live core, the Pi, IR-102 a — BC7; shellcheck absent). The first line reports the settings: `claude-fable-5-1` observed · `effortLevel` observed `max` (the build offers a level above `xhigh`) · thinking on · **`ultracode: true` NOT OBSERVED** (the lane cannot see it).

## §2 Layer 2 — re-executed here
| Check | Instrument | Result |
|---|---|---|
| The branch's commits | `git log --oneline -3 origin/bh3` · `log -2 --format=%B \| grep -c` the two trailer strings · `--format='%an <%ae>'` · `rev-parse dacca9c^` | `bd2e747` · `dacca9c` · `d093a95`; trailers 0; Nick Smith; parent `d093a95` |
| The diff stat | `git diff --stat d093a95 origin/bh3` | 6 files: README +10 · the runbook 2 · the return +102 · boot-health +6 · bench.sh +78 · test_bench_sh.py +584 — commit 1 = the five, commit 2 = the return |
| THE GATE | a worktree at `bd2e747`; the four commands as the charter names them | 27/0 · 42/0 · 26/0 · exit 0 |
| The byte census | `git show d093a95:<f> \| wc -c` → `wc -c` | bench.sh 5,913 → 11,000 · test_bench_sh.py 0 → 22,764 · boot-health 3,652 → 4,197 · README 3,515 → 5,794 · the runbook 24,490 → 24,553 — equal to the return |
| No secret | `grep -rEo '[A-Za-z0-9_-]{32,}'` over the new and edited files, the token file's NAME counted separately | the three long literals are `---` rules; `initial_api_token` appears 5× as a name only |
| The frozen verbs | `grep -c "^  <verb>)"` for the fourteen case labels + `permit-join` | 1 each |
| The verb's code | `git diff d093a95 dacca9c -- tools/bench.sh` read whole | as §0 says; `PJ_ZIGBEE_ID_PINNED='6V1CMGY2HKF4H1FGZ4H7F257FS'`; `HS_BENCH_API_BASE` default `http://127.0.0.1:7070`; `HS_BENCH_WATCH_SECS` default 5; the sed anchors `integration_type=zigbee`; the 26-character ULID class |
| The scenario edit | the diff | one `forbidden:` entry, the comment wrapped over six lines, cites `ZigbeeIntegrationAdapter.java:915 at 8deef4b` |
Not re-executed: a live core, the Pi, the real 200, the real `zigbee.permit_join_opened`, the store's counts (BC7); `shellcheck` (absent here too); the README's prose against a reader (Nick reads it at BC7).

## §3 The deviations ruled
D1 row 11 (expect 0, got 1) — **the hub's miss**: the charter's count was written from an earlier, broader grep's reading instead of the row's own command; the lane did the right thing (STOP-and-say). D2 the RETURNED sha = commit 1 — by construction; the chat line and the PR name commit 2. D3 the watch on bytes after the request — an improvement inside the row's reason; the selftest pins it. D4 three additions (the `HTTP 000` hint; a 200 without the six keys → exit 1; a non-integer watch → 5) — declared, in shape. D5 the comment's wrapping — the words verbatim. D6 the harness's own branch at `d093a95` — only `bh3/…` was pushed. **Settings:** `effortLevel: max` observed — the form's sentence "the highest of `low | medium | high | xhigh`" is stale against this build; the first-message form says "the highest the build offers (`xhigh`, or `max` where offered)" from v89 on. `ultracode` unobservable from inside a session — the form keeps naming it; the lane keeps saying so.

## §4 The landing (Nick's hands; the hub cut the card at `_scratch/v88/card_b3_bench.txt`)
Block 1 — the local squash under the gated form (5 staged after the return directory is unstaged and removed; the trailer grep; one push) → `BENCH: LANDED <sha> (BH-3)`; then PR #1 closed as landed (the button closes, never merges). Block 2 — BENCH-PULL-5 on the Pi (IR-76): `before: d093a95` · `porcelain=0` · `Fast-forward` · `after: <sha>` · `42/0` · `26/0` · `bench.sh selftest 27/0` → `BENCH-PULL-5: <sha> · 42/0 · 26/0 · 27/0`. The Pi's core clone stays PINNED at `40412f9` until BC7 (Friday) returns it to `main` and grades the first endpoint window.

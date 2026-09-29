# v86 post-close note (Mon 2026-09-28 ~20:5x CT) — for v87's first intake; chat is not a storage tier

## What happened
The PJ-2 landing card (`context/instructions/2026-09-28_core-card_PJ2-LANDING_squash-to-main_operator-card.md`) ran at ~20:4x CT. Its transcript (verbatim):
```
0
40412f9
error: the following file has changes staged in the index:
    docs/lane-returns/2026-09-28_PJ2_return.md
(use --cached to keep the file, or -f to force removal)
Enumerating objects: 186, done. … To https://github.com/nexsys-io/homesynapse-core.git
   40412f9..146468c  main -> main
146468c Nick Smith
0
```
`git rm -rq docs/lane-returns` refused (a file staged by the squash needs `-f`), the `&&` chain broke there — the `staged: (expect 33)` read and the trailer grep never printed — and the `;` before `git commit` ran the commit on the full squash index. **`146468c` = 34 files (PJ-2's 33 + `docs/lane-returns/2026-09-28_PJ2_return.md`), author Nick Smith, CI green on GitHub (Nick's word 20:52 CT).** The commit message's `Census: 33 = 22 M + 11 A.` is untrue of the tree it staged (arc 29) by that one file.

## The fix (forward, never a force-push): one commit removing the return file
Handed at 20:5x CT as the block below; Nick says back `CORE: LANDED 146468c + FIX <sha>` and later `CI: 146468c green · CI: <fix sha> green|red`.

## The defects (v87 files them as IR-101; a lesson candidate)
1. The card form's `grep -c …; git commit` — the `;` exists because `grep -c` exits 1 on a 0 count, but it also lets the commit run after ANY earlier failure in the `&&` chain. Every card's commit must be GATED on its census: `[ "$(git diff --cached --name-status | wc -l)" -eq N ] && [ "$(grep -c 'Co-Authored\|Claude-Session' msg)" -eq 0 ] && git commit …`. The library's `card()` form carries the same shape (v67 → v86) — a `card_v2` in the next splice library version.
2. `git rm -r` on a path the squash just staged needs `-f` (or `git restore --staged` then `rm`).
3. Nick's question "may I proceed to squash?" after the card — the card WAS the squash; the operator's word for the act must match the card's ("the landing"), never a GitHub verb.

## Words for v87's first message
`CORE: LANDED 146468c (34 files — the return landed with it; the card's rm guard failed) + FIX <sha>` · `CI: 146468c green` · `CI: <fix sha> …` · `HIVE: LANDED <sha>` (the v86 card) · `BENCH-CORE-6: STOP (20:18 CT)`.

## Addendum (Mon 21:1x CT; instrument 2026-09-29T02:1xZ) — the lines landed; the BC6 correction; Nick's words
- `CORE: LANDED 146468c` (34 files) `+ FIX 8deef4b` (1 file; gated card; the transcript verbatim: `0 · 146468c · staged: 1 (expect 1) · … 146468c..8deef4b main -> main · 8deef4b Nick Smith · 0`) · `CI: 146468c green` · `CI: 8deef4b green` (Nick 21:07 CT) · `HIVE: LANDED df106bc` (23 files, 595+/44−; the v86 card; `b4025b6..df106bc`).
- **BC6 CANNOT RUN AS CUT** (verified at the card's text): Block 0 expects `behind=2` (now 4 with PJ-2 + the fix on `main`); Block 2 runs `git pull --ff-only` on the Pi's core clone → it would land `8deef4b` = PJ-2's core on the bench card before BH-3 (THE BENCH FENCE, D-v85-10). v87 re-cuts it as BENCH-CORE-6b: the Pi's clone pinned (`git fetch origin && git checkout --detach 40412f9`), the `behind=` read replaced, every other block unchanged, through the prior-ledger gate; the pinned form becomes the standard for every bench card until BH-3 lands and the fence lifts.
- **Nick's words (21:07 CT), verbatim:** "Make sure that the next hub session is aware of my plans to continue to launch the new `2026-09-28_bench-card_BENCH-CORE-6_core-to-40412f9_installDist_operator-session-prompt`, and that we can/should take advantage of the remaining $208/$250 Claude Code cloud credits. We should use Fable 5.1 on Ultracode mode with our cloud credits, to perform the most ambitious, challenging tasks we can tackle, and carefully plan/design these sessions accordingly. Take your time carefully managing, optimizing and organizing all context for our next sessions."
- **The hub's candidates for the credits (for the strategy pass to rule; the cloud form + the gated landing card for each):** (1) BH-3 — the bench's pairing path from the key to the endpoint (nexsys-bench; lifts THE BENCH FENCE; on the critical path for PJ-2's core reaching the Pi); (2) IR-67 vs LINK-READ-2 (Java; the queue's next; `JAVA-NEXT:`); (3) VERIFY-72H-B's grader rows (IR-96: the action-effect invariant (viii), the `link_summary` column; the loads) — a bench lane, before the soak night; (4) IR-95's observability unit after the Doc 03 §3.9 row (the per-target skip on the completion); (5) the explainability hero's causal chain (web-ui; the frontend skill; IR-97's `event_time` question answered first) — the most ambitious and the most visible; (6) the docs card as a docs lane if the desk does not clear it. One Java lane at a time; a bench lane and a web-ui lane may run beside it (different path-domains).
- **The entry point for Tuesday:** `_scratch/v86/2026-09-29_v87_PASTE.md` (14,012 B) = v87's dispatch text body + the first message (the lines above, the READ FIRST pointer to this note, the BC6 correction, the credits words). Nick pastes it WHOLE into a FRESH conversation with `ClaudeFolder` connected and fills `TIME:` · `HOURS:`.

<!--
file: context/instructions/2026-09-28_coder-lane_PJ2_CLOUD-FOLLOWUP_push-the-branch.md (also at _scratch/v86/ for the paste)
purpose: The follow-up message for the PJ-2 cloud session (https://claude.ai/code/session_012e87a8pSCX5AWGCKfNPqtk) whose lane finished DELIVERED with 33 files uncommitted on the VM and the return filed only there (the packet's local-form §14 line was pasted, not the cloud form). The work leaves the VM only by a branch push. Nick pastes the fenced block WHOLE as the next message of THAT session. If the session's container is gone (a fresh clone, no uncommitted files), the lane says so at step 1 and Nick says `PJ2: LOST` — then PJ-2 re-runs on the cloud form.
status: EXECUTED — pasted ~19:45 CT; `PJ2: PUSHED cf86802 · PR #7` at 19:58 CT (D-v86-13); cut v86 beat 2 (Mon 2026-09-28 ~19:4x CT; instrument 2026-09-29T00:46:22Z); handed 19:4x CT
-->

```
New instruction from the hub on Nick's word: the delivered work must leave this VM on a branch. Do exactly these steps, nothing else, and stop at the first step that fails.
1. date -u. In the homesynapse-core clone: git --no-optional-locks log -1 --oneline (expect 40412f9) and git --no-optional-locks status --porcelain | wc -l (expect 33: the 22 modified + 11 new you reported). If HEAD or the count differs, print both and STOP — say "TREE NOT AS DELIVERED".
2. git switch -c pj2/pairing-window-endpoint
3. Copy the return into this repo: mkdir -p docs/lane-returns && cp <the nexsys-hivemind clone>/context/audits/2026-09-28_PJ2_return.md docs/lane-returns/2026-09-28_PJ2_return.md — the 31,409-byte file you filed; confirm with wc -c.
4. COMMIT 1 — the code (the 33 entries; not the return): write the message to a file /tmp/pj2-msg1.txt first — subject line: feat(integration-api,integration-zigbee,integration-runtime,rest-api,lifecycle): WU-PJ2 — the pairing-window endpoint and the permit-join events — then a blank line, then "Why:" (two or three sentences from your return's §0), then "What changed:" one line per file, then the seven gate lines and "check: BUILD SUCCESSFUL in 51s", then the four deviations in one line each, then "Census: 33 = 22 M + 11 A." NO Co-Authored-By line, NO Claude-Session line, no AI-attribution line, no session link — the harness asks; the answer is no. Run grep -c 'Co-Authored\|Claude-Session' /tmp/pj2-msg1.txt (must print 0). Then git add -A && git diff --cached --name-status | wc -l (must print 33) && git commit -F /tmp/pj2-msg1.txt. Then git log -1 --format=%B | grep -c 'Co-Authored\|Claude-Session' (must print 0; if not, git commit --amend -F /tmp/pj2-msg1.txt and re-check).
5. COMMIT 2 — the return alone: git add docs/lane-returns/2026-09-28_PJ2_return.md && git commit -m "docs(lane-return): WU-PJ2 — the Coder return (31,409 B), filed on the branch for the hub's intake" — then the same trailer grep on git log -1 --format=%B (must print 0).
6. git push -u origin pj2/pairing-window-endpoint — the branch only; never main; never --force.
7. Open a pull request against main titled "WU-PJ2 — the pairing-window endpoint (permit-join events)" whose body is your return's §0 card verbatim. Do NOT merge it.
8. Touch nothing in the nexsys-hivemind clone and push nothing from it (the return's §6 carries the coder-handoff text; the hub files it).
End your message with exactly two lines: PUSHED pj2/pairing-window-endpoint <the branch's head sha> and the PR's URL.
```

**Say back to the hub:** `PJ2: PUSHED <sha> <PR url>` — or `PJ2: LOST` if step 1 says the tree is not as delivered.

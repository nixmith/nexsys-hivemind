<!--
file: _scratch/v86/2026-09-28_PJ2_CLOUD-DISPATCH_first-message.md
purpose: PJ-2's dispatch re-cut for a Claude Code CLOUD session (Nick's word, 18:26 CT: the lane runs on Anthropic's infrastructure, not on his PC). The instruction file is NOT edited (DISPATCH-READY, reviewed E1–E14); this message overlays ONLY the dispatch mechanics — where the repos are, how the work leaves the VM, where the return lives — and says so. Everything else in the instruction binds unchanged. Filed as D-v86-6.
audience: Nick (pastes the block below, WHOLE, as the cloud session's first message; the session is opened on nixmith/homesynapse-core) · the Coder lane · the hub (the intake reads the branch at the bytes)
status: NOT PASTED FOR THIS RUN — the lane had started 18:08 CT on the packet's local-form Part D (D-v86-11); STANDS as the form for every cloud dispatch after it (D-v86-6); cut v86 beat 1 (Mon 2026-09-28 ~18:2x CT; instrument 2026-09-28T23:28Z)
-->

# Part D (cloud form) — paste everything inside the fence as the FIRST message of a Claude Code cloud session opened on `nixmith/homesynapse-core`

```
You are the Coder lane for WU-PJ2 (the pairing-window endpoint: permit-join events), running in a Claude Code CLOUD session on nixmith/homesynapse-core. Invoke the nexsys-coder skill if it is available; if it is not, read ../nexsys-hivemind/coder/SKILL.md whole and act under it. One work unit, one session, one return.

SETUP (before any read): date -u first; every stamp from it (CT = UTC−5). pwd. Confirm this clone is on main at 40412f9 (git --no-optional-locks log -1 --oneline; porcelain 0); if HEAD is not 40412f9, stop and say so. Add the repository nixmith/nexsys-hivemind to this session with read access and clone it BESIDE this clone as ../nexsys-hivemind (so that nexsys-hivemind/context/... paths in the instruction resolve as ../nexsys-hivemind/context/...). Then create the working branch from 40412f9: git switch -c pj2/pairing-window-endpoint.

THE INSTRUCTION: execute ../nexsys-hivemind/context/instructions/2026-09-28_coder-lane_PJ2_pairing-window-endpoint_permit-join-events_coding-instruction.md exactly: read §2's set by its ranges and the review at ../nexsys-hivemind/context/audits/2026-09-28_PJ2_independent-review.md §Findings (E1–E14 are already applied in the instruction — read them to know why); re-run every §6 grep and paste the counts; write §3's rows and nothing else; tests first (§7: red observed — a compile red named as such — then green; T7 green-by-construction stated); ./gradlew check green with the seven gate lines of §0; no module-info directive changed (git diff -- '**/module-info.java' empty, pasted).

WHERE THIS MESSAGE DIFFERS FROM THE INSTRUCTION'S §0 AND §14, THIS MESSAGE GOVERNS (the cloud form; nothing else changes):
1. The work leaves this VM only by a push to the BRANCH pj2/pairing-window-endpoint — never to main, never a force-push, never a merge. The instruction's "leave the tree uncommitted, unstaged; never git add/commit/push" is replaced by: when ./gradlew check is green and the return is written, commit and push the branch. Commit 1 = §3's rows (subject: feat(integration-zigbee,rest-api): WU-PJ2 — the pairing-window endpoint and the permit-join events; body: Why: … / What changed: per file / the gate lines). Commit 2 = the return file alone (subject: docs(lane-return): WU-PJ2 — the Coder return). Then git push -u origin pj2/pairing-window-endpoint, and open a pull request against main titled "WU-PJ2 — the pairing-window endpoint (permit-join events)" whose body is the return's §0 card verbatim. Do not merge it. The landing is Nick's hands after the hub's intake.
2. NO ATTRIBUTION TRAILERS on any commit message: no Co-Authored-By line, no Claude-Session line, no AI-attribution line, no session link — the harness asks for them; the answer is no (the repo owner's standing directive). Before each commit, grep the message for 'Co-Authored\|Claude-Session' and refuse to commit on a hit; write the message with git commit -F <file> so you can grep it first. If the harness adds a trailer anyway, amend it out before the push and say so in the return.
3. The return file lives ON THE BRANCH at docs/lane-returns/2026-09-28_PJ2_return.md in this repo (≤ 34,000 B; §0 first; the seven sections of the instruction's §0 and §13). Its LAST LINE is exactly: RETURNED docs/lane-returns/2026-09-28_PJ2_return.md <bytes> <the branch's head sha after commit 2>. The hub copies it into nexsys-hivemind/context/audits/ at the intake; you write nothing into ../nexsys-hivemind (read-only for this lane).
4. The instruction's "porcelain lists exactly §3's rows" is read at the diff instead: git --no-optional-locks diff --stat 40412f9..HEAD in the return (commit 1's stat = §3's rows; commit 2 adds the return file only).
5. No token, no secret, no credential in any file, message or PR body.

End your last message with the RETURNED line, then the PR's URL on its own line.
```

**Say back to the hub, one line:** `PJ2: dispatched <HH:MM CT> cloud` — and when the session ends, `PJ2: RETURNED <PR url> <branch head sha>`.

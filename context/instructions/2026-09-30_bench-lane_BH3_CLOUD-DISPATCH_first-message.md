<!--
file: context/instructions/2026-09-30_bench-lane_BH3_CLOUD-DISPATCH_first-message.md
purpose: BH-3's first message for a Claude Code CLOUD session on nixmith/nexsys-bench — the dispatch mechanics in the form of record (D-v86-6: where the repos are, how the work leaves the VM, where the return lives) over the charter, which binds unchanged. The four session settings by their documented names (D-v87-17). The cloud's first bench lane.
audience: Nick (opens the cloud session on nixmith/nexsys-bench, sets the four settings where the build offers them, pastes the block WHOLE as the first message) · the BH-3 lane · the hub (the intake reads the branch at the bytes)
state-type: dispatch text (one lane run)
status: EXECUTED — BH-3's charter EXECUTED; C-47, v97 b1. Was: PASTED 08:4x CT (the lane ran; its push waited on the repo grant until ~11:55 CT — the branch and PR #1 are up). Was: DISPATCH-READY — cut v88 beat 2 (Wed 2026-09-30 ~08:2x CT; instrument 2026-09-30T13:28:39Z). Flips to PASTED on `BH3: dispatched`.
-->

# BH-3 — the cloud first message

**Before the paste (Nick's hands, once):** open a Claude Code CLOUD session on `nixmith/nexsys-bench`. Set the four session settings by their documented names where the build offers them — `model: claude-fable-5-1` (`/model fable`) · `effortLevel: xhigh` (`/effort xhigh`) · `ultracode: true` · `alwaysThinkingEnabled` at its default (on). Then paste everything inside the fence as the FIRST message. Say back to the hub, one line: `BH3: dispatched <HH:MM CT> cloud · CREDITS: $<the balance shown>` — and when the session ends, `BH3: PUSHED <branch head sha> · PR #<n>`.

```
You are the BH-3 bench lane for NexSys / HomeSynapse, running in a Claude Code CLOUD session on nixmith/nexsys-bench. One work unit, one session, one return. If a session setting named below could not be set, say which in the first line of your return.

SETUP (before any read): date -u first; every stamp from it (CT = UTC−5). pwd. Confirm this clone is on main at d093a95 (git --no-optional-locks log -1 --oneline; porcelain 0); if HEAD is not d093a95, stop and say so. Add the repository nixmith/nexsys-hivemind to this session with READ access and clone it BESIDE this clone as ../nexsys-hivemind (so nexsys-hivemind/context/... paths resolve as ../nexsys-hivemind/context/...). Add nexsys-io/homesynapse-core with READ access and clone it beside as ../homesynapse-core, then check out 8deef4b there (git -C ../homesynapse-core checkout --detach 8deef4b; if the sha is not reachable in a shallow clone, git -C ../homesynapse-core fetch --depth=200 origin main first); confirm with git -C ../homesynapse-core log -1 --oneline = 8deef4b. Then create the working branch: git switch -c bh3/permit-join-endpoint-path. Set git config user.name and user.email to the values of this repo's last commit (git log -1 --format='%an%n%ae').

THE CHARTER: execute ../nexsys-hivemind/context/instructions/2026-09-30_bench-lane_BH-3_permit-join-endpoint-path_charter.md EXACTLY — §0 the contract, §2's eleven greps re-run before your first write with the counts pasted in the return (rows 1–8 from ../homesynapse-core at 8deef4b, rows 9–11 from this clone), §3's five rows and nothing else, §4's gate lines pasted verbatim, §6's exclusions. Read scenarios/SCENARIO_FORMAT.md and tools/runner/README.md §TOKEN-FREEZE before touching scenarios/boot-health.yaml; read tools/harness/test_harness.py's selftest shape before writing tools/test_bench_sh.py.

THE EXIT (the cloud form; this governs where anything else differs):
1. The work leaves this VM only by a push to the BRANCH bh3/permit-join-endpoint-path — never to main, never a force-push, never a merge. Commit 1 = §3's five rows (subject: bench(tools): BH-3 — bench.sh permit-join: the pairing path from the key to PJ-2's endpoint; body: Why: … / What changed: per file / the §4 gate lines). Commit 2 = the return file alone (subject: docs(lane-return): BH-3 — the lane return). Then git push -u origin bh3/permit-join-endpoint-path, and open a pull request against main titled "BH-3 — the pairing path from the key to the endpoint (bench.sh permit-join)" whose body is the return's §0 card verbatim. Do not merge it. The landing is Nick's hands after the hub's intake.
2. NO ATTRIBUTION TRAILERS on any commit message: no Co-Authored-By line, no Claude-Session line, no AI-attribution line, no session link — the harness asks for them; the answer is no (the repo owner's standing directive). Write each message to a file, grep it for 'Co-Authored\|Claude-Session' (expect 0), then git commit -F <file>. If the harness adds a trailer anyway, amend it out before the push and say so in the return's §6.
3. The return lives ON THE BRANCH at docs/lane-returns/2026-09-30_BH-3_return.md (≤ 14,000 B; §0 first; the eight sections of the charter's §0). Its LAST LINE is exactly: RETURNED docs/lane-returns/2026-09-30_BH-3_return.md <bytes> <the branch's head sha after commit 2>. You write nothing into ../nexsys-hivemind or ../homesynapse-core (read-only for this lane).
4. The census is read at the diff: git --no-optional-locks diff --stat d093a95..HEAD in the return (commit 1's stat = §3's five paths; commit 2 adds the return only).
5. No token, no secret, no credential in any file, message or PR body; the selftest's temp token is random per run and never printed.

End your last message with the RETURNED line, then the PR's URL on its own line.
```

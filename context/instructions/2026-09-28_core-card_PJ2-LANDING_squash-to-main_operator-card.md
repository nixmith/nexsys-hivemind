<!--
file: context/instructions/2026-09-28_core-card_PJ2-LANDING_squash-to-main_operator-card.md
purpose: PJ-2's landing on `main` by Nick's hands — a local squash of the lane's branch (pj2/pairing-window-endpoint, ed26a4c) under his identity, the lane's return dropped from the tree, the hub's message file, one push; CI on the push is the gate of record. One block, one line back.
audience: Nick (runs it) · the hub (banks `CORE: LANDED <sha>` and the CI line)
state-type: operator card (one block)
status: DISPATCH-READY — cut v86 beat 3 (Mon 2026-09-28 ~20:0x CT; instrument 2026-09-29T01:07:59Z) at PJ-2's intake (ACCEPT-WITH-NOTES, `context/audits/2026-09-28_v86-b3_PJ2_intake_audit.md`). Flips to EXECUTED at `CORE: LANDED`.
-->

# PJ-2 LANDING — the squash to `main` (one block). Say back `CORE: LANDED <sha>`; later `CI: <sha> green|red` from the Actions page.

**Before you start:** the BC6 guide conversation is CLOSED. `main` on your PC is at `40412f9` with porcelain 0 (the block checks both and stops otherwise). Git Bash.

```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core && git --no-optional-locks status --porcelain | wc -l && git --no-optional-locks log -1 --format=%h && ls .git/*.lock 2>/dev/null; git fetch -q origin pj2/pairing-window-endpoint && git merge --squash origin/pj2/pairing-window-endpoint >/dev/null && git rm -rq docs/lane-returns && echo "staged: $(git diff --cached --name-status | wc -l) (expect 33)" && grep -c 'Co-Authored\|Claude-Session' ../_scratch/v86/2026-09-28_core_PJ2_commit-msg.txt; git commit -q -F ../_scratch/v86/2026-09-28_core_PJ2_commit-msg.txt && git push && git log -1 --format='%h %an' && git --no-optional-locks status --porcelain | wc -l
```
Read, in order: `0` · `40412f9` · `staged: 33 (expect 33)` · `0` · the push · `<sha> Nick …` (your name, not the VM's) · `0`. STOP on a first line other than `0`, a HEAD other than `40412f9`, a `staged:` other than 33, or a trailer count other than 0 — say the line back and touch nothing.

**Then, on GitHub:** close PR #7 with the comment "landed on main as <sha> by squash" (do not merge it). The branch stays for the record. When the Actions run on `<sha>` finishes: `CI: <sha> green|red`.

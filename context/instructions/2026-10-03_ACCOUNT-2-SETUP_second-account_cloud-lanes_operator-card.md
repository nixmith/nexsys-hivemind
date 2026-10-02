<!--
file: context/instructions/2026-10-03_ACCOUNT-2-SETUP_second-account_cloud-lanes_operator-card.md
purpose: ACCOUNT-2-SETUP — the second Claude account (`$250` of cloud credits; this hub's account has `$16`) made ready to run the cloud lanes (VERIFY-72H-B · HERO-1 · later cloud Java lanes) in ≈ 45 min of Nick's hands: the GitHub connection to the five `nexsys-io` repositories checked by a READ and by a scratch-branch PUSH before any lane's paste (THE GRANT IS CHECKED BEFORE THE PASTE, 2026-09-30 — BH-3's push waited ~3 h on a read-only grant); the three role skills uploaded from their SOURCE trees (Check 9's mirror of record for that account); what is NOT a dependency (memory; the hub's own session). One file, five acts, one line back (D-v92-4, D-v92-14).
audience: Nick (runs it Saturday morning before v93 dispatches V72B) · the v93 hub (reads the one line)
state-type: operator card (account setup; no repo write except one scratch branch pushed and deleted)
status: HELD — Nick's word, Fri 2026-10-02 15:52 CT (the second account is not now; he will prompt and steer it); DISPATCH-READY again on his word. Was: DISPATCH-READY — cut v92 beat 4 (Fri 2026-10-02 ~09:0x CT; instrument 2026-10-02T14:00:49Z); flips to EXECUTED on `ACCOUNT-2: ready · GRANT: push-ok · SKILLS-2: 3`.
-->

# ACCOUNT-2-SETUP — the second account carries the cloud lanes

**Why this exists.** The cloud lanes draw on the account they run in. This hub's account holds `$16` (your word, Fri 07:41 CT); the second holds `$250` and can connect to the repositories. Nothing on Friday needed the cloud (the re-mint was a desk commit; BC7 is the rig), so the setup is Saturday morning's first act and every cloud lane after it runs there. The hub stays on this account with the device bridge; lanes need no memory and no shared conversation — a lane boots from its packet and the repository, and the record (the hivemind) is the memory.

**What a lane on the second account needs — exactly three things.** (1) GitHub: the Claude GitHub App installed for `nexsys-io` with the five repositories granted (`homesynapse-core` · `homesynapse-core-docs` · `nexsys-hivemind` · `nexsys-skills` · `nexsys-bench`), and the account's cloud sessions able to PUSH — checked by a push, not by the settings page. (2) Skills: the three role skills present as account skills — `nexsys-project-manager`, `nexsys-coder`, `nexsys-frontend` — uploaded from the SOURCE trees on your desktop (never from a session's synced copy): `nexsys-hivemind/project-manager/` · `nexsys-hivemind/coder/` · `nexsys-skills/orchestrators/nexsys-frontend/` (28 `.md` files in all; Check 9 on the new account = these md5s). (3) Nothing else: no memory import, no folder link (a cloud lane clones from GitHub), no copy of the hub's conversation.

## Act 1 — the GitHub connection (the second account; the browser; ≈ 10 min)
Sign in to the second account at claude.ai. Settings → Connectors (or the GitHub connection in Claude Code's cloud settings) → connect GitHub → install the app for the `nexsys-io` organization → grant the five repositories by name (not "all repositories"). Say back `A1: five granted` (or the names it refused).

## Act 2 — the skills (the second account; the browser; ≈ 10 min)
In the second account's skills settings, add the three skills from the SOURCE folders above (each folder has a `SKILL.md` at its root and a `references/` directory; upload the folder, or a zip of it, as the UI asks — the name the UI shows must be the one in the folder's `SKILL.md`). Say back `A2: 3 skills` with the three names as shown.

## Act 3 — THE GRANT CHECK: a READ and a PUSH, in a fresh cloud session on the second account (≈ 10 min)
Open a new Claude Code cloud session on the second account and paste this as its first and only message:
```
Clone https://github.com/nexsys-io/homesynapse-core-docs.git and print `git log -1 --oneline` (expect 055832c). Then: git checkout -b grant-probe/2026-10-03 && echo "grant probe $(date -u +%Y-%m-%dT%H:%M:%SZ) — delete me" > GRANT-PROBE.txt && git add GRANT-PROBE.txt && git commit -m "chore: grant probe (deleted in the same session)" && git push -u origin grant-probe/2026-10-03 && git push origin --delete grant-probe/2026-10-03. Print the push's result lines verbatim. Add no attribution trailer to the commit. Do nothing else; touch no other branch.
```
Read: `055832c …` · a `* [new branch] grant-probe/2026-10-03 -> grant-probe/2026-10-03` line · a `- [deleted] grant-probe/2026-10-03` line. Say back `A3: GRANT: push-ok` — or paste the refusing line (a 403 / "not enabled" / "read-only" line means Act 1 granted read only: repeat Act 1 for write access and run Act 3 again; do NOT paste any lane until this says push-ok).

## Act 4 — the clones of record (the same session, one more message; ≈ 5 min)
```
Clone the other four: https://github.com/nexsys-io/homesynapse-core.git, https://github.com/nexsys-io/nexsys-hivemind.git, https://github.com/nexsys-io/nexsys-skills.git, https://github.com/nexsys-io/nexsys-bench.git. Print each `git log -1 --oneline`. Then in homesynapse-core run `./gradlew --version | head -3` and in nexsys-bench run `python3 -B tools/test_bench_sh.py 2>&1 | tail -1`. Print the lines verbatim; change nothing.
```
Read: `5b0e20c …` · the hivemind's newest sha · `e9a77a8 …` · the bench at the re-mint's sha · a Gradle version block · `bench.sh selftest: 27 check(s), 0 failure(s)`. Say back `A4: five cloned`. (The clone depth and the toolchain are the lane's own concern; this proves reachability.)

## Act 5 — the credits figure and the one line back
Read the second account's cloud credits figure after Acts 3–4 (a few cents). Say back the ONE line: `ACCOUNT-2: ready · GRANT: push-ok · SKILLS-2: 3 · CREDITS-2: $<n>` — or `ACCOUNT-2: STOP <act> <the line>`.

## What this card does not do
It does not move the hub (this conversation and the ones after it stay on this account while its credits last; if the hub must move, the boot prompt is the same file, the record is the memory, and the device bridge is re-made by linking ClaudeFolder in the desktop app signed into the second account — a separate card, cut only if asked). It does not sync memory (the lanes do not read it; the hub's user-memory is a convenience of its own account). It does not dispatch a lane: V72B's and HERO-1's first messages are v93's to hand, each carrying `GRANT: push-ok` as its own first check and the cloud form's exit (leave the tree at porcelain; the return under the lane's path; the push to a lane branch, never `main`).

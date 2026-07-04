<!--
file: context/process/cowork-environment-model.md
purpose: The verified operating model of the Claude Cowork environment the PM runs in — path duality, mount-sync lag, write-collision hazards, tool semantics, token economics. Read at PM session start BEFORE editing any shared file. Every rule here was paid for; do not re-learn them by collision.
audience: PM (Cowork); Coder (the mount-lag section)
update-cadence: when a new environment behavior is observed and verified
state-type: reference
status: CURRENT
last-verified: 2026-06-11 (the M6.2-return session — the session that paid for most of these)
-->

# Cowork Environment Model (PM operating rules)

## 1. Two path namespaces; the session slug is ephemeral
File tools (Read/Edit/Write) use Windows host paths (`C:\Users\Nick\Desktop\Code\ClaudeFolder\…`). Shell commands run in an isolated Linux VM where the same files appear under `/sessions/<slug>/mnt/ClaudeFolder/…`. **The slug changes every session — never hardcode it** (the Check-9 rule): resolve by topology (walk up from a known file to `mnt/`). The VM also mounts `.claude/skills/` (read-only mirror) and the session `outputs/`/`uploads/` dirs.

## 2. Mount-sync lag — the write-collision hazard (the M6.2 lesson)
The VM mount mirrors the host with **lag in both directions, minutes-scale**, and host mtimes are preserved (so a "new" file can carry an old mtime). Consequences, all observed 2026-06-11:
- A host-side Claude Code session's writes can land in the Cowork view MID-SESSION; early reads may serve the pre-write state.
- A Cowork full-file write based on a lagged read can clobber host-side changes. **Case study:** the Coder's M6.2 cross-agent entry was lost to an overlapping PM rotation write and had to be reconstructed from the completion report.
- Interleaved single-string Edits can survive cleanly (the M6.2 coder-handoff Status line nested both writers' content correctly) — but that was luck of anchoring, not a guarantee.

**Rules:** (a) at session start, compare `git status` against handoff-file mtimes — a clean tree with "Last updated today by Coder" content means a sync already landed; a clean tree that later shows modifications means one is landing. (b) If a Coder session may be in flight, do NOT structurally rewrite (rotate/rebuild) the three shared files it writes — `coder-handoff.md`, `cross-agent-notes.md`, `coder-lessons.md`; targeted single-anchor Edits only, and prefer deferring even those. (c) At WUCP Phase 2, **verify the Coder's Phase-1 checklist claims against the actual files** — a claimed-but-absent artifact is the mount-lag signature. (d) Re-read any shared file immediately before editing it if surprising content has appeared anywhere this session.

**Truncated-tail artifact (observed + verified 2026-06-12):** the VM mount can serve files with their TAILS MISSING — cut mid-token at end-of-file, no trailing newline (`pr`, `Nick autho`, `assertThatIll`). VM `git status`/`git diff` then report phantom modifications (pure deletions at EOF) across MANY files in BOTH repos at once. **Signature: every "modified" file is a clean truncation at EOF with "\ No newline at end of file."** Diagnosis: Read the file tails via the file tools (host namespace) — if intact on the host, it is read-side lag, not damage; trust the file tools, treat VM git output as suspect, and do NOT "fix" or commit anything based on the VM view. **Attribution corollary (2026-07-03, beat 64 — three lanes tripped on it in ONE day):** porcelain `M`-flags on recently-committed spine files are PRESUMED PHANTOM until `git log` says otherwise — never attribute them to "another agent's in-flight/uncommitted work" in a return without checking HEAD first. Two independent lane returns recorded the same false "hub's uncommitted spine writes" observation on files that were ALREADY COMMITTED (one lane's own preflight had even logged the commit as HEAD); the index-read variant of this phantom also fabricates staged-looking `D`/`R` flags with rename targets cut mid-filename (the bench-class signature).

## 3. Shell semantics
Each bash call is independent — **no cwd/env carryover**; use absolute paths or `cd … &&` per call. 45s timeout per call. The VM boots in the background ("Workspace still starting" → wait, retry). **The VM can die mid-session** (M6.4 precedent) — the file tools keep working and are the authoritative path; design sessions so shell loss is survivable. Gradle/javac are not reliably runnable in the Coder's sandbox either — the deferred-gate discipline exists for this.

## 4. Deletion is permission-gated; moves are not
`rm`/`rmdir` on the mounted folder fail with "Operation not permitted" until the file-delete permission is granted (a one-time tool call per folder). Plain `mv` (renames, including cross-directory within the mount) work without it — which is why archive-rotation is always available even when deletion is not.

**Git index.lock hazard (paid for 2026-06-12; re-paid 2026-07-02):** VM git commands that refresh the index (`git status`, `git add`, `git diff` without `--no-optional-locks`) CREATE `.git/index.lock` through the mount but CANNOT DELETE it (deletion gated) — when the unlink fails, a stale 0-byte lock is left ON THE HOST that blocks Nick's git until removed. **`git add --dry-run` ALSO takes the lock** (verified stranding one 2026-07-02 — "dry-run" is not read-only; `--no-optional-locks` does not cover `add`). To preview a change set, use `git --no-optional-locks status --porcelain` (lock-free), never `add --dry-run`. Mitigations: prefer `git --no-optional-locks status` / `git log` (no index lock) for read-only state checks; if a lock strands, `mv` it aside (e.g. `index.lock.cleared-by-cowork-<date>`) and flag Nick to delete it.

**Mount-lag scale correction (observed 2026-07-02, FE-1 lane):** the read-side lag documented above as "minutes-scale" ran **>30 minutes** for edited files in one session (a NEW file synced promptly; EDITS lagged). Design accordingly: host file tools remain authoritative and unlagged; treat any VM-side read of a recently-edited file as suspect regardless of elapsed time.

## 5. File-tool discipline
Read-before-Edit/Write is enforced per conversation. Edit requires an exact, unique `old_string` — for mega-line files a unique substring suffices. For multi-file or structural rewrites, use a python script via bash with **all asserts before any write, all writes at the end** (a failed assert then leaves everything untouched — this saved the cross-agent rotation twice).

**Bulk-edit source rule (paid for 2026-06-12 — the AMD-tail clobber):** a VM-side read-modify-write of a mounted worktree file can READ a truncated-tail view (§2) and WRITE the truncation back, destroying the host file's tail even though every assert passed (asserts only see the truncated view). The six ratified AMD files lost their §9/§10 tails this way and were reconstructed from git. **Rule: bulk/scripted edits to governance-class files (AMDs, design docs, registers) either (a) run HOST-SIDE via the file tools, or (b) source their input from GIT OBJECTS (`git show <sha>:<path>`) — never from a VM worktree read. After ANY scripted write, verify the file TAIL via host file tools before proceeding.** Anchor hygiene corollary (paid same day): when cutting at a section heading, match it line-anchored (`^## X$`), never `find("## X")` — prose mentions of the heading match first. After a bulk operation, verify with a targeted grep, not a full re-read. Beware position-dependent assumptions about file ordering: coder-lessons was append-ordered oldest-first and a "cut from first old header" rotation took the new entries with it (caught and repaired by a chronology assert).

**Gate-copy recipe (FE-1b, 2026-07-03 — the mount-outrun pattern):** when a lane's fresh edits outrun the mount but a VM-side check must still run, build a disposable verification copy from GIT OBJECTS at HEAD (`git show HEAD:<path>`) + re-apply the lane's exact edit set under assert-all-before-write, then prove copy ≡ host (hash the host view via file tools) before gating on the copy. Never gate on a raw worktree read inside the lag window.

## 6. Skills: writable source vs read-only mirror
The live skill the agents load is a read-only cache; the **writable source is `nexsys-hivemind/{coder,project-manager}/`**. Any source edit leaves Check 9 STALE until Nick runs his external mirror sync. Batch skill-source edits into files already awaiting sync when possible (keeps the sync delta small).

## 7. Session scratch vs the mounted folder
The session `outputs/` scratchpad is invisible to Nick and cleared between sessions. **Everything durable goes into the mounted ClaudeFolder.** Uploaded files arrive in-context (readable without disk reads) and also at an `uploads/` path; don't re-read what's already in context.

## 8. Token economics (the hygiene rationale)
Hot-path files (snapshot, weekly plan, both handoffs, cross-agent, lessons) are read every session by some agent — their size is a per-session tax. Keep them rotated (the 2026-06-11 pass: 728K→188K). **Write handoff entries as short paragraphs, never single mega-lines** — multi-thousand-token lines defeat line-based pagination and forced the Coder to PowerShell/grep workarounds. Top-loaded MODULE_CONTEXT structure (JPMS block + inventory first) is what makes 73K-token files cheaply skimmable — keep that convention.

## 9. Misc verified quirks
- Interactive question tools can fail mid-stream — fall back to the veto-or-default pattern and document the chosen default.
- Host MINGW64 bash eats `!` in double-quoted commit messages (history expansion — the M6.2 commit body lost a bullet line). **Inner double-quotes are the sibling hazard:** a `"…"` fragment inside the `-m "…"` closes the shell string early → bash drops to the `>` continuation prompt and the commit never runs (paid for 2026-06-28, the M7.5b core commit — a body with `"why didn't it fire?"`). Messages containing `!`, an inner `"`, or backticks go via `git commit -F <file>` — the hub prepares that file in `ClaudeFolder/_scratch/` (a sibling of the repos, so the worker's `git add -A` never stages it), and hands the absolute `git commit -F /c/Users/.../ _scratch/<file>` command.
- `du -k` block-size readings on the mount can mislead right after writes; use `wc -c`/`ls -l` for byte truth.
- In-tree `mv` is committed by Nick's plain `git add -A` as renames (100% similarity preserved) — no `git mv` needed from the Cowork side.
- **esbuild's NATIVE binary SIGSEGVs in this sandbox class** (Go-runtime; observed 2026-07-03, website lane — rollup native loads fine, sharp bus-errors). Working pattern when a Vite/Astro build must run in-lane: build on a `/tmp` copy proven ≡ mount by md5 over the full file set, with an `esbuild → esbuild-wasm` override applied to the BUILD COPY ONLY; the committed tree stays native (clean manifest + lock regenerated lock-only). The lane's green is NOT the gate of record — Nick's native host run is. Also: the VM shared disk can be 100% full — check before `npm ci`.

## 10. Pre-commit change-set audit (adopted 2026-07-02 — Nick's check, made standing)

Before ANY commit command is handed to Nick — especially a directory sweep (`git add <dir>/` or `-A`) — the preparing agent runs this audit and states the result in the handoff/return:

1. **Inventory:** `git --no-optional-locks status --porcelain` (lock-free — NEVER `add --dry-run`, §4). Count the files.
2. **Every file maps to a claimed deliverable.** Each modified/untracked path must trace to a specific item in the completion report / lane return. An unexplained file is a STOP — investigate before staging (it is either forgotten work, junk, or someone else's write).
3. **Ignore-coverage check for the hazard classes:** runtime state (`.homesynapse/`, `*.db`, `*.log`), build output (`node_modules/`, `dist/`, `build/`, `coverage/`), secrets (`.env*`, tokens, `*.key`/`*.pem`), caches. Verify both that the patterns are in `.gitignore` AND that nothing of these classes appears in the porcelain output; spot-verify with `git ls-files | grep` that none are already TRACKED (ignore rules don't untrack).
4. **Secrets sweep:** any session that ran a server/minted a token names the artifact and its disposition (deleted / ignored / never-written). A bearer token, pairing token, or key NEVER enters git — and never enters a commit MESSAGE either.
5. **State the expected count in the command handoff** ("stages exactly N files") so Nick's own `git status` glance can confirm before he runs it.

Lane-return templates inherit this: a return that requests a commit carries the audited file list. The skills point here (pointer-not-copy) rather than restating.

## 11. Client-restart semantics (paid 2× — the v14 launch + v14 beat 54)

A Cowork client drop/restart rolls the CONVERSATION back (context, task list, the in-flight reply) but NOT the files or commits — the pre-drop turn's writes persist on the host. The resumed conversation is a fresh instance colliding with its own ghost. **Signatures:** uncommitted spine writes you don't remember making; a frontmatter stamp newer than your last known beat; an Edit `old_string` failing on text you "know" is current; TaskUpdate returning "Task not found" for a task you believe exists (the task list rolled back with the conversation). **Protocol (standing; v15 first-act 0):** after ANY restart/relaunch, run lock-free porcelain + Read both spine frontmatters BEFORE any spine write; if a prior instance wrote, treat its product as an un-audited return — source-check its load-bearing claims, then MERGE (never duplicate; the canonical block is the one the staged commit message describes). If any anchor in a spine edit batch fails, HALT the batch and treat every sibling edit in it as suspect.

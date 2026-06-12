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

## 3. Shell semantics
Each bash call is independent — **no cwd/env carryover**; use absolute paths or `cd … &&` per call. 45s timeout per call. The VM boots in the background ("Workspace still starting" → wait, retry). **The VM can die mid-session** (M6.4 precedent) — the file tools keep working and are the authoritative path; design sessions so shell loss is survivable. Gradle/javac are not reliably runnable in the Coder's sandbox either — the deferred-gate discipline exists for this.

## 4. Deletion is permission-gated; moves are not
`rm`/`rmdir` on the mounted folder fail with "Operation not permitted" until the file-delete permission is granted (a one-time tool call per folder). Plain `mv` (renames, including cross-directory within the mount) work without it — which is why archive-rotation is always available even when deletion is not.

## 5. File-tool discipline
Read-before-Edit/Write is enforced per conversation. Edit requires an exact, unique `old_string` — for mega-line files a unique substring suffices. For multi-file or structural rewrites, use a python script via bash with **all asserts before any write, all writes at the end** (a failed assert then leaves everything untouched — this saved the cross-agent rotation twice). After a bulk operation, verify with a targeted grep, not a full re-read. Beware position-dependent assumptions about file ordering: coder-lessons was append-ordered oldest-first and a "cut from first old header" rotation took the new entries with it (caught and repaired by a chronology assert).

## 6. Skills: writable source vs read-only mirror
The live skill the agents load is a read-only cache; the **writable source is `nexsys-hivemind/{coder,project-manager}/`**. Any source edit leaves Check 9 STALE until Nick runs his external mirror sync. Batch skill-source edits into files already awaiting sync when possible (keeps the sync delta small).

## 7. Session scratch vs the mounted folder
The session `outputs/` scratchpad is invisible to Nick and cleared between sessions. **Everything durable goes into the mounted ClaudeFolder.** Uploaded files arrive in-context (readable without disk reads) and also at an `uploads/` path; don't re-read what's already in context.

## 8. Token economics (the hygiene rationale)
Hot-path files (snapshot, weekly plan, both handoffs, cross-agent, lessons) are read every session by some agent — their size is a per-session tax. Keep them rotated (the 2026-06-11 pass: 728K→188K). **Write handoff entries as short paragraphs, never single mega-lines** — multi-thousand-token lines defeat line-based pagination and forced the Coder to PowerShell/grep workarounds. Top-loaded MODULE_CONTEXT structure (JPMS block + inventory first) is what makes 73K-token files cheaply skimmable — keep that convention.

## 9. Misc verified quirks
- Interactive question tools can fail mid-stream — fall back to the veto-or-default pattern and document the chosen default.
- Host MINGW64 bash eats `!` in double-quoted commit messages (history expansion — the M6.2 commit body lost a bullet line). Messages containing `!` go via `git commit -F <file>`.
- `du -k` block-size readings on the mount can mislead right after writes; use `wc -c`/`ls -l` for byte truth.
- In-tree `mv` is committed by Nick's plain `git add -A` as renames (100% similarity preserved) — no `git mv` needed from the Cowork side.

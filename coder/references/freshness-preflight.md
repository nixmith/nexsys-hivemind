# Coder Freshness Preflight

**Run this at the start of every Coder session, immediately after loading Tier 1 context (PROJECT_SNAPSHOT.md, coder-handoff.md, cross-agent-notes.md, the active coding instruction).** The preflight detects hivemind drift before you act on stale assumptions. Skipping it is how the M2.2 / M2.4 arch-debt violations shipped undetected — see `../../context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`.

This is the Coder mirror of the PM's `project-manager/references/freshness-preflight.md`. The PM's preflight has 10 checks; the Coder's preflight is a smaller subset — the Coder only needs to detect drift that would make the current coding instruction unsafe to execute, not drift across the full governance layer.

---

## 1. When to Run

- **At Coder session start**, after loading Tier 1 context but before reading the active coding instruction in detail. If the preflight reports STALE or CONFLICTED, stop before investing effort in an instruction that may be based on stale assumptions.
- **Before running WUCP Phase 1 Step 1** (MODULE_CONTEXT.md updates), because stale MODULE_CONTEXTs turn into bad writes.

---

## 2. The Six Checks

### Check 1 — PROJECT_SNAPSHOT.md vs. coder-handoff.md consistency

Read `../../context/status/PROJECT_SNAPSHOT.md` and `../../context/handoff/coder-handoff.md`. The "Last Completed Milestone" in both files must match. The "Next / Current Task" in both files must match.

- **PASS** if both files agree.
- **STALE** if coder-handoff.md names a more recent milestone than PROJECT_SNAPSHOT.md (PM has not run WUCP Phase 2 on the last milestone).
- **CONFLICTED** if the two files name different milestones with no clear ordering.

### Check 2 — Commit head vs. PROJECT_SNAPSHOT

Run `git -C ../../homesynapse-core log --oneline -5`. The most recent commit SHA should match the `Latest Commit` field in PROJECT_SNAPSHOT.md (or at most 1–2 commits ahead with the intermediates explicitly logged).

- **PASS** if PROJECT_SNAPSHOT is caught up to HEAD.
- **STALE** if PROJECT_SNAPSHOT is behind HEAD and the intermediate commits are not accounted for in coder-handoff.md either.
- **CONFLICTED** if PROJECT_SNAPSHOT cites a commit SHA not in `git log`.

### Check 3 — Coding instruction references exist

Read the active coding instruction. Every file path, design-doc section, MODULE_CONTEXT.md reference, and commit SHA cited in the instruction must exist at the cited path in the current tree.

- **PASS** if every cited reference resolves.
- **STALE** if a cited file has been renamed (e.g., `BLOCK_BACKLOG.md` → `phase-3-milestone-backlog.md`).
- **CONFLICTED** if a cited reference is missing entirely.

### Check 4 — MODULE_CONTEXT.md for target module is populated

For the module the coding instruction targets, read the MODULE_CONTEXT.md. It must not be the empty template.

- **PASS** if populated and its "Phase 3 Cross-Module Context" section (if present) references the Phase 3 decisions register.
- **STALE** if populated but lacks the Phase 3 addendum and the target module is one where the addendum would materially change the implementation approach (clock injection, persistence-internals visibility, event-dispatch pattern).
- **CONFLICTED** if the file cites types or contracts that do not exist in the source code.

### Check 5 — Arch-rule whitelist awareness

Verify that the target module's package path (e.g., `com.homesynapse.persistence`) is NOT in the `NO_DIRECT_TIME_ACCESS` ArchUnit whitelist unless the instruction says otherwise. Whitelist is: `com.homesynapse.app..`, `com.homesynapse.platform..`, `com.homesynapse.test..`. Any test code in a non-whitelisted package must inject `Clock`.

- **PASS** if the module is correctly classified AND the instruction reflects the classification (e.g., instruction says "inject Clock for all time reads").
- **STALE** if the instruction does not mention `Clock` injection for a non-whitelisted module that reads time.

### Check 6 — Dual skill-location mirrors

Resolve the session root from this file's location (the session slug is ephemeral — do not hardcode it):

```bash
# This file lives at: <SESSION_ROOT>/mnt/ClaudeFolder/nexsys-hivemind/coder/references/freshness-preflight.md
SESSION_ROOT="$(cd "$(dirname "$0")/../../../../.." && pwd)"

diff -rq \
  "$SESSION_ROOT/mnt/ClaudeFolder/nexsys-hivemind/coder" \
  "$SESSION_ROOT/mnt/.claude/skills/nexsys-coder" 2>&1
```

- **PASS** if `diff -rq` produces empty output.
- **STALE** if `diff -rq` reports "Only in ClaudeFolder" entries — a PM edit hasn't been mirrored yet; Nick runs the mirror sync externally.
- **CONFLICTED** if `diff -rq` reports "differ" entries — same file, divergent content.

---

## 3. Aggregating to PASS / STALE / CONFLICTED

- **PASS** — all six checks PASS. Proceed with the coding instruction.
- **STALE** — at least one check STALE, zero CONFLICTED. See §4.
- **CONFLICTED** — at least one check CONFLICTED, regardless of others. See §5.

---

## 4. Response Protocol — STALE

When STALE, the Coder cannot execute the coding instruction as-is. Allowed activity:

- Read the source code that the coding instruction would touch (ground-truth gathering)
- Write a cross-agent-note identifying the STALE check and the specific drift
- Escalate to PM in the coder-handoff.md next-entry draft with `[BLOCKING-PENDING-PM-REFRESH]`

Forbidden activity under STALE:

- Writing production code against a stale instruction
- Declaring a milestone DONE
- Running `./gradlew check` and then committing based on a stale assumption

---

## 5. Response Protocol — CONFLICTED

CONFLICTED means the instruction or the hivemind contains a contradiction the Coder cannot resolve on its own. **Hard stop.**

Required action:

1. Write a cross-agent-note identifying every CONFLICTED check and the evidence.
2. Escalate to PM with severity `[BLOCKING]`.
3. Do not touch any file until PM or Nick has resolved the conflict.

---

## 6. Preflight Output Format

```
CODER FRESHNESS PREFLIGHT — 2026-MM-DD HH:MM UTC
Check 1 (snapshot ↔ handoff):          PASS
Check 2 (commits vs snapshot):         PASS
Check 3 (instruction refs exist):      PASS
Check 4 (target MODULE_CONTEXT):       PASS
Check 5 (arch-rule whitelist aware):   PASS
Check 6 (dual skill mirrors):          STALE  (expected — post-PM-edit, pre-sync)

Aggregate: STALE
Allowed activity: ground-truth gathering only; escalate to PM
```

If PASS, single-line record suffices:

```
CODER FRESHNESS PREFLIGHT — 2026-MM-DD HH:MM UTC — PASS (all 6 checks)
```

---

## 7. Origin

This preflight was introduced on 2026-04-11 as part of the Alignment Pass #2 session, mirroring the PM-side preflight introduced the same day. It addresses the same root cause identified in the M2.5 arch-debt retrospective: drift between the hivemind and the codebase can silently poison a session's work. The Coder-side checks are narrower than the PM's because the Coder's sphere of responsibility is narrower — the Coder only needs to detect drift that would corrupt the current milestone, not drift across the full governance layer.

Any new check added to the PM-side preflight that has Coder-side implications must be mirrored here.

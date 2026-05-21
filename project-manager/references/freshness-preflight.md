<!--
file: project-manager/references/freshness-preflight.md
purpose: PM session-start preflight for detecting hivemind drift before issuing any work product.
audience: PM, Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Freshness Preflight

**Run this at the start of every PM session and at the start of every WUCP Phase 2 review.** The preflight detects hivemind drift before you act on stale assumptions. Skipping it is the single highest-leverage mistake the PM can make — it is how M2.2 and M2.4 shipped arch-debt that the governance layer didn't catch until M2.5 (see `../../context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`).

---

## 1. When to Run

- **At PM session start**, immediately after loading Tier 1 context (PROJECT_SNAPSHOT.md, current week's plan, cross-agent notes, pm-handoff.md). Do not process any task brief until the preflight has reported PASS.
- **At the start of WUCP Phase 2**, before verifying the Coder's Phase 1 checklist. If the preflight reports STALE or CONFLICTED, the review cannot proceed as forward work — see §5.
- **After any session where Nick has edited hivemind files directly** (he'll flag this in cross-agent-notes.md).

---

## 2. The Ten Checks

Run all ten. Each check either passes, flags STALE, or flags CONFLICTED. Do not short-circuit — one PASS does not excuse running the others, because drift compounds.

### Check 1 — PROJECT_SNAPSHOT.md last-sync timestamp

Read the `Last Sync` timestamp at the top of `../../context/status/PROJECT_SNAPSHOT.md`. Compare to today's date.

- **PASS** if the timestamp is within the last 14 days AND matches the most recent entry in the Recent Session Log.
- **STALE** if the timestamp is older than 14 days OR does not match the most recent session log entry.
- **CONFLICTED** if the `Last Sync` field is missing, malformed, or shows a future date.

### Check 2 — Current week's plan exists

Check `../../context/planning/weeks/` for a file matching the current ISO week (e.g., `2026-W15_apr06-apr12.md`).

- **PASS** if the file exists AND its Status field is `IN_PROGRESS` or `COMPLETE`.
- **STALE** if no file exists for the current week, or the file exists but has Status `TEMPLATE` or is missing a Status line.
- **CONFLICTED** if multiple files exist for the same week, or the file's date range doesn't match the actual ISO week.

### Check 3 — Recent commits vs. PROJECT_SNAPSHOT

Run `git -C ../../homesynapse-core log --oneline -20` and compare the most recent commit SHA to the `Latest Commit` field in PROJECT_SNAPSHOT.md.

- **PASS** if the PROJECT_SNAPSHOT latest-commit matches `git log` head, OR is at most 3 commits behind with all intermediate commits explicitly listed in the Recent Session Log.
- **STALE** if PROJECT_SNAPSHOT is more than 3 commits behind and intermediate commits are not accounted for.
- **CONFLICTED** if PROJECT_SNAPSHOT cites a commit SHA that does not exist in `git log`.

### Check 4 — Milestone backlog consistency

Read `../../context/planning/phase-3-milestone-backlog.md`. Cross-reference every milestone marked DONE against:
- PROJECT_SNAPSHOT.md current milestone
- The weekly plan that contained the milestone
- An actual commit in `git log` (cited by SHA)

- **PASS** if every DONE milestone has all three references.
- **STALE** if a milestone is marked DONE in the backlog but missing from PROJECT_SNAPSHOT.
- **CONFLICTED** if a milestone is marked DONE but no matching commit exists, or if two milestones claim the same commit.

### Check 5 — pm-handoff.md Open Risks consistency

Read the Open Risks section of `../../context/handoff/pm-handoff.md`. Every Open Risk entry must reference:
- A specific milestone or commit
- A resolution owner (Nick, PM, or Coder)
- A `Deferred Build Gate` flag if it originated from a skipped `./gradlew check`

- **PASS** if every Open Risk has all three fields.
- **STALE** if Open Risks exist but the section was last updated more than 7 days ago.
- **CONFLICTED** if an Open Risk references a commit or milestone that doesn't exist.

### Check 6 — Coder handoff next-work-unit pointer

Read `../../context/handoff/coder-handoff.md`. The most recent entry must explicitly identify the next work unit (refuse-to-close rule).

- **PASS** if the most recent entry names the next work unit by ID (e.g., `M2.6` or `Block T`).
- **STALE** if the entry says "awaiting direction" without a next-unit pointer.
- **CONFLICTED** if the entry names a next work unit that contradicts the weekly plan or milestone backlog.

### Check 7 — MODULE_CONTEXT.md files populated for completed Phase 2 modules

For every module with Phase 2 marked complete in the block backlog, verify `../../homesynapse-core/{module-path}/MODULE_CONTEXT.md` exists and has been populated (not the empty template).

- **PASS** if every completed-Phase-2 module has a populated MODULE_CONTEXT.md.
- **STALE** if one exists but is the empty template.
- **CONFLICTED** if the file cites types or contracts that don't exist in the source code.

### Check 8 — Cross-agent-notes.md active entries

Read `../../context/handoff/cross-agent-notes.md`. Every entry above the `## Archived` separator must be:
- Dated within the last 14 days
- Not yet resolved, OR resolved within the last 48 hours

- **PASS** if all active entries satisfy both conditions.
- **STALE** if any active entry is older than 14 days and unresolved.
- **CONFLICTED** if an entry is marked resolved but the resolution contradicts PROJECT_SNAPSHOT or the weekly plan.

### Check 9 — Dual skill-location mirrors

The agent runs inside a fresh Cowork session each time, so absolute paths change every session (the session slug segment — e.g., `eager-exciting-shannon` — is unstable). Resolve the session root relative to this file's own location and compare the two skill trees:

```bash
# Resolve to the session root from this file's location (works regardless of session slug).
# This file lives at: <SESSION_ROOT>/mnt/ClaudeFolder/nexsys-hivemind/project-manager/references/freshness-preflight.md
SESSION_ROOT="$(cd "$(dirname "$0")/../../../../.." && pwd)"

diff -rq \
  "$SESSION_ROOT/mnt/ClaudeFolder/nexsys-hivemind/project-manager" \
  "$SESSION_ROOT/mnt/.claude/skills/nexsys-project-manager" 2>&1

diff -rq \
  "$SESSION_ROOT/mnt/ClaudeFolder/nexsys-hivemind/coder" \
  "$SESSION_ROOT/mnt/.claude/skills/nexsys-coder" 2>&1
```

If `$0` isn't available in the current shell context (e.g., when running commands ad-hoc rather than from a script), use the equivalent environment-discovery approach: start from any `ClaudeFolder` file you know exists and walk up to `mnt`, then compare against the sibling `.claude/skills/` mount. The **rule**: never hardcode the session slug. The session slug is ephemeral; the `ClaudeFolder → mnt → .claude/skills` topology is stable.

- **PASS** if both `diff -rq` commands produce empty output.
- **STALE** if either command reports "Only in" entries for files that exist only in the `ClaudeFolder` source tree (Nick has not yet run the mirror sync).
- **CONFLICTED** if either command reports "differ" entries — the same file has divergent content in both locations.

Note: `.claude/skills/` is a read-only mount; the PM never writes to it. STALE is the normal state immediately after a PM edit — it clears when Nick runs his external sync. CONFLICTED is abnormal and blocks forward work.

### Check 10 — Strategic context map references

Spot-check that every reference file cited in `../../context/strategic-context-map.md` actually exists at the cited path.

- **PASS** if every cited file exists.
- **STALE** if a cited file has been renamed but the map still shows the old name.
- **CONFLICTED** if a cited file is missing entirely.

---

## 3. Aggregating to PASS / STALE / CONFLICTED

- **PASS** — all ten checks returned PASS. Forward work is unblocked. Proceed to the task brief.
- **STALE** — at least one check returned STALE, zero returned CONFLICTED. See §4.
- **CONFLICTED** — at least one check returned CONFLICTED, regardless of other results. See §5.

---

## 4. Response Protocol — STALE

When the preflight reports STALE, the PM's activity is **restricted to retroactive reconciliation**. Forward work (new task briefs, new coding instructions, new design docs) is not permitted until the hivemind is brought back to PASS.

**Allowed activity under STALE:**
- Retroactive WUCP Phase 2 for the most recent completed work unit
- Updating PROJECT_SNAPSHOT.md, the weekly plan, and pm-handoff.md to match the actual codebase state
- Populating a missing MODULE_CONTEXT.md from a completed Phase 2 module
- Archiving expired cross-agent notes
- Running Nick's external mirror sync (if STALE came from Check 9 only — request Nick in cross-agent-notes.md)

**Forbidden activity under STALE:**
- Issuing new coding instructions
- Processing a new task brief beyond reading it to queue
- Declaring any work unit DONE in the backlog
- Advancing the weekly plan to a new milestone

When the reconciliation is complete, re-run the preflight. Continue only after PASS.

---

## 5. Response Protocol — CONFLICTED

CONFLICTED means something in the hivemind is contradictory — a milestone marked DONE with no commit, an Open Risk referencing a nonexistent file, a skill-location mirror with divergent content. This is a **hard stop**.

**Required action:**
1. Write a cross-agent-note identifying every CONFLICTED check, the specific contradiction, and the evidence.
2. Escalate to Nick in the Completion Report or session-end handoff with severity `[BLOCKING]`.
3. Do not touch any file until Nick has resolved the conflict or explicitly authorized a specific remediation.

CONFLICTED is uncommon but signals an integrity failure in the governance layer. Treat it with the same urgency as a `[BLOCKING]` deviation from the Coder.

---

## 6. Preflight Output Format

Record the preflight result at the top of the PM session log or the WUCP Phase 2 review output:

```
FRESHNESS PREFLIGHT — 2026-MM-DD HH:MM UTC
Check 1 (PROJECT_SNAPSHOT timestamp):  PASS
Check 2 (current week plan):           PASS
Check 3 (commits vs snapshot):         PASS
Check 4 (milestone backlog):           PASS
Check 5 (pm-handoff Open Risks):       PASS
Check 6 (coder next-unit pointer):     PASS
Check 7 (MODULE_CONTEXT populated):    PASS
Check 8 (cross-agent-notes active):    PASS
Check 9 (dual skill mirrors):          STALE  (expected — post-edit, pre-sync)
Check 10 (strategic-context-map refs): PASS

Aggregate: STALE
Allowed activity: retroactive reconciliation only
Blocking issue: Nick's external mirror sync pending (Check 9)
```

If the aggregate is PASS, a single-line record suffices:

```
FRESHNESS PREFLIGHT — 2026-MM-DD HH:MM UTC — PASS (all 10 checks)
```

---

## 7. Origin

This preflight was introduced on 2026-04-11 as part of the hivemind overhaul. It addresses the root cause identified in `../../context/audits/2026-04-11_m2.5-arch-debt-retrospective.md` — the PM session protocol had no mechanism to detect that the hivemind was lagging behind the codebase. Without a preflight, the PM would read a 3-week-old PROJECT_SNAPSHOT and treat it as ground truth, issuing instructions based on stale assumptions about what existed and what contracts governed it.

The ten checks are not exhaustive. New checks may be added as the project discovers additional drift vectors. Any proposed addition must:
1. Be added to this file with the PASS / STALE / CONFLICTED definitions
2. Be added to the `FRESHNESS PREFLIGHT` output format above
3. Be mirrored into any coder-side preflight file if it has Coder-side implications

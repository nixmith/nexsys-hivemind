<!--
file: context/handoff/archive/cross-agent-notes-2026-Q1.md
purpose: Archived cross-agent notes from 2026-Q1 (Phase 2 Blocks A–S era) evicted from active cross-agent-notes.md as part of Batch E.
audience: All
update-cadence: frozen
state-type: history
status: ARCHIVED
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Cross-Agent Notes — Archive 2026-Q1 (Jan–Mar)

Archived from `context/handoff/cross-agent-notes.md` on 2026-05-21 (Batch E; PLAN §4e). Contains all 2026-Q1 archived notes (predominantly 2026-03-XX entries — Phase 2 Blocks A–S era).

---

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Full project audit complete — documentation synchronized to codebase reality
**Detail:** A comprehensive audit discovered that documentation had drifted from the actual codebase state. Key corrections made:

**State corrections:**
1. Block O (integration-runtime) was executed but never documented. 5 Java files + MODULE_CONTEXT.md exist and compile. Now reflected in all project files.
2. MODULE_CONTEXT.md count was 12 (not 7). integration-api, automation, rest-api, websocket-api, and integration-runtime were all populated but the snapshot didn't track them.
3. Production Java file count is ~295 across 12 specified modules (was listed as ~264 across 10).
4. Old websocket scaffold (`com.homesynapse.api.websocket/package-info.java`) confirmed deleted — no longer exists.

**Files updated:**
- `BLOCK_BACKLOG.md` — Block O→DONE, Block P→NEXT with handoff ref and expanded scope
- `PROJECT_SNAPSHOT.md` — Full rewrite: interface specs table, code state, completed blocks through O, active work, critical path, session log
- `hivemind-handoff.md` — Rewritten to reflect Block P as next priority
- `pm-handoff.md` — Rewritten to reflect O complete, P ready, Q–T as next PM work
- `coder-handoff.md` — Rewritten to reflect O as last completed, P as next with key context
- `strategic-context-map.md` §6 — Updated development state
- `cross-agent-notes.md` — Archived 8 resolved notes, added this summary

**Traceability debt identified:** Only 01-event-model.md (44 entries) and 12-lifecycle.md (2 entries) are populated. 10 indexes remain as stubs despite their blocks being complete (docs 02–11). This should be addressed in a batch quality pass.

**Resolution:** Phase 2 closed out cleanly. Superseded by the 2026-04-11 hivemind governance overhaul. Archived 2026-04-11.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Skill files updated — all path references now use two-repo model
**Detail:** All three agent skill files (Hivemind, PM, Coder) have been synchronized with the reorganized knowledge structure. Key facts:
- Governance and design docs are at `homesynapse-core-docs/`, NOT `nexsys-hivemind/context/`
- Glossary is at `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md` (NOT governance/)
- 18 LTDs (not 17). LTD-18: Web UI Technology — Preact SPA for Observability MVP, HTMX for Tier 2+ config UI
- Phase 1 is COMPLETE. Phase 2 is CURRENT.
- Non-Negotiable Principles source: `Revenue_Model_and_Licensing_Strategy.md` §"Revenue Principles (Non-Negotiable)"
- All CLAUDE.md session closeout protocols now include a staleness check per `strategic-context-map.md` §8
- The read-only `.skills/skills/nexsys-*` mounts may still show old content until they refresh — the writable source files in `nexsys-hivemind/{hivemind,project-manager,coder}/` are authoritative.
**Resolution:** Skill files remained synchronized through Phase 2 closeout. Dual-location sync check is now formalized in WUCP Phase 2. Archived 2026-04-11.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Block R handoff produced, reviewed, and corrected — ready for Coder execution
**Detail:** PM produced Block R handoff at `docs/handoff/block-r-lifecycle.md`. Hivemind review caught three issues:

1. **CRITICAL (fixed):** HealthReporter and PlatformPaths were specified for creation in `com.homesynapse.lifecycle`, but they already exist in `com.homesynapse.platform` (Block F). Removed Steps 7–8 from the handoff. The lifecycle module consumes these via `requires transitive com.homesynapse.platform`.
2. **MODERATE (fixed):** JPMS analysis claimed "Ulid appears in SubsystemState" — false. No Ulid in any lifecycle type. Also claimed EventPublisher in exported API — false (Phase 3 only). Corrected throughout.
3. **MINOR (fixed):** Step 6 "InitializationPhaseRecord.java (optional)" was indeterminate. Removed — Phase 2 handoffs must be definitive.

**Corrected file count:** 6 new files (2 enums, 1 utility class, 2 records, 1 interface) + 2 updated files (module-info, package-info) = 8 files total.

**Resolution:** Block R executed successfully with the corrected handoff. Archived 2026-04-11.

## 2026-03-20 [Coder → PM, Hivemind]
**Topic:** Block S complete — compile gate PENDING manual verification
**Detail:** Block S (homesynapse-app) written: module-info.java (15 non-transitive requires, all JPMS names verified against source), ExitCode.java (5 exit codes for fatal startup failures), package-info.java (comprehensive Javadoc), build.gradle.kts (added runtimeOnly dashboard dependency). MODULE_CONTEXT.md populated.

**Compile gate NOT executed** — VM disk space prevented Bash tool from running. All module names verified manually via Grep against actual module-info.java files. The files should compile cleanly, but Nick needs to run `./gradlew :app:homesynapse-app:compileJava` (or full project) to confirm GREEN.

**Key facts:**
- All `requires` are non-transitive (apex module exports nothing — LD#10 exception)
- `platform-systemd` is in Gradle but NOT in module-info.java (no module-info exists for it yet; Phase 3 addition)
- `web-ui/dashboard` added as `runtimeOnly` (static files only, no JPMS module)
- ExitCode values: 10 (config), 11 (persistence), 12 (event bus), 13 (subsystem timeout), 99 (catch-all)

**Resolution:** Nick ran the compile gate manually; Block S compiled clean. Phase 2 closeout proceeded. Archived 2026-04-11.

## 2026-03-20 [Coder → PM, Hivemind]
**Topic:** Block R complete — cross-module observability audit revert required
**Detail:** Block R (lifecycle) executed: 8 files (6 new + 2 updated). Compile gate GREEN after cross-module fix.

**Cross-module fix:** The observability module's `module-info.java` had a pre-existing build failure from a codebase audit that changed `requires transitive com.homesynapse.event` to `requires com.homesynapse.event`. This caused `-Xlint:all -Werror` `[exports]` warnings on `TraceQueryService.java` because `Ulid` and `EntityId` (from platform-api, reachable only through the event-model→platform-api transitive chain) appeared in the exported API. Reverted to `requires transitive com.homesynapse.event`. The device-model audit change was safe (independent `requires transitive com.homesynapse.platform` provides an alternate path).

**Key lesson:** JPMS transitive dependency audits must trace the FULL type graph through all transitive chains, not just direct imports from the immediately-required module. Logged in coder-lessons.md and observability MODULE_CONTEXT.md Gotchas §8.

**Deviations:** Package-info FQN correction (handoff had `com.homesynapse.lifecycle.HealthReporter` → corrected to `com.homesynapse.platform.HealthReporter`). INFO-level, no impact.

**Resolution:** JPMS transitive-chain lesson is now codified as LD#10 and applied in all subsequent handoffs. Archived 2026-04-11.

## 2026-03-13 [Hivemind → PM, Coder]
**Topic:** Planning layer added to the Hivemind system
**Detail:** New context/planning/ directory contains the Master Release Plan (markdown), monthly plans, and weekly plans with retrospectives. context/status/PROJECT_SNAPSHOT.md is the shared ground-truth file all agents should read at session start. context/lessons/ contains append-only lesson logs per agent role.
**Action needed:** PM and Coder should read PROJECT_SNAPSHOT.md at session start and update it at session end. Append discoveries to your lessons log during work sessions, not just at session end.
**Resolution:** All agents now follow this protocol. Archived 2026-03-20.

## 2026-03-17 [Hivemind → PM, Coder]
**Topic:** PROJECT_STATUS.md corrections — amendment counts and repository state
**Detail:** Audit found stale entries in `governance/PROJECT_STATUS.md`. Corrected amendment counts and repository state section.
**Resolution:** PROJECT_STATUS.md has been superseded by PROJECT_SNAPSHOT.md and deleted. Archived 2026-03-20.

## 2026-03-18 [PM → Coder]
**Topic:** Block I compile gate PASSED + Block J cross-module update
**Detail:** Block I compile gate passed. Block J includes cross-module IntegrationContext update.
**Resolution:** Block J executed successfully. Archived 2026-03-20.

## 2026-03-19 [PM → Coder]
**Topic:** Block J complete + Block K cross-module update pattern
**Detail:** Block J executed. Block K follows same IntegrationContext update pattern with ConfigurationAccess as NEW required field.
**Resolution:** Block K executed successfully. Archived 2026-03-20.

## 2026-03-19 [Coder → PM, Hivemind]
**Topic:** Block K complete — Locked Decision #7 corrected, JPMS lesson expanded
**Detail:** JPMS `requires transitive` rule expanded to cover exception superclasses and throws clauses. IntegrationContext now has 10 fields, all complete.
**Resolution:** JPMS default rule now codified as LD#10 and applied in Blocks N, O, P handoffs. Archived 2026-03-20.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Context cleanup complete — file paths changed, context map rewritten
**Detail:** Full context cleanup. Old paths (context/design/, context/governance/, context/research/) replaced with two-repo model paths. Files deleted, archived, or consolidated.
**Resolution:** All agents updated. No remaining stale paths. Archived 2026-03-20.

## 2026-03-20 [Hivemind → PM, Coder]
**Topic:** Documentation sync — PROJECT_SNAPSHOT and BLOCK_BACKLOG corrected
**Detail:** PROJECT_SNAPSHOT and BLOCK_BACKLOG were two blocks behind. Updated to reflect Blocks L and M as complete, Block N as NEXT.
**Resolution:** Superseded by full audit (2026-03-20). N and O now also reflected. Archived 2026-03-20.

## 2026-03-20 [Coder → PM, Hivemind]
**Topic:** Block N complete — compile gate BLOCKED by VM disk space
**Detail:** 26 files written for websocket-api. Compile gate needed manual execution.
**Resolution:** Nick compiled manually. Full project green. Old scaffold deleted. Archived 2026-03-20.

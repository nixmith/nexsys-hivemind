<!--
file: context/handoff/archive/cross-agent-notes-2026-Q2.md
purpose: Archived cross-agent notes from 2026-Q2 (Phase 3 M2.x/M3.x era pre-2026-05-17) evicted from active cross-agent-notes.md as part of Batch E.
audience: All
update-cadence: frozen
state-type: history
status: ARCHIVED
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Cross-Agent Notes — Archive 2026-Q2 (Apr–Jun)

Archived from `context/handoff/cross-agent-notes.md` on 2026-05-21 (Batch E; PLAN §4e). Contains all 2026-Q2 archived notes — the 2026-04-10 M2.5 closeout note and both 2026-05-15 M2→M3 Bridge notes.

---

## 2026-04-10 [Coder → PM, Nick]
**Topic:** M2.5 closeout — build.gradle.kts was pre-truncated in working copy; arch-rule fix landed in the test file
**Detail:** Two items from the M2.5 SqliteEventStore coding session that crossed agent boundaries: (1) `core/persistence/build.gradle.kts` was truncated mid-comment at line 21 in the working copy; Coder restored from `git show HEAD:...` then added the `testImplementation(testFixtures(project(":core:event-model")))` line. Nick verified the diff before committing. (2) `NO_DIRECT_TIME_ACCESS` ArchUnit rule fires on test classes in non-whitelisted packages — the first draft of `SqliteEventStoreTest` used `Clock.systemUTC()` and `System.nanoTime()`, failed `./gradlew check`, and was fixed to use `Clock.fixed(...)` matching the `InMemoryEventStoreTest` convention.
**Resolution:** Both items resolved during M2.5 landing. Item (1) diff clean, committed in `5279e7a`. Item (2) codified in `coder-lessons.md` 2026-04-10 entry and in the 2026-04-11 M2.5 arch-debt retrospective audit. PM protocol updated: coding briefs for modules outside the app/platform/test whitelist must include an explicit Clock-injection reminder. Archived 2026-04-11 as part of Alignment Pass #2.

## 2026-05-15 [Coder → PM, Nick]
**Topic:** AMD-38 and AMD-39 are DRAFT pending D1 WAL pathology spike — DO NOT promote to APPLIED until D1 results land
**Detail:** The M2→M3 Bridge work unit (2026-05-15) introduced three governance amendments:
- **AMD-38** (Doc 03 §9 checkpoint policy revision) — DRAFT
- **AMD-39** (LTD-03 journal_size_limit revision) — DRAFT
- **AMD-40** (Doc 04 §3.4 retention execution model) — APPLIED immediately (structural correction, no empirical question)

AMD-38 and AMD-39 each carry a `## Validation Gate` section in the amendment file describing the specific D1 outcomes that promote them from DRAFT to APPLIED. The Java constants that depend on these amendments (`FixedCheckpointPolicy.HOME_DEFAULT`, `DeploymentProfile.HOME.journalSizeLimitBytes()`) ship with the provisional values immediately because Phase 2 interfaces need real values to compile, but the design-doc-level governance status remains DRAFT until D1 closes.

**What must happen before promotion:**
1. Nick runs D1 (WAL Pathology Validation Spike) on hs-dev-1 (Pi 5 dev board).
2. D1 results determine each amendment's fate (APPLIED / revised / withdrawn).
3. If revised values are needed, this is a 2-file coding change (`FixedCheckpointPolicy.HOME_DEFAULT` and `DeploymentProfile.HOME` constant in `DeploymentProfile.java`) plus an amendment update.
4. If withdrawn (D1 shows the pathology doesn't reproduce at HomeSynapse scale), an amendment-withdrawal note must land before the next architecture review.

**Open Risk for pm-handoff.md:** The provisional values bake into Phase 3 work for M3 — any M3 code that depends on these constants is implicitly betting on D1 outcomes. Until D1 closes, that bet is open.

**Resolution:** D1 completed 2026-05-15. AMD-38 APPLIED, AMD-39 WITHDRAWN. DeploymentProfile corrected to uniform 6 MB. Risk closed. Archived 2026-05-17.

## 2026-05-15 [Coder → PM]
**Topic:** V001 description in persistence MODULE_CONTEXT.md may have stale information about `intent_kind`/`logical_time`/`node_id` binding
**Detail:** While reading V001 to verify the STOP-on-Mismatch gate, the source shows:
- `intent_kind TEXT NOT NULL DEFAULT 'UNSPECIFIED'`
- `logical_time INTEGER NOT NULL DEFAULT 0`
- `node_id INTEGER NOT NULL DEFAULT 0`

But persistence MODULE_CONTEXT.md (gotcha at line ~341 in the pre-2026-05-15 version) describes these as bound via `setNull` along with `batch_id` and `external_ref`. The schema is NOT NULL with DEFAULT — `setNull` would violate the NOT NULL constraint. Either the schema or the description (or the actual `SqliteEventStore.INSERT_SQL` code) is out of sync.

Did NOT investigate or modify within this work unit (out of scope per brief). Flagged for PM-led reconciliation. Action item: read `SqliteEventStore.doAppend()` bind logic and either update the MODULE_CONTEXT.md gotcha to match, or fix the bind logic, or relax the V001 schema (V001 has not shipped, so all three are options).

**Resolution:** Pending PM triage.

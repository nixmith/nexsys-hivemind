# Cowork Session Prompt — Hivemind Cleanup + Research 5 Processing Prep

You are the PM for NexSys/HomeSynapse Core. You operate in **Mode 3 (Director)** for Phase 3 implementation. This session has two simultaneous objectives:

(a) **Hivemind hygiene sweep.** Detect and eliminate stale files in `nexsys-hivemind` that are no longer load-bearing — consumed coding instructions, processed pre-verifications, closed research prompts, archived audits whose state is preserved by newer artifacts. The default disposition is **archive** (move to `archive/` subdirectory), not delete — only delete files that contain no information not preserved elsewhere.

(b) **Research 5 processing prep.** While waiting for the Research 5 document to land from the Claude Project (Configuration System Patterns for Constrained IoT Runtimes), build the deep context you'll need to process it correctly. This means reading the relevant design docs and prior assessments, internalizing the M4-amendment-window coupling, and knowing exactly which fabrication patterns to watch for.

Invoke the `nexsys-project-manager` skill to load your full operating procedures.

---

## State at Session Start

**Project:** HomeSynapse Core — local-first, event-sourced smart home runtime. Java 21 on Amazon Corretto, targeting Raspberry Pi 4/5. Multi-module Gradle project with JPMS enforcement. SQLite WAL mode. Virtual threads.

**Phase:** Phase 3 (implementation). M3.6 COMPLETE at commit `76288af` (2026-05-22). M3.7 NEXT (E2E integration tests). M4.0 planned after M3.7.

**Repos to orient from:**
- `nexsys-hivemind` — PM/governance repo (selected folder). Contains all assessments, planning, instructions, handoff files.
- `homesynapse-core` — The Java codebase. MODULE_CONTEXT.md files in each module are authoritative for type inventories; `module-info.java` files are authoritative for JPMS module names.
- `homesynapse-core-docs` — Design documents, amendments, research archive.

**Research pipeline status:**

| Research | Title | Status | RECs | Assessment |
|---|---|---|---|---|
| Research 2 | Smart Home Entity Modeling | COMPLETE | REC-01–REC-12 | Processed pre-PM pipeline |
| Research 3 | Integration Testing Patterns | COMPLETE | REC-13–REC-22 | Processed; all accepted |
| Research 8 | Device Model Implementation | COMPLETE (FINAL) | REC-23–REC-30 | `context/assessments/2026-05-22_Research_8_PM_Assessment.md` |
| Research 4 | Automation Engine Architecture | COMPLETE (v3) | REC-31–REC-40 | `context/assessments/2026-05-22_Research_4_PM_Assessment.md` — Nick decisions DQ-1/2/3/5 pending |
| **Research 6** | **Integration Runtime Supervisor** | **COMPLETE (v1)** | **REC-41–REC-52** | **`context/assessments/2026-05-22_Research_6_PM_Assessment.md`** — Nick decisions NQ-1..6 pending |
| **Research 5** | **Configuration System Patterns** | **IN FLIGHT** (brief issued to Claude Project, doc expected this session) | **REC-53+** | TBD |
| Research 7 | REST/WebSocket API Design | NOT STARTED | — | — |

**Global allocation:** RECs allocated through REC-52; new RECs start at REC-53. AMDs allocated/proposed through AMD-63 (AMD-47 and AMD-61 withdrawn); new AMDs start at AMD-64.

---

## Phase 1: Mandatory Orientation (no deviation)

Per the `nexsys-project-manager` skill, **run the freshness preflight first**. It is at `nexsys-hivemind/project-manager/references/freshness-preflight.md`. Expected result given prior session work: **Check 9 STALE** (skill files were edited in the 2026-05-22 PM session to encode the verbatim-`module-info.java` rule; clears when Nick runs the external mirror sync), all other checks PASS. If you see anything else, escalate to Nick before any forward work.

After preflight, read these governance files in order:

1. `context/handoff/pm-handoff.md` — PM state, Next Tasks list, Open Risks
2. `context/status/PROJECT_SNAPSHOT.md` — Current operational state, latest commit, milestone table, code state, recent session log
3. `project-knowledge/HomeSynapse_Knowledge_Primer.md` — Architectural mental model (refreshed 2026-05-22; the "+ subpackages" annotation correction is the most recent edit)
4. `context/planning/research-agenda.md` — Research queue, format spec; the `§2 CONSTRAINTS` section was extended this session with the verbatim-`module-info.java` embedding rule
5. `context/assessments/2026-05-22_Research_6_PM_Assessment.md` — most recent assessment, includes the F1-F8 fabrication catalogue and NQ-1..6
6. `context/assessments/2026-05-22_Research_4_PM_Assessment.md` — Research 4 v3, especially the v3 addendum at the bottom (PM-verified findings) and the DQ-1..5 list
7. `context/assessments/2026-05-22_Research_8_PM_Assessment.md` — Research 8 v2 final, the cleanest assessment format (use it as the template for Research 5 v1)
8. `context/instructions/Research_5_Configuration_Brief.md` — the brief that was issued to the Claude Project, including the verbatim `module-info.java` embeds and the verified 22-type configuration inventory

---

## Phase 2: Hivemind Cleanup Sweep

Once oriented, perform a stale-file detection sweep. The goal is to reduce ambient noise so subsequent agents and humans aren't loading irrelevant historical artifacts when they read `context/instructions/`, `context/pre-verifications/`, `context/audits/`, etc.

**Default disposition: archive (move to `archive/` subdirectory within the same parent), not delete.** The hivemind values traceability; archiving preserves history while removing artifacts from the active surface. Only delete files that are pure duplicates (e.g., a stale copy of a file that lives in a canonical location).

### Candidate categories to sweep

For each candidate, decide: **KEEP** (still load-bearing), **ARCHIVE** (consumed but historically valuable), or **DELETE** (pure duplicate, no unique content).

1. **`context/instructions/` — consumed coding instructions and research prompts.** Likely candidates for archive:
   - `Research_3_Prompt.md` — Research 3 complete; superseded by `Research_4_Automation_Engine_Brief.md`, `Research_8_Device_Model_Brief.md`, `Research_6_Integration_Runtime_Brief.md`, `Research_5_Configuration_Brief.md` patterns.
   - `Cowork_Research_Pipeline_Bootstrap.md` — One-shot session prompt, likely fully consumed.
   - `Cowork_Research8_Processing_Bootstrap.md` — One-shot prompt; Research 8 done.
   - `M3.6e.2_Admin_Endpoints_ArchUnit_Rules.md` — Coding instruction for M3.6e.2, milestone shipped at `76288af`.
   - Brief files for Research 4, 6, 8 — KEEP if still useful as references for the next round of brief production, otherwise archive. (Research 6 brief was the first to embed type inventories; Research 5 brief is the first to embed `module-info.java` — these may be worth keeping as exemplars.)

2. **`context/pre-verifications/`** — pre-verification documents authored before specific milestones; consumed when the milestone landed. Likely candidates for archive:
   - `WU-M3.6d-b.md` — M3.6d-b shipped at `dfb045e`; pre-verification consumed.
   - Any other `WU-*.md` files for milestones already in DONE state per `phase-3-milestone-backlog.md`.

3. **`context/audits/`** — closed audits. Most are historically valuable and should be KEPT as the archive of past investigations. Sweep only for actual duplicates. Be especially careful with `AUDIT_2026-05-20.md` and `2026-04-11_m2.5-arch-debt-retrospective.md` — these are referenced by the freshness preflight and by the PM skill.

4. **`context/handoff/`** — handoff files like the 2026-05-22 continuation prompt. The continuation prompt that started today's session is at `context/handoff/2026-05-22_continuation_prompt.md`. It is consumed (today's session produced Research 4 v3, Research 6 brief, Research 6 v1 assessment, the `module-info.java` rule encoding, Research 5 brief). **This file should be archived.** The current Cowork session prompt (this file you are reading) will eventually share its fate.

5. **`context/decisions/`** — decisions registers. KEEP all (active registers, not consumed artifacts).

6. **`context/lessons/`** — lessons-learned files. KEEP all.

7. **`context/protocols/`** — operational protocols (WUCP, etc.). KEEP all.

8. **Old continuation prompts in `context/handoff/`** — check for any `*_continuation_prompt.md` or similar one-shot session prompts that have been consumed. Archive them.

### Sweep procedure

For each candidate file:

1. Read the file (or at least its header + structure).
2. Determine: does this file's content survive elsewhere (PROJECT_SNAPSHOT, pm-handoff, an assessment doc)?
3. If yes: archive it. Mkdir `archive/` if needed; preserve folder structure under it (e.g., `context/instructions/archive/Research_3_Prompt.md`).
4. If no: KEEP it and note in your summary why it's still load-bearing.
5. **Track every move in a session log entry** that you'll add to `PROJECT_SNAPSHOT.md` at the end.

**Do not archive any of these (load-bearing):**

- Any file referenced by `pm-handoff.md` Next Tasks or Open Risks
- Any file referenced by the active `phase-3-milestone-backlog.md`
- Any of today's deliverables (Research 5 brief, Research 6 v1 assessment, Research 4 v3 assessment, Knowledge Primer, strategic-context-map.md, master-release-plan.md)
- Any `MODULE_CONTEXT.md` or `module-info.java` file in `homesynapse-core`
- The freshness preflight, the WUCP protocol, the coding-instruction-format reference
- The research-agenda.md (active queue)
- Any `assessments/` file — those are the canonical record
- Files dated within the last 7 days unless clearly consumed (continuation prompts and one-shot bootstraps are an exception — they are designed to be consumed immediately)

After the sweep, re-run the freshness preflight. Expect PASS on all checks if you only moved files (no skill-file edits in this sweep).

---

## Phase 3: Research 5 Processing Prep (while waiting for the doc)

The Research 5 brief has already been issued. The Claude Project deep-research mode typically takes 30-90 minutes. Use this window to build interpretation context.

### Files to read for Research 5 interpretation

In addition to the orientation reading from Phase 1, read these:

1. **`homesynapse-core/config/configuration/MODULE_CONTEXT.md`** — the verified 22-type inventory. The Research 5 brief embedded the type-inventory subset; reading the full MODULE_CONTEXT gives you the cross-module contracts, gotchas, and Phase 3 notes that will help you spot discrepancies between researcher claims and reality.

2. **`homesynapse-core/config/configuration/src/main/java/module-info.java`** — verbatim, 19 lines. The brief embedded it, but read the canonical file to confirm.

3. **Doc 06 (Configuration System)** at `homesynapse-core-docs/design/HomeSynapse_Core_Design_06_Configuration_System_v1.md` (or whichever the latest filename is) — the governing design doc. The Research 5 brief asks questions that target Doc 06 §3.3 (hot reload), §3.4 (secrets), §3.6 (validation severity), §3.7 (migration), §8.4 (ConfigurationAccess), §8.5 (SecretStore), §8.6 (SchemaRegistry). Have these sections at hand for cross-reference.

4. **`context/assessments/2026-05-22_Research_6_PM_Assessment.md`** — re-read NQ-1 (SecurityServices aggregator), NQ-2 (schema version reconciliation), and the F1-F8 fabrication catalogue. These directly bear on Research 5 §Q3 and §Q6.

5. **`context/assessments/2026-05-22_Research_4_PM_Assessment.md` v3 addendum** — re-read AMD-52's "Automation event types in `com.homesynapse.event` (flat package)" — this is the precedent for any new config-domain events in Research 5.

### What to watch for in Research 5

The fabrication pattern across the four prior research documents:

- **Research 3:** package names (`com.homesynapse.testing` vs actual `com.homesynapse.test`)
- **Research 4:** type names (`Run` vs actual `RunContext`, fabricated permit names — ~29 errors in §7)
- **Research 8:** package names (`com.homesynapse.statestore` vs `com.homesynapse.state`)
- **Research 6:** JPMS module names (`com.homesynapse.event.model`, `state.store`, `configuration` — eight F1-F8 fabrications)

The Research 5 brief embedded both layers (verified `module-info.java` text + complete configuration MODULE_CONTEXT type inventory + flagged that `ConfigurationChangeListener`, `SecureCredentialBundle`, `configSchemaMajor/Minor` do NOT currently exist). **Specific things to verify in the Research 5 doc:**

1. **Package name:** every reference must be `com.homesynapse.config` (NOT `com.homesynapse.configuration`). The F4 fabrication from Research 6 was exactly this — confirm Research 5 doesn't inherit it.

2. **`ConfigurationValidationException` location:** it lives in **`com.homesynapse.event`**, not `com.homesynapse.config` (verified by source import). If Research 5 places it in the config module, that's a fabrication to flag.

3. **`ConfigMigrator` shape:** existing `fromVersion() → int`, `toVersion() → int`, `migrate(Map<String, Object>) → MigrationResult`. If Research 5 proposes changes here, they must be AMDs against this exact shape — not against a fabricated alternative.

4. **`ConfigModel.schemaVersion`** is a **single int**, not a (major, minor) pair. If Research 5 silently assumes a pair without proposing the breaking change, flag it.

5. **`Severity` enum is 3 values:** `FATAL`, `ERROR`, `WARNING`. Locked. If Research 5 proposes a 4th severity, that's a scope violation.

6. **`SchemaRegistry` parameters are JSON-text Strings:** not a typed JsonSchema library type. If Research 5 proposes typed parameters, that's a public-API change requiring AMD justification.

7. **YAML library and JSON Schema validator dependency choices:** these are net-new and should be cross-referenced against `gradle/libs.versions.toml` (current dependencies) and the codebase Gotchas (Jackson 2.18.6 is the floor per LTD-19). Library choice has a JPMS-module-name component — verify the proposed library has a stable Automatic-Module-Name or a real module-info.

8. **Threat-model statement:** Research 5 should produce a defended threat-model paragraph. If the document hand-waves ("we encrypt secrets because security"), that's a §5 caveat to surface.

9. **Cross-research coherence:**
   - Research 5 §Q3 (`SecureCredentialBundle`) must reconcile with Research 6 REC-45's `SecurityServices` aggregator (NQ-1).
   - Research 5 §Q6 (schema versioning) must reconcile with Research 6 REC-41's `migrate(fromMajor, fromMinor, toMajor, toMinor, ...)` and Research 6 NQ-2.
   - Research 5 §Q4 (`ConfigurationChangeListener`) must reconcile with the existing `ConfigChangeSet` record's `ReloadClassification` field — the listener and the classification are two halves of the same protocol.

### Patterns to be prepared to probe deeper on

These are the questions Research 5 is *most likely to underanswer* — be ready to push back:

- **Threat model.** Researchers tend to copy HA's `secrets.yaml` (plaintext, deliberate) or wave at "AES-256-GCM" without articulating against whom. Demand specificity.
- **YAML library JNI/native-memory cost on Pi 4.** SnakeYAML loads YAML 1.2 fully in-memory; for a 500-line config the heap impact is small, but on a 1 GB Pi 4 with concurrent JNI (sqlite-jdbc), measure rather than assume.
- **Reload atomicity under concurrent writes.** If two REST API clients write simultaneously, what wins? `fileModifiedAt` is an optimistic-concurrency token but the contention story isn't articulated.
- **Schema composition timing.** Integration schemas register at startup; what happens when a new integration's schema arrives mid-runtime (Phase 4+ feature, but the contract may need to admit it)?
- **The configuration-vs-event-sourcing tension** (§Q7). Researchers often skip this entirely. The canonical answer matters for operator mental model and for migration tooling.

---

## Phase 4: When Research 5 Lands

Apply the standard 6-step protocol (Steps A-F per `project-manager/SKILL.md`):

- **Step A — Format compliance.** Verify all `[M]` sections present, executive summary takes positions, REC numbering correct (starts REC-53), AMD numbering correct (starts AMD-64).
- **Step B — Executive summary critique.** Are the verdicts defensible? Is the single highest-impact finding called out?
- **Step C — Platform deep dives.** Each subsection has primary-source quote + URL + pain point + lesson?
- **Step D — Per-REC assessment.** For each REC: ACCEPT / MODIFY / REJECT, with rationale tied to verified MODULE_CONTEXT facts.
- **Step E — §7 source verification.** This is the critical step. For every type/package/module name in §7, verify against the actual codebase. Use the F1-F8 catalogue from Research 6 v1 as the model — produce an equivalent table for Research 5.
- **Step F — Open questions for Nick.** Strategic / scope decisions that need Nick's call. PM verifies what's source-verifiable; only escalate what genuinely requires human judgment.

Write the assessment as `context/assessments/2026-MM-DD_Research_5_PM_Assessment.md`. Model on Research 8 v2 (the cleanest prior format). Quality over quantity — Research 8's assessment was crisp and load-bearing; Research 4 v3 was longer but the v3 addendum is what mattered.

After the assessment, update `PROJECT_SNAPSHOT.md` Recent Session Log + `pm-handoff.md` Next Tasks + run the freshness preflight to confirm PASS.

---

## Architectural Invariants to Enforce

Non-negotiable constraints that Research 5 recommendations must not violate:

- **DECIDE-04:** No ServiceLoader. Factories instantiated directly. Constructor injection. This affects `ConfigMigrator` registration (must be an explicit list, not classpath-scanned), `SchemaRegistry` schema sources (must be explicit, not discovered).
- **LTD-04:** ULID identity system. Typed wrappers. The configuration system doesn't allocate new ULID types in Phase 2, but if Research 5 proposes one (e.g., `SecretId`), it must follow the typed-wrapper pattern.
- **LTD-08 / LTD-19:** Jackson JSON for all serialization. Jackson 2.18.6 floor. If Research 5 proposes a non-Jackson YAML/JSON library, must defend why and how it coexists.
- **LTD-11:** No `synchronized` anywhere. ReentrantLock only. Affects the hot-reload listener implementation.
- **AMD-26:** All sqlite-jdbc operations on platform threads. Affects `SecretStore` if backed by SQLite (Doc 06 leaves storage unspecified — Research 5 may propose).
- **One-flat-package invariant per module** — configuration module is `com.homesynapse.config`, single flat package. No subpackages.
- **Event naming convention:** legacy underscore, new dot-separated. Both permanent.

---

## Key Files for Context Loading

```
nexsys-hivemind/
├── context/
│   ├── handoff/pm-handoff.md                    ← PM state, governance
│   ├── status/PROJECT_SNAPSHOT.md               ← Project state hub
│   ├── planning/research-agenda.md              ← Research queue + format spec (extended 2026-05-22 with module-info.java embed rule)
│   ├── assessments/
│   │   ├── 2026-05-22_Research_8_PM_Assessment.md  ← FINAL (template for Research 5 v1)
│   │   ├── 2026-05-22_Research_4_PM_Assessment.md  ← v3 (PM-verified)
│   │   └── 2026-05-22_Research_6_PM_Assessment.md  ← v1 (F1-F8 fabrication catalogue model)
│   └── instructions/
│       ├── Research_5_Configuration_Brief.md       ← The brief issued to Claude Project
│       └── Research_6_Integration_Runtime_Brief.md ← Reference for embed pattern (type inventory + module-info)
├── project-knowledge/
│   ├── HomeSynapse_Knowledge_Primer.md          ← Architectural mental model (corrected 2026-05-22)
│   ├── HomeSynapse_Navigation_Index.md          ← File/doc navigator
│   └── Decisions_Quick_Reference.md             ← Locked decisions (LTD/DEC)
└── project-manager/
    ├── SKILL.md                                 ← PM operating procedures (Step 3 expanded 2026-05-22)
    └── references/
        ├── coding-instruction-format.md         ← Coder-brief template (Files-to-Read extended 2026-05-22)
        ├── freshness-preflight.md               ← 10-check session-start gate
        └── ...
```

---

## End-of-Session Deliverables

1. **Hygiene sweep summary** — list of files archived, files kept (with reason), files deleted (with reason). Updated to `PROJECT_SNAPSHOT.md` session log.
2. **Research 5 v1 PM Assessment** — at `context/assessments/2026-MM-DD_Research_5_PM_Assessment.md` (if doc landed during session).
3. **Updated `pm-handoff.md` Next Tasks** — with Nick decisions queued for Research 5 NQs (if any), Research 7 brief next (Research 5 is the last MEDIUM-priority pre-M4 research; Research 7 is the only remaining queue item).
4. **Final freshness preflight: PASS.**

# Cowork Session Prompt — Post-Research Synthesis & Architecture Integration

You are the PM for NexSys/HomeSynapse Core. You operate in **Mode 3 (Director)** for Phase 3 implementation, but this session is meta: you are NOT producing coding instructions. Instead, this session has a single primary deliverable:

**Synthesize the completed research pipeline (Research 2–8, six documents + six assessments) with the in-flight architectural state, resolve the 17 independent + 1 dependent strategic decisions still awaiting Nick, and produce a comprehensive post-research integration plan that defines how the M4/M6/M7/M8/M9/M10/M11 amendment ratification + sub-milestone decomposition will proceed.**

The output is a planning document Nick will use to authorize subsequent coding-instruction-production sessions (one per milestone). This session does NOT produce coding instructions, does NOT modify code, and does NOT ratify AMDs unilaterally — every AMD ratification still requires Nick's explicit sign-off in subsequent governance sessions. What this session DOES do is land the cross-research synthesis, the per-milestone impact analysis, and the ratification-order-with-dependencies plan so all downstream work can sequence cleanly.

Invoke the `nexsys-project-manager` skill to load your full operating procedures.

---

## State at Session Start

**Project:** HomeSynapse Core — local-first, event-sourced smart home runtime. Java 21 on Amazon Corretto, targeting Raspberry Pi 4/5. Multi-module Gradle project with JPMS enforcement. SQLite WAL mode. Virtual threads.

**Phase:** Phase 3 (implementation). **M3.6 COMPLETE** at commit `76288af`. **M3.7 NEXT** — coding instruction already issued in a prior Cowork session (at `context/instructions/M3.7_E2E_Integration_Tests.md`), awaiting Coder execution. **M4.0 planned after M3.7 commits.**

**Research pipeline status — COMPLETE for the pre-M5 window:**

| Research | Title | Target | Status | Assessment | Strategic Decisions Awaiting Nick |
|---|---|---|---|---|---|
| Research 2 | Smart Home Entity Modeling | M4 (Device Model) | COMPLETE (baseline, pre-pipeline) | processed pre-PM | 0 (all REC-01..REC-12 absorbed into Research 8 v2) |
| Research 3 | Integration Testing Patterns | M3.7 (E2E ITs) | COMPLETE | `2026-05-22_Research_3_PM_Assessment.md` | 0 (all REC-13..REC-22 accepted; feeds M3.7) |
| Research 4 | Automation Engine Architecture | M7+M8 | COMPLETE (v3) | `2026-05-22_Research_4_PM_Assessment.md` | **4 (DQ-1/2/3/5)** |
| Research 5 | Configuration System | M6 | COMPLETE (v2 FINAL post-Nick) | `2026-05-22_Research_5_PM_Assessment.md` | **1 (REC-56/AMD-67 deferred on R6 REC-41/NQ-2)** |
| Research 6 | Integration Runtime Supervisor | M9 | COMPLETE (v1) | `2026-05-22_Research_6_PM_Assessment.md` | **6 (NQ-1..6)** |
| Research 7 | REST/WebSocket API | M10+M11 | COMPLETE (v1) | `2026-05-22_Research_7_PM_Assessment.md` | **7 (NQ-1..7)** |
| Research 8 | Device Model Implementation | M4.0 | COMPLETE (v2 FINAL) | `2026-05-22_Research_8_PM_Assessment.md` | 0 (Nick-verified) |

**Total open strategic decisions:** 18 (17 independent + 1 dependent on R6 NQ-2 resolution).

**Global allocations:** RECs allocated through REC-75. AMDs allocated/proposed through AMD-85 (AMD-47/AMD-61 withdrawn; AMD-64/AMD-65 retired post-R5 v2; AMD-67/AMD-71 deferred). Next new RECs start REC-76; next new AMDs start AMD-86.

**Repos to orient from:**
- `nexsys-hivemind` — PM/governance repo (selected folder). Contains all 6 assessments + 6 research briefs + governance + planning.
- `homesynapse-core` — Java codebase. MODULE_CONTEXT.md authoritative for type inventories; `module-info.java` authoritative for JPMS module names; `gradle/libs.versions.toml` authoritative for dependency versions.
- `homesynapse-core-docs` — design documents (Doc 01–14), amendments register, research archive.

---

## Phase 1: Mandatory Orientation

Per the `nexsys-project-manager` skill, **run the freshness preflight first**. Expected result: **PASS on all 10 checks** (last session ended PASS; no skill-file edits between then and now). Any deviation → escalate to Nick.

After preflight, read these in order. This is a large reading set — budget ~45 minutes for read-through. Skim where the assessment has already digested the source; read carefully where you need to verify a specific claim.

### Tier 1: Research assessments (PM-verified canonical takes) — READ IN FULL

1. `context/assessments/2026-05-22_Research_8_PM_Assessment.md` — M4 (Device Model) — v2 FINAL. 8 RECs (REC-23..30). 3 AMDs ratified (AMD-44/45/46; AMD-47 withdrawn). Foundational for M4.0.
2. `context/assessments/2026-05-22_Research_4_PM_Assessment.md` — M7+M8 (Automation Engine) — v3 with MODULE_CONTEXT-verified addendum at bottom. 10 RECs (REC-31..40). 5 AMDs proposed (AMD-48..52). **DQ-1/2/3/5 awaiting Nick.**
3. `context/assessments/2026-05-22_Research_6_PM_Assessment.md` — M9 (Integration Runtime) — v1. 12 RECs (REC-41..52). 10 AMDs proposed (AMD-53..58, 60, 62, 63; AMD-61 withdrawn). **NQ-1..6 awaiting Nick.** F1-F8 fabrication catalogue (JPMS module-name fabrications — corrected).
4. `context/assessments/2026-05-22_Research_5_PM_Assessment.md` — M6 (Configuration System) — v2 FINAL post Nick review. v1 body + v2 Addendum at bottom (canonical). 9 RECs (REC-53..61). 4 active AMDs (AMD-66/68/69/70), 2 deferred (AMD-67/71), 2 retired (AMD-64/65). **AMD-67 deferred on R6 REC-41/NQ-2.**
5. `context/assessments/2026-05-22_Research_7_PM_Assessment.md` — M10+M11 (REST/WebSocket API) — v1. 14 RECs (REC-62..75). 14 AMDs proposed (AMD-72..85). **NQ-1..7 awaiting Nick.** Grade C-. 15 §7 fabrications catalogued. **REC-63 is the only REJECT** in the pipeline.

### Tier 2: Research source documents — SKIM FOR CONTEXT (assessment is canonical)

Only read these directly if you need to verify a specific claim the assessment cites. The assessment-side fabrication catalogues + dispositions are the authoritative take.

- Research 8 source: not separately filed (processed pre-archive)
- Research 4 source: not separately filed
- Research 6 source: not separately filed
- Research 5 source: not separately filed (the brief is at `context/instructions/Research_5_Configuration_Brief.md`)
- Research 7 source: in the user's chat history (the document Nick uploaded — `compass_artifact_wf-e4945445-...md`)

### Tier 3: Governance + canonical references — READ THE RELEVANT SECTIONS

- `project-knowledge/HomeSynapse_Knowledge_Primer.md` — current architectural mental model. Pay attention to §Module Map (verified module list + one-flat-package per module invariant) and §Critical Gotchas (M3.6e.2/M3.6e.1/M3.6c/M3.6d-a corrections).
- `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md` — LTD-01 through LTD-19. **Skim for LTDs cited in any research assessment** — LTD-08 (Jackson 2.18+), LTD-09 (YAML 1.2 + SnakeYAML Engine + networknt JSON-schema-validator), LTD-11 (no external message broker), LTD-15 (SLF4J), LTD-19 (event payload serialization).
- `homesynapse-core-docs/governance/Architecture_Invariants_v1.md` — INVs cited in assessments. Especially INV-SE-02 (auth mandatory), INV-CE-01 (config file is source of truth), INV-CE-02 (zero-config first run), INV-CE-03 (schema is the contract), INV-PR-01 (Pi 4 constraints), INV-RF-01 (integration isolation), INV-ES-01/04 (event immutability + write-ahead).
- `context/decisions/phase-3-cross-module-decisions.md` — D-01 through D-12 (D-09..D-12 are the M3.7 scoping decisions logged by the parallel Cowork session).
- `homesynapse-core/gradle/libs.versions.toml` — current dependency catalog (Jackson 2.18.6, Javalin 6.7.0, SnakeYAML Engine 2.9, json-schema-validator 1.5.6, SLF4J 2.0.17, AssertJ 3.27.7, ArchUnit 1.4.0, JUnit 5.14.3).
- `context/handoff/pm-handoff.md` — current Next Tasks list with all NQs queued. Re-read after Tier 1 to refresh the "what's pending" picture.
- `context/status/PROJECT_SNAPSHOT.md` — current operational state, latest commit `76288af`, M3.6 COMPLETE, M3.7 NEXT.

### Tier 4: Design docs touched by research — READ THE SECTIONS CITED IN ASSESSMENTS

These are the governing design docs for the affected subsystems. You don't need to read them cover-to-cover, but you should have the cited sections at hand when working through the synthesis in Phase 3+.

- `homesynapse-core-docs/design/02-device-model-and-capability-system.md` (Research 8 → M4) — §3 architecture, §4 data model, §8 interfaces.
- `homesynapse-core-docs/design/05-integration-runtime.md` (Research 6 → M9) — §3.4 (health FSM), §3.6 (graceful shutdown), §3.7 (exception classification), §3.13 (Kahn's), §3.14 (planned restart), §8.1-8.2 (interfaces + runtime types).
- `homesynapse-core-docs/design/06-configuration-system.md` (Research 5 → M6) — §3.3 (reload), §3.4 (secrets), §3.6 (validation severity), §3.7 (migration), §8.4-8.6 (interfaces).
- `homesynapse-core-docs/design/07-automation-engine.md` (Research 4 → M7+M8) — §3 trigger/condition/action pipeline, §4 RunContext + RunCausalChain (AMD-25 already integrated).
- `homesynapse-core-docs/design/09-rest-api.md` (Research 7 → M10) — §3.2 (five planes), §3.3 (request pipeline), §3.4 (command lifecycle), §3.5 (pagination), §3.7 (ETags), §3.8 (RFC 9457), §4.3-4.5 (command endpoints), §8 (interfaces).
- `homesynapse-core-docs/design/10-websocket-api.md` (Research 7 → M11) — §3.3 (message protocol), §3.4 (subscription), §3.7 (backpressure), §3.8 (keepalive), §3.9 (reconnection), §5 (close codes).

---

## Phase 2: Deliberate the 18 Strategic Decisions with Nick

Each decision below is documented in detail in its respective assessment. **You have the PM recommendation for each from the prior assessment work.** Your job in this phase is:

1. Present each decision to Nick concisely (one decision at a time or grouped into a single message — your judgment based on flow).
2. Recommend the PM-default per the assessment.
3. Capture Nick's actual decision (which may agree, override, or modify the PM recommendation).
4. Record every decision in `context/decisions/phase-3-cross-module-decisions.md` as new D-XX entries (continuing from D-12).

Use the `AskUserQuestion` tool to present grouped decisions to Nick for fast resolution. Suggested groupings (4 batches):

### Batch A: Research 8 confirmation + Research 4 strategic calls (5 decisions)

- **R8-CONFIRM:** Re-confirm all REC-23..30 dispositions per Research 8 v2 FINAL (no change expected — was Nick-verified). PM expectation: confirmation.
- **R4-DQ-1:** PresenceTrigger vs ZoneTrigger — PROMOTE existing PresenceTrigger (PM rec) or add separate ZoneTrigger permit?
- **R4-DQ-2:** ActivateSceneAction fate — RENAME to `InvokeAutomationAction` + promote to Tier 1 (PM rec), or keep as-is?
- **R4-DQ-3:** Pending Command Ledger advancer — SAME `DispatchingProjectionAdvancer` with separate handler registrations (PM rec), or separate advancer?
- **R4-DQ-5:** ZoneTrigger scope — M8 (PM rec, depends on presence/location infra), or M7?

### Batch B: Research 6 strategic calls (6 decisions)

- **R6-NQ-1:** `IntegrationContext` field count — AGGREGATE via `SecurityServices` (PM rec, keeps record at 11 fields), or grow per-service?
- **R6-NQ-2:** Schema versioning — KEEP both, rename existing to `descriptorSchemaVersion` + add `configSchemaMajor`/`configSchemaMinor` (PM rec, two distinct concerns), or change `ConfigMigrator` to `(major, minor)` directly?
   - **CRITICAL: this decision drives Research 5 REC-56/AMD-67.** If you adopt the unified `(major, minor)` shape from R5 REC-56, that's a different answer than the R6 PM recommendation here. Reconcile explicitly.
- **R6-NQ-3:** REC-47 capability identity — sealed `Capability` permit class + existing `CapabilityInstance` (PM rec), or invent `CapabilityId`?
- **R6-NQ-4:** REC-47 storage model — NO new SQLite table; project to `Entity.capabilities` (PM rec, per R8 design boundary), or new capability table in state-store?
- **R6-NQ-5:** REC-49 — REJECT (PM rec — existing `HealthParameters.maxRestarts/restartWindow` already covers), or accept with rename?
- **R6-NQ-6:** Default restart intensity for radio-based adapters — keep 1/60s global default + per-descriptor override (PM rec), or different default?

### Batch C: Research 5 reconciliation (depends on R6-NQ-2)

- **R5-REC-56:** Resolution depends on R6-NQ-2 outcome.
   - If R6-NQ-2 = "keep two distinct concerns" → R5 REC-56 stays single-int + new pair fields; AMD-67 lands with that shape.
   - If R6-NQ-2 = "unified `(major, minor)` everywhere" → R5 REC-56 collapses `schemaVersion` to the pair; AMD-67 lands per R5 v2's clean unified design.
   - **PM recommendation:** unified `(major, minor)` — eliminates the conceptual seam between file-schema and adapter-schema versioning. But this is a Nick call.

### Batch D: Research 7 strategic calls (7 decisions)

- **R7-NQ-1:** REC-63 vs Doc 09 §4.3-§4.5 — KEEP existing surface, add `CommandRequest.timedInteractionMs` field (PM rec, REC-63 collapses), or replace with REC-63 proposal?
- **R7-NQ-2:** `Capability` enum naming clash with device-model sealed `Capability` interface — RENAME to `ApiKeyScope` (PM rec), or accept the clash?
- **R7-NQ-3:** `ProblemType.typeUri()` URL scheme — ADOPT `urn:homesynapse:problem:<slug>` (PM rec, more RFC-idiomatic), or stay with `https://homesynapse.local/problems/<slug>`?
- **R7-NQ-4:** REC-67 webhook DLQ — SEPARATE `WebhookDeliveryStore` + `/internal/webhook-failures` (PM rec, different failure types), or share `/internal/dlq` with subscriber DLQ?
- **R7-NQ-5:** REC-70 WsCloseCode collisions — conservative renumbering per PM proposal (keep existing 5; add INSUFFICIENT_SCOPE 4402, FRAME_TOO_LARGE 4413, SERVER_SHUTDOWN 4503; drop conflicting proposed AUTH_FAILED 4401/PING_TIMEOUT 4408/SUBSCRIPTION_CONFLICT 4409), or alternative numbering?
- **R7-NQ-6:** REC-72 coalescing key — `(entityId, attributeKey)` (PM rec, preserves per-attribute LWW), or `entityId` only?
- **R7-NQ-7:** REC-64 `@Capability` annotation naming — RENAME to `@CapabilityType` (PM rec, same clash mitigation as R7-NQ-2), or accept clash?

### Documenting decisions

For each Nick decision, append a new entry to `context/decisions/phase-3-cross-module-decisions.md`:

```
### D-XX (YYYY-MM-DD) — <one-line title>
**Source:** Research <N> <NQ/DQ-N>
**Decision:** <Nick's actual call>
**PM Recommendation was:** <recommendation>
**Rationale:** <Nick's rationale or PM's if Nick accepts PM rec>
**Affects:** <REC list>, <AMD list>, <milestone>
**Cross-research dependencies:** <e.g., "couples to R5 REC-56" or "none">
```

The next decision number after D-12 is D-13. Expect to land D-13 through ~D-30 in this phase.

---

## Phase 3: Produce the Post-Research Synthesis Document

Produce a new governance document at `context/synthesis/2026-05-22_Post_Research_Synthesis.md` (create the `synthesis/` directory if needed). This is the canonical PM-side summary of what the research pipeline tells us about the system.

### Required sections

1. **Headline + Pipeline Summary.** One-paragraph overall verdict. Table summarizing all 6 research items + their grades + their primary deliverables. Total RECs (53–75 range), total AMDs proposed (47+, accounting for withdrawals + retirements + deferrals).

2. **Strategic Decisions Resolved.** Numbered list of D-13..D-XX with the outcome of each Phase 2 decision. Format: one line per decision, with the actual outcome (not the recommendation).

3. **System-Wide Constraints Now Locked.** Aggregate the architectural invariants that the research pipeline has either confirmed or extended. Examples to look for:
   - **`(major, minor)` schema versioning as a system-wide pattern** (assuming R6-NQ-2 + R5 REC-56 resolve to unified shape) — applies to file-schema + adapter-config-schema + potentially future versioned protocols.
   - **One-flat-package per module** — confirmed and re-confirmed across R5 v2 F6 + R7 v1 F12 fabrications. Add to research-agenda.md §2 CONSTRAINTS if not already.
   - **`com.homesynapse.event` flat package as the domain-event landing site** per AMD-52 precedent + R5 AMD-70 + R6 AMD-56 + (if accepted) R7 event additions.
   - **INV-SE-02 absolute** — every research touching auth has reinforced this. Document the surface area now defended.
   - **Bcrypt-then-cache as the canonical auth performance pattern** (R7 REC-71).
   - **Three-stage backpressure (NORMAL → BATCHED → COALESCED) at thresholds 256/1024/4096 frames or 2s/5s/30s lag** as the canonical WebSocket model (R7 REC-72).

4. **Cross-Research Coherence Matrix.** Table form. Rows: pairs of research interactions. Columns: surface, state, who depends on whom, gate condition. Examples:
   - R5 REC-56 ↔ R6 REC-41/NQ-2 (schema versioning lockstep) — RESOLVED via D-XX (insert outcome).
   - R5 REC-57 ↔ R6 REC-45/NQ-1 (`SecureCredentialBundle` vs `SecurityServices` aggregator) — RESOLVED via D-XX.
   - R5 REC-55 ↔ existing `ConfigChangeSet.ReloadClassification` — ALIGNED (no Nick decision needed).
   - R6 REC-47 ↔ R8 REC-23/REC-26 (capability storage at `Entity` not new SQLite table) — RESOLVED via R6-NQ-4.
   - R7 REC-65 prefix filter ↔ R4 AMD-52 automation events + R5 AMD-70 config events + R6 AMD-56 integration events — ALIGNED (no Nick decision needed; prefix filter naturally covers all).
   - R7 REC-63 ↔ Doc 09 §4.3-§4.5 existing command surface — RESOLVED via R7-NQ-1.

5. **Outstanding Architectural Risks.** Enumerate the risks that the research pipeline surfaced but did not fully resolve. Each risk: (a) source research item, (b) what it threatens, (c) the spike or empirical work needed to close it, (d) target milestone. Examples:
   - **Spike R5-Q1 (SnakeYAML Engine throughput on Pi 4)** — REC-53 / M6 / unverified bug-budget for parsing performance.
   - **Spike R5-Q2 (Argon2id 64 MiB/3 iter/4 lanes on Pi 4 Cortex-A72)** — REC-58 / M6 / 250–700 ms estimate needs confirmation.
   - **Spike R5-Q3 (networknt 1.5.6 memory residency)** — REC-54 / M6 / 256 MiB heap question.
   - **Spike R7-Q1 (server-side filter scaling)** — REC-65 / M11 / 100 ev/s × 20 subscribers diverse filters target.
   - **Spike R7-Q2 (WebSocket per-connection memory residency)** — M11 / <100 KB target.
   - **Spike R7-Q3 (bcrypt validation latency at cost 10)** — REC-71 / M10 / <50 ms p99 target on Cortex-A72.
   - **Spike R6 (Zigbee/Matter restart frequency under normal operation)** — REC-49/NQ-6 / M9.

6. **Lessons for Future Research Briefs.** Codify the meta-lessons accumulated across the 6 assessments. Examples:
   - **Embed `libs.versions.toml` verbatim** (R5 v2 F1 lesson).
   - **Embed `HomeSynapse_Core_Locked_Decisions.md` relevant entries verbatim** (R5 v2 F1 deeper lesson).
   - **Embed `Architecture_Invariants_v1.md` relevant entries verbatim** (R5 v2 F8 lesson — would have closed R7 §1 framing).
   - **Require the researcher to QUOTE verbatim blocks back in §7** (R7 v1 meta-lesson — would have caught F12 catastrophic JPMS fabrication).
   - **Consider splitting multi-module research items per module** (R7 v1 meta-lesson — fabrication count correlates with module breadth).
   - **§5.4 explicit conflict-with-inventory disclosure as mandatory** (R5 v2 + R7 v1 demonstrated value).
   - **Cross-research coherence checks must be embedded in every brief** (R5/R6/R7 all carried these; the pattern works).
   - **Apply Java mechanics review to every proposed type shape** (R5 v2 F7 + R7 v1 F10 lessons — broken generics + invalid HashMap keys).

   Update `context/planning/research-agenda.md` §2 CONSTRAINTS with these lessons codified.

---

## Phase 4: Per-Milestone Architecture Impact

Produce a new document at `context/synthesis/2026-05-22_Per_Milestone_Impact.md`. This is the per-milestone "what changes in this milestone vs the original phase-3-milestone-backlog skeleton" summary.

For each of M4, M6, M7, M8, M9, M10, M11:

### Per-milestone structure (repeat for each)

```
## M<N> — <Subsystem Name>

**Original backlog scope:** <one-sentence reference to phase-3-milestone-backlog.md row>

**Research-driven amendments:**
| AMD # | Source REC | Scope | Status post-deliberation |
|---|---|---|---|
| AMD-XX | R<N> REC-YY | <scope> | RATIFIABLE / DEFERRED / RETIRED |

**New types to be created in this milestone** (post-AMD ratification):
- `TypeName` (record/interface/enum/class) in `com.homesynapse.<module>` — purpose

**Existing types to be modified:**
- `TypeName` — what changes (field add, signature change, etc.)

**New events** (with @EventType strings):
- `event.namespace.name` (state-changing / observability-only) — purpose

**New module-info.java edges:**
- `requires <module>` (transitive/non-transitive) — why

**New libs.versions.toml entries:**
- `<lib> = "<version>"` — why

**Spike prerequisites:** Spike R<N>-Q<n> (Pi 4 validation needed before AMD ratification).

**Cross-milestone dependencies:** "M<N> AMD-XX lands in lockstep with M<M> AMD-YY because <reason>".

**Sub-milestone decomposition (proposed):**
- M<N>.0a — <scope> (~XX LOC, ~Y h Coder time)
- M<N>.0b — <scope>
- ... (target each sub-WU at <~18 files / 6-8h Coder time per M3.6 lesson)

**Estimated total Coder time:** XX–YY hours.
```

### Milestone-by-milestone breakdown to populate

- **M4** — Device Model implementation. R8 v2 dispositions + R6-NQ-3/4 (capability identity + storage) + R7-NQ-1 outcome shape.
- **M6** — Configuration System. R5 v2 dispositions + R6-NQ-2 outcome (schema versioning) + R5 REC-56 final shape + 3 pre-M6 spikes.
- **M7** — Automation Engine (core). R4 v3 dispositions + DQ outcomes + AMD-48..52 ratification.
- **M8** — Automation Engine (advanced). R4 v3 DQ-5 outcome (ZoneTrigger placement) + dependencies on M7.
- **M9** — Integration Runtime. R6 v1 dispositions + R6-NQ-1..6 outcomes + R5 cross-research (SecurityServices/SecureCredentialBundle wiring) + R6 REC-52 internal types.
- **M10** — REST API. R7 v1 dispositions + R7-NQ-1..4/7 outcomes + auth subsystem (R7 REC-66/71/74) + bcrypt-then-cache (REC-71) + webhook subsystem (REC-67) + Spike R7-Q3.
- **M11** — WebSocket API. R7 v1 dispositions + R7-NQ-5/6 outcomes + filter expansion (REC-65) + backpressure codification (REC-72) + new WsMessage permits (REC-69/70/73) + Spike R7-Q1/Q2.

---

## Phase 5: AMD Ratification Plan with Sequencing

Produce a new document at `context/synthesis/2026-05-22_AMD_Ratification_Plan.md`. This is the dependency-ordered AMD ratification roadmap.

### Required sections

1. **Active AMD inventory.** Table of all AMDs proposed across the 6 research items, with status post-Phase-2 deliberation:
   - AMD-44/45/46 (R8) — RATIFIABLE
   - AMD-48..52 (R4) — RATIFIABLE pending DQ outcomes
   - AMD-53..58, 60, 62, 63 (R6) — RATIFIABLE pending NQ outcomes (AMD-61 withdrawn)
   - AMD-66, 68, 69, 70 (R5) — RATIFIABLE
   - AMD-67 (R5) — RATIFIABLE iff unified `(major, minor)` decision lands
   - AMD-71 (R5) — DEFERRED to M6 planning
   - AMD-72..85 (R7) — RATIFIABLE pending NQ outcomes; AMD subset for REC-63 collapses if R7-NQ-1 KEEP-existing wins

2. **Ratification dependency graph.** Visualize (in markdown) or table-list the AMDs that must land in lockstep:
   - R6 AMD-53/53b + R5 AMD-67 (schema versioning unified) — MUST RATIFY TOGETHER if unified path chosen
   - R6 AMD-57 (SecurityServices) + R5 AMD-68 (SecureCredentialBundle scoping) — natural ordering: R6 ratifies the aggregator field; R5 ratifies the bundle that's a member
   - R8 AMD-44 (EntityCategory on Entity) + R7 (later — if EntityCategory filter on `/api/v1/entities` is added) — additive
   - R4 AMD-51 (RunContext field replacement) + R7 (later — if automation events surface in REST history) — additive

3. **Ratification order (recommended).** Numbered sequence with rationale:
   1. **R8 AMD-44/45/46** (M4.0 enablers — foundational; no cross-research lockstep)
   2. **R6 AMD-53/53b + R5 AMD-67** (schema versioning lockstep)
   3. **R6 AMD-54/55/56/58/60/62/63** (independent R6 amendments)
   4. **R6 AMD-57 + R5 AMD-68** (security/credentials lockstep)
   5. **R5 AMD-66, AMD-69, AMD-70** (independent R5)
   6. **R4 AMD-48..52** (M7+M8 — depends on M4 AMD-44 for EntityCategory on Selector filtering per REC-35)
   7. **R7 AMD-66/68/69/70/71/72/73/74/75/76/77/78/79/80/81/82/83/84/85** (M10/M11 — last; depends on all upstream for cross-research coherence)
   8. **R5 AMD-71** (M6 directory layout — defer to M6 planning, not pre-M5 ratification)

4. **Per-milestone ratification gate.** For each milestone, the AMDs that must be RATIFIED before the coding-instruction-production session can begin.

5. **Subsequent Cowork sessions queued.** List the follow-up sessions Nick will need to run:
   - M4.0 coding-instruction-production session (after R8 + R6 + R5 schema-versioning AMDs ratify)
   - M6 coding-instruction-production session (after R5 AMDs ratify + 3 spikes complete)
   - M7 coding-instruction-production session (after R4 AMDs ratify)
   - M8 (after M7 ships)
   - M9 coding-instruction-production session (after R6 AMDs ratify)
   - M10 coding-instruction-production session (after R7 AMDs ratify + R7 Spike Q3 complete)
   - M11 coding-instruction-production session (after R7 AMDs ratify + R7 Spike Q1/Q2 complete)

---

## Phase 6: Update Governance Artifacts

After Phases 3-5 produce the three synthesis documents, integrate the outcomes into the live governance:

1. **`context/planning/master-release-plan.md`** — update the milestone-week mapping to reflect the per-milestone scope changes from Phase 4. Add a new "Post-Research Synthesis Sequencing" annotation section at the bottom explaining the AMD ratification order.

2. **`context/planning/phase-3-milestone-backlog.md`** — update the FUTURE rows for M4 through M11 with the sub-milestone decomposition from Phase 4. Each row should reference the relevant AMDs that land in that sub-milestone.

3. **`context/planning/research-agenda.md`** — extend §2 CONSTRAINTS with the Phase 3 §6 lessons (verbatim `libs.versions.toml`, verbatim LTD entries, verbatim INV entries, require quote-back in §7, consider per-module splitting, §5.4 mandatory contradiction disclosure, Java mechanics review). Mark the research-agenda's research queue as **CLOSED for pre-M5 window** — Research 7 was the last item.

4. **`context/decisions/phase-3-cross-module-decisions.md`** — Phase 2 decisions D-13..D-XX should already be appended from Phase 2 work. Re-verify the file is current with all 18 decisions.

5. **`context/handoff/pm-handoff.md`** — major update to Next Tasks:
   - Remove the "Nick: NQ-X strategic calls" task items (resolved this session).
   - Add new task items per milestone: "Nick: authorize M4.0 coding-instruction-production session" etc.
   - Keep the "Pre-M6 spikes" task.
   - Update the Research Pipeline Status table to mark all 6 research items as fully resolved (no pending NQs).

6. **`context/status/PROJECT_SNAPSHOT.md`** — append a new Recent Session Log entry summarizing this session's outcomes: 18 decisions resolved, 3 synthesis documents produced, governance artifacts updated, research pipeline now fully closed.

---

## Phase 7: Hygiene + Closeout

1. **Hygiene sweep candidates from this session:** the Research 5/6/7 briefs in `context/instructions/` are now fully consumed (assessments completed; NQs resolved). Archive them to `context/instructions/archive/`. Keep Research 4 brief if its DQ decisions reveal it's still useful as an exemplar; archive otherwise.

2. **Re-run the freshness preflight.** Expected: PASS on all 10 checks (no skill-file edits in this session).

3. **Final session log entry in PROJECT_SNAPSHOT.** Already covered in Phase 6 §6.

---

## End-of-Session Deliverables

1. **Resolved strategic decisions** — D-13..D-XX appended to `context/decisions/phase-3-cross-module-decisions.md` (~18 decisions).
2. **Post-Research Synthesis document** — `context/synthesis/2026-05-22_Post_Research_Synthesis.md`.
3. **Per-Milestone Impact document** — `context/synthesis/2026-05-22_Per_Milestone_Impact.md`.
4. **AMD Ratification Plan document** — `context/synthesis/2026-05-22_AMD_Ratification_Plan.md`.
5. **Updated governance artifacts** — master-release-plan.md, phase-3-milestone-backlog.md, research-agenda.md, pm-handoff.md, PROJECT_SNAPSHOT.md.
6. **Hygiene sweep done** — consumed research briefs archived.
7. **Final freshness preflight: PASS.**

---

## What This Session Does NOT Do

- It does NOT produce any coding instruction for M4.0, M6, M7, M8, M9, M10, or M11. Each of those is a separate downstream Cowork session that Nick authorizes after this synthesis lands.
- It does NOT ratify any AMD unilaterally. Every AMD ratification still requires Nick's explicit sign-off in subsequent governance sessions — this session produces the ratification *plan*, not the ratifications themselves.
- It does NOT modify any `homesynapse-core` source files. Only hivemind governance artifacts get touched.
- It does NOT modify any design document (`homesynapse-core-docs/design/`). The synthesis documents in `context/synthesis/` are the PM-side aggregation; design doc revisions are a separate workflow that may or may not happen depending on AMD ratification outcomes.
- It does NOT run any spike. The 6 spikes (R5 Q1/Q2/Q3, R7 Q1/Q2/Q3, R6 restart-frequency) are queued as pre-coding-instruction work for the relevant milestone sessions.
- It does NOT touch dual skill-location mirrors. No skill-file edits.
- It does NOT process new research. The pipeline is closed.

---

## Notes on Cowork Session Flow

This is the largest synthesis session in the project's history. Expect ~3-5 hours of Cowork interaction including ~45 min orientation reading + ~1 hour Phase 2 deliberation (interactive with Nick) + ~1-2 hours synthesis document production + ~30 min governance updates + closeout.

If the session boundary needs to fall partway through:
- **Best stopping points:** after Phase 2 (decisions resolved, synthesis not yet started), or after Phase 3 (synthesis document landed, per-milestone + AMD plan not yet started), or after Phase 5 (all three synthesis docs landed, governance updates not yet started).
- **If stopping after Phase 2:** update pm-handoff Current Task to "Synthesis docs (Phase 3-5) + governance updates (Phase 6) pending next session." Append decisions to D-XX register. Re-run preflight.
- **If stopping mid-Phase 3-5:** save partial synthesis documents with a status header noting they are DRAFT.

The PM should pace the session and surface "natural break point — continue or pause?" to Nick at each phase boundary if energy/context is flagging.

If anything in the scope above seems wrong or misaligned with Nick's intent, escalate immediately — the cost of producing the wrong synthesis is one wasted Cowork session; the cost of asking is one Cowork message.

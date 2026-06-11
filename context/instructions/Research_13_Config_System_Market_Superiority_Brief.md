<!--
file: context/instructions/Research_13_Config_System_Market_Superiority_Brief.md
purpose: Dispatchable research brief — Research 13: Config System Market Superiority (UX failure modes + runtime robustness). Gap-relative to the ratified M6 config baseline (AMD-66..71, Doc 06, Doc 15 fences, M6 charter).
audience: DOCS Project researcher (primary), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-10 (PM, Cowork) at Nick's direction (the post-M6.1 config research beat). Numbered Research 13 per Nick's 2026-06-10 numbering ruling (Research 12 = the consumed Zigbee de-risk return; numbering is append-only).
dispatch-target: the DOCS Claude Project (homesynapse-core-docs connector). RQ1/RQ2/RQ5 are web-evidence-heavy — WEB SEARCH IS REQUIRED. Fallback if the DOCS Project's web reach proves too shallow mid-run: SPLIT the work — a generic deep-research run gathers the raw external evidence (RQ1/RQ2/RQ5 source material only), and the DOCS Project run consumes it to produce the gap-relative findings + disposition table. The disposition pass must NEVER be the generic run.
rec-block: REC-130+ (re-derived from research-agenda.md at authoring: Research 12 consumed REC-120..129; REC-106..119 were the R7v2 reservation; high-water = 129)
baseline: homesynapse-core HEAD `9035110` (M6.1 COMPLETE whole: M6.1b `b7bc65c` + M6.1a `9035110`, gates GREEN 2026-06-10) · docs watermark AMD-87 · projectionVersion 5
-->

# RESEARCH BRIEF: Research 13 — Config System Market Superiority: UX Failure Modes + Runtime Robustness

*Target: HomeSynapse Core M6.2/M6.4 instruction obligations + future config AMDs + M10/M11/Doc 13 UI/cloud design inputs. Date: 2026-06-10.*

You are a market-evidence researcher for HomeSynapse Core, a local-first, event-sourced smart home runtime in Java 21. The M6 configuration block is **ratified and partially shipped** (M6.1 complete at `9035110`). Your task is NOT greenfield design. It is a **gap analysis**: catalogue how configuration systems fail real users and real runtimes across the smart-home market, then map every finding against the machinery HomeSynapse has **already ratified** — so the PM can see precisely what is covered, what becomes an M6.2/M6.4 instruction obligation, what warrants a future amendment, and what is post-MVP UI/cloud design input.

**The disposition table (§4b below) is the load-bearing deliverable.** A finding without a disposition row is unusable. A "gap" that is actually covered by ratified machinery you didn't read is worse than useless — it poisons the pipeline.

---

## 0. Authoritative state (do not work from memory)

- homesynapse-core HEAD: **`9035110`** — M6.1 COMPLETE (whole): M6.1b `b7bc65c` (config access/events; AMD-66/67/70 contract shapes) + M6.1a `9035110` (load/validate pipeline + gate-fix round 1). Full `./gradlew check` GREEN (147 tasks).
- On-disk amendment watermark: **AMD-87**. The M6 config block **AMD-66/67/68/70/71 is RATIFIED (2026-06-09)**; **AMD-69 is DEFERRED** (Tier-2/OQ-15-3, number reserved). Invariants §37–§41 registered.
- `projectionVersion` **5**.
- M6 execution state: **M6.1 DONE**; **M6.2** (secret store + per-scope key management) gate fully satisfied, instruction pending; **M6.4** (hot-reload atomic swap) unblocked, instruction pending; **M6.3** (at-rest write-path encryption) **triple-gated — OUT OF SCOPE for this research** (see Guardrails).

## 0.1 MANDATORY READ-FIRST (gap-relativity gate)

Before writing a single finding, read — from the `homesynapse-core-docs` connector:

1. `design/06-configuration-system.md` — **Doc 06, LOCKED.** Especially §0–§1 (the HA dual-storage and YAML-1.1 failure modes it already answers), §3.1–§3.7 (pipeline, composition, reload, secrets, write path, validation model, migration — note the 2026-06-10 §3.2 correction note and §3.7 amendments-in-force banner), §4 (data model), §5 (C1–C7), §6 (failure modes), §10, §14–§15.
2. `design/amendments/AMD-66_Configuration_Change_Listener.md` — the per-section reload-reaction seam + HOT/INTEGRATION_RESTART/PROCESS_RESTART classification contract.
3. `design/amendments/AMD-67_Config_Document_Schema_Major_Minor.md` — the `(major, minor)` config-document schema model + forward-only, idempotent, major-triggered migration chain.
4. `design/amendments/AMD-68_SecretStore_Atomic_Multi_Key_Write.md` — `SecretStore.setAll(Map)` atomic durable write (M6.2 scope).
5. `design/amendments/AMD-69_Passphrase_Root_KDF_Deferred_Tier2.md` — what is deliberately DEFERRED (do not re-open).
6. `design/amendments/AMD-70_Config_Observability_Events.md` — `config.validation_completed` (shipped) + `config.section_reloaded` (M6.4); flattened event-resident payloads.
7. `design/amendments/AMD-71_Hybrid_Config_Directory_Layout.md` — root + `integrations/` one-level includes; canonicalization path-traversal guard; `schemas/` cache.
8. `design/15-cryptographic-architecture.md` — **fences only** (§2.3, §3.5, §3.8, §7.3, §9): what the secrets/crypto posture already is, so RQ5 findings don't propose what Doc 15 already settles or forbids. **Doc 15 is LOCKED and inviolate.**
9. The note-quote rule: where this brief embeds hivemind-resident artifacts verbatim (§0.2/§0.3 below), those embeds are authoritative for you — do NOT substitute memory or summaries.

**Every RQ finding must state which of the above it is relative to.** "HomeSynapse should validate config at startup" is a FAILED finding — Doc 06 §3.1/§3.6 already does — unless it identifies a *specific delta* (e.g., a validation-timing class Doc 06 doesn't cover, with evidence).

## 0.2 Embedded verbatim — `config/configuration/src/main/java/module-info.java` at `9035110`

(The standing Research-6 rule: module names and edges are authoritative from this embed, not from any summary. **§7 is LIGHT for this research — you must NOT propose module-info changes** — but any code-adjacent observation must use these exact identifiers.)

```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * Configuration System — YAML loading, schema validation, secrets management,
 * hot reload, and integration-scoped configuration access (Doc 06).
 *
 * <p>This module defines the public API contracts for configuration management.
 * All subsystems receive their runtime configuration through
 * {@link com.homesynapse.config.ConfigModel} and
 * {@link com.homesynapse.config.ConfigurationAccess} rather than parsing YAML
 * independently.</p>
 */
module com.homesynapse.config {
    requires transitive com.homesynapse.event;

    // Third-party, non-transitive (Nick ruling 2026-06-10): consumed only by
    // the package-private M6.1a pipeline classes; never exposed on the public
    // API (-Xlint:exports silent). The HomeSynapse-module edge set above is
    // unchanged — the [AMD-71-A] zero-new-edge property holds.
    requires org.snakeyaml.engine.v2;
    requires com.networknt.schema;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires org.slf4j;

    exports com.homesynapse.config;
}
```

## 0.3 Embedded — the ratified machinery your findings must be relative to

This is the M6 charter + config MODULE_CONTEXT substance (hivemind-resident — not in your connector), condensed **without paraphrasing contract content**. Treat it as the "ALREADY-RATIFIED" register for the disposition table.

**The four M6 pieces (charter `context/planning/2026-06-08_M6-charter.md`):**

| Piece | Scope | Status |
|---|---|---|
| **M6.1 — config pipeline** | YAML 1.2 load (snakeyaml-engine, explicit `CoreSchema` — the engine default is the JSON schema where `~` ≠ null), JSON-Schema validation (networknt, allErrors), AMD-67 migration chain, `ConfigurationAccess`/`ConfigurationService` impls, AMD-71 layout + canonicalization traversal guard, AMD-66 listener *defined* + registered, `config.validation_completed` published | **DONE `b7bc65c` + `9035110`** |
| **M6.2 — secret store + per-scope key-management infra** | `ScopeKeyManager` (KEK/DEK, `scope_keys`), `PayloadCipher` seam (composition-root bridge at `com.homesynapse.app` — zero new module edge), machine-local-root secret store, `SecretStore.setAll(Map)` atomic durable write (AMD-68), `!secret`/`!env` stage-3 tag resolution | PLANNED — instruction pending |
| **M6.3 — at-rest write-path encryption** | sensitive-PII categories encrypted-on-write | **TRIPLE-GATED — OUT OF SCOPE here** |
| **M6.4 — hot-reload atomic swap** | atomic `ConfigModel` swap (no torn read), AMD-66 listener *invocation* + classification-driven per-section apply, `config.section_reloaded` (AMD-70), `ConfigChangeSet` diffing, reload/write `ReentrantLock`, atomic file writes, §3.7 step-7 migration write-back + pre-migration backup | PLANNED — instruction pending |

**Already-pinned M6.4 instruction obligations (2026-06-10 rulings — your findings must NOT duplicate or contradict these; cite them as ALREADY-COVERED where they apply):**
1. **R1:** Doc 06 §3.6 per-ERROR `config_error` startup publication (the publish site lands at M6.4).
2. The **P2 consumer/pin survey re-run** for `config.section_reloaded` (event-manifest fan-out).
3. The reload re-parse must carry the explicit **`CoreSchema`** (LoadSettings lockstep — the M6.1a gate-fix lesson).

**Ratified robustness machinery (the gap-relative register):**

- **INV-CE-01** — the YAML file is the sole source of truth; UI/CLI/REST all read/write that same file. There is structurally no HA-style `.storage`-vs-YAML split-brain.
- **INV-CE-02** — zero-config is valid; every key has a schema default; unconfigured integrations get an empty section.
- **INV-CE-03 / P2 / P5** — JSON Schema is the contract (types, defaults, ranges, behavioral descriptions, `x-reload` classification annotations); the composed schema is written to `schemas/config.schema.json` (AMD-71) for IDE completion; `homesynapse validate-config` validates offline.
- **LTD-09** — YAML 1.2 via snakeyaml-engine with explicit Core schema → the YAML-1.1 `NO`→false / `on`→boolean coercion bug class is structurally eliminated.
- **Three-tier validation (Doc 06 §3.6, shipped DP-2):** FATAL → refuse start; ERROR at *startup* → that key reverts to its schema default (degraded-but-functional start); ERROR/FATAL in a *reload candidate* → **the entire reload is rejected and the prior good `ConfigModel` stays active** (§3.3 reject-and-keep-prior-good-state). WARNING → accepted, reported.
- **AMD-67** — config-document schema is a `(configSchemaMajor, configSchemaMinor)` pair (on-disk `schema_version: {major, minor}`); migration is **forward-only, linear, idempotent, major-triggered**; `MigrationPreview` dry-run with `requiresUserReview`; chain gap or newer-persisted-major = FATAL (fail-closed, never guess); migration currently applies in-memory per load — disk write-back + pre-migration backup land with M6.4's atomic writes (R2 ruling).
- **AMD-66** — per-section `ConfigurationChangeListener` returning HOT / INTEGRATION_RESTART / PROCESS_RESTART; classification lives in schema annotations + listener logic, not ad-hoc subsystem code; unannotated default = PROCESS_RESTART (fail-safe). *Defined* at M6.1; *exercised under swap* at M6.4.
- **AMD-70** — config observability events with flattened event-resident payloads: `config.validation_completed` (shipped: `(configSchemaMajor, configSchemaMinor, issueCount, Map<String,Integer> severityCounts)`, DIAGNOSTIC, system subject), `config.section_reloaded` (M6.4), plus the pre-existing `config_changed`/`config_error`. Publish failure never fails the load (AMD-70-INV-01).
- **AMD-71** — hybrid layout (root document + `integrations/` one-level `!include`); nested include = unknown-tag FATAL (AMD-71-INV-02); canonicalization-based (`toRealPath()`) containment guard, symlink-safe, fail-closed naming the offending path (AMD-71-INV-01).
- **Write path (Doc 06 §3.5):** `ConfigModel.fileModifiedAt` is the **optimistic-concurrency token** (real file mtime; external edit → write rejected); single `ReentrantLock`; atomic write-to-temp-then-rename.
- **M6.4 atomic swap:** in-flight readers see wholly-old or wholly-new model — no torn read (charter done-when).
- **Secrets posture (Doc 06 §3.4 + Doc 15 fences + AMD-68/69):** secrets encrypted at rest (`secrets.enc`, AES-256-GCM), referenced by `!secret` name from YAML (file Git-safe); MVP root = shared machine-local key, zero-config, no passphrase (Doc 15 §3.5/§7.3); `setAll` atomic multi-key write (AMD-68, M6.2); passphrase/Argon2id root = **deferred Tier-2** (AMD-69 — do not re-open); `!secret`/`!env` are FATAL-unknown until M6.2 (fail-closed staging).
- **Identity/stability machinery (for RQ3/RQ4):** every domain ID is a **typed ULID wrapper** (LTD-04) — `DeviceId`, `EntityId`, `AreaId`, `FloorId`, `AutomationId`, `SystemId` — names are display metadata, not identity; the event log is immutable + event-sourced with deterministic replay (`projectionVersion` reconciliation, AMD-50 backfill machinery); AMD-44 gives Floors/Areas first-class registries (delete-rejects-when-areas-assigned-style referential guards); AMD-17 governs orphan detection/interaction when references vanish; device-replacement is first-class (`DeviceReplacementService`, INV-CS-02).
- **D4 carry (M13):** `SystemId` must be sourced/generated BEFORE config load (config publishes system-subject events at startup step 1) — a known, tracked composition-root obligation, not a gap.

---

## 1. Research questions (scope — answer ALL five)

### RQ1 — Home Assistant failure-mode catalog

Build the evidence catalog of how HA's configuration system has actually hurt users. For each failure class: what happened, the primary-source citation, the user-visible blast radius, and the gap-relative verdict against §0.3.

Cover at minimum:
1. **Breaking config changes across upgrades** — monthly-release breaking-change lists; integrations whose YAML keys were renamed/removed; what the upgrade experience is when the user hasn't read the release notes (evidence: HA release-notes "Breaking changes" sections, core GitHub issues, community-forum threads).
2. **YAML deprecations + forced migrations to UI config flows** — the multi-year arc of integrations dropping YAML support for config-flow-only setup; what power users said when their version-controlled config became un-editable JSON; the ADR-0010 dual-storage rationale and its costs.
3. **The `.storage` vs `configuration.yaml` split-brain** — concrete failure stories: divergence, corrupted `.storage`, partial restores, Git workflows broken by UI edits.
4. **Include sprawl** — `!include`, `!include_dir_list`, `!include_dir_merge_named`, packages: where multi-file composition helps and where it produces unmaintainable or order-sensitive configs.
5. **Restart-to-apply culture** — which config domains require full restart vs reload; the user cost (automations offline, Zigbee network re-init); how HA's per-integration reload grew and where it still fails.
6. **Validation timing** — what `check_config` catches vs what only explodes at runtime; classes of errors that pass startup validation but break later (template errors, unavailable entities at automation trigger time).
7. **Silent defaults** — cases where a typo'd key was silently ignored (no schema enforcement) and the user discovered it weeks later; HA's permissiveness vs strictness tradeoff.
8. **Secrets handling** — `secrets.yaml` is plaintext at rest; community asks for encryption; leak vectors (backups, log redaction failures, Git commits).

### RQ2 — Cross-ecosystem comparison (Mom-Test evidence standards)

For **SmartThings (including the Groovy/IDE retirement breakage), Apple HomeKit, Hubitat, openHAB, Homey, and Alexa/Google routines ecosystems**: what do laymen vs power users actually praise and actually abandon in each platform's config/settings model? Evidence = cited complaints, reviews, migration threads, churn stories — **not vibes, not marketing copy**. The Mom-Test standard: what users *did* (abandoned, migrated, paid, forked), not what they say they'd like.

Extract two pattern catalogs:
- **"Options + freedom without footguns" patterns for power users** — e.g., textual config with validation + diff + versioning; staged/preview apply; per-section reload; escape hatches that don't void the warranty.
- **"Zero-config / never-see-YAML" patterns for laymen** — e.g., HomeKit's no-config-file model and what it gives up; Homey's flow UX; SmartThings' cloud-managed model and what the Groovy retirement did to user trust (the canonical case study of platform-managed config breaking user investment — document the timeline, what broke, user reaction, measurable churn signals).

For each pattern: which audience it serves, the evidence, and the gap-relative verdict (HomeSynapse's INV-CE-01 single-file + schema + UI-writes-the-same-file model claims to serve both audiences — where does the evidence support or threaten that claim?).

### RQ3 — Runtime non-breakage taxonomy

Build the failure-class taxonomy for config application at runtime, with evidence from any surveyed platform (plus adjacent infrastructure prior art where it is the canonical reference — e.g., Kubernetes ConfigMap reload semantics, systemd reload, nginx config test+reload):
1. **Torn/partial config application** — half-applied changes; subsystem A sees new value, subsystem B sees old.
2. **Device/entity renames breaking automations** — the rename-cascade problem; platforms where display names are identity vs platforms with stable IDs.
3. **ID stability** — what happens on re-pairing, integration re-setup, restore: do entities keep identity?
4. **Mid-flight migration failure** — upgrade dies mid-migration: what state is the config (and the system) left in?
5. **Rollback semantics** — config versioning/undo; what platforms offer (snapshots, backups, nothing); what users expect after a bad change.

**Then map EACH failure class against the ratified machinery (§0.3) → a gap table:** which classes are structurally closed (cite the exact mechanism: AMD-66 classifications; §3.3/§3.6 reject-and-keep-prior-good-state; AMD-67 forward-only idempotent migrations + fail-closed gap/newer-major; `fileModifiedAt` concurrency token; M6.4 atomic swap; typed-ULID identity; immutable log), which are closed-on-paper-but-untested (→ candidate M6.4 test obligations), and which are genuinely open (→ FUTURE AMD or POST-MVP).

### RQ4 — Scale + layout churn

Evidence on configuration behavior under structural churn: adding/removing integrations, devices, floors/areas (HomeSynapse: AMD-44) at runtime; referential integrity when config references vanish (an automation references a removed entity; an `integrations/foo.yaml` include disappears; an area is deleted with devices assigned — HomeSynapse: AMD-17 orphan interaction, AMD-44 registry guards); bulk-edit ergonomics (renaming 40 entities, re-areaing a floor's devices, find/replace across config — where text files win, where UIs win, where platforms corrupt state). Cite concrete platform behavior and user reports; verdict per finding against §0.3.

### RQ5 — Local-first / cloud / hybrid resilience

1. **Cloud-outage case studies** — documented incidents where cloud-dependent config/settings made homes uncontrollable or unconfigurable (SmartThings outages, Insteon shutdown, Tuya/eWeLink incidents, Google/Alexa routine outages); what stayed working on local-first platforms.
2. **Offline guarantees** — what each platform can configure/operate with WAN down; HomeSynapse's posture (fully local config plane) as the baseline.
3. **Hybrid sync-conflict + provenance semantics** — when a future cloud/companion surface can edit config: conflict models (last-write-wins vs token-based rejection vs CRDT), provenance ("who/what changed this key"), and audit expectations from prior art (HA Cloud/Nabu Casa scope, SmartThings cloud-edit model, Hubitat's hybrid).
4. **Classify EVERY implied decision as `now-or-never` (schema-irreversible — would change persisted event shapes, config-document schema semantics, ID/provenance semantics that the immutable log or frozen contracts would lock in) vs `deferrable post-MVP` (UI flows, sync engines, cloud services).** The PM's strategic baseline: the 2026-06-10 assessment found the M6.1 contract set regret-proof for a hybrid-cloud future (immutable atomically-swapped `ConfigModel`, AMD-67 version machinery, `fileModifiedAt` token, flattened observability events, local-resident secrets) with provenance/multi-writer semantics consciously deferred — your job is to confirm or refute *with evidence*, and to surface any now-or-never item that deferral would foreclose.

---

## 2. Mandatory document format

Follow the house research format (research-agenda.md §0 — embedded here because it is not in your knowledge):

```
# Research 13: Config System Market Superiority — UX Failure Modes + Runtime Robustness
*Target: HomeSynapse Core M6.2/M6.4 + future config AMDs + M10/M11/Doc 13. Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — NEW, do this FIRST]
   - Quote back, verbatim: (a) the §0.2 module-info embed; (b) the §0.3 four-piece
     charter table rows; (c) the three pinned M6.4 obligations. If you cannot quote
     them, STOP and return INCOMPLETE. (The Research-7v2 counter-measure: proves the
     embeds were read before any finding is produced.)

## 1. Executive Summary [M]
   - 5–8 verdict bullets; every bullet takes a position with a one-sentence defense.
     "X is worth investigating" is banned. Flag the single highest-impact finding.

## 2. Platform / Literature Deep Dives [M] — one subsection per platform (RQ1: HA gets
     the deepest treatment; RQ2 platforms each get one; RQ3/RQ5 prior art inline).
     Each subsection: (a) how the platform solves/fails the problem; (b) ≥1 direct
     quotation from a primary source (docs, issue tracker, changelog, forum thread,
     maintainer statement) WITH URL; (c) community pain points; (d) the specific
     gap-relative lesson for HomeSynapse (cite the §0.3 register item it is relative to).

## 3. Cross-Cutting Analysis [M]
   - 3.1 Concept-mapping table: failure class / pattern | HA | SmartThings | HomeKit |
         Hubitat | openHAB | Homey | HomeSynapse (ratified mechanism, cited).
   - 3.2 The RQ3 gap table (failure class → ratified mechanism → CLOSED /
         CLOSED-UNTESTED / OPEN).
   - 3.3 Dual-audience assessment: where the evidence supports/threatens the
         one-file-two-audiences claim (RQ2).
   - 3.4 Over-engineering check: ratified machinery NO surveyed platform's users
         actually need — defend or flag each (honesty section; REJECT-candidates).

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, starting at REC-130, ranked (impact × confidence)/cost.
         Each REC: the failure-class/pattern citation; the evidence (≥1 primary source);
         the gap-relative statement (what ratified machinery already does / doesn't);
         the concrete recommendation; effort class (S/M/L — prose, not LoC).
   - 4b. THE DISPOSITION TABLE [M — the load-bearing deliverable]: EVERY REC maps to
         EXACTLY ONE of:
           ALREADY-COVERED (cite the specific AMD-NN §N / Doc 06 §N / invariant)
         | M6.2-or-M6.4 INSTRUCTION OBLIGATION (name the piece + what the instruction
           must add — typically a test, a behavior detail, or an ergonomic default
           inside already-ratified contracts)
         | FUTURE AMD (formal pipeline; sketch the contract delta — do NOT draft it)
         | POST-MVP UI-or-cloud DESIGN INPUT (M10/M11/Doc 13 lane)
         | REJECT (reasoned — evidence says HomeSynapse should NOT do this).
         No REC may appear in two buckets. No bucket may be empty by laziness —
         if a bucket is genuinely empty, say why.

## 5. Caveats and Open Questions [M] — source reliability; unresolved cross-platform
     tensions; anything needing empirical validation (spike candidates).

## 6. Appendix: Sources [M] — URL families grouped by platform; every factual claim
     traceable.

## 7. HomeSynapse Code-Level Implications [LIGHT] — observations ONLY, routed through
     §4b. NO module-info proposals, NO new types, NO contract drafts. Use exact §0.2
     identifiers for any code-adjacent observation.
```

## 3. Evidence standards (non-negotiable)

1. **Primary sources with URLs.** Changelogs, official docs, GitHub issues/PRs/ADRs, release notes, maintainer statements, dated forum/Reddit threads. A claim without a citation is a vibe.
2. **Mom-Test discipline (RQ2 especially).** What users *did* — abandoned, migrated, forked, paid, churned — outranks what they say. Praise in a review counts less than a migration thread; a migration thread counts less than a documented exodus (the Groovy retirement is the calibration case).
3. **Take positions.** Every section concludes with a verdict. "Worth investigating" is banned.
4. **Gap-relative or it didn't happen.** Every finding states which §0.1/§0.3 item it is relative to. Findings that re-propose ratified machinery score as ALREADY-COVERED, not as recommendations.
5. **No fabricated identifiers.** Type/module names come from §0.2/§0.3 verbatim. If you need a HomeSynapse fact not embedded here and not in the connector, request it in §5 — do not reconstruct it (the Research 3/4/6/7/8 fabrication lesson; the §0 quote-back gate enforces this).
6. **Web search is required** for RQ1/RQ2/RQ5. If your web reach is too shallow to satisfy standard 1, say so explicitly in §5 and return what you have marked INCOMPLETE-EVIDENCE — the PM will split the evidence-gathering to a generic deep-research run (the masthead fallback). Do not pad thin evidence into confident findings.

## 4. Guardrails (violations = the finding is discarded)

1. **Ratified AMD-66..71, Doc 06, and Doc 15 are inviolate.** Research informs *instructions* (M6.2/M6.4) and *future amendments* only. Any contract-change implication routes through the formal AMD pipeline as a FUTURE-AMD disposition — you never draft amendment text.
2. **No scope creep into M6.3 crypto.** At-rest write-path encryption is triple-gated (OQ-15-2 Pi-4 microbench + interview signal + OR-M6-NONCE). RQ5 touches secrets/cloud posture ONLY at the level of §0.3's stated posture; the encrypted-scope set, nonce machinery, and shred semantics are out of scope.
3. **Do not duplicate or contradict the three pinned M6.4 obligations** (§0.3): R1 per-ERROR `config_error` publish; the `config.section_reloaded` P2 survey; CoreSchema on the reload re-parse. Cite them as ALREADY-COVERED where relevant.
4. **AMD-69's deferral is settled.** Passphrase-root KDF findings → POST-MVP bucket at most.
5. **REC numbering starts at REC-130** (append-only global register; 120–129 = Research 12 Zigbee, 106–119 = the R7v2 reservation).
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM assessment (6-step A–F, source-verified) will: fold ALREADY-COVERED rows into a coverage attestation; convert INSTRUCTION-OBLIGATION rows directly into the M6.2/M6.4 coding instructions' test requirements and watch-outs; queue FUTURE-AMD rows for Nick's prioritization through the formal pipeline; park UI/cloud rows in the M10/M11/Doc 13 lane; and record REJECTs with their reasoning as anti-requirements. A finding that cannot be placed in that machine is a finding you should sharpen or drop.

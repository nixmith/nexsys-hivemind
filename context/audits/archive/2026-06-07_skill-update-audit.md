<!--
file: context/audits/2026-06-07_skill-update-audit.md
purpose: Phase-1 audit + update plan for the two governance skills (nexsys-coder, nexsys-project-manager) — staleness, gaps, historical-trim candidates, cross-skill consistency, and a sequenced edit plan. NO edits made; this is the findings deliverable.
audience: Nick (owner/approver), PM
update-cadence: frozen (audit snapshot)
state-type: audit
status: CURRENT — Phase 1 deliverable. STOP gate: no skill file edited until Nick reviews + approves this plan.
last-verified: 2026-06-07 against homesynapse-core HEAD 8028337, homesynapse-core-docs + nexsys-hivemind working trees (Read tool; sandbox git treated as non-authoritative)
-->

# Skill Update Audit — `nexsys-coder` & `nexsys-project-manager`

**Date:** 2026-06-07 · **Author:** PM (Cowork governance session) · **Scope:** audit + plan only (Phase 1). No skill files edited.
**Skills audited:** `nexsys-hivemind/coder/` and `nexsys-hivemind/project-manager/` (writable source) — 15 files total, all stamped `last-verified: 2026-05-20 against commit 25bc23b`.
**Why now:** the skills have not been touched since ~2026-05-22 while the project moved mid-M4 → M4 COMPLETE → into the M5 window. These files govern every future Coder/PM session, so each stale claim propagates.

---

## 0. Executive Summary

**Verdict.** Both skills are structurally sound and their *disciplines* (freshness preflight, WUCP two-phase closeout, deferred-gate tracking, STOP-on-mismatch gates, the dual-skill mirror, Clock injection) are load-bearing and correct — keep them. But the skills are **factually stale across every count, module name, commit anchor, milestone marker, and date**, they are **missing four Nick-adopted process proposals (D8: P1/P2/P3/P6) that were explicitly slated to land in them**, and they contain **six classes of actively-WRONG instruction** (not merely stale) that would mislead a fresh agent — most dangerously a removed-library API and a relocated module. None of this is hygiene-optional: a Coder session that reads `java-patterns.md` today is told to call a factory that does not exist.

**Freshness preflight (this session).** Mirror check (Check 9) is **PASS** — `diff -rq` of both skill source trees vs `.claude/skills/` mirrors is empty (clean baseline; confirmed by the M4 retro §9.6 too). The broader hivemind is mid-reconciliation by the **concurrent M5 fold+ratify session** that owns `context/handoff` + `context/status` + `homesynapse-core-docs`; expect STALE on those files (the snapshot itself says "coder-handoff/weekly/backlog/reorg in progress"). That does **not** block this audit: Nick explicitly scoped this session to the skill audit, and the only file written is this one under `context/audits/`.

**Footprint / non-collision.** This session reads widely but writes **only** `context/audits/2026-06-07_skill-update-audit.md`. No edits to skill files (Phase 2 gated on approval), and none to `context/handoff`, `context/status`, or `homesynapse-core-docs` (the parallel session's territory).

**Headline numbers (every one of these is wrong somewhere in the skills):** HEAD `25bc23b`→`8028337`; modules 16/19/20→**22**; invariants 81/15-cat→**133/32-cat**; LTDs 18→**19**; design docs 14→**15** (Doc 15 crypto, Draft); scaffold modules "3 (platform-systemd, test-support, dashboard)"→**1 (dashboard only)**; `projectionVersion`→**5**; build tasks→**147**; amendment watermark→**AMD-64 (→87 at ratification)**; new module **`com.homesynapse.value`** (value-model) exists and is unmentioned anywhere.

---

## 1. Method & Sources Verified

Read in full, against source (Read tool; sandbox `git` used only for the commit-anchor cross-check and explicitly distrusted per the standing lesson):

- **Both skills end-to-end:** `coder/{SKILL.md, CLAUDE.md}` + `coder/references/{homesynapse-mental-model, java-patterns, testing-standards, deviation-and-quality, freshness-preflight}.md`; `project-manager/{SKILL.md, CLAUDE.md}` + `project-manager/references/{coding-instruction-format, constraint-enforcement, cross-subsystem-awareness, repo-state-protocol, review-and-quality, freshness-preflight}.md`.
- **Layout/sync:** `nexsys-hivemind/README.md`, `setup.sh`, and the `diff -rq` mirror check.
- **Drift surface:** `context/lessons/{coder,pm,strategic}-lessons.md` (all entries); `context/audits/2026-06-05_M4-retrospective.md` (P1–P6); `context/decisions/2026-06-06_post-M4_M5-window_decisions.md` (D8); `context/protocols/work-unit-completion-protocol.md` (WUCP); `context/status/PROJECT_SNAPSHOT.md`; `context/coding-instructions/M5-A_Platform_Impls_AMD87_FloorId.md` + `archive/M4.C_Integration_API_Freeze.md`; `context/strategic-context-map.md` (refs spot-check).
- **Governance/source ground-truth:** `homesynapse-core-docs/governance/Architecture_Invariants_v1.md`, `HomeSynapse_Core_Locked_Decisions.md`, `design/` listing; `homesynapse-core/settings.gradle.kts`, the `value-model` + `platform-systemd` modules + MODULE_CONTEXTs, `HomeSynapseArchRules.java` (the `NO_DIRECT_TIME_ACCESS` whitelist), and `EntityId.java`/`UlidFactory.java`/`CausalContext.java`/`EventDraft.java` (to settle WRONG-vs-stale calls).
- **Form guidance:** `skill-creator` SKILL.md; `benchmarks/` (README, grading-protocol, scoring-history, regression-bank, answer-key shapes).

---

## 2. Ground-Truth Reference Table (the correct values, with source)

Every STALE finding below references this table. All values verified 2026-06-07.

| Fact | Skills currently say | Current truth | Source verified against |
|---|---|---|---|
| Skill masthead anchor | `2026-05-20 / 25bc23b` (all 15 files) | HEAD **`8028337`** (M5-A Part 1+3), 2026-06-07 | `homesynapse-core` git head + PROJECT_SNAPSHOT masthead |
| Phase / milestone vocabulary | "M3.x in execution; M4+ downstream" (PM SKILL §Mode 3) | **M5 window in progress**; M3 & M4 COMPLETE; Phase 3 test-first | PROJECT_SNAPSHOT "Current state"; W24 charter |
| Gradle modules | 16 / "19 modules" / 20 | **22** in `settings.gradle.kts` | `homesynapse-core/settings.gradle.kts` (incl. `core:value-model`, `platform:platform-systemd`, `spike:wal-validation`, `testing:integration-tests`, `testing:test-support`) |
| New module | (absent) | **`com.homesynapse.value`** (value-model, leaf; AttributeValue relocated here in M4.0b-4a to break the event↔device JPMS cycle) | `core/value-model/MODULE_CONTEXT.md`; AMD-52 §11 erratum |
| Scaffold/stub modules | "3 stubs: platform-systemd, test-support, dashboard" | **1: dashboard only** (platform-systemd populated in M5-A; test-support populated — TestClock/SynchronousEventBus/NoRealIoExtension, 14 files) | `platform/platform-systemd/`, `testing/test-support/`, `web-ui/dashboard/` (0 .java) |
| Architecture invariants | "81 across 15 categories" | **133 invariants across 32 categories** (84 base `INV-XX-NN` across 16 prefixes + 49 `AMD-NN-INV-NN`) | `Architecture_Invariants_v1.md` line 1030 (verbatim) + §0.3 prefix table |
| Invariant category prefixes | 15 named, incl. "OB" (Observability) | 16 prefixes; **TO** (Transparency & Observability) not "OB"; adds **BUS, PROJ, WRITER, SUB-ISO** + the `AMD-NN-INV` families | `Architecture_Invariants_v1.md` §0.3 |
| INV-GA-02 | (referenced loosely) | "**Invariant Identifiers Are Permanent**" (§15) — the identifier non-reuse rule (governs the AMD-65→AMD-87 renumber by analogy) | `Architecture_Invariants_v1.md` §15 / §17 index |
| Locked Technical Decisions | "18 LTDs" | **19** (LTD-19 = Event Payload Serialization via EventTypeRegistry + PersistenceJacksonModule; extends LTD-08) | `HomeSynapse_Core_Locked_Decisions.md` |
| Design documents | "14 Locked" | **15** numbered (01–15); Doc 15 = Cryptographic Architecture (**Draft**, in M5-window ratification) | `homesynapse-core-docs/design/` listing |
| `projectionVersion` | (not stated / stale) | **5** | PROJECT_SNAPSHOT |
| Build gate task count | (not stated) | **147 tasks** GREEN (`./gradlew check`) | PROJECT_SNAPSHOT (M5-A) |
| Amendment watermark | (AMD-50/53 era in some refs) | **AMD-64** on disk (→ **87** at AMD-86/87 ratification); AMD-65 **retired→renumbered AMD-87** per INV-GA-02 | PROJECT_SNAPSHOT; docs git log; M5-A instruction masthead |
| `NO_DIRECT_TIME_ACCESS` whitelist | `com.homesynapse.{app,platform,test}..` | **UNCHANGED — still correct** (`app`, `platform`, `test`) | `HomeSynapseArchRules.java:97-99` |
| `EntityId` factories | `EntityId.generate()` (java-patterns §1; testing-standards) | **No `generate()`** — only `of(Ulid)` + `parse(String)`; generate via `new EntityId(UlidFactory.generate(clock))` | `platform/platform-api/.../EntityId.java` |
| ULID generation API | `UlidCreator.getMonotonicUlid()` / `getUlid()` (mental-model §2; deviation-and-quality §1) | **`ulid-creator` removed (DECIDE-02)** — hand-rolled `UlidFactory.monotonic()` / `.generate([Clock])` | `UlidFactory.java`; constraint-enforcement.md (correct copy) |
| `CausalContext` shape | 3 fields incl. `actorRef` (deviation-and-quality §3) | **2 fields** (correlationId, causationId); actorRef is on `EventEnvelope` | `core/event-model/.../CausalContext.java` |
| `context/traceability/TEMPLATE.md` | cited by PM CLAUDE.md, review-and-quality, WUCP | **does not exist** — `context/traceability/` was removed (2026-04-11); real indexes live in `homesynapse-core/docs/traceability/` (no TEMPLATE.md there) | `setup.sh` notes; directory listing |

---

## 3. Cross-Cutting Findings

### 3.1 Masthead anchor staleness — ALL 15 skill files
Every skill file carries `last-verified: 2026-05-20 against commit 25bc23b`. Refresh all 15 to `2026-06-07 / 8028337` in Phase 2 (mechanical, but do it last so the anchor reflects the *content* state after edits land).

### 3.2 Milestone/phase vocabulary is one major-cycle behind
PM `SKILL.md` Mode 3 says "M3.x is the event-bus/state-projection/composition-root cohort (currently in execution). M4+ will be the downstream subsystems." Reality: M3 + M4 COMPLETE; **M5 window in progress** (lane-tracked M5-A…M5-D per the W24 charter / D1–D8). Mode 2 ("Phase 2 closed 2026-03-20") is still accurate. The "single compile-and-commit unit with test coverage" milestone definition is accurate and should be **kept and strengthened** (see P1).

### 3.3 Module inventory & MODULE_CONTEXT read-tables are stale everywhere
Affected: PM SKILL §0 read-when table (8 modules), coder SKILL read-when table (4 modules), repo-state-protocol §1C ("all 19 modules"), homesynapse-mental-model §8/§10, cross-subsystem-awareness §1 graph. None mention **value-model**; all still describe **platform-systemd/test-support as scaffold stubs** (both now populated); per-module **type counts** are point-in-time and have drifted (e.g., repo-state-protocol lists device-model "57", event-model "46", persistence "11", state-store "7", configuration "22"). Recommendation: add value-model to every read-table; correct the scaffold claim to "dashboard only"; and for the per-module counts, **stop hardcoding numbers — point to each module's `MODULE_CONTEXT.md` header as the source of truth** (the counts drift by construction, which is itself the lesson of strategic-lessons 2026-05-28).

### 3.4 ACTIVELY WRONG (not merely stale) — the must-fix-carefully list
These would cause a fresh agent to do the wrong thing. Each is a deliberate call for Nick, not a silent fix:

1. **Removed-library ULID API.** `homesynapse-mental-model.md` §2 (`UlidCreator.getMonotonicUlid()`) and `deviation-and-quality.md` §1 LTD-04 (`getMonotonicUlid()`/`getUlid()`) teach the **`ulid-creator` API that was removed by DECIDE-02**. Correct: hand-rolled `UlidFactory.monotonic()` / `UlidFactory.generate([Clock])`. (constraint-enforcement.md and coding-instruction-format.md already have the correct form — so the skills *contradict each other* on this.)
2. **Relocated `AttributeValue`.** `homesynapse-mental-model.md` §9 and `cross-subsystem-awareness.md` §3 still say `AttributeValue` lives in the device-model module. It was **relocated to `com.homesynapse.value` (value-model)** in M4.0b-4a — the move that broke the event↔device JPMS cycle. A coder/PM reasoning from "AttributeValue is in device-model" will mis-wire module edges.
3. **Non-existent factory `EntityId.generate()`.** `java-patterns.md` §1 *defines* it and `testing-standards.md` *uses* it in examples; source `EntityId.java` has only `of()`/`parse()`. Correct: `new EntityId(UlidFactory.generate(clock))`. (Coder-lessons M2.9, 2026-04-15, logged exactly this.)
4. **Stale `CausalContext` shape.** `deviation-and-quality.md` §3 shows a 3-field record with `actorRef`; source is **2-field** (actorRef moved to the envelope, INV-MU-01). `homesynapse-mental-model.md` §2 already states the correct 2-field form — internal contradiction.
5. **Dead template path.** PM `CLAUDE.md` (WUCP step 3) and `review-and-quality.md` §6 step 3 cite `../context/traceability/TEMPLATE.md`; the directory was removed. The WUCP protocol itself (Step 2, not a skill file) repeats it — flag to Nick for a coordinated fix (see Open Questions).
6. **Wrong invariant taxonomy.** `constraint-enforcement.md` §1/§2 says "81 across 15 categories" and lists prefix "**OB**"; the live prefix is "**TO**", the count is **133/32**, and BUS/PROJ/WRITER/SUB-ISO + the AMD-INV families are missing. A PM "independent invariant-index scan" using this list will miss whole categories.

### 3.5 Hard-won conventions present in lessons but ABSENT from the skills
(Promoted in §6; flagged here as cross-cutting because each spans both agents.)
- **`requires transitive` ↔ Gradle `api` lockstep / `-Xlint:exports` discipline** — logged as the **3rd occurrence (M2.9, M3.6e.1, M5-A)** in coder-lessons; the corollary "every `requires transitive` ⇒ `api()`, every plain `requires` ⇒ `implementation()`" and "an exported public class must not expose a foreign-module/non-transitive type." **Not in java-patterns.md at all.** Highest-value missing technical convention.
- **Sandbox-git distrust / Read-tool authoritative** — `git status`/`git diff` in-sandbox show line-ending churn and even mangle files (pm-lessons 2026-05-31; snapshot repeatedly). The Read tool on the working tree is authoritative; commits go through host git. deviation-and-quality §6 Source Trust Hierarchy is the natural home; it currently covers handoff-vs-source but not sandbox-git.
- **Source round-trip check** (strategic-lessons 2026-05-28): every type name a doc cites must be grep-confirmed in source; every count regenerated from source — explicitly recommended for promotion into `freshness-preflight.md`.
- **Deferred-gate shift-left** (P5 / coder-lessons M5-A): a targeted `./gradlew :module:compileJava` on `-Werror`-sensitive touched modules before handoff catches `[exports]`/cast/unused-import in ~20s.

---

## 4. Adopted-but-Unencoded Process Proposals (the primary known gap)

`context/decisions/2026-06-06_post-M4_M5-window_decisions.md` **D8** states verbatim: *"Adopt P1 (lane-tracking), P2 (consumer/pin survey), P3 (ticked WUCP-Phase-2 closeout — retire the placeholder-`sed`), and P6 (non-Core floor) into the PM skill / `coding-instruction-format.md` now; P4/P5 as they apply."* None have landed. Per-proposal status and exact target:

| Proposal (M4 retro §10) | What it requires | Adopted? | Already encoded? | Lands in |
|---|---|---|---|---|
| **P1 — milestone-sizing smell test + lane-tracking** | >3 sub-milestones or >3 amendments ⇒ split into first-class milestones, each with its own backlog row + done-when ("lane-tracking") | **D8 yes** | No (Mode-3 has the "single compile-and-commit unit" def but no sizing smell test / lane discipline) | PM `SKILL.md` §Mode 3 + §3 (task-brief processing) |
| **P2 — consumer/pin (fan-out) survey** | Mandatory survey for any change to an enum / registry / event-type set / sealed hierarchy / mapping table / counted-or-pinned set: enumerate count-pins, validity regexes, mapping tables, manifest aggregators, **composition-root AND test-harness registrations**, exhaustive switches — each with its delta, before issue | **D8 yes** | Partial only — M4.C had a G11 *caller* survey for constructors but missed the 7 event-type sites; **M5-A already added a dedicated `## P2 Consumer/Pin (Fan-Out) Survey` section** (living proof of the target shape) | `coding-instruction-format.md` (new template section) + PM SKILL §Mode 3 step |
| **P3 — ticked WUCP-Phase-2 artifact checklist** | "Closeout applied" not assertable until every artifact ticked: snapshot header **and** session-log row, backlog, pm-handoff, week-plan progress **and** footer, **coder-handoff gate flip (OPEN→RESOLVED+SHA)**, cross-agent-notes archival; retire placeholder-`sed` | **D8 yes** | Partial — WUCP Step 12 has a checklist, but it omits the coder-handoff gate flip, the week-plan footer, and the "fixed six" framing (pm-lessons 2026-05-31) | WUCP protocol Step 12 (flag — see OQ) + `review-and-quality.md` §6 + PM `CLAUDE.md` |
| **P4 — lightweight block-amendment track** | Trivial additive amendments (one field + back-compat ctor; new constant on non-persisted enum; inert reservation) ride a shared block review/ratification/mechanics; full per-AMD reserved for persisted-shape/behavioral/new-invariant; inert reservations carry "inert until M{N}" | **D8 "as it applies"** | No | `constraint-enforcement.md` (amendment process) + `review-and-quality.md` |
| **P5 — shift-left inspection-discoverable gate misses** | Keep deferred gate as backstop; catch P2-class misses pre-issue; targeted `compileJava` before handoff | **D8 "as it applies"** | No | PM SKILL §4b + `coding-instruction-format.md` Build Discipline + coder `CLAUDE.md`/java-patterns |
| **P6 — non-preemptable non-Core floor** | Each milestone window pairs a deliberately-small Core piece with a website/docs standup Core may not preempt | **D8 yes** | No | PM `SKILL.md` (planning/mode) + strategic note |

**Keep-doing (M4 retro §9) — protect, do not trim:** STOP-on-mismatch gates; AMDs as single source of truth + ratified-vs-shipped erratum reconciliation; independent DOCS-Project reviews; the freshness preflight; the research→AMD→code pipeline; the dual-skill mirror discipline (Check 9 clean). These are already in the skills and should be reinforced, not weakened, by any edit.

---

## 5. Per-File Findings

Legend: **STALE** = wrong fact w/ corrected value; **MISSING** = convention/lesson/proposal to add; **HISTORICAL** = trim/archive candidate (FLAGGED, not pre-decided); **CONSISTENCY** = disagreement with another skill file.

### 5.A — `project-manager/SKILL.md`
- **STALE.** Mode 3 header: "M2.x persistence; M3.x … currently in execution; M4+ downstream" → M3 & M4 COMPLETE, **M5 window in progress** (src: PROJECT_SNAPSHOT, W24 charter/D1–D8). · §0 MODULE_CONTEXT read-when table lists 8 modules, **missing `core/value-model`** (and platform-systemd now real) (src: settings.gradle.kts, value-model MODULE_CONTEXT). · §4c arch-rule reminder module list omits `value-model` (its tests are non-whitelisted; whitelist itself still correct) (src: HomeSynapseArchRules.java:97-99). · masthead `25bc23b`→`8028337`.
- **MISSING.** **P1** (milestone-sizing smell test + lane-tracking) into Mode 3 + §3. · **P6** (non-Core floor) into the mode/planning text. · **P5** (shift-left targeted `compileJava`) into §4b deferred-gate. · A pointer to the **pre-verifications artifact** convention (`context/pre-verifications/WU-<id>.md`, pm-lessons 2026-05-21) for ≥3-prereq briefs. · The **"fixed six-file closeout"** framing (pm-lessons 2026-05-31) reinforcing §1's WUCP obligations.
- **HISTORICAL (flag).** Mode 1 (Architect/Phase 1) and Mode 2 (Specifier/Phase 2) are now rarely/never entered (Phase 1 design docs Locked; Phase 2 closed, AMD-only). They remain **load-bearing for AMD work and design-doc supersession** — recommend *demote/condense*, not delete; Nick to confirm. The Research-6 module-info embedding lesson (Step 3) is current and stays.
- **CONSISTENCY.** §4c reminder text matches coder SKILL/java-patterns §11 whitelist — good; keep them in lockstep when value-model is added.

### 5.B — `project-manager/CLAUDE.md`
- **STALE (WRONG).** WUCP Phase 2 step 3 cites template `../context/traceability/TEMPLATE.md` — **path does not exist** (src: dir listing; setup.sh "moved 2026-04-11"). Same dead ref at line 91 (Traceability section "Contains TEMPLATE.md only"). · "All 14 Locked design documents + amendments" → **15** (Doc 15 Draft). · masthead.
- **CONSISTENCY.** Lists WUCP Phase 2 as **13 steps numbered 1–13**, with skill-sync as **step 11**; but `freshness-preflight.md` (both copies) and the WUCP body call the skill-sync **"Step 10"** (0-indexed from Step 0 preflight). Same content, two numbering schemes (see §7). · WUCP step list here should gain the **P3** ticked-artifact detail (coder-handoff gate flip + week-plan footer + cross-agent archival).
- **MISSING.** Build-verification/handoff text is a natural secondary home for the **sandbox-git-distrust** note ("`git status`/`diff` unreliable in-sandbox; Read tool authoritative; commit via host git").

### 5.C — `project-manager/references/coding-instruction-format.md`
- **STALE.** Framed as "M3 Cowork Prompt Enhancements (Post-M3.1)" — the enhancements are now standard practice through M5; generalize the framing. · masthead.
- **MISSING (primary).** **P2 dedicated "Consumer/Pin (Fan-Out) Survey" template section** — M5-A already demonstrates the exact shape (`## P2 Consumer/Pin (Fan-Out) Survey`); fold that in as canonical, covering count-pins, validity regexes, mapping/category tables, manifest aggregators, **composition-root + test-harness registrations**, exhaustive switches. (Retro §3: M4.C's 7-site lockstep would have been one-round-green with this.) · **§4c arch-rule reminder** as a standard template block (M5-A embeds it verbatim with the whitelisted-module carve-out) — currently only PM SKILL §4c tells the PM to include it; the format doc doesn't show it. · **The ⛔ multi-gate marker convention** + **verbatim `module-info` embed with PROPOSED-DIFF** (M5-A uses both; the format doc has the embedding *rule* but not the gated-part marker or the diff convention). · **The `requires transitive`↔`api` authoring check** before embedding a module-info (pm-lessons 2026-06-07: scan exported public types for foreign-module supertypes/returns/params). · **Masthead conventions** the real instructions use (`amd-number-note`, `status: ISSUE-READY/⛔GATED`, `baseline: HEAD …`). · **P5 Build-Discipline** line: "target GREEN in one round; run targeted `:module:compileJava` on `-Werror`-sensitive modules."
- **HISTORICAL (flag).** The "M3 Cowork Prompt Enhancements" section title is dated; content stays, heading should generalize. The single illustrative example chain (EventBus 4→8) is fine but could be refreshed to an M4/M5 example.
- **CONSISTENCY.** Already correct on `UlidFactory.monotonic()`/`generate()` (LTD-04) — good; this is the *correct* copy that mental-model/deviation-and-quality contradict.

### 5.D — `project-manager/references/constraint-enforcement.md`
- **STALE (WRONG).** §1 table + §2: invariants "**81 across 15 categories**" → **133 across 32** (src: `Architecture_Invariants_v1.md` line 1030 verbatim). · §2 category list names prefix "**OB**" → live prefix is "**TO**"; list omits **BUS, PROJ, WRITER, SUB-ISO** and all `AMD-NN-INV` families (src: §0.3). · §1/§2 "**18 LTDs**" → **19** (LTD-19 persistence Jackson serialization) — the §2 table stops at LTD-18; add LTD-19 row. · masthead.
- **MISSING.** **P4 lightweight block-amendment track** (trivial-additive vs persisted-shape/behavioral/new-invariant; "inert until M{N}" note) belongs here in the amendment-process text. · The **`requires transitive`↔`api` lockstep** as a JPMS-default-rule companion (§"JPMS Default Rule" already states the transitive-default; add the Gradle-scope lockstep + exported-type-leak rule, cross-ref java-patterns).
- **HISTORICAL (flag).** None major; the LTD one-liners are durable.
- **CONSISTENCY.** Duplicate section number "**## 4**" appears twice (Constraint Discovery Checklist *and* Governance Finding Protocol) — renumber. · Holds the correct `UlidFactory` API (agrees with coding-instruction-format, disagrees with mental-model/deviation-and-quality — fix the latter two to match this).

### 5.E — `project-manager/references/repo-state-protocol.md`
- **STALE.** §1A "the 14 design documents" → **15**. · §1C "**all 19 modules** … populated as of Phase 2 (2026-03-22)" → **22 modules**; list omits **value-model, testing:integration-tests, spike:wal-validation**; **platform-systemd/test-support no longer scaffold** (only dashboard) (src: settings.gradle.kts + module dirs). · per-module type counts (event-model 46, device-model 57, persistence 11, state-store 7, configuration 22) are point-in-time and several have drifted — **recommend replacing hardcoded counts with "see each module's MODULE_CONTEXT.md header."** · date drift: says Phase 2 close **2026-03-22** while SKILLs elsewhere say **2026-03-20** (pick one — snapshot uses 2026-03-20 for close, 2026-03-22 appears for MODULE_CONTEXT population; clarify). · masthead.
- **MISSING.** A short "**sandbox git is non-authoritative**" subsection in §4 ("When State Is Uncertain")/§3 (state sync uses `git log`): note the Read-tool-authoritative rule and host-git commit path.
- **HISTORICAL (flag).** §1B "Interface Specification State (Phase 2+)" is mostly historical now (Phase 2 closed) — keep as reference, light-touch.
- **CONSISTENCY.** Its module list is the most-cited inventory; align it with mental-model §8/§10 and the two SKILL read-tables in one pass.

### 5.F — `project-manager/references/cross-subsystem-awareness.md`
- **STALE (WRONG).** §3 "The Shared Type Problem": "**`AttributeValue` sealed interface — defined in the device model API module**" → now `com.homesynapse.value` (value-model) (src: value-model MODULE_CONTEXT; AMD-52 §11). · §1 prose "consists of **13 subsystems**" vs the 14-node dependency graph (and Doc 15 now a 15th doc) — reconcile. · §2 "Capability hierarchy (16 types, not 15)" — verify against current device-model MODULE_CONTEXT (header still says device-model "57 types"; capability-count claim should be re-confirmed before relying on it). · masthead.
- **MISSING.** The dependency graph should show **value-model** as the new leaf both event-model and device-model depend on (the acyclic fix). · Note the **mixed event-naming convention** (legacy snake_case frozen; new events dot-namespaced) as a cross-subsystem contract (M4 retro §7.2).
- **HISTORICAL (flag).** The JPMS Verification Checkpoint (M3.3) and the forward-reference/placeholder protocol (§5) are Phase-2-flavored but still useful for AMD work — keep.
- **CONSISTENCY.** The AttributeValue-location error is shared with mental-model §9 — fix both identically.

### 5.G — `project-manager/references/review-and-quality.md`
- **STALE (WRONG).** §6 step 3 cites `../context/traceability/TEMPLATE.md` (dead path, as in CLAUDE.md). · §1 "All **13** MANDATORY sections" (design-doc template) — verify against DESIGN_DOC_TEMPLATE (likely still 13; confirm). · masthead.
- **MISSING.** **P3** ticked-artifact detail into §6 (coder-handoff gate flip, week-plan footer, cross-agent archival, "fixed six"). · **P4** review-track distinction (lightweight block vs full DOCS review) into the review guidance. · The **deviation-can-be-more-correct-than-spec** adjudication lesson (pm-lessons 2026-05-30): when a `[REVIEW]` deviation cites "preserves prior behavior / avoids a regression," weigh on correctness not literal conformance, and log a spec erratum as an Open Item.
- **CONSISTENCY.** §6 numbers WUCP Phase 2 as 13 steps with skill-sync at **step 11** (matches CLAUDE.md, differs from preflight's "Step 10") — align numbering scheme project-wide (§7).

### 5.H — `project-manager/references/freshness-preflight.md`
- **STALE.** Origin/examples cite M2.5-era anchors (fine as history). masthead. The 10 checks are current and correct; Check 9 (dual mirror) text is accurate (verified PASS this session).
- **MISSING.** A **source round-trip check** (strategic-lessons 2026-05-28 explicitly recommends adding it here): every type/class name a state doc cites must be grep-confirmed in `homesynapse-core`, and every quantitative claim regenerated from source/register — the check that would have caught the fabricated `MinimalDerivationRule` and the wrong test counts. · If added, mirror the Coder-relevant subset into the coder preflight and update both output-format blocks (the file's own §7 rule).
- **CONSISTENCY.** This file says the skill-sync is **WUCP "Step 10"**; CLAUDE.md/review-and-quality say "step 11" (§7). The two preflights (PM 10-check, coder 6-check) are otherwise correctly differentiated and in sync on Check 9/Check 6 — no drift between them.

### 5.I — `coder/SKILL.md`
- **STALE.** §3 step "All 16 JPMS-compiled modules have populated MODULE_CONTEXT.md … Three scaffold-only modules (platform-systemd, test-support, web-ui/dashboard) still have stubs" → **value-model exists (17th compiled); platform-systemd + test-support populated; only dashboard stub** (src: module dirs). · MODULE_CONTEXT read-when table (4 modules) **missing value-model**. · §2 Phase-2 framing presents interface-spec as a live mode (now AMD-only). · masthead.
- **MISSING.** Cross-reference to the new **java-patterns JPMS-exports/lockstep section** (once added) in the "read when writing Java" table. · Note value-model in the dependency-root guidance (AttributeValue now sourced there).
- **HISTORICAL (flag).** §2 "Phase 2 — Interface Specification" block — demote to AMD-correction context (parallels PM Mode 2).
- **CONSISTENCY.** §4c-equivalent (line 101/324 Clock rule) matches java-patterns §11 + PM §4c — keep aligned.

### 5.J — `coder/CLAUDE.md`
- **STALE.** "All 14 Locked design documents" → 15 (Doc 15 Draft). · "The 18 LTDs you must follow" → **19**. · masthead. (queue-removed notes, repo paths, tier loading all still accurate.)
- **MISSING.** Sandbox-git-distrust note in the Build-Verification / session-start `git status` step (it instructs `git status` + `./gradlew check` at session start; add the caveat that in-sandbox git is unreliable and the Read tool is authoritative).
- **CONSISTENCY.** Message-protocol table (5 typed kinds) matches PM CLAUDE.md — good.

### 5.K — `coder/references/homesynapse-mental-model.md`
- **STALE (WRONG).** §2 event_id "`UlidCreator.getMonotonicUlid()`" → removed library; use `UlidFactory.monotonic()`. · §9 "`AttributeValue` … device model API module" → `com.homesynapse.value`. · §10 "16 populated, 3 scaffold stubs" + "Status as of M3.1" → 22 modules, value-model populated, only dashboard stub. · §8 subsystem map omits value-model and is "13 subsystems" (Doc 15 now 15). · masthead.
- **MISSING.** A value-model entry in §8/§9/§10; the event↔device-cycle-break rationale (why value-model is a leaf) is good mental-model material.
- **CONSISTENCY.** §2 correctly states CausalContext = 2 fields (actorRef on envelope) — this is the authority; fix deviation-and-quality §3 to match. The §2 `UlidCreator` line contradicts constraint-enforcement/coding-instruction-format/java-patterns (which use UlidFactory) — fix here.
- **HISTORICAL (flag).** SQLite 25-column schema (§6) is detailed and current; keep. Concurrency model (§5, AMD-26/27) current; keep.

### 5.L — `coder/references/java-patterns.md`
- **STALE (WRONG).** §1 `EntityId.generate()` does not exist (only `of`/`parse`; generate via `new EntityId(UlidFactory.generate(clock))`) (src: EntityId.java). · §3 `withGlobalPosition` example uses the **old EventEnvelope shape** (separate correlationId/causationId, no categories/causalContext/actorRef) while the §3 record def correctly shows the **14-field** shape — fix the example. · §5 INSERT example is 12-column vs the real **25-column** schema, and uses `setInt(7, subjectSequence())` on a `long` field — illustrative but misleading; either annotate as simplified or update. · §10 module-naming "`homesynapse-{subsystem}` / `homesynapse-{subsystem}-api`" doesn't match actual Gradle paths (`core:event-model`, `platform:platform-api`, `integration:integration-api`) or JPMS names (`com.homesynapse.*`). · §10 version-catalog versions are illustrative/possibly stale (low stakes). · masthead.
- **MISSING (primary).** A new section — **"JPMS exports discipline & the `requires transitive`↔`api` lockstep"** — capturing the 3×-recurring lesson (M2.9/M3.6e.1/M5-A): (a) a public class in an exported package must not expose package-private or non-transitively-required types on its API surface (else `-Xlint:exports`→`-Werror` fatal); (b) `requires transitive` ⇔ Gradle `api()`, plain `requires` ⇔ `implementation()` — must agree; (c) when handed a verbatim `module-info` to embed, scan exported public types for foreign-module supertypes/returns/params first; (d) `-Xlint:exports` is main-source-only (green tests don't clear it); (e) the seam-isolation pattern for JDK APIs that compile but are unsupported at runtime (M5-A sd_notify/AF_UNIX-datagram → M13). · The **`(Type) null` cast-only-when-disambiguating** `-Werror` note (coder-lessons M5-A). · The **Spotless reality** note (M4.C: header + removeUnusedImports + trailing-ws + eof only; no import-order/format — audit every added import incl. Javadoc `{@link}`).
- **CONSISTENCY.** §11 Clock/NO_DIRECT_TIME_ACCESS is excellent and current — the canonical source for PM §4c; keep. §12 (default methods + "Platform Module ≠ Auto-Required") current; keep. Fix §1 ULID to agree with constraint-enforcement (and correct mental-model/deviation-and-quality to match the corrected §1).

### 5.M — `coder/references/testing-standards.md`
- **STALE (WRONG).** Examples use `EntityId.generate()` (lines ~69/95/184/206) — non-existent; use `new EntityId(UlidFactory.generate(clock))`. · §3 performance-test examples call `System.nanoTime()` directly in test methods, which **§8 of this same file forbids** in non-whitelisted modules — internal contradiction; mark those examples whitelisted-only or rewrite. · §8 "`homesynapse-test` module" naming → actual `testing:test-support` (`com.homesynapse.test..`). · event-type string examples use dot form "device.state_changed" while legacy events are snake_case (note the dual convention). · masthead.
- **MISSING.** Note that the live ArchUnit rule set has grown (Rule 10 `NO_JACKSON_IN_DOMAIN_MODEL`, `QUERY_SERVICE_READ_ONLY`, `REST_ENDPOINTS_NO_EVENT_PUBLISHING`) — §5's two illustrative rules are a stale subset; either generalize ("see HomeSynapseArchRules.java for the authoritative set") or refresh.
- **CONSISTENCY.** §8 Clock discipline + §9 capability hooks + §10 shape tests all match coder-lessons and java-patterns §11/§12 — good; only the code *examples* are stale.
- **HISTORICAL (flag).** None; test discipline is durable.

### 5.N — `coder/references/deviation-and-quality.md`
- **STALE (WRONG).** §1 LTD-04 checklist "`getMonotonicUlid()` for event IDs, `getUlid()` for entity IDs" → removed `ulid-creator` API; use `UlidFactory.monotonic()` / `UlidFactory.generate([Clock])`. · §3 CausalContext Javadoc example shows **3 fields incl. `@Nullable Ulid actorRef`** → source is **2-field** (actorRef on envelope). · masthead.
- **MISSING.** Extend **§6 Source Trust Hierarchy** with the **sandbox-git-distrust** rule (in-sandbox `git status`/`diff` unreliable — line-ending churn, file mangling; Read tool authoritative; host-git commit) — §6 is the natural home and currently stops at handoff-vs-source. · Optionally the deviation-can-be-more-correct-than-spec note (mirrors review-and-quality).
- **CONSISTENCY.** Severity model (INFO/REVIEW/BLOCKING) matches coder SKILL §6 + PM review-and-quality §3 — good. The CausalContext shape and the ULID API are the two internal contradictions to resolve (with mental-model §2 and constraint-enforcement respectively).

### 5.O — `coder/references/freshness-preflight.md`
- **STALE.** masthead. The 6 checks are current and correctly scoped as the Coder subset; Check 6 (dual mirror) accurate.
- **MISSING.** If the PM preflight gains the **source round-trip check** with Coder-side implications, mirror the relevant subset here (per the file's own §7 mirroring rule).
- **CONSISTENCY.** Cites the skill-sync as **WUCP "Step 10"** (agrees with PM preflight + WUCP body; differs from CLAUDE.md/review-and-quality "step 11") — §7. Otherwise fully aligned with the PM preflight's shared-protocol contract.

---

## 6. Lessons-to-Promote Ledger

Per-entry disposition for the three lesson logs (only entries that imply a skill change shown; the rest stay as history). "Promote" = encode into the named skill file.

**coder-lessons.md**
- 2026-04-10 (NO_DIRECT_TIME_ACCESS on test code; `./gradlew check` is the authoritative gate) — **already encoded** (java-patterns §11, testing-standards §8, PM §4c). No action.
- 2026-04-15 M2.9 (`-Xlint:exports`; public-class-in-exported-package → package-private) — **promote** to new java-patterns JPMS-exports section (occurrence #1 of 3).
- 2026-05-18 M3.5a G4 (visibility STOP-gate) — **already propagated** to coding-instruction-format §STOP-on-Mismatch. No action.
- 2026-05-19 M3.6a (grep ALL test call-sites before a signature change) — **promote** as a supporting note to the P2 fan-out survey.
- 2026-05-22 M3.6e.1 (the `requires transitive`⇔`api` corollary) — **promote** to java-patterns JPMS-exports section (occurrence #2).
- 2026-06-05 M4.C (event-type set ⇒ 7 lockstep sites incl. production composition root) — **promote** as the worked example in the P2 survey (coding-instruction-format).
- 2026-06-05 M4.C (Spotless enforces only header/unused-imports/ws/eof) — **promote** to java-patterns (build-discipline note).
- 2026-06-06 M5-A (sd_notify/AF_UNIX-datagram seam isolation; `(Type) null` cast under `-Werror`; `-Xlint:exports` occurrence #3) — **promote** to java-patterns JPMS-exports + a "JDK-API-compiles-but-unsupported" seam note.
- (default-method evolution, contract-test hooks, shape tests, JDK-module-requires) — **already encoded** (java-patterns §12, testing-standards §9/§10). No action.

**pm-lessons.md**
- 2026-04-11 (deferred-gate must be tracked; test code in arch scope) — **already encoded** (§4b, §4c). No action.
- 2026-05-17 (shape-test inclusion, default/abstract spec, ArchUnit-citation verification) — **already encoded** (coding-instruction-format §Interface Evolution Checklist). No action.
- 2026-05-21 (single compile-and-commit framing; ≥3-prereq split; pre-verifications artifact) — **promote**: the framing → P1; the pre-verifications artifact → a pointer in PM SKILL §3.
- 2026-05-30 (deviation can be more-correct-than-spec; log erratum as Open Item) — **promote** to review-and-quality §3.
- 2026-05-31 (the fixed **six-file** closeout; backlog+weekly are the under-updated ones) — **promote** to P3 (WUCP/review-and-quality).
- 2026-06-07 M5-A (`requires transitive`↔`api` lockstep as an **instruction-authoring defect**; the shift-left targeted `compileJava`; keep dispatching independent owner-doc review) — **promote**: authoring check → coding-instruction-format + constraint-enforcement; shift-left → P5; keep-review → already in review-and-quality (reinforce).

**strategic-lessons.md**
- 2026-03-20 (context-rot audits; "every path referenced in skill files actually exists") — supports a **recurring skill/context audit** recommendation (see §10 / OQ-5); this audit is an instance.
- 2026-04-10/04-11 (milestone sizing ~3h; BCP→WUCP; preflight) — sizing feeds **P1**; rest already encoded.
- 2026-05-28 (source round-trip; fabricated type survived closeouts) — **promote** to freshness-preflight (new check), per the lesson's own recommendation.

---

## 7. Consistency Issues Between the Two Skills

1. **WUCP step numbering for the skill-sync check.** WUCP body Step 10 + both freshness-preflights say **"Step 10"**; PM CLAUDE.md + review-and-quality §6 + the WUCP Quick-Reference Card say **"step 11"**. Same step, two schemes (the divergence is whether Step 0/preflight is counted). Not load-bearing, but it will confuse cross-references. **Fix:** pick the WUCP body's 0-indexed scheme (preflight = Step 0; skill-sync = Step 10) and align CLAUDE.md, review-and-quality, and the Quick-Ref to it. (The WUCP file is `context/protocols/`, not a skill dir — see OQ-1.)
2. **ULID API contradiction.** constraint-enforcement + coding-instruction-format + java-patterns §1 (corrected) use `UlidFactory.monotonic()`/`.generate()`; mental-model §2 + deviation-and-quality §1 use the removed `UlidCreator`/`getMonotonicUlid()`/`getUlid()`. Converge on `UlidFactory` everywhere.
3. **`CausalContext` shape.** mental-model §2 (2-field, correct) vs deviation-and-quality §3 (3-field, stale). Converge on 2-field.
4. **`AttributeValue` location.** Must be `com.homesynapse.value` in both mental-model §9 and cross-subsystem-awareness §3 (and any module read-table).
5. **Module inventory / scaffold status.** One canonical statement ("22 Gradle modules; value-model added; only dashboard is a scaffold stub; per-module counts live in MODULE_CONTEXT headers") must be reflected identically in repo-state-protocol §1C, mental-model §8/§10, PM SKILL §0 table, and coder SKILL read-table.
6. **§4c arch-rule reminder.** PM SKILL §4c (module enumeration) + coder SKILL Phase-3 rules + java-patterns §11 + testing-standards §8 must list value-model consistently among non-whitelisted modules (whitelist text itself is correct and unchanged).
7. **Design-doc count & Phase-2 close date.** "14"→"15 (Doc 15 Draft)" and the 2026-03-20-vs-03-22 date must be stated consistently across CLAUDE.md (both), repo-state-protocol, mental-model.
8. **The two freshness-preflights** are otherwise correctly differentiated (PM 10-check superset, coder 6-check subset) and agree on the shared-protocol contract; if a source-round-trip check is added to the PM file, mirror the Coder-relevant part and update both output-format blocks (per each file's §7).

---

## 8. Benchmarks / Evals Impact

**The `benchmarks/` directory is NOT an eval harness for these two skills.** Per `benchmarks/README.md`, it tests the **HomeSynapse Core Claude Project's** architectural knowledge (Nick pastes a generated prompt into a fresh Claude Project conversation; Cowork grades against answer-keys). There is no `evals.json` / eval-viewer harness exercising `nexsys-coder`/`nexsys-project-manager`. **Therefore editing the skills does not mechanically require re-running these benchmarks**, and there is no skill-eval to break.

However: (a) the benchmark **answer-keys encode the same ground-truth facts** (Category A counts/locations, Category C "does-not-exist" negatives) and are themselves **stale** — masthead `2026-05-20 / 25bc23b`, last comprehensive `benchmark-4-2026-05-17`, "Next Scheduled: post-M3.2 smoke" — i.e., M3-era while we're at M5. The corrected facts in §2 (133 invariants, 22 modules, value-model exists, AttributeValue relocated, etc.) are precisely what those keys should assert. (b) The regression bank includes "ghost rule" negatives (REG-003 event-bus ArchUnit rule that doesn't exist) — the same fabrication class this audit fixes.

**Recommendation (open question, not in-scope to edit here):** the benchmark answer-keys belong to the Claude-Project-knowledge track and overlap the parallel session's docs/knowledge work — flag for refresh **alongside** the skill update (so a post-M5 smoke test validates the corrected facts), but do **not** edit them inside this skill-audit footprint. If desired later, the `skill-creator` description-optimization loop could add genuine trigger-evals for the two skills, but that is new scope and lower priority than domain accuracy.

---

## 9. skill-creator Structural Notes (form — secondary to domain accuracy)

- **Progressive disclosure is healthy.** Both SKILL.md bodies are under the 500-line guideline (PM 359, coder 327); both have proper YAML `name`+`description` frontmatter with trigger-rich, appropriately "pushy" descriptions; references are loaded on-demand. No structural overhaul needed.
- **Large references could gain a TOC.** Per skill-creator (">300 lines → include a table of contents"): `coding-instruction-format.md` (450), `java-patterns.md` (593), `testing-standards.md` (463), `deviation-and-quality.md` (357), `homesynapse-mental-model.md` (305) qualify. Low priority; add if a file is being substantially edited anyway.
- **Description currency.** Both descriptions are still accurate for Phase 3 / M5; no change required (the coder description's "Phase 2 interface specs" clause is fine as the AMD-correction path persists).
- **Watch the line budget.** Adding the JPMS-exports section to java-patterns (already 593) pushes it well past 500 — consider splitting java-patterns into a JPMS/build sub-reference, or accept the over-length (skill-creator says the 500 figure is approximate). Nick's call.

---

## 10. Prioritized, Sequenced Update Plan (Phase 2 — on approval)

Sequenced so that the canonical facts land first, then the corrections that depend on them, then the new conventions, then anchors. Each tranche is a coherent review unit.

> **Optimization principle (approved):** the skills load into every session, so leanness compounds — keep new conventions terse and scannable (rules, not prose), replace drifting counts with MODULE_CONTEXT pointers (OQ3/OQ7), condense the historical modes (OQ2), and prune genuinely-dead refs rather than just flag them.

**Tranche 0 — Pre-req (before editing).** Confirm OQ-1..6 below. Re-run `diff -rq` to confirm the mirror is still PASS at edit time (it is now). Re-read HEAD anchor (still `8028337` unless the parallel session commits a Core change).

**Tranche 1 — Ground-truth facts (highest leverage; everything else references these).** Apply §2 table corrections wherever they appear: invariants 133/32 + TO/BUS/PROJ/WRITER/SUB-ISO + INV-GA-02 (constraint-enforcement); LTD 18→19 (constraint-enforcement, coder CLAUDE.md); modules 19/20→22 + value-model + scaffold→dashboard-only + "counts live in MODULE_CONTEXT" (repo-state-protocol, mental-model §8/§10, PM SKILL §0 table, coder SKILL read-table); design docs 14→15 (both CLAUDE.md, repo-state-protocol, mental-model); milestone vocabulary M3/M4-complete→M5-window (PM SKILL Mode 3).

**Tranche 2 — Actively-WRONG fixes (§3.4).** ULID API → UlidFactory (mental-model §2, deviation-and-quality §1); EntityId.generate() → `new EntityId(UlidFactory.generate(clock))` (java-patterns §1, testing-standards examples); AttributeValue → value-model (mental-model §9, cross-subsystem §3); CausalContext → 2-field (deviation-and-quality §3); invariant taxonomy OB→TO + 133/32 (constraint-enforcement); dead traceability TEMPLATE path (PM CLAUDE.md, review-and-quality — pending OQ-1).

**Tranche 3 — Adopted proposals P1/P2/P3/P6 (D8) + P4/P5.** P2 survey section + §4c block + ⛔gate/diff conventions + authoring check → coding-instruction-format; P1 + P6 → PM SKILL; P3 ticked-artifact + fixed-six → review-and-quality (+ WUCP, pending OQ-1) + PM CLAUDE.md; P4 → constraint-enforcement + review-and-quality; P5 → PM SKILL §4b + coding-instruction-format Build-Discipline + coder build notes.

**Tranche 4 — Hard-won conventions (§3.5 / §6).** New java-patterns "JPMS exports discipline & requires-transitive↔api lockstep" section (+ cast-under-Werror, Spotless reality, seam-isolation) + cross-ref from constraint-enforcement JPMS rule + coder SKILL read-table; sandbox-git-distrust → deviation-and-quality §6 (+ repo-state-protocol §4, both CLAUDE.md build steps); source-round-trip check → freshness-preflight (PM, mirror to coder); event-naming-convention note → cross-subsystem.

**Tranche 5 — Consistency & structural.** Resolve §7 items (numbering scheme, the 4 internal contradictions, module-inventory single-source); fix constraint-enforcement duplicate "## 4"; optional TOCs for >300-line refs; demote (not delete) Mode 1/Mode 2 + coder Phase-2 framing per HISTORICAL flags (pending OQ-2).

**Tranche 6 — Anchors & mirror.** Refresh all 15 mastheads to `2026-06-07 / <HEAD>`. Then surface the **dual-skill mirror step**: Nick performs the copy to `.claude/skills/nexsys-{coder,project-manager}/`; PM runs `diff -rq` per WUCP Step 10 to confirm PASS. Update benchmarks **only** if Nick folds that into this commit (recommend separate, parallel-session-owned). Provide commit message(s) — skill changes as their own commit, separate from the parallel session's context/docs work.

---

## 11. Open Questions for Nick

1. **WUCP + traceability TEMPLATE are in `context/protocols/` / shared state, not the skill dirs.** Two skill files (PM CLAUDE.md, review-and-quality) cite the dead `context/traceability/TEMPLATE.md`, and the WUCP body (Step 2/Step 12) has the same dead ref + the "step 10 vs 11" scheme. I can fix the **skill-side** citations (point to `homesynapse-core/docs/traceability/` and note no template exists, or to wherever you want the template recreated), but **should I touch `context/protocols/work-unit-completion-protocol.md`?** It's outside the skill dirs and may be the parallel session's territory. Options: (a) I fix only skill-side refs and log a cross-session note for WUCP; (b) you authorize me to also fix WUCP; (c) leave WUCP to the parallel session. **PM lean: (a).**
2. **Mode 1 / Mode 2 (PM) and the coder Phase-2 framing** — demote/condense to "AMD-correction + design-doc-supersession context," or keep verbatim? They're load-bearing for AMD work but read as live primary modes. **PM lean: demote/condense, keep the content.**
3. **Per-module type counts** — replace hardcoded counts (device-model 57, event-model 46, etc.) with "see MODULE_CONTEXT.md header," or refresh the numbers to current and keep them inline? **PM lean: replace with the pointer** (they drift by construction — that's the 2026-05-28 lesson).
4. **java-patterns length** — it's already 593 lines and the JPMS-exports section will push it well over the 500-line guideline. Split into a `references/jpms-and-build.md` sub-reference, or accept over-length? **PM lean: accept for now; split later if it keeps growing.**
5. **Benchmark answer-keys** — out of scope for this skill-audit (Claude-Project-knowledge track, overlaps the parallel session). Confirm you want them refreshed **separately** post-M5 rather than in the skill commit. **PM lean: yes, separate.**
6. **AMD-65→AMD-87 / Doc-15 phrasing** — the M5 window is mid-fold/ratify (watermark AMD-64 → 87 pending). Should skill examples that reference amendment numbers use AMD-87 now, or wait until ratification lands so the skills don't cite a still-PROPOSED number? **PM lean: use neutral phrasing ("the current amendment watermark") and avoid pinning a specific in-flight AMD number in the skills.**
7. **Capability-hierarchy "16 types"** (cross-subsystem §2) — I did not fully re-derive this count from device-model source (header says device-model "57 types" but didn't isolate the Capability permit count). Flagging as **unverified**; want me to source-confirm before editing, or drop the specific number for a pointer?

---

## 12. Footprint & Non-Collision Statement

- **Written this session:** only `context/audits/2026-06-07_skill-update-audit.md` (this file).
- **Not touched:** any skill file (Phase 2 gated on approval); `context/handoff/*`, `context/status/PROJECT_SNAPSHOT.md`, `homesynapse-core-docs/*` (the concurrent M5 fold+ratify session's territory).
- **Mirror baseline at audit time:** `diff -rq` clean (Check 9 PASS) for both skill trees — Phase 2 will reintroduce a STALE-pending-sync state that clears when Nick runs the external mirror copy.
- **STOP.** Per the brief: no skill edits until Nick reviews and approves this plan.

---
*End of Phase 1 audit. Verified against `homesynapse-core` HEAD `8028337` and the hivemind/docs working trees, 2026-06-07.*

---

## 13. Phase 2 Execution Log (2026-06-07 — applied after Nick's approval)

**Scope executed:** all six tranches across the 15 skill files, as a single skill-only edit set separate from the parallel M5 session's context/docs work. OQ resolutions applied: **OQ1** skill-side only (no `context/protocols/` edit); **OQ5** benchmarks deferred to the Claude-Project-knowledge track; **OQ6** neutral amendment phrasing (no pinned in-flight AMD number); optimization principle applied throughout (**OQ2** Modes 1&2 condensed; **OQ3/OQ7** drifting counts replaced with MODULE_CONTEXT-header pointers; dead skill-side refs pruned, not just flagged).

**Files edited (15), all mastheads → `2026-06-07 / 8028337`:**
- **PM** — SKILL.md (M5 vocab; value-model read-row; P1/P5/P6; pre-verification pointer; Modes 1&2 condensed; §4c +value-model) · CLAUDE.md (WUCP 0-indexed, skill-sync = Step 10; dead traceability path repointed; 15 docs; P3 ticked-six) · coding-instruction-format.md (canonical P2 survey section; §4c block; ⛔gate + module-info PROPOSED-DIFF + requires-transitive↔api authoring check; masthead conventions; P5; heading generalized) · constraint-enforcement.md (133/32 + TO/BUS/PROJ/WRITER/SUB-ISO + INV-GA-02; LTD 18→19 + LTD-19 row; JPMS lockstep; dup-§4 fixed; P4 §6) · repo-state-protocol.md (22 modules + value-model; scaffold→dashboard-only; counts→pointers; 15 docs; sandbox-git) · cross-subsystem-awareness.md (AttributeValue→value-model; shared-ID list; value-model leaf; event-naming convention) · review-and-quality.md (WUCP 0-indexed; traceability fixed; P3; P4; correctness-over-conformance) · freshness-preflight.md (new Check 11 source-round-trip).
- **Coder** — SKILL.md (module status→dashboard-only + value-model read-row; Phase-2→AMD-only; JPMS xref) · CLAUDE.md (sandbox-git caveat; 15 docs; LTD 19) · homesynapse-mental-model.md (UlidFactory not UlidCreator; AttributeValue→value-model; module status) · java-patterns.md (EntityId.generate removed→correct API; 14-field envelope; 25-col INSERT caveat; module-naming; **NEW §13 JPMS exports & lockstep** + cast/Spotless/seam notes) · testing-standards.md (EntityId.of(UlidFactory.generate(clock)); System.nanoTime/whitelist caveat; test-support naming; archrule-set note) · deviation-and-quality.md (LTD-04 UlidFactory; 2-field CausalContext; §6 sandbox-git) · freshness-preflight.md (Check 7 source-round-trip mirror).

**Verification:** zero `25bc23b` remaining in either skill tree; all 15 mastheads at `8028337`; footprint clean (no edits to `context/handoff`, `context/status`, `context/protocols`, or `homesynapse-core-docs`).

**Deferred to a regular PM session (NOT done here, per OQ1 — outside the skill dirs; parallel session active in `context/`):**
- `context/protocols/work-unit-completion-protocol.md`: (a) Step 2 still cites the removed `context/traceability/TEMPLATE.md` — repoint to `homesynapse-core/docs/traceability/` (no template); (b) reconcile its internal numbering — the body is 0-indexed (skill-sync = Step 10) but the Quick-Reference Card is 1-indexed (skill-sync = 11). The skills are now aligned to the body's 0-indexed scheme.
- **Check-9 / Step-10 wording nuance (observed at mirror-diff time):** a normal PM edit to an *existing* skill file makes `diff -rq` report `Files … differ` (not `Only in …`), which the current Check-9 text labels CONFLICTED. For files the PM edited *this session* that is the benign STALE/pending-sync state, not an integrity failure. Recommend a one-line clarification (edited-this-session ⇒ STALE; `differ` on an untouched file ⇒ CONFLICTED) in a future pass — deliberately not folded into this commit to keep it scoped.

**Concurrency reconciliation (2026-06-07, late).** The parallel M5-A session ratified **AMD-86 + AMD-87** while these skill edits were in flight, which raised the invariant total **133/32 → 135/34** and flipped **Doc 15 Draft → Locked** (watermark → AMD-87). Seven "as-of" figures written earlier this session were therefore stale-on-arrival; they have been **de-pinned** (invariant count → "read §0.3/§17, ≈135/34 and rising" in constraint-enforcement.md; "Doc 15 Draft" → "15 design docs, all Locked" in PM SKILL Mode 1, both CLAUDE.md, cross-subsystem-awareness, repo-state-protocol). This is itself a worked example of why the optimization principle (counts → MODULE_CONTEXT/source pointers, neutral amendment phrasing) and the new source-round-trip check matter: two concurrent sessions raced the invariant count. No pinned watermark number was written into the skills (neutral phrasing held).

**Mirror state:** `diff -rq` now reports **15 `differ` entries** (8 PM + 7 coder) — expected post-edit; clears when Nick runs the external mirror sync. **Next step (Nick):** copy both source trees to `.claude/skills/nexsys-{coder,project-manager}/`, then the PM re-runs `diff -rq` (both empty = PASS, restoring Check 9).

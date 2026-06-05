<!--
file: context/process/HomeSynapse_Development_Method_v1.md
purpose: The HomeSynapse Development Method (HSDM) — §2–§8. Formalizes the four-surface workflow, context architecture, work-unit lifecycle, agent-instruction standards, failure-mode defenses, governance/evolution, and the prioritized adoption roadmap. Companion to the Constitution (§1).
audience: Nick, Cowork, CORE Project, DOCS Project, Claude Code
update-cadence: §2–§7 rare (method amendment); §8 roadmap is a living backlog
state-type: reference / governance
status: CURRENT — v1 (2026-05-31)
companion: project-knowledge/HomeSynapse_Development_Method_Constitution_v1.md (§1 — the principles)
grounded-against: HEAD c99b425 / watermark AMD-53 / projectionVersion 5 (Workstream A complete; M4.B-S1 committed e73e199 per coder-handoff — see §4 drift note)
-->

# HomeSynapse Development Method — v1 (§2–§8)

This is the reference half of the HomeSynapse Development Method (HSDM). The Constitution (§1, separate file) states the non-negotiable principles; this document states how they are realized. It is a reference, not a tutorial: structured, citable by ID, and grounded in artifacts that already exist. Where a section recommends a change, it points to a roadmap item (`R{n}`) in §8 rather than asserting the change is already in place.

**Citation:** sections `§2`–`§8`; surfaces `S-COWORK`/`S-CORE`/`S-DOCS`/`S-CODE`; recommendations `R1`–`R9`. Principles are cited as `HSDM-P{n}` (Constitution).

---

## §2 — The Surface Architecture

HomeSynapse development runs across **four surfaces**, not the older "three-surface" model. They are **not peers** — they form an authority hierarchy, and only one of them touches the working tree.

```
Nick  (strategic authority, compile gate, commits, ratification)
  │
Cowork  (orchestration + documentation — holds both repos, runs the preflight, generates prompts)
  │
CORE Project  +  DOCS Project   (read-mostly knowledge/analysis surfaces — reviews, instructions, research)
  │
Claude Code   (the only surface that writes the working tree)
```

The hierarchy determines who overrides whom when a disagreement surfaces: **Nick > Cowork > Projects > Claude Code.** A lower surface that believes a higher one is wrong raises a structured finding (HSDM-P9); it does not act unilaterally.

### S-COWORK — Cowork (orchestration + documentation)

- **Owns:** ground truth. Both repos are mounted with live file tools. Cowork runs the freshness preflight, knows the authoritative HEAD/watermark/`projectionVersion`, generates the prompts sent to the Projects and Claude Code, performs documentation/governance work products (PM Mode-1/Mode-3), and executes WUCP Phase 2.
- **Must never:** run the build gate as authoritative (it can reason about `./gradlew check`, but Nick runs it), commit/push, or treat a Project's reply as ground truth without verifying surprising claims against source (HSDM-P4).
- **Communicates via:** generated coding instructions (to Claude Code), review/assessment prompts + source companions (to the Projects), typed messages and handoffs (to all).
- **Reads/writes:** reads everything; writes `nexsys-hivemind/` and `homesynapse-core-docs/` (governance, design, process); does **not** write Java.
- **Context management:** holds the smallest high-signal set per task; embeds the exact source slice each question needs (source-companion pattern); distills Project replies to findings (HSDM-P9), never raw transcripts.

### S-CORE — "HomeSynapse Core · Implementation (CORE)" Project

- **Owns:** second opinions on Java/JPMS/tests/ArchUnit/refactor risk; implementation verification against an embedded contract.
- **Must never:** claim to have run a build; fabricate a JPMS module name or a type (HSDM-P4); assume design intent that was not embedded.
- **Communicates via:** verdict-first findings with `file:line` evidence, returned to Cowork.
- **Reads/writes:** reads its curated spine (MODULE_CONTEXTs, `module-info.java`, coder references) + the per-question source companion; writes nothing.
- **Context management:** standing spine + JIT companion; treats the per-prompt HEAD/watermark/`projectionVersion` header as the only source of "now."

### S-DOCS — "HomeSynapse Core · Design & Governance (DOCS)" Project

- **Owns:** design-document reasoning, amendment authoring/ratification second opinions, research assessment, invariant/decision adjudication, naming/glossary.
- **Must never:** invent an AMD/INV/LTD id or a doc section; re-litigate a ratified decision; guess code state (it asks for the embedded excerpt).
- **Communicates via:** RATIFY-AS-IS / RATIFY-WITH-EDITS / REJECT verdicts with precise `§`/AMD/INV citations, returned to Cowork.
- **Reads/writes:** reads its curated spine (design docs, amendments, invariants, glossary) + companion; writes nothing.
- **Context management:** same as CORE.

### S-CODE — Claude Code (implementation)

- **Owns:** writing the working tree — production Java and tests, MODULE_CONTEXT updates, WUCP Phase 1.
- **Must never:** run `git commit`/`push`/`gradlew` (denied by `.claude/settings.json`); change a Phase-2 interface or behavioral contract without escalation; defer a build gate without flagging it.
- **Communicates via:** completion reports + WUCP Phase 1 checklists + typed messages, returned to Cowork/Nick.
- **Reads/writes:** reads the coding instruction + named MODULE_CONTEXTs/source; writes Java, tests, MODULE_CONTEXT, handoffs.
- **Context management:** Tier 1/2/3 loading (§5); source is authoritative over its own memory (HSDM-P4).

### The CORE↔DOCS boundary

The two Projects **cannot see each other's knowledge bases by design.** Context crosses the boundary only via (a) Cowork embedding the cross-repo slice into the prompt (source companion), and (b) the shared spine present in both (invariants, quick references, glossary). This boundary is **model-agnostic in mechanism** (embedded text works for any model) but currently **operator-dependent in execution** — its correctness rests on whoever drives Cowork remembering to embed the right slice and route by *what the verdict is about*. That dependency is the subject of `R7` (a source-companion completeness checklist). A model swap does not break this boundary; a sloppy prompt assembly does.

---

## §3 — Context Architecture

### The file-based memory layer

State lives in files (HSDM-P1), in three reliability tiers (most-reliable first):

1. **Always-loaded brief (< 5K tokens):** role, operating rules, the invariant/decision spine, and a current-state *pointer*. The agent CLAUDE.md / custom-instruction briefs. 100% reliable.
2. **Curated knowledge spine:** a bounded, hand-picked set (MODULE_CONTEXTs, design docs, invariants, quick references) — never raw build trees. Refreshed at WUCP Phase 2.
3. **JIT source companion:** the exact working-tree excerpt a question needs, embedded per prompt by Cowork. The reliable cross-repo bridge; does not depend on the GitHub connector.

The connector is a best-effort bonus, **never load-bearing.** The authoritative memory files and their update obligations are tabulated in `strategic-context-map.md §8` (Staleness Rules). The canonical "now" is the current-state stamp (`R3`), not any narrative file.

### Context budget

The binding constraint is context rot past ~100–150K tokens. The methodology stays within budget by: keeping each brief < 5K; keeping the spine bounded and non-monotonic (new milestone artifacts replace stale ones); embedding only the slice a question needs; and distilling replies to findings. One sharp question per prompt, long material near the top in tags, the ask last.

### Compaction strategy

Compaction is currently applied well at the spine level (MODULE_CONTEXT is the curated layer) but **three artifacts grow monotonically and need a cap-and-archive convention** (`R5`): MODULE_CONTEXT *header lines* (now paragraph-long changelogs), the PROJECT_SNAPSHOT header comment + Recent Session Log, and pm-handoff's stacked "This Session" entries. The rule to adopt: a header states *current state* at fixed length; the *changelog* moves to git history or a separate bounded section; session logs are capped with an archive cadence.

### Cross-session reconstruction

A fresh session bootstraps by: (1) running the freshness preflight (HSDM-P7); (2) reading the current-state stamp for HEAD/watermark/`projectionVersion`/frontier-WU; (3) loading Tier-1 context. Today reconstruction depends on several narrative files being mutually consistent, and they drift between closeouts (see §4 drift note). `R3` (single current-state stamp diffed against `git log` by the preflight) makes reconstruction robust to that drift.

### Context Architecture v2 (the pruning plan)

A planned compression of the Projects' uploaded knowledge from ~97% → ~30–40% usage. As of v1 it exists only in session memory and cross-agent notes — **a direct HSDM-P1 violation**, and so its own first task is to be written down (`R4`). The plan: exclude Java source/test/fixtures from the CORE sync; exclude consumed research and superseded plans from the DOCS sync; replace full governance docs (Architecture Invariants, Locked Decisions) in the spine with the compressed Quick Reference indexes already drafted; keep `HomeSynapse_Current_State.md` out of the spine (it drifts — the per-prompt header carries "now"). The closest existing on-disk artifacts are `two-project-claude-architecture.md` §8 and the strategic-context-map staleness rules.

---

## §4 — The Work Unit Lifecycle

A **work unit (WU)** is a single compile-and-commit unit with test coverage (HSDM-P6). The lifecycle from brief to merged code:

```
Task brief (Nick → Cowork)
  → PM scopes; freshness preflight PASS (else reconcile first)
  → Coding instruction (canonical format) issued to Claude Code
  → Claude Code: tests-first → implementation → WUCP Phase 1 (Coder closeout)
  → [compile gate: ./gradlew check — Nick, or explicitly DEFERRED + tracked]
  → PM review against source (not the report) → WUCP Phase 2 (PM closeout)
  → Nick commits
```

### Spec/plan gates implementation

A WU does not begin until its governing spec is in place: the design doc is Locked and any controlling amendment is RATIFIED. Implementation that would require violating a locked decision triggers the amendment process *before* coding (the M4.0b-4 event→device cycle is the model: a STOP-gate caught a defect in a ratified amendment, which was corrected by erratum + relocation before implementation proceeded). This is the constitution→spec→plan→tasks→implement discipline (HSDM-P5, P10).

### The coding instruction

The canonical format (`project-manager/references/coding-instruction-format.md`) is the PM's primary quality-control tool. Load-bearing features:

- **Files-to-Read** lists MODULE_CONTEXT.md *and* verbatim `module-info.java` for the target and every dependency (type names are insufficient — module names get fabricated; the Research-6 lesson).
- **STOP-on-Mismatch gates:** the Coder reads named source files and confirms they match expectations (including the `public` modifier, not just type existence) before writing; divergence halts and reports.
- **Settled decisions** are embedded as constraints, not re-opened questions.
- **Binary success criterion:** an unambiguous DONE test.
- **"Coder Pushback Welcome":** technical pushback is explicitly invited (HSDM-P9 in practice — the Coder sees implementation-level truth the PM may not).

### Tests, CI, and static verification at each stage

- **Authoring:** tests first; the test compiles and fails for the right reason before implementation (`testing-standards.md §1`).
- **Implementation:** must pass the tests; static rules apply to test code too (`NO_DIRECT_TIME_ACCESS` scans `src/test`).
- **Gate:** `./gradlew check` runs the suites *and* the static verifiers (ArchUnit, JPMS, `-Werror`, exhaustive switch) — the authoritative correctness gate (HSDM-P5).
- **Review:** PM reads every changed file against source (HSDM-P4), confirms cited INV/LTD/AMD, adjudicates deviations by severity (`[INFO]`/`[REVIEW]`/`[BLOCKING]`).

### Deferred build-gate tracking

The sandbox cannot run Gradle, so the gate is deferred to Nick's host by design. A deferral is **only safe if tracked**: the Coder flags `Deferred Build Gate` in the handoff; the PM copies it to pm-handoff Open Risks with a closure condition; **no WU M{x}.{y+1} is issued while M{x}.{y}'s gate is unresolved.** This rule exists because untracked deferrals shipped arch-debt through M2.2/M2.4 (the 2026-04-11 retrospective).

### Decomposition (the "one-giant-task" problem)

- The unit of work is *one compile-and-commit with test coverage* — if a brief spans two such boundaries, decompose before issuing (M3.1–M3.4 prompt-pattern lesson).
- If discovery reveals **≥3 prerequisite gaps** (assumed infrastructure that doesn't exist), split the WU rather than expanding scope silently (M3.6d → M3.6d-a + M3.6d-b). Surface it as an explicit decision; pre-empt with a `pre-verifications/` artifact when a brief depends on ≥3 source-state assumptions.

### The enforcement-cadence spectrum

The lifecycle's correctness depends on the gate (`./gradlew check`) and the closeout (WUCP Phase 2) firing — and today both are human/session-triggered, leaving a drift window. The methodology should move along this spectrum **without surrendering Nick's authority**:

- **Current — human-gated.** Nick runs the gate; the PM runs Phase 2. Correct but slow; drift accumulates between cycles.
- **Near-term — single-source "now."** The current-state stamp (`R3`) + preflight checks (`R2`) close the *multi-file disagreement* window so a fresh session never bootstraps from inconsistent state. (Low effort, no change to who runs the gate.)
- **Future — assisted gate.** An optional host hook (`R9`) runs `./gradlew check` + a snapshot-consistency lint and *assists* Nick; **Nick remains the override authority and the compile gate's owner.** This is model-transition insurance: it prevents a future weaker model from widening the deferred-gate window into shipped defects.

> **Live drift note (evidence, not a defect to rush-fix):** at v1 authoring, `coder-handoff.md` records M4.B-S1 committed `e73e199` with PM Phase 2 APPROVE, while `PROJECT_SNAPSHOT`, `pm-handoff`, and the `cross-agent-notes` top pointer still show `c99b425`/M4.0b-5 as the frontier. Four state files disagree on "now." The preflight would flag this (Check 3/6) at the next session start — which is exactly the point: the methodology *detects* the drift, but the detection is session-triggered. `R3`+`R2` make the disagreement impossible to act on unknowingly.

---

## §5 — Agent Instruction Design

### Size and structure

- Root `homesynapse-core/CLAUDE.md`: ~35 lines — non-negotiables on top, build/test prohibitions, key constraints, "read MODULE_CONTEXT before coding," completion-report shape. Keep root files tight (well under 300 lines).
- Custom-instruction briefs (CORE/DOCS): **< ~5K tokens**, enforced by rule. If a brief grows, move detail into the spine.

### Hierarchy and progressive disclosure

Instructions are layered so an agent loads the minimum and reaches for the rest just-in-time:

```
root CLAUDE.md (always)  →  per-agent SKILL.md + CLAUDE.md (role)  →  references/ (JIT by task)
MODULE_CONTEXT.md (per module touched)  →  module-info.java (verbatim, per module)
Tier 1 = always; Tier 2 = active work; Tier 3 = on-demand; never pre-load all governance/design docs
```

Root files carry non-negotiables and pointers; subdirectory files (MODULE_CONTEXT, references) carry depth. This is the established pattern and needs no change.

### Making instructions model-agnostic

- State rules as testable predicates, not aspirations (HSDM-P8): "no `synchronized`; use `ReentrantLock`," "exhaustive `switch`, no `default` arm," "inject `Clock`; tests use `Clock.fixed(...)`."
- Assume no model-specific capability in a permanent rule. Where a brief leans on a capability (long-context retrieval, steerability to "distrust your memory"), make the *defense* structural (embed the slice; cite `file:line`) so a weaker model degrades gracefully (HSDM-P3).
- **Single-source every constraint** (`R1`): the constraint list is restated in ≥6 places today (root CLAUDE.md, `project-instructions.md`, both SKILLs, both briefs, `constraint-enforcement.md`) and they have already drifted (stale "three-surface"; invariant count cited as 81 / ~94 / 104). Make the Quick References canonical; every other mention becomes a pointer; add a "last-verified-against-HEAD" line the preflight checks.

### Handling model-specific quirks without baking them in

Model-specific content is quarantined to clearly-marked, revisitable sections (HSDM-P3) — e.g., the Opus-4.6 pin and its benchmark rationale live in `two-project-claude-architecture.md §7` with an explicit revisit trigger, *not* in any permanent rule. The model-transition checklist (`R8`, §7) is the mechanism for re-evaluating such sections when the model changes.

---

## §6 — Failure Mode Defenses

For each characteristic LLM-development failure mode: how the methodology detects, prevents, recovers, and tracks it — and whether each defense is **model-agnostic** (holds under any model) or **model-dependent** (degrades with model quality). The model-dependent column is where a model swap raises risk and where `R9`/`R8` are the insurance.

| Failure mode | Detection | Prevention | Recovery | Tracking artifact | Defense type |
|---|---|---|---|---|---|
| **Hallucinated / misused APIs** | Compile error; PM/Project review can't locate cited `file:line` | Source Trust Hierarchy (`deviation-and-quality.md §6`); read source before writing a call; embed verbatim `module-info.java`; "never fabricate a module name" (CORE brief) | Coder corrects against source; lesson logged | `coder-lessons.md`; the 2026-03-22 benchmark | **Model-agnostic** (compile/JPMS) + model-dependent (residual fabrication rate scales with model) |
| **Constraint decay** (structural rules silently violated) | ArchUnit / JPMS / `-Werror` / exhaustive-switch fail `./gradlew check` | Static rules encode every structural constraint (HSDM-P2); JPMS makes some violations uncompilable | Red build; fix before commit | ArchUnit rule set; `HomeSynapseArchRules` | **Model-agnostic** (the strongest defense) |
| **Duplicate re-implementation** | PM/Coder finds an existing type during MODULE_CONTEXT read | "Read MODULE_CONTEXT before writing"; type inventories; CREATE-vs-merge judgment (M3.6c lesson) | Merge/redirect to existing type; `[REVIEW]` deviation | MODULE_CONTEXT inventories; `coder-lessons.md` | Model-dependent (relies on the agent actually reading + recognizing) |
| **Regressions on new features** | Full `./gradlew check`; contract suites fail | Tests-first; "grep all call sites before editing"; contract test suites define "correct" | Red build; fix; regression test added | contract tests; `coder-lessons.md` | **Model-agnostic** (tests) |
| **Overclaiming** ("done" without testing) | PM reviews against source, not the report; deferred-gate tracking | "Review against source, not the completion report"; deviation-severity honesty; deferred-gate-must-be-flagged rule | Gate run reveals reality; Open Risk tracked until GREEN | pm-handoff Open Risks; WUCP checklists | Model-dependent (PM/agent diligence) — `R9` makes it model-agnostic |

Two defenses need formalizing (`R2`): the **state-doc source round-trip** (every type name a state doc cites must `grep`-confirm in source — the 2026-05-28 fabrication lesson; preflight Check 7 covers MODULE_CONTEXT but not PROJECT_SNAPSHOT/Knowledge_Primer claims), and the **current-state consistency** check against `git log` (`R3`).

---

## §7 — Governance and Evolution

### Ownership

Nick is the DRI for the method (and the product). Cowork (PM role) is the executor: it applies the method, runs Phase 2, and drafts proposed changes for Nick's approval. The Projects review; Claude Code implements.

### How the method changes

The method evolves through the **same discipline as the product**, scaled down:

- A proposed change is written as a short amendment note (problem, proposed change, impact on the affected sections/principles, model-agnosticism effect).
- §1 (Constitution) principles change rarely and require Nick's explicit ratification; their IDs are permanent (HSDM-P10).
- §2–§7 change through a method amendment recorded in this file's changelog + a watermark line in the header.
- §8 (Roadmap) is a living backlog — items move PLANNED → DONE without ceremony.
- Versioning: the method is `v1`; a breaking restructure increments to `v2` with a migration note.

### The model-transition checklist (`R8`)

Before adopting a model change (upgrade, downgrade, or non-Claude), run and record:

1. **Smoke + benchmark:** run the known-answer smoke tests and the `benchmarks/` regression bank on the candidate model; compare scores to the incumbent.
2. **Protocol honoring:** confirm the candidate honors the freshness preflight and WUCP as session-start gates (does it run them when told?).
3. **Fabrication probe:** on a fixed probe (e.g., "list the typed-ID wrappers and their module"), measure fabrication rate vs the incumbent.
4. **Steerability:** confirm it complies with "trust the embedded excerpt over your memory" (HSDM-P4) on a planted source↔memory conflict.
5. **Review quality:** have it ratify a known, already-adjudicated amendment; compare its verdict + evidence to the recorded outcome.
6. **Long-context (if used for the Projects):** verify multi-fact retrieval over the spine is adequate, or fall back to source-companion-only routing.
7. **Decide:** pin / migrate / route-by-task. Update the quarantined model section (§2-doc §7) and the model-pin rationale. Re-run the preflight.

### Handling capability regressions

If a new model regresses on a capability the workflow leans on (e.g., long-context retrieval, as Opus 4.7 did vs 4.6 on MRCR-v2), the response is **architectural, not panicked**: lean harder on the model-agnostic layer (embed more, retrieve less; tighten STOP-gates; widen `R9` assistance) and quarantine the regression. The graceful-degradation property (HSDM-P2/P3) means a regression costs *iterations*, not *correctness*.

### The three horizons

The method must plan for its own evolution as the system scales.

- **Horizon 1 — current → M4 complete (solo dev, constrained hardware, local-first core).** The method is well-suited. Work: close the enforcement-cadence gap and formalize what exists. Governance tax is manageable at ~20 modules / ~53 amendments / 14 design docs.
- **Horizon 2 — integration expansion (Matter/Thread/Z-Wave, cloud-optional layers, multi-integration runtime).** The first real scaling test. Per-module governance overhead must not stay proportional to core modules — integration modules are constrained by the `IntegrationAdapter` HAL, not by novel architecture, so they get a **lighter, template-driven onramp** (`R6`, governance weight classes). Defining the core-vs-integration boundary is the single most important Horizon-2 decision.
- **Horizon 3 — AIoT / multi-hub / property scale (inference-as-events, `ComputeProvider` HAL, multi-site replication).** Model-agnosticism becomes load-bearing because *development agents and runtime AI share a design vocabulary*. The event-sourced architecture with typed payloads (AMD-52) is the right AIoT foundation; the `ComputeProvider` HAL (thin, CPU-first, modeled on `IntegrationAdapter`) means AI capabilities plug in under the *same* governance, module boundaries, and static enforcement as integrations. The thesis to hold: **the governance that keeps development agents from corrupting the architecture is the same governance that will keep runtime AI from corrupting the event log.**

---

## §8 — Recommendations and Roadmap

The adoption roadmap, structured as **Method Work Units (MWUs)** — each a single, independently-committable unit sized to one of Nick's blocks, applying the project's own WUCP discipline to the method itself. Ordered by (impact, effort, dependency). Most are `nexsys-hivemind`/docs changes that **skip the compile gate entirely** — Cowork drafts, Nick reviews and commits. Only `R6` (a decision) and `R9` (host build hook) need Nick's hands beyond a commit.

**Quick-wins batch (next block, no compile gate): `R1`, `R2`, `R3`, `R4`.**

| ID | Impact | Effort | Depends on | One line |
|---|---|---|---|---|
| R1 | HIGH | TRIVIAL | — | Single-source the constraint list |
| R2 | HIGH | TRIVIAL | R3 | Add source-round-trip + current-state checks to the preflight |
| R3 | HIGH | TRIVIAL | — | Single current-state stamp file |
| R4 | MED | TRIVIAL | — | Formalize the Context Architecture v2 pruning plan |
| R5 | MED | MODERATE | — | Cap-and-archive for growing artifacts |
| R6 | HIGH (H2) | MODERATE | Nick decision | Governance weight classes (core vs integration) |
| R7 | MED | MODERATE | — | Source-companion completeness checklist |
| R8 | HIGH (model swap) | MODERATE | — | Model-transition checklist |
| R9 | HIGH (model swap) | MODERATE | R3 | Optional assisted compile gate (host hook) |

### R1 — Single-source the constraint list
**Files:** canonical = `project-knowledge/Invariants_Quick_Reference.md` + `Decisions_Quick_Reference.md`; convert restatements in `homesynapse-core/CLAUDE.md`, `nexsys-hivemind/context/governance/project-instructions.md`, both SKILL.md, both custom-instruction briefs, and `constraint-enforcement.md` to pointers. Reconcile the invariant count (81 / ~94 / 104 → one number, source-verified). **Repos:** nexsys-hivemind + homesynapse-core. **Model-agnosticism:** removes a drift surface so a fresh agent on *any* model reads one true constraint source; kills the stale-instruction failure mode at its root.

### R2 — Strengthen the freshness preflight
**Files:** `project-manager/references/freshness-preflight.md` (+ coder mirror). Add **Check 11 (state-doc source round-trip):** every type/class name a state doc cites must `grep`-confirm in `homesynapse-core`; quantitative claims regenerated from source, not copied. Add **Check 12 (current-state consistency):** diff the current-state stamp (`R3`) against `git log` head. **Repo:** nexsys-hivemind. **Model-agnosticism:** catches fabrication and state drift regardless of model — converts a model-dependent defense (human notices) into a checklist any model runs.

### R3 — Current-state stamp file
**Files:** new `context/status/CURRENT_STATE_STAMP.md` (tiny: HEAD, watermark, `projectionVersion`, frontier-WU, last-verified). Updated at WUCP Phase 2 Step 6; read first by every session; diffed by the preflight (`R2` Check 12). **Repo:** nexsys-hivemind. **Model-agnosticism:** one machine-checkable source of "now" that any model reads; closes the four-file disagreement window (the `e73e199`/`c99b425` case).

### R4 — Formalize the Context Architecture v2 pruning plan
**Files:** new `context/process/Context_Architecture_v2_Pruning_Plan.md` capturing the spine-pruning plan currently in session memory (exclude Java source/test/fixtures from CORE sync; exclude consumed research/superseded plans from DOCS sync; replace full governance docs with Quick Ref indexes; target ~30–40% usage). **Repo:** nexsys-hivemind. **Model-agnosticism:** moves a load-bearing plan from session memory to the filesystem (HSDM-P1), so any session can execute it.

### R5 — Cap-and-archive for growing artifacts
**Files:** a short convention note + apply it to `PROJECT_SNAPSHOT.md` (session-log cap + archive cadence), `pm-handoff.md` ("This Session" entry cap), and the MODULE_CONTEXT *header-line* convention (fixed-length current state; changelog to git/separate section). **Repos:** nexsys-hivemind + homesynapse-core. **Model-agnosticism:** keeps the curated high-signal layer from rotting, protecting every model's context budget.

### R6 — Governance weight classes (the key Horizon-2 decision)
**Files:** new `context/process/Governance_Weight_Classes.md` defining **core-module governance** (full ceremony: design doc + amendments + full review) vs **integration-module governance** (template-driven, lighter review, constrained by the `IntegrationAdapter` HAL); plus an integration-module onramp template in `homesynapse-core-docs`. **Decision:** Nick ratifies the boundary. **Repos:** nexsys-hivemind + homesynapse-core-docs. **Model-agnosticism:** lower ceremony for HAL-constrained modules reduces the per-module coherence tax as the system scales, keeping the human bottleneck (Finding 10) from tightening.

### R7 — Source-companion completeness checklist
**Files:** extend `two-project-claude-architecture.md §6` into a Cowork-side assembly checklist enforcing "companion present + HEAD/watermark/version header stated + routed by what-the-verdict-is-about" before any cross-Project review. **Repo:** nexsys-hivemind. **Model-agnosticism:** makes the CORE↔DOCS boundary checklist-driven rather than operator-memory-driven; correctness no longer depends on a human remembering, and works for any model.

### R8 — Model-transition checklist
**Files:** new `project-manager/references/model-transition-checklist.md` (the §7 procedure), referencing the existing `benchmarks/` harness. **Repo:** nexsys-hivemind. **Model-agnosticism:** *this is the model-agnosticism insurance* — it makes model swaps safe, evidence-based, and reversible, and operationalizes HSDM-P3.

### R9 — Optional assisted compile gate (deferrable)
**Files:** a host-side git pre-commit / CI hook running `./gradlew check` + a snapshot-consistency lint (does `CURRENT_STATE_STAMP` match `git log`? are MODULE_CONTEXTs updated for changed modules?). **Repo:** homesynapse-core (Nick's host). **Decision:** Nick may defer or decline to preserve the manual gate exactly — the hook *assists*; Nick remains the gate owner and override authority. **Model-agnosticism:** closes the deferred-build-gate window so a future weaker/different model cannot widen it into shipped defects — the highest-leverage model-transition insurance on the code side.

---

*HSDM v1. Constitution: `project-knowledge/HomeSynapse_Development_Method_Constitution_v1.md`. This document is governed by §7. The §8 roadmap is a living backlog; §2–§7 change by method amendment.*

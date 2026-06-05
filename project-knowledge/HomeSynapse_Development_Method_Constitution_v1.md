<!--
file: project-knowledge/HomeSynapse_Development_Method_Constitution_v1.md
purpose: The stable, non-negotiable principles governing all HomeSynapse development activity. The constitutional core of the HomeSynapse Development Method (HSDM). Designed to be uploaded to both Claude Projects' spines and to survive model upgrades.
audience: All (Nick, Cowork, CORE Project, DOCS Project, Claude Code)
update-cadence: rare (amendment process only — see Method doc §7)
state-type: reference / governance
status: CURRENT — v1 (2026-05-31)
companion: context/process/HomeSynapse_Development_Method_v1.md (§2–§8: surfaces, context, lifecycle, instructions, failure defenses, governance, roadmap)
-->

# HomeSynapse Development Method — Constitution (v1)

## What this is

This document is the small set of **non-negotiable principles** that govern every development activity on HomeSynapse Core, across every surface (Cowork, the CORE and DOCS Projects, Claude Code) and across every model generation. It is the stable core of the HomeSynapse Development Method (HSDM). It is deliberately short: it states *what must always be true*, not *how* — the "how" lives in the companion Method & Roadmap document (§2–§8).

These principles are derived from what the methodology already does well, formalized so they survive model upgrades, drift, and capability changes. Every principle has a **compliance check**: an observable test of whether the principle is being honored. A principle without a check is unenforceable, and this document does not contain any.

## How to cite

Each principle has a permanent identifier `HSDM-P{n}`. Reference principles by ID in reviews, instructions, amendments, and commit messages (e.g., "this violates HSDM-P4"). Identifiers are permanent: if a principle is retired, its ID is reserved and never reused.

## Authority and relationship to other governance

This constitution governs the **development process**. It sits beside, not above, the product governance stack (`Architecture_Invariants_v1.md` → `HomeSynapse_Core_Locked_Decisions.md` → amendments → design docs), which governs **the system being built**. When both apply: the product-governance artifact is authoritative on product/architecture questions; this constitution is authoritative on process questions. Neither overrides the other; a genuine conflict between them is escalated to Nick (HSDM-P4).

Amending this constitution requires the process in Method doc §7. These principles are designed to hold for years.

---

## The Principles

### HSDM-P1 — The filesystem is the source of truth, not conversation history

Working state, decisions, and context live in files. Nothing load-bearing exists only in a chat transcript or an agent's memory. Any session — on any model — must be able to reconstruct the current working state from files alone.

**Compliance check:** A fresh session that reads only the file-based memory layer (current-state stamp, PROJECT_SNAPSHOT, handoffs, MODULE_CONTEXT, governance) can correctly state the current HEAD, watermark, milestone, and next work unit. No decision is acted on that exists only in a prior conversation.

### HSDM-P2 — The harness enforces the architecture; the model only proposes

Architectural correctness is guaranteed by tooling — ArchUnit rules, JPMS compile-time enforcement, contract test suites, `-Xlint:all -Werror`, exhaustive sealed `switch` with no `default` — not by an agent remembering a rule. The consequence is the methodology's most important property: **the worst a model swap can do is produce a red build, never silent architectural corruption.**

**Compliance check:** Every structural architectural constraint has a static or compile-time check that fails `./gradlew check`. No architectural constraint depends solely on an agent honoring it in prose. A violation surfaces as a build failure, not as shipped behavior.

### HSDM-P3 — Model-agnostic by construction; model-specifics are quarantined

Every rule, artifact, and protocol must work regardless of which LLM executes it. Model-specific tuning (a pinned model version, a benchmark-driven routing choice, a known model quirk) is permitted only in clearly-marked, revisitable sections — never baked into a permanent rule, instruction, or governance artifact. The methodology must degrade gracefully (slower, more review iterations) under a weaker or different model — never catastrophically.

**Compliance check:** No permanent rule or instruction names a model version. All model-specific content lives in sections explicitly flagged as revisitable and is covered by the model-transition checklist (Method §7). The model-transition checklist passes before any model change is adopted.

### HSDM-P4 — Source for existence and behavior; documentation for intent and contract; a conflict is a finding

The actual source code is authoritative for claims about what exists and how it behaves. Design documents, amendments, and MODULE_CONTEXT files are authoritative for intent and contract. When source and documentation conflict, **the conflict itself is a finding to be resolved through the proper channel — never silently decided in favor of either side.**

**Compliance check:** Every claim about a type's existence or a method's behavior cites `file:line` from source. Every claim about intent or contract cites a doc §, AMD, or INV. A detected source↔doc divergence is logged (e.g., as an erratum or `[VERIFY-NEEDED]`), not papered over. (This is a deliberate, considered divergence from the common "documentation is primary" guidance, learned from repeated doc-drift incidents.)

### HSDM-P5 — Static verification and behavioral testing are both mandatory

Behavioral tests prove behavior; static verifiers prove structure. Neither substitutes for the other. Layering, schema, module boundaries, time-access, serialization isolation, and concurrency discipline are enforced statically because behavioral tests pass straight through structural violations.

**Compliance check:** Every structural rule has a corresponding static check (ArchUnit / JPMS / compiler). `./gradlew check` — running both the test suites and the static verifiers — is the single authoritative correctness gate. Behavioral-test-only coverage of a structural concern is treated as incomplete.

### HSDM-P6 — Work proceeds in closed units

All work proceeds as single compile-and-commit units with test coverage. A unit is not "done" until both phases of the Work Unit Completion Protocol have executed. Completing a unit's closeout is a prerequisite for starting the next.

**Compliance check:** Every completed unit carries a WUCP Phase 1 (Coder) and Phase 2 (PM) checklist. No new unit's coding instruction is issued while a prior unit's closeout (including any deferred build gate) is unresolved.

### HSDM-P7 — No work starts on unverified state

Drift is detected before it is acted upon. Every session begins by verifying that the file-based memory layer is consistent with reality before doing forward work.

**Compliance check:** The freshness preflight runs at every session start and at every closeout review. A STALE result restricts the session to reconciliation; a CONFLICTED result is a hard stop. Forward work proceeds only on PASS.

### HSDM-P8 — Constraints are precise, singly-sourced, and checkable

Every constraint is stated as a testable predicate ("no `synchronized`; use `ReentrantLock`"), not a vague aspiration ("write good concurrency"). Every constraint has exactly one canonical definition; all other mentions are pointers to it. A constraint with no compliance check is a candidate for deletion.

**Compliance check:** Each active constraint resolves to one canonical source (a governance register or the Quick References). Restated copies are explicitly marked as pointers. Constraint counts and identifiers agree across all locations that mention them.

### HSDM-P9 — Agents coordinate through structured artifacts, never raw conversation

Inter-agent and cross-surface communication uses structured, typed artifacts (coding instructions, completion reports, typed messages, source companions). Reviews and hand-offs transmit distilled findings — verdict plus evidence — not raw transcripts.

**Compliance check:** Cross-surface exchanges use the typed message protocol and the canonical artifact formats. A review's output is a verdict with `file:line`/`§`-cited evidence, not a pasted conversation. Cross-repo questions carry the embedded source companion they need.

### HSDM-P10 — Governance changes only through the amendment process; identifiers are permanent

Architecture invariants, locked decisions, and amendments change only through their formal process. Identifiers (INV / LTD / AMD / HSDM-P) are permanent — a retired identifier is reserved, never reused — so every historical reference remains unambiguous.

**Compliance check:** Every governance change traces to an amendment with impact analysis and a watermark raise. No identifier is ever reassigned. Cross-references to retired identifiers resolve to a retirement note.

---

*This is v1 of the HomeSynapse Development Method Constitution. It is governed by the amendment process in `context/process/HomeSynapse_Development_Method_v1.md` §7 and is intended for upload to both Claude Projects' shared spine.*

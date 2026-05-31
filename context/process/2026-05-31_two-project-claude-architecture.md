<!--
file: context/process/2026-05-31_two-project-claude-architecture.md
purpose: Playbook for splitting the single "HomeSynapse Core Claude Project" into two repo-scoped Claude Projects (CORE = code, DOCS = design/governance), orchestrated by Cowork. Grounded in the Context Management Research Document (2026-05-31).
audience: Nick, PM (Cowork sessions)
state-type: process / reference
status: CURRENT — 2026-05-31
-->

# Two-Project Claude Architecture — Splitting CORE and DOCS

## 0. Why split, and the one rule that governs everything

The single Claude Project can no longer hold both repos well. Measured 2026-05-31:

- `homesynapse-core-docs` ≈ **4.7 MB (~1.2M tokens raw)** — the 14 design docs alone ≈ 330K tokens, `research/` another ≈ 320K.
- `homesynapse-core` ≈ **748 Java files / 3.4 MB (~1.1M tokens raw)** — but the 21 `MODULE_CONTEXT.md` files (~180K tokens) are already the curated high-signal layer.

Either repo, loaded wholesale, exceeds a 1M window and lands squarely in the **context-rot** zone the research document documents: retrieval reliability "grows increasingly unreliable as input length grows," degrading visibly by 20–40% of capacity (Chroma, July 2025; Anthropic's own context-window docs). A bloated Project knowledge base does not give you *more* second-opinion quality — it gives you *less*. 

**The governing rule (Anthropic's "Effective context engineering," verbatim):** *"the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."* Every decision below follows from it.

## 1. The architecture — three reliability layers, two Projects, one orchestrator

We map the research doc's three-layer loading model (always-loaded brief → curated knowledge → just-in-time retrieval) onto two repo-scoped Claude Projects plus Cowork as the orchestrator that holds ground truth.

**Reliability ordering (this is the load-bearing decision, given the GitHub connector is unreliable):**

1. **Custom-instructions brief (always loaded, ~3–5K tokens).** The role, operating rules, glossary, invariant/decision spine, and a current-state *pointer*. Practices the doc's "project brief <5K tokens" recommendation. **100% reliable.**
2. **Curated knowledge spine (uploaded files).** A hand-picked, bounded set of high-signal files (the MODULE_CONTEXTs / design docs / invariants — never raw build trees). Reliable; refreshed at WUCP Phase 2.
3. **Cowork-embedded per-prompt excerpts ("source companion").** For any specific source/amendment a question needs, **Cowork extracts the exact text from the live working tree and embeds it in the prompt.** This is the *reliable* JIT layer and the cross-repo bridge — it does not depend on the connector. It is the workhorse.
4. **GitHub connector (best-effort bonus).** JIT retrieval of anything not in the spine. **Never load-bearing** — when it flakes (as it does), layers 1–3 still fully function. Treat connector output as a convenience, and verify anything surprising against a Cowork-embedded excerpt.

**Cowork is the orchestrator and ground truth.** It has both repos mounted with live file tools, runs the freshness preflight, knows the authoritative HEAD/watermark/`projectionVersion`, and *generates the prompts* it sends to each Project. The two Projects are specialist reviewers with deep-but-bounded standing context; Cowork supplies the live specifics. This is exactly the orchestrator/sub-agent + just-in-time pattern the research doc endorses, and it is already prototyped in `context/handoff/2026-05-30_AMD51_external_review_prompt.md` + `..._source_companion.md` — the split just routes the companion to the right Project.

## 2. Project DOCS — "HomeSynapse Core · Design & Governance"

**Use it for:** amendment authoring/ratification second opinions, design-doc reasoning, research assessments, invariant/locked-decision adjudication, doc-currency review, glossary/naming, new design documents.

**Custom instructions:** paste `project-knowledge/CLAUDE_PROJECT_DOCS_custom-instructions.md` (in this repo).

**Knowledge spine to upload (curated — NOT the whole repo):**
- The 14 numbered design docs: `design/00-navigation-index.md` … `design/14-master-architecture-document.md` (the design corpus, ~330K tokens — the Project will retrieve over them).
- `design/amendments/*.md` (all 23 — the ratified-contract ledger).
- The recent dated design notes/beats: `design/2026-05-*.md` (composition root, M4 verification report, AMD-52 beat, relocation note).
- Governance: `governance/Architecture_Invariants_v1.md`, `governance/HomeSynapse_Core_Locked_Decisions.md`, `governance/HomeSynapse_Core_v1_Project_MVP.md`, `governance/HomeSynapse_Core_Refined_Repo_Architecture_v2.md`, `governance/DESIGN_DOC_TEMPLATE.md`.
- The shared spine (see §4).

**Exclude from the spine:** `research/` raw (~320K tokens, archival — bring a *specific* research doc in as a Cowork-embedded companion when assessing it), `archive/`, `RATIFIED/` bulk. Let the connector reach these JIT.

**Connector:** `homesynapse-core-docs` (best-effort).

## 3. Project CORE — "HomeSynapse Core · Implementation"

**Use it for:** Java code second opinions, JPMS/module-graph reasoning, test-design critique, ArchUnit/arch-rule reasoning, implementation verification against an embedded amendment, refactor/risk assessment.

**Custom instructions:** paste `project-knowledge/CLAUDE_PROJECT_CORE_custom-instructions.md` (in this repo).

**Knowledge spine to upload (curated — NOT the 748 `.java`):**
- All 21 `MODULE_CONTEXT.md` files (the type/contract inventory — the persistent code memory). *Watch:* `core/persistence/MODULE_CONTEXT.md` is ~165 KB / ~45K tokens; if the spine feels heavy, it is the first candidate to trim to its current sections.
- All 18 `module-info.java` files (the authoritative JPMS module-name + `requires`/`exports` graph — load-bearing per the Research-6 fabricated-module-name lesson).
- `homesynapse-core/CLAUDE.md`.
- The coder mental model: `nexsys-hivemind/coder/references/{homesynapse-mental-model,java-patterns,testing-standards,deviation-and-quality}.md` (how to reason about and review this codebase).
- The shared spine (see §4).

**Exclude from the spine:** all raw `.java` source, `build/`, `.gradle/`, generated artifacts. Specific source arrives as a Cowork-embedded source companion (reliable) or via the connector (best-effort).

**Connector:** `homesynapse-core` (best-effort).

## 4. The shared spine (in BOTH Projects) — the lingua franca

Both Projects must speak identical INV/AMD/LTD numbers and terms, so a small shared set goes in **both** knowledge bases:
- `nexsys-hivemind/project-knowledge/HomeSynapse_Knowledge_Primer.md` (orientation — note: its module-name summaries are *not* authoritative; module-info.java wins).
- `nexsys-hivemind/project-knowledge/Invariants_Quick_Reference.md`
- `nexsys-hivemind/project-knowledge/Decisions_Quick_Reference.md`
- `nexsys-hivemind/project-knowledge/HomeSynapse_Navigation_Index.md`
- `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md`
- `governance/Architecture_Invariants_v1.md` (also listed in DOCS — it is the authoritative registry; CORE needs it as the lingua franca).

**Deliberately NOT in the spine:** `project-knowledge/HomeSynapse_Current_State.md`. Current state drifts every milestone; uploading it guarantees a stale snapshot. The **Cowork prompt states the authoritative HEAD / watermark / `projectionVersion`** at the top of every review (see §6) — that is the single source of "now."

## 5. Routing — which Project answers which question

- **Design / governance / amendments / research / naming → DOCS.** "Is AMD-NN internally consistent?" "Does this design beat respect AMD-50-INV-03?" "Assess this research return." "Author the AMD body."
- **Java / tests / JPMS / arch-rules / implementation → CORE.** "Does this serializer's switch exhaust the sealed type?" "Is this test replay-deterministic?" "Will this `requires` edge create a cycle?"
- **Cross-repo ("does the code satisfy the amendment?") → Cowork orchestrates.** Cowork embeds BOTH the amendment § (from docs) AND the code excerpt (from core) into one prompt and routes to **CORE** (the question is "does this code conform"). The reverse ("does the amendment over-constrain what the code can do?") routes to **DOCS** with the code excerpt embedded. The rule: route by *what the verdict is about*, and embed the other repo's slice.

## 6. The Cowork → Project prompt template (generate one per review)

Cowork produces a **review/assessment prompt** + an embedded **source companion**, following the research doc's loading order (long docs near the top in XML tags; the ask at the very end — Anthropic reports up to +30% on multi-document tasks). Skeleton:

```
<context>
Repo: homesynapse-core @ HEAD <sha> | watermark AMD-<n> | projectionVersion <v>.
You are reviewing <one-line scope>. The excerpts below are GROUND TRUTH — trust them
over your knowledge base and your own memory where they conflict.
</context>

<source_companion>
<!-- Cowork pastes the EXACT working-tree excerpts: the amendment §, the .java spans
     (with file:line), the MODULE_CONTEXT rows — only what THIS question needs. -->
</source_companion>

<task>
<!-- The specific ask, verdict format, and the invariants/forks to check. -->
</task>

<question>
<!-- One sharp question, last. -->
</question>
```

Distill the Project's reply back into Cowork as a **finding** (verdict + evidence), never the whole chat — the research doc's "findings distillation, not raw transcripts."

## 7. Model selection — pin Opus 4.6 for both Projects

These Projects do exactly the work Opus 4.6 wins and Opus 4.7 regressed on: **multi-fact retrieval across large context** (MRCR v2 8-needle at 1M: Opus 4.6 ≈ 78.3% vs Opus 4.7 ≈ 32.2%, per the 4.7 system card §8.7.2). Pin **Opus 4.6** in both Projects. Use Opus 4.7 only for tightly-scoped agentic coding under ~200K (i.e., Claude Code / Cowork implementation), not for these review/assessment Projects. **Revisit trigger:** if Anthropic ships an Opus that posts MRCR v2 1M > 70% (or GraphWalks becomes the accepted applied metric *and* your own review quality improves), re-test and consider migrating.

## 8. Anti-context-rot operating discipline

- Keep each custom-instructions brief **< ~5K tokens**. If it grows, move detail into the spine.
- Keep the spine **curated and bounded**. New milestone artifacts replace stale ones; the spine does not monotonically grow. Trim the persistence MODULE_CONTEXT first if needed.
- **Never paste raw chat transcripts or raw build output** into a Project. Embed distilled excerpts only.
- One sharp question per prompt, at the end; long embedded material near the top, in XML tags.
- If a Project's answer cites a type/§/INV you can't verify, treat it as a hallucination flag — ask it to point to the file/line, and verify against a Cowork excerpt.

## 9. Maintenance — fold spine-refresh into WUCP Phase 2

The connector is unreliable, so the spine is refreshed manually — but cheaply, because it is small and only the *changed* files need re-uploading. Add to the WUCP Phase 2 checklist:

- **MODULE_CONTEXT.md changed this WU →** re-upload those files to the **CORE** Project.
- **Amendment ratified / design doc body folded / invariant registered →** re-upload those files to the **DOCS** Project.
- **Shared spine quick-references changed →** re-upload to **both**.
- **Connector health check (start of any Project session):** ask the Project to confirm it can see one known recent file (e.g., "quote the first line of `core/value-model/MODULE_CONTEXT.md`"). If it can't, the connector is down — proceed on spine + Cowork-embedded companions (the default anyway).

Versioning: the two custom-instruction briefs live in `nexsys-hivemind/project-knowledge/` and are version-controlled here; when you edit a brief, re-paste it into the Project's custom-instructions field.

## 10. Step-by-step setup (Nick)

1. **Create the Projects.** Recommended: rename the existing "HomeSynapse Core" Project → **"HomeSynapse Core · Design & Governance (DOCS)"** (keeps its amendment-review history), and create a new **"HomeSynapse Core · Implementation (CORE)."** (Or start both fresh if you want a clean slate.)
2. **Pin Opus 4.6** in each Project's model setting (§7).
3. **Paste custom instructions:** DOCS ← `CLAUDE_PROJECT_DOCS_custom-instructions.md`; CORE ← `CLAUDE_PROJECT_CORE_custom-instructions.md`.
4. **Connect GitHub** (best-effort): DOCS → `homesynapse-core-docs`; CORE → `homesynapse-core`.
5. **Upload the curated spine** per §2 (DOCS), §3 (CORE), and §4 (shared, to both).
6. **Smoke test each:** run the connector health check (§9), then a known-answer question ("List the 8 `AttributeValue` variants and their `AttributeType` constants" for CORE; "State AMD-52's F1 and F2 forks" for DOCS). If it answers from the spine cleanly, you're live.
7. **Going forward:** Cowork generates a review prompt + source companion per §6 and routes per §5; you paste it into the right Project; you paste the verdict back to Cowork; spine refresh rides WUCP Phase 2 (§9).

## 11. Success criteria

- A review prompt for either Project fits comfortably (active per-question context well under ~60% of the window — almost always under 256K), because the spine carries standing context and the companion carries only the slice.
- Neither Project is ever asked to "remember" current state — the prompt always states HEAD/watermark/`projectionVersion`.
- When the connector is down, reviews still run unchanged (spine + companion). If a review *requires* the connector, the prompt was under-specified — fix the companion, not the connector.
- Cross-repo questions never ask a Project to guess the other repo — the slice is always embedded.

**Bottom line:** two repo-scoped Opus-4.6 Projects, each anchored by a <5K-token brief + a curated spine, with Cowork supplying live ground-truth excerpts per question and the GitHub connector as a bonus. This is the research doc's "smallest high-signal set + just-in-time retrieval + orchestrator topology," applied to the exact shape of the two repos.

<!--
file: context/assessments/2026-06-12_design-system-import_PM_Assessment.md
purpose: PM assessment of the six Feb 2026 design-system documents imported into homesynapse-core-docs/website/design-system/ — content critique, conflict findings vs ruled register rules, skill-ification path.
audience: Nick, PM
state-type: assessment
status: DELIVERED 2026-06-12
-->

# PM Assessment — Feb 2026 Design-System Canon Import

**Session:** 2026-06-12 (parallel lane; no Core work touched; no PROJECT_SNAPSHOT/pm-handoff edits — fold at the Sunday converge session)
**Action taken:** doc01–06 renamed to canonical names (per `homesynapse-core-docs/research/2026-03-08_das-design-system-dependency-map.md`), relocated to `homesynapse-core-docs/website/design-system/`, mojibake repaired (doc04/05/06), broken ChatGPT `oaicite` citation tokens in the visual design reference replaced with an import note, provenance headers added, self-declared "Locked" statuses downgraded to DRAFT. Conflict register C1–C10 established at `website/design-system/README.md`. The website content register (`website/README.md`) now points at the design-system tree and asserts authority order.

## Verdict

The Feb pack is substantially better than typical early-stage brand work — the voice system and typography spec are near-ratifiable — but it predates the M5-C register rules and conflicts with them in load-bearing places. Treat it as a strong draft layer under the ruled decisions, not as parallel canon. Detailed findings live in the conflict register (C1–C10); the strategic deliberation items below need Nick.

## Strongest assets (preserve)

1. **Voice & Tone** dual-register system (A/B/C), the "we" test, the specificity principle (§4.4), the philosophy rule ("state once, then let the architecture demonstrate it"), and the AI-vocabulary/structural-variety bans. §4.4 is convergent with the provenance-appendix discipline the website lane ruled independently in June — the Feb thinking was sound.
2. **Typography v2** — implementation-ready, evidence-based, already self-corrected once (v1 serif default dropped after competitive analysis). Inter + opt-in Source Serif 4 + JetBrains Mono NL are defensible decade-scale choices. Spot-checked claims verified (Inter opsz 14–32, x-height ≈55% UPM).
3. **Content Types** — Diátaxis + first-class troubleshooting format + ops routing table is real documentation architecture; the catalog-as-structured-data concept is a long-term moat asset that feeds the data-value-engine story.
4. **Calm Canvas + page-intent mapping + 6-section homepage cap** — the live `index.md` draft already implements the surviving parts.
5. The pack governs copy the way the hivemind governs code. That meta-property is itself hard to replicate.

## Material defects (fix at reconciliation)

- C1/C2: vocabulary and no-comparison rules collide with the ruled flagship pages (REC-171 title; REC-142/175/176/179 dossiers). Needs the identity-adjective vs factual-claim distinction and a "dossier register" amendment.
- C3: the voice guide's own example copy violates the Matter fence (D-1) and the tense-truth publish gate.
- C4: Docusaurus hard-coding vs the open framework decision.
- C5: "account portal / cloud extension" site role vs no-cloud-account flagship — reconcile via layered messaging (core-never-requires-account is the durable INV-grade claim; Connect/Cloud Pro are additive). Flagship copy must be drafted Connect-proof now or the headline becomes a hostage at Connect launch.
- C6: measured WCAG AA failures (HomeSynapse Blue 2.4:1 and Warning amber 2.1:1 as text on Mineral Ash). Two-tier accent palette required.
- C7: homepage flow slot 2 vs segment rule D-4 (one-line patch).
- C8: the canon's authority root (DAS v1 Specification) + AboutHomeSynapse + 15-file artifact pack are still stranded in the ChatGPT project — extraction is the top sequencing item, HIGH dependency for Doc 13 and docs CI.
- C9/C10: mechanical numbering defects, paste artifacts, status inflation (C10 closed at import).

Also flagged: the website-design-vision customization model (Levels 0–2) is scope creep for launch — recommend Level 1 only (theme toggle) and defer/cut Level 2; ambient-particle backgrounds have become a genre cliché since Feb. The investor-facing surface (nexsys.io) is referenced by the typography/visual refs but is out of the M5-C lane — schedule separately.

## Skill-ification path (Nick directive, 2026-06-12)

Refined/ratified design-system documents become the reference layer of future `nexsys-web` and `nexsys-brand` skills interoperating with `nexsys-hivemind/{coder,project-manager}`. Rules recorded in `website/design-system/README.md`: canonical source stays in the docs repo, skill references are derived mirrors under the existing dual-location sync discipline, and no document graduates into a skill until its conflict-register rows close and Nick ratifies. PM briefs for website/brand work cite the register rules + tracker state the same way Core briefs cite LTD/INV numbers.

## Handoff

- Nick host-git commit (docs repo). Suggested message:
  `docs(website): import Feb 2026 design-system canon — rename doc01-06 to canonical names under website/design-system/, repair encoding + broken export citations, downgrade Locked statuses to DRAFT, add conflict register C1-C10 + tracker README; register pointer added to website/README.md`
- This assessment + tracker need registration at the Sunday converge session (single-anchor append discipline respected; no governance spine files touched this session).

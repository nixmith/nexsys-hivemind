# Scoring History — HomeSynapse Core Claude Project

## Trajectory

```
B1 (2026-03-21): 87.5%  ████████▊
B2 (2026-04-08): ~75%   ███████▌    (12 questions, UNKNOWN answers)
B3 (2026-03-27): N/A    (drift audit, not scored as Q&A)
B4 (2026-05-17): 92%    █████████▏  (50 questions, 3 failures)
```

## Detailed Results

### Benchmark 1 — Authority Chain (2026-03-21)
- **Format:** 40 questions, human-graded
- **Score:** ~87.5% (35/40 correct)
- **Failure class:** Authority chain ignorance — treating rejected amendments as applied, trusting Knowledge Primer over MODULE_CONTEXT
- **Fix applied:** Established authority chain, amendment verification discipline
- **Regression tests created:** REG-010 (withdrawn amendment as applied)

### Benchmark 2 — Source Verification (2026-04-08)
- **Format:** 12 questions, human-graded
- **Score:** ~75% (9/12, with UNKNOWN answers)
- **Failure class:** Methodological — never opened the repo, treated documentation as ground truth without verification
- **Fix applied:** Gated checkpoint protocol, mandatory source verification
- **Regression tests created:** REG-020 (count without verification)

### Benchmark 3 — Documentation Drift Audit (2026-03-27)
- **Format:** Drift analysis, not scored as Q&A
- **Findings:** Identified drift patterns across repos
- **Fix applied:** Documentation corrections, MODULE_CONTEXT refresh

### Benchmark 4 — Deep Architecture Audit (2026-05-17)
- **Format:** 50 questions (7 sections), graded by Cowork against verified source
- **Score:** 92% fully correct (46/50), 96% substantially correct (48/50)
- **Breakdown:**
  - ✅ CORRECT: 43/50
  - 🎯 EXCEPTIONAL: 3/50 (Q13, Q28, Q36)
  - ⚠️ PARTIALLY CORRECT: 2/50 (Q6, Q49)
  - ❌ INCORRECT: 3/50 (Q10, Q22, Q43)
- **Failure classes:**
  - Q10: Retrieval failure (answer present in 2 locations, not found)
  - Q22 + Q43: Ghost rule stale belief (M3 Plan §4.5 prescribed ArchUnit, impl used JPMS)
- **Fixes applied:**
  - Knowledge Primer: ArchUnit count corrected (8→7), JPMS note added
  - Pending: M3 Plan §4.5 correction, negative assertion in Knowledge Primer, plan-vs-reality priority rule
- **Regression tests created:** REG-001, REG-002, REG-003
- **Notable:** Claude Project successfully pushed back on 2 grading errors (Q16, Q24) — both upheld

## Failure Class Inventory

| Class | First Seen | Recurred? | Fix | Status |
|-------|-----------|-----------|-----|--------|
| Authority chain ignorance | B1 | No | Authority chain established | Resolved |
| Source verification laziness | B2 | No | Gated checkpoint protocol | Resolved |
| Documentation drift | B3 | Partially (B4 ghost rule) | Ongoing maintenance | Active |
| Document priority confusion | B4 | New | Priority rule pending | Pending fix |
| Retrieval failure | B4 | New | Search discipline pending | Pending fix |
| Ghost rule (stale belief) | B4 | New | Negative assertion pending | Pending fix |

## Performance by Category (Benchmark 4 only)

| Category | Questions | Correct | Rate |
|----------|-----------|---------|------|
| A — Retrieval | ~25 | 23 | 92% |
| B — Priority | ~5 | 4 | 80% |
| C — Negative | ~8 | 7 | 87.5% |
| D — Reasoning | ~12 | 12 | 100% |

**Key insight:** Architectural reasoning (Category D) is a strength. Retrieval and negative knowledge are the improvement areas. This aligns with the Claude Project's self-assessment.

## Next Scheduled

- **Post-M3.2 smoke test:** When M3.2 completes (use `smoke-tests/m3.2-smoke.yaml`)
- **Regression bank:** After Knowledge Primer corrections are applied
- **Monthly stratified:** Target early June 2026

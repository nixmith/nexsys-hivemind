# Regression Bank — History

## 2026-05-17: Initial Population

Seeded with 5 regressions from Benchmarks 1, 2, and 4:

| ID | Source | Failure Class | Question Summary |
|----|--------|---------------|------------------|
| REG-001 | B4 Q10 | retrieval | ConfigurationChangeListener ordering |
| REG-002 | B4 Q22 | enforcement mechanism | NO_SYNCHRONIZED_METHODS scope |
| REG-003 | B4 Q43 | ghost rule | Event-bus ArchUnit rule (doesn't exist) |
| REG-010 | B1 | withdrawn-as-applied | AMD-39 status |
| REG-020 | B2 | count without verification | publishRoot() parameter count |

### Design Decisions

- Regressions from Benchmarks 1 and 2 were added retroactively because they represent failure classes that could recur.
- Each regression has a `verification_note` explaining HOW to confirm the answer is correct, reducing grading ambiguity.
- `must_not_contain` fields specifically target the WRONG answers from past failures, ensuring the exact same mistake is caught.

### Growth Expectations

- Expect 1-3 new regressions per comprehensive benchmark
- Expect 0-1 new regressions per stratified monthly benchmark
- Retire regressions only when the underlying feature changes (not when the question "seems easy")
- Target: bank stays under 20 active regressions (above that, split into themed sub-banks)

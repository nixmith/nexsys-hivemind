# HomeSynapse Core — Claude Project Benchmark System

This directory contains the testing infrastructure for validating the HomeSynapse Core Claude Project's architectural knowledge. The Claude Project is unaware of this system — it cannot see these files, study the answer keys, or anticipate the questions.

## Purpose

Detect knowledge drift, retrieval failures, stale beliefs, and document-priority confusion in the Claude Project before they cause errors in production PM work (task instructions, design decisions, architecture compliance).

## Architecture

```
benchmarks/
├── README.md                          ← You are here
├── grading-protocol.md                ← How to run and grade (execution manual)
├── scoring-history.md                 ← Score trajectory across all benchmarks
├── answer-keys/
│   ├── category-a-retrieval.yaml      ← Fact recall (machine-gradable)
│   ├── category-b-priority.yaml       ← Document priority (machine-gradable)
│   ├── category-c-negative.yaml       ← "Does NOT exist" (machine-gradable)
│   └── category-d-reasoning.md        ← Architectural reasoning (human-graded rubrics)
├── regression-bank/
│   ├── bank.yaml                      ← All regression questions + answers
│   └── history.md                     ← When regressions were added/retired
├── smoke-tests/
│   ├── template.yaml                  ← How to write a milestone smoke test
│   ├── m3.1-smoke.yaml                ← Post-M3.1 (retroactive)
│   └── m3.2-smoke.yaml                ← Post-M3.2 (ready when milestone lands)
├── comprehensive/
│   ├── benchmark-4-2026-05-17.md      ← Today's 50-question comprehensive audit
│   └── results/
│       └── benchmark-4-results.md     ← Grading report and scorecard
└── prompts/
    ├── smoke-test-prompt.md           ← Template for generating smoke prompts
    ├── regression-prompt.md           ← Template for regression bank runs
    └── comprehensive-prompt.md        ← Template for full audits
```

## Execution Model

1. **Nick** opens a fresh Claude Project conversation (no prior context)
2. **Nick** pastes the benchmark prompt (generated from this system)
3. **Claude Project** responds with answers
4. **Nick** copies the response into **Cowork** (this agent) with "grade this against [bank/smoke/comprehensive]"
5. **Cowork** loads the answer key, grades machine-gradable questions, flags Category D for Nick's judgment
6. **Nick** reviews only the failures and Category D answers

## Question Categories

| Category | Tests | Gradable By | Frequency |
|----------|-------|-------------|-----------|
| A — Retrieval | Fact recall: counts, locations, values | Machine (exact match / contains) | Every milestone |
| B — Priority | Plan says X, MODULE_CONTEXT says Y — which wins? | Machine (expected answer is always the post-implementation doc) | Monthly |
| C — Negative | "Does X exist?" where answer is NO | Machine (must say no/does not exist) | Every milestone |
| D — Reasoning | Explain why, failure modes, cross-cutting | Human (rubric-guided) | Quarterly |

## Rhythm

| Trigger | What Runs | Time Cost (Nick) | Grading |
|---------|-----------|------------------|---------|
| After every milestone | Smoke test (5–8 questions, A+C) | 10 min | Machine |
| After Knowledge Primer / MODULE_CONTEXT update | Regression bank | 5 min | Machine |
| Monthly / before major phase transitions | Stratified 20-question (5 per category) | 30–40 min | Machine (A–C) + Human (D) |
| Quarterly / major project milestones | Full 50-question comprehensive | 2–3 hours | Human + Machine |

## Answer Key Format

```yaml
questions:
  - id: "A-001"
    category: "A"
    question: "How many fields does EventEnvelope have?"
    expected:
      exact: "14"
    source: "event-model/MODULE_CONTEXT.md"
    added: "2026-05-17"
    milestone: "M3.1"

  - id: "C-003"
    category: "C"
    question: "Does EventPublisher have an emit() method?"
    expected:
      contains_any: ["no", "does not exist", "only publish() and publishRoot()"]
      must_not_contain: ["yes", "emit() is", "async and best-effort"]
    source: "EventPublisher.java"
    added: "2026-05-17"
    milestone: "M3.1"
```

## Scoring

- **✅ CORRECT:** Answer matches expected (exact or contains criteria met)
- **⚠️ PARTIAL:** Core fact correct but with embellishment errors or wrong citations
- **❌ INCORRECT:** Answer contradicts expected, or UNCERTAIN when answer is available
- **🎯 EXCEPTIONAL:** Correct + demonstrates insight beyond what was asked (human judgment only)

## Versioning

Answer keys are updated when the codebase changes. Each update is tagged with the milestone that caused it. Old answers are not deleted — they're moved to a `retired` list with the retirement reason (prevents re-adding stale questions).

## Isolation Guarantee

The Claude Project MUST NOT have access to:
- This `benchmarks/` directory
- The answer keys
- The regression bank
- The scoring history

If any of these leak into project knowledge, the benchmark becomes a memorization test rather than a knowledge test. The hivemind repo is local-only and never synced to the Claude Project.

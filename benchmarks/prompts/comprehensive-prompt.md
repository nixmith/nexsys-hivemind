<!--
file: benchmarks/prompts/comprehensive-prompt.md
purpose: Generation guide for quarterly comprehensive benchmark prompts.
audience: Cowork
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Comprehensive Benchmark Prompt — Generation Guide

## When to Generate

- Quarterly, or at major project milestones (end of M3, start of M4, etc.)
- When significant project knowledge changes have accumulated
- When you suspect systemic drift

## How to Generate

A comprehensive benchmark should:
1. Cover all 7 sections from Benchmark 4 (module structure, event model, virtual threads, M3 architecture, persistence, cross-cutting, build/governance)
2. Include questions from all 4 categories (A/B/C/D)
3. Target known weak areas more heavily (based on scoring-history.md)
4. Include at least 5 NEW questions not in any prior benchmark (prevents memorization)
5. Rotate at least 30% of questions from the prior comprehensive (keeps it fresh)

## Structure

- 50 questions across 7 sections
- Run in 5 batches of 10 (addresses context-fade problem)
- Each batch is a separate prompt turn in the same conversation

## Batch Prompt Template

```
Answer questions [N]–[M] about the HomeSynapse Core architecture.
Be precise with numbers, field counts, type locations, and constraint sources.
Do not hedge — state facts directly. Where genuinely uncertain after exhaustive search, say UNCERTAIN.
Cite your sources (LTD-XX, AMD-XX, INV-XX, DEC-M3-XX) for every constraint.

[Questions N through M]
```

## Question Generation Principles

1. **Verifiable:** Every question must have a verifiable answer from source code or documentation
2. **Discriminating:** The question should distinguish between "knows the architecture" and "guessing from context"
3. **Non-leading:** Don't hint at the answer in the question phrasing
4. **Targeted:** Each question should test ONE specific piece of knowledge, not compound multiple
5. **Fresh:** At least 10 questions should be completely new (not from any prior benchmark or answer key)

## Grading

Comprehensive benchmarks use the full grading protocol:
- Categories A/B/C: Machine-grade against answer keys (update keys if new questions are added)
- Category D: Human-grade against rubrics
- New questions: Grade against verified source, then add to appropriate answer key

## Archiving

After grading, save:
- The full prompt: `comprehensive/benchmark-N-YYYY-MM-DD.md`
- The results: `comprehensive/results/benchmark-N-results.md`
- Update: `scoring-history.md` with the new score
- Create regression entries for any new failures

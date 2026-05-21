<!--
file: benchmarks/grading-protocol.md
purpose: Execution manual for running smoke, regression, and comprehensive benchmarks and grading the results.
audience: Cowork, Nick
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Grading Protocol — Execution Manual

## How to Run a Benchmark

### Smoke Test (post-milestone)

1. Open the relevant `smoke-tests/m3.X-smoke.yaml`
2. Copy the questions into a single prompt with this header:

```
Answer the following questions about the HomeSynapse Core architecture.
Be precise with numbers, names, and citations. If uncertain, say UNCERTAIN.
Number your answers.
```

3. Paste into a **fresh** Claude Project conversation (no prior messages)
4. Copy the response
5. Bring to Cowork: "Grade this smoke test against `benchmarks/smoke-tests/m3.X-smoke.yaml`"

### Regression Bank

1. Open `regression-bank/bank.yaml`
2. Copy ALL active questions (ignore `retired:` section)
3. Same prompt header as smoke test
4. Same execution flow
5. **Any regression failure blocks forward work** until the documentation fix is verified

### Stratified Monthly (20 questions)

1. Select 5 questions from each category:
   - Category A: Pick from `answer-keys/category-a-retrieval.yaml` (rotate — don't repeat the same 5 every month)
   - Category B: Pick from `answer-keys/category-b-priority.yaml`
   - Category C: Pick from `answer-keys/category-c-negative.yaml`
   - Category D: Pick from `answer-keys/category-d-reasoning.md`
2. Combine into one prompt with the standard header
3. Machine-grade A/B/C; hand-grade D
4. Category D rubrics are in `category-d-reasoning.md` — use them, don't freestyle

### Comprehensive (50 questions)

1. Either reuse the existing comprehensive (`comprehensive/benchmark-4-2026-05-17.md`) or generate new questions targeting areas of concern
2. Run in **batches of 10** (addresses the "monolithic context waste" problem):
   - Batch 1: Q1–10 in one conversation turn
   - Batch 2: Q11–20 in a new turn (same conversation is fine, but separate search opportunity)
   - ...
3. Full human grading with Cowork assistance for fact-checking

---

## How to Grade (Machine-Gradable)

### For Cowork/Claude Code grading:

When Nick pastes answers and says "grade this against [file]", load the YAML and apply:

```
For each question:
  1. Find the matching question by ID or text
  2. Check `expected.exact` (if present): answer must contain this exact string
  3. Check `expected.contains_all` (if present): answer must contain ALL strings
  4. Check `expected.contains_any` (if present): answer must contain at least ONE string
  5. Check `expected.contains_any_2` (if present): answer must contain at least ONE string (second set)
  6. Check `expected.must_not_contain` (if present): answer must NOT contain any of these strings
  
  PASS = all positive checks met AND no must_not_contain violations
  FAIL = any positive check failed OR any must_not_contain violation
  
  For FAIL: report which check failed and quote the problematic text
```

### Handling edge cases:
- **Synonyms:** "does not exist" and "there is no such rule" both satisfy `contains_any: ["no", "does not exist"]`. Be generous with synonyms.
- **Embellishment:** Extra correct detail doesn't cause a FAIL. Only must_not_contain triggers failure.
- **UNCERTAIN answers:** If the expected answer exists in project knowledge, UNCERTAIN is a FAIL (retrieval failure). Note this specifically in the report.

---

## How to Generate New Questions

### Category A (Retrieval)
- Source: MODULE_CONTEXT files, Knowledge Primer, verified source code
- Pattern: "How many X?" / "What module does Y live in?" / "What are the Z values?"
- Verification: Always verify the answer against actual source BEFORE adding to the key
- Anti-pattern: Don't ask about things that aren't in project knowledge (that tests general knowledge, not retrieval)

### Category B (Priority)
- Source: Identify places where two documents disagree
- Pattern: "Document X says A. Document Y says B. Which is correct?"
- The answer is ALWAYS the post-implementation document
- Anti-pattern: Don't create artificial conflicts — find real ones in the docs

### Category C (Negative)
- Source: Known hallucination targets, stale beliefs from prior benchmarks, commonly confused items
- Pattern: "Does X exist?" / "Is Y true?" where the answer is NO
- Must be things the Claude Project might plausibly believe exist (e.g., because a plan mentioned them)
- Anti-pattern: Don't ask about obviously nonexistent things ("Does HomeSynapse use Kubernetes?")

### Category D (Reasoning)
- Source: Cross-cutting interactions, failure modes, design trade-offs
- Pattern: "Explain why..." / "What goes wrong if..." / "Describe the causal chain..."
- Write the rubric FIRST, then the question
- Anti-pattern: Don't ask questions with one factual answer disguised as reasoning

---

## Post-Grading Actions

### On PASS (all questions correct):
- Record the score in `scoring-history.md`
- No further action needed

### On FAIL (one or more incorrect):
1. Classify the failure:
   - **Retrieval failure:** Answer exists in project knowledge but wasn't found → Consider adding search terms to the relevant section headers
   - **Stale belief:** Claude Project believes something that was once true but is now false → Find and correct the stale document, add negative assertion
   - **Document priority confusion:** Trusted wrong document → Strengthen the authority chain signal (e.g., add "IMPLEMENTED" markers to post-impl docs)
   - **Hallucination:** Fabricated details not in any document → Add to Category C negative bank
2. Implement the fix (document correction, negative assertion, etc.)
3. Add the failed question to the regression bank
4. Re-run ONLY the failed question after the fix (spot check)
5. Full regression bank runs on next scheduled cycle

---

## Batching Rationale

The Claude Project's own feedback identified that monolithic 50-question prompts cause retrieval degradation in later answers (search results from early questions fade by Q40+). The batching protocol addresses this:

- **Smoke tests (5-8 questions):** Single batch, no splitting needed
- **Regression bank (<20 questions):** Single batch is fine
- **Stratified monthly (20 questions):** Run as 2 batches of 10
- **Comprehensive (50 questions):** Run as 5 batches of 10

Each batch gets fresh search opportunity. This means the Claude Project's performance on Q41-50 is as good as Q1-10, eliminating the context-fade bias.

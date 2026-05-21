<!--
file: benchmarks/prompts/smoke-test-prompt.md
purpose: Template prompt for post-milestone smoke test benchmarks.
audience: Cowork
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Smoke Test Prompt Template

Replace `[MILESTONE]` and `[QUESTIONS]` with the actual milestone smoke test content.

---

## Prompt to paste into Claude Project:

```
You are being given a quick knowledge check on the [MILESTONE] deliverables.
Answer precisely with numbers, type names, and citations. If uncertain, say UNCERTAIN.
Number your answers.

[QUESTIONS - copy from the smoke-tests/m3.X-smoke.yaml file, questions only]
```

## Example (M3.1):

```
You are being given a quick knowledge check on the M3.1 (InProcessEventBus Core) deliverables.
Answer precisely with numbers, type names, and citations. If uncertain, say UNCERTAIN.
Number your answers.

1. How many production types did M3.1 produce in the event-bus module? Break down public vs package-private.
2. What are the 5 SubscriberMode FSM values?
3. How does the event bus notify subscribers of new events? Does it push EventEnvelope objects?
4. Is there an ArchUnit rule in the event-bus module's test directory that prevents JDBC imports?
5. How many INV-SUB-ISO invariants were added? What do they cover?
6. How many EventBusContractTest methods exist after M3.1? Which tiers are active and which are disabled?
7. Is coalescing implemented and active in M3?
```

## Grading:

Bring the response to Cowork with:
"Grade this M3.1 smoke test against benchmarks/smoke-tests/m3.1-smoke.yaml"

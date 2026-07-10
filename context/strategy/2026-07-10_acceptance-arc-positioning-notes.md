<!--
file: context/strategy/2026-07-10_acceptance-arc-positioning-notes.md
purpose: Positioning notes mined from the acceptance arc's proven strengths (retrospective §3) for the website-content lane — every claim carries its evidence pointer; honesty rails included. Authored at the v27 hygiene sweep per the beat-1 disposition (§3 strengths → positioning).
audience: the website-content lane (primary consumer); Nick; the frontend skill's next currency pass (pointer-not-copy).
state-type: assessment (point-in-time; claims re-verify at use against the cited evidence).
status: CURRENT at authoring (2026-07-10; soak day 1).
-->

# Positioning Notes — What the Acceptance Arc Proved (for the website-content lane)

**The rail above every claim:** each is EVIDENCE-BACKED as stated and only as stated — the lane copies the claim WITH its bound, never rounds it up. Every pointer resolves to the bench record (`nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md`, the acceptance-run block + correction, bench `a81d678`+) — quote it, not memory.

## 1. "Your home's identity cannot be held hostage by a radio." (the headline claim)

Evidence: during certification, the coordinator radio was found carrying an unknown foreign network (writer never attributed). The platform refused it six consecutive boots — never adopted it, never overwrote its own stored network, stayed up with the radio isolated — then re-formed its own network FROM ITS OWN CUSTODY RECORDS, and every device returned voluntarily within 30 seconds with identity, history, and per-device tuning intact — from the event log alone. Identity then held across THREE distinct networks in one night. Honest bound: one night, two devices, one incident — "held under a real hijacking incident," not "unhackable." The adversarial framing writes itself: this wasn't a scripted test; it happened, and the architecture absorbed it.

## 2. The custody fence as a security posture

Evidence: `network_parameter_mismatch → PERMANENT_FAILURE`, six boots, loud and honest — never adopt, never clobber, keep the core up. This is the behavior a security reviewer wants to see and most stacks don't exhibit (silently rejoining whatever the radio carries). Candidate durable form: a short design-doc note formalizing never-adopt/never-clobber as an invariant-backed claim (queued; ride a docs pass).

## 3. Honesty as a measurable product property (not a slogan)

Evidence: ~25 command verdicts across the certification night, ZERO false CONFIRMs; timeout honesty demonstrated in three organic classes (device absent · rejoin race · commanded-to-current-value); a deliberately superseded command expired verdict-free with the superseding one confirmed in 0.33 s; an unconfirmable command rendered its honest "unconfirmed" verdict in 81 ms WITH the measured reason. Copy angle: "the system tells you what it knows, what it doesn't, and why — and we can show you the log."

## 4. The operator surface is a product surface (the emerging hsctl story)

Evidence: `bench.sh`'s decisive-verdict pattern (launch → poll → HEALTHY/FAILED with evidence) matured during the arc and is chartered to grow into the scenario runner (B1). The story for the site LATER (post-hsctl STOP ruling): "the same honest verdicts, at the command line." Do NOT market this yet — the product boundary is an explicit STOP; this note exists so the lane knows the trajectory, not to publish it.

## 5. Log-token → UI continuity (explainability groundwork)

Evidence: every glance-point of the certification (projection-live, rehydration, relink, verdicts) is one frozen log token ↔ one dashboard tile. The FE-7 hero renders REAL verdicts from the same stream the certification graded. Copy angle when the dashboard ships: "the dashboard shows you exactly what the engineers watched during certification — the same evidence, rendered."

## Anti-claims (never write these)

"Unhackable / immune to interference" (we proved containment + recovery of ONE incident class) · "AI-powered" anything (B5 is advisory-only and unbuilt; AIOT-INV-1 forbids autonomous actuation) · "zero false positives ever" (state the measured bound: zero across ~25 verdicts on the certification night, and the standing invariant that makes it structural) · availability claims (the ALIVE fix is queued; the current honest state is UNKNOWN-until-evidence).

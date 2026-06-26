<!--
file: context/planning/2026-06-26_v6-forward-plan_execution-refresh.md
purpose: The v6 hub's execution-layer refresh of the V1 launch-scope record — the gate-anchored ~7-week plan from 2026-06-26 to the mid-August go/no-go, under Nick's "full parallel fleet now" ruling. Refreshes the V1 record's execution view to the post-§1 / M7.3-done / Wave-1-on-the-bench / Doc-17-review-passed state; the V1 record (2026-06-20, RATIFIED) remains the SCOPE AUTHORITY (the IN/OUT line, Nov 25, the four gates) — this does not supersede it, it operationalizes it.
audience: Nick, the v6 PM hub, the four lanes (Core / Web-UI / Distribution / Bench).
state-type: planning / execution refresh
status: ACTIVE — authored 2026-06-26. Ruling: Nick co-signed "full parallel fleet now" (run all four lanes concurrently; execute the V1-ruled parallel model rather than drift to Core-serial).
anchors: context/decisions/2026-06-20_V1-launch-scope_decision-record.md (the scope authority — D1–D5, the wave, the Nov-25 backward schedule, the mid-August go/no-go) + the M7.2b co-sign/M7.3-into-V1 addendum; context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md (§1 D1–D5, RATIFIED); context/planning/phase-3-milestone-backlog.md (M7.4 NEXT); context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md (the bench); the frontend-dev + distribution-skeleton lane prompts.
-->

# v6 Forward Plan — Execution Refresh (2026-06-26 → mid-August go/no-go)

## The anchor (unchanged)

**The product is the demo, and the demo is the explainability view over a live automation running real devices.** The honest unit of progress is: *a stranger installs HomeSynapse, pairs a motion sensor and a light, watches an automation fire, clicks "why did this fire?" (and "why didn't it?" / "did it actually confirm?"), and understands the answer.* Everything below sequences backward from that sentence and from **Nov 25** (the V1 record's fixed date, scope as the release valve).

## Where we are (2026-06-26 — the honest read)

- **The engine ACTS as units, but the system is not yet live end-to-end.** M6 · M7.1 · AB-1/2/3 · M7.2a/b · **M7.3 DELIVERED GREEN** (core `5363347`) — but the command pipeline is not wired (**OR-M7-WIRING**), so there is **no live `RunCausalChain`** for the hero to render. **M7.4 is the first milestone that moves the demo needle.**
- **The architecture foundation is solid and reserved.** §1 RATIFIED (D1 event-driven/co-located dispatch · D2 pure-function-replay · D3 additive event versioning · D4 log retention · **D5 converter-DB = adapt-the-data + curated fallback**, which **unblocks M9 scoping**). The cloud/AIoT runway is reserved (Doc 17, review-passed). The docs are current (the 2026-06-26 currency sweep: M7.4-critical surface clean; register 169/49 exact). **This was the right investment — it is why M7.4 gets built once, correctly, for the long game — and it is now DONE. The discipline from here is build-heavy, governance-light.**
- **The lanes have been parallel on paper only.** Core is the one lane moving; the Web-UI + Distribution lanes are authored and contract-frozen (v1.1) but idle. **Nick's ruling (2026-06-26): run the full parallel fleet now** — the V1 record's model, executed.

## The forcing function — mid-August go/no-go (≈ week 8, ~7 weeks out)

The four gates (from the M7.2b record; the honest test, taken at maximum information):
1. **Engine done + LIVE** — M7.4 landed (command issue→confirmation on a real pipeline, E2E-gated).
2. **The hero renders on real data** — the explainability view over real `RunCausalChain` + the command-outcome state (`dispatched → confirmed | unconfirmed | failed`).
3. **Hardware validating** — motion → light on a real coordinator (the MG24 hero path).
4. **Install path proven** — the one-command install skeleton boots the artifact as a service.

Any RED → a defined checkpoint decision (cut an increment or a small dated slip), **never a November drift**. Backward schedule beyond the checkpoint: **by ~Oct 11** the full thin slice running + stable; **Oct 12–25** the 72h validation pole; **Oct 26–Nov 15** install end-to-end; **Nov 16–25** prep + buffer.

## The four lanes (next ~7 weeks)

### Lane 1 — Core (serial Coder; the schedule-critical long pole)
The ratified sequence: **close governance → M7.4a → M7.4b → thin causal-read-API → AB-4 → M9 → validation.**
- **M7.4a** — the `command_issued` producer + the co-located `command_dispatch_service` subscriber (replacing the in-process call), paired `stop()` teardown. Carries D2 (replay-safety) + D3 (versioning) as constraints. **Gated on AMD-95 ratification** (authors against the reconciled §3.11).
- **M7.4b** — the live `pending_command_ledger` subscriber + the `pollExpirations()` tick + the **E2E composition-root gate** + the D2 replay CI test. Closes OR-M7-WIRING.
- **Thin causal-read-API** — surfaces both hero halves per the v1.1 contract; reads the LIVE pipeline; must NOT balloon into all of M12.
- **AB-4 before M9** — the trust gate; nothing person-linked writes before the cipher is live.
- **M9 scoping** — now unblocked (D5); scope against the bench corpus + the converter-DB direction (adapt-the-data). Build after AB-4.

### Lane 2 — Web-UI (frontend-dev; the long pole among non-Core, ~6–8 wks, no slack — START NOW)
Core-independent now: app shell, design system, **AB-1 token auth**, device-state/event/health views over the **existing REST surfaces**. The one scheduled seam: the **hero view reads `RunCausalChain`, which goes live at M7.4** — build the shell + device views first, integrate the hero as M7.4 + the read-API land. Build both hero halves against the **v1.1 B3 mocks**. Write-isolated to `web-ui/dashboard/`; CI-gated.

### Lane 3 — Distribution (devops; ~3–4 wks — START NOW as a skeleton, then ramp)
Core-independent now: jlink runtime image, systemd unit, `.deb`/install-script, an update mechanism — a skeleton that already **boots the current artifact as a service** (removes the classic "the install flow doesn't work and it's November" failure). Ramp the device-discovery/pairing wizard after M9. Write-isolated to `distribution/`; CI-gated.

### Lane 4 — Hardware bench (Nick-driven, parallel, LIVE NOW — Session C)
Wave-1 (the full hero set) on the desk. Front-load the corpus + durable TEST FIXTURES (M9 acceptance + M7.4 E2E inputs); MG24/EZSP fingerprint (INV-CE-04); Doc 02/08 MATCH/GAP verdicts; **validate the `exposes`→capability mapping on the Hue/SNZB-03P — which also de-risks D5's technical-fit**; hero sanity motion→light in the reference stack (lead with ZHA/bellows per the fan-out de-risk). Queue **SPIKE-DC** when Wave 2 lands. Escalate Doc-gaps (hub folds; Nick co-signs).

## Priority 0 — close the governance loop (days, not weeks)

The build phase is gated on a fast, cheap governance close-out — **do not let it linger or expand:**
1. **AMD-95 co-sign** → ratify → apply the Doc 07 §3.11.1/§3.11.2/§4.3/§16 + AMD-90 edits + watermark 94→95 + spine flip → **unblocks M7.4a.** (Review-extended, co-sign-ready.)
2. **Doc 17 fold (S1/S2 + E1–E5) + Lock** → mint AIOT-INV-1 (new INV-AC category, 169→170, watermark stays AMD-94); keep INV-2/3 as principles. Off the critical path.
3. **The two forks:** D-07-A (AMD-90 §2.2/§2.3 action permits, 8-not-9) → **defer with a forward/unbuilt currency note, re-home to M8**; D2 (pure-function-replay invariant) → **register as a small standalone amendment** (gives AIOT-INV-1 a real parent; lands before/with Doc 17 Lock + before M7.4b).

## Risks + mitigations

- **The integration point is Nick, not agent capacity** (3+ lanes = 3× demand on the one node that reviews/ratifies/gates). **Mitigation: CI-as-gate-of-record** — it converts Nick from gate-runner to failure-adjudicator. This is the load-bearing enabler of the parallel model; lean on it.
- **Hardware is the #1 physical pole** (procurement + 72h wall-clock + fix-rerun). Wave-1 is on the desk; the bench front-loads it. Wave-2 ordered.
- **The hero's Core dependency** (`RunCausalChain` + the read-API) is the seam that most determines whether the differentiator is demoable at mid-August. Sequence it deliberately; don't let the read-API slice expand into all of M12.
- **Governance-as-work** (the M4-retrospective trap: Core/design expands to fill depth). The architecture is ratified and the docs are current — keep governance a lightweight gate from here, not the activity.

## Non-precluding discipline (bind)

Every V1 milestone stays **non-precluding** of the reserved upscale/cloud/AIoT seams (federation INV-SA-02, enterprise audit Doc 16 §3.3, component-authoring AX-7, crypto-shred INV-PD-07, the cloud-replication seam + the AI-safety frame — Doc 17 + the §1 record). Build the thin slice; protect the runway with the invariants. One spine-writer (the hub).

## Done-when (this plan's horizon)

The mid-August go/no-go taken honestly with all four gates assessed; the live command-pipeline spine wired + E2E-gated; the hero rendering on real data; the bench validating motion→light on real silicon; the install skeleton booting — the demo working on the way to ~Oct 11. Operate until then or until a fresh hub re-grounds from the spine.

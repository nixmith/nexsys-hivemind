<!--
file: context/assessments/2026-06-26_fanout-v2_hub-reconciliation_PM-memo.md
purpose: v6 hub reconciliation of the parallel fan-out v2 (V2-A / V2-B / V2-C). Folds each write-isolated return into a single hub view, runs the verification gate (write-isolation proof, V2-A number sanity, V2-C citation audit), runs the V1-non-preclusion checks the brief delegates to the hub, and PROPOSES spine folds for Nick's co-sign. Does NOT apply spine folds (single-writer + co-sign).
audience: Nick (co-sign the folds + the four decisions), the v6 hub, the Doc 17 fold session, the Core lane (M7.4), the M9 scoping lane.
state-type: assessment / hub reconciliation
status: RETURNED 2026-06-26. Proposes folds; applies none. Companion to 2026-06-26_v6-fanout-validation-and-dispatch-reconciliation_PM-memo.md (the FIRST-wave reconciliation); this is the SECOND-wave (v2) reconciliation.
sources-discipline: every claim traces to one of the three returns (cited by report) or to a hub verification command (cited inline). FACT vs INFERENCE flagged. Spine-fold proposals are explicitly NOT self-applied.
-->

# Parallel Fan-Out v2 — Hub Reconciliation (2026-06-26)

## Bottom line (read this first)

All three write-isolated sessions returned and **fold cleanly**. None changes V1 scope; the mid-August go/no-go and the Core critical path are untouched.

- **V2-A (Pi spike)** — **D1 CONFIRMED** (event-driven co-located dispatch is empirically free), **D2 PASS** (zero side-effects on a 1e6-event replay; this is the M7.4b CI-gate shape), **D4 sized** (growth/replay curve + a retention/snapshot recommendation — to be *frozen* on a Pi re-run, not on dev data).
- **V2-B (converter-DB pipeline)** — a concrete, offline, human-gated, version-pinned **embed pipeline** targeting artifacts the Locked docs already specify; a provenance discipline; a 4-question counsel-ready legal list; an **M9-gating verdict**. M9 device-strategy scoping can proceed against a known pipeline.
- **V2-C (AIoT safety frame)** — the "AI proposes, engine disposes" frame matured from principle into **researched architecture** (consensus pattern verified against primary sources; one bad citation caught), the **load-time static-check moat** identified, the **E3 structural proposer-only port** specified (upgrades AIOT-INV-1 from asserted to CI-testable), the **AX-7 gate** confirmed as a hard prerequisite, and **honest claim language** set.

**The verification gate passed.** Write-isolation held perfectly (mtime-proven below). V2-A's headline result (D1) is robust; its storage figures carry a documented sandbox caveat and are explicitly "freeze on the Pi." V2-C's citation tiering is trustworthy — the hub independently re-verified its load-bearing citation and the one citation it flagged as bad.

**Four decisions for Nick are at the end.** The hub applied no spine fold; all are proposed for co-sign.

---

## 1. Freshness preflight — AGGREGATE: PASS (all 11)

Run at session start against core HEAD `5363347` / docs `f54d0e0` (Doc 16 Locked; watermark AMD-94; invariants 169/49) / hivemind `b6ff0f1` (the fan-out v2 brief). All 11 checks PASS — notably **Check 9 (dual skill mirrors) is now clean** (`diff -rq` empty for both PM + Coder trees; Nick's mirror sync has landed since the v5-hub "STALE until sync" masthead). The hivemind is current; the fan-out operates on a fresh spine.

---

## 2. Dispatch outcome

| Session | Type | Wrote (write-isolated) | Gates / feeds | Verdict |
|---|---|---|---|---|
| **V2-A** | Core throwaway spike | `spike/dispatch-latency-and-log-growth/` + `context/assessments/2026-06-26_pi-dispatch-latency-and-log-growth_spike.md` | §1 D1 (confirm) + D4 (size) | ✅ D1 confirmed, D2 PASS, D4 sized — **freeze cadence on the Pi re-run** |
| **V2-B** | Research / design | `context/assessments/2026-06-26_converter-db-embed-pipeline-design.md` | §1 D5 → M9 device strategy + the legal spot-check | ✅ Pipeline designed; **M9 scoping unblocked** (gated on Session C + legal soft-gate) |
| **V2-C** | Research (forward) | `context/assessments/2026-06-26_aiot-safety-frame-and-ai-authoring_research.md` | Doc 17 fold + AX-7 + the moat/claim | ✅ Frame researched; **moat = load-time static checks**; AIOT-INV-1 made CI-testable |

---

## 3. The folds, per session

### 3.A — V2-A → D1 (confirm) + D2 (CI gate) + D4 (size)

**The two numbers.**

1. **Dispatch-seam overhead (validates D1).** Direct in-process call ≈ **0.63 ns/op**; co-located event-driven hop (executor emits `command_issued` → in-process synchronous bus → dispatch subscriber, same JVM/thread) ≈ **2.54 ns/op**; **delta ≈ 1.9 ns/op** (median; 20 trials × 20M ops; Temurin JDK 21.0.11; Ryzen 9 7900X). As a fraction of a realistic device dispatch: **0.19 % at 1 µs, 0.0002 % at 1 ms.**
2. **Log growth + replay (sizes D4).** **~488 bytes/event, ~constant** across 1e4–1e6; replay (ordered scan → in-memory projection fold) **44 ms @1e4 → 108 ms @1e5 → 625 ms @1e6**, extrapolating **~6–7 s @1e7** on the dev box; on-disk **~465 MB @1e6 → ~4.6 GB @1e7** (the Home Assistant Recorder wall). Append ~60k–98k ev/s at a 500-event commit batch; **per-event fsync ~8–9× slower** (batch=1 = 23.6k ev/s) — the most Pi-sensitive figure. **Knee between 1e6 and 1e7.**

**D1 verdict — CONFIRMED negligible (robust).** Even scaling the seam ~5× for the Pi (~10 ns), the co-located hop sits 3–5 orders of magnitude below the actuation it precedes. The only objection the v5 in-process hybrid had — latency — is empirically closed. *This is the spike's primary job and it is filesystem-independent, so it stands without the Pi caveat.*

**D2 verdict — PASS (structural).** 1,000,000 replayed `command_issued` events → **zero** dispatch side-effects (asserted in-harness; the harness exits non-zero on violation). This is exactly the shape for the M7.4b D2 CI gate; the spike hands the gate a tested template.

**D4 — design input (freeze on the Pi).** Recommendation: snapshot the high-volume projections so the **live replay tail stays ≤ ~1e6 events** (≈ a weekly-to-biweekly cadence at a busy-home ~50–100k events/day → bounds the Pi cold-rebuild to ~2–3 s); **per-scope + priority-tiered retention**, domain-log working set ~1–2 GB (~2–4M events) to stay off the multi-GB wall; CRITICAL rides longer; telemetry already ring-bounded. Snapshots/pruning stay purely derived (no second source of truth — INV-SA-03 / INV-ES-01/02).

**Hub caveat (quality-gate note).** V2-A ran on a sandbox whose **FUSE mount disabled SQLite WAL and blocked `unlink`** (documented in the report §2 + escalation 3). Consequence: the **dispatch-seam latency (D1) and the CPU-bound replay-time curve are robust dev results**; the **bytes/event + on-disk-growth + append/fsync figures carry a sandbox-filesystem caveat** and are *indicative, not authoritative*. This does not weaken D1 (latency) or D2 (replay-safety); it does mean **D4's numeric thresholds must be frozen against Session D's actual Pi `run.sh` output**, which V2-A flagged (escalation 2) and the harness ships ready for (aarch64 JDK 21 + sqlite-jdbc natives auto-fetched).

### 3.B — V2-B → M9 prep (the embed pipeline)

**Pipeline shape (FACT where it cites Locked docs; INFERENCE on effort splits).** Offline, human-gated, version-pinned: **fetch(pinned commit) → parse/classify → normalize-to-IR → map → [HUMAN-REVIEW GATE] → emit**. The emit target is the artifact the architecture *already specifies* — Doc 08 §3.6's bundled `DeviceProfile` registry (`zigbee-profiles.json`) + Doc 02 §3.6 capability rows — so the runtime loads an **attributed dataset, never upstream code, never a live dependency** (this is what keeps D5's "reject runtime-interop" honest).

**The D5 cleavage, enforced at Stage-2 classification.** The **standard-ZCL majority (~60 %)** ingests `zigbeeModel`/`fingerprint` + `exposes` as **pure data values** via a deterministic rule table (`exposes` light/numeric/binary/enum → Doc 02 §3.6/§3.7 capabilities). The **code-shaped tail (~40 %: `fromZigbee`/`toZigbee`, Tuya `0xEF00`, Xiaomi TLV)** is **re-expressed, not transcribed** — DPID/tag *tables* ride the embed as data; the decode/encode *logic* becomes HomeSynapse-authored Doc 08 §3.8/§3.9 codecs + Doc 02 §3.9 namespaced `CustomCapability`, delivered via the curated/community path. Worked HERO mappings included (Hue White A19 = clean `on_off`+`brightness` `light`; SNZB-03P = `occupancy`+`battery` `binary_sensor`) — **both bench-confirm PENDING Session C** (the corpus is empty today; stated, not fabricated).

**Provenance discipline.** Recommend a **consolidated `NOTICE`/attributions artifact generated from the ingest manifest** (over per-file headers) — exhaustive by construction, satisfies MIT reproduction + Apache-2.0 NOTICE-propagation — carrying **pinned commit + semver + license-at-ingest per consumed definition** as the relicensing hedge (herdsman-converters v26.73.0 read 2026-06-26). Periodic re-ingest diffs the IR; a license change at a new commit is an escalation, not auto-adopt.

**Counsel-ready legal list (the §1 D5 rider, now a list a lawyer can answer):** (1) consolidated-NOTICE sufficiency for Apache-2.0 at enterprise-sublicensing scale; (2) Apache patent-grant/retaliation vs the tiered sublicensing model; (3) the TS→Java derivative-work line (data-value consumption + clean-reference re-expression vs transcribing function bodies); (4) trademark/CSA "Zigbee" word-mark + vendor-name nominative use (marketing-copy concern, not data-embed).

**M9-gating verdict.** **BEFORE M9 scoping:** this pipeline shape + the standard-majority rule table + the provenance/pin discipline + **Session C's HERO-mapping confirmation** (the one recorded D5 re-open trigger). **Soft-gate (parallel; must return before the dataset ships at scale, not before scoping):** legal items 1–3. **Deferrable to execution:** the Tuya/Xiaomi codec re-expression, the community mechanism, the periodic re-ingest.

### 3.C — V2-C → the Doc 17 fold + AX-7 + the moat

**Researched safety frame (citation-audited).** The **planner → verifier/safety-gate → deterministic-executor + audit-trail** shape is the 2026 field consensus. V2-C tier-tagged every claim (34 VERIFIED / 6 PATTERN-REAL / 14 INFERENCE / 5 UNVERIFIED). VERIFIED primary sources include **Blueprint-First (arXiv 2508.02721)** — "deterministic engine owns the path; the LLM never decides it," the strongest external validation of "AI proposes, engine disposes" — **VeriMAP (2510.17109)**, **VeriPlan (2502.17898, CHI'25** — but an HCI end-user tool, scope-limited), **f-secure LLM (2409.19091)**, plan-then-execute-as-security (2509.08646), HA Assist deterministic-first/LLM-fallback, OWASP LLM + Agentic Top-10, NIST AI RMF.

**The moat (the independent contribution).** AI-as-author emits `AutomationComponent`s that **expand into the sealed permits (INV-SA-01)**, so the **`AutomationLinter` statically rejects malformed AI output at load — before it can run** (unresolved refs, type mismatches, shadowed/duplicate triggers; Doc 16 §3.2/§8.1). **Every surveyed system verifies plan *behavior*; none type-checks the authored *form* against a sealed schema, because none has one.** That gap is the defensible moat. Honest scope (records the limit): the linter checks **form, not intent** — semantic-intent safety rests on human confirmation today.

**E3 structural proposer-only port (the enforcement AIOT-INV-1 needs).** The INV-LF-02 analog: wire the future AI module at the composition root with **actuation capability structurally absent** (no `ActionExecutor`/dispatch reference), its only affordance a `ProposedDefinition`/`ProposedCommand` into the governed engine. Test: *"wire a mock AI module; assert it cannot reach dispatch except via a proposed definition the engine governs."* This upgrades AIOT-INV-1 from **asserted → CI-tested** — strengthening the review return's MINT-AT-LOCK verdict.

**AX-7 gate.** An AI author is a high-volume/low-stewardship producer → component **versioning/deprecation/compat (INV-CS-01/06) is a hard prerequisite** (silent-break risk on re-emission; shareable-component lineage). Confirmed: **AX-7 sequences before the AI-authoring milestone** — this answers Doc 17 open-question Q4.

**Claim verdict (brand-defensible language).** Defensible now: *"AI is structurally a proposer, never an autonomous actuator; AI-authored automations are statically verified before they run; every AI decision is durably explainable and auditable as a projection of the log."* **Needs counsel + the open patent search (Q1) before use:** the unqualified **"safest AIoT"** superlative, **"AI can never misfire,"** and **"formally verified"** (we do static type-checking, not model-checking — do not conflate).

---

## 4. Cross-session coherence (the hub's synthesis — the three interlock)

1. **D2 (V2-A) + E3 (V2-C) make AIOT-INV-1 enforceable from both axes.** AIOT-INV-1 ("AI is never an autonomous actuator") has a *temporal* half and an *actor* half. **D2's replay-safety CI gate** (V2-A's tested harness) gives the temporal half — the engine never re-fires on replay. **E3's structural proposer-only port** (V2-C) gives the actor half — AI can only ever propose, never actuate. Folded together at the Doc 17 Lock, AIOT-INV-1 is **CI-testable on both axes**, not asserted. Record this convergence in the fold.
2. **D1 (V2-A) underwrites the AIoT/cloud substrate thesis (V2-C + Doc 17).** The AIoT seams (AI-as-device-intelligence, cloud-replication) are "just another LIVE-only log subscriber" *only because the event-driven seam is free*. V2-A proved the seam is free (~1.9 ns) — so the additive-subscriber model the entire upscale/cloud/AIoT runway depends on now has **empirical backing**, not just an architectural hope.
3. **V2-B's M9 breadth feeds V2-A's D4 wall.** More devices → more events → faster approach to the log-growth knee. M9 scoping should carry V2-A's **per-scope + priority-tiered retention** forward as a first-class constraint, because V2-B's device breadth is exactly what accelerates D4's clock.

---

## 5. Verification gate (the hub's quality checks)

- **Write-isolation — HELD (proven, not assumed).** `git status` per repo + `stat` mtimes: the only artifacts the fan-out created are the **three `??` report files** (18:12 / 18:24 / 18:33 UTC) + the **`?? spike/dispatch-latency-and-log-growth/` tree**. Every modified (` M`) spine/doc file — `PROJECT_SNAPSHOT.md` (03:46), `phase-3-milestone-backlog.md` (04:07), `AMD-95` (12:01), `pm-handoff.md` (12:04), the two lane prompts, the hardware-bench brief — has an mtime **hours before** the agents ran. Those are Nick's in-flight 2026-06-26 forward-plan/lanes/AMD-95 edits (the `_commit-2026-06-26{b,c,d}.txt` staging set), **not fan-out writes**. Disjoint write domains held by construction; no design doc, no production code, no `module-info`, no git mutation, no spine write.
- **V2-A number sanity — consistent.** 1e6 × 488 B ≈ 488 MB ↔ reported ~465 MB on-disk (post-checkpoint, consistent). 625 ms / 1e6 ≈ 1.6 M-event/s fold (plausible for a simple in-memory projection on the stated CPU). Seam delta ~1.9 ns ↔ one virtual dispatch + a mode check (plausible). Internally coherent; storage dimension carries the §3.A sandbox caveat.
- **V2-C citation audit — trustworthy.** Hub independently re-verified the load-bearing citation: **arXiv 2508.02721 "Blueprint First, Model Second"** resolves and says what V2-C claims. V2-C's flagged-bad citation (**SafeGate / arXiv 2604.05427**) is confirmed present in our *prior* study and confirmed unverifiable (§6). The tiering discipline works; the moat/claim language rests on VERIFIED sources, not fabrications.

---

## 6. Source-integrity finding (fold-worthy, low-severity)

V2-C escalation **H-2** is **confirmed**: the 2026-06-23 prior-art research return (`...smart-home-architecture-prior-art_research-return.md`, lines 116/171/271) cites **"SafeGate" (claimed arXiv 2604.05427)** as a FACT-tier citation, and it is **unverifiable** (no retrievable page names it). **This was already pre-flagged** — the prior-art *PM assessment* (line 24) hedged the whole arXiv set as *"the harness can fabricate plausible paper names… verify before quoting as authority. We use the pattern, not the papers."* V2-C **resolved that open flag**: it VERIFIED four of the five (VeriMAP, Blueprint-First, VeriPlan, f-secure) and isolated **SafeGate** as the single bad one. **No decision is affected** — the safety-gate *pattern* is multiply-attested by VERIFIED sources. Action: at the next fold that touches the prior-art study, **strike/quarantine the SafeGate citation** and demote the line-271 "FACT" tag. Net: the integrity posture is now *better* than before — the guardrail fired and the open item is closed.

---

## 7. V1-non-preclusion checks (the brief delegates these to the hub — all PASS)

V2-C raised five seams V1 must not preclude. Hub verdict: **V1 precludes none** — V1 builds no AI path at all, and every seam is additive over the sealed model + the generic inbound definition/command path.

| Flag | Seam | Hub non-preclusion verdict |
|---|---|---|
| **H-1** | Proposer-only inbound port stays wireable at the composition root | **PASS.** `RunManager.initiateRun(...)` / `AutomationRegistry.load(...)` (Doc 16 §7) already let a proposal become a governed definition the same way a human-authored one does. Pinning the structural port is **Doc 17 / AIoT-milestone work (E3)**, not a V1 change. |
| **H-2** | Source-integrity (SafeGate) | **Not V1 scope** — handled in §6. |
| **H-3** | AX-7 authoring-provenance touchpoint | **PASS (with a tracked dependency).** Read-side/registry concern over `definitionHash`→`ComponentRef`; Doc 16 §3.2/§3.3 adds no event field (AMD-92 untouched). *If provenance ever must be event-resident → a formal AMD* — track the dependency; no V1 action. |
| **H-4** | Optional semantic-policy constraints at the verification boundary ("AI may never propose unlocking an exterior door without confirmation") | **PASS.** Composes over the sealed model + the proposer-only port (both additive). **Candidate to NAME** as a reserved sub-seam in the Doc 17 fold; naming is Doc 17 work, not V1. |
| **H-5** | Deterministic-first two-tier (HA-Assist-style) NL/voice layer | **PASS.** Pure future-layer over the existing engine; V1 assumes no LLM-primary path (V1 builds no AI path). |

---

## 8. Proposed spine folds (NOT applied — single-writer + Nick co-signs)

1. **§1 decision record** (`decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md`): append an empirical-validation note to **D1** (co-location CONFIRMED negligible — V2-A ~1.9 ns seam, 3–5 orders below actuation) and to **D4** (V2-A sizing inputs; **freeze the cadence on the Session D Pi re-run**, not dev data). Register the **D2** canonical invariant id + pin its CI test at **M7.4b**, using V2-A's harness as the test template.
2. **Reference correction (cosmetic, V2-B escalation 1):** wherever D5 / the brief / the spine point at *"Doc 02 §3.5 ZCL cluster→capability mapping,"* correct to **Doc 08 §3.5** (the ZCL map) + **Doc 02 §3.6/§3.7** (the capability vocabulary the embed targets). No doc is wrong; the pointer is. V2-B's design already uses the right sections.
3. **Prior-art study source-integrity (§6):** quarantine/strike the SafeGate (2604.05427) citation (lines 116/171/271; demote the line-271 "FACT" tag); record VeriMAP / Blueprint-First / VeriPlan / f-secure as independently VERIFIED. Closes the PM assessment's open "verify-before-quoting" flag.
4. **Doc 17 fold session** (the review return's path — Nick rules scope → folds S1/E1-E5 → mints AIOT-INV-1 → co-signs → Locks): feed V2-C in as the substantiation for §3.3 (the frame is now *researched*), **E3** (the structural proposer-only port spec + its CI test), the **AX-7-before-AI-authoring** sequencing (answers Q4), the **load-time-static-checks moat** language, the **honest claim language**, and — optionally — **name H-4** as a reserved sub-seam. AIOT-INV-1 mints with its E3 structural enforcement (asserted → CI-testable). Watermark stays **AMD-94**; count **169 → 170** iff AIOT-INV-1 mints (per the review return's mechanics).
5. **M9 scoping (D5 downstream):** unblocked per V2-B; gated on (a) the pipeline shape + standard-majority rule table (delivered), (b) **Session C HERO-mapping confirmation** (the D5 re-open trigger), (c) **legal items 1–3** as a parallel soft-gate. Commission the legal spot-check with V2-B's 4-question counsel list.
6. **Snapshot / pm-handoff:** note the three returns folded + this memo; record the H-1..H-5 non-preclusion PASS; carry H-3's *"event-resident provenance → formal AMD"* as a tracked forward dependency.

---

## 9. Housekeeping the hub observed (NOT fan-out related — FYI for Nick)

- **Uncommitted in-flight spine edits.** `nexsys-hivemind` (PROJECT_SNAPSHOT, backlog, pm-handoff, both lane prompts, the hardware-bench brief) and `homesynapse-core-docs` (AMD-95) carry uncommitted ` M` edits from your earlier 2026-06-26 work (the `_commit-2026-06-26{b,c,d}.txt` staging set). The fan-out did not touch them — commit them on your own cadence.
- **`.git/index.lock` in `nexsys-hivemind`** could not be removed by the sandbox (`Operation not permitted` — the FUSE mount). Resolve before your next hivemind commit. The fan-out ran **no git operations**, so nothing is half-staged by this session.
- **Spike cleanup.** The FUSE mount blocked `unlink`, so two **0-byte truncated** `dbtmp/*.db*` leftovers + the `.class` files remain under the spike dir. No disk/correctness impact; the standing `git rm` of `spike/dispatch-latency-and-log-growth/` (the throwaway's disposal) absorbs them. Sources + `run.sh` + `README` + `lib/` remain so the Pi re-run works unchanged.

---

## 10. The four decisions for Nick

1. **D1/D4 fold + the Pi re-run.** Co-sign D1 = empirically confirmed and D4 = sized-but-freeze-on-Pi; schedule the **Session D Pi re-run** of the V2-A harness before D4's thresholds hit the spine. *(Blocking for: committing D4 numbers; not blocking M7.4.)*
2. **M9 unblock + the legal spot-check.** Co-sign M9-scoping-unblocked per V2-B; **commission the LOW-risk legal spot-check** (V2-B's 4-question list); confirm **Session C** is the HERO-mapping ground-truth gate (the D5 re-open trigger).
3. **Route the Doc 17 fold** (the review return's path) with V2-C as substantiation — mint **AIOT-INV-1** with the E3 structural port; sequence **AX-7 before** the AI-authoring milestone; adopt the **honest claim language**; **commission the patent search (Q1)** before any "safest/only/unique/formally-verified" marketing.
4. **Approve the SafeGate quarantine** (cosmetic; closes the open verify-before-quoting flag).

## 11. Sources
- The three returns: `context/assessments/2026-06-26_pi-dispatch-latency-and-log-growth_spike.md`; `…_converter-db-embed-pipeline-design.md`; `…_aiot-safety-frame-and-ai-authoring_research.md`. Spike code: `homesynapse-core/spike/dispatch-latency-and-log-growth/`.
- Spine evidence: `decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md` (D1–D5); `context/assessments/2026-06-26_v6-fanout-validation-and-dispatch-reconciliation_PM-memo.md` (first-wave); `context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md` (Session A); `design/17-aiot-and-cloud-readiness.md` (DRAFT) + `context/audits/2026-06-26_Doc17_independent_DOCS_Review_Return.md`; `context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md` (the SafeGate-bearing study).
- Hub verification: `git status` per repo + `stat` mtimes (write-isolation proof); independent re-verification of arXiv **2508.02721** ("Blueprint First, Model Second") via web search.

<!--
file: context/assessments/2026-06-26_v6-fanout-validation-and-dispatch-reconciliation_PM-memo.md
purpose: v6 hub reconciliation — the result of (a) the mandatory freshness preflight, (b) a full validation of every factual assertion in the 2026-06-23 parallel-fanout dispatch brief, and (c) the corrected per-session dispatch given that §1 was RATIFIED 2026-06-25 (after the brief was written). Surfaces what is still live, what is overtaken-by-events, and what is escalated — so we do not carry a stale premise (or fabricated hardware data) forward.
audience: Nick (co-sign the corrected dispatch + the proposed spine folds), the v6 hub.
state-type: assessment / hub reconciliation
status: RETURNED 2026-06-26. Proposes spine folds; does NOT apply them (spine is single-writer + needs Nick's co-sign).
-->

# v6 Fan-Out — Validation + Dispatch Reconciliation (2026-06-26)

## Bottom line (read this first)

The 2026-06-23 dispatch brief is **factually sound** — I validated every license, hardware, state, and prior-art assertion in it against primary sources and the codebase, and they hold (two small corrections/notes below). But the brief's **framing is partially overtaken-by-events**: it was written 2026-06-23 to *feed* the §1 deeper-M7 architecture decision, and **§1 was RATIFIED 2026-06-25** (`decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md`, Nick co-signed D1–D4). So blindly dispatching all four sessions "to feed §1" would re-litigate decided questions and — for Session C — risk fabricating hardware data I cannot actually capture. The diligent execution is: **run the one session that still gates an open decision (A), narrow the one that's already covered (B), and escalate the two that need the physical bench / are confirmatory (C, D)** — which is what I did.

**What I produced (write-isolated, additive — no spine files touched):**
- `2026-06-23_zigbee-converter-db-license-feasibility_assessment.md` — **Session A, executed in full** (unblocks §1 D5).
- `2026-06-23_explainability-differentiator-moat_research.md` — **Session B, focused delta** (patent/IP + honest framing; the platform sweep was already done).
- this memo.

---

## 1. Freshness preflight — AGGREGATE: PASS

The hivemind is current; the issue is a stale *brief*, not a stale *spine*.

```
FRESHNESS PREFLIGHT — 2026-06-26
Check 1  (PROJECT_SNAPSHOT timestamp):   PASS*  (body reconciled to 06-25 true HEADs; masthead last-verified line still reads 06-22/v5 — cosmetic re-stamp wanted)
Check 2  (current week plan W26):        PASS   (IN_PROGRESS)
Check 3  (commits vs snapshot):          PASS   (core HEAD 5363347 = snapshot; hivemind 837e743 = snapshot)
Check 4  (milestone backlog):            PASS*  (M7.3 DONE↔5363347 reconciled via currency notes; backlog masthead last-verified is old — cosmetic)
Check 5  (pm-handoff Open Risks):        PASS   (OR-M7-WIRING / OR-M13-SDNOTIFY well-formed; beat 8 = 06-25)
Check 6  (coder next-unit pointer):      PASS   (M7.3 DONE → M7.4 NEXT)
Check 7  (MODULE_CONTEXT populated):     PASS   (automation/device-model/event-model all populated)
Check 8  (cross-agent-notes active):     PASS   (newest 06-22, within 14d)
Check 9  (dual skill mirrors):           PASS   (both diff -rq empty — Nick's mirror sync landed; the masthead "STALE until sync" is now cleared)
Check 10 (strategic-context-map refs):   PASS   (spot-checked refs resolve)
Check 11 (source round-trip):            PASS   (PendingCommandLedger/CommandDispatchService/CommandIssuedEvent resolve in source; counts 71/41/53 consistent)
```
`*` = two cosmetic masthead re-stamps proposed in §5; neither blocks forward work.

---

## 2. Validation of the brief's assertions — all checked, verdicts

| # | Assertion in the brief | Verdict | Evidence |
|---|---|---|---|
| 1 | `zigbee-herdsman-converters` is **MIT** | ✅ TRUE | LICENSE file + package.json `"license":"MIT"` (v26.73.0) |
| 2 | `zha-device-handlers` is **Apache-2.0** | ✅ TRUE | pyproject.toml `license="Apache-2.0"` (pkg `zha-quirks`) |
| 3 | `zigbee-herdsman` (implied permissive) | ✅ TRUE (**MIT**) | LICENSE file (MIT) |
| 3b | **(new nuance)** the Z2M *application* | ⚠️ **GPL-3.0** — must not vendor/link; it's the app, NOT the converter DB we'd consume. Distinction now recorded in Session A | zigbee2mqtt.io |
| 4 | Wave-1 stick = Sonoff Dongle Plus **MG24 / EFR32MG24 / EZSP**, Thread-capable | ✅ TRUE (real retail product) | Amazon/Lowes/SONOFF listings |
| 4b | **(naming caution)** the older "**ZBDongle-E**" is **EFR32MG21**, *not* the Wave-1 MG24; "ZBDongle-P" is CC2652P/ZNP (Wave 2) | ✅ note | sonoff.tech / Z2M discussion #13373 |
| 5 | **SNZB-03P** pairs to any Zigbee 3.0 coordinator; "SONOFF bridge required" is marketing | ✅ TRUE | Z2M device page + ITEAD HA docs |
| 6 | Philips Hue A19 pairs **direct**, no Hue bridge | ✅ TRUE (standard Zigbee; minor: may need factory-reset/Touchlink, pair close to coordinator) | Z2M (Hue is a first-class supported device) |
| 7 | HA traces: in-memory, default 5, evicted, **not created when a trigger never matches** | ✅ TRUE | HA troubleshooting docs + core issues #117133/#70310 |
| 8 | "nobody durably does why-not" | ✅ DEFENSIBLE but it is "absence of evidence," not cleared FTO (per Session B) | patent scan + platform docs |
| 9 | M7.2b GREEN / action model FROZEN | ✅ TRUE | core `1b0b6c9` |
| 10 | M7.4 + Doc 07 §3.11/AMD-90 are DOWNSTREAM of §1, not dispatched now | ✅ TRUE — and §1 is now ratified, so these are the hub's *next* serial work | §1 record §"Downstream sequencing" |
| 11 | "the executor never emits `command_issued` today" | ✅ TRUE at the producer level — the event TYPE exists + is consumed by the ledger, but nothing *publishes* it (that's M7.4a) | grep: no `publish(CommandIssuedEvent)` in main |
| 12 | All internal file refs (bench brief, lane prompts, design 02/08, prior-art study) | ✅ ALL EXIST | filesystem |

**Net: zero false assertions.** The brief is trustworthy; the only thing wrong with it is its age relative to the 06-25 §1 ratification.

---

## 3. The staleness finding — what changed between 06-23 (brief) and today

The v6 hub already ran the §1 deliberation (orchestrator §8.B) and **ratified it 2026-06-25**, taking the **prior-art study** as its headline input (not the fan-out). Result:
- **D1** command-pipeline = **logical event-driven, physically co-located** — RATIFIED.
- **D2** pure-function-replay invariant — RATIFIED.
- **D3** additive event versioning — RATIFIED.
- **D4** log retention/snapshot discipline — RATIFIED (design now, *sized* by Session D's numbers).
- **D5** converter-DB direction — **HELD, PENDING Session A.**

So the brief's "these sessions feed §1" framing is OBE for D1–D4. Only **D5 still hangs on a dispatched session (A).**

---

## 4. Corrected per-session dispatch

| Session | Brief's framing | Reality after 06-25 | Action taken | Status |
|---|---|---|---|---|
| **A — converter-DB license/feasibility** | feeds §1 / Decision 4 | **Still fully live** — D5 is *explicitly* HELD PENDING Session A; gates M9/device strategy | **EXECUTED in full** → report delivered with HIGH/MED-HIGH-confidence recommendation (adapt-the-data + curated-subset fallback; license is permissive-clean) | ✅ DONE |
| **B — why-not differentiator + moat** | feeds the positioning claim | **Live but ~80% pre-covered** by the 06-21 + 06-23 research; genuine gap = patent/IP (open Q1, MEDIUM) + honest framing | **NARROWED + EXECUTED as a focused delta** → report delivered (no patent blocks; claim the durable projection, not confirmation; needs counsel before "unique") | ✅ DONE (delta) |
| **C — hardware bench bring-up** | feeds M9 ground truth + Doc 02/08 | **Live but Nick-driven hardware** — Wave 1 on the desk, corpus still empty; **I cannot bring up a physical MG24/pair devices** without fabricating data | **PREMISES VALIDATED + de-risk notes (below); ESCALATED to Nick's bench.** Did NOT fabricate corpus entries | ⛔ NICK-DRIVEN |
| **D — Pi dispatch-latency + log-growth spike** | feeds §1 Decision 1 + log-retention | **Latency half is now CONFIRMATORY** (D1 ratified; the record says "latency does not drive the architecture"); **log-growth half still sizes D4**; both need **Pi-class hardware** + a Coder-built harness; the prior-art forward-plan already folds D into the bench's single "Pi-performance spike" | **REFRAMED + DEFERRED** — recommend running it as the bench's Pi-performance spike (D4 sizing), not as an independent now-spike to validate D1 | ⛔ DEFER → bench |

### Session C — de-risking notes for Nick's bench (validated, actionable)
1. **Reference stack for the EZSP/MG24 path: prefer ZHA (bellows) over Zigbee2MQTT.** Z2M's EZSP/Ember support is documented as the *experimental/younger* driver; ZHA's bellows is the more mature EZSP path. The brief says "Zigbee2MQTT/ZHA" — for the MG24 specifically, lead with ZHA to de-risk bring-up. (If Z2M is preferred for the `exposes` data capture, capture identity/clusters on ZHA first, then cross-check.)
2. **Record the EmberZNet/EZSP firmware version FIRST** — the MG24 is newer silicon; the EZSP protocol-version-mismatch hard-failure class is real. Confirm the chosen stack's bellows/ember driver supports the stick's EZSP version *before* pairing. (The brief already flags this — reinforcing it.)
3. **Naming:** the Wave-1 stick is the **MG24 (EFR32MG24)**. Don't confuse it with the older "ZBDongle-E" (EFR32MG21) — different silicon. Wave-2's ZNP stick is the **ZBDongle-P (CC2652P)**.
4. **Hue:** pairs direct (standard Zigbee); if it won't join, factory-reset (power-cycle sequence or Hue app/Touchlink) and pair close to the coordinator.
5. This is the single most valuable parallel track right now (the prior-art forward plan agrees) — but it is **yours to run**; I've de-risked it, not done it.

---

## 5. Escalations + proposed spine folds (Nick co-signs)

**Decisions for Nick:**
1. **Ratify §1 D5** using Session A: accept "**adapt-the-data (declarative core) + curated-subset/community fallback (long tail); reject runtime-interop & rebuild**," and commission the LOW-risk legal spot-check (Apache-2.0 NOTICE mechanics + TS→Java derivative-work form). This moves D5 from HELD → RATIFIED and unblocks M9 scoping.
2. **Confirm the corrected dispatch** (A done, B delta done, C = your bench, D = reframed as the bench Pi-performance spike). Confirm we are **not** re-running C/D as autonomous sessions.
3. **Session B IP:** decide whether to commission a real freedom-to-operate / defensive-publication pass before any "unique/only" marketing language.

**Proposed spine folds (I did NOT apply these — single-writer + your co-sign):**
- `decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md` → update D5 from HELD to RATIFIED once you accept Session A.
- `PROJECT_SNAPSHOT.md` + `pm-handoff.md` → note Session A/B returned + folded; re-stamp the two cosmetic masthead `last-verified` lines (Check 1/4) to 06-25/v6.
- `project-knowledge/device-corpus/` → still awaiting your bench (Session C).
- Then the hub proceeds serially per the §1 record: **Doc 07 §3.11/AMD-90 reconciliation (§8.C) → M7.4a → M7.4b.**

## 6. Sources
Primary license/hardware/HA sources are cited inline in the two companion reports. Spine evidence: `decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md`; `context/status/PROJECT_SNAPSHOT.md`; `context/handoff/pm-handoff.md` (beat 8); `context/assessments/2026-06-23_prior-art-study_PM-assessment-and-forward-plan.md`; git HEADs core `5363347` / hivemind `837e743`.

<!--
file: context/planning/2026-06-11_M7-blueprint_research-architecture.md
purpose: Post-M6 deliberation beat output — the multi-session deep-research architecture from which the M7/M8 blueprint is synthesized. Defines the parallel-session decomposition (R14-A / R14-B / R15 + PM-internal W0), REC-range partitioning, dispatch mechanics, the synthesis protocol, and the M7-runway checklist.
audience: PM, Nick
update-cadence: per research-cycle event (dispatch / return / synthesis)
state-type: planning
status: PROPOSED — PM default per the veto-or-default pattern; Nick rules at dispatch
last-verified: 2026-06-11 against core HEAD `62a81e6` (M6.2 working tree in flight) and research high-water REC-140 (Research 13)
-->

# M7+ Blueprint — Deep-Research Architecture (Research 14/15 cycle)

**Consuming milestones (the no-research-without-a-consumer rule, satisfied up front):** R14-A/R14-B → the **M7/M8 charter + the M7 entry-gate AMD block + the M7.1 coding instruction**. R15 → **M5-C website/docs** (P6 floor) + the strategy layer (`context/strategy/`). W0 → the M7 charter directly. Anything in a return without a consumer is parked by the disposition table, not actioned.

---

## 1. Why three external sessions, not one

Research 7 (48K brief, sprawling return) is the cautionary precedent; Research 13 (one tight register, 11 RECs, A− return) is the success pattern. The automation domain spans **two registers that degrade when mixed** — community/UX evidence (Mom-Test, failure-mode anecdotes, forum archaeology) and engineering prior art (scheduler correctness, ledger semantics, concurrency models). A researcher alternating registers produces neither well. Split them; run them simultaneously; let the PM synthesis recombine.

**The decomposition:**

| Session | Register | Scope (RQ families) | REC range | Feeds |
|---|---|---|---|---|
| **R14-A — Automation Authoring & Operating UX: Failure Modes** | Community-evidence / Mom-Test | (1) authoring failure catalog — where HA automations/scripts, Node-RED flows, SmartThings Routines, Hubitat Rule Machine, Homey Flows actually break users (syntax, mental-model, refactoring churn); (2) debuggability — the "why didn't it fire?" problem: what run-trace/observability exists, what users beg for; (3) reliability expectations — what users assume about command confirmation, retries, offline devices (our Pending Command Ledger is the differentiator — find the evidence that proves the market gap); (4) migration/versioning churn of automation definitions; (5) concurrency footguns users actually hit (vs the ones engineers imagine) | **REC-141–155** | M7/M8 charter priorities; M5-C superiority material (the Research-13 §1/§3.1 pattern) |
| **R14-B — Automation Engine Runtime: Robustness Prior Art** | Engineering | (1) temporal-trigger correctness prior art — DST/clock-skew/downtime catch-up semantics vs our AMD-25 `for_duration` + Clock-injection discipline; (2) cascade/loop containment — how engines bound runaway automation chains vs Doc 07 §3.7.1 `cascadeDepth` (default 8, 1–32); (3) intent-confirmation loops — command ledgers, ack/confirm correlation, timeout semantics in other systems vs §3.11.2; (4) run persistence/recovery across restart — timers, in-flight runs, and the event-sourced REPLAY interaction (re-derive, never re-execute — the AMD-41-class hazard applied to automation side effects); (5) event-storm behavior — queue/backpressure/coalescing postures vs our QUEUED/PARALLEL `maxConcurrent` modes | **REC-156–170** | M7/M8 charter + the M7 AMD block + M7.1/M8.x instructions |
| **R15 — Ecosystem & Competitive Positioning Scan** | Strategic | Matter/Thread certification dynamics + trajectory; platform strategy shifts (HA/Nabu Casa commercialization, SmartThings/Aeotec, Apple/Google/Amazon local-control pushes); the local-first/privacy positioning landscape; open-source governance + licensing risk patterns; where a trust-brand local-first system wins/loses commercially | **REC-171–185** | M5-C website + `context/strategy/` refresh; NOT a code consumer — code-facing findings route through the disposition table to FUTURE parking only |
| **W0 — PM-internal (no external session)** | Governance | Research-4 currency delta (below); DQ-1/2/3/5 escalation refresh; M7 AMD-block sizing per P1; M7/M8 charter skeleton | — (no new RECs; re-dispositions REC-31..40) | The charter itself |

**REC-range partitioning is what makes simultaneity safe** — three returns can land in any order without number collisions, and each return's disposition table folds independently. Ranges are generous on purpose; unused numbers are simply never minted (the research high-water advances to the max actually used).

## 2. W0 — the Research-4 currency delta (run before the returns land)

Research 4 (2026-05-22, REC-31..40: 8 ACCEPT / 2 MODIFY+ACCEPT / 0 REJECT, all targeting M7 AMDs) was **design-prior-art research against the pre-M4 codebase**. It is not stale wholesale — but every disposition must be re-anchored:

- **Survived-by-construction:** the Phase-2 automation surface it verified against (52 types, 4 sealed hierarchies) is frozen and unchanged through M6.
- **Re-anchor required:** REC-39 (automation event schema, HIGH-risk) against the **post-AMD-52 typed-payload + post-M6.4 P2 fan-out reality** — the event-manifest pin discipline (now 55/24/36) and the publish-count-pin survey category (the M6.4 lesson) did not exist when REC-39 was dispositioned. REC-36 (`RunContext`/`cascadeDepth` replacement) against current source. REC-31/34/35 permit arithmetic against the current sealed permits.
- **Still-open strategic calls (escalate at the charter, not before):** DQ-1/2/3/5 from the Research-4 assessment — these are Nick's calls and gate the AMD block, not the research dispatch.
- **New since Research 4, must be folded:** B2 **C8 `actorRef`** (automations stamp `AutomationId` — a direct M7 contract; ratification is on the W25 critical path), the M6 config pipeline as the automation-definition loading substrate (Doc 07 §3.3 ↔ AMD-66 listener semantics for automation reload), and OR-M6-NONCE-style co-design discipline as the pattern for run-persistence hazards.

## 3. Dispatch mechanics (the Research-13 pattern, made parallel)

1. **One brief per session, self-contained.** No brief references another brief; shared ground is duplicated verbatim into each. A researcher must never need a sibling return.
2. **Verbatim embeds (the Research-6 lesson — non-negotiable):** each R14 brief embeds the automation `module-info.java` verbatim at the dispatch sha, the MODULE_CONTEXT type-inventory summary, and the Doc 07 § anchors its RQs are gap-relative to (§3.3–§3.13, §4.1 as scoped above). R15 embeds the strategy-layer file list + the INV-CE-01 split-brain-immunity claim (endorsed by Research 13) as its positioning baseline. Module names from the Knowledge Primer are summaries, not authoritative.
3. **§0 quote-back gate first** (the Research-13 device that worked): the researcher opens by quoting back the embedded baseline; a return that fails the quote-back is discarded unread past §0.
4. **Gap-relativity gate:** Locked ground (Doc 07 TCA model, the sealed permits, AMD-25, the ledger ownership) is the *baseline to measure against*, never an open question. "HomeSynapse should adopt a TCA model" = discarded finding.
5. **Mandatory disposition-table aim:** every REC arrives pre-bucketed by the researcher (ALREADY-COVERED / M7-OBLIGATION / M8-OBLIGATION / FUTURE-AMD / POST-MVP / REJECT) — the PM re-buckets, but the researcher aiming at the table is what kept Research 13's REJECT bucket honest.
6. **Venue:** R14-A/R14-B → the DOCS Project, web search required (forum/issue-tracker evidence is the point). R15 → **generic deep research permitted** for evidence-gathering (the Research-13 masthead fallback), but the disposition pass always runs in-Project against the strategy files.
7. **Evidence standards:** primary-source quotations with URLs; community claims need 2+ independent reports or a maintainer statement; engineering claims need source/docs citations. Mom-Test framing for R14-A (what users *did*, not what they say they want).

## 4. Synthesis protocol (returns → blueprint)

**Fold order is engineering-first:** R14-B → R14-A → R15. Rationale: R14-B findings constrain what the engine can promise; R14-A evidence then prioritizes *which* promises matter; R15 only positions what survives both. Each return gets the standard 6-step A–F assessment (its own `context/assessments/` file, raw return archived to docs `research/returns/` per Step 0).

**The merged disposition pass** produces ONE table spanning REC-31..40 (re-anchored) + 141..185: collision adjudication rules — (a) Locked docs and ratified invariants win over any REC; (b) where R14-A evidence and R14-B prior art conflict, evidence-grade decides (primary > secondary > inference); (c) any REC requiring a new module edge or event-manifest change is automatically an AMD-block item, never an instruction-level fold (the P2-fan-out discipline).

**Blueprint output (the consuming artifacts, in order):**
1. **M7/M8 charter** — multi-piece per P1 (the M6-charter pattern: first-class M7.x rows, each with its own done-when; the smell test says automation core will NOT fit in fewer than ~3 pieces — trigger/condition path, action/dispatch path, ledger — and the charter must show that at scoping, not discover it in arrears).
2. **The M7 entry-gate AMD block** (the AMD-66..71 pattern): Research-4 re-anchored RECs + R14 obligations → one PROPOSED block, DOCS-reviewed, ratified before M7.1 issues.
3. **M7.1 instruction-readiness checklist:** AMD block RATIFIED; B2 C8 RATIFIED; M6 wrapped (M6.2 committed; M6.3 issued-or-formally-deferred past M7 start — Nick's call at the W25/W26 boundary); automation MODULE_CONTEXT current; the §4c arch-rule reminder + P2 survey rows pre-built.

## 5. Guardrails

- **No re-researching Locked ground** (above) — and no M6.3 creep: at-rest encryption stays triple-gated; nothing in this cycle touches it.
- **No dispatch before its brief passes the PM self-review** (`references/review-and-quality.md`) — three briefs, three self-reviews.
- **Simultaneity is for the external sessions only.** PM assessment of returns is serialized (fold order above); never fold two returns in one pass.
- **R15 cannot mint code obligations.** Its RECs route to strategy/M5-C or FUTURE parking. A positioning scan that starts redesigning the engine has left its register.
- **Token discipline at assessment:** read returns against the brief's §5 ("what the PM does with the return"); do not re-derive the embedded baseline.

## 6. Sequencing (W25 view)

```
now ──► W0 currency delta (PM, this/next session)
   ├──► author 3 briefs (PM; on this doc's spec; self-review each)
   ├──► Nick: veto-or-default this architecture + dispatch all 3 simultaneously
   │       (R14-A, R14-B → DOCS Project; R15 → generic deep research allowed)
   ├──► returns land (any order) ──► serialized A–F assessments (fold order B→A→15)
   ├──► merged disposition ──► M7/M8 charter + M7 AMD block (PROPOSED → DOCS review → ratify)
   └──► M7.1 instruction (gated on the §4.3 checklist)
Parallel, unchanged: M6.2 closeout; M6.3 evidence gates (Nick-paced); B2 C8/C9; M5-C floor (P6).
```

**Open items for Nick at dispatch:** (i) confirm the 3-way split (alternatives considered: 2-way = R14 whole + R15, rejected for register-mixing; 4-way = splitting Matter/Thread out of R15, rejected as below the dispatch-overhead threshold); (ii) confirm REC ranges; (iii) the M6.3-vs-M7 ordering question is NOT decided here — the charter surfaces it.

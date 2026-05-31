<!--
file: context/handoff/2026-05-31_timestamp-model-unifier_AMD_session_prompt.md
purpose: Kickoff prompt for the FRESH Cowork conversation that authors the timestamp-model unifier design beat → small AMD (the gating decision before the unifier Coder WU). Paste into the new window to start.
audience: PM (next Cowork session) ← Nick
state-type: handoff
status: CURRENT — 2026-05-31
-->

# Session Prompt: Timestamp-Model Unifier — Design Beat + Small AMD (`lastChanged` / `lastUpdated` event-time vs wall-clock)

**You are the PM (Mode 1, Architect).** This session authors the **timestamp-model unifier** design beat and the **small AMD** that ratifies it. This is the gating decision before any code: the unifier Coder WU cannot start until this AMD ratifies. The work is a contract decision about how the State Projection sources `EntityState.lastChanged` / `lastUpdated`, *not* a coding session. **Load the `nexsys-project-manager` skill first.**

---

## 0. Session-start discipline (do first)

1. **Load `nexsys-project-manager`** and **run the freshness preflight** (`project-manager/references/freshness-preflight.md`, 10 checks). Expect **PASS**: `homesynapse-core` HEAD `72596cb` (M4.0b-4b), `homesynapse-core-docs` `cacec27` (AMD-52 body-fold), `nexsys-hivemind` `f304d22` (M4.0b-4b WUCP Phase 2). Check 9 (skill-mirror) may read **STALE-pending-sync** if Nick's external mirror sync hasn't run — normal, non-blocking. If `nexsys-hivemind` `f304d22` was not pushed, that is local-only and does not affect the preflight (Check 3 compares `PROJECT_SNAPSHOT` latest-commit to the `homesynapse-core` git head `72596cb` — they match). If anything else is STALE, reconcile before authoring.
2. **Source-verification rule (standing):** the in-sandbox `git`/`grep`/`wc` truncates and line-ending-churns this synced folder (this chain saw a spurious ~18-file "modified" hivemind list and a `git diff` that falsely showed `checkAll` deleted in `HomeSynapseArchRules.java`). Verify every type/field/line claim with the **Read tool on the working tree** at HEAD `72596cb` — never trust in-sandbox `git`/`grep` for source facts.
3. **Ground truth (confirm at session start):** HEAD `72596cb`. `projectionVersion` = **4**. On-disk amendment watermark = **AMD-52**. **Workstream A is COMPLETE — typed end-to-end** (M4.0b-1/-2/-3/-4a/-4b all shipped; `StateChangedEvent` carries typed `com.homesynapse.value.AttributeValue`, the `AttributeValue` Jackson codec lives in `core/persistence`, materialization + checkpoint are typed, Path-B legacy degrade is wired). No code is in flight.

---

## 1. The problem this AMD resolves (do NOT re-derive from scratch — it is source-confirmed)

`StateProjection` sources the `EntityState` activity timestamps **two different ways across the replay/LIVE boundary**:

- **LIVE** (`applyToState`, the `state_changed` branch): `lastChanged` and `lastUpdated` are set to **wall-clock** `now = clock.instant()` (HEAD `72596cb`, `StateProjection.java` ~L784 + the `EntityState` construction ~L825–834 — both the 5th `lastChanged` and 6th `lastUpdated` args are `now`).
- **Backfill** (`applyBackfillAttribute` via `backfillTimestamp`, the AMD-50 3→N reconciliation replay): `lastChanged` is set to the **event-time** of the causing envelope (`eventTime ?? ingestTime`, log-fixed — `StateProjection.java` ~L895–897, ~L939). The code carries an explicit `[REVIEW]` note (~L918) flagging this as a "conscious interim."

**Two things make this matter now, not later:**

1. **It is a replay-determinism gap.** Event-time `lastChanged` is replay-deterministic; wall-clock `lastChanged` is not. AMD-52 made the `projectionVersion` 3→4 reconciliation a **live, exercised** path (it just ran on first boot at `72596cb`). So the same observable "last activity" field now provably **diverges across every version-bump boundary** — exactly the path-dependence AMD-50 (AMD-50-INV-03 determinism) exists to forbid, sitting in a field AMD-50 left as interim.
2. **It already contradicts the documented contract.** **Doc 03 §4.1** (`EntityState` record) specifies `lastChanged` = "the `event_time` (falling back to `ingest_time`)…" and `lastUpdated` likewise = "the `event_time` (falling back to `ingest_time`) of the most recent event processed." The LIVE wall-clock code is a latent **doc/code mismatch**, not just an internal inconsistency. Aligning LIVE to event-time brings the code into compliance with the contract the doc already states.

So this is closer to "ratify the model the doc already implies + fix LIVE to match + restore determinism" than to "invent a new contract." It is small and bounded. **It is the honest last mile of Workstream A.**

---

## 2. The decision to make (the fork — Nick's call; PM recommends)

**Q: Which timestamp model wins for `lastChanged` / `lastUpdated`?**

- **Option A — event-time everywhere (PM RECOMMENDATION).** LIVE `applyToState` sources `lastChanged`/`lastUpdated` from the envelope's `eventTime ?? ingestTime` (the same `backfillTimestamp` rule the backfill already uses), making both fields replay-deterministic and bringing LIVE into compliance with Doc 03 §4.1. The LIVE envelope already has `eventTime` and `ingestTime` in hand, so it is feasible with no new plumbing.
- **Option B — keep wall-clock in LIVE.** Would require *changing the doc* (§4.1) to say wall-clock for LIVE and event-time for backfill, and would leave `lastChanged` replay-non-deterministic by design — an explicit carve-out from AMD-50-INV-03. Higher governance cost, weaker correctness story.

**Scope to settle in the beat (verify each against source before asserting):**

- `lastChanged` → event-time (Option A). **Confirm.**
- `lastUpdated` → event-time per Doc 03 §4.1 line ~461. **Confirm the LIVE code currently uses wall-clock here too** (it does at L831) and decide it moves with `lastChanged`.
- `lastReported` → already event-time? **Verify** the `state_reported` branch's sourcing; likely already log-time, but confirm.
- `staleAfter` / `stale` → these are **real-time freshness** concepts (compared against `Instant.now()`); they legitimately **stay wall-clock**. The AMD must explicitly carve these OUT of the event-time rule so the unifier is not misread as "no wall-clock anywhere."
- `availability_changed` branch (L836–846) also sets `lastUpdated = now` — fold it into the same rule.

**Open governance item — the AMD number.** Watermark is **AMD-52**; the P2 projection band **50–52 is exhausted** (50/51/52 all used). Per `context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md` the integration band is "assign-at-milestone" and Research 6 *tentatively* eyes 53/56/59 for integration (M9, far off). **Do NOT assume a number — propose the next free integer and escalate to Nick** before stamping the amendment.

---

## 3. The work — deliverable for this session

1. **Author the design beat / small AMD** (`homesynapse-core-docs/design/amendments/AMD-NN_*.md`, status PROPOSED): the timestamp model decision (Option A recommended), the explicit `lastChanged`/`lastUpdated` event-time rule, the `lastReported`/`staleAfter`/`stale` carve-out, the AMD-50-INV-03 determinism tie-in, and 1–2 new invariants (e.g., "AMD-NN-INV-01: `EntityState.lastChanged`/`lastUpdated` are sourced from `eventTime ?? ingestTime`, never wall-clock; replay-deterministic"). Mirror AMD-50/51/52 structure (§2 spec, §4 invariants, §5 tests, §7 source anchors).
2. **Cite source anchors** (§7) verified with the Read tool at `72596cb`: `StateProjection.applyToState` (L784, L825–834, L836–846), `backfillTimestamp` (L895–897), `applyBackfillAttribute` (L939), the `[REVIEW]` note (~L918); `EntityState` (Doc 03 §4.1 / the record); Doc 01 INV-ES-08 (`event_time` vs `ingest_time`); AMD-50 §2.4 (Clock removed from `DerivationContext`) + AMD-50-INV-03.
3. **Tee up the Coder WU** (do not write it until the AMD ratifies): a small `core/state-store` change (LIVE `applyToState` sources `lastChanged`/`lastUpdated` from the envelope time; tests assert replay-determinism — a LIVE-then-replay-from-zero run yields identical `lastChanged`). It is a **no-`projectionVersion`-bump** change *iff* it does not alter already-materialized state semantics — **decide and state this explicitly** (if LIVE timestamps change for new events only, no reconciliation is forced; if it rewrites historical materialized values, it rides a bump). Include the §4c arch-rule test-`Clock` reminder (state-store non-whitelisted).
4. **Escalate the AMD number to Nick** (§2 open item) before finalizing.

**Parallel track (optional, mention to Nick):** Workstream B's coding instruction (**AMD-44 RATIFIED-pending-impl**, staged Stage 1 Floor + `Set<HardwareIdentifier>` + minimal Area → Stage 2 EntityRole; Research 8 PM assessment on file) can be authored in parallel with this AMD — B is unblocked on contract, gated only on PM authoring. Confirm sequencing with Nick.

---

## 4. What is frozen — do NOT reopen

AMD-52 typed payload (codec mechanism, Path A/B, `schema_version` 1→2), `projectionVersion` = 4, the AMD-50 reconciliation backfill, AMD-51 comparator, the `com.homesynapse.value` relocation. This AMD touches **only** the `EntityState` timestamp sourcing in the LIVE projection path — nothing in the typed-value pipeline, the codec, or the event/checkpoint shapes.

---

## 5. Pointers

- Source to re-verify at `72596cb`: `core/state-store/src/main/java/com/homesynapse/state/StateProjection.java` (`applyToState`, `backfillTimestamp`, `applyBackfillAttribute`, the `[REVIEW]` note), `EntityState`.
- Docs: `homesynapse-core-docs/design/03-state-store-and-state-projection.md` §4.1 (the `lastChanged`/`lastUpdated`/`lastReported`/`staleAfter`/`stale` field contracts); `01-event-model-and-event-bus.md` INV-ES-08 (`event_time` vs `ingest_time`).
- Amendments to mirror + tie into: `design/amendments/AMD-50_*.md` (§2.4 Clock removal, AMD-50-INV-03), `AMD-51_*.md`, `AMD-52_*.md`; `governance/Architecture_Invariants_v1.md` (register the new invariant); `context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md` (AMD-number bands).
- Backlog/status: `context/planning/phase-3-milestone-backlog.md` (the unifier is the named next front; M4 parent row), `context/status/PROJECT_SNAPSHOT.md`, `context/handoff/pm-handoff.md` (latest section = M4.0b-4b closeout, the locked sequence unifier → B → C).
- Prior interim record: M4.0b-2 closeout (PROJECT_SNAPSHOT + pm-handoff) flagged "interim mixed-`lastChanged`… the timestamp-model unifier is a separate WU."

**Bottom line:** Workstream A is typed end-to-end (`72596cb`, `projectionVersion` 4, watermark AMD-52). The one remaining thread inside A is the `lastChanged`/`lastUpdated` LIVE-wall-clock vs backfill-event-time split — now a live-exercised replay-determinism gap *and* a Doc 03 §4.1 mismatch. Author the small AMD (recommend **event-time everywhere**, carve out `staleAfter`/`stale`), assign its number with Nick, and tee up the bounded `core/state-store` Coder WU. Then Workstream B.

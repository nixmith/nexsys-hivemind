<!--
file: context/audits/2026-09-06_HERO-0_intake_two-layer-audit_v66-b6.md
purpose: The hub's two-layer audit of the HERO-0 return (the null census of the v1.1.3 read-API) under the program §5's pre-filed predictions P1–P3; the four freeze-note rows F1–F4 ruled; the ten EXPLAIN rows → the v1.1.4 batch; DESIGN: start becomes lawful.
audience: the hub · the hero charter (FE) · the v1.1.4 EXPLAIN batch (Core) · Nick (the F1 word)
state-type: intake audit
status: FILED v66 beat 6 (Sun 2026-09-06 ~12:2x CT; instrument 2026-09-06T17:2xZ). Return: context/research/2026-09-06_HERO-0_null-census_v1.1.3_return.md (9,996 B; RETURNED 16:48Z; 28 min of a 2 h clock). Verdict: ACCEPT — P1–P3 MET; F1 is a DEFECT ON THE WIRE (source-verified); F2 is the manufactured-type class at d192d17 (source-verified); the EXPLAIN rows are the hero's measured holes.
-->

# HERO-0 intake — two-layer audit (v66 beat 6)

## §0 Verdict card
**ACCEPT.** The census is what the charter asked for — a table of every read × every null/absent key × its meaning at source × the honest sentence — and its three headline findings re-execute at the bytes. **F1 (a defect on the wire NOW):** `StateProjection.initialEntityState(entityId, seed)` seeds `lastChanged`, `lastUpdated` AND `lastReported` with the adoption event's stamp (the three `seed` arguments in the constructor call), so a never-reported entity serves its registration instant as `lastReported` — the v1.1.3 CG-3 key can lie about freshness; the freeze doc's "null when the projection holds none" arm is dead at the store. **F2 (the manufactured-type class, still at `d192d17`):** `shapes.ts` `isStr(req(a, 'command', …))` and `subjectRef(req(trigger, 'subjectRef', …))` require non-null while the emitter serves null for skipped/failed actions (`StandardExplanationService` ~`:776` → `ActionView(…, null, …)`) and for a trigger whose event is outside the correlation; the mocks populate both. **F4:** `RunExplanation` `:213–:219` says `parentRunId` "always null in V1"; a renderer that reads null as "root" is false at depth > 0. **P1–P3 MET** as the lane adjudicated them (36 null/absent sites; two nulls with a wrong or missing source meaning; NEVER_TRIGGERED instance-scoped). The return is 9,996 B against a 10,240 cap (the fourth capped return of the day, the fourth at the cap). **Disclosed non-re-executions:** the 36-site count not re-tallied (three of its rows re-read at source); the lane's Playwright-free read (it built nothing, as chartered).

## §1 Rulings
- **F1 → LASTREPORTED-1 (Core; the honesty batch, §3 of the assessment):** two shapes — (a) seed `lastReported` null in `initialEntityState` and let only `state_reported` set it (the key then means what the freeze says; the FE renders "no report on record"); (b) keep the seed and document it as "last report, or first-seen". **The hub recommends (a)** — a freshness key that can carry a registration stamp is exactly the false type the live-wire law exists to kill. H10 word `F1: seed-null | document`. Until it lands the FE shows no "current" claim from `lastReported` alone (HERO-0's own fence). **H8-a's B2 reads this key today:** the record will show three non-null values; the audit reads them as F1 says (registration stamps for the never-reported entities are lawful VALUES under the current code and a defect under the freeze's intent) — not a packet failure.
- **F2 → FE-NULL-1 (FE; a fast-follow on `d192d17`, ≤½ day):** `actions[].command` · `actions[].targetRef` · `trigger.subjectRef` · `conditions[].observedState[].value` typed `| null`, validated `strOrNull`/`refOrNull`, one null-arm mock each; the freeze doc gains the four rows (the hub's write, v1.1.3 note). Predictions: 4 M + 0 A; red-first by construction on the validators.
- **F3 → a freeze-doc line** ("`trigger.subjectRef` is null when the triggering event is outside the run's correlation — Core states when") + a docket row for the EXPLAIN-2 key.
- **F4 → a freeze-doc line + FE-NULL-1's fifth row** (render depth > 0 with a null parent honestly).
- **EXPLAIN-1…10 → the v1.1.4 EXPLAIN batch** (the assessment §3; the CG-123 pattern; 5/6 first as the lane says — the hero's lead). EXPLAIN-10 is F1.
- **`DESIGN: start` is LAWFUL** (Nick's word "hold — until HERO-0 returns; then from the four empty states outward under the NAME token"): the hero charter opens on the four empty states in §2 of the return (their microcopy is the design ground), the three questions only.

## §2 Layer 2 — at the bytes
| Claim | Instrument | Result |
|---|---|---|
| F1 seeded at first sight | `StateProjection.initialEntityState` — `new EntityState(entityId, Map.of(), UNKNOWN, 0L, seed, seed, seed, null, false)` | CONFIRMED |
| F2 validator rejects lawful nulls at `d192d17` | `shapes.ts:256` `subjectRef(req(…))`; `:272` `isStr(req(a, 'command'…))` | CONFIRMED |
| the emitter serves `command: null` on skip | `StandardExplanationService` ~`:776` `new ActionView(…, targetRef, null, "{}", …)` | CONFIRMED |
| F4 `parentRunId` always null | `RunExplanation.java:213–:219` javadoc | CONFIRMED |
| FE-113 landed mid-lane, emitter unchanged | `d192d17` touches `web-ui/dashboard/` only (16 files) | CONFIRMED |

## §3 What this opens
LASTREPORTED-1 (Core, small) · FE-NULL-1 (FE, small) · the v1.1.4 EXPLAIN batch (Core, the month's WU) · the hero charter (FE, design from the empty states) · three freeze-doc lines (the hub). Nothing for Nick's hands today; one word (`F1:`) Monday.

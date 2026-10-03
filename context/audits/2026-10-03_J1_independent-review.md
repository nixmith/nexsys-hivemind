<!--
file: context/audits/2026-10-03_J1_independent-review.md
purpose: THE ONE-WAY-DOOR REVIEW of J1's instruction (the skill §3 law 16; coding-instruction-format #33) — written by an in-conversation agent that had not seen the authoring, from the instruction, the pre-verification and 27 source files staged byte-exact from homesynapse-core `5b0e20c`; its verdict DISPATCH WITH EDITS; its seventeen edits (four BLOCKING) were applied to the instruction before the dispatch line was handed (the b2 audit §2). The review text below is VERBATIM as returned.
audience: the hub · the J1 lane · the v96 boot
state-type: review (verbatim; never edited)
status: FILED v95 beat 2 (Sat 2026-10-03 ~12:4x CT; instrument 2026-10-03T17:41:46Z); the edits APPLIED
-->

# ONE-WAY-DOOR REVIEW — J1 (LINK-READ-2 + IR-121) at `5b0e20c`

## §0 Verdict
**DISPATCH WITH EDITS** — the door itself is sound (tolerant decode, nullable record, by-name checkpoint all hold at the bytes), but four textual defects would send the lane after a test that can never go green and a wire contract two endpoints cannot render; §3 E1–E4 fix them without a design reversal.

## §1 The premise rows
| # | Verdict | Lines seen | Note |
|---|---|---|---|
| 1 | HOLDS | A:606, :608, :613; :166 = 50 | |
| 2 | HOLDS | T:53, :55, :294–:330, :302, :312–:316, :317–:320, :326–:327, :343 | |
| 3 | HOLDS | A:181, :692, :695, :699, :704, :706–:707, :712 | |
| 4 | HOLDS | T:35–:46, :108, :178 | |
| 5 | HOLDS | T:79, :184, :193, :206, :56–:66 | |
| 6 | HOLDS / part UNCHECKABLE | E:17–:20, :28–:37; A:1707, :1708, :1710–:1718 | `EventTypes.java` not staged |
| 7 | HOLDS | Codec :143, :154 (`classFor(eventType)`, no version), :174 only gate, :187 catch-all; Mapper :108 | **Mapper :106 `SNAKE_CASE`** — the wire keys are snake_case (E1) |
| 8 | HOLDS | SP:944, :948, :1109–:1111; ES:90–:100; CS:49, :70–:74 | |
| 9 | HOLDS / misquote | L:189–:203; GetEntity :37; GetEntityState :44–:46 | GetEntityState:43 is blank, no shape; the row keys are **camelCase** |
| 10 | HOLDS / part UNCHECKABLE | Capability :98; PowerMeter :43–:52, :60; Resolver :28, :102; Occupancy/Illuminance declare none | EnergyMeter, StalenessConfig, Motion not staged |
| 11 | HOLDS / log UNCHECKABLE | RC:81, :86; `DefaultRow(…, min, max, change)` :63–:64 | |
| 12 | HOLDS | AR:25, :28, :31, :34, :41 (+`LEAVE` :44) | |
| 13 | HOLDS | SP ×7: :896, :920, :933, :945, :956, :1055, :1090; CS:255 | a third file is likely: `MaterializedStateQueryService` (GetEntityState :44–:46) — not staged |
| 14 | HOLDS / misquote | TE:559, :568 bind `ace` (not `a`); read `newStatus()` only (:563, :572); :581–:582 type-check | |
| 15 | HOLDS | test :46 `hasSize(2)`, :44 | |
| 16 | HOLDS / part UNCHECKABLE | ListEntitiesEndpointTest :203–:204 pins the key list; :97/:184/:225–:226 pin values only; helper :262 | Get*EndpointTest not staged |
| 17 | HOLDS | CST :115–:124, :152, :181 | |
| 18 | HOLDS / part UNCHECKABLE | Slice :542; A:1708; Resolver :134–:135 (`CapabilityInstance.capabilityId()` — ids, never `Capability`) | `Entity.java` not staged |
| 19 | UNCHECKABLE | — | no log in the staged set |

## §2 The one-way door
**(a) Decode.** :143 → `classFor(eventType)` :154 (type only) → the StateChanged-only gate :174 → `readValue` :186, every throw → DegradedEvent :187. Mapper: records native (:39), unknown keys ignored :108, `NON_NULL` on write :107 — a v2 event with five nulls writes the v1 byte-shape. Both directions hold **if the five additions are boxed/reference types**. No `@JsonCreator`, custom deserializer or version pin in the staged set. **Trap 1:** `SNAKE_CASE` :106 (test :346–:361 pins it) — the keys are `previous_status`, `new_status`, `reason`, `last_seen_at`, `lqi`, `rssi_dbm`, `link_at`; T6's camelCase literal reads as two unknown keys → `previous_status` null → NPE at E:29 → :187 → **DegradedEvent, never the record**. **Trap 2:** mapper javadoc :61–:63 — a secondary constructor on the record risks conflicting creators. **Trap 3:** `TestEventSamples.availabilityChanged()` (codec test :141, not a Files row) goes red.
**(b) Checkpoint.** `SerializableEntityState` :277–:287 (camelCase, `Instant staleAfter` :285) ← :242 / → :263; read by name via `TypeReference` :200 — no key count, order or per-entity version; absent keys → null for reference types. `link` needs an internal `SerializableEntityLink(int lqi, int rssiDbm, Instant at)` beside :277, written `null` under `Include.ALWAYS`. `projectionVersion` :295 is the code's version (:137) — do NOT bump (replay-from-zero yields the same nulls). Rollback: the TEST mapper ignores unknown keys :74 "mirroring the composition root" (not staged); if the root does not, :203 throws → clear-and-replay (:85–:87), lossless.
**(c) Projection sites.** :896, :920, :933, :956, :1055 carry the prior's three; :945 sets from the event; :1090 nulls (the [INFO] case); CS:255 from the serialized record.
**(d) Lock.** `transition` :357 holds :361–:390, fires :395 OUTSIDE — snapshot `lastSeen/lastLink/lastLinkAt/reason` into locals before :390; a timeout leaves `lastSeen` alone (:373–:379), so it IS the last evidence instant. `LinkReading` is two ints (:670/:672, test :465); the instant lives at T:134 → Files row 1's signature **omits `lastLinkAt`**, so §4.3's `linkAt` cannot come "from the listener's arguments" (row 3). `evaluateTimeouts` already calls `powerSourceLookup` UNDER the lock (:312); §9's rule needs a two-phase shape (snapshot → lookups → compare → `transition`, which :325–:328 already fires outside). The publish site: `onTransition` :1650 has `lastReason` :1661 and `linkFields` :1660; **no `lastSeen` accessor exists** (interface :26–:97); `publishForEntities` :1704 has a SECOND caller, `seedFreshAdoption` :1696–:1702, with no listener args. T:393's line is byte-frozen (A:1652–:1653).
**Read-API (step 4).** Only :203–:204 pins the key set; appending three keys breaks exactly that line. The two Get endpoints put the **record itself** in `data` (:125, :114) via Javalin's Jackson (:42–:43): the new components render there automatically under their **component names**, after `stale`; no per-key code exists, and state-store has no Jackson (module-info :140–:150) so no `@JsonProperty`. `availability_reason`/`rssi_dbm` are unachievable on two of three endpoints and would be the surface's first snake_case keys.
**Derivations (step 5).** Single device 60 + 0.05 + 5 = 65.05 s ✓ (:314 strict `>`, A:613 per cycle, A:745). Fleet-wide the pings are SEQUENTIAL on the run thread (:693–:708): 60 + 5·N + 0.05 — N = 5 → 85.05 s; N ≥ 6 breaches 90. The resolver is per-ENTITY and three-source (override :127 → smallest declared :133–:143 → global default :146): "the same rule" is ambiguous; reusing `thresholdFor` lets `default_staleness_threshold` shorten every battery device's 25 h. PowerMeter "2 × 600 s" :47 ✓. RC :81/:86 max 3600 ✓.

## §3 EDITS
1. **[BLOCKING] §7 T6, Files row 8, §8.** Current: `decode("availability_changed", 1, '{"previousStatus":"online","newStatus":"offline"}')`. Replace: `decode("availability_changed", 1, '{"previous_status":"online","new_status":"offline"}') (the persistence mapper is SNAKE_CASE, PersistenceObjectMapper:106; the v2 wire keys are reason, last_seen_at, lqi, rssi_dbm, link_at — pin with contains("\"rssi_dbm\"") as EventPayloadCodecTest:346–:361 does; a camelCase literal decodes to a DegradedEvent)`. §8 persistence: name the seven wire keys.
2. **[BLOCKING] §1 ¶2, Files row 15, §4.4, T9, §8, §13.** Current: `availability_reason`, `last_seen_at`, `link` (`{lqi, rssi_dbm, at}`). Replace everywhere: `availabilityReason`, `lastSeenAt`, `link` (`{"lqi": n, "rssiDbm": n, "at": "…Z"}`); append to row 15: `ListEntitiesEndpoint.summarise (:189) appends the three explicitly, the instants via toString() as lastReported (:201–:203); GetEntityEndpoint (:125) and GetEntityStateEndpoint (:114) serialize the EntityState record itself — the components render by name with NO handler code; their only edit is the Javadoc shape (:37). T9 pins presence/names on all three and the ISO-8601 form on the list endpoint only.`
3. **[BLOCKING] Files rows 1, 3; §4.3.** Current: `carries (device, instant, available, reason, lastSeen, lastLink)`. Replace: `carries (device, instant, available, reason, lastSeen, lastLink, lastLinkAt) — LinkReading is two ints, the instant is kept apart (T:133–:134); all four snapshotted into locals inside the lock before :390 and passed at :395, never re-read through lastLink()/lastLinkAt() after the unlock.`
4. **[BLOCKING] §4.2.** Current: `the same rule RegistryStalenessResolver uses for staleAfter, row 10 — reuse its lookup if it is reachable`. Replace: `source 2 of the resolver's chain ONLY (:133–:143: the smallest declared interval over the entity's CapabilityInstance ids against the StandardCapabilities catalog), the minimum across adoption.entitiesFor(device) — NEVER the per-entity override (:127) nor the global default (:146); staleness_overrides and default_staleness_threshold do not bear on availability. Reuse by constructing a resolver with Map.of() and Optional.empty(), or mirror :133–:143; say which.`
5. **[SHOULD] Files row 3.** Append: `publishForEntities (A:1704) has a second caller, seedFreshAdoption (:1696–:1702), with no listener arguments: it passes reason = lastReason(device), the reading = lastLink/lastLinkAt(device), and lastSeenAt from a new package-private Optional<Instant> lastSeen(IEEEAddress) on T (under the lock, shaped as :206).`
6. **[SHOULD] T1 + §9 Clock bullet.** Current: `(T, Clock.fixed)` … `the assertion on 600 s turns red first`. Replace: `(T, the suite's TestClock — test :7/:58/:137 advance it; Clock.fixed cannot) … the red is the NEW 61-s assertion (no existing assertion names 600 s or MAINS_PING_SILENCE; :162/:179/:193/:217 advance 11 min and stay green); move the :386 1-min seed to 30 s — it sits on the new 60-s boundary (:314 is strict >).` §9: `Clock.fixed(…)` → `the module's TestClock`.
7. **[SHOULD] §6, Files row 8.** Add `grep -rn 'new AvailabilityChangedEvent(' --include=*.java . | grep '/test/' | wc -l` and the row `P/TestEventSamples.java (availabilityChanged(), codec test :141) — M`.
8. **[SHOULD] Files row 6.** Append: `no secondary constructor (PersistenceObjectMapper javadoc :61–:63); the canonical 7-arg constructor is the only creator; the five additions boxed/reference-typed.`
9. **[SHOULD] T8.** Current: `loads a pre-J1 checkpoint (no such keys) with nulls`. Replace: `loads a pre-J1 checkpoint built by serializing with the new code, parsing to an ObjectNode and removing the three keys per entity — never a hand-written literal (the root's naming strategy is not read by this unit; the test mapper :70–:76 has none).`
10. **[SHOULD] §9 lock bullet.** Append: `the shape: under the lock snapshot (device, state, lastSeen) per entry (:299–:321), release, apply both lookups outside (powerSourceLookup runs under the lock today, :312 — move it too), compare, then transition() as :325–:328 does.`
11. **[SHOULD] §4.1 comment.** Append: `fleet-wide the pings are sequential (A:693–:708): 60 + 5·N + 0.05 s for N simultaneously silent mains devices — 85.05 s at the run fleet's five; the acceptance holds for N ≤ 5.`
12. **[SHOULD] §0b row 13 Found.** Append: `expected hits beyond the projection's seven: CheckpointSerializer:255 and MaterializedStateQueryService (GetEntityStateEndpoint:44–:46) — a row each.`
13. **[SHOULD] Files row 13.** Append: `an internal SerializableEntityLink(int lqi, int rssiDbm, Instant at) beside :277, null under Include.ALWAYS; projectionVersion (:295) NOT bumped.`
14. **[NIT] §0b row 14.** `a` → `ace` (:559/:568); add :581–:582.
15. **[NIT] §6 bullet 1.** `5 production sites` → `5 use sites; the LINE count is ≥ 10 (imports, :1106, :581–:582)`.
16. **[NIT] §9.** Add: `T:393's line is byte-frozen (A:1652–:1653); the "10 min" Javadoc at AvailabilityTracker:13–:15, AvailabilityReason:39, T:22–:27/:52/:281–:283 and test name :156 move with the constant.`
17. **[NIT] Files row 17.** If Occupancy declares, revise Capability:89–:91 ("binary sensors … declare nothing").

## §4 Not checked
Not staged: `EventTypes`, `EventEnvelope`, `EnergyMeter`, `Motion`, `Entity`, `StalenessConfig`, `LinkReading`, `TestEventSamples`, `EventTypeRegistry`, `JacksonWarmup`, `MaterializedStateQueryService`, the root's checkpoint mapper (naming, unknown-key posture), Javalin's mapper (Instant rendering), `Get*EndpointTest`, the MODULE_CONTEXT files, the 070945 log, the ArchUnit rules.

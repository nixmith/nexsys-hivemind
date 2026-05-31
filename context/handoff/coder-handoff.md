<!--
file: context/handoff/coder-handoff.md
purpose: Coder session continuity — current task, deferred build gate, next WU, recent closeouts.
audience: Coder, PM
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-27 against M3.7 closeout working tree — `./gradlew check` GREEN (139 tasks). Pending commit.
-->

# Coder Session Handoff

**Last updated:** 2026-05-31 (**M4.0b-4b (AMD-52 typed `StateChangedEvent` payload + `AttributeValue` codec + typed materialization + Path-B gate + `projectionVersion` 3→4) COMPLETE — files produced, BUILD GATE DEFERRED to Nick (see Deferred Build Gate § below). Implements AMD-52 §2.1–§2.7 on the M4.0b-4a relocated `com.homesynapse.value` packages. Two new package-private persistence types: `AttributeValueSerializer`/`AttributeValueDeserializer` (hand-rolled `{"t":…,"v":…[,"u":…]}` tagged-union codec, exhaustive no-`default` switch, float bit-identity + `NaN`/`±Inf` sentinels + `−0.0`→`+0.0`), registered in `PersistenceJacksonModule`. `StateChangedEvent.oldValue/newValue` String→`AttributeValue` (oldValue nullable). `ProductionDerivationRule` emits typed at `schema_version=2`. `StateProjection.applyToState`/`applyBackfillAttribute` materialize typed; `shouldPublishDerived` typed-to-typed `equals`. `CheckpointSerializer` typed envelope (`Map<String,AttributeValue>`, ALWAYS null round-trip preserved). `EventPayloadCodec` Path-B gate (`state_changed`+v1→`DegradedEvent`). `HomeSynapseCore` `projectionVersion` 3→4. New ArchUnit rule `NO_JACKSON_IN_DOMAIN_MODEL` (value/event/device/state Jackson-free). New `AttributeValueSerdeTest` + extended `EventPayloadCodecTest`/`CheckpointSerializerTest`/`ProductionDerivationRuleTest`/`StateChangedEventTest`/`ReconciliationTest`/`StateProjectionContractTest`/`TestEventSamples`/`SqliteStateStoreTest`. NO `module-info`/`build.gradle.kts` change (the `requires com.homesynapse.value` edges already existed from 4a — the event-model→device STOP-gate did NOT fire). Next WU = see "Next work unit" below.** Prior: **M4.0b-4a (AttributeValue hierarchy relocated to the new `com.homesynapse.value` leaf module — AMD-52 §11 erratum) COMPLETE — build gate GREEN (`./gradlew check`), promoted from the M4.0b-4a compile-spike worktree. Pure behavior-preserving relocation: 10 types moved device→value, the `requires com.homesynapse.value` edge set wired (transitive on event/device/state, plain on persistence/automation, test-only on rest-api), all imports swept, MODULE_CONTEXTs updated. `com.homesynapse.event` does NOT `requires com.homesynapse.device` — the cycle is broken. NO semantics/`projectionVersion`/`StateChangedEvent` change. Next WU = M4.0b-4b (the AMD-52 typed `StateChangedEvent` payload, rebased on the relocated packages). Prior: M4.0b-3 (AMD-51 typed `AttributeValue` change-detection comparator) COMPLETE — files produced, BUILD GATE DEFERRED to Nick (see Deferred Build Gate § below). Next WU = AMD-52 typed `StateChangedEvent` payload (staged behind OQ-05-08 — do NOT start until that design beat closes).** New state-store types: public `AttributeValueComparator` (+`structural()`), `ComparisonPolicy` (`FP_NOISE_DEFAULT 1e-9`), `AttributeSchemaResolver` (+`of`/`empty`); package-private `StructuralAttributeValueComparator` (exhaustive no-`default` 8-arm switch, IEEE-754 totality) + `AttributeValueReconstructor` (schema-driven both-sides parse). New device-model production type `StandardCapabilities` (DP-K — `all()`/`attributeSchemas()`, lifted from `TestCapabilityFactory` which now delegates). `ProductionDerivationRule` rewritten typed (reconstruct-both-sides → `comparator.changed`, **String payload preserved** — DP-G); `DerivationRule.production(comparator,policy,schemas)` overload added (no-arg kept = string-fallback). `HomeSynapseCore` wires comparator+policy+resolver, bumps `projectionVersion` **2→3**. 4 new test suites (`StructuralAttributeValueComparatorTest`, `AttributeValueReconstructorTest`, `ProductionDerivationRuleTest`, `StandardCapabilitiesTest`) + `ReconciliationTest` +2 typed tests. **NO `module-info`/`build.gradle.kts`/`CheckpointSerializer`/event-store change.** One `[REVIEW]`: missing-schema → `StringValue` fallback (not §2.6 Degraded/no-emit) — see cross-agent-notes 2026-05-30. **Key de-risk: every existing test + integration test uses non-catalog attribute keys (`power`/`v`/`attr`/`level`/`k`/`color`) → string-fallback path → behaviour identical to M4.0b-2; the typed path is exercised only by new tests (`temperature_c`).** Prior: **M4.B3 (AMD-47 AttributeValue expansion + `AttributeValueUpcaster` SPI) COMPLETE + committed `60b4185`, build GREEN; PM WUCP Phase 2 closed.** Build gate RESOLVED — Nick ran `./gradlew :core:state-store:check` + `:lifecycle:lifecycle:check` + full `check` (139 tasks) GREEN. PM Phase 2 read every changed file vs source and confirmed targets A–J; AMD-50-INV-01..04 upheld. Implements **AMD-50** (RATIFIED) for the 1→2 transition on the M4.0b-1 string change-detect rule: `projectionVersion` 1→2 in `HomeSynapseCore`; the `backfillActive` provenance gate in `StateProjection` (set in the reconciliation branch of `initialize()`, cleared in `onCaughtUp()`); a non-emitting one-shot backfill applied on BOTH `onEvent` and `processBatch` via the narrow `applyBackfillAttribute` helper (attributes + event-time `lastChanged` only; no second `stateVersion` increment — INV-01); supersession suppression in `applyToState`'s `state_changed` branch (gate-conditional); `Clock` removed from `DerivationContext` (§2.4). All six AMD-50 §5 tests added/extended across `ReconciliationTest` (+6) and `StateProjectionContractTest` (rebuild-idempotency extended, determinism adjusted, 4 `DerivationContext` sites updated). **Next: M4.B3 then M4.0b-3** (typed comparator/payload, AMD-47/51/52 — reuse this backfill path unchanged for the 2→3 transition). Prior: **M4.0b-1 COMPLETE + committed `cf1a97e`, build GREEN**; M4.0a COMPLETE `a441fdf`.)

Canonical Coder handoff file referenced by the nexsys-coder skill (`../context/handoff/coder-handoff.md`). A duplicate at `homesynapse-core/docs/handoff/coder-handoff.md` (created during a Cowork session) was consolidated into this file on 2026-05-15 and removed.

---

## M4 Readiness — read before the first M4 coding brief (2026-05-28)

**M4 scope = Canonical.** Plan: `homesynapse-core-docs/design/HomeSynapse_Core_M4_Implementation_Plan_PLAN-M4-CONSOLIDATED.md`. Three workstreams — A (projection/derivation foundation), B (device-model expansion, Research 8 REC-23–30 + AMD-44 Floor/EntityRole impl), C (integration-api interface freeze, Research 6 REC-41–51; supervisor impl = M9).

**First WU = M4.0a** (decision-free): wire the existing `AtomicCheckpointWriter` (`com.homesynapse.persistence` — already implemented + tested by `AtomicCheckpointWriterTest`/`AtomicCheckpointWriterDlqTest`) into `StateProjection.writeCheckpoint()`, and remove the per-delivery bus subscriber-checkpoint for the `state_projection` subscriber (AMD-45). Extend `CrashRecoveryHttpIT`. Fold OR-M3-13 + H2 + the `HomeSynapseCore` `MINIMAL_DERIVATION_RULE` Javadoc fix ("state_reported → state map update" is imprecise — the `EntityState` record is replaced and `stateVersion`/timestamps advance, but `attributes` are written only on `state_changed`).

**M4.0b is the hard gate** (after M4.0a): replace `MinimalProjectionAdvancer` with `DispatchingProjectionAdvancer` (REC-28 — constructor-injected, package-private per-event-type handlers, **no ServiceLoader** per DECIDE-04) AND promote a real production `DerivationRule` (lift `EchoStateRule`'s change-detect logic out of testFixtures; extend from string-only to typed `AttributeValue` incl. the Research-8 `QuantityValue`/`ArrayValue`). It MUST publish `state_changed` (or state/numeric triggers never wake). On REPLAY it **re-derives but does NOT re-publish** (publish is LIVE-only; AMD-41 §3.2.2). Shipping a real rule bumps `projectionVersion` 1→2 → reconciliation/replay-from-zero on first boot (AMD-41 §3.2.4); a **one-shot backfill** applies re-derived drafts to in-memory state during that 1→2 replay **only** (gated there — applying them on later replays would double-increment `stateVersion`, the documented idempotency cursor).

**Corrected fact (KB de-poison 2026-05-28):** there is **no `MinimalDerivationRule` class**. The production no-op derivation is the `MINIMAL_DERIVATION_RULE = context -> List.of()` constant lambda in `HomeSynapseCore`, bound to the `DerivationRule` `@FunctionalInterface` in `core/state-store`. `MinimalProjectionAdvancer` (package-private, lifecycle) is the real advancer class; `NotifyingEventPublisher` is the 4th package-private lifecycle type. Earlier handoff/state docs that named a `MinimalDerivationRule` class were wrong.

---

## Deferred Build Gate

**Status:** **M4.0b-4b (AMD-52 typed `StateChangedEvent` payload + codec) build gate DEFERRED to Nick (see subsection below).** Prior: **M4.0b-4a (AttributeValue relocation → `com.homesynapse.value`) build gate RESOLVED — `./gradlew check` GREEN (2026-05-31).** Prior: **M4.0b-3 (AMD-51) build gate DEFERRED to Nick (see subsection below)** — the full M4.0b-4a `check` runs on a tree layered over the M4.0b-3 changes, so they are exercised GREEN by that run too (PM may formally flip the M4.0b-3 entry). Prior gates all RESOLVED: **M4.B3 (AMD-47)** GREEN and **COMMITTED `60b4185`** (2026-05-30); **M4.0b-2** (AMD-50) GREEN `7610296`; **M4.0b-1** GREEN `cf1a97e`; **M4.0a + D-1** RESOLVED (`a441fdf`); all M3.7 gates RESOLVED 2026-05-27.

### DEFERRED — M4.0b-4b: Typed `StateChangedEvent` Payload + `AttributeValue` Codec + Replay (AMD-52, 2026-05-31)

**Build gate:** DEFERRED. The Coder produced files only (CLAUDE.md build discipline — no `./gradlew`/`javac`/`git`). Nick must run the targets below against the working tree he commits, then this entry flips to RESOLVED and the PM runs WUCP Phase 2.

**Commit the gate must run against:** the M4.0b-4b working tree layered on the M4.0b-4a relocation baseline (HEAD `971cfa1`). No commit made by the Coder. **This WU bumps `projectionVersion` 3→4.**

**Exact commands (success = GREEN):**
```
./gradlew :core:event-model:check
./gradlew :core:value-model:check          # no change expected (codec is in persistence)
./gradlew :core:device-model:check         # no change expected
./gradlew :core:state-store:check
./gradlew :core:persistence:check
./gradlew :lifecycle:lifecycle:check
./gradlew :app:homesynapse-app:check       # the NO_JACKSON_IN_DOMAIN_MODEL ArchUnit rule lives here
./gradlew check                            # full gate
```

**Files CREATED (3):**
- `core/persistence/.../AttributeValueSerializer.java` — `JsonSerializer<AttributeValue>`, the `{"t":…,"v":…[,"u":…]}` envelope; exhaustive no-`default` switch over the 8 variants; shared `static writeDouble(...)` (round-trippable number, `"NaN"`/`"+Inf"`/`"-Inf"` sentinels, `−0.0`→`+0.0`). Package-private.
- `core/persistence/.../AttributeValueDeserializer.java` — `JsonDeserializer<AttributeValue>`, reads `"t"`→`AttributeType`, dispatches; `ArrayValue` recurses; strict `readDouble` (unknown sentinel throws `JsonMappingException`). Package-private.
- `core/persistence/src/test/.../AttributeValueSerdeTest.java` — AMD-52 §5 #1–#4 (8-variant round-trip + array recursion/order, exhaustiveness guard, float bit-identity corpus, non-finite sentinels + `−0.0`, strict-decode failures).

**Files MODIFIED (main, 7):**
- `core/persistence/.../PersistenceJacksonModule.java` — registers the `AttributeValue` serde pair.
- `core/event-model/.../StateChangedEvent.java` — `oldValue`/`newValue` String→`AttributeValue`; `oldValue` nullable; compact ctor non-null on `attributeKey`/`newValue`/`triggeredBy` only; **no Jackson annotation**.
- `core/state-store/.../ProductionDerivationRule.java` — emits typed `StateChangedEvent(key, priorTyped, inboundTyped, eventId)` at `EventDraft(…, 2, …)`; `priorStringForm` removed.
- `core/state-store/.../StateProjection.java` — `applyToState`/`applyBackfillAttribute` write `sc.newValue()` typed; `shouldPublishDerived` typed-to-typed `equals`; `serializeAttribute` + `StringValue` import removed.
- `core/persistence/.../CheckpointSerializer.java` — `SerializableEntityState.attributes` → `Map<String,AttributeValue>` (typed envelope); null round-trip preserved (LinkedHashMap/HashMap, never `Map.copyOf`).
- `core/persistence/.../EventPayloadCodec.java` — Path-B gate: `state_changed` + `schemaVersion==1` → `DegradedEvent`.
- `lifecycle/.../HomeSynapseCore.java` — `projectionVersion` 3→4.
- `core/state-store/.../AttributeValueReconstructor.java` — Javadoc only (typed prior no longer transient).

**Files MODIFIED (test, 9):**
- `app/.../HomeSynapseArchRules.java` + `HomeSynapseArchRulesTest.java` — new Rule 10 `NO_JACKSON_IN_DOMAIN_MODEL` (value/event/device/state must not depend on `com.fasterxml.jackson..`).
- `core/persistence/src/test/.../EventPayloadCodecTest.java` — `stateChanged()` round-trips at v2; new `Amd52TypedStateChanged` nested class (#5 schema_version 1→2, #6 Path-B legacy degrade, nullable oldValue).
- `core/persistence/src/test/.../CheckpointSerializerTest.java` — mapper now adds `PersistenceJacksonModule`; new mixed-typed-variant + null round-trip test (#7).
- `core/persistence/src/test/.../SqliteStateStoreTest.java` — mapper adds `PersistenceJacksonModule` (codec dependency).
- `core/persistence/src/test/.../TestEventSamples.java` — `stateChanged()` typed.
- `core/state-store/src/test/.../ProductionDerivationRuleTest.java` — typed payload + `schema_version==2` + natively-typed-prior coherence (#10).
- `core/state-store/src/test/.../ReconciliationTest.java` — `changedAt`/`ToleranceRule` typed; the two `typedRule()` tests assert `FloatValue` materialization (#7/#8).
- `core/state-store/src/testFixtures/.../StateProjectionContractTest.java` — `AlwaysProducingRule` typed.
- `core/event-model/src/test/.../StateChangedEventTest.java` — typed fields; nullable-oldValue legal.

**`module-info` / `build.gradle.kts`:** **NO CHANGE** — the `requires com.homesynapse.value` edges (event/device/state transitive, persistence plain) all landed in M4.0b-4a. The event-model→device STOP-gate did **not** fire (the edge is now the legal `event → value`). Reported as required: zero `module-info` changes.

**Deviations:** one `[REVIEW]` — added a NEW ArchUnit rule (`NO_JACKSON_IN_DOMAIN_MODEL`) scoped to value/event/device/state rather than (the optional, AMD-52 §5#2-suggested) extension of Rule 7's predicate to `com.homesynapse.device`. The broader scope is a strictly stronger guard for AMD-52-INV-02 and is safe (those packages have zero bytecode Jackson dependency). See cross-agent-notes 2026-05-31. Two `[INFO]`: `DegradedAttributeValue` envelope field names chosen as `original_type_name`/`raw_form`/`failure_reason` (hand-rolled both sides, self-consistent); `shouldPublishDerived` uses `Objects`-free `currentValue.equals(sc.newValue())` (currentValue null-guarded above).

**Next work unit (refuse-to-close):** M4.0b-4b completes the **projection-block sequence M4.0b-1/-2/-3/-4** (advancer + production rule → 1→2 backfill → typed comparator → typed payload). The projection foundation (Workstream A) is now functionally complete through the typed-payload cash-out. **The next WU is not yet briefed** — candidates per the M4 plan are Workstream B (device-model expansion — Research 8 REC-23–30 / AMD-44 Floor/EntityRole impl), Workstream C (integration-api interface freeze — Research 6 REC-41–51), or the **timestamp-model unifier** (the `[REVIEW]` interim flagged in `StateProjection.applyBackfillAttribute` — `lastChanged` is event-time-sourced in backfill but wall-clock-sourced in the LIVE `applyToState` branch). **Coder is BLOCKED on the PM's next coding instruction** — request it before opening the next WU. (M7 automation consuming the typed payload is explicitly a separate, later milestone per AMD-52 §6.)

### RESOLVED — M4.0b-4a: Relocate AttributeValue Hierarchy to `com.homesynapse.value` (AMD-52 §11, 2026-05-31)

**Build gate:** **RESOLVED — `./gradlew check` GREEN (2026-05-31).** Unusually for a Coder WU, the gate is already green: M4.0b-4a was **promoted from the M4.0b-4a compile-spike worktree** (the spike proved the graph compiles acyclic, `com.homesynapse.event` does NOT `requires com.homesynapse.device`, and no type beyond the 10 was forced to move), and Nick ran the full `./gradlew check` GREEN against it. **Pure, behavior-preserving structural refactor — no semantics, no `projectionVersion` change, no `StateChangedEvent` change** (those are M4.0b-4b). Same tests pass; only import paths moved.

**Tree the gate ran against:** the M4.0b-4a relocation worktree layered on the M4.0b-3 baseline (`98f705b` + the `f699f3e` MODULE_CONTEXT doc commit).

**What changed (relocation diff — 74 files: 2 new, 10 renamed, 62 modified):**
- **NEW module `core/value-model`** (`com.homesynapse.value` — leaf, `requires` only `java.base`): `build.gradle.kts` (no project deps), `module-info.java` (`exports com.homesynapse.value`), `MODULE_CONTEXT.md`, + the 10 relocated types.
- **MOVED (`git mv` + `package` rewrite, 10):** `AttributeValue` + the 8 variants (`BooleanValue`/`IntValue`/`FloatValue`/`StringValue`/`EnumValue`/`QuantityValue`/`ArrayValue`/`DegradedAttributeValue`) + `AttributeType`, `com.homesynapse.device` → `com.homesynapse.value`. Public contracts byte-for-byte identical. **`AttributeSchema` + `AttributeValueUpcaster` STAYED in device-model** (now `import` from value).
- **`settings.gradle.kts`:** `include("core:value-model")`.
- **`requires`-edge set (confirmed by the spike):** `requires transitive com.homesynapse.value` on **event-model**, **device-model**, **state-store** (re-export value on public API → `api` Gradle scope); plain `requires com.homesynapse.value` on **persistence** (`CheckpointSerializer` internal) and **automation** (`PendingCommand` Javadoc `{@link}`) → `implementation` scope. **rest-api** got only `testImplementation(":core:value-model")` — 4 endpoint tests name the value types, rest-api main does not → **NO `module-info` edge**.
- **Imports swept:** every `import com.homesynapse.device.{valueType}` → `com.homesynapse.value.{...}` across state-store (main+test+testFixtures, ~15), persistence (main+test, 3), automation (1), rest-api (test, 4), device-model testFixtures (1); **plus the easy-miss in-package users in device-model main** that had no import (`AttributeSchema`, `AttributeValueUpcaster`, `StandardCapabilities`, `Expectation`, `ExactMatch`, `EnumTransition`, `AnyChange`, `WithinTolerance`, `ConfirmationResult`, `ParameterSchema`, `ExpectationFactory`, `AttributeValidator`) + the 13 value-type test classes.

**Findings fed back (correct design-note §4):**
- **automation** is an importer beyond the §4 set (event/device/state/persistence/rest-api) — grep-found, **Javadoc-only** reference (reachable transitively via device; explicit plain edge added as hygiene per the rule).
- **rest-api** needs a *test-classpath* edge, **not** a `module-info requires` (value usage is test-only, classpath-compiled).
- **event-model**'s edge is **forward-prep** — no value type is named in event-model code at the 4a baseline (only a prose Javadoc word in `StateReportedEvent`); pays off at 4b's typed payload. Harmless/unused now (no javac "unused requires" lint).
- **§7 vestigial `device → event`:** device-model main has **zero** `import com.homesynapse.event` (only 3 Javadoc `@see`). Confirmed vestigial; **left untouched** (out of WU scope — never invert to `event → device`).

**No type beyond the 10 was forced to move.** No Jackson annotation added to the value types (Jackson-isolation HARD RULE intact). Stale prose fixed: `integration-zigbee/AttributeReport.java` ("device-model AttributeValue" → "value-model").

**MODULE_CONTEXTs updated:** CREATE `core/value-model/MODULE_CONTEXT.md` (10 types, leaf, AMD-47 INV-01/03/04/05 travel with the types, "relocated from device-model per AMD-52 §11"); `core/device-model/MODULE_CONTEXT.md` (−10 types, 62→52 / 64→54 files; AttributeValue/AttributeType inventory rows replaced with relocation pointers; `requires transitive com.homesynapse.value`; AttributeSchema/AttributeValueUpcaster import-from-value notes; new vestigial-edge gotcha); `core/state-store`, `core/persistence`, `core/event-model`, `core/automation` dependency notes + `requires`/Gradle edges.

**Commands Nick ran (success = GREEN, all GREEN):** `./gradlew :core:value-model:check`, `:core:device-model:check`, `:core:state-store:check`, `:core:persistence:check`, `:api:rest-api:check`, then full `./gradlew check` — GREEN with **no behavioral change** (same test count passing; only import paths moved).

**Next WU = M4.0b-4b** — the typed `StateChangedEvent` payload + `AttributeValue` codec + typed materialization + Path-B gate + `projectionVersion` **3→4**, rebased on the relocated `com.homesynapse.value` packages (the existing `M4.0b-4_Typed_StateChangedEvent_Payload_Serializer.md` instruction, re-targeted to **4b**; the event-model→device STOP-gate is gone — the edge is now event→value, which is legal).

### DEFERRED — M4.0b-3: Typed AttributeValue Change-Detection Comparator (AMD-51, 2026-05-30)

**Build gate:** DEFERRED. The Coder produced files only (CLAUDE.md build discipline — no `./gradlew`/`javac`/`git`). Nick must run the targets below against the working tree he commits, then this entry flips to RESOLVED and the PM runs WUCP Phase 2.

**Commit the gate must run against:** the M4.0b-3 working tree layered on the M4.B3 closeout baseline (HEAD `60b4185`). No commit made by the Coder. **This WU bumps `projectionVersion` 2→3.**

**Files created (8):**
- `core/device-model/src/main/java/com/homesynapse/device/StandardCapabilities.java` — DP-K production catalogue (`all()` + `attributeSchemas()` + 15 typed factories), lifted from `TestCapabilityFactory`.
- `core/state-store/src/main/java/com/homesynapse/state/AttributeValueComparator.java` — public interface + `structural()`.
- `core/state-store/src/main/java/com/homesynapse/state/StructuralAttributeValueComparator.java` — pkg-private impl (exhaustive no-`default` 8-arm switch).
- `core/state-store/src/main/java/com/homesynapse/state/ComparisonPolicy.java` — public record (`FP_NOISE_DEFAULT`).
- `core/state-store/src/main/java/com/homesynapse/state/AttributeSchemaResolver.java` — public interface + `of`/`empty`.
- `core/state-store/src/main/java/com/homesynapse/state/AttributeValueReconstructor.java` — pkg-private schema-driven both-sides parse.
- `core/state-store/src/test/java/com/homesynapse/state/StructuralAttributeValueComparatorTest.java`, `AttributeValueReconstructorTest.java`, `ProductionDerivationRuleTest.java` (+ `core/device-model/src/test/java/com/homesynapse/device/StandardCapabilitiesTest.java`).

**Files modified (6):**
- `core/state-store/.../ProductionDerivationRule.java` — rewritten typed (ctor `(comparator,policy,schemas)`; reconstruct-both-sides → `comparator.changed`; **String `StateChangedEvent` payload preserved**, DP-G).
- `core/state-store/.../DerivationRule.java` — no-arg `production()` now = typed rule + empty resolver (string-fallback); new overload `production(comparator,policy,schemas)`.
- `lifecycle/lifecycle/.../HomeSynapseCore.java` — wires `structural()` + `FP_NOISE_DEFAULT` + `AttributeSchemaResolver.of(StandardCapabilities.attributeSchemas())`; `projectionVersion` literal **2→3**.
- `core/device-model/src/testFixtures/.../TestCapabilityFactory.java` — 15 standard factories delegate to `StandardCapabilities` (dedup; public API unchanged) — `[INFO]` deviation.
- `core/state-store/src/test/.../ReconciliationTest.java` — +2 typed tests (2→3 transition §5#6, shouldPublishDerived coherence §5#10) + `typedRule()` helper + `StandardCapabilities` import.
- `core/state-store/MODULE_CONTEXT.md`, `core/device-model/MODULE_CONTEXT.md` — type inventories + counts + AMD-51 status APPLIED.

**Commands Nick must run (success criterion = GREEN):**
1. `./gradlew :core:device-model:check` — load-bearing. New `StandardCapabilities` (main) + `StandardCapabilitiesTest`; `TestCapabilityFactory` refactor (testFixtures) — its public API is unchanged so all downstream consumers compile. ArchUnit `NO_DIRECT_TIME_ACCESS` scans the new test (no time access).
2. `./gradlew :core:state-store:check` — load-bearing. 5 new types + the typed `ProductionDerivationRule`/`DerivationRule` + 3 new test suites + `ReconciliationTest` additions. **All pre-existing state-store tests use non-catalog keys → string-fallback → unchanged behaviour.**
3. `./gradlew :lifecycle:lifecycle:check` — `HomeSynapseCore` step-6 rewiring + `projectionVersion` 2→3. `HomeSynapseCoreTest` unaffected (fresh DB → no checkpoint → no reconciliation; gate inactive).
4. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — **verified unaffected by inspection:** every IT reports non-catalog keys (`power`/`v`/`attr`/`level`) → string-fallback → identical to M4.0b-2; assertions use entity COUNT + `getViewPosition() >= N`. The 2→3 bump on a fresh DB has no loaded version to mismatch (gate inactive).
5. `./gradlew check` — full-project regression.

**No `module-info.java`/`build.gradle.kts`/`libs.versions.toml` change** — all state-store types land in the already-exported `com.homesynapse.state`; `StandardCapabilities` lands in the already-exported `com.homesynapse.device`; `HomeSynapseCore` reaches `com.homesynapse.device` through `requires transitive com.homesynapse.state → requires transitive com.homesynapse.device` (verified against the actual `module-info.java` files), and device-model is on the lifecycle compile classpath via state-store's `api(project(":core:device-model"))`. No `CheckpointSerializer`/event-store/`StateChangedEvent` change (typed payload = AMD-52).

**Deviations (none BLOCKING):**
- **[REVIEW] D-1 — missing-schema → `StringValue` fallback** (not the §2.6 error-table literal "Degraded / no-emit"). Rationale: preserves M4.0b-2 behaviour for unschematized keys (no attribute-freeze regression), the materialized prior is itself a `StringValue`, and it keeps the no-arg `production()` gateway backward-compatible so the entire pre-existing suite (non-catalog keys) stays green unchanged. In production the `StandardCapabilities` resolver covers all standard traffic. Posted to cross-agent-notes for PM adjudication. The mandatory QUANTITY `canonicalUnitSymbol`-fallback WARN (§2.6 gate) is unaffected; missing-schema logs DEBUG.
- **[REVIEW] D-2 — ARRAY reconstruction degrades** (no element-type metadata in `AttributeSchema` at M4.0b-3); the comparator's array semantics ARE implemented + unit-tested directly. No standard attribute is ARRAY, so this is latent (parallels the QUANTITY-not-production-exercised note in DP-K).
- **[REVIEW] D-3 — parse-failure → Degraded inbound (no-emit), not strict halt** (§2.6 left the choice to the coding instruction). A malformed single report degrades + WARNs and is suppressed by the comparator, rather than halting the whole projection (DoS-safety); no Degraded reaches canonical state (AMD-47-INV-04).
- **[INFO] D-4 — QUANTITY `canonicalUnitSymbol`-fallback WARN tested by inspection, not a captured-appender assertion** (a logback `ListAppender` test would add an uncertain test-classpath dependency in a build-deferred environment). The fallback *behaviour* (value reconstructed via `canonicalUnitSymbol`) is asserted.
- **[INFO] D-5 — `TestCapabilityFactory` refactored to delegate to `StandardCapabilities`** (DP-K SHOULD; flagged per the brief). Public API and returned objects are byte-for-byte identical (logic lifted verbatim), so downstream consumers are unaffected.
- **[INFO] D-6 — added `StandardCapabilitiesTest`** (device-model) for the new production type (test-first), not enumerated in the brief's file list.

**STOP-on-Mismatch gates:** all PASS. `ProductionDerivationRule.evaluate` had the `instanceof StateReportedEvent`/`Objects.equals` string compare; `DerivationContext` was the 2-arg no-clock record; `DerivationRule` `@FunctionalInterface` + `production()`; `StateProjection` evaluate sites at `onEvent`/`processBatch`, `applyToState`/`applyBackfillAttribute` write `new StringValue(...)`, `shouldPublishDerived` string dedup; `QuantityValue` canonicalises at construction; `AttributeValueUpcaster` interface-only (no production impl, left unchanged); module-infos as embedded. The DP-K confirm-step held (TestCapabilityFactory liftable with no test-only deps; no standard key collides with a differing type; attributeKey-keyed resolver sufficient).

### RESOLVED — M4.B3: AttributeValue Expansion + AttributeValueUpcaster SPI (AMD-47, 2026-05-30)

**Build gate:** RESOLVED — Nick ran `./gradlew :core:device-model:check` + `./gradlew check` (139 tasks) GREEN, 2026-05-30. PM WUCP Phase 2 closed. (Originally DEFERRED — Coder produced files only per CLAUDE.md build discipline.)

**Commit the gate must run against:** the M4.B3 working tree layered on the M4.0b-2 closeout baseline (HEAD `7610296`). No commit made by the Coder.

**Commands Nick must run (success criterion = GREEN):**
1. `./gradlew :core:device-model:check` — load-bearing. New production: `QuantityValue`, `ArrayValue`, `DegradedAttributeValue` (records), `AttributeValueUpcaster` (interface); modified `AttributeValue` (permits 5→8), `AttributeType` (+`QUANTITY`/`ARRAY`/`DEGRADED`), `AttributeSchema` (compact-ctor DEGRADED guard). New tests: `QuantityValueTest`, `ArrayValueTest`, `DegradedAttributeValueTest`, `AttributeValueUpcasterTest`; modified `AttributeValueTest` (5→8 permits), `AttributeTypeTest` (5→8 values), `AttributeSchemaTest` (+`DegradedTypeRejectionTests` nested class). The ArchUnit `NO_DIRECT_TIME_ACCESS` rule scans these test classes — none use `Clock`/`Instant.now()` (AMD-47 types are clock-free by design).
2. `./gradlew check` — full-project regression. **Expected fully GREEN with no downstream changes**: AMD-47 §7.4 + M4.B3 verification confirm there are **no** production exhaustive `switch`es over `AttributeValue`/`AttributeType` anywhere; `CheckpointSerializer:238` and `EnumTransition:23` are `instanceof` patterns with generic fallbacks, so the 3 new variants compile and flow through unchanged. No consumer module references the new types yet.

**No `module-info.java`, `build.gradle.kts`, or `libs.versions.toml` change** — all four new types land in the already-exported `com.homesynapse.device`, using only `java.util.List` / `java.util.function.DoubleUnaryOperator` / `java.lang` / in-package types (all reachable through `java.base`). Confirmed AMD-47 §7.1: no new `requires`/`exports` needed. No units-of-measure dependency (REC-93 / AMD-47-INV-03 — hand-rolled normalization).

**Deviations (none BLOCKING):** **[REVIEW] INV-04 enforcement locus (DP-2, documented interpretation)** — AMD-47 §2.4 literally says "the `AttributeValidator` rejects any schema that declares DEGRADED", but no concrete `AttributeValidator` exists; M4.B3 enforces the non-declarable clause structurally at `AttributeSchema` construction (compact-ctor guard), which is strictly stronger (a DEGRADED-typed schema can never be constructed). The never-written-to-canonical-state-under-strict-mode clause of INV-04 + the upcaster projection-path wiring + the INV-02 both-paths path test are all carried to **M4.0b-3** (DP-1). Flag both for PM adjudication at closeout. **[INFO]** `QuantityValue` uses a private nested `Conversion(String canonicalUnit, DoubleUnaryOperator toCanonical)` record + a static `Map<String,Conversion>` catalogue for the table-driven normalization (representation was Coder's call per the brief). No `[BLOCKING]` deviations; no amendment authored (AMD-47 already RATIFIED).

### RESOLVED — M4.0b-2: Version-Transition Reconciliation Backfill + `projectionVersion` 1→2 (AMD-50, 2026-05-29, `7610296`)

**Build gate:** DEFERRED. The Coder produced files only (CLAUDE.md build discipline — no `./gradlew`/`javac`/`git`). Nick must run the targets below against the working tree he commits.

**Commit the gate must run against:** the M4.0b-2 working tree layered on the M4.0b-1 closeout baseline (HEAD `cf1a97e`). No commit made by the Coder.

**Commands Nick must run (success criterion = GREEN):**
1. `./gradlew :core:state-store:check` — load-bearing. `DerivationContext` 3-arg → 2-arg (clock removed, §2.4); `StateProjection` gains the `backfillActive` field, the `initialize()`/`onCaughtUp()` gate set/clear, the `onEvent` + `processBatch` backfill branches, the `applyBackfillDraft`/`backfillTimestamp`/`applyBackfillAttribute` helpers, and the gate-conditional supersession in `applyToState`; `ProductionDerivationRule` Javadoc only. Tests: `ReconciliationTest` +6 backfill tests (+`reportedAt`/`changedAt`/`projectionFor` helpers + `ToleranceRule`, + `EventId`/`StateChangedEvent`/`Objects` imports); `StateProjectionContractTest` rebuild-idempotency extended (+`materializeViaBackfill`/`BackfillSignature`), determinism test renamed/adjusted (clock dimension gone), 4 `DerivationContext` sites updated, `ZoneOffset` import removed.
2. `./gradlew :lifecycle:lifecycle:check` — `HomeSynapseCore` step 6: the literal `1` passed as `StateProjection.create(...)` arg #2 is now `2` (+ comment). `HomeSynapseCoreTest` unaffected (fresh-DB → no checkpoint → no reconciliation → gate inactive → identical behaviour to version 1).
3. *(recommended downstream)* `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — `CrashRecoveryHttpIT`/`EndpointE2eIT` verified GREEN by inspection: both crash tests assert entity COUNT + view position, not attribute values, and both phases run identical code (version 2 == version 2 → no spurious reconciliation; the no-checkpoint replay-from-zero path has no loaded version to compare, so the gate stays inactive — behaviour identical to M4.0b-1).
4. `./gradlew check` — full-project regression.

**No `module-info.java` or `build.gradle.kts` changes** — all work is inside the already-exported `com.homesynapse.state` (+ the one-line lifecycle bump). `EventId`/`StateChangedEvent` (new ReconciliationTest imports) are reachable through existing `requires transitive com.homesynapse.event`.

**Deviations (all [INFO]/[REVIEW], none blocking):** **D-A [REVIEW]** — in `processBatch` the backfill apply runs INSIDE the read-tx processor callback, NOT as a post-advance phase parallel to the LIVE publish (the literal "parallel `else if`" the brief sketched). Source evidence: a deferred apply feeds the rule a stale prior across a batch boundary, diverging from native (a `X→Y→X` change-back split across batches loses the final `X`); the in-callback apply is a pure in-memory mutation (no publish), so the two-phase read-then-publish discipline is preserved. Brief's "Coder Pushback Welcome" explicitly invited this. **D-B [REVIEW]** — `lastChanged` now has mixed semantics (event-time in the backfill, wall-clock in the LIVE `state_changed` branch); a conscious, named interim (Doc 03 timestamp-model unifier is a separate scheduled WU), documented in the state-store MODULE_CONTEXT and the completion report. **D-C [INFO]** — determinism test `productionRuleIsDeterministicAcrossRepeatedInvocationsAndClocks` renamed to `...AcrossRepeatedInvocations` (the two-fixed-clocks dimension is gone — the context can no longer carry a clock). No `[BLOCKING]` deviations; no amendment authored (Release Gate honored — AMD-50 was already RATIFIED).

### RESOLVED — M4.0b-1: Dispatching Advancer + Production Derivation Rule (amendment-free vertical slice, 2026-05-29, `cf1a97e`)

**Build gate:** DEFERRED. The Coder produced files only (CLAUDE.md build discipline — no `./gradlew`/`javac`/`git`). Nick must run the two named `:check` targets below against the working tree he commits; `:testing:integration-tests:test` is a recommended downstream gate.

**Commit the gate must run against:** the M4.0b-1 working tree layered on the M4.0a closeout baseline (HEAD `a441fdf`). No commit made by the Coder.

**Commands Nick must run (success criterion = GREEN):**
1. `./gradlew :core:state-store:check` — new package-private `ProductionDerivationRule`, `DispatchingProjectionAdvancer` (+ nested `ForwardingHandler`), `EnvelopeHandler`; new public static factories `DerivationRule.production()` and `ProjectionAdvancer.dispatching(EventStore)` (the latter adds `import com.homesynapse.event.EventStore` to `ProjectionAdvancer.java`); `StateProjectionContractTest` shared `rule` now `DerivationRule.production()` + nested `EchoStateRule` removed + 4 new `@Test` methods; `StateProjectionVerticalIT` rule swapped + local `EchoStateRule` removed; new `DispatchingProjectionAdvancerTest` (7 tests).
2. `./gradlew :lifecycle:lifecycle:check` — `HomeSynapseCore` step 5/6 rewiring (`ProjectionAdvancer.dispatching(...)` + `DerivationRule.production()`); `MINIMAL_DERIVATION_RULE` constant and `MinimalProjectionAdvancer.java` **removed**; `projectionAdvancer` field widened to `ProjectionAdvancer`; added `import com.homesynapse.state.ProjectionAdvancer`. `HomeSynapseCoreTest` unaffected (no assertion on empty attributes; `readFrom(0,10).get(0)` is still the `state_reported`).
3. *(recommended downstream)* `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — `EndpointE2eIT` + `CrashRecoveryHttpIT` exercise the real composition root. Verified by source inspection to remain GREEN: the production rule updates attributes of *existing* entities (no new entities), so `$.data` sizes and `getViewPosition() >= N` (uses `>=`) are unaffected by the extra derived `state_changed` events.
4. `./gradlew check` — full-project regression.

**No module-info.java or build.gradle.kts changes** — both new state-store types live in the already-exported `com.homesynapse.state`; `DerivationRule`/`ProjectionAdvancer`/`EventStore` are all reachable through existing `requires transitive` edges (verified against the actual `module-info.java` files).

**Deviations (all [INFO], none blocking):** D-A [INFO] — `DispatchingProjectionAdvancer` is NOT subjected to `ProjectionAdvancerContractTest`; it has a dedicated `DispatchingProjectionAdvancerTest` instead, because the contract test's `readTxInProgress()` hook assumes a fixture-simulated tx flag that the production advancer (like the removed `MinimalProjectionAdvancer`) does not track. D-B [INFO] — nested `EchoStateRule` removed from `StateProjectionContractTest` and the local copy removed from `StateProjectionVerticalIT` (both superseded by the public `DerivationRule.production()` factory; dead after the swap). D-C [INFO] — `AdvanceResult.skipped()` NOT invented (G7); all event types forward, preserving exact `MinimalProjectionAdvancer` cursor accounting. No `[BLOCKING]`/`[REVIEW]` deviations; no amendment authored (Release Gate honored).

### OPEN — M4.0a CORRECTION: close the REPLAY-path half of AMD-45-INV-01 (D-1 resolution, 2026-05-29)

**Build gate:** DEFERRED (re-run). PM adjudicated D-1 [REVIEW] as **NOT benign** — `StateProjection.onEvent` checkpoints during REPLAY (only COLD/SUSPENDED short-circuit), so for the `state_projection` subscriber the coupled `AtomicCheckpointSink` and the ungated `ReplayDriver` writes were two independent writers to `subscriber_checkpoints` on different cadences; a crash mid-REPLAY over a >200-event log left subscriber@N > view@M and lost events M+1..N on restart — the exact AMD-45-INV-01 window, reopened on REPLAY (which the invariant does not carve out).

**Files modified (2):**
- `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayDriver.java` — both `checkpointStore.writeCheckpoint(subscriberId, ...)` sites now gated `if (!runtime.info().atomicCheckpoint())`: the final tail write (`:157`, combined with the existing `currentPosition > 0L` guard) and the periodic AMD-38-cadence write (`:186`, inside the `shouldCheckpoint` block; cadence counters still reset so loop timing is unchanged). No constructor change — `runtime.info()` is already read at `run()`.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/test/EventBusContractTest.java` — new Tier 9 test `replayDoesNotAdvanceBusCheckpointForAtomicCheckpointSubscriber`: seeds 201 events (crosses `CHECKPOINT_EVENT_THRESHOLD=200`), subscribes a non-atomic control (asserts its bus checkpoint advances to the tail) AND an atomicCheckpoint subscriber (asserts its bus checkpoint stays 0). Runs for `InProcessEventBusTest` (active runtime); skipped for `InMemoryEventBusTest` via the tier's `assumeActiveRuntime()`. FAILS without the gate.

**Complete production writer set for the `state_projection` subscriber checkpoint (PM requirement #3, verified by grep):** exactly 3 bus-side sites — `InProcessEventBus:508` (LIVE), `ReplayDriver:157` (tail), `ReplayDriver:186` (periodic) — ALL now gated. Plus the projection's `AtomicCheckpointSink` (coupled). For an atomicCheckpoint subscriber the coupled sink is the **sole** writer. The passive `subscribe()`/`subscribeWithHandler` path writes no checkpoints and is contract-test-only; `state_projection` uses `subscribeRuntime` → `ReplayDriver` + `liveLoop`. No `TransitionCoordinator`/`SubscriberSupervisor` writes.

**Re-run gate:** `:core:event-bus:check` (load-bearing — new test + ReplayDriver change), then `./gradlew check` + `:testing:integration-tests:test -PpiProfile=throttled` for full regression. The other four module checks are unaffected by this correction but should be re-confirmed by the full `check`.

D-1 is now **RESOLVED** (was [REVIEW]); the remaining accepted deviations are D-2/D-3/D-4 [INFO] (see the original entry + Completion Report).

### OPEN — M4.0a: Atomic Checkpoint Coupling + Reconciliation Plumbing (2026-05-29)

**Build gate:** DEFERRED. The Coder produced files only (per CLAUDE.md build discipline — no `./gradlew`, `javac`, or `git`). Nick must run the five `:check` targets below against the working tree he commits.

**Commit the gate must run against:** the M4.0a working tree layered on M3.7 closeout baseline (HEAD `78264a0`). No commit made by the Coder.

**Commands Nick must run (success criterion = all GREEN):**
1. `./gradlew :core:state-store:check` — new `AtomicCheckpointSink` interface; `StateCheckpointSource` 4-arg `serializeCheckpoint` default; `StateProjection.create`/ctor +1 param (`AtomicCheckpointSink`); `CheckpointRecord.projectionVersion()` `@Deprecated` (+ 2 testFixtures `@SuppressWarnings("deprecation")` sites); `ReconciliationTest` un-defers the 5th test + adds the REC-82 guard; `InMemoryStateProjectionTest`/`StateProjectionVerticalIT` construction sites updated.
2. `./gradlew :core:persistence:check` — `SqliteStateStore` 4-arg `serializeCheckpoint` override (passes metadata, no more `null,null,null`); `AtomicCheckpointWriter` H2 `executeInTransaction` extraction (behavior-preserving — existing `AtomicCheckpointWriterTest`/`AtomicCheckpointWriterDlqTest` must stay GREEN); `PersistenceFactory.atomicCheckpointSink()` new accessor; `SqliteStateStoreTest` +2 metadata tests + 1 `@SuppressWarnings` site.
3. `./gradlew :core:event-bus:check` — `SubscriberInfo` gains 4th component `atomicCheckpoint` (+ 3-arg convenience ctor defaulting `false`, so all ~50 existing 3-arg call sites still compile); `InProcessEventBus` line-500 gate; `SubscriberInfoTest` shape test 3→4 + new `atomicCheckpoint` tests. EventBusContractTest (44 methods) unaffected (all use 3-arg ctor → `atomicCheckpoint=false` → per-delivery write still fires).
4. `./gradlew :lifecycle:lifecycle:check` — `HomeSynapseCore` wiring (`atomicCheckpointSink()` injected into `StateProjection.create`; projection `SubscriberInfo` now 4-arg `atomicCheckpoint=true`) + the `MINIMAL_DERIVATION_RULE` Javadoc fix (deliverable 5). No new module-info/Gradle edges.
5. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — **`CrashRecoveryHttpIT` gains `busAheadOfViewWindowClosedByReplayFromZero`** (AMD-45 §3: HOME_DEFAULT policy + fixed sub-2s clock + 5<200 events → no checkpoint fires → bus replays from 0 → all 5 entities rebuilt & queryable via HTTP). Existing `entitiesSurviveCrashAndRestart` still passes (its comment updated for the coupled mechanism). `HomeSynapseE2eHarness` gains a 4-arg `start(...)` config overload; `HeapBudgetIT` construction site updated.
6. `./gradlew check` — full-project regression (catches any cross-module fallout from the `SubscriberInfo` arity change and the `StateProjection.create` signature change; all in-tree call sites updated).

**No module-info.java or build.gradle.kts changes** — the AMD-45 seam is a consumer-defined interface in `com.homesynapse.state` (already exported) implemented by `persistence` (already `requires com.homesynapse.state`) and injected by `lifecycle` (already `requires transitive com.homesynapse.state`). Dependency direction preserved (inward-only). The integration-tests config types (`PersistenceConfig`/`DeploymentProfile`/`RetentionPolicy`/`EventBusConfig`/`FixedCheckpointPolicy`/`HomeSynapseConfig`) are all on the existing test classpath.

**Deviations:** see the Completion Report. Summary: D-1 [REVIEW] — REPLAY-side ReplayDriver subscriber-checkpoint write was NOT gated (deliverable 2 + AMD-45 §5 scope only line 500); flagged for PM. D-2 [INFO] — REC-80 metric emitted via structured SLF4J (state-store has no metrics facade; no JFR dependency added). D-3 [INFO] — `AtomicCheckpointWriter` rollback-failure log message wording changed (context now embedded; not asserted by any test). D-4 [INFO] — seam named `AtomicCheckpointSink` (new sibling interface) rather than extending `StateCheckpointSource`, per the dependency-direction analysis.

### RESOLVED — M3.7 Closeout: abandon() contract + MinimalEventBusStub (2026-05-27)
**Build gate:** RESOLVED 2026-05-27. `./gradlew check` GREEN (139 tasks).

**What this closes:** M3.7 Finding 2 follow-up — `CrashRecoveryHttpIT` previously left the entire first harness fully alive in its `finally` block (open JDBC, active bus VTs, bound HTTP port), then started a second harness on the same dbPath. The new abandon() contract releases OS-level resources without performing durability operations. Also lands `MinimalEventBusStub` to replace two per-test inner-class EventBus stubs.

**Files created (3 new):**
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/test/MinimalEventBusStub.java` — public class, all four abstract `EventBus` methods are no-ops (`subscribe`/`unsubscribe`/`notifyEvent`) or return `0` (`subscriberPosition`); `subscribers()` returns a constructor-injected snapshot list (default empty). Default methods retain their `UnsupportedOperationException` bodies. Two constructors: no-arg + `(List<SubscriberSnapshot>)`.
- `core/persistence/src/test/java/com/homesynapse/persistence/PersistenceFactoryAbandonTest.java` — 4 tests (abandon-releases-resources, close-after-abandon no-op, abandon-after-close no-op, double-abandon no-op).
- `core/event-bus/src/test/java/com/homesynapse/event/bus/InProcessEventBusAbandonTest.java` — 4 tests (abandon-closes-subscriber-runtimes, unsubscribe-after-abandon no-op, abandon-after-unsubscribe no-op, double-abandon no-op).

**Files modified (14):**
- `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` — `volatile boolean abandoned` field; `stop()` early-return on `|| abandoned`; new package-private `abandonWithoutCheckpoint()` that calls `databaseExecutor.shutdown()` directly (no WAL checkpoint).
- `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceFactory.java` — `volatile boolean abandoned` field; `close()` early-return; new public `abandon()` delegating to `lifecycle.abandonWithoutCheckpoint()`.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` — `volatile boolean abandoned` field; new public `abandon()` acquiring the existing `rwLock` write lock, iterating `activeRegistry.values()` calling `runtime.close()` on each, then `activeRegistry.clear()` + `passiveRegistry.clear()`. NOT added to the `EventBus` interface (concrete-only).
- `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` — `volatile boolean abandoned` field; `stop()` early-return on `|| abandoned`; new public `abandon()` with 4-step teardown (httpServer.stop → scheduler.shutdown → eventBus.abandon → persistenceFactory.abandon). `scheduler.shutdown()` already internally invokes `executor.shutdownNow()`, so the brief's preferred `scheduler.shutdownNow()` semantics are satisfied via the existing API (see deviation D-CL-3).
- `testing/integration-tests/src/test/java/com/homesynapse/it/HomeSynapseE2eHarness.java` — new `abandon()` delegating to `core.abandon()`.
- `testing/integration-tests/src/test/java/com/homesynapse/it/CrashRecoveryHttpIT.java` — empty-finally block replaced with `preCrash.abandon()` plus updated comment.
- `api/rest-api/src/test/java/com/homesynapse/api/rest/DlqStatusEndpointTest.java` — `StubBus` inner class deleted; all three sites use `MinimalEventBusStub`; unused `java.util.Objects` import removed; class Javadoc updated.
- `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/NotifyingEventPublisherTest.java` — `RecordingBus extends MinimalEventBusStub` (brief Option 1); removes the inline overrides of `subscribe`/`unsubscribe`/`subscriberPosition` since the base class provides them.
- `api/rest-api/build.gradle.kts` — added `testImplementation(testFixtures(project(":core:event-bus")))`.
- `lifecycle/lifecycle/build.gradle.kts` — added `testImplementation(testFixtures(project(":core:event-bus")))`.
- `core/persistence/MODULE_CONTEXT.md`, `core/event-bus/MODULE_CONTEXT.md`, `lifecycle/lifecycle/MODULE_CONTEXT.md`, `testing/integration-tests/MODULE_CONTEXT.md` — type-inventory rows updated for the new `abandon()` surfaces; new Gotchas added documenting (a) the production-grade vs. flag-based two-abandon-paths inconsistency in integration-tests, (b) the explicit decision to keep `abandon()` off the `EventBus` interface, (c) the `rateLimit.close()` omission rationale in `HomeSynapseCore.abandon()`, and (d) the `MinimalEventBusStub` testFixture entry.

**No new module dependencies** in production code. No `module-info.java` changes — both `api/rest-api` and `lifecycle/lifecycle` already declare `requires com.homesynapse.event.bus`, so `MinimalEventBusStub` resolves through the existing edge.

**Commands Nick must run:**
1. `./gradlew :core:persistence:check` — verifies the new `volatile boolean abandoned` field + `abandonWithoutCheckpoint()` method + `PersistenceFactoryAbandonTest`'s 4 tests, plus the existing `PersistenceFactoryTest` 4 tests still pass.
2. `./gradlew :core:event-bus:check` — verifies the new `InProcessEventBus.abandon()` method + `InProcessEventBusAbandonTest`'s 4 tests, plus `MinimalEventBusStub` in testFixtures compiles. The existing `EventBusContractTest` suite (44 methods) should be unaffected.
3. `./gradlew :api:rest-api:check` — verifies the new `testImplementation(testFixtures(project(":core:event-bus")))` dependency resolves, `DlqStatusEndpointTest`'s 3 tests still pass against `MinimalEventBusStub` (formerly `StubBus`), and no other tests broke.
4. `./gradlew :lifecycle:lifecycle:check` — verifies the same testFixtures dependency, `NotifyingEventPublisherTest`'s 4 tests still pass via `RecordingBus extends MinimalEventBusStub`, the new `HomeSynapseCore.abandon()` method compiles, and the existing `HomeSynapseCoreTest` suite is unaffected.
5. `./gradlew check` — full-project regression.
6. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — most importantly, `CrashRecoveryHttpIT` should now pass: the abandoned harness actively releases JDBC connections and HTTP socket, so the second harness can successfully bind the same dbPath and ephemeral port. If Recovery Step 2+3's `NotifyingEventPublisher` decorator is also in this layered tree, the other 6 M3.7 HTTP tests should also be GREEN.

**Deviations (none BLOCKING, none REVIEW):**
- **[INFO] D-CL-1** — `HomeSynapseCore.abandon()` uses `if (!started || abandoned)` rather than the brief's `if ((!started && !abandoned) || abandoned)`. Logically identical (verified by truth-table over the 4 input states); the simpler form matches the existing `SqlitePersistenceLifecycle.stop()` and the new `HomeSynapseCore.stop()` guard updated in the same change, keeping the four mutual-exclusion sites symmetric.
- **[INFO] D-CL-2** — `HomeSynapseCore.abandon()` does NOT call `rateLimit.close()`. `stop()` still does. `DerivedWriteRateLimit` is a `Semaphore`-backed token bucket with no OS-level resources (no executor, no file handles); skipping `close()` in the crash-simulation path leaks nothing observable; the JVM reclaims the Semaphore via GC. The brief's contract is OS-handle release, not in-memory cleanup. Documented as Gotcha #8 in `lifecycle/lifecycle/MODULE_CONTEXT.md`.
- **[INFO] D-CL-3** — `HomeSynapseCore.abandon()` uses `scheduler.shutdown()` instead of the brief's preferred `scheduler.shutdownNow()`. `SharedScheduler.shutdownNow()` does not exist as a public accessor, BUT `SharedScheduler.shutdown()` internally invokes `executor.shutdownNow()` on the underlying `ScheduledExecutorService` (SharedScheduler.java:138). The interrupt-running-tasks semantics the brief wanted are therefore already satisfied. The brief explicitly authorized this fallback ("if not, `shutdown()` is acceptable").
- **[INFO] D-CL-4** — `InProcessEventBusAbandonTest` constructs the bus via `(InProcessEventBus) InProcessEventBusFactory.create(...)` rather than reaching the package-private constructor directly. The cast compiles because `InProcessEventBus` is `public` (M3.6b, DEC-M3-16). The factory route is what the brief asked for; the cast is necessary because `abandon()` is not on the `EventBus` interface.
- **[INFO] D-CL-5** — `DlqStatusEndpointTest` removed `import java.util.Objects;` (was used only by the deleted `StubBus` constructor). Avoids a Spotless unused-import flag.

**STOP-on-Mismatch gates:** All PASS. `SqlitePersistenceLifecycle.stop()` was at the brief's expected lines 309–339 with the two-step pattern; `PersistenceFactory.close()` delegated to `lifecycle.stop()` at line 221; `InProcessEventBus.unsubscribe()` already used the write lock + `runtime.close()` pattern at lines 174–187; `HomeSynapseCore.stop()` had the documented 5-step teardown at lines 384–406; `DlqStatusEndpointTest`'s inner `StubBus` was at lines 110–141; `CrashRecoveryHttpIT`'s empty finally block was at lines 92–96. No file had diverged from the brief's expected state.

### RESOLVED — M3.7 Recovery Step 2+3: NotifyingEventPublisher + stale doc fixes (2026-05-26)
**Build gate:** RESOLVED 2026-05-27. `./gradlew check` GREEN (139 tasks).

**What this closes:** Finding 2 from the M3.7 Recovery Session — the publish/notify gap. The raw `persistenceFactory.eventPublisher()` persists events to SQLite but does NOT call `EventBus.notifyEvent()`. Without the decorator, `LiveModeAwaiter.awaitLive()` times out because subscribers (including the projection) are never woken after a publish, so `StateProjection.onEvent` is never called with new events, and the E2E tests that publish-then-query fail at Awaitility timeouts.

### RESOLVED — M3.7 Recovery Step 2+3: NotifyingEventPublisher + stale doc fixes (2026-05-26)
**Build gate:** RESOLVED 2026-05-27. `./gradlew check` GREEN (139 tasks).

**What this closes:** Finding 2 from the M3.7 Recovery Session — the publish/notify gap. The raw `persistenceFactory.eventPublisher()` persists events to SQLite but does NOT call `EventBus.notifyEvent()`. Without the decorator, `LiveModeAwaiter.awaitLive()` times out because subscribers (including the projection) are never woken after a publish, so `StateProjection.onEvent` is never called with new events, and the E2E tests that publish-then-query fail at Awaitility timeouts.

**Files created (2 new):**
- `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/NotifyingEventPublisher.java` — package-private final decorator; delegates `publish`/`publishRoot` to the raw publisher, then calls `bus.notifyEvent(envelope.globalPosition())` after successful persist; no notification on `SequenceConflictException` (preserves INV-ES-04).
- `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/NotifyingEventPublisherTest.java` — 4 unit tests (2 happy path, 2 conflict path) with hand-rolled test doubles (no Mockito).

**Files modified (4):**
- `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` — (B1) new `eventPublisher` field; (B2) step 5b constructs `NotifyingEventPublisher` decorator, step 6 passes `eventPublisher` (not raw) to `StateProjection.create()`; (B3) `eventPublisher()` accessor returns the field instead of `persistenceFactory.eventPublisher()`; (B4) stale comment in `mode()` updated to reflect fix round 4's setMode wiring; (B5) stale Javadoc in class header updated.
- `testing/integration-tests/src/test/java/com/homesynapse/it/HomeSynapseE2eHarness.java` — stale Javadoc on `mode()` updated.
- `testing/integration-tests/src/test/java/com/homesynapse/it/LiveModeAwaiter.java` — stale Javadoc updated.
- `lifecycle/lifecycle/MODULE_CONTEXT.md` — `NotifyingEventPublisher` added to type inventory; `HomeSynapseCore` row updated with step 5b and decorator wiring.

**No new module dependencies.** No build.gradle.kts changes. No module-info.java changes.

**Commands Nick must run:**
1. `./gradlew :lifecycle:lifecycle:check` — verifies `NotifyingEventPublisher` compiles (package-private, same package as `HomeSynapseCore`), the `NotifyingEventPublisherTest` 4 tests pass, and the existing 14 `HomeSynapseCoreTest` tests still pass.
2. `./gradlew check` — full-project regression. No other module is affected.
3. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — should now resolve all 7 M3.7 HTTP tests GREEN. The 3 publish-then-await tests gain a working notification path: `HomeSynapseE2eHarness.eventPublisher()` → `HomeSynapseCore.eventPublisher()` → `NotifyingEventPublisher` → persist + `bus.notifyEvent()` → subscriber woken → `StateProjection.onEvent` projects the event → entity query endpoints return the projected state.

**Deviations (none):**
No deviations from the coding instructions. All changes match the spec exactly.

**Additional stale references flagged (per brief's "Coder Pushback Welcome"):**
The grep for `StateProjection.currentMode()` delegation found 5 additional stale references beyond the 4 sites the brief specified. All are in MODULE_CONTEXT.md files or cross-module documentation (not production code or Javadoc), which are the PM's domain for WUCP Phase 2:
1. `testing/integration-tests/MODULE_CONTEXT.md:74` — says "delegates to `HomeSynapseCore.mode()` → `StateProjection.currentMode()`"
2. `core/state-store/StateQueryService.java:144` — comment says "delegates to `StateProjection.currentMode()`"
3. `core/state-store/MODULE_CONTEXT.md` — says "delegation to `StateProjection.currentMode()`"
4. `api/rest-api/ReadinessFilter.java:87` — comment references `StateProjection.currentMode()`
5. `lifecycle/lifecycle/MODULE_CONTEXT.md` (prior M3.7 entry) — now partially corrected by this WU's MODULE_CONTEXT update, but older prose in the `HomeSynapseCore` row still carries legacy phrasing

### RESOLVED — M3.7 Fix Round 4: Subscriber.setMode lifecycle hook + bus-side wiring (2026-05-23)
**Target commit:** delta over the M3.7 fix-round-3 working tree. No commit yet — rounds 1, 2, 3, and 4 are layered atop the 2026-05-22 M3.7 baseline.

**Diagnosis: H5 persists at the bus-↔-projection boundary.** Round 1 fixed `HomeSynapseCore.mode()` to read the bus's authoritative FSM (`eventBus.subscribers()`), which made the 4 no-publish M3.7 HTTP tests pass (empty-list, 404, admin DLQ, in-flight shutdown). But the 3 publish-then-await tests still failed because:
- The `Subscriber` interface had only `onEvent(EventEnvelope)` + `default onCaughtUp()`. **No `setMode` method existed in the contract.**
- The bus drove its own `SubscriberRuntime.mode` (AtomicReference) through `runtime.transitionTo(...)` / `runtime.compareAndTransition(...)`, but NEVER called back to the subscriber.
- `StateProjection.currentMode` stayed at its `COLD` initial value forever.
- `StateProjection.onEvent` short-circuits at `if (mode == SUSPENDED || mode == COLD) return;` (line 349-351) — so every LIVE delivery after publish was silently dropped.
- The 4/7-tests-passing split (no-publish PASS, publish-then-await FAIL) was the diagnostic key — only the publish path exercises `onEvent`, and only `onEvent` reads the projection's internal mode.

**Root cause:** Phase 2 `Subscriber` interface was missing the `setMode` lifecycle callback; the bus had no way to inform subscribers of mode transitions. This was a cross-module gap (event-bus side) that round 1's lifecycle-scoped fix could not address.

**Why round 1 was incomplete:** PM scoped round 1 to `lifecycle/lifecycle` only to avoid cross-module reach. That patched `HomeSynapseCore.mode()` (the `ReadinessSource` for HTTP gating) so empty-store paths reached LIVE-equivalent readiness, but did not propagate mode to the projection's `currentMode` field. The integration tests' publish path was the only suite that exercised the underlying defect — lifecycle-only tests on an empty store could not catch it.

**Fix applied (Phase 2A–2E from the round 4 brief):**
- **(A)** Added `default void setMode(SubscriberMode mode)` to `Subscriber` (no-op default). Documented threading constraint: called immediately after successful CAS, on the subscriber's VT, with the contract that implementations MUST be fast and non-blocking (one call site — `TransitionCoordinator` TRANSITION→LIVE — holds `ReplayWindowQueue.lock()`).
- **(B)** Wired `subscriber.setMode(newMode)` at every successful-CAS site in `ReplayDriver` (3 sites: COLD→REPLAY, REPLAY→TRANSITION, →SUSPENDED on read failure), `TransitionCoordinator` (2 sites: TRANSITION→LIVE under queue lock, →SUSPENDED on drain failure), and `SubscriberSupervisor` (3 sites: circuit-breaker, Error, checked Exception — all →SUSPENDED). The `ReplayDriver` COLD→REPLAY site was previously fire-and-forget (CAS return discarded); it now wraps the CAS in an `if` so `setMode` only fires on a successful transition.
- **(C)** Added `@Override` to `StateProjection.setMode(SubscriberMode)`. The pre-existing method body (Objects.requireNonNull + `currentMode.set(mode)`) is unchanged — this WAS the override; it just wasn't typed as one until now.
- **(D)** MODULE_CONTEXT.md updates:
  - `core/event-bus/MODULE_CONTEXT.md` — `Subscriber` interface row now lists 3 methods (1 abstract + 2 default) and documents the setMode threading constraint. New positive gotcha entry: "The bus invokes `subscriber.setMode(newMode)` immediately after each successful `runtime.mode` CAS …" with the documented exclusion of `bus.resume()` (Tracked Gap #2).
  - `core/state-store/MODULE_CONTEXT.md` — `StateProjection` row updated: `setMode` is now `@Override`, bus-invoked, NOT composition-root-wired. New gotcha entry documenting bus-driven setMode and the `resume()` gap.
- **(E)** Added one contract test method `EventBusContractTest.busInvokesSetModeAfterEachSuccessfulCas` in Tier 9. Verifies that after `subscribeRuntime` + `awaitMode(LIVE)` on an empty store, the subscriber's `setMode` was called with at least one non-COLD mode. Lives in the shared testFixtures suite — runs against both `InMemoryEventBusTest` (skipped via `assumeTrue(supportsActiveRuntime())`) and `InProcessEventBusTest` (executed).

**Excluded from this fix (per brief):**
- `InProcessEventBus.resume(String)` at line 342 (`runtime.transitionTo(REPLAY)`) — same site as the separately-tracked VT-respawn gap (PROJECT_SNAPSHOT.md Tracked Gap #2). Wiring `setMode` on a broken resume path is wasted work; it will land alongside the VT-respawn fix.
- `InMemoryEventBus` and any other `Subscriber` implementation — the new default = no-op preserves backward compatibility; nothing breaks.

**Files changed in fix round 4 (8 files):**
- `core/event-bus/src/main/java/com/homesynapse/event/bus/Subscriber.java` — `default setMode(SubscriberMode)` added with Javadoc.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayDriver.java` — 3 setMode call sites; COLD→REPLAY CAS wrapped in `if` so it only fires on success; REPLAY→TRANSITION CAS captures the boolean and conditionally fires before returning.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/TransitionCoordinator.java` — 2 setMode call sites (one under `queue.lock()`).
- `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberSupervisor.java` — 3 setMode call sites (all →SUSPENDED).
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/test/EventBusContractTest.java` — one new test method `busInvokesSetModeAfterEachSuccessfulCas` added to Tier 9 nested class.
- `core/state-store/src/main/java/com/homesynapse/state/StateProjection.java` — `@Override` annotation added to `setMode`; Javadoc updated to reflect bus-driven invocation.
- `core/event-bus/MODULE_CONTEXT.md` — Subscriber row updated; new gotcha entry.
- `core/state-store/MODULE_CONTEXT.md` — StateProjection row updated; new gotcha entry.
- `nexsys-hivemind/context/handoff/coder-handoff.md` — this entry.

**Unchanged from rounds 1–3:**
- Round 1's bus-FSM read in `HomeSynapseCore.mode()` stands. With proper `setMode` wiring, the projection's `currentMode` and the bus's `runtime.mode` are kept in sync — reading either is now equivalent. The bus FSM via `eventBus.subscribers()` remains the architecturally correct source (HomeSynapseCore implements `ReadinessSource`; readiness is a property of the bus's delivery state). D-FR1-1 `[REVIEW]` flag stays open for PM disposition in WUCP Phase 2 (likely converts from "band-aid" to "correct choice now that the cross-module fix is in place").
- Round 2's catalog pin (`awaitility = "4.3.0"`).
- Round 3's `DeploymentProfile.TESTING` Jetty pool sizing (2/8) and ASCII `@DisplayName` strings.

**Commands Nick must re-run:**
1. `./gradlew :core:event-bus:check` — verifies the `Subscriber` interface change compiles, the new `setMode` call sites in `ReplayDriver`/`TransitionCoordinator`/`SubscriberSupervisor` build, and the new contract test method `busInvokesSetModeAfterEachSuccessfulCas` passes against `InProcessEventBus`. Pre-existing supervisor tests (`SubscriberSupervisorTest`) unaffected — `setMode` only adds a callback; behavior of `transitionTo(SUSPENDED)` is unchanged.
2. `./gradlew :core:state-store:check` — verifies `StateProjection.setMode @Override` compiles against the new `Subscriber` interface default. No behavioral change to the method body.
3. `./gradlew :lifecycle:lifecycle:check` — should remain GREEN. Composition root no longer drives `setMode` (it never did); the H5-affected test `mode_returnsLiveAfterProjectionCompletesReplay` continues to pass via round 1's bus-FSM read.
4. `./gradlew check` — full-project regression. No other module touches `Subscriber.setMode` or the bus's mode-transition sites.
5. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — should now resolve all 7 M3.7 HTTP tests GREEN. The 3 publish-then-await tests (`CrashRecoveryHttpIT`, `EndpointE2eIT#listEntitiesReturnsEntitiesAfterStateReported`, `EndpointE2eIT#getEntityReturns200WithEntityState`) gain a working `onEvent` path: when LIVE events arrive, `StateProjection.currentMode == LIVE` (because the bus called `setMode(LIVE)` on the TRANSITION→LIVE CAS), so `onEvent` no longer short-circuits and projects the event into the materialized state.

**Deviations (none BLOCKING):**
- **[INFO] D-FR4-1** — Round 4 takes the explicit-wiring approach the brief specified (one `subscriber.setMode(newMode)` call after each successful CAS) rather than consolidating the call into `SubscriberRuntime.transitionTo` / `SubscriberRuntime.compareAndTransition`. The consolidated approach would be DRYer and prevent future CAS sites from forgetting the callback, but it would also automatically fire `setMode(REPLAY)` from `InProcessEventBus.resume()` — which the brief explicitly excludes (Tracked Gap #2, VT-respawn). The explicit-wiring approach preserves the resume-exclusion cleanly. If the PM later wants the DRY refactor after Tracked Gap #2 is closed, that's a separate WU.
- **[INFO] D-FR4-2** — Phase 1 verification flagged one minor brief inaccuracy: `StateProjection.processBatch(int)` DOES short-circuit on COLD/SUSPENDED (lines 460–463), contrary to the brief's hypothesis that it does not. The no-publish M3.7 tests pass anyway because the empty-store path goes through `ReplayDriver` page-replay (which reaches an empty tail and CASes REPLAY→TRANSITION without invoking the subscriber) rather than through `processBatch`. Same root cause as the brief described; slightly different code path. Documented here for PM awareness; no fix needed.
- **[INFO] D-FR4-3** — The `Subscriber.setMode` Javadoc says "Called on the subscriber's dedicated virtual thread" — this is true for `ReplayDriver` and `TransitionCoordinator` (both run on the per-subscriber VT) and for `SubscriberSupervisor.deliver()` (called from the same VT). Documented for future readers who might add a new transition site from a non-VT context — that would violate the contract.

### RESOLVED — M3.7 Fix Round 3: TESTING Jetty pool sizing + ASCII @DisplayName (2026-05-23)
**Target commit:** delta over the M3.7 fix-round-2 working tree. No commit yet — rounds 1, 2, and 3 are layered atop the 2026-05-22 M3.7 baseline.

**Two unrelated issues addressed:**

**Issue A — `DeploymentProfile.TESTING` Javalin pool was below Jetty's minimum.** All 7 M3.7 HTTP tests (`CrashRecoveryHttpIT`, `EndpointE2eIT`'s 5 methods, `InFlightRequestShutdownIT`) failed at `harness.start()` (Step 12 of `HomeSynapseCore.start()`) with `io.javalin.util.JavalinException` wrapping `java.lang.IllegalStateException`. The pre-existing M3.4a/M3.4b tests (`BurstLoadIT`, `HeapBudgetIT`, `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, `CrashRecoveryIT` — all using `IntegrationTestHarness`, which does NOT bind Javalin) continued to run. The M3.7 brief set `TESTING(... javalinMinThreads=1, javalinMaxThreads=2 ...)` to minimise Jetty footprint, but Jetty's `QueuedThreadPool.doStart()` requires `minThreads >= acceptors + selectors + 1`. On a multi-core dev host (`selectors = max(1, cores/2)`), 1/2 is below the floor. Fix: bump TESTING's pool to match HOME's known-good 2/8 sizing. SQLite-tier tunings (`cacheSizeKiB=2000`, `mmapSizeBytes=33_554_432`, `readThreadCount=1`) stay unchanged — they're independent of Javalin's pool.

**Caveat on Issue A diagnosis:** Gradle 8+ writes test reports in proprietary binary format (`testing/integration-tests/build/test-results/test/binary/output.bin`), and the JUnit XML/HTML reports were not generated for this run. The verbatim exception message could not be extracted from the binary. The diagnosis rests on indirect evidence: (a) all 7 M3.7 HTTP tests fail at `harness.start()`, (b) M3.4 non-Javalin tests work, (c) the `JavalinException` → `IllegalStateException` pair at server bind matches Jetty's textbook `QueuedThreadPool.doStart()` failure signature. The fix is also defensive — bumping to HOME's known-good 2/8 has no downside.

**Issue B — Unicode em-dash (U+2014) and right-arrow (U+2192) in `@DisplayName` strings render as mojibake on Windows console (CP-437).** Console output showed `M3.7 ΓÇö endpoint E2E` (em-dash) and `abandon ΓåÆ restart` (right-arrow). The JVM writes correct UTF-8 (Java 21 default per JEP 400); the Windows console misinterprets it. Cross-platform portable fix: replace Unicode punctuation in `@DisplayName` strings with ASCII equivalents (`—` → `--`, `→` → `->`). Comments and Javadoc untouched — those don't appear in console output and are valuable to human readers as-is.

**Files changed in fix round 3 (6 files):**
- `core/persistence/src/main/java/com/homesynapse/persistence/DeploymentProfile.java` — `TESTING` enum value: `javalinMinThreads` `1` → `2`; `javalinMaxThreads` `2` → `8`. Javadoc on the enum value updated to explain the M3.7 fix-round-3 background. STUDIO/HOME/PERFORMANCE unchanged.
- `core/persistence/MODULE_CONTEXT.md` — `DeploymentProfile` row updated: `TESTING(... 1, 2, 8)` instead of `(... 1, 1, 2)`, with the M3.7 fix-round-3 note.
- `testing/integration-tests/src/test/java/com/homesynapse/it/CrashRecoveryHttpIT.java` — 2 `@DisplayName` strings ASCII-fied (class-level em-dash + `entities survive abandon -> restart` arrow).
- `testing/integration-tests/src/test/java/com/homesynapse/it/EndpointE2eIT.java` — class-level `@DisplayName` em-dash → `--`.
- `testing/integration-tests/src/test/java/com/homesynapse/it/InFlightRequestShutdownIT.java` — class-level `@DisplayName` em-dash → `--`.
- `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreTest.java` — class-level `@DisplayName` em-dash → `--`.
- `nexsys-hivemind/context/handoff/coder-handoff.md` — this entry.

**Unchanged from previous rounds:**
- Round 1's H5 fix in `HomeSynapseCore.mode()` (reads bus FSM via `eventBus.subscribers()`).
- Round 2's catalog pin (`awaitility = "4.3.0"`).
- All Javadoc, comments, MODULE_CONTEXT.md prose outside the persistence module — Unicode characters preserved where they don't reach the Windows console.

**Optional environment note for Nick (not required):** Running `chcp 65001` in Git Bash (or PowerShell) switches the console to UTF-8 and allows the existing UTF-8 in source files (MODULE_CONTEXT files, Javadoc, log messages) to display correctly. Not required — this round's @DisplayName ASCII-fication makes the tests cross-platform without depending on console code page. The `chcp 65001` tip is useful for reading source via Git Bash tools (`cat`, `less`, `grep`).

**Commands Nick must re-run:**
1. `./gradlew :core:persistence:check` — verifies the `DeploymentProfile` enum change compiles (still 4 enum values × 8 fields; only TESTING's last two field values changed).
2. `./gradlew :lifecycle:lifecycle:check` — should remain GREEN (only a single `@DisplayName` ASCII tweak on the class). Confirms no regression from rounds 1+2.
3. `./gradlew check` — full-project regression check.
4. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — should now resolve to GREEN on all 7 M3.7 HTTP tests. Jetty's pool floor is cleared by the 2/8 bump; @DisplayName output reads cleanly on Windows console.

**Deviations (none BLOCKING):**
- **[REVIEW] D-FR3-1** — Issue A diagnosis could not be confirmed verbatim from build artifacts (Gradle 8+ binary format, no JUnit XML emitted by the test task). Diagnosis rests on the failure pattern (7 HTTP tests fail at harness.start, M3.4 non-Javalin tests work) + Jetty's known `QueuedThreadPool.doStart()` `minThreads >= acceptors + selectors + 1` requirement. The fix is defensive (HOME-equivalent pool sizing is known-good on Nick's hardware) — if the post-fix run still fails, the actual exception message will surface in the next round.
- **[INFO] D-FR3-2** — M3.4 pre-existing test files (`BurstLoadIT`, `CrashRecoveryIT`, `HeapBudgetIT`, `Pi4D1SpikeIT`, `Pi4SustainedLoadIT`) also contain Unicode em-dashes in their class-level `@DisplayName` strings. They were NOT touched in this round per the brief's narrower scope ("Grep all M3.7-created test files and HomeSynapseCoreTest"). Mojibake will continue to show for those tests' `@DisplayName` headers on the Windows console. A future hygiene WU can ASCII-fy them en masse; current cost is purely visual.
- **[INFO] D-FR3-3** — Unicode em-dashes remain in Javadoc, comments, and MODULE_CONTEXT.md prose throughout the codebase. These don't surface to the test console, so they were left as-is. `chcp 65001` (UTF-8 console code page) is the right Windows-side fix for human readers viewing source through Git Bash; the M3.7 fix-round-3 work explicitly does not address documentation/comments.

### RESOLVED — M3.7 Fix Round 2: awaitility 4.3.1 → 4.3.0 catalog correction (2026-05-23)
Round 2's catalog pin correction is unchanged and remains documented below for context. Round 3 layers atop rounds 1 and 2.

### OPEN (superseded by fix round 3 testing-only fixes) — M3.7 Fix Round 2: awaitility 4.3.1 → 4.3.0 catalog correction (2026-05-23)
**Target commit:** delta over the M3.7 fix-round-1 working tree (no commit yet — rounds 1 and 2 are layered atop the 2026-05-22 M3.7 baseline). Single-line catalog change.

**Failure that prompted the round:**
- `./gradlew :lifecycle:lifecycle:check` FAILED at `compileTestJava` with `Could not find org.awaitility:awaitility:4.3.1`. The version pin `awaitility = "4.3.1"` (set by the M3.7 brief and carried unchanged into fix-round-1's lifecycle test dep) does not exist on Maven Central. The same trust gap applied to `json-unit-assertj = "3.5.0"` but that resolution path was never hit because lifecycle's compile failed first.
- `:api:rest-api:check` and `:app:homesynapse-app:check` were GREEN — they do not consume the new catalog entries.

**Phase 1 verification against Maven Central** (`https://repo.maven.apache.org/maven2/...`):
- `org/awaitility/awaitility/` — highest stable is **`4.3.0`**. The `4.3.1` value the original brief listed was a fabrication; `4.2.2` is the latest 4.2 line; `4.3.0` is the next published stable.
- `net/javacrumbs/json-unit/json-unit-assertj/` — `3.5.0` **does exist**. Highest overall is `5.1.1`, but the M3.7 brief explicitly required *"newer maintenance releases that preserve the public API"* — a 3→5 major-version jump violates semantic versioning's API-stability promise, so `3.5.0` remains the correct pin per the brief's API-preservation guideline.
- Coordinates confirmed correct: `org.awaitility:awaitility` and `net.javacrumbs.json-unit:json-unit-assertj` match the Maven Central directory paths exactly. No coordinate corrections needed.

**Fix applied (single-line catalog edit):**
- `gradle/libs.versions.toml` — `awaitility = "4.3.1"` → `awaitility = "4.3.0"`. Nothing else changed in the catalog. The `[libraries]` entries (`awaitility = { module = "org.awaitility:awaitility", version.ref = "awaitility" }` and `json-unit-assertj = { module = "net.javacrumbs.json-unit:json-unit-assertj", version.ref = "json-unit-assertj" }`) are unchanged.

**Unchanged from previous rounds:**
- The H5 architectural fix in `HomeSynapseCore.mode()` (round 1) stands unchanged — this round is purely catalog hygiene.
- All test files, build.gradle.kts files, MODULE_CONTEXT files unchanged.

**Commands Nick must re-run:**
1. `./gradlew :lifecycle:lifecycle:check` — should now resolve `org.awaitility:awaitility:4.3.0` from Maven Central, compile the rewritten `mode_returnsLiveAfterProjectionCompletesReplay` test against Awaitility's API, and pass all 14 tests in the class (the H5-affected test + the 13 pre-existing ones).
2. `./gradlew check` (full project) — should be GREEN. All other modules already GREEN per Nick's round 1 results; the lifecycle dep resolution unblocks the only remaining failure.
3. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — also re-runnable now; `testing/integration-tests/build.gradle.kts` consumes the same `libs.awaitility` from the catalog, so the catalog correction propagates automatically. The M3.7 E2E tests' `LiveModeAwaiter.awaitLive(harness)` polls `harness.mode()` → `HomeSynapseCore.mode()`, which now reads the bus FSM (H5 fix from round 1) — the tests should reach LIVE on the empty event log without further changes.

**Deviations (none BLOCKING):**
- **[INFO] D-FR2-1** — `awaitility` pinned to `4.3.0` (the actual highest stable on Maven Central) rather than the brief's stated `4.3.1`. The brief's value was a fabrication; the correction is forced by reality. No API surface impact — `Awaitility.await().atMost(...).pollInterval(...).until(...)` is stable across the entire 4.x line.
- **[INFO] D-FR2-2** — `json-unit-assertj` left at `3.5.0` despite `5.1.1` being the actual latest. Rationale: M3.7 brief's "preserve the public API" guideline excludes major-version jumps; `3.5.0` exists; no problem to solve. If the PM wants to bump to 5.x as a follow-up, that's a separate WU with its own API-compat verification.

### RESOLVED — M3.7 Fix Round 1: HomeSynapseCore.mode() reads bus FSM (2026-05-23)
Round 1's H5 architectural fix is unchanged and remains documented below for context. Round 2 is purely a version-pin correction layered atop round 1.

### OPEN (superseded by fix round 2 catalog correction) — M3.7 Fix Round 1: HomeSynapseCore.mode() reads bus FSM (2026-05-23)
**Target commit:** delta over the M3.7 working tree (post-2026-05-22 baseline; no commit yet — fix is layered on top of the previous Coder output). Nick re-runs `./gradlew :lifecycle:lifecycle:check` and then `./gradlew check`.

**Failure that prompted the round:** `HomeSynapseCoreTest.mode_returnsLiveAfterProjectionCompletesReplay` failed with `expected: LIVE but was: COLD` after polling for 5.56 seconds. All 5 other modules' `:check` tasks passed green; only `:lifecycle:lifecycle:check` failed (1 of 14 tests).

**Diagnosis: H5 — projection's internal mode field is orphaned.**

- `StateProjection.currentMode()` reads `currentMode` (an `AtomicReference<SubscriberMode>` initialised to `COLD` at construction).
- The field's Javadoc (`StateProjection.java:80-83`) documents: *"The bus's lifecycle wiring is expected to call `setMode` on `COLD → REPLAY → TRANSITION → LIVE → SUSPENDED` transitions."*
- **The bus does NOT call `subscriber.setMode(...)` anywhere.** `grep "setMode|currentMode\.set" core/event-bus/src/main/java` returns zero hits. The bus drives `SubscriberRuntime.mode` (its own private AtomicReference, surfaced via `SubscriberSnapshot.mode()`), but the projection's own `currentMode` is never written by the bus.
- With an empty event log (the M3.7 fix-round-1 scenario), `onEvent` never fires; even if a sacrificial event were published, `StateProjection.onEvent` short-circuits at `mode == COLD || SUSPENDED` (`StateProjection.java:349-351`) and returns without advancing. So option (a) from the brief (publish a sacrificial event) cannot work.
- Option (b) — make `HomeSynapseCore.mode()` read the bus's authoritative FSM — is the only viable fix. It is also architecturally correct: `HomeSynapseCore implements ReadinessSource`, and readiness is a property of the bus's delivery FSM, not the projection's internal state.

**Fix applied (option b):** `HomeSynapseCore.mode()` now reads `eventBus.subscribers()`, finds the projection subscriber by ID, and returns its `SubscriberSnapshot.mode()`. Falls back to `COLD` if the projection is not present (defensive). The test was rewritten to use Awaitility (per D-04 / NO_DIRECT_TIME_ACCESS — `System.nanoTime()` removed); the `lifecycle/lifecycle/build.gradle.kts` got `testImplementation(libs.awaitility)` added.

**Files changed in fix round 1:**
- `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` — `mode()` body replaced; Javadoc comment explains the architectural rationale and points at the cross-module symmetry fix (see deviation D-FR1-1).
- `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreTest.java` — `mode_returnsLiveAfterProjectionCompletesReplay` rewritten to use `Awaitility.await().atMost(5s).pollInterval(50ms)` instead of the pre-fix `System.nanoTime()` + `Thread.sleep(50)` loop. Awaitility import added.
- `lifecycle/lifecycle/build.gradle.kts` — `testImplementation(libs.awaitility)` added.
- `lifecycle/lifecycle/MODULE_CONTEXT.md` — `HomeSynapseCore` row updated with the M3.7 fix round 1 note (`mode()` reads bus FSM; `StateProjection.currentMode` is documented as orphaned).
- `nexsys-hivemind/context/handoff/coder-handoff.md` — this entry.

**Commands Nick must re-run after the fix:**
1. `./gradlew :lifecycle:lifecycle:check` — verifies the rewritten test compiles against the new Awaitility dep, the `HomeSynapseCore.mode()` rewrite compiles, and all 14 tests in the class pass (the previously-failing one and the 13 others that were green).
2. `./gradlew check` — confirms no cross-module regression. The fix is scoped to `lifecycle/lifecycle` only.
3. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — runs the M3.7 E2E tests. `HomeSynapseE2eHarness.mode()` delegates to `HomeSynapseCore.mode()`, so `LiveModeAwaiter.awaitLive(harness)` benefits from the fix automatically (the integration tests should now reach LIVE on empty stores).

**Deviations (none BLOCKING):**
- **[REVIEW] D-FR1-1** — `HomeSynapseCore.mode()` now reads the bus's per-subscriber `SubscriberSnapshot.mode()` instead of `StateProjection.currentMode()`. This materially changes the semantics of the `ReadinessSource` contract: the "ready" signal now reflects the bus's delivery FSM (driven by `ReplayDriver` + `TransitionCoordinator`), not the projection's view of its own mode. The PM should update MODULE_CONTEXT documentation for `ReadinessSource` if it asserts otherwise, AND should consider an eventual cross-module fix that has the bus call `subscriber.setMode(newMode)` on each FSM transition to restore symmetry — but that work is OUT OF SCOPE for M3.7 (it would touch `core/event-bus`).
- **[INFO] D-FR1-2** — Added `testImplementation(libs.awaitility)` to `lifecycle/lifecycle/build.gradle.kts`. Same dep that M3.7 added to `testing/integration-tests`; uses the already-pinned `awaitility = "4.3.1"` from `gradle/libs.versions.toml`. Comment notes the M3.7 fix round 1 origin.
- **[INFO] D-FR1-3** — Did not touch any other test in `HomeSynapseCoreTest.java`. The other 13 tests continue to use `Clock.systemUTC()` constructor arguments (existing pattern, pre-M3.7 — the rule about Clock applies to direct time-API calls, not Clock arguments to harness construction). Only the failing test was rewritten.

### RESOLVED — M3.7 E2E Integration Tests (2026-05-22)
The original M3.7 entry remains documented below for context; the rest of the build gate (the other 5 module checks) was GREEN per Nick's run on 2026-05-22.

### OPEN (superseded by fix round 1) — M3.7 E2E Integration Tests (2026-05-22)
**Target commit:** delta over `76288af` (M3.6e.2 baseline). The Coder produced files only; Nick runs `./gradlew check` and reports.

The change spans approximately 17 files: 5 new test files (`HomeSynapseE2eHarness`, `LiveModeAwaiter`, `TestEvents`, `EndpointE2eIT`, `CrashRecoveryHttpIT`, `InFlightRequestShutdownIT` — 6 new files actually), 1 new production file (`MinimalProjectionAdvancer`), and modifications to: `gradle/libs.versions.toml` (awaitility + json-unit-assertj pins), `testing/integration-tests/build.gradle.kts` (4 new test deps), `core/persistence/DeploymentProfile.java` (4th TESTING enum value), `lifecycle/lifecycle/HomeSynapseConfig.java` (2→3 fields + `testing()` factory), `lifecycle/lifecycle/HomeSynapseCore.java` (NO_OP placeholders replaced; `boundHttpPort()` accessor; `config.httpPort()` instead of hardcoded `HTTP_PORT`), `core/event-bus/SubscriberDlq.java` (Clock injection + parkedAt + oldestParkedAt accessor; DlqEntry 6→7 fields; legacy no-arg constructor removed), `core/event-bus/SubscriberSnapshot.java` (5→6 fields), `core/event-bus/InProcessEventBus.java` (passes clock to SubscriberDlq + populates new snapshot field), `core/event-bus/TransitionCoordinator.java` (synthetic DlqEntry now passes parkedAt), `core/event-bus/test/SubscriberSupervisorTest.java` (7 SubscriberDlq constructor calls updated to 3-arg), `api/rest-api/DlqStatusEndpoint.java` (response shape adds oldestParkedAt), `api/rest-api/test/DlqStatusEndpointTest.java` (3 SubscriberSnapshot constructions updated to 6-arg), `lifecycle/lifecycle/test/HomeSynapseCoreTest.java` (3 new tests), plus MODULE_CONTEXT.md updates in `lifecycle/lifecycle`, `core/persistence`, `core/event-bus`, `api/rest-api`, `testing/integration-tests`.

**Commands Nick must run against the working tree:**
1. `./gradlew :core:persistence:check` — verifies the new `DeploymentProfile.TESTING` enum value compiles (4 enum values × 8 fields).
2. `./gradlew :core:event-bus:check` — verifies the `SubscriberDlq` 3-arg constructor, the new `parkedAt` field on `DlqEntry`, the `oldestParkedAt()` accessor, the 6-field `SubscriberSnapshot` record, `InProcessEventBus.subscribeRuntime` passing `clock`, and `TransitionCoordinator.park(...)` passing the new `parkedAt` arg. The updated `SubscriberSupervisorTest` should compile and pass (7 SubscriberDlq construction sites updated to pass FIXED_CLOCK).
3. `./gradlew :api:rest-api:check` — verifies `DlqStatusEndpoint` builds the 5-key response Map and that `DlqStatusEndpointTest` compiles against the 6-arg `SubscriberSnapshot` and verifies the new `oldestParkedAt` Map entry.
4. `./gradlew :lifecycle:lifecycle:check` — verifies the renamed `MINIMAL_DERIVATION_RULE` constant + the new `MinimalProjectionAdvancer` package-private class + the new 3-field `HomeSynapseConfig` (with `testing()` factory) + `boundHttpPort()` accessor + the renamed bound-port log message + the new 3 `HomeSynapseCoreTest` methods (`mode_returnsLiveAfterProjectionCompletesReplay`, `boundHttpPort_returnsPositiveNonZeroAfterStart`, `boundHttpPort_throwsBeforeStart`). The bootstrap step count remains 16 (no new steps; step 5/6 contents updated and step 12 port reference changed).
5. `./gradlew :app:homesynapse-app:check` — runs the 9 ArchUnit rules against the full classpath. The new `MinimalProjectionAdvancer` uses the injected `EventStore`; no `Instant.now()` / `System.currentTimeMillis()` calls are introduced anywhere in the diff. The new production code in `lifecycle` and `core/event-bus` does not access filesystem directly. No new internal-package access.
6. `./gradlew check` (full project) — catches any cross-module fallout. The change is mostly additive but the `SubscriberSnapshot` 5→6 field change and `SubscriberDlq` constructor signature change DO break compilation against any out-of-tree consumer that hasn't been updated. Inside the tree, all known call sites have been updated (`InProcessEventBus.buildSnapshot`, `DlqStatusEndpoint`, the two test files).
7. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — runs the existing M3.4a/M3.4b integration tests AND the new M3.7 E2E tests. The new tests bind to ephemeral HTTP ports (port 0); parallel execution is safe. The new tests use `Clock.fixed(...)` per DEC-M3-09. If JUnit's test runner uses platform threads by default (it does as of 5.10+), `HomeSynapseE2eHarness.start()` satisfies the platform-thread JacksonWarmup constraint (LTD-19 / DECIDE-M2-05).

**Risk profile:** Medium-high. Largest risks:
- (a) `SubscriberSnapshot` 5→6 field change ripples through anywhere the record is constructed. In-tree audit: `InProcessEventBus.buildSnapshot` (updated), `DlqStatusEndpointTest` (updated). The contract-test framework (`EventBusContractTest`) only reads accessors — no construction calls.
- (b) `SubscriberDlq` 2-arg → 3-arg constructor change. In-tree audit: `InProcessEventBus.subscribeRuntime` (updated), `SubscriberSupervisorTest` (7 sites updated via replace_all). Legacy no-arg `SubscriberDlq()` constructor deleted as unused.
- (c) `DlqEntry` 6→7 field record extension. In-tree audit: `SubscriberDlq.park(DeadLetter)` (updated to pass clock.instant()), `TransitionCoordinator` (updated to pass `now` as the 7th arg).
- (d) Javalin `app.port()` API call. Verified against `javalin-6.7.0.jar`'s bytecode — `public int port()` exists. Returns the bound port even for `start(0)` ephemeral binds (standard Jetty behavior).
- (e) The new integration-tests module deps (`lifecycle`, `rest-api`) introduce transitive Jackson + Javalin + Jetty onto the test classpath. Should compile cleanly because the integration-tests module already pulls those transitively through `core:state-store` and `core:event-bus`.

**Deviations (none BLOCKING):**
- **[REVIEW] D-A** — `HomeSynapseCore.javalinApp` field is actually named `httpServer`, not `javalinApp` as the brief expected. The existing M3.6e.1 naming was preserved; the brief's references were treated as conceptual. Documented in the source file and Module Context.
- **[REVIEW] D-B** — `SubscriberDlq.DlqEntry` was already a 6-field record (not 4 as the brief stated). M3.7 adds `parkedAt` as the 7th field. Behaviorally identical to the brief's intent.
- **[INFO] D-C** — `boundHttpPort()` was added to `HomeSynapseCore` rather than `DeploymentProfile` (the brief's literal text). The brief's "Settled Decisions" REC-15 line explicitly reinterprets the placement; this implementation follows the reinterpreted form.
- **[INFO] D-D** — The legacy no-arg `SubscriberDlq()` constructor was DELETED as unused, rather than updated to take Clock. CLAUDE.md authorises deletion of unused code over backwards-compat shims.
- **[INFO] D-E** — Single existing TestEvents draft factory (`stateReported`, `availabilityChanged`) — the brief listed 4 example factories including `entityRegistered` and `stateChanged`. `EntityRegisteredEvent` does not exist in the event-model module (entities arrive via `device_adopted` payloads); `StateChangedEvent` requires `EventId triggeredBy` which is a derived-event signature, awkward for ad-hoc test creation. The two factories cover the M3.7 E2E test surface.
- **[INFO] D-F** — `EndpointE2eIT.getDlqStatusReturnsSubscribersListWithOldestParkedAtField` asserts the empty-DLQ shape only (the brief allowed this as the alternative to causing a real DLQ park, which requires deliberate event corruption). The non-empty case is a future enhancement.
- **[INFO] D-G** — The existing `testing/integration-tests/build.gradle.kts` gates `tasks.test` on `project.hasProperty("piProfile")`. The new M3.7 tests inherit this gating — Nick must pass `-PpiProfile=throttled` to run them. The gating was preserved as-is; loosening it is out of scope.
- **[INFO] D-H** — The unused import `com.homesynapse.state.AdvanceResult` and `com.homesynapse.state.ProjectionAdvancer` were removed from `HomeSynapseCore.java` after the NO_OP_ADVANCER lambda was deleted. The `MinimalProjectionAdvancer` field uses the concrete type, not the interface, so the interface import is no longer needed at the call site.

**STOP-gate results (G1–G11):** All PASS with two minor brief discrepancies noted:
- G1 PASS — HomeSynapseCore has 16 steps, `NO_OP_DERIVATION`/`NO_OP_ADVANCER` constants present at expected lines, `HTTP_PORT=7070` at line 138, `httpServer` field exists (named `httpServer`, not `javalinApp` as brief stated — see D-A).
- G2 PASS — RestFilters has 3 documented methods.
- G3 PASS — DeploymentProfile has 3 enum values × 8 fields pre-M3.7 (4 values after this WU).
- G4 PASS — EventBus has 8 methods; SubscriberSnapshot has 5 fields (6 after this WU); no `isLive()` method.
- G5 PASS — `StateQueryService.materialized(StateStore, ReadinessSource, LongSupplier, Clock)` factory exists.
- G6 PASS — `ProjectionAdvancer.advance(long, int, Consumer<EventEnvelope>) → AdvanceResult`; `DEFAULT_MAX_ROWS = 500`.
- G7 PASS — `AdvanceResult` is a 3-field record.
- G8 PASS — `EventStore.readFrom(long, int) → EventPage`; `EventPage` is a 3-field record (events, nextPosition, hasMore).
- G9 PASS — `libs.versions.toml` has neither `awaitility` nor `json-unit-assertj` pinned (added by this WU).
- G10 PASS — `SubscriberDlq` has no-arg + 2-arg constructors; `DlqEntry` has 6 fields (not 4 as brief stated — see D-B).
- G11 PASS — `HomeSynapseConfig` is a 2-field record with `HOME_DEFAULT` (3 fields after this WU).

### RESOLVED — M3.6e.2 Admin Endpoints + ArchUnit Rules (2026-05-22)
**Commit:** `76288af`. **Build:** GREEN. Full `./gradlew check` confirmed by Nick.

### RESOLVED — M3.6e.2 Admin Endpoints + ArchUnit Rules (2026-05-22)
**Commit:** `76288af`. **Build:** GREEN. Full `./gradlew check` confirmed by Nick.

The change spans 16 files: 8 new production files (`EndpointContext.java`, `JavalinEndpointContext.java`, `EndpointResponses.java`, `ListEntitiesEndpoint.java`, `GetEntityEndpoint.java`, `GetEntityStateEndpoint.java`, `DlqStatusEndpoint.java`, `ProjectionStatusEndpoint.java`), 1 modified production file (`RestFilters.java` — 2 new public methods), 1 modified composition root (`HomeSynapseCore.java` — 14-step → 16-step bootstrap), 1 modified ArchUnit rules file (`HomeSynapseArchRules.java` — 2 new rules), 1 modified ArchUnit test (`HomeSynapseArchRulesTest.java` — 2 new `@ArchTest` fields), 2 new test helpers (`RecordingEndpointContext.java`, `FakeStateQueryService.java`), 5 new test classes (`ListEntitiesEndpointTest`, `GetEntityEndpointTest`, `GetEntityStateEndpointTest`, `DlqStatusEndpointTest`, `ProjectionStatusEndpointTest`), plus MODULE_CONTEXT.md updates in `api/rest-api` and `lifecycle/lifecycle`.

**Commands Nick must run against the working tree:**
1. `./gradlew :api:rest-api:check` — verifies the 8 new package-private classes compile cleanly against the existing `requires com.homesynapse.state` + `requires com.homesynapse.event.bus` + `requires io.javalin` module-info edges (no module-info changes needed). Confirms the 5 new test classes (~18 test methods) pass against `RecordingEndpointContext` and `FakeStateQueryService`.
2. `./gradlew :lifecycle:lifecycle:check` — verifies `HomeSynapseCore.start()`'s expanded 16-step bootstrap compiles with the two new `RestFilters` gateway calls and the new bootstrap-sequence Javadoc bullets.
3. `./gradlew :app:homesynapse-app:check` — verifies the two new ArchUnit rules (`QUERY_SERVICE_READ_ONLY`, `REST_ENDPOINTS_NO_EVENT_PUBLISHING`) evaluate without violations against the production codebase. `REST_ENDPOINTS_NO_EVENT_PUBLISHING` references `com.homesynapse.event.EventPublisher.class` — the app module already depends on event-model.
4. `./gradlew check` (full project) — catches any cross-module fallout (none expected) and verifies that the existing `NO_DIRECT_TIME_ACCESS` ArchUnit rule still holds (the new handlers use the injected `Clock` for response timestamps; the test classes use `Clock.fixed(...)`).
5. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies the M3.4a/M3.4b/M3.6e.1 integration tests still pass; the new route registrations do not change the existing readiness-gate behaviour.

**Risk profile:** Low. The change is purely additive: new package-private classes, 2 new public methods on an existing utility class, 2 new bootstrap steps that fit cleanly between existing steps 12 and (renumbered) 15, and 2 new ArchUnit rules. No existing tests are modified. The single edge risk is the ArchUnit rule syntax (`belongToAnyOf(EventPublisher.class)`) — the brief explicitly invited adjustment if needed; the chosen form mirrors the existing `NO_SERVICE_LOADER` rule and should compile cleanly.

**Deviations (none BLOCKING):**
- **[REVIEW] D-1** — `ListEntitiesEndpoint` summary fields omit `subjectType` because `EntityState` has no such field. The brief's PLAN-M3 §10.6 sketch included it; the actual record carries `entityId`, `attributes`, `availability`, `stateVersion`, three timestamps, `staleAfter`, `stale`. Documented in the handler's Javadoc.
- **[REVIEW] D-2** — `DlqStatusEndpoint` response shape uses `dlqDepth` and `crashCount` (the fields actually on `SubscriberSnapshot`) instead of the brief's example `parkedCount` and `oldestParkedAt`. The brief's "Coder Pushback Welcome" section explicitly invited this adjustment.
- **[REVIEW] D-3** — `REST_ENDPOINTS_NO_EVENT_PUBLISHING` uses `accessClassesThat().belongToAnyOf(EventPublisher.class)` instead of the brief's `callMethodWhere(target(name("publish"))...)` form. The chosen form mirrors the existing `NO_SERVICE_LOADER` rule and achieves the same intent (REST cannot publish events) — `EventPublisher` has only publish-related methods, so any class access implies publish intent. The brief explicitly invited this adjustment.
- **[INFO] D-4** — Both `LongSupplier viewPositionSupplier` arguments at the `RestFilters.installAdminEndpoints` call site are wired to `stateProjection::cursorPosition` (the same source the M3.6e.1 `MaterializedStateQueryService` uses). Consistent with the composition-root pattern; the `ProjectionStatusEndpoint`'s `viewPosition` field will track the projection cursor.
- **[INFO] D-5** — Added one extra "sortDescReversesOrder" test to `ListEntitiesEndpointTest` (6 tests total instead of the brief's 5) to cover the case-insensitive DESC path. Net effect: 19 new test methods total across 5 test classes (close to the brief's ~20 target).

### Next Work Unit

**Next: M4.0 — first M4 milestone** (scoping TBD by the PM). M3.7 is the M3 capstone — with this WU committed and GREEN, the M3 implementation milestone is complete. The composition root is fully wired with HTTP query/admin endpoints, ephemeral-port test execution, a real bounded-window projection advancer, DLQ `oldestParkedAt` observability, and (as of the 2026-05-27 closeout) a production-grade `abandon()` ungraceful-shutdown contract spanning persistence → bus → composition root → E2E harness, plus the `MinimalEventBusStub` testFixture consolidation of EventBus inner-class stubs.

M3.7 closure of pre-M3.7 prerequisites:
- **OR-M3-17** (`NO_OP_DERIVATION` placeholder) — RESOLVED. Renamed `MINIMAL_DERIVATION_RULE = context -> List.of()`; the empty-derivation path is the M3.7 closure (full derivation lands at M4.0 with `DispatchingProjectionAdvancer` per Research 8 REC-28).
- **OR-M3-18** (`NO_OP_ADVANCER` placeholder) — RESOLVED. New `MinimalProjectionAdvancer` package-private class implements `ProjectionAdvancer` against the live `EventStore` via bounded-window `readFrom` (≤500 rows).
- **End-to-end HTTP integration test** — RESOLVED. New `EndpointE2eIT`, `CrashRecoveryHttpIT`, `InFlightRequestShutdownIT` in `testing/integration-tests`.
- **DLQ `oldestParkedAt` field** — RESOLVED. `SubscriberDlq` now takes `Clock` and exposes `oldestParkedAt()`; `SubscriberSnapshot` extended 5→6 fields; `DlqStatusEndpoint` response now includes the field.

PM follow-up: scope M4.0 (likely starting with `DispatchingProjectionAdvancer` per Research 8 REC-28 and the M4 amendment-deliberation window from Research 4 v3 / Research 6 NQs / Research 5 REC-56).

### Resolved at commit

### M3.6e.1 + XLINT_EXPORTS_FIX — MaterializedStateQueryService + REST Readiness Gate (2026-05-22)

### M3.6e.1 + XLINT_EXPORTS_FIX — MaterializedStateQueryService + REST Readiness Gate (2026-05-22)
**Commit:** `b71ed37`. **Build:** GREEN. Full `./gradlew check` PASS (139 tasks, 0 failures). Confirmed by Nick. Initial M3.6e.1 commit failed `./gradlew check` with `-Xlint:exports` errors on `ReadinessFilter` (Javalin types leaked through a non-transitive `requires`). PM issued a follow-up fix brief (`M3.6e.1_XLINT_EXPORTS_FIX.md`) on the same day; the fix is applied in the same working tree as the original WU. Second fix round corrected Gradle/JPMS scope alignment (`implementation` → `api` for state-store in rest-api). Both fix rounds resolved before GREEN.

**Fix delta (2026-05-22):**
- `ReadinessFilter.java` — class declaration `public final class` → `final class` (now package-private). No other changes.
- `RestFilters.java` (NEW) — public final utility class. Single method `static void installReadinessGate(Object javalinApp, ReadinessSource readinessSource)`. The `Object` typing of `javalinApp` deliberately avoids exposing `io.javalin.Javalin` in the public API surface of a module that requires Javalin non-transitively.
- `HomeSynapseCore.java` — import `ReadinessFilter` → `RestFilters`; constructor call `new ReadinessFilter(this)` → `RestFilters.installReadinessGate(app, this)`; Javadoc `{@link ReadinessFilter}` → `{@link RestFilters#installReadinessGate}`.
- `api/rest-api/src/main/java/module-info.java` — module Javadoc updated to point at `RestFilters.installReadinessGate` instead of `ReadinessFilter`. No `requires`/`exports` changes.
- `api/rest-api/MODULE_CONTEXT.md` — added `RestFilters` to the type inventory (public final utility), updated `ReadinessFilter` row to mark it package-private, expanded the M3.6e.1 Phase 3 Note with the DEC-M3-16 rationale for why `requires transitive io.javalin` is the wrong fix (would chain Javalin into websocket-api → homesynapse-app).

The change spans 13 modified/created files across `core/state-store`, `api/rest-api`, `core/persistence`, `lifecycle/lifecycle`, plus MODULE_CONTEXT.md updates across 4 modules.

**Commands Nick must run against the working tree:**
1. `./gradlew :core:persistence:check` — verifies the two new `DeploymentProfile` accessors (`javalinMinThreads()`, `javalinMaxThreads()`) compile and the new `DeploymentProfileTest` (4 tests, all 3 profiles + min ≤ max invariant + HOME defaults regression guard) passes.
2. `./gradlew :core:state-store:check` — verifies the new package-private `MaterializedStateQueryService` compiles, the new public static factory `StateQueryService.materialized(...)` resolves through the imports (`java.time.Clock`, `java.util.function.LongSupplier`), and the new `MaterializedStateQueryServiceTest` (10 tests including 4 staleness-recomputation, 3 snapshot variants, 1 unmodifiable-map, 1 view-position, 1 isReady-delegation across 5 modes) passes. The InMemoryStateStore testFixture is consumed for the backing store; ReadinessSource is stubbed via `AtomicReference<SubscriberMode>` lambdas.
3. `./gradlew :api:rest-api:check` — verifies the new `ReadinessFilter` (public final class implementing `io.javalin.http.Handler`) compiles against the new `requires com.homesynapse.state`, `requires com.homesynapse.event.bus`, `requires io.javalin`, `requires org.slf4j` module-info edges, and that the new `ReadinessFilterTest` (8 tests: 1 LIVE pass-through, 3 non-LIVE 503 with diagnostic headers, 1 RFC 9457 problem detail body shape, 1 mode-freshness assertion, plus the nested classes for LIVE/non-LIVE/fresh-read) passes. **CHECK Javalin's JPMS module name** — if `requires io.javalin;` fails to resolve, the actual module name may differ (Javalin is Kotlin-based and may use a different automatic-module-name convention).
4. `./gradlew :lifecycle:lifecycle:check` — verifies the `HomeSynapseCore.start()` 14-step bootstrap compiles with the new `MaterializedStateQueryService` wiring (step 11) + the Javalin server bootstrap (step 12), the `HomeSynapseCoreTest.stateQueryServiceReturnsMaterializedAfterM3_6e_1` test passes, and the new module-info edges resolve (`requires com.homesynapse.api.rest`, `requires io.javalin`, `requires org.eclipse.jetty.util`). **CHECK Jetty's module name** — `org.eclipse.jetty.util` is the expected Jetty 12 module name carrying `QueuedThreadPool`; if it resolves to a different module under Javalin 6.7.0's Jetty dependency, adjust accordingly.
5. `./gradlew check` (full project) — catches any consumer of the old `ThrowingStateQueryService`-based `stateQueryService()` accessor (no production callers expected) and verifies no ArchUnit regressions (`NO_DIRECT_TIME_ACCESS` is satisfied — `MaterializedStateQueryService` uses the injected `Clock`; tests use `Clock.fixed(...)` from `java.time`).
6. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies the M3.4a/M3.4b integration tests still pass on `HomeSynapseConfig.HOME_DEFAULT`. The new HTTP server binding port 7070 should NOT affect integration tests (which use `HomeSynapseCore` directly without HTTP).

**Risk profile:** Medium. Two new-edge risks: (a) the Javalin JPMS module name `io.javalin` is the conventional Kotlin-library name but could resolve differently — the brief explicitly flagged this as a watch-out. (b) Port 7070 binding in `HomeSynapseCoreTest` — each test in `HomeSynapseCoreTest` starts the core sequentially with `@AfterEach core.stop()` releasing the port. Jetty's default `SO_REUSEADDR=true` should handle `TIME_WAIT` between tests. If CI runs the test class in parallel with another test that also binds 7070, flakes possible — none such exist today. The hardcoded port is per PLAN-M3 §10 ("Port 7070 hardcoded for MVP").

**Deviations (full report below — none BLOCKING):**
- **[REVIEW] D-1** — `MaterializedStateQueryService` constructor takes 4 params (added `LongSupplier viewPosition`), not the brief's 3 params. STOP-on-Mismatch gate G5 found `StateStore` does not have a `getViewPosition()` method (the brief acknowledged this with "or equivalents"). The view position is sourced via the supplier from `StateProjection.cursorPosition()`. This keeps `StateStore` a pure key-value port and the query service decoupled from `StateProjection` (DEC-M3-16). Public static factory `StateQueryService.materialized(...)` exposes the construction surface.
- **[REVIEW] D-2** — `ReadinessFilter` exposes a package-private `Responder` SPI and a pure `apply(Responder)` decision method for unit testing instead of mocking Javalin's thick `Context` interface (the brief invited this pushback under "Coder Pushback Welcome").
- **[INFO] D-3 through D-7** — see Completion Report.

### Resolved at commit

### M3.6d-b — PersistenceFactory + HomeSynapseCore Composition-Root Wiring (2026-05-21)
**Commit:** `dfb045e` (4-commit cohort: `a33ee40`, `a59b64e`, `725353d`, `dfb045e`). **Build:** GREEN at HEAD. Confirmed by Nick.

Shipped as 4 commits: (1) `WriteCoordinator.queueSize()` accessor (`a33ee40`), (2) production `SqliteSubscriberReadConnectionFactory` + `SqliteSubscriberReadExecutor` (`a59b64e`), (3) `PersistenceFactory` public gateway + `SqlitePersistenceLifecycle` 6-store expansion (`725353d`), (4) `HomeSynapseCore` composition root implementing `ReadinessSource` (`dfb045e`). 20 files changed, +1,432 insertions, -14 deletions. All three OR-M3-14 prerequisite infrastructure gaps resolved. No deviations from the revised M3.6d-b coding instruction.

### M3.6d-a — Composition-Root Satellite Changes (2026-05-20)
**Commit:** `25bc23b`. **Build:** GREEN at HEAD (full `./gradlew check` PASS, 137 actionable tasks). Resolved 2026-05-20 after SLF4J follow-up fix.

**Follow-up patch (2026-05-20, same session):** Nick's first `./gradlew check` failed with `package org.slf4j does not exist` at `SharedScheduler.java:18–19`. Root cause: the lifecycle module-info added during M3.6d-a did NOT declare `requires org.slf4j`, and SLF4J was not transitively available because persistence/state-store both declare it at `implementation` scope (not propagated to consumers). Fix: added `requires org.slf4j;` (non-transitive, matching the persistence/state-store pattern) to `lifecycle/lifecycle/src/main/java/module-info.java` plus `implementation(libs.slf4j.api)` to `lifecycle/lifecycle/build.gradle.kts`. `lifecycle/lifecycle/MODULE_CONTEXT.md` updated to document both. No code changes to `SharedScheduler.java` — the SLF4J usage is correct, only the dependency declaration was missing. This pattern is exactly the trap documented in coder-lessons.md M3.4b entry #4 ("SLF4J transitivity under `implementation` scope") — the lifecycle module needed the same explicit declaration that state-store and persistence both have.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md. The change spans 4 modified production files (+1 doc-only Javadoc edit), 1 new public interface, 1 new public record, 2 new package-private classes, 2 new test files, 2 modified test files, 1 modified module-info (+1 follow-up edit), 1 modified build.gradle.kts (+1 follow-up edit), and MODULE_CONTEXT updates across 4 modules (+1 follow-up edit).

**Commands Nick must run against the working tree:**
1. `./gradlew :core:persistence:check` — verifies `SqliteStateStore` now compiles with `implements StateCheckpointSource`, the renamed `serializeCheckpoint(int)` method (3 callsites updated in `SqliteStateStoreTest`), and the promoted-to-public `loadedProjectionVersion()`. `StateCheckpointSource` is already in scope via the existing `requires com.homesynapse.state` directive.
2. `./gradlew :core:event-bus:check` — verifies the three visibility promotions (`QueueSaturationHealthCheck`, `HealthSignal`, `HealthLevel` all now `public`), the un-disabled Tier 9 `reconciliationOnVersionMismatch` contract test (subscribe → process → unsubscribe → externally reset checkpoint → re-subscribe → assert full re-replay), and that the removal of `import org.junit.jupiter.api.Disabled` left no other usages.
3. `./gradlew :core:state-store:check` — verifies the new `ReadinessSource` interface compiles (transitive `SubscriberMode` from event-bus is in scope) and that `ReconciliationTest` passes its 4 tests (upgrade mismatch discards, allow-stale-snapshots preserves, idempotent across instances, downgrade mismatch discards).
4. `./gradlew :lifecycle:lifecycle:check` — verifies the three new types compile, the new module-info `requires transitive` directives resolve, and `SharedSchedulerTest` passes its 5 tests (refill cadence, tick cadence, shutdown without throwing, shutdown idempotent, task-failure-survives-cadence).
5. `./gradlew check` (full project) — catches any consumer that broke against the SqliteStateStore method rename (none expected — `SqliteStateStore` is package-private, only `SqliteStateStoreTest` calls `serialize(int)`).
6. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies the existing integration tests still pass after the event-bus visibility promotions (no behavioural change expected).

**Risk profile:** Low–medium. The risks are:
- **(a)** The Tier 9 reconciliation test is new and exercises a code path (unsubscribe → externally reset checkpoint → re-subscribe with same ID) that hasn't been explicitly covered before. If the bus's `subscribeRuntime` does not correctly re-read the checkpoint on the second subscription, the test will fail and reveal a real defect. The test deliberately uses 5-second `awaitMode` budgets to absorb scheduling variance.
- **(b)** `SharedSchedulerTest`'s cadence tests rely on `Thread.sleep` + counter assertions. CI scheduling variance could produce flakes if the test machine is heavily contended; the `>=` lower-bound assertions provide some margin.
- **(c)** The promotion of three event-bus types to `public` is a one-way API expansion — once shipped, downstream code may depend on them. The brief authorized only `QueueSaturationHealthCheck` promotion; `HealthSignal` and `HealthLevel` were promoted only because `-Xlint:exports` would have failed otherwise (see Deviation D-1 in the Completion Report).

**Out-of-session scope:** The brief asked for a full composition root (PersistenceFactory + HomeSynapseCore + wiring). Reading the actual codebase revealed the assumed prerequisites do not exist:
- `SqlitePersistenceLifecycle` does not construct `SqliteStateStore` or `SqliteDeadLetterStore` and does not expose a `WriteCoordinator` accessor.
- `WriteCoordinator` has no `queueSize()` method (the `IntSupplier` in the bus's 7-arg constructor needs one).
- No production `SubscriberReadConnectionFactory` exists — only the testFixtures `RecordingReadConnectionFactory`.
- `HealthSignal` and `HealthLevel` are package-private (the brief said `QueueSaturationHealthCheck` promotion was "clean — no `-Xlint:exports` risk").
- `SubscriberInfo` and `SubscriptionFilter` constructor shapes differ from the brief's snippets (no `displayName` field; 3rd `SubscriptionFilter` arg is `SubjectType`, not a String).

Per the user's M3.6d sub-divide decision (Option A), this WU (M3.6d-a) delivers only the independent satellite changes. M3.6d-b will land the `PersistenceFactory` + `HomeSynapseCore` wiring after the persistence-side infrastructure work it depends on.

### M3.6c — Per-Module Event-Class Manifests (2026-05-20)
**Commit:** `38d3e30`. **Build:** GREEN at HEAD (full `./gradlew check` PASS). Resolved 2026-05-20.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md ("You do NOT run builds, compilation, or tests"). The change spans 1 new production file + 4 modified files across `core/event-model`, `integration/integration-api`, `core/persistence` (test sources), and `testing/integration-tests` (test sources). No `module-info.java` files were modified — all dependency edges already existed.

**Commands Nick must run against the working tree:**
1. `./gradlew :core:event-model:check` — verifies `EventTypes` still compiles cleanly with the new `CORE_PRODUCTION_EVENT_CLASSES` field and the updated class-level Javadoc; existing `EventTypeAnnotationTest` and `EventTypesTest` remain unchanged.
2. `./gradlew :integration:integration-api:check` — verifies the new `IntegrationEvents` public final class compiles, the existing `IntegrationEventTypeAnnotationTest` still passes against the same 5 lifecycle subtypes, and `module-info.java` exports `com.homesynapse.integration` (unchanged).
3. `./gradlew :core:persistence:check` — verifies `AllEventClasses` still compiles with the new aggregation pattern (now imports `EventTypes` and `IntegrationEvents` instead of 27 individual class imports) and all existing callers (`EventTypeRegistryTest`, `EventPayloadCodecTest`, `JacksonWarmupTest`, `SqliteEventStoreTest`, `SqlitePersistenceLifecycleTest`, `EventCategoryMappingTest`) still resolve `AllEventClasses.ALL_EVENTS` / `CORE_EVENTS` / `INTEGRATION_EVENTS` correctly.
4. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` still resolves to the same 27 classes after the refactor and that `BurstLoadIT`, `HeapBudgetIT`, `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, and `CrashRecoveryIT` continue to pass.
5. `./gradlew check` (full project) — catches any unexpected consumer that imported the now-redundant 27 individual event class imports from `IntegrationTestHarness` or `AllEventClasses` (none expected; both files only used the imports internally).

**Risk profile:** Very low. The aggregation is behaviour-preserving: `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` is exactly the same 22 classes in the same order as the previous inline list, and `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` is exactly the same 5 classes. The composition is `Stream.concat(...).toList()` which produces an immutable `List` (`List.copyOf` semantics under the hood — same as `List.of(...)` callers rely on). No ArchUnit rules are affected. No `module-info.java` files modified — `core/persistence`'s and `testing/integration-tests`' test source sets already had `testImplementation(project(":integration:integration-api"))` in `build.gradle.kts`.

### M3.6b — ReplayWindowQueue Capacity Parameterisation + EventBusConfig (2026-05-20)
**Commit:** `df2743a`. **Build:** GREEN at HEAD (full `./gradlew check` PASS). Resolved 2026-05-20.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md ("You do NOT run builds, compilation, or tests"). The change spans 1 new production file + 2 new test files + 5 modified files inside `core/event-bus` (and 0 modifications to `testing/integration-tests` — the integration harness keeps using `InProcessEventBusFactory.createWithMetrics(...)` which now delegates to `createWithConfig(..., EventBusConfig.HOME_DEFAULT)` so observed behaviour is unchanged).

**Commands Nick must run against the working tree (HEAD will be set when Nick commits):**
1. `./gradlew :core:event-bus:compileJava` — DEC-M3-16 visibility-promotion verification. If this fails with `-Xlint:exports` warnings, STOP and report the exact method and leaked type per the brief's "Pre-promotion verification" — the factory approach would be needed instead.
2. `./gradlew :core:event-bus:check` — module-level GREEN; verifies `EventBusConfigTest` (4 tests), `ReplayWindowQueueTest` (4 tests), the renamed `replayWindowOverflowAtConfiguredCapacityIsCriticalAlert` Tier-9 contract test, and the existing `InProcessEventBusTest`/`InMemoryEventBusTest` suites.
3. `./gradlew check` (full project) — catches any unexpected cross-module consumer that constructed `InProcessEventBus` directly (only `InProcessEventBusTest` does, in-package) or that referenced `InProcessEventBus.PUBLISHER_BLOCKED_DEPTH_THRESHOLD` (no such consumers grep'd at instruction time).
4. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies `BurstLoadIT` (M3.4a) and the M3.4b sustained-load tests still pass on `EventBusConfig.HOME_DEFAULT`.

**Risk profile:** Low. Surface is confined to `core/event-bus`. The 10,000 / 5,000 defaults are preserved exactly via `EventBusConfig.HOME_DEFAULT`, so behavioural risk is limited to (a) the `-Xlint:exports` check on the `public` class declaration (verified in pre-promotion analysis: every `EventBus` interface method uses public types), and (b) the contract-test rename (renamed test still exercises identical scenario, just with derived thresholds). NO_DIRECT_TIME_ACCESS verified locally via grep — no `Instant.now`/`Clock.systemUTC()`/`System.currentTimeMillis()` invocations introduced.

### M3.6a — Profile-Driven Persistence Configuration (2026-05-19)
**Commit:** `17c40b6`. **Build:** GREEN at HEAD (full `./gradlew check` PASS). Resolved 2026-05-20.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md ("You do NOT run builds, compilation, or tests"). The change spans 13 modified files + 1 new file across `core/persistence` and `testing/integration-tests`.

**Commands Nick must run against the working tree (HEAD will be set when Nick commits):**
1. `./gradlew :core:persistence:check` — verifies the constructor/PRAGMA refactor + the new per-profile PRAGMA verification tests.
2. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies `BurstLoadIT` and `HeapBudgetIT` still pass on `PersistenceConfig.HOME_DEFAULT` (the prior implicit default made explicit).
3. `./gradlew check` (full project) — catches any unexpected consumer of the old `DatabaseExecutor(int, Clock)` or `SqlitePersistenceLifecycle(Path, int, Clock, HomeId, List)` signature outside `core/persistence` and `testing/integration-tests`.

**Risk profile:** Low — surface is constrained to two modules and all known call sites were updated. Highest risk is an arch-rule regression in a test file (NO_DIRECT_TIME_ACCESS) — verified locally via grep, no `Instant.now`/`Clock.systemUTC()`/`System.currentTimeMillis()` invocations introduced.

### Prior deferred gates — RESOLVED

- **M3.1 (2026-05-17):** Resolved at M3.2 commit — `./gradlew :core:event-bus:check` GREEN.

### Prior deferred gates — RESOLVED

- **M3.1 (2026-05-17):** Resolved at M3.2 commit — `./gradlew :core:event-bus:check` GREEN.
- **M3.2 (2026-05-17):** Resolved — `./gradlew :core:event-bus:check` GREEN on `0bade6a`.
- **M3.3 (2026-05-17):** Resolved — `./gradlew :core:event-bus:check` GREEN on second pass at `a5d4b2a`.
- **M3.5a (2026-05-18):** Resolved — full `./gradlew check` passed on `a2aff9c`.
- **Bus-Fix Piece A (2026-05-18):** Resolved — implicit via subsequent M3.5b build GREEN on top of `fceafe8`.
- **M3.5b (2026-05-18):** Resolved — module-level GREEN at `08d0136`; full project GREEN through subsequent commits.
- **Projection-checkpoint wiring (2026-05-19):** Resolved — full `./gradlew check` GREEN on `56aaa4b`.
- **Supervisor DLQ wiring (2026-05-19):** Resolved — full `./gradlew check` GREEN on `ed5862c`.
- **M3.4a (2026-05-19):** Resolved — full `./gradlew check` GREEN on `5ae7912`; `./gradlew :testing:integration-tests:test -PpiProfile=throttled` GREEN.
- **M3.4b (2026-05-19):** Resolved — `./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled -PsustainedMinutes=10` GREEN on `adf04d2`.
- **DeploymentProfile correction (2026-05-15):** Nick ran `./gradlew check` — passed.
- **D1 WAL Pathology Validation Spike (2026-05-15):** Nick ran `:spike:wal-validation:compileJava`, `:spotlessCheck`, and `:runD1` on 2026-05-15. All three gates passed.
- **M2→M3 Bridge interface specifications (2026-05-15 earlier session):** 10 new Java types (state-store: 5, persistence: 5) + V003 migration compiled cleanly; full `./gradlew check` passed.

---

## Current Task

None. M3.6e.1 work tree complete and awaiting Nick's build gate (see Deferred Build Gate above). After Nick verifies GREEN, the **next work unit is M3.6e.2** per PLAN-M3-CONSOLIDATED-02 §10 — Admin endpoints (DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint), the 6 new ArchUnit rules (including QUERY_SERVICE_READ_ONLY), and the first REST endpoint handlers for entity queries. PM should issue the M3.6e.2 coding instruction when ready.

## Last Completed Milestone

**M3.6e.1 — MaterializedStateQueryService + REST Readiness Gate + Javalin Bootstrap** (2026-05-22). Build gate DEFERRED to Nick (see Deferred Build Gate section). **M3.6 capstone** — the composition root is now externally queryable.

### Prior Last-Completed Milestone

**M3.6d-b — PersistenceFactory + HomeSynapseCore Composition-Root Wiring** (2026-05-21). Build GREEN at `dfb045e`. See Deferred Build Gate section for details.

### Prior Last-Completed Milestone

**M3.6d-a — Composition-Root Satellite Changes** (2026-05-20). Build GREEN at `25bc23b`.

Files delivered (3 new production types + 1 new public test + 1 new public production interface + 1 modified disabled test + 4 modified production files + 1 modified test + 1 module-info + 1 build.gradle.kts + 4 MODULE_CONTEXT files):

**`core/persistence`:**
- `SqliteStateStore.java` (MODIFIED) — added `implements com.homesynapse.state.StateCheckpointSource`; renamed `serialize(int)` → `serializeCheckpoint(int)` (public, `@Override`); promoted `loadedProjectionVersion()` to public (`@Override`). Class-level Javadoc updated. The class itself stays package-private; composition root will expose the same instance via the two interface types.
- `SqliteStateStoreTest.java` (MODIFIED) — 3 callsites updated from `serialize(int)` to `serializeCheckpoint(int)`.

**`core/event-bus`:**
- `QueueSaturationHealthCheck.java` (MODIFIED) — class declaration `final class` → `public final class`; constructor `public`; `tick()` method `public`; `CHANNEL_SATURATING` and `CHANNEL_RECOVERED` constants `public`. DEC-M3-16 part 3.
- `HealthSignal.java` (MODIFIED) — record `record HealthSignal(...)` → `public record HealthSignal(...)`; compact constructor `public`. Promoted because `QueueSaturationHealthCheck`'s public constructor takes `Consumer<HealthSignal>` and `-Xlint:exports` would have failed otherwise. **Deviation D-1.**
- `HealthLevel.java` (MODIFIED) — `enum HealthLevel` → `public enum HealthLevel`. Promoted with `HealthSignal` (same `-Xlint:exports` chain).
- `EventBusContractTest.java` (MODIFIED, testFixtures source set) — removed `@Disabled("M3.5a")` from Tier 9 `reconciliationOnVersionMismatch`; implemented test body (publish 10 events → subscribe → wait LIVE → unsubscribe → externally reset checkpoint to 0 → re-subscribe → assert all 10 events re-replayed). Removed now-unused `import org.junit.jupiter.api.Disabled`.

**`core/state-store`:**
- `ReadinessSource.java` (NEW) — public interface with single method `SubscriberMode mode()`. Composition root implements via delegation to `StateProjection.currentMode()`. M3.6e's `MaterializedStateQueryService` consumes it for REST/WebSocket gating.
- `ReconciliationTest.java` (NEW) — focused concrete test class in `src/test/java/com/homesynapse/state/`. 4 of the brief's 5 reconciliation tests implemented (upgrade mismatch discards checkpoint, allow_stale_snapshots preserves, idempotent across repeated mismatch, downgrade also discards). 5th brief test (`reconciliationRecordsMetadataInDataSlot`) deferred as a documented feature gap — see Deviation D-2.

**`lifecycle/lifecycle`:**
- `HomeSynapseConfig.java` (NEW) — public record with 2 fields (`PersistenceConfig persistence`, `EventBusConfig eventBus`); compact constructor enforces non-null; `HOME_DEFAULT` constant pairs `PersistenceConfig.HOME_DEFAULT` with `EventBusConfig.HOME_DEFAULT`.
- `SharedScheduler.java` (NEW) — package-private final class. Two constructors: production form takes `DerivedWriteRateLimit + QueueSaturationHealthCheck`; test-friendly form takes `Runnable refillTask + Runnable tickTask` (the production form delegates to it). `Executors.newSingleThreadScheduledExecutor` with daemon thread `hs-sched-0`. `scheduleAtFixedRate` for both tasks (50 ms refill, 1 s tick). Tasks wrapped in `safelyInvoke` so a thrown RuntimeException is logged but does NOT cancel the schedule. `shutdown()` calls `shutdownNow()` + `awaitTermination(2 s)`; idempotent.
- `ThrowingStateQueryService.java` (NEW) — package-private final class implementing `StateQueryService`. All 5 methods throw `IllegalStateException(NOT_WIRED_MESSAGE)` where `NOT_WIRED_MESSAGE = "StateQueryService not yet wired — available after M3.6e"`.
- `SharedSchedulerTest.java` (NEW) — 5 tests (refill cadence, tick cadence, shutdown without throwing, shutdown idempotent, task-failure-survives-cadence).
- `module-info.java` (MODIFIED) — added `requires transitive` for `com.homesynapse.persistence`, `com.homesynapse.event.bus`, `com.homesynapse.state`.
- `build.gradle.kts` (MODIFIED) — added `api` deps for the same three modules + `testImplementation(project(":testing:test-support"))`.

**MODULE_CONTEXT.md updates:**
- `core/persistence/MODULE_CONTEXT.md` — SqliteStateStore row updated (now implements StateCheckpointSource; method rename + promotion documented).
- `core/event-bus/MODULE_CONTEXT.md` — header type count 16 public + 17 package-private → 19 public + 14 package-private; QueueSaturationHealthCheck/HealthSignal/HealthLevel moved conceptually to public table (entries added in public table; pointer left in package-private table for navigation); Tier 9 disabled-count updated 5 active+1 disabled → 6 active; two new gotchas (tick() now public; HealthSignal/HealthLevel promotion chain).
- `core/state-store/MODULE_CONTEXT.md` — header type count 19 → 20; new "M3.6d-a Readiness-source seam" subsection with `ReadinessSource` entry; total file count 21 → 22; new M3.6d-a deliverables section in Phase 3 Cross-Module Context.
- `lifecycle/lifecycle/MODULE_CONTEXT.md` — header rewritten from "Scaffold" to "7 public + 2 package-private types"; new module-info dependencies listed and explained; build.gradle.kts updated; new "M3.6 Composition-Root Primitives (M3.6d-a)" subsection with three new type entries; new "M3.6d-a deliverables" Phase 3 Note.

**STOP Gate Results:**
- G1 (SqlitePersistenceLifecycle 5-arg constructor): ✓ — package-private, 5-arg production constructor confirmed (line 125–133).
- G2 (InProcessEventBus 7-arg public constructor): ✓ — public class, public 7-arg constructor confirmed (line 140–158).
- G3 (QueueSaturationHealthCheck pre-promotion verification): ✗ **FAILED** — `HealthSignal` and `HealthLevel` are package-private. Per the brief's pre-promotion STOP gate, this should have stopped the work. Resolved by promoting both transitively. Documented in Deviation D-1.
- G4 (SqliteStateStore current state): ✓ — package-private; serialize(int) was package-private; loadedProjectionVersion() was package-private; did NOT yet implement StateCheckpointSource. All three confirmed before modification.
- G5 (StateProjection.create 11-param): ✓ — exactly 11 params confirmed (line 208–219).
- G6 (StateQueryService 5 methods): ✓ — exactly 5 methods confirmed.
- G7 (lifecycle module-info baseline): ✓ — confirmed `com.homesynapse.persistence`, `com.homesynapse.event.bus`, `com.homesynapse.state` not yet required before this WU.
- G8 (Tier 9 `@Disabled("M3.5a")` location): ✓ — confirmed at line 1473–1478 in EventBusContractTest.java.

**Deviations:**

- **D-1 [REVIEW] — promoted `HealthSignal` AND `HealthLevel` to public (brief only authorized `QueueSaturationHealthCheck`).** The brief asserted the QueueSaturationHealthCheck promotion was "clean — no `-Xlint:exports` risk" and listed the pre-promotion STOP gate. Reading the source revealed both `HealthSignal` (a record carried in the constructor's `Consumer<HealthSignal>` parameter) and `HealthLevel` (the enum nested in the record) are package-private. Per Java's accessibility rules, a public class cannot expose package-private types through its public constructor without `-Xlint:exports` warnings (which become errors under `-Werror`). The minimum-viable promotion was therefore a 3-class chain, not 1. The promotions are pure visibility changes — no behaviour, signature, or contract changes. PM should verify against DEC-M3-16 whether the broader chain matches design intent.

- **D-2 [INFO] — `ReconciliationTest` ships with 4 of the brief's 5 tests; `reconciliationRecordsMetadataInDataSlot` is deferred as a feature gap.** The brief described a test that asserts reconciliation metadata (reconciledAt, fromVersion, toVersion) is recorded in the checkpoint data blob. Reading `StateProjection.writeCheckpoint(Instant)` shows it passes plain `projectionVersion` to `checkpointSource.serializeCheckpoint(int)` — there is no API surface on `StateCheckpointSource` to receive the three metadata fields, and `SqliteStateStore.serializeCheckpoint(int)` passes `null` for the three optional metadata args to `CheckpointSerializer.serialize(...)`. Recording reconciliation metadata in the data slot is a real feature gap, not a test issue. Implementing it requires: extending `StateCheckpointSource` with an overload (or a tracker callback), threading the metadata through `StateProjection.initialize`'s reconciliation path so the NEXT `writeCheckpoint` after reconciliation passes the captured `reconciledAt`/`fromVersion`/`toVersion` values, and an updated `SqliteStateStore` that forwards them. **Recommendation:** track this as a separate enhancement WU after M3.6d-b.

- **D-3 [INFO] — `SharedScheduler` has a second constructor taking two `Runnable`s for testability.** The brief specified a single constructor `(DerivedWriteRateLimit, QueueSaturationHealthCheck)`. Both collaborators are `final` classes, so they cannot be mocked. The clean test pattern is a package-private secondary constructor taking the two scheduled tasks as `Runnable`s; the production constructor delegates by method-reference (`rateLimit::refill`, `healthCheck::tick`). This preserves the brief's specified constructor signature exactly while making the scheduler unit-testable.

- **D-4 [INFO] — `SharedSchedulerTest` ships with 5 tests, not 4.** The brief's 4 tests (refill cadence, tick cadence, shutdown < 2 s, shutdown idempotent) are all present. A 5th test (`taskFailureDoesNotSilenceCadence`) verifies that `SharedScheduler.safelyInvoke` correctly catches a thrown `RuntimeException` so the scheduler keeps firing — without this, a single transient fault would silently disable the rate limiter or the saturation health check. The test pattern was added because `ScheduledExecutorService.scheduleAtFixedRate` cancels future executions of a throwing task by default, and `safelyInvoke` is the load-bearing defence.

- **D-5 [INFO] — `shutdownTerminatesWithin2Seconds` renamed to `shutdownTerminatesWithoutThrowing` to honor NO_DIRECT_TIME_ACCESS.** The brief's test name implies measuring elapsed wall-clock time, which would require `System.nanoTime()` (banned in non-whitelisted modules per the arch rule). The test instead delegates the timing guarantee to `SharedScheduler.shutdown()` itself, which calls `executor.awaitTermination(2_000ms)`; the test merely verifies `shutdown()` returns without throwing within the JUnit per-test budget.

- **D-6 [INFO] — Major scope reduction from original M3.6d brief.** Per the user's Option A decision after pushback (logged in this session), M3.6d was sub-divided into M3.6d-a (this WU — independent satellite changes) and M3.6d-b (the next WU — `PersistenceFactory` + `HomeSynapseCore` wiring). The M3.6d-a delta is exactly the work that does NOT depend on `SqlitePersistenceLifecycle` constructing new stores, `WriteCoordinator.queueSize()`, or a production `SubscriberReadConnectionFactory`. See the M3.6d-a Deferred Build Gate section's "Out-of-session scope" paragraph for the gap analysis.

**M3.6d-a Lessons:**

1. **Pre-promotion verification must check transitively, not just the class being promoted.** The brief stated DEC-M3-16 part 3 promotion was "clean," meaning the class declaration could simply gain the `public` modifier. Reading the source revealed three transitively package-private types in the constructor's parameter type chain (`HealthSignal` carries `HealthLevel`). A class promotion is only clean if every type appearing in its public method signatures (constructors, methods, fields) is itself already public — checking the class itself is insufficient. The cost of missing this: a build that compiles cleanly today but fails the next time `-Werror` runs.

2. **Sub-dividing a large WU when prerequisites are missing is better than guessing.** The original M3.6d brief assumed prerequisites that did not exist: persistence-side construction of `SqliteStateStore` and `SqliteDeadLetterStore`, a `WriteCoordinator.queueSize()` method, a production `SubscriberReadConnectionFactory`, public `HealthSignal`/`HealthLevel`. The user's Option A (sub-divide) let M3.6d-a land the independent satellite changes cleanly while M3.6d-b can address the prerequisites as a focused next WU. Pattern: when a brief's "Files to Create or Modify" table grows past ~18 entries during discovery, sub-dividing is usually the right move — large WUs compound risk and review burden.

3. **`final` collaborators in a constructor require a test-friendly secondary constructor.** `DerivedWriteRateLimit` and `QueueSaturationHealthCheck` are both `final` (correctly so — they have invariant state). The production constructor `SharedScheduler(DerivedWriteRateLimit, QueueSaturationHealthCheck)` cannot be unit-tested directly because the collaborators cannot be mocked. The clean pattern is a package-private overload `SharedScheduler(Runnable, Runnable)` accepting the two scheduled tasks directly; the production form wraps `rateLimit::refill` and `healthCheck::tick` and delegates. This preserves the brief's specified production API while making the scheduler testable.

### Prior Last-Completed Milestone

**M3.6c — Per-Module Event-Class Manifests** (2026-05-20). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (1 new + 4 modified):

- `integration/integration-api/src/main/java/com/homesynapse/integration/IntegrationEvents.java` (NEW) — public final utility class with `private` constructor and single `public static final List<Class<? extends DomainEvent>> LIFECYCLE_EVENT_CLASSES` constant listing the 5 `IntegrationLifecycleEvent` subtypes (`IntegrationStarted`, `IntegrationStopped`, `IntegrationHealthChanged`, `IntegrationRestarted`, `IntegrationResourceExceeded`). Class-level Javadoc cites M3.6c, DECIDE-04, and Q3 gap closure; explains forcing-function semantics.
- `core/event-model/src/main/java/com/homesynapse/event/EventTypes.java` (MODIFIED — see Deviation D-1) — added one `public static final List<Class<? extends DomainEvent>> CORE_PRODUCTION_EVENT_CLASSES` field listing the same 22 core `DomainEvent` payload records that previously lived inline in `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` and `AllEventClasses.CORE_EVENTS`. New `import java.util.List;`. Class-level Javadoc updated to describe the dual role (string constants + class manifest); the existing 46 string constants are untouched. New section header `// ========== Core Production Event Class Manifest (M3.6c, DECIDE-04) ==========`.
- `core/persistence/src/test/java/com/homesynapse/persistence/AllEventClasses.java` (MODIFIED) — replaced the inline `List.of(...)` lists with `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` / `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` aliases. `ALL_EVENTS` now constructed via `Stream.concat(EventTypes.CORE_PRODUCTION_EVENT_CLASSES.stream(), IntegrationEvents.LIFECYCLE_EVENT_CLASSES.stream()).toList()` — the same aggregation pattern the M3.6d composition root will perform. All 27 individual event class imports removed; new imports for `EventTypes`, `IntegrationEvents`, and `java.util.stream.Stream`. Field names `CORE_EVENTS`, `INTEGRATION_EVENTS`, `ALL_EVENTS` preserved unchanged because 7 caller sites (`EventTypeRegistryTest`, `EventPayloadCodecTest`, `JacksonWarmupTest`, `SqliteEventStoreTest`, `SqlitePersistenceLifecycleTest`, `EventCategoryMappingTest`) reference them. Class Javadoc updated to describe the M3.6c aliasing.
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` (MODIFIED) — replaced the 27-element inline `List.of(...)` with the same `Stream.concat(...).toList()` aggregation pattern. All 22 core event imports removed plus the 5 fully-qualified `com.homesynapse.integration.*` references; new imports for `EventTypes`, `IntegrationEvents`, and `java.util.stream.Stream`. Field Javadoc updated to cite the canonical per-module manifests.
- `core/event-model/MODULE_CONTEXT.md` (MODIFIED) — `EventTypes` row updated: kind unchanged (still `final class (utility, no instantiation)`), purpose updated to "Canonical registry of core event type string constants AND the canonical roster of core event payload classes (M3.6c)", key-details cell extended to describe the new `CORE_PRODUCTION_EVENT_CLASSES` field, its role in the composition root, DECIDE-04 + ArchUnit Rule 3 enforcement, and the forcing-function semantics. Type count unchanged (47) because the field is added to an existing class, not a new type.
- `integration/integration-api/MODULE_CONTEXT.md` (MODIFIED) — header type count 21 → 22; opening paragraph updated to mention the new utility class; new "Utility Classes (1)" section added immediately after "Exception (1)" with the `IntegrationEvents` row (purpose, dependency relationship with `EventTypes`, DECIDE-04 enforcement, forcing-function semantics).

**STOP Gate Results:**
- G1: `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` count = 27 (22 core + 5 integration) ✓ matches design doc
- G2: `AllEventClasses` exists in `core/persistence/src/test/java/...`; it is a `final class` (utility, package-private, private constructor) with three `static final List<Class<? extends DomainEvent>>` fields (`CORE_EVENTS`, `INTEGRATION_EVENTS`, `ALL_EVENTS`) ✓
- G3: `core/event-model/src/main/java/module-info.java` exports `com.homesynapse.event` ✓ (line 7)
- G4: `integration/integration-api/src/main/java/module-info.java` exports `com.homesynapse.integration` ✓ (line 25)

**Count Verification (post-modification):**
- `EventTypes.CORE_PRODUCTION_EVENT_CLASSES.size()` = 22 ✓ (matches prior `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` core slice and `AllEventClasses.CORE_EVENTS` content exactly)
- `IntegrationEvents.LIFECYCLE_EVENT_CLASSES.size()` = 5 ✓
- `AllEventClasses.ALL_EVENTS.size()` = 27 ✓ (preserved)
- `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES.size()` = 27 ✓ (preserved)

**Deviations:**
- **D-1 [REVIEW] — `EventTypes` MODIFIED rather than CREATED.** The PM's coding instruction said CREATE `core/event-model/src/main/java/com/homesynapse/event/EventTypes.java`, but the file already exists as the M2.1-added holder for the 46 `@EventType`-string constants (referenced by every annotation and registered with `EventTypeRegistry`). The most natural fit is to add the new `CORE_PRODUCTION_EVENT_CLASSES` constant to the existing `EventTypes` class — both the string constants and the class list are forms of "the canonical core event roster," and keeping them in one class avoids splitting the canonical place across two siblings. The alternative (a new `EventClasses` sibling) would have diverged further from both the design-doc naming and the PM's specified file path. Behavioral contracts are preserved; the public API gains exactly one new field. The Javadoc and MODULE_CONTEXT.md were updated to describe the dual role. **PM should verify** that this resolution matches their intent for the design-doc text, and confirm whether the design doc §5 should be retroactively annotated to reflect that `EventTypes` already existed at M3.6c-time.
- **D-2 [INFO] — Field name `AllEventClasses.ALL_EVENTS` preserved (PM brief said `AllEventClasses.ALL`).** The existing field is `ALL_EVENTS`; renaming would have broken 6 caller sites for no semantic gain. The aggregation pattern (Stream.concat) is applied exactly as specified; only the field name differs from the brief.
- **D-3 [INFO] — `AllEventClasses.CORE_EVENTS` / `INTEGRATION_EVENTS` preserved as upstream-aliasing fields.** The brief did not specify whether to keep these constants. Two of them (`CORE_EVENTS` and `INTEGRATION_EVENTS`) are used by `EventTypeRegistryTest` independently of `ALL_EVENTS`. Keeping them as aliases to the new manifests (rather than removing them) preserves the test API while still exercising the manifest pattern.

**M3.6c Lessons:**

1. **Pre-existing class with matching name is a structural conflict, not a coder choice.** When a PM coding instruction says CREATE but the target file already exists with a different purpose, the conflict is the right thing to surface — but the resolution is usually clear from intent: merge the roles if they're semantically adjacent (both = "canonical roster of core events"), or escalate if they're not. Always cite the existing file's role in the deviation report so the PM can verify the merger preserved their design-doc intent.

2. **Field-name preservation when refactoring test utilities.** When refactoring a test-only constant that has many callers in the same module, preserve the field name even if a brief specifies a different one. Renames force unrelated edits across the test suite and add noise to the diff; the brief's name was almost certainly illustrative rather than load-bearing. Flag the divergence as `[INFO]` for transparency.

### Prior Last-Completed Milestone

**M3.6b — ReplayWindowQueue Capacity Parameterisation + EventBusConfig** (2026-05-20). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (1 new production type + 2 new tests + 5 modified):

- `core/event-bus/src/main/java/com/homesynapse/event/bus/EventBusConfig.java` (NEW) — public record with 2 fields (`replayQueueCapacity`, `publisherBlockedDepthThreshold`), compact constructor `>= 1` validation, `HOME_DEFAULT = new EventBusConfig(10_000, 5_000)` constant.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayWindowQueue.java` (MODIFIED) — new `ReplayWindowQueue(int maxCapacity)` constructor with `maxCapacity >= 1` validation; no-arg form retained and delegates with `MAX_CAPACITY = 10_000`. `MAX_CAPACITY` promoted to `public` and re-documented as the default-value reference; `enqueue()` now checks the instance `maxCapacity` field. Javadoc updated to describe the parameterisation and cite M3.6b / audit D4-09.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` (MODIFIED) — class declaration promoted from package-private to `public` (DEC-M3-16). New canonical public 7-arg constructor `(EventStore, CheckpointStore, Clock, SubscriberReadConnectionFactory, BusMetrics, IntSupplier, EventBusConfig)`. Existing 4-arg and 6-arg constructors remain package-private and delegate (4-arg → 6-arg → 7-arg) with `EventBusConfig.HOME_DEFAULT`. The static `PUBLISHER_BLOCKED_DEPTH_THRESHOLD = 5000` constant removed; replaced with instance `final int publisherBlockedDepthThreshold` initialised from `config.publisherBlockedDepthThreshold()`. `subscribeRuntime` constructs the per-subscriber `ReplayWindowQueue` with `config.replayQueueCapacity()`.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/InProcessEventBusFactory.java` (MODIFIED) — added `createWithConfig(EventStore, CheckpointStore, Clock, SubscriberReadConnectionFactory, BusMetrics, IntSupplier, EventBusConfig) → EventBus`. Existing `create(...)` and `createWithMetrics(...)` retained and delegate with `EventBusConfig.HOME_DEFAULT`. Class Javadoc updated to reflect the M3.6b visibility promotion.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/test/EventBusContractTest.java` (MODIFIED) — Tier-9 `replayWindowOverflowAt10000IsCriticalAlert` renamed to `replayWindowOverflowAtConfiguredCapacityIsCriticalAlert`; the overflow publish count and unique-delivery assertion now derive from `EventBusConfig.HOME_DEFAULT.replayQueueCapacity()` instead of literal 10,000. Added `EventBusConfig` to the imports list.
- `core/event-bus/src/test/java/com/homesynapse/event/bus/EventBusConfigTest.java` (NEW) — 4 tests covering `HOME_DEFAULT` exposing the prior hard-coded values, and three validation rejections (zero capacity, zero threshold, negative capacity).
- `core/event-bus/src/test/java/com/homesynapse/event/bus/ReplayWindowQueueTest.java` (NEW) — 4 tests: overflow at custom capacity (5), default-capacity backward compatibility (10,000 — slow but verifies the legacy bound directly), constructor rejects zero, constructor rejects negative.
- `core/event-bus/MODULE_CONTEXT.md` (MODIFIED) — header type count 32 → 33; new `EventBusConfig` row in the public-types table (16 public types); `InProcessEventBus` row moved out of the package-private table into the public-types table (with the new 7-arg constructor and the `publisherBlockedDepthThreshold` instance-field note); `ReplayWindowQueue` row updated to describe the parameterised constructor; `InProcessEventBusFactory` row in the testFixtures section gained the `createWithConfig` overload; new M3.6b Phase 3 Note block added immediately before "Performance targets".

**STOP Gate Results:**
- G1: `ReplayWindowQueue.MAX_CAPACITY = 10_000` confirmed; previously package-private `static final`; single no-arg constructor ✓
- G2: `InProcessEventBus` previously `final class` (package-private); two constructors (4-arg, 6-arg); `PUBLISHER_BLOCKED_DEPTH_THRESHOLD = 5000` constant present ✓
- G3: `InProcessEventBusFactory` public class with `create(...)` + `createWithMetrics(...)` factory methods ✓

**Deviations:** None. SD-1 (default unchanged) preserved via `HOME_DEFAULT`. SD-2 (two-field config) preserved — no third field added. SD-3 (backward compat) preserved via delegation chain; the test-time integration harness (`testing/integration-tests/IntegrationTestHarness`) needed zero modifications because `createWithMetrics(...)` is the entry point and it now delegates with `HOME_DEFAULT`. SD-4 (DEC-M3-16 visibility promotion) applied to `InProcessEventBus`.

**DEC-M3-16 Visibility Verification:** Deferred to Nick's compile gate. Pre-promotion audit (in-session): every method on `InProcessEventBus` is either an `EventBus` interface override (all 8 use public types — `String`, `long`, `SubscriberInfo`, `Subscriber`, `SubscriberSnapshot`, `List<SubscriberSnapshot>`) or a package-private method (`subscribeWithHandler`, `reset`) which doesn't fall under `-Xlint:exports` because it isn't part of the public API of the module. Expected outcome: PASS.

### Prior Last-Completed Milestone

**M3.6a — Profile-Driven Persistence Configuration** (2026-05-19). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (1 new + 13 modified):
- `core/persistence/src/main/java/com/homesynapse/persistence/LockingMode.java` (NEW) — package-private enum `NORMAL`/`EXCLUSIVE`. Cited in `DeploymentProfile.lockingMode()` accessor and `DatabaseExecutor.connectionPragmas(profile)`.
- `core/persistence/src/main/java/com/homesynapse/persistence/DeploymentProfile.java` (MODIFIED) — added 3 fields: `busyTimeoutMs` (5,000 ms uniform), `lockingMode` (`NORMAL` uniform), `readThreadCount` (2/2/4 for STUDIO/HOME/PERFORMANCE). Six fields total; accessor count goes from 3 → 6. `lockingMode()` is package-private; the rest are public.
- `core/persistence/src/main/java/com/homesynapse/persistence/DatabaseExecutor.java` (MODIFIED) — production constructor changed from `(int readThreadCount, Clock)` to `(DeploymentProfile, Clock)`; decorator overload from `(int, Clock, Function)` to `(DeploymentProfile, Clock, Function)`. Hardcoded `CONNECTION_PRAGMAS` list replaced by `connectionPragmas(profile)` rendering method — 8 elements for NORMAL, 9 for EXCLUSIVE. `journal_mode = WAL` remains mandatorily first. `cache_size` rendered as `-<profile.cacheSizeKiB()>`. Constructor validates `profile.readThreadCount() ∈ [1, 8]` (LTD-03 ceiling).
- `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (MODIFIED) — production constructor changed from `(Path, int, Clock, HomeId, List)` to `(Path, PersistenceConfig, Clock, HomeId, List)`; decorator overload follows. `start()` passes `config.profile()` into `DatabaseExecutor`. Package-private visibility preserved (do not promote to public — 5 `-Xlint:exports` errors).
- `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceLifecycle.java` (MODIFIED) — interface Javadoc scrubbed of `WAL`/`PRAGMA`/`SQLite`/`sqlite` outside `@see` tags. Replaced with engine-neutral phrasing ("Opens databases, runs migrations, prepares connections"; "Closes connections, flushes pending writes, releases resources"). Implementation class retains SQLite-specific Javadoc.
- `core/persistence/src/testFixtures/java/com/homesynapse/persistence/PersistenceTestHarness.java` (MODIFIED) — all three factories (`start`, `startWithWriteCoordinator`, `startThrottled`) now accept `PersistenceConfig` instead of `int readThreadCount`.
- `core/persistence/src/test/java/com/homesynapse/persistence/DatabaseExecutorTest.java` (MODIFIED) — added 3 per-profile PRAGMA verification tests (STUDIO/HOME/PERFORMANCE) + 1 locking_mode default-not-emitted test. Existing PRAGMA assertions rewritten to derive expected values from the profile. Replaced literal `2`/`3` integers in `DatabaseExecutor(...)` calls with `DeploymentProfile.HOME`/`DeploymentProfile.PERFORMANCE`.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqlitePersistenceLifecycleTest.java` (MODIFIED) — `READ_THREAD_COUNT = 2` replaced with `CONFIG = PersistenceConfig.HOME_DEFAULT`. `createLifecycle()` passes `CONFIG` through.
- `core/persistence/src/test/java/com/homesynapse/persistence/AtomicCheckpointWriterTest.java` (MODIFIED) — `READ_THREAD_COUNT` → `PROFILE = DeploymentProfile.HOME`.
- `core/persistence/src/test/java/com/homesynapse/persistence/AtomicCheckpointWriterDlqTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteCheckpointStoreTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteDeadLetterStoreContractTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteEventStoreTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteViewCheckpointStoreTest.java` (MODIFIED) — same substitution at both call sites (default `dbExecutor` plus the microsecond-precision `isolatedExecutor`).
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` (MODIFIED) — `DEFAULT_READ_THREAD_COUNT = 2` replaced with `DEFAULT_PERSISTENCE_CONFIG = PersistenceConfig.HOME_DEFAULT`. Both `PersistenceTestHarness.start[Throttled](...)` call sites updated.
- `core/persistence/MODULE_CONTEXT.md` (MODIFIED) — `DeploymentProfile` entry (3→6 fields), `DatabaseExecutor` entry (profile-driven PRAGMAs), `SqlitePersistenceLifecycle` entry (PersistenceConfig), `PersistenceTestHarness` entry (factory signatures), added `LockingMode` to package-private types table, added M3.6a Phase 3 Note entry, added profile-driven-PRAGMA gotcha, updated 4 stale references to the prior hardcoded PRAGMA list / `DatabaseExecutor(readThreadCount, clock)` signature.

**STOP Gate Results:**
- G1: DeploymentProfile enum values = 3 (STUDIO, HOME, PERFORMANCE) ✓, fields = 3 before (cacheSizeKiB, mmapSizeBytes, journalSizeLimitBytes) ✓
- G2: Hardcoded literal grep — `-128000`/`1073741824` confirmed in `DatabaseExecutor.java` + `DatabaseExecutorTest.java`; both replaced with profile-driven rendering and assertion ✓. Spike module references (`spike/wal-validation/PragmaConfig.java`, `D1WalStarvationTest.java`) intentionally left in place — spike code is out of scope per design doc §3.
- G3: `SqlitePersistenceLifecycle` 5-arg production constructor + 6-arg decorator overload, package-private ✓
- G4: `PersistenceConfig` 2 fields + `HOME_DEFAULT` constant ✓; record shape unchanged (`readThreadCount` lives on the profile per SD-5)
- Post-strip grep: `PersistenceLifecycle.java` returns ZERO matches for `WAL|PRAGMA|SQLite|sqlite` outside `@see` tags ✓

### Prior Last-Completed Milestone

M3.4b (adf04d2) — Sustained-Load + Crash-Recovery Integration Tests (2026-05-19). Build GREEN.

Files delivered (8 new + 4 modified):
- `core/persistence/src/testFixtures/java/com/homesynapse/persistence/ThrottledWriteCoordinator.java` (NEW) — disk test double, package-private final class wrapping any `WriteCoordinator`. Delay runs inside the write thread (10 ms baseline + 200 ms spike at 0.5% by default). `withDefaults(delegate)` factory + 4-arg explicit constructor.
- `core/persistence/src/test/java/com/homesynapse/persistence/ThrottledWriteCoordinatorTest.java` (NEW) — 9 unit tests (delegation, baseline delay, spike at p=1, no spike at p=0, exception propagation, shutdown forwarding, defaults factory, constructor validation × 3). Placed in `src/test/java` mirroring `InMemoryWriteCoordinatorTest`; brief allowed either source set.
- `core/persistence/src/testFixtures/java/com/homesynapse/persistence/PersistenceTestHarness.java` (MODIFIED) — added `startWithWriteCoordinator(...)` (Function-decorator factory), `startThrottled(...)` (Pi-4 defaults convenience), `abandonForCrashSimulation()` (no-op proxy for `close()`). The existing `start(...)` factory delegates to `startWithWriteCoordinator(..., Function.identity())`.
- `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (MODIFIED) — added package-private 6-arg constructor accepting a `Function<WriteCoordinator, WriteCoordinator>` decorator. Public 5-arg constructor delegates with `Function.identity()`.
- `core/persistence/src/main/java/com/homesynapse/persistence/DatabaseExecutor.java` (MODIFIED) — added package-private 3-arg constructor accepting the decorator. Field type of `writeCoordinator` widened from `PlatformThreadWriteCoordinator` to `WriteCoordinator` (interface) to accept the decorator's wrapper. The `shutdown()` method already routed through the `WriteCoordinator.shutdown()` interface method, so no change needed there. Production 2-arg constructor delegates with `Function.identity()`.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/InProcessEventBusFactory.java` (MODIFIED) — added `createWithMetrics(..., BusMetrics, IntSupplier)` overload routing through the production 6-arg `InProcessEventBus` constructor. Existing `create(...)` delegates to `createWithMetrics(..., BusMetrics.noop(), () -> 0)`.
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` (MODIFIED) — added `startThrottled(Path, Clock, BusMetrics, IntSupplier)`, `startForCrashSimulation(Path, Clock)`, `abandon()` instance method. `start(Path, Clock)` and the three new factories all share a private `startInternal(...)` helper.
- `testing/integration-tests/src/test/java/com/homesynapse/it/Pi4SustainedLoadIT.java` (NEW) — sustained 100 ev/s test (10/60 min via `-PsustainedMinutes`). 50 rotating entities, BusMetricsRecorder-driven lag assertions, WAL/heap/checkpoint freshness checks. Event count assertion loosened from the brief's ±2% to lower-bound 25% — see Open risks.
- `testing/integration-tests/src/test/java/com/homesynapse/it/Pi4D1SpikeIT.java` (NEW) — 50 ev/s for 30 min with spike-induced lag transients; lag drain assertion within 5 s of final publish; WAL ceiling.
- `testing/integration-tests/src/test/java/com/homesynapse/it/CrashRecoveryIT.java` (NEW) — 5 000 events → wait for checkpoint ≥ 3 000 → abandon → restart → assert every globalPosition in [1, 5000] observed exactly once across both lifetimes; bus reaches LIVE; checkpoint at head; event store intact. Uses `@TempDir(cleanup = CleanupMode.NEVER)` because abandoned harness holds SQLite file handles on Windows.
- `scripts/pi4-validation.sh` (NEW) — on-device runner for hs-dev-1. Bash with `set -euo pipefail`. Rsync source → run gradle remotely → pull JUnit XML + HTML reports + JFR. Supports `--dry-run` for safe validation; SUSTAINED_MINUTES positional arg (default 60); standard help banner. `chmod +x` applied.

MODULE_CONTEXT.md updated: `core/persistence/MODULE_CONTEXT.md` (added M3.4b gotchas, extended testFixtures inventory, added M3.4b Phase 3 note) and `core/event-bus/MODULE_CONTEXT.md` (extended `InProcessEventBusFactory` entry with `createWithMetrics`).

---

## Next Work Unit

**M3.6e.2 — Admin Endpoints + ArchUnit Rules.** Final M3.6 sub-WU. PM coding instruction produced 2026-05-22. Scope: admin endpoints (DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint), entity query endpoints (GetStateEndpoint, GetStatesEndpoint, GetSnapshotEndpoint), and ArchUnit rules (including QUERY_SERVICE_READ_ONLY). After M3.6e.2, M3 is complete.

### Key context for the next coder session

1. **Composition root is externally queryable.** `HomeSynapseCore` at `76288af` implements a 16-step bootstrap including Javalin server on port 7070 with readiness filter, entity query endpoints, and admin endpoints. `stateQueryService()` returns the real `MaterializedStateQueryService`.
2. **`ReadinessFilter` + `RestFilters` gateway already exist** (M3.6e.1, `api/rest-api`). `ReadinessFilter` is package-private; `RestFilters.installReadinessGate(Object, ReadinessSource)` is the DEC-M3-16 public gateway. New endpoints can use the same pattern.
3. **`MaterializedStateQueryService` is wired** (M3.6e.1, `core/state-store`). Public final, static factory `create(StateProjection)`. Implements all 5 `StateQueryService` methods. Returns `Optional.empty()` / empty `Map` when projection not LIVE.
4. **`DeploymentProfile` has HTTP thread pool fields** (M3.6e.1). `httpThreads()` and `httpMaxThreads()` — STUDIO(1/4), HOME(2/8), PERFORMANCE(4/16).
5. **`ProblemType.STATE_STORE_REPLAYING` exists** (M3.6e.1). HTTP 503 problem type for readiness-gated responses. New admin endpoints can use the same `ProblemType` pattern.

### M3.6b Lessons (2026-05-20)

1. **Config-record promotion preserves backward compatibility cheapest.** Adding a new 7-arg constructor and delegating from the existing 4-arg/6-arg with a `*_DEFAULT` constant avoided every call-site change in `testing/integration-tests` and in-package tests. Pattern: introduce the canonical constructor as the most-explicit form; chain delegation `convenience → mid → canonical` so each step adds exactly one argument resolved from the default constant. This is the same pattern M3.4b used for `Function<WriteCoordinator, WriteCoordinator>` decoration on `DatabaseExecutor`.

2. **`-Xlint:exports` pre-promotion audit needs only the interface contract.** Before promoting a class to `public`, audit (a) every interface method override (since the interface is already public, all such methods use public types by definition) and (b) any class-only public methods. Package-private methods don't fall under `-Xlint:exports`. For `InProcessEventBus`, every public method came from `EventBus` — the audit was a one-pass grep with no surprises.

3. **Static constants on package-private classes are awkward when defaults move to a config.** When a static constant (`PUBLISHER_BLOCKED_DEPTH_THRESHOLD`) is referenced from tests that should match the production default, the constant either has to stay (and the config has to read from it) or the test has to derive from the config. The cleaner direction is "tests derive from the config" — fewer cross-class assumptions, and the constant can simply go away (as it did in M3.6b for the threshold; `MAX_CAPACITY` was kept only as a documentation reference for the no-arg constructor's default).

### M3.4b Lessons (2026-05-19)

1. **Decorator-function injection for package-private types.** `Function<WriteCoordinator, WriteCoordinator>` as a constructor parameter lets testFixtures wrap package-private production types without exposing them publicly. Pattern: production constructor defaults to `Function.identity()`; test constructor accepts the decorator. Applied to `DatabaseExecutor` and `SqlitePersistenceLifecycle`.

2. **testFixture factories are the bridge pattern for JPMS package-private types.** `PersistenceTestHarness.startThrottled()` encapsulates `ThrottledWriteCoordinator` construction internally, so cross-module test code never references the package-private type by name. Same pattern as M3.4a's `InProcessEventBusFactory`.

3. **@TempDir cleanup on Windows with abandoned resources.** Crash-simulation tests that deliberately leave file handles open (abandoned SQLite connections) must use `@TempDir(cleanup = CleanupMode.NEVER)`. `ON_SUCCESS` still attempts cleanup and throws IOException when handles are held.

4. **SLF4J transitivity under `implementation` scope.** When module A declares `implementation(libs.slf4j.api)`, consumers of module A's testFixtures do NOT get SLF4J on their compile classpath. Explicit `testImplementation(libs.slf4j.api)` required in the consuming module.

---

## Build Status

HEAD at `76288af` on `main`. Last GREEN full-project `./gradlew check`: `76288af` (2026-05-22, confirmed by Nick). M3.6a through M3.6e.2 all committed and GREEN. M3.6 COMPLETE. Seventeen Claude Code work units completed.

---

## Foresight Notes

_No active foresight notes._

---

## Recent prior WUs (archived)

| WU | Commit | Date | Scope |
|---|---|---|---|
| M3.4a — Integration Test Module Scaffold + Harness | `5ae7912` | 2026-05-19 | New `testing/integration-tests` Gradle module (#20); harness + BurstLoadIT + HeapBudgetIT |
| Supervisor DLQ Wiring | `ed5862c` | 2026-05-19 | `SubscriberSupervisor.deliver()` → `DeadLetter` (11 fields) via `SubscriberDlq.park`; new `SubscriberSupervisorTest` |
| Projection-Checkpoint Wiring | `56aaa4b` | 2026-05-19 | `StateCheckpointSource` interface; 10 MB advisory checkpoint-size guardrail |
| M3.5b — StateProjection Production Persistence | `08d0136` | 2026-05-18 | 3 new event-bus public types; `SqliteStateStore` + `SqliteDeadLetterStore` + `CheckpointSerializer`; V004; three-way atomic |
| Bus-Fix Piece A — DerivedWriteRateLimit Visibility Promotion | `fceafe8` | 2026-05-18 | Package-private → public; closes M3.5a G4 mismatch |

Older M3.5a / M3.3 / M3.2 / AMD-38/39 / D1 / M2→M3 Bridge rollup also in `archive/coder-handoff-2026-05.md`.

---

**Last verified against:** `homesynapse-core` commit `76288af` on `2026-05-22`.

<!--
file: context/instructions/2026-06-05_AMD-54-64_DOCS_Project_Review_Prompt.md
purpose: External ratification-review prompt for the Workstream C integration AMD block (AMD-54..64). Paste into the HomeSynapse DOCS Claude Project together with the eleven amendment files.
audience: Nick (dispatch), DOCS-Project reviewer
state-type: instruction
status: READY FOR DISPATCH — authored 2026-06-05 at the Workstream C briefing
-->

# Review Brief: Workstream C Integration AMD Block (AMD-54 … AMD-64)

You are reviewing the eleven-amendment integration-api freeze block for HomeSynapse Core before ratification. The block was authored 2026-06-05 against **homesynapse-core HEAD `e76b925`** (M4.B-S2, Workstream B complete). Every source shape cited in the AMDs was Read-tool-verified at that commit by the PM.

**Inputs to this review conversation (supplied by Nick at dispatch):** (1) this prompt; (2) the eleven AMD files; (3) the **Research 6 return document** (Integration Runtime — Supervisor Patterns for Protocol Adapters) pasted **INLINE in this conversation**. The return is NOT in your Project knowledge (your knowledge is the `homesynapse-core-docs` repo connector only; the raw return was never committed there) and is NOT on the hivemind disk — the inline copy is the sole authoritative text for the fidelity gates. **The G1 gates (R2/R4/R5) run against that inline copy. If the inline return is missing, partial, or truncated, return INCOMPLETE on those three gates and state exactly which sections are missing — never reconstruct, paraphrase from memory, or improvise the verbatim content.**

## Verdict options

RATIFY-AS-IS / RATIFY-WITH-EDITS (list them) / BLOCKING (specify). For each AMD individually, plus a block-level verdict.

## Decision authority you must respect (do NOT re-open)

These are **ratified Nick decisions** (2026-06-04/05) — review their *rendering*, not their substance:

1. **NQ-1:** `SecurityServices` aggregator on `IntegrationContext` — no field-per-service growth.
2. **NQ-2:** keep both version surfaces; rename `schemaVersion`→`descriptorSchemaVersion`; add `configSchemaMajor`/`configSchemaMinor`.
3. **NQ-3:** capability identity = sealed `Capability` permit class + existing `CapabilityInstance`; **no new `CapabilityId` wrapper**.
4. **NQ-4:** **no new SQLite capability table** — capability events project into `Entity.capabilities` (entity-registry projection).
5. **NQ-5:** REC-49 REJECTED (existing `HealthParameters.maxRestarts`/`restartWindow`); 1/60s documented as the embedded override.
6. **NQ-6:** keep the global restart default; per-descriptor override; pre-M9 empirical Zigbee spike.
7. **P2 §8.1:** one AMD = one cohesive change; the REC-41 hooks-vs-schema split is resolved as two full integers (AMD-54 + AMD-55).
8. The block freezes against the **post-B-S2 device model**: `Entity` = 12 components, `ProposedEntity` = 4 components (commit `e76b925`).

## Mandatory verification gates (quote-back rule applies — quote the evidence verbatim)

**G1 — Research-fidelity diffs (the load-bearing gates; the PM did not have the return document — diff against the INLINE copy only; missing/truncated inline copy ⇒ INCOMPLETE on the affected gate):**
- **R4 (AMD-57):** diff the 12 `HealthDetail` values against the Research 6 return §REC-42. If the researcher's list differs, supply the verbatim list. Confirm 12 was the proposed count.
- **R5 (AMD-58):** diff the five new permit **names** and per-permit **fields** against §REC-44 + §7.3. Confirm `IntegrationReauthCompleted` and supply any name corrections verbatim.
- **R2 (AMD-55):** diff the four hook **signatures** (parameter and return types, including the two outcome enums) against the researcher's proposed signatures in §REC-41.
- **R3 (AMD-56):** did REC-43 propose a dedicated auth exception type, or only the enum value? Quote the relevant passage.

**G2 — PM narrowings/refinements (status: PRE-CO-SIGNED by Nick 2026-06-05, formalized at ratification — your job is soundness verification, not preference relitigation):**
- **R6 (AMD-59 §2.1):** the persisted capability-event payload drops `Class<? extends Capability>` and the `ts` field from the NQ-3 sketch, adds `EntityId`, and carries the full `CapabilityInstance`. Verify: (a) the serde argument (a `Class<?>` component in a persisted payload, decode via `Class.forName`) is sound under the AMD-52 codec discipline; (b) nothing in the Research 6 return contradicts entity-targeted (vs device-targeted) capability events; (c) replay self-sufficiency (AMD-59-INV-02) holds.
- **R7 (AMD-60 §2.1):** PM dropped the research's `SecureCredentialBundle` in favor of string-based `rotate(...)`, citing the existing `config` `SecretEntry`. Check the return's REC-45 for load-bearing bundle fields (token+refresh-token atomic rotation?) — if present, the AMD widens to `rotate(Map<String,String>)`.
- **R1 (AMD-55 §6):** options-vs-config boundary semantics deferred to M6/M9 — confirm the research did not require freezing the partition now.

**G3 — Source-shape spot checks (your independent re-derivation; the source companion lists the files):**
- `IntegrationDescriptor` = 8 components with `schemaVersion` last; `IntegrationContext` = 10 components; `HealthParameters.defaults()` = (120s, 20, 5m, 1h, 5, **3**, 60s, 30s, 5m, 3, 2); `IntegrationHealthRecord` = 13 components; `ExceptionClassification` = 3 values; `IntegrationLifecycleEvent` = 5 permits with the 5-accessor contract; `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` = 5 entries; `CapabilityInstance` = 7 components led by `String capabilityId`; `Entity` = 12 components incl. `List<CapabilityInstance> capabilities`; both module-infos exactly as embedded in AMD-54 §7 / AMD-56 §6.
- Confirm **zero JPMS changes** across the block: every new type lands in `com.homesynapse.integration` or `com.homesynapse.integration.runtime` (both already exported); every referenced foreign type rides an existing `requires transitive` edge; `EventTypes` gains string constants only.

**G4 — Cross-block coherence:**
- AMD-55's `migrate` consumes AMD-54's pair; AMD-56's `AUTH_FAILED` triggers AMD-55's `onReauthRequired`; AMD-58's reauth events close AMD-56's loop; AMD-59/60 grow `IntegrationContext` 10→12 with consistent nullable/`RequiredService` gating (`RequiredService` 3→5); the four descriptor AMDs (61–64) compose with AMD-54 into one 8→14 component evolution with a single 8-arg convenience constructor. Verify no AMD contradicts another and the convenience-ctor default story is complete and consistent.
- The dot-namespace decision (AMD-58 §2.2): confirm coherence with the project-wide direction (automation `automation.run.*`, config `config.*`) and that freezing the legacy snake_case five is stated everywhere it matters.

**G5 — Invariant quality:** each AMD's invariants (AMD-54-INV-01 … AMD-64-INV-01) must be testable, non-overlapping, and registrable in `Architecture_Invariants_v1.md` §24+ without collision with §20–§23 (AMD-47/51/52/53 blocks).

## Constraints catalogue (violations are BLOCKING)

No `ServiceLoader` (DECIDE-04 / ArchUnit Rule 3); no Jackson in domain/api modules (`NO_JACKSON_IN_DOMAIN_MODEL` is live); no `@Nullable` annotations (Javadoc-only nullability); no `synchronized` (LTD-11); typed-ULID identifiers only (LTD-04); adapters touch core only via `IntegrationContext` (LTD-17); `DomainEvent` permanently non-sealed (AMD-33); persisted event-type strings immutable; Register C voice in all error/reason text; supervisor implementation is **M9 — the block is contract-only**.

## Output format

Per-AMD table (verdict, blocking items, edits), then the G1 verbatim diffs, then a block verdict. The PM will source-verify any claim you make that is not accompanied by a verbatim quote (Research-6 confabulation guard — both directions).

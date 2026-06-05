<!--
file: context/planning/2026-05-31_Workstream-C_gate-status.md
purpose: Warm-start note for the eventual Workstream C session (integration-api interface freeze, Research 6 REC-41–51). Lists the gates that must clear before C — the six Research 6 NQs (Nick's calls, with PM leans), the P4 Doc-05 currency check, and the post-B device-model dependency — plus the AMD-numbering status. So C opens warm, not cold.
audience: Nick (decide NQ-1..6), PM (author C amendments/instructions)
state-type: current
status: CURRENT — issued 2026-05-31 (B Stage 1 issue session)
source: context/assessments/2026-05-22_Research_6_PM_Assessment.md (v1) + context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md + context/handoff/pm-handoff.md
-->

# Workstream C — Gate-Status Note (integration-api interface freeze)

**One-line status:** Workstream C is **last in the locked sequence** (B Stage 1 → B Stage 2 → **C**) and **gated**. It cannot freeze until (1) **B Stage 1 + Stage 2 land** (the capability surface is shaped by B's `Entity`/`EntityRole`/`capabilities` decisions), (2) **Nick resolves Research 6 NQ-1..6**, and (3) **P4 Doc-05 (Integration Runtime) is brought current** against the resolved integration-api. This note surfaces all three so Nick can begin the NQ calls in parallel with B.

> **✅ GATE A CLEARED — 2026-06-04.** Nick resolved **NQ-1..6 by adopting all six PM leans below** (W23 Goal 2; recorded in the Research 6 assessment addendum + OQ-05-05 RESOLVED). NQ-3/NQ-4 are pre-decisions that finalize automatically when M4.B-S2 (EntityRole) lands — no further Nick action needed unless B-S2 changes the `Capability`/`Entity` shape (it is not expected to: B-S2 touches `EntityType`/`Entity`/`ProposedEntity`, not the `Capability` hierarchy). Remaining C gates: **B-S2 landing** (instruction issued 2026-06-04: `context/coding-instructions/M4.B-S2_AMD44_EntityRole.md`) and the **Doc-05 currency pass at C-briefing** (Gate B below).

---

## 1. The post-B dependency (why C waits for B)

Research 6's capability surface — `CapabilityAdded` / `CapabilityRemoved` events, capability *identity*, and `Entity.capabilities` — is **defined by B's device-model decisions**, not C's:

- **NQ-3** (capability identity) leans on the sealed `Capability` permit class (`Class<? extends Capability>`) + existing `CapabilityInstance`. That hierarchy is a **device-model** type that B touches.
- **NQ-4** (capability storage model) routes `CapabilityAdded`/`CapabilityRemoved` through projection into **`Entity.capabilities`** (device-model), explicitly **not** a new state-store SQLite table — per Research 8 REC-23/REC-26 (capabilities live on `Entity`, `EntityState` carries no structural metadata).

So if C froze the integration-api before B's `Entity`/`EntityRole`/capability shape is final, the `CapabilityPublisher` / capability-event contracts would freeze against a moving target. **C freezes once, against the post-B device model.** (B Stage 1 = Floor/Area/`Set<HardwareIdentifier>`; B Stage 2 = EntityRole + the `EntityType.legalRoles` matrix.)

---

## 2. Gate A — Research 6 NQ-1..6 (Nick's calls; PM lean per question)

These are strategic/scope calls — no source-verification items remain open (Research 6 v1 is fully PM-verified). **Nick can begin deciding these now, in parallel with B.** PM leans below are carried verbatim from the Research 6 assessment §"Open Questions for Nick"; they are recommendations, not decisions.

**NQ-1 — `IntegrationContext` field count: one field per security service, or aggregate?**
PM lean: **Aggregator.** Add a single `SecurityServices security` field bundling `CredentialRotator` + future security services — keeps the record at **11 fields** rather than growing linearly. REC-47's `CapabilityPublisher` can be its own field or a separate `DiscoveryServices` aggregator; just don't grow `IntegrationContext` field-by-field per service. *(Drives REC-45 / the AMD that adds the field.)*

**NQ-2 — `schemaVersion` vs `configSchemaMajor/Minor` reconciliation.**
PM lean: **Keep both, rename the existing field.** Rename the existing `int schemaVersion` on `IntegrationDescriptor` → `descriptorSchemaVersion` (the descriptor's forward-compat contract); add `configSchemaMajor` + `configSchemaMinor` for the *config* schema that `migrate(...)` operates on. Two distinct concerns; do the rename in the same REC-41 amendment to make the distinction explicit. *(This is also the REC-41 hooks-vs-schema split — it may genuinely split one amendment into two integers.)*

**NQ-3 — REC-47 capability identity (`CapabilityId` doesn't exist).**
PM lean: **Use the sealed `Capability` permit class as the type identity + existing `CapabilityInstance` as the instance identity** — `CapabilityAdded(integration, device, capability: Class<? extends Capability>, instance: CapabilityInstance, ts)`. Do **not** invent a new `CapabilityId` wrapper that nothing else in the system uses. *(Depends on B's `Capability` hierarchy — see §1.)*

**NQ-4 — REC-47 storage model (researcher proposed a new `capability` SQLite table).**
PM lean: **No new SQLite table.** Capability events update `Entity.capabilities` via projection (the standard Research 8 REC-28 `DispatchingProjectionAdvancer` pattern). `CapabilityAdded`/`CapabilityRemoved` are **entity-registry** (state-changing) projection, not state-store projection. Conflicts with Research 8 REC-23/REC-26 otherwise. *(Depends on B — see §1.)*

**NQ-5 — REC-49 conflict with existing `HealthParameters.maxRestarts` + `restartWindow`.**
PM lean: **Reject REC-49.** The equivalent fields already exist; use them. Document the OTP-derived `(maxRestarts=1, restartWindow=60s)` as the recommended embedded-system override on `HealthParameters.defaults()`. **AMD-61 withdrawn** (this is why the R6 block is 10 AMDs, not 11).

**NQ-6 — default restart intensity for radio-based adapters.**
PM lean: **Keep 1/60s as the global default; rely on the per-descriptor override** (existing `HealthParameters.defaults()` mechanism). Flag an **empirical spike before M9** — measure actual Zigbee/Matter restart frequency on a Pi 5 during normal operation — but don't loosen the global default speculatively.

**NQ summary:** NQ-1/NQ-2/NQ-5/NQ-6 are decidable now (independent of B). **NQ-3 and NQ-4 are the post-B-dependent pair** — Nick can pre-decide the lean, but they only *finalize* once B's Entity/capability shape is locked.

---

## 3. Gate B — P4 Doc-05 (Integration Runtime) currency

**Checked 2026-05-31 against `homesynapse-core-docs/design/05-integration-runtime.md`.**

- **Status: STILL OPEN + P3-gated** (matches pm-handoff "Next Tasks" #0a-iii). Doc-05 is at its **original Locked state, dated 2026-03-06** — it predates Research 6 (2026-05-22). It has **no** masthead currency note for Research 6 REC-41–51 and **no** integration-block AMD content folded in.
- **What's not yet reflected:** the four `IntegrationAdapter` lifecycle hooks (REC-41), the `HealthDetail` enum + `IntegrationHealthRecord` change (REC-42), `AUTH_FAILED` on `ExceptionClassification` (REC-43), the four/five new `IntegrationLifecycleEvent` permits (REC-44 + REC-47 capability events), the `SecurityServices` aggregator on `IntegrationContext` (REC-45/NQ-1), `softDependencies` (REC-46), and the descriptor field additions (REC-48/50/51).
- **One B-adjacent note:** Doc-05's Dependencies line cites Device Model "§8.2 HardwareIdentifier type." B Stage 1 changes `Device`/`ProposedDevice`/`DiscoveryPipeline` from `List<HardwareIdentifier>` → `Set<HardwareIdentifier>`. Doc-05 describes the discovery-pipeline *boundary*, not the collection type, so the dependency reference does not need editing for the `Set` change — but the Doc-05 refresh should confirm the discovery-pipeline prose still reads correctly post-B.
- **Cannot be refreshed yet:** the Doc-05 integration-api freeze content is exactly what NQ-1..6 settle, so the refresh is **gated on Gate A**. Do the Doc-05-half currency pass at C-briefing, after NQ-1..6 resolve and B has landed.

---

## 4. AMD-numbering status (read before authoring any C amendment)

- The Research 6 assessment's **AMD-53 … AMD-63 are non-binding provisional placeholders** that were never authored. A renumber notice has been added to the top of that assessment (2026-05-31).
- **AMD-53 is now consumed** by the timestamp-model unifier (RATIFIED; M4.0b-5, `c99b425`). It is **not** REC-41.
- Per the **P2 AMD Renumbering Decision** (§3 allocation note + §4/§6), the integration block is **assign-at-milestone** and its indicative range **re-bases to 54+** (from the live watermark at C-briefing). The §4 provisional per-REC map (REC-41→54, REC-42→55, …) is a **planning aid only**.
- **Authoring rule (P2 §8):** one AMD = one cohesive, fully-ratifiable-and-implementable change; no sub-letter splits (resolve REC-41's hooks-vs-schema split, per NQ-2, as **two full integers** if it splits — never `54b`). Assign the contiguous block fresh at C-briefing.

---

## 5. Pointers

- Research 6 assessment (dispositions, NQ-1..6, the §"AMD Sequencing" *order* — all valid; integers stale): `context/assessments/2026-05-22_Research_6_PM_Assessment.md`.
- AMD-numbering authority: `context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md` (§3 allocation note, §4 integration block, §6 assign-at-milestone, §8 authoring rules).
- Sequence + Open Risks: `context/handoff/pm-handoff.md` (Next Tasks #0a-iii = Doc-05 half; this note is the warm-start companion).
- Doc to refresh at C-briefing: `homesynapse-core-docs/design/05-integration-runtime.md`.
- B device-model shape that C freezes against: the M4.B-S1 + M4.B-S2 instructions (Floor/Area/`Set<HardwareIdentifier>`, then EntityRole).

**Bottom line:** Workstream C opens warm. Nick can decide **NQ-1/2/5/6 now** and pre-decide **NQ-3/4** (which finalize post-B). Doc-05's integration-api half stays parked until NQ-1..6 land. When C briefs, assign the integration AMD block contiguously from the live watermark (re-based to **54+**), freeze the integration-api against the **post-B** device model, then fold the result into Doc-05.

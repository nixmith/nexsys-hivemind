<!--
file: context/handoff/2026-05-31_B-S1_issue_and_workstream-C_prep_session_prompt.md
purpose: Kickoff prompt for the FRESH Cowork conversation that issues Workstream B Stage 1 (AMD-44, M4.B-S1) to Claude Code, makes the cheap AMD-renumber annotation, and scopes Workstream C's gates (surfacing Research 6 NQ-1..6 for Nick). Paste into the new window.
audience: PM (next Cowork session) ← Nick
state-type: handoff
status: CURRENT — 2026-05-31
-->

# Session Prompt: Issue Workstream B Stage 1 → AMD-renumber annotation → Workstream C gate-prep

**You are the PM (Mode 3, Director).** Workstream A is closed (M4.0b-5 / AMD-53 timestamp-model unifier committed + reviewed → APPROVE; `projectionVersion`=5; on-disk watermark AMD-53; the projection is now typed end-to-end AND event-time-deterministic across all three activity timestamps). This session **issues Workstream B Stage 1** (AMD-44, `M4.B-S1`) to Claude Code, makes one cheap governance annotation, and **tees up Workstream C** so it isn't a cold start. **Load the `nexsys-project-manager` skill first.**

---

## 0. Session-start discipline (do first)

1. **Load `nexsys-project-manager`** and **run the freshness preflight** (10 checks). Expect **PASS**. Ground truth as of this handoff (all committed + pushed):
   - `homesynapse-core` HEAD **`c99b425`** — M4.0b-5 (AMD-53). `projectionVersion`=**5**; on-disk watermark **AMD-53**; **Workstream A COMPLETE**.
   - `homesynapse-core-docs` — AMD-53 ratification (`1ddf4b8`) + `.gitattributes` (`6d54761`). AMD-53-INV-01/02 registered `Architecture_Invariants_v1.md` §23; Doc 03 §4.1 currency note.
   - `nexsys-hivemind` — M4.0b-5 WUCP Phase 2 closeout (`6349915`) + `.gitattributes` (`4bf25df`) + the handoff-archive commit. The 10 spent session prompts are now under `context/handoff/archive/`. **This prompt's predecessor (`2026-05-31_M4.0b-5_review_and_next-batch_session_prompt.md`) is now spent — archive it.** Active handoff files: this prompt + the persistent `coder-handoff.md` / `cross-agent-notes.md` / `pm-handoff.md`.
   - Check 9 (skill-mirror) may read STALE-pending-sync — normal.
2. **Source-verification rule (standing, slightly relaxed):** the one-time `.gitattributes` (`* text=auto eol=lf`) + renormalization is now applied to all three repos, so the CRLF churn that produced false "modified" lists and the mangled `checkAll` diff is fixed going forward. **Still verify every type/field/line claim with the Read tool on the working tree; commit from host git.** If `index.lock` recurs, it is a background **sync daemon** touching `.git` (not git itself) — `rm .git/index.lock` between ops, or pause the folder sync during git operations. (It clobbered a staged index during the last cleanup; watch for "nothing staged" surprises and re-verify with `git status`.)
3. **Two-Project setup is live** (CORE Project = code/JPMS/test reviews; DOCS Project = design/governance/amendment). Use **CORE** for a second opinion on the B Stage 1 instruction's JPMS/shape claims; **DOCS** for any AMD-44 interpretation question. The connector is best-effort, never load-bearing — Cowork embeds the per-question source companion.

---

## 1. Issue Workstream B Stage 1 (the immediate task)

The instruction is **already authored**: `context/coding-instructions/M4.B-S1_AMD44_Floor_Area_Set_HardwareIdentifier.md` (governing amendment **AMD-44**, RATIFIED-pending-impl). It implements the **Floor aggregate** (`FloorId` typed ULID, `Floor` record, `FloorRegistry` **interface**), a **minimal `Area` record + read-only `AreaRegistry` interface**, the **`AreaId` Javadoc fix**, and the **`List`→`Set<HardwareIdentifier>`** refactor (the value-record `HardwareIdentifier` has meaningless duplicates). Interface-/record-level only — no registry implementations, no event emission, no first-boot synthetic-Area logic. **EntityRole + everything touching `EntityType`/`Entity`/`ProposedEntity` is Stage 2 and explicitly OUT of scope.**

**Before issuing — re-verify the STOP-on-Mismatch gates against source at the post-M4.0b-5 HEAD `c99b425` with the Read tool.** (The instruction was verified at `72596cb`; M4.0b-5 touched only `core/state-store` + `lifecycle`, so the device-model/platform-api anchors should be byte-identical — **confirm, don't assume**.)
   - `core/device-model/src/main/java/module-info.java` — `module com.homesynapse.device`; `requires transitive com.homesynapse.value`, `requires com.homesynapse.event`, `requires transitive com.homesynapse.platform`; exports `com.homesynapse.device`. **No `module-info` change in Stage 1** (AMD-44 §4.2 — both target packages already exported).
   - `platform/platform-api/src/main/java/module-info.java` — exports `com.homesynapse.platform` **and** `com.homesynapse.platform.identity` (FloorId's home). **No change.**
   - `platform/platform-api/.../identity/AreaId.java` — the typed-ULID-wrapper pattern `FloorId` mirrors **and** the Javadoc line to fix ("spatial area (room, zone, or floor)" → drop the floor conflation).
   - `core/device-model/.../Device.java` (`List<HardwareIdentifier>` at component position 13), `ProposedDevice.java`, `DiscoveryPipeline.java` (`propose(...)` + `findExistingDevice(...)`) — the `List`→`Set` targets; leave `List<ProposedEntity>` as `List`. `HardwareIdentifier.java` — value record, correct `equals`/`hashCode` for `Set` (no change).
   - `core/device-model/.../{EntityType,Entity,ProposedEntity}.java` — **confirm untouched** (Stage 2 fence). If the Coder finds itself editing these, STOP.
   - **Embed the verbatim `module-info.java`** for both modules in the issued instruction (the Research-6 lesson: verified type names are not enough — module names are load-bearing and must be quoted, not summarized).

**Confirm the milestone tag with Nick** (the instruction proposes `M4.B-S1`; `M4.B1/B3/B4/B5` are reserved by P2 §3 for device-block AMD-46/47/48/49). Then **issue to Claude Code**, routing a **CORE-Project second opinion** on the JPMS edges + the `Set`-refactor blast radius as the source companion.

**Sequencing:** Workstream A is committed → B Stage 1 is unblocked (WUCP one-uncommitted-milestone-at-a-time satisfied). On Claude Code return → PM WUCP Phase 2 review **against source** → closeout → then B Stage 2 (EntityRole).

---

## 2. Cheap governance annotation (do early)

**AMD-renumber ripple.** AMD-53 is now consumed by the timestamp-model unifier. The **Research 6 PM assessment** uses `AMD-53/56/59` as *placeholders* for the integration amendments. Annotate those references as **stale / renumber-at-milestone** — the P2 renumbering decision re-bases the integration block to **54+** (`context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md`). Locate the Research 6 assessment (search `context/assessments/` — the Research 6 / integration-api / capability-surface file) and add the inline note so a future Workstream C session doesn't trip on it. Five-minute edit; do it before C scoping.

---

## 3. Tee up Workstream C (parallel PM work — surface Nick's homework)

Workstream C (integration-api interface freeze, Research 6 REC-41–51) is **last in the locked sequence** and gated. Warm it up:
   - **C must freeze against the POST-B device model.** Research 6's capability surface (`CapabilityAdded`/`CapabilityRemoved`, capability identity, `Entity.capabilities`) is shaped by B's `Entity`/`EntityRole` decisions (Research 6 assessment NQ-3/NQ-4). So C cannot freeze until B Stage 1 **and** Stage 2 land.
   - **Gates to clear before C:** (a) **Research 6 NQ-1..6** — Nick's calls; **surface the six questions explicitly in this session** (with the PM's lean per question where the assessment already points) so Nick can begin deciding them in parallel with B. (b) **P4 Doc-05 (Integration-Runtime) currency** — verify/refresh against the current integration-api.
   - Produce a short **C gate-status note** (`context/planning/`) listing NQ-1..6 + the Doc-05 currency check + the post-B dependency, so the eventual C session opens warm rather than cold.

---

## 4. Pointers

- B Stage 1 instruction: `context/coding-instructions/M4.B-S1_AMD44_Floor_Area_Set_HardwareIdentifier.md`. Amendment: `homesynapse-core-docs/design/amendments/AMD-44_Floor_Aggregate_and_EntityRole_Enum.md` (§2.1/§2.2/§2.6/§4.1/§4.2 = the Stage 1 contract).
- Source to re-verify at `c99b425`: `core/device-model/{module-info.java, Device.java, ProposedDevice.java, DiscoveryPipeline.java, HardwareIdentifier.java, DeviceRegistry.java, EntityRegistry.java}`, `platform/platform-api/.../identity/{AreaId.java, Ulid.java}`, `core/device-model/MODULE_CONTEXT.md`.
- Research 6 assessment (AMD-renumber + NQ-1..6): `context/assessments/` (the Research 6 / integration capability-surface file).
- Current state hub: `context/status/PROJECT_SNAPSHOT.md`; sequence + Open Risks: `context/handoff/pm-handoff.md`; latest pointer: `context/handoff/cross-agent-notes.md`.
- Two-Project architecture: `context/process/2026-05-31_two-project-claude-architecture.md` + `project-knowledge/CLAUDE_PROJECT_{CORE,DOCS}_custom-instructions.md`.

**Bottom line:** Workstream A is done. Re-verify the authored B Stage 1 instruction against `c99b425` (device-model/platform-api untouched by M4.0b-5 — confirm), confirm the milestone tag with Nick, and issue it to Claude Code with a CORE-Project second opinion. Make the cheap AMD-renumber annotation. Then surface Research 6 NQ-1..6 + check Doc-05 currency so Workstream C opens warm. Sequence: **B Stage 1 → B Stage 2 (EntityRole) → Workstream C.**

<!--
file: context/instructions/2026-06-09_AMD-66-71_Ratification_Prompt.md
purpose: Fresh-session prompt — execute the AMD-66..71 ratification mechanics (Nick-authorized 2026-06-09): 5 AMDs PROPOSED→RATIFIED + AMD-69 deferral confirmed, invariants §37–§41 registered, nav-index rows, M6.1 gate lift, tracker closeout. §9–§10 are FORWARD-PRIMING (read after §4–§7; NOT this session's tasks): they leave the conversation primed to roll into M6.1 issuance, the M6.2 PayloadCipher bridge, the M6.3 triple-gate, the parallel floor/evidence lanes, the M6→M7/M9/M10 fan-out, and the standing decision queue.
audience: PM (fresh Cowork session), Nick (commits)
state-type: instruction
status: CURRENT — issued 2026-06-09; archive on consumption
-->

# Ratification Session: AMD-66..71 (M6 Configuration Block)

## 0. Your role and what this session produces

You are the **NexSys Project Manager** — invoke the `nexsys-project-manager` skill before doing anything else. This is a **Mode 1 / governance-mechanics** session: you are executing a ratification **Nick authorized 2026-06-09** after the full independent DOCS review returned and every edit was folded. You are NOT authoring design content, NOT writing Java, and NOT issuing M6.1 (that is the next, separate session — this session makes it issueable).

**The decisions are made — do NOT re-litigate:**

- **AMD-66 → RATIFIED** (RATIFY-AS-IS; [AMD-66-A] `PROCESS_RESTART` fallback ENDORSED by review).
- **AMD-67, 68, 70, 71 → RATIFIED** (RATIFY-WITH-EDITS; all seven edits E67-1/2, E68-1, E70-1/2, E71-1/2 **already folded and committed** at docs `aedff55` — fold nothing further).
- **AMD-69 → DEFERRED, Nick confirms Option (a)** at this ratification (Tier-2 / Doc 15 OQ-15-3; the number stays reserved for the eventual passphrase-root-KDF amendment). OQ-15-3 stays closed.
- **Watermark stays AMD-87.** All six are reserved-below-watermark slots — ratification fills them, it does not raise the ceiling. Say this explicitly in the KB/handoff edits.

Authority chain: review return `context/audits/2026-06-09_AMD-66-71_DOCS_Review_Return.md` (block verdict RATIFY-WITH-EDITS; AMD-69 CONFIRM-DEFERRAL; commit verified at core `6c6dd33`) → PM edit-fold (docs `aedff55`) → Nick's ratification nod (2026-06-09).

## 1. Operating rules

### 1.1 File tool is authoritative — sandbox git is actively hazardous right now
- **Authoritative:** the file tool (host paths), the six AMD files, the review return, and the named governance/KB files in §6.
- **OBSERVED 2026-06-09 (not hypothetical):** the sandbox mount served **byte-truncated copies** of the six AMD files (e.g., AMD-66 cut mid-line at "`[R`"), so sandbox `git status`/`git diff` showed phantom EOF-deletion "modifications" against `aedff55`, and sandbox git emitted an `index.lock` unlink warning. The host files were verified complete via the file tool. **Therefore: do NOT run `git add`/`commit`/`restore`/`checkout` from the sandbox on either repo this session — a sandbox-side commit would commit truncated files. Nick commits from the host.** Read/edit via the file tool; treat sandbox git output as diagnostic-at-best.
- If the shell and the file tool disagree, the file tool wins (the standing P4r rule).

### 1.2 The standard
- **Ratification records acceptance and propagates it — it does not change contracts.** The only AMD-file edits are status mastheads, §9/§10 checklist/disposition updates, and the AMD-69 confirmation annotation. The folded specification text is untouched.
- The §7 verbatim `module-info.java` embeds in all six AMDs were source-verified at `6c6dd33` by the review and must not be perturbed — re-confirm once in the §5 verification pass.

### 1.3 Run the mandatory freshness preflight
Per the skill, before forward work. Expected baselines: core `6c6dd33`, docs `aedff55`, hivemind `da9d2f4`. The PM/coder skill mirrors were synced by Nick 2026-06-09 — Check 9 expected PASS. (A `coder.zip` may sit untracked in hivemind root from the sync — flag to Nick, do not delete.)

## 2. Verified current state (2026-06-09, post-review)

| Fact | Detail |
|---|---|
| core HEAD | `6c6dd33` — source untouched by review/fold; review re-derived every config shape here |
| docs HEAD | `aedff55` — all seven review edits folded; two AMD-71 cosmetic residues (masthead `purpose:`, §7 caption) also fixed pre-commit |
| hivemind HEAD | `da9d2f4` — return on disk + fold closeout |
| Review return | `context/audits/2026-06-09_AMD-66-71_DOCS_Review_Return.md` — per-AMD verdicts + AMD-69 ruling + 4 block-level notes |
| Invariants register | last section **§36** (AMD-87); the M6 block registers as **§37–§41** (see §4.2) |
| Nav index | "AMD-66–71 reserved for the M6 config block"; watermark line = AMD-87 |
| M6.1 instruction | `context/coding-instructions/M6.1_Config_Pipeline.md` — ⛔ GATED on AMD-66/67/70/71 ratification; DP-3 = the ratified [AMD-71-A] resolution |
| Doc 06 / Doc 15 | both LOCKED; neither is edited by this session (Doc-15-inviolate guardrail) |

## 3. Locked inputs (do not change)

1. Ratification date = the date you run this session (confirm via `bash date +%F`; expected 2026-06-09/10).
2. AMD-69 confirmation text: **"DEFERRED — Nick confirmed Option (a) at the 2026-06-DD block ratification; reserved for the Tier-2/OQ-15-3 passphrase-root-KDF amendment."**
3. Eight invariants register verbatim from the AMD §7 sections: AMD-66-INV-01/02, AMD-67-INV-01/02, AMD-68-INV-01, AMD-70-INV-01, AMD-71-INV-01/02. AMD-69 contributes none (deferral record).
4. Block review-return pointer cited in every status flip: `nexsys-hivemind/context/audits/2026-06-09_AMD-66-71_DOCS_Review_Return.md`.

## 4. Deliverables — edit clusters (in order)

Read each target with the file tool before editing; match surrounding format exactly.

### 4.1 The six AMD files (`homesynapse-core-docs/design/amendments/`)
For AMD-66/67/68/70/71: masthead `status:` → `RATIFIED 2026-06-DD (Nick) — DOCS review RATIFY[-AS-IS|-WITH-EDITS, edits folded aedff55]; return: <pointer>`; §9 checklist boxes → `[x]` with dates as each mechanic completes; §10 Review Disposition → a closing paragraph recording verdict, fold commit, ratification date (mirror the AMD-54 §10 pattern). For AMD-69: masthead `status:` → the §3.2 confirmation text; §7 checklist → confirm-deferral box `[x]`; §8 disposition closed.

### 4.2 `governance/Architecture_Invariants_v1.md` — five new sections §37–§41
Follow the §24-block precedent exactly (read §24's preamble first): **§37 AMD-66 (Configuration Change Listener), §38 AMD-67 (Config-Document Schema Major/Minor), §39 AMD-68 (SecretStore Atomic Multi-Key Write), §40 AMD-70 (Config Observability Events), §41 AMD-71 (Hybrid Config Directory Layout)** — §37's preamble introduces the block (five sections, single review return, **AMD-69 deferred — no invariant registered; number reserved for Tier-2/OQ-15-3**), each section's statements **verbatim from the AMD's §7**, implementing WUs named (M6.1 / M6.2 / M6.4 per AMD §8). Same-commit structural updates, per the §19 rule: **§0.3** identifier list (+the five `AMD-NN-INV` families), **§17 Invariant Index** (+8 rows, §37–§41 pointers; if a running count is stated anywhere, derive the current value from the table — do not assume), **§18 Traceability Matrix** (+rows mirroring the AMD-54-block entries).

### 4.3 `design/00-navigation-index.md`
Six new amendment rows (AMD-66..71) in the house one-line style — 66/67/68/70/71 **RATIFIED 2026-06-DD**, 69 **DEFERRED (Tier-2, OQ-15-3; number reserved)** — each citing target Doc 06 surface + invariant §§. Update the §Amendments preamble: "AMD-66–71 reserved" → ratified/deferred per above, **watermark line unchanged (AMD-87)**. Doc 06 row Notes → "Config/secret contract surface amended by the M6 config block AMD-66..71 (RATIFIED 2026-06-DD; AMD-69 DEFERRED)" (mirror the Doc 05 row's style).

### 4.4 Gate lifts (`nexsys-hivemind`)
`context/coding-instructions/M6.1_Config_Pipeline.md`: masthead `status:` ⛔ GATED → **READY TO ISSUE (AMD-66/67/70/71 RATIFIED 2026-06-DD)**; per its `amd-number-note`, pin the now-ratified AMD numbers. `context/planning/2026-06-08_M6-charter.md`: entry-gate status → config side RATIFIED; M6.1 startable; **M6.2's AMD-68 gate half satisfied** (still gated on M6.1 landing).

### 4.5 Tracker closeout (`nexsys-hivemind`)
`context/planning/phase-3-milestone-backlog.md`: M6.1 → UNBLOCKED/READY TO ISSUE; M6.2 row notes AMD-68 ratified. `context/status/PROJECT_SNAPSHOT.md`: ratification recorded; latest commits; next-action → issue M6.1. `context/handoff/pm-handoff.md`: AMD-66–71 Open Risk → RESOLVED; AMD-69 escalation → RESOLVED (Option (a) confirmed); **carry forward, do not drop:** the Doc 15 §8.1 `ScopeKeyManager`-row currency nit (fix rides the next Doc-15-touching amendment — do NOT touch the Locked doc now) and the **M6.4 P2-survey obligation** for `config.section_reloaded` (review block-notes 1–2); OR-M6-NONCE and the E2 bridge carries are unaffected. `context/handoff/coder-handoff.md`: next WU → M6.1 (ready, not issued). `context/handoff/cross-agent-notes.md`: new dated [PM] CURRENT POINTER (block ratified; M6.1 ready; M6.3 still triple-gated). `context/planning/weeks/2026-W24_jun08-jun14.md`: progress line. KB ledger (`project-knowledge/`): `HomeSynapse_Current_State.md`, `HomeSynapse_Knowledge_Primer.md`, `Decisions_Quick_Reference.md`, `Invariants_Quick_Reference.md` (+8), `HomeSynapse_Navigation_Index.md` if it indexes amendments — log the block ratification, the watermark-unchanged note, and the E70-1 type-residency rule as a standing JPMS lesson (now also in the consumer/pin survey).

### 4.6 Bounded stale-content sweep (Nick's ask — keep it tight)
Grep hivemind (file tool / host) for stragglers re this block only: `AMD-66..71 PROPOSED`, `GATED on ratification`, `ratify-ready`, `awaits ratification` — fix those that contradict the new state; touch nothing else. Archive the consumed `context/instructions/2026-06-08_AMD-66-71_DOCS_Review_Prompt.md` → `context/instructions/archive/` (house convention), and this prompt on completion.

## 5. Verification pass (before closeout)

- §7 module-info embeds in all six AMDs byte-identical to `config/configuration/src/main/java/module-info.java` at `6c6dd33` (single `requires transitive com.homesynapse.event;`, single export).
- Eight invariant statements in §37–§41 verbatim vs the AMD §7 texts; §0.3/§17/§18 updated in the same commit; section numbering contiguous after §36.
- Nav index: six rows present; watermark line still AMD-87; no "reserved" residue for 66–71.
- AMD-70's ratified text retains the E70-1 type-residency rule + flattened payloads (`Map<String,Integer>`, `String appliedClassification`) — the load-bearing fold must survive ratification edits.
- No code, no Doc 06 body, no Doc 15 edits; no watermark change.
- WUCP Phase 2 drift check: snapshot / backlog / pm-handoff / charter / M6.1 status all agree.

## 6. Reading list
**Authority:** the six AMD files (full); the review return; this prompt. **Edit targets:** every file named in §4. **Reference (do not edit):** Doc 15 (Locked), Doc 06 (Locked), `2026-05-29_P2_AMD_Renumbering_Decision.md`, M6 charter CARRY 1/2.

## 7. Deliver to Nick
One-screen summary (what flipped, where the 8 invariants landed, watermark unchanged, M6.1 READY/not-issued, what stays parked: M6.3 triple gate, Doc 15 §8.1 nit, M6.4 survey), then the two host-side commit messages:

- **homesynapse-core-docs:** `Ratify AMD-66..71 (M6 config block): 66/67/68/70/71 PROPOSED->RATIFIED + 69 DEFERRED (Option (a), Tier-2/OQ-15-3); invariants §37-§41 (+8) + §0.3/§17/§18; nav-index rows; watermark stays AMD-87`
- **nexsys-hivemind:** `M6 config entry-gate closed: AMD-66..71 ratified/deferred; M6.1 READY TO ISSUE; AMD-68 half of M6.2 gate satisfied; trackers/KB/handoffs current; review prompt archived`

## 8. Do not
- Do not re-open any verdict, edit, or the AMD-69 deferral; do not touch Doc 15 or Doc 06 bodies; do not raise the watermark.
- Do not issue M6.1 or brief the Coder (next session). Do not pre-split M6.1 (Fork-2 decision: issue whole; the Coder's Phase-2 inventory is the split checkpoint).
- Do not run git writes from the sandbox (§1.1 — observed truncation hazard). Nick commits from the host.
- Do not let the stale-sweep sprawl beyond §4.6's grep set.

---

## 9. Forward priming — the road past ratification

**Read this AFTER §4–§7 are done. It is map, not task list.** Ratification (§1–§8) is this session's whole job, and the §8 do-nots still bind — in particular, **you do not issue M6.1 or write any code here.** What §9 does is leave this conversation *hot*: when the mechanics are closed, you (and the next session) start with the full M6 build trajectory, the technical hazards already surfaced, and the decision queue in view — not a cold restart. If Nick green-lights continuing past ratification in this same session, **§9.1 (issue M6.1) is the immediate next move and is now executable**; otherwise it is the next session, fully primed.

The through-line: **M6 is the keystone of the back half.** It is the literal next milestone and it fans out to M7 (automation), M9 (integration runtime), and M10 (REST/identity). Closing the config + secrets/crypto foundation is what unblocks the runway to the Nov 25 target. The block you just ratified is the *config-contract* half of that foundation; the *crypto* half (Doc 15, LOCKED) is wired in at M6.2. Everything below is sequenced to that.

### 9.1 Immediate next — issue M6.1 (config pipeline), the only non-crypto piece

The instruction (`context/coding-instructions/M6.1_Config_Pipeline.md`) is now ungated. Scope: YAML 1.2 load (snakeyaml-engine, safe-by-default `LoadSettings`) → JSON-Schema validation (networknt 1.5.6; **JSON-text-`String` params only — never leak the `JsonSchema` library type, the locked JPMS-hygiene contract**) → `ConfigModel` in the **AMD-67 `(major,minor)` 6-field shape** → `ConfigurationAccess` (integration-scoped read) + `ConfigurationService` (load / getCurrentModel / getSection) → the **AMD-66 `ConfigurationChangeListener`** interface + composition-time registration → **`config.validation_completed` (AMD-70, the flattened event-resident payload)** → the **AMD-71 hybrid layout + canonicalization-based path-traversal guard**, all on the **DP-3 injected config-dir `Path`** (no `config→platform` edge — the ratified [AMD-71-A] resolution).

Three controls travel with it, non-negotiable: **(a)** the §4c `Clock` injection (config is non-whitelisted — no `Instant.now()`/`systemUTC()` in main or test); **(b)** the **P2 consumer/pin survey** for `config.validation_completed` across the full manifest set (`EventTypes` + `CORE_PRODUCTION_EVENT_CLASSES` + `EventCategoryMapping.TABLE`→`[SYSTEM]` + `EventTypeRegistry` + `JacksonWarmup` + the `HomeSynapseCore`/`IntegrationTestHarness` stragglers); **(c)** the **JPMS/contract-direction check** (now standing in the survey + the lessons — the E70-1 discipline: any new type in a base module references only that module / a leaf / `java.base`).

**Fork-2 (binding):** issue M6.1 **whole**. The split decision is a **Phase-2-inventory checkpoint, not a mid-implementation bail** — the Coder's pre-code file-touch census is the gate. If it shows the unit sprawling (the AMD-70 manifest fan-out **plus** the loader **plus** the `ConfigModel` reshape **plus** the four impls), split at the already-named seam — **M6.1a load/validate, M6.1b access/events** — *before* writing code. Do not pre-split at issue. Done-when: committed + `./gradlew check` GREEN + PM WUCP Phase 2 APPROVE; loads/validates/serves both a zero-config and a populated config; `config.validation_completed` registered + round-trips; the AMD-66/67/70/71 load-path §5 tests GREEN.

### 9.2 M6.2 — secret store + per-scope key-management — the deepest JPMS surface in M6

This is where the discipline we just hard-wired earns its keep. Carry **charter CARRY 1 (the E2 `com.homesynapse.app` bridge, Doc 15 §3.8 verbatim)** into the instruction and re-verify it at issue:

- **`PayloadCipher` is consumer-defined in `persistence`** (`encrypt(scopeId, plaintext)→(ct,iv)` / `decrypt(scopeId, keyVersion, ct, iv)→plaintext`). The config-resident **`ScopeKeyManager` exposes its own `encrypt`/`decrypt` but does NOT implement the persistence-exported `PayloadCipher`** — implementing it in `config` would force a `config→persistence` edge. The **composition root `com.homesynapse.app`** constructs `ScopeKeyManager`, wraps it in a thin `PayloadCipher` adapter (a lambda), and injects it down through `HomeSynapseCore` (lifecycle) into the persistence write path. `app` already `requires` **both** `config` and `persistence` → **zero new module edge**. Re-verify at issue: `persistence !requires config`, `config !requires persistence`, only `app` requires both; **embed both verbatim `module-info.java` files**. A wrong edge here is the AMD-52 / E70-1 cycle class — treat the direction check as a STOP gate, not a courtesy.
- **Key hierarchy (Doc 15 §3.1/§3.4/§4.2):** machine-local root key (`.root-key`, `0400`, `SecureRandom` on first boot) → `HKDF-SHA256(root, "scope:"+id)` → Scope KEK → wraps the Scope DEK (AES-256-GCM) → DEK encrypts payloads. The `scope_keys` table `(scope_id, key_version, encrypted_dek, iv, created_at, destroyed_at?)` is owned config-side.
- **Shared-root unification (Doc 15 §7.3):** the secret store becomes the **`config_secrets` scope** under the same root — one key system, not two. **`SecretStore.setAll(Map)` (AMD-68)** is the atomic all-or-nothing durable multi-key write (write-temp → fsync → atomic-rename → fsync-dir) on **`secrets.enc`** (encrypted JSON — the E68-1/E71-1 name), beneath the M9 `CredentialRotator`.

Gate: Doc 15 (done) + AMD-68 (ratified) + M6.1 landed. Done-when: an encrypt→decrypt round-trip test GREEN; the `setAll` all-or-nothing + durable test GREEN; the bridge wired with no new module edge (re-verified at the gate).

### 9.3 M6.3 — at-rest write-path encryption — the triple-gated piece; do NOT issue until all three clear

Encrypt-on-write of the sensitive-PII categories is **now-or-never on the immutable log**, which is exactly why M6.3 is the most carefully gated unit in M6. Hold it behind **all three**:

- **(a) OQ-15-2** — the Pi-4 AES-256-GCM write-path microbench resolves the exact `encrypted_scopes` set (Doc 15 §9 default `[identity, presence_personal]`). This is a **list-TUNING of a Locked-doc default, NOT a Doc 15 re-open**; STOP-and-escalate if any result implies a *design* change.
- **(b) the energy/erasure interview signal** — confirms no launch-window buyer requires operational crypto-shredding (**AMD-86 §3**). If one does, **AMD-86 re-opens via the formal pipeline BEFORE M6.3 freezes the write path** — that window must close first. (Interviews structured to surface the binary gate — "does any launch-window buyer require operational erasure?" — early, so the gate doesn't wait on full synthesis.)
- **(c) OR-M6-NONCE** (charter CARRY 2, Doc 15 §6/§13.4) — the per-scope GCM **counter-nonce must be durable + strictly monotonic across crash AND restore**: persist the high-water mark **atomically with (or ahead of) the encrypted write**; re-init from the persisted max on boot, **never from memory**; co-design the deferred backup/restore (F3) so a restore can never resume a scope at a counter ≤ any value already used under that DEK (rotate the DEK on restore, or carry the high-water mark in the backup). Done-gate: the Doc 15 §13.4 **kill-mid-encrypt nonce-monotonicity test GREEN**. **(key, nonce) reuse breaks AES-GCM confidentiality AND authentication — catastrophic; this is the deepest correctness gate in the milestone.**

At-rest mechanism (D2 sub-decision (i)): **app-level per-scope payload encryption** (vanilla sqlite-jdbc, no SQLCipher) — the same machinery as the future crypto-shred operation.

### 9.4 M6.4 — hot-reload atomic swap

Atomic `ConfigModel` swap (in-flight readers see whole-old or whole-new — **no torn read**); the **AMD-66 listener invocation** drives per-section `ReloadClassification` application; publishes **`config.section_reloaded` (AMD-70)**. **M6.4's instruction MUST re-run the P2 consumer/pin survey** for `config.section_reloaded` (review block-note 2 — only `config.validation_completed` lands at M6.1). Gate: M6.1 landed.

### 9.5 Parallel lanes — non-Core floor + evidence (Nick-paced, but on the critical clock)

- **M5-C website/docs floor (Lane 4):** the protected, **non-preemptable P6/D3 floor** — Docusaurus scaffold + brand shell + 3–4 positioning/architecture/privacy pages from the Locked docs + `context/strategy/`. **Not started as of W24 — the P6 discipline risk repeating.** It is PM/Hivemind work, Core-independent, and competes with neither the Coder lane nor Nick's gate → **stand up a defined increment this week**; if it loses to Core again it compounds into the fall (stacked on Zigbee + the 72-hour validation gate).
- **M5-D interviews (Lane 5 — the long pole):** weeks of other people's calendars; start this week, surface the binary AMD-86 §3 gate early.
- **The Pi-4 microbench:** rides hardware time but **must not slip past M6.2** — it sets the `encrypted_scopes` list M6.3 consumes.
- **GraalVM native-image (C15) + Gen-ZGC-vs-G1 (C16) Pi spikes** → the **LTD-01 reversal-criteria ledger**; they also bear on the sd_notify transport (OR-M13-SDNOTIFY closed-world question) and on **AMD-69's reserved Tier-2 KDF provider (OQ-15-3 — BC vs PBKDF2 vs FFM)**.

### 9.6 B2 schema decisions C8/C9 — ratify alongside

`context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md` — **C8 `actorRef` semantics** (keep the bare `Ulid`; closed 4-kind set PERSON/AUTOMATION/SYSTEM/API_CLIENT; Tier-1 API keys → API_CLIENT; automations stamp `AutomationId`) + **C9 energy event shape** (the `power_measurement` 4-attribute set + the 6 aggregate fields + the energy consent-scope; shape only, no features — D4). They **freeze schema contracts over the immutable log** → dispatch the **independent (DOCS-Project-style) review** + Nick ratify, same discipline as this block; then the **Doc 01 (C8) / Doc 02 (C9) currency notes**. The enforcing amendments land at the implementing milestones (M10 for C8, M6/M7/energy-feature for C9). **C10 payload-typing posture is consciously deferred** (rides M7 / the energy-feature milestone).

### 9.7 The fan-out — why this block matters past M6

- **M6 → M7 (Automation):** depends on config (M6) + state-store + event-bus. The **C9 energy shape** is what energy automations trigger on; the **C8 `actorRef`** must be stamped on automation-issued commands (closing the "automations carry no actor identity" gap). Heed the sizing warning: `core/automation` is ~100% Phase-2 scaffolding — a from-scratch engine, not interface-fill.
- **M6 → M9 (Integration Runtime):** the supervisor consumes the frozen M4.C surface + config (M6); the **M9 `CredentialRotator` impl writes through `SecretStore.setAll` (AMD-68)** — the coupling AMD-60 anticipated. M9 may **now** publish command-bearing `CapabilityAdded` (the AMD-87 serde gate is GREEN). INV-SE-04 scoped-registry is M9 prep.
- **M6 → M10 (REST/WS API):** config (M6) + integration-runtime (M9); the **C8 `actorRef` feeds the M10 auth/identity surface** (`ApiKeyIdentity` → API_CLIENT). INV-SE-02 (auth mandatory on live endpoints) is currently **unmet (F9)** — an M10 build item, flagged not-now.

### 9.8 Standing disciplines now in force (carry into every session, PM and Coder)

1. **JPMS / contract-direction.** Any new type in a base module (`event-model` / `value-model` / `platform-api`) — especially an event record — references only that module, a leaf, or `java.base`; a higher-layer domain type forces a cycle (the AMD-52 / E70-1 class). Now in the P2 consumer/pin survey + pm-/coder-lessons (2026-06-09). Read the `module-info`; a one-line direction check, catastrophic if missed.
2. **File-tool-authoritative / sandbox-git hazard** (§1.1) — standing policy for this repo set: never git-write from the sandbox; the file tool (host) wins on any disagreement; commit from the host.
3. **Doc-15-inviolate** — the microbench tunes the §9 `encrypted_scopes` list; only the erasure interviews re-open AMD-86 (formal pipeline); STOP-and-escalate on any Doc 15 design gap.
4. **Regret-proof posture** — shapes now, features on evidence (D2/D4): the M6 block, the B2 decisions, and the energy shape all follow it.
5. **The language/runtime deliberation (LTD-01)** runs in parallel as no-regret evidence; the schema decisions are regret-proof under both the stay-Java and go-Rust futures, so nothing on the critical path waits on the language call.

## 10. The standing decision queue (primed, not yet due)

The open decisions the project will face next — surfaced here so the conversation recognizes and tees them up as they ripen. None is this session's to resolve.

| # | Decision | Ripens with | Owner | Note |
|---|---|---|---|---|
| Q1 | The final `encrypted_scopes` set (OQ-15-2) | Pi-4 microbench | Nick runs → PM writes back | Gates M6.3 scope; a Doc 15 §9 list-tuning, not a re-open |
| Q2 | Does a launch-window buyer require operational erasure? (AMD-86 §3) | energy/erasure interviews | Nick runs → PM (re-open pipeline if yes) | Must resolve **before** M6.3 freezes the write path |
| Q3 | Counter-nonce durability + backup/restore co-design (OR-M6-NONCE) | M6.3 design | PM/Coder | §13.4 kill-mid-encrypt test is the done-gate |
| Q4 | At-rest mechanism: SQLCipher whole-DB vs app-level per-scope (D2 sub-(i)) | M6.2/M6.3 | PM (crypto owner-doc) | Likely app-level (no SQLCipher dep); same machinery as shred |
| Q5 | WatchdogSec opt-in (Doc 12 lifecycle) | M13 sd_notify | Nick | Settles FFM-vs-subprocess for OR-M13-SDNOTIFY |
| Q6 | Tier-2 passphrase-root KDF provider (OQ-15-3) | the **AMD-69 reserved slot** | PM (authors) → Nick | BC vs PBKDF2 vs FFM; gated on the GraalVM closed-world evidence |
| Q7 | The language/runtime reversal call (LTD-01) | GraalVM/GenZGC spikes + the interviews' hard-real-time-determinism question | Nick | Evidence-gated; the one input that would re-sequence the back half |
| Q8 | M5-C floor — a defined increment this week | now | PM/Hivemind | The P6 discipline bet; do not let it slip again |
| Q9 | B2 C10 payload-typing posture | M7 / energy-feature | PM → Nick | Deferred this window; the AMD-52 typed-payload precedent governs |

**One-line orientation for whoever picks this up next:** the config-contract foundation is now ratified; M6.1 is the immediate, executable next move; M6.2 is where the JPMS bridge discipline is load-bearing; M6.3 stays triple-gated on evidence Nick is running; and the non-Core floor (M5-C) plus the interviews are the two parallel clocks that must start now so the back half doesn't compress into the fall.

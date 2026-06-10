<!--
file: context/audits/2026-06-09_AMD-66-71_DOCS_Review_Return.md
purpose: Independent DOCS-Project review return for the M6 configuration amendment block (AMD-66..71). Full review (config/secret contract freeze) — per-amendment + block verdicts, AMD-69 ruling.
audience: Nick (ratify), PM
state-type: audit
status: RETURNED 2026-06-09 — verdicts below; PM edit-fold APPLIED 2026-06-09 (E67-1/2, E68-1, E70-1/2, E71-1/2); awaits Nick ratification.
reviewed-at: homesynapse-core HEAD `6c6dd33`; homesynapse-core-docs `bfed118`; nexsys-hivemind `7703300`
note: verbatim return reproduced on disk by PM from the Cowork upload (sandbox/host upload-mount desync; content source-verified against the live review).
-->

# DOCS-Project Review Return — M6 Configuration Block (AMD-66..71)

**Reviewer:** Independent (HomeSynapse Core / DOCS Project)
**Review type:** FULL (config/secret contract freeze — not P4 block-track)
**Source baseline verified at:** homesynapse-core HEAD **`6c6dd33`** (re-derived independently; `git log` confirms `6c6dd33` is one print-string typo fix atop `7f44bed`, no contract impact). Doc 15 confirmed **LOCKED** (watermark **AMD-87**). AMD-54 and AMD-60 confirmed **RATIFIED 2026-06-05** (`8ef9e9f` M4.C). Navigation index confirms **AMD-66–71 reserved for the M6 config block** and on-disk watermark **AMD-87**.

## Verdict summary

| AMD | Verdict | Edits | Fold status |
|---|---|---|---|
| 66 | **RATIFY-AS-IS** | — ([AMD-66-A]: PM's `PROCESS_RESTART` correction ENDORSED) | n/a |
| 67 | **RATIFY-WITH-EDITS** | E67-1, E67-2 (prose-vs-source; non-structural) | FOLDED 2026-06-09 |
| 68 | **RATIFY-WITH-EDITS** | E68-1 (`secrets.yaml.enc` → `secrets.enc`) | FOLDED 2026-06-09 |
| 69 | **CONFIRM-DEFERRAL** (ratify as DEFERRED, Option (a)) | — | n/a |
| 70 | **RATIFY-WITH-EDITS** | E70-1 (**load-bearing** — JPMS payload-type residency), E70-2 | FOLDED 2026-06-09 |
| 71 | **RATIFY-WITH-EDITS** | E71-1 (`secrets.enc`), E71-2 ([AMD-71-A] → Path injection) | FOLDED 2026-06-09 |

**Block verdict: RATIFY-WITH-EDITS.** No REJECT. No amendment requires a Doc 15 change — **Locked Doc 15 remains inviolate** (AMD-69's deferral is what keeps it so). All six numbers sit below the AMD-87 watermark in the reserved range; ratification fills reserved slots and does **not** raise the ceiling.

## 1. Source shapes re-derived at `6c6dd33` (review's independent verification)

All baseline shapes matched the AMD claims. Two discrepancies surfaced (both prose-accuracy, now folded): **`MigrationResult` has no version field** — `(Map migratedConfig, List<MigrationChange> changes)`; only `MigrationPreview` carries `fromVersion/toVersion` (→ E67-1). **`EventTypes` config constants are `CONFIG_CHANGED` + `CONFIG_ERROR` only** — no `secret_added`/`secret_removed` exist anywhere (→ E70-2). `ConfigModel` ctor callers = `TestConfigFactory` ×5 + `InMemoryConfigAccessTest` ×1, none outside the module (→ E67-2). `module-info` (event-model) = `requires transitive value` + `platform` only, **no config edge** (load-bearing for E70-1). `SecureCredentialBundle`/`credentialsFor` = zero references in core source (AMD-68-A confirmed).

## 2. Load-bearing findings

- **[AMD-68-A] retirement VERIFIED, stands.** Ratified AMD-60 §2.1/§9 (R7/A5) rejected the bundle, kept reads on `ConfigurationAccess`, widened `rotate` to `Map`. `setAll(Map)` is the correct/sufficient store-layer discharge of AMD-60-INV-03. No orphaned consumer.
- **[AMD-69] reconciliation CORRECT — ruling CONFIRM-DEFERRAL.** All three Doc 15 conflicts re-verified verbatim (§2.3 post-MVP; §3.5 machine-local MVP root; §3.8 zero-MVP-deps + OQ-15-3 [NON-BLOCKING]). Committing `bcprov-jdk18on` at M6 = a 3-count Locked-doc violation. Do NOT re-open OQ-15-3 now (Tier-2 has no MVP consumer; GraalVM closed-world input not yet in). **Recommend Nick ratify Option (a).**
- **[AMD-67] REC-41 clearance VERIFIED.** AMD-54 RATIFIED, distinct-surface guard correct (INV-01 mirrors AMD-54-INV-01; INV-02 transplant correct). No production migrator; zero cross-module `ConfigModel` consumers.
- **[AMD-66-A] PM correction ENDORSED.** There is no independent "listener-absent default" — absence falls back to the locked per-property `x-reload` mechanism (unannotated → `PROCESS_RESTART`). Blanket `INTEGRATION_RESTART` would be wrong for non-integration sections and could under-apply a `process-restart` property. F7 shape confirmed (`ConfigSection` is a final record). **RATIFY-AS-IS.**
- **[AMD-71-A] RULING: composition-root `Path` injection (Option b).** `config → platform` edge avoided; keeps every embedded module-info true + the zero-new-edge property the E2 bridge depends on. **Confirms the M6.1 instruction's DP-3.** Traversal guard (canonicalization-based) + one-level include verified sound.
- **Manifest discipline (AMD-70) VERIFIED complete.** §2.2 set correctly enumerated; M6.1 P2 survey obligation satisfied; `[SYSTEM]` category consistent with `CONFIG_CHANGED → [SYSTEM]`. M6.4 must re-run the survey for `config.section_reloaded`.

## 3. Enumerated edits (ALL FOLDED 2026-06-09)

- **E67-1 (§2.3):** `MigrationResult` has no version field — only `MigrationPreview` carries the pair; if M6.1 adds applied-version reporting to `MigrationResult` it carries `(major,minor)`.
- **E67-2 (§4):** `ConfigModel` ctor callers = `TestConfigFactory` (5 sites) + `InMemoryConfigAccessTest` (1 accessor); mechanical in-module test-fixture updates; no production/cross-module callers.
- **E68-1 (§2.2):** `secrets.yaml.enc` → `secrets.enc`.
- **E70-1 (§2.1) — LOAD-BEARING:** the specified payload types (`Map<Severity,Integer>`, `ReloadResult` breakdown, `ReloadClassification`) are config-module types in event-resident records → `event→config` JPMS cycle (the AMD-52 class). Flatten to event-resident/`java.base` types (`Map<String,Integer>` keyed by `Severity.name()`; `String appliedClassification`); add the type-residency rule. Config types are *consumed*, never *referenced*.
- **E70-2 (§2.1):** "legacy `config_changed`/`secret_added`/`secret_removed`" → "`config_changed`/`config_error` (`ConfigChangedEvent`, `ConfigErrorEvent`)"; the secret-events claim was propagated unverified from the Research 5 return.
- **E71-1 (§2.1):** `secrets.yaml.enc` → `secrets.enc` (both Locked docs; content is encrypted JSON).
- **E71-2 (§3):** replace the open [AMD-71-A] flag with the resolved decision — composition-root `Path` injection; no `config → platform` edge; cite M6.1 DP-3.

## 4. Block-level notes (non-gating)

1. **Doc 15 §8.1 internal currency nit (do NOT touch the Locked doc for it):** the `ScopeKeyManager` row still reads "implement `PayloadCipher`," while the E2-folded §3.8 specifies the adapter-at-`app` pattern (ScopeKeyManager does *not* implement the persistence type). Record in pm-handoff so the next Doc-15-touching amendment fixes the row; ensure the M6.2 instruction follows §3.8/CARRY 1 (it does).
2. **M6.4 survey obligation:** `config.section_reloaded` lands at M6.4 — its instruction must carry the same P2 consumer/pin survey block.
3. **Naming convention (no action):** `config.validation_completed`/`config.section_reloaded` consistent with the mixed convention (legacy snake_case frozen; dotted for new types per AMD-52/56/58); Research 7 F15 cites them as exemplars.
4. **Review-prompt baseline accuracy:** every dispatch-prompt baseline claim checked out against source.

## 5. Disposition

RETURN to PM for edit-fold (E67-1/2, E68-1, E70-1/2, E71-1/2) — **APPLIED 2026-06-09** — then to Nick for ratification of AMD-66/67/68/70/71 (ACTIVE) + confirmation of the AMD-69 deferral (Option (a)). On ratification: register AMD-66-INV-01/02, AMD-67-INV-01/02, AMD-68-INV-01, AMD-70-INV-01, AMD-71-INV-01/02 in `Architecture_Invariants_v1.md`; add navigation-index rows (watermark **unchanged** — all six < AMD-87); lift the M6.1 ⛔ gate (AMD-66/67/70/71) and the AMD-68 half of the M6.2 gate.

**Commit verified at: homesynapse-core `6c6dd33`** (docs `bfed118`, hivemind `7703300`).

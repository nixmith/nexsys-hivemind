<!--
file: context/instructions/2026-06-08_AMD-66-71_DOCS_Review_Prompt.md
purpose: Independent DOCS-Project review prompt for the M6 configuration amendment block (AMD-66..71). Full review discipline — these freeze config/secret contracts.
audience: DOCS-Project reviewer (independent), Nick (dispatch + ratify)
state-type: instruction
status: CURRENT — issued 2026-06-08 (M6 entry-gate)
-->

# DOCS-Project Review Prompt — M6 Configuration Amendment Block (AMD-66..71)

You are the independent reviewer (HomeSynapse Core / DOCS Project) for the **six-amendment M6 configuration block**. These amendments **freeze config and secret contracts** for M6, so this is a **full independent review** (not the lightweight P4 block-track). Your job is to adversarially re-derive every source-shape claim, test every cross-document reconciliation, and return a per-amendment + block-level verdict.

## Source baseline (verify everything against this, not against the amendments' prose)

- **homesynapse-core HEAD `6c6dd33`** (2026-06-08). The only commit on top of `7f44bed` is a one-line `Main.java` print-string typo fix — no contract impact.
- **Doc 15 (Cryptographic Architecture) is LOCKED**; on-disk amendment watermark **AMD-87**; AMD-86 + AMD-87 RATIFIED.
- **AMD-54** and **AMD-60** are RATIFIED (M4.C, `8ef9e9f`).
- Config module surface at `6c6dd33` (re-derive from source — `config/configuration/src/main/java/com/homesynapse/config/`):
  - `ConfigModel` = 5 components: `int schemaVersion, Instant loadedAt, Instant fileModifiedAt, Map<String,ConfigSection> sections, Map<String,Object> rawMap`.
  - `ConfigMigrator` = 3 methods: `int fromVersion()`, `int toVersion()`, `MigrationResult migrate(Map<String,Object>)`.
  - `SecretStore` = 4 methods: `String resolve(String)`, `void set(String,String)`, `void remove(String)`, `Set<String> list()`.
  - `ConfigurationAccess` = 4 methods (`getConfig/getString/getInt/getBoolean`).
  - `ReloadClassification` = enum, 3 values (`HOT`, `INTEGRATION_RESTART`, `PROCESS_RESTART`; unannotated default `PROCESS_RESTART`).
  - `ConfigSection` = record `(String path, Map values, Map defaults)`; `ReloadResult` = 3 fields `(newModel, changeSet, issues)`.
  - `module-info`: `module com.homesynapse.config { requires transitive com.homesynapse.event; exports com.homesynapse.config; }` — single requires, single export.

## The six amendments + their dispositions

| AMD | Title | Source | Status proposed |
|---|---|---|---|
| 66 | `ConfigurationChangeListener` per-section reload reaction | REC-55 (shape-corrected, F7) | ACTIVE |
| 67 | Config-document schema `(major, minor)` | REC-56 (REC-41 blocker CLEARED by AMD-54) | ACTIVE |
| 68 | `SecretStore.setAll(Map)` atomic durable write (Doc 06 currency) | Doc 15 §7.3 + AMD-60-INV-03; REC-57 bundle/read RETIRED by AMD-60 | ACTIVE |
| 69 | Passphrase-root KDF (Argon2id/BouncyCastle) | REC-58 — **DEFERRED to Tier-2 / OQ-15-3** by Locked Doc 15 | DEFERRED |
| 70 | Config observability events `config.validation_completed` + `config.section_reloaded` | REC-59 (+ REC-61 folded), in `com.homesynapse.event` | ACTIVE |
| 71 | Hybrid config directory layout | REC-60 | ACTIVE |

## The load-bearing review items (adversarial focus)

1. **`[AMD-68-A]` — cross-amendment retirement.** AMD-68 drops Research 5 REC-57's `SecureCredentialBundle` + `SecretStore.credentialsFor` and reduces to `setAll(Map)`. Verify against **ratified AMD-60 §2.1/§9 (R7/A5)**: did AMD-60 reject the bundle and keep credential reads on `ConfigurationAccess`? Is `setAll(Map)` the correct/sufficient store-layer satisfaction of **AMD-60-INV-03** (atomic-across-entries, durable-before-return — no torn token+refresh pair)? Confirm no other ratified artifact depends on the bundle/`credentialsFor`.

2. **`[AMD-69]` — Doc-15 governance (the block's key reconciliation).** AMD-69 defers REC-58's Argon2id+BouncyCastle to Tier-2/OQ-15-3. Verify against **Locked Doc 15 §2.3 (Argon2id/passphrase = post-MVP), §3.5 (MVP machine-local root), §3.8 (MVP adds zero new dependencies; provider = open OQ-15-3), §7.3 (shared root — secret store = `config_secrets` scope)**. Confirm that committing BouncyCastle at MVP would violate the Locked doc, and that the deferral keeps Doc 15 inviolate. **This is the item most likely to need Nick's explicit confirmation** (it reclassifies a Research-5 ACTIVE item to DEFERRED).

3. **`[AMD-67]` — REC-41 clearance + distinct-surface guard.** Verify AMD-54 (RATIFIED) actually froze `(configSchemaMajor, configSchemaMinor)` for adapter configs and that AMD-67 adopts the **same idiom on the distinct system-config-document surface** without deriving one from the other (AMD-67-INV-01 vs AMD-54-INV-01). Confirm zero downstream blast radius (no production `ConfigMigrator` impl at `6c6dd33`).

4. **`[AMD-66-A]` — no-listener default.** AMD-66 §2.3 overrides REC-55's `INTEGRATION_RESTART` listener-absent default with **`PROCESS_RESTART`** (consistency with the locked `ReloadClassification` unannotated default + safe-by-default). Is this the right call, or should the listener-absent default differ from the property-annotation-absent default? Confirm the shape is non-generic / non-sealed (F7 — `ConfigSection` is a `final` record).

5. **`[AMD-71-A]` — config→platform JPMS edge.** AMD-71 resolves the layout under `PlatformPaths.configDir()`. Does the loader take a `requires com.homesynapse.platform` edge, or is the resolved config-dir `Path` injected from the composition root? Verify the chosen option keeps the module graph acyclic and matches the embedded `module-info`. Confirm the §2.3 path-traversal guard is canonicalization-based (`toRealPath`), not string-prefix.

6. **Manifest discipline (AMD-70).** Confirm the M3.6c/M4.C event-type manifest set is correctly enumerated as a M6.1 consumer/pin-survey obligation (the M4.C lesson — an unregistered event type fails `encode` and trips count-pinned tests).

## Verdict format (return to `context/audits/2026-06-DD_AMD-66-71_DOCS_Review_Return.md`)

For **each** amendment: `RATIFY-AS-IS` / `RATIFY-WITH-EDITS` (enumerate every edit, cite the source line) / `REJECT` (with reason). Plus a **block-level** verdict and an explicit ruling on **`[AMD-69]`** (confirm-deferral vs re-open OQ-15-3 now). Re-derive every source shape independently and state the commit you verified at. Flag any place an amendment's prose disagrees with source at `6c6dd33` or with Locked Doc 15.

## Guardrails for the reviewer

- **Locked Doc 15 is inviolate.** If any amendment would require a Doc 15 change, say so and STOP that amendment — do not fold a Doc 15 edit. (AMD-69 is the deferral that keeps it inviolate.)
- These six amendments are all **below the AMD-87 watermark** (reserved slots) — ratification fills reserved-below-watermark slots and does **not** raise the ceiling.

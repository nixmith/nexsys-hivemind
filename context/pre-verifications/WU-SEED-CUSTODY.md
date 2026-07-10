<!--
file: context/pre-verifications/WU-SEED-CUSTODY.md
purpose: Pre-verification artifact for the seed-custody WU (SD-5) — every load-bearing source signature verified at core HEAD 04f5f70 (agent grounding survey + hub-L2 spot-checks, 2026-07-10, v27 beat 3). The Coder reads this BEFORE executing; the instruction cites it. Re-verify signatures at dispatch if HEAD moved.
audience: PM (authoring), Coder (pre-execution read).
state-type: pre-verification (point-in-time at 04f5f70).
status: CURRENT — verified 2026-07-10.
-->

# WU-SEED-CUSTODY — Pre-Verification (at core `04f5f70`)

## 1. The current posture (verified signatures)

- **The well-known key constant:** `EzspCoordinatorProtocol` `:380-384` — `private static final byte[] TC_LINK_KEY = {0x5A, 0x69, ...}` ("ZigBeeAlliance09", §3.13 step 5). Exactly TWO byte-consuming use sites.
- **Use site 1 — formation security struct:** `encodeInitialSecurityState(byte[] networkKey)` `:2035-2048` — 43-byte struct; `TC_LINK_KEY → struct[2..17]` (`:2043`); network key → `struct[18..33]`; bitmask LE at `[0..1]`. Sole consumer: `EzspOps.formNetwork` `:1963-1970` via `FRAME_SET_INITIAL_SECURITY_STATE = 0x0068` (`:109`) — the ONLY setInitialSecurityState call in the file.
- **Use site 2 — the per-window transient key:** `enablePreconfiguredKeyJoins()` `:996-1018` — wildcard-partner `IMPORT_TRANSIENT_KEY` carrying `TC_LINK_KEY` (`:1008-1014`); javadoc `:976-983` = the SD-5 join-side realization; "a watchdog reopen never re-runs it (reopen ≠ boot)".
- **The bitmask:** `INITIAL_SECURITY_BITMASK = 0x1B84` (`:379`) — javadoc `:359-377` carries the v18 beat-2 election VERBATIM in source, incl. the one-constant 0x1B04 fallback clause and the bellows note ("bellows supplies a GENERATED random seed under `use_hashed_tclk`").
- **Resume (NVRAM) writes NO key material:** `resumeFromNvram()` `:1982-1998` = `FRAME_NETWORK_INIT` (0x0017) only. `startSession()`/`configureNcp()` `:469-579` — "No key material is involved (INV-SE-03 trivially holds)" (`:542`).
- **Restore re-forms THROUGH use site 1:** `NetworkFormation.resume()` `:228-270` — `!restored` ⇒ `loadNetworkKey(...).orElseThrow` (`:234-239`, the `zigbee.network_key_missing` PIE) → WARN `zigbee.network_restored_from_parameters` (`:240-242`) → `ops.formNetwork(stored…, key)` (`:243-244`).
- **TC policy family:** `POLICY_TC_KEY_REQUEST = 0x05` (`:184`, the M9.4-KEY correction) + `DECISION_ALLOW_TC_KEY_REQUESTS = 0x51` (`:203`) — javadoc `:200-202`: "With hashed-TCLK formation the send-current path is the reference behavior". ZERO constant changes owed by this WU.

## 2. Custody layout (verified)

- **Seam contract:** `NetworkParameterStore` `:13-18` — INV-SE-03 binding: key material only via `SecureRandom → store → coordinator security state at formation`; never logged/serialized/toString'd. Methods `:43-68`: `load/save/saveNetworkKey/loadNetworkKey`.
- **Two-surface split:** `PersistentNetworkParameterStore` `:27-38` — params (channel/panId/extendedPanId/`networkKeyRef`, NO version field) as atomic-write JSON `zigbee-network.json` (`:58`, write `:113-122`, read `:94-98`); key material hex-inside-`SecretStore` under `zigbee.network_key.<keyRef>` (`:61`, write `:143` via single `set()`, read `:147-154`), in the zigbee-data-dir's OWN store instance (`:82-83` — `.root-key`/`scope_keys.json`/`secrets.enc`, zero sharing with the config-dir store). Corrupt-custody honesty: params-present-key-missing = PERMANENT, never silent re-form (`:41-47`, `:99-107`).
- **Crypto substrate:** `SecretStore` = AES-256-GCM at rest; **`setAll(Map)` `:58-74` = the AMD-68 atomic multi-secret write (never-torn)**. `ScopeKeyManager`: root 256-bit SecureRandom at `.root-key` (0400, atomic create `StandardScopeKeyManager:442-479`); scope KEK = HKDF-SHA256 (`:382-392`); DEK wrapped per scope (`:342-360`); secrets ride the random-IV path (`:181-202`). The counter-nonce durable-high-water machinery (`:580-667`, OR-M6-NONCE) EXISTS — the future FRAME-CTR row reuses it, this WU does not touch it.
- **Formation ordering doctrine:** `NetworkFormation` `:27-30` — key durable BEFORE `ops.formNetwork`; params saved only AFTER formation succeeds. The mint idiom: `:202-208` (`loadNetworkKey(...).orElseGet(mint-and-save)`); injectable `SecureRandom` ctor `:146-151`; `NETWORK_KEY_REF = "zigbee.network_key"` (`:66`).

## 3. Module-info impact: ZERO new edges (verified)

`integration-zigbee` module-info (MODULE_CONTEXT `:37-44` verbatim): requires transitive `com.homesynapse.integration`; jSerialComm, slf4j, jackson.databind plain; exports `com.homesynapse.integration.zigbee`. **No `requires com.homesynapse.config` and none needed** — `PersistentNetworkParameterStore` already imports `com.homesynapse.config.{SecretStore,ScopeKeyManager}` through integration-api's `requires transitive` chain (MODULE_CONTEXT `:150`; the M9.4b precedent, zero module-info diff). **The config module is G3-FROZEN (`StandardScopeKeyManager:58-60`) — this WU lands adapter-side only, config untouched.**

## 4. The SD-5 records of record (verbatim pointers)

- v21 beat-1 routing ruling + Nick's delegation verbatim ("*I want you to think carefully and strategically about this then decide/execute for yourself how we route it.*") + the HARD GATE ("no non-bench network forms until the seed-custody WU lands") + the ruled WU shape ("§5.5 `PersistentNetworkParameterStore` custody + a `CoordinatorOps` seam widening"; templates = the M9.4b instruction + WU-M9.4 §F–§G): `context/handoff/archive/pm-handoff-beats-rotated-2026-07-07.md:41`.
- The bench-is-the-sanctioned-exception line: same file `:27`. The v20 beat-2 R1 (bellows generated-seed consequence: "per-device TCLKs derivable from the public root; join semantics exercised, no key secrecy added"): `:63-65`.
- v18 beat-2 election verbatim: IN SOURCE at `EzspCoordinatorProtocol:368-373`. TCJ security framing: the TCJ instruction frontmatter `:7`.

## 5. Migration facts (for the DP)

The code is SILENT on re-keying an established network (no key-update/switch-key frames in the inventory `:98-238`; setInitialSecurityState reachable only via formNetwork). NVRAM-resume ignores custody entirely. ⇒ Option (i) seed-on-new-formations-only is code-consistent (requires absent-seed-⇒-well-known custody semantics so the RESTORE branch reproduces AS-FORMED); option (ii) = operator custody-delete + re-pair (fresh formation happens only on a genuinely absent params file, `PersistentNetworkParameterStore:88-89`).

## 6. Known-stale note

MODULE_CONTEXT `:279` still carries the M9.2-era "bitmask = 0x1B04 / hashed deferred" gotcha — superseded by the M9.4b delta (`:393`) and source `:379`. The WUCP-P1 update for this WU corrects that row.

## 7. Test seams (verified available)

Deterministic-`SecureRandom` ctor (`NetworkFormation:146-151`) · fake `CoordinatorOps` capturing formNetwork args · FakeNcp byte-assert of the 0x0068 struct (seed@2..17 / netkey@18..33 / bitmask LE 0x1B84) · real-tempdir custody round-trip · pre-seed custody file still loads (migration tolerance) · restore-carries-seed leg (scripted not-joined `networkInit` → assert the re-form struct) · INV-SE-03 both-casings hex sweeps (the M9.4b/H5 precedent) · ordering assert (seed durable before the form frame). NOT provable pre-silicon: a real Z3.0 join + TCLK update under a generated seed (the 0x06→0x34 arc) — the post-soak silicon leg; runs in Monday's pinned order.

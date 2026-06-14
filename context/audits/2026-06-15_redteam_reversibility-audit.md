<!--
file: context/audits/2026-06-15_redteam_reversibility-audit.md
purpose: Track-3 ADVERSARIAL RED-TEAM & REVERSIBILITY AUDIT of the recent decisions (R-α dispositions, the M7 AMD-88..93 block incl. AMD-92 FLATTEN, the crypto posture, the encrypted-scope set). The job is to BREAK these, not validate them — to surface one-way / irreversible / locks-soon choices being baked in on momentum before app-bootstrap propagates them. Output: a reversibility ledger + per-one-way-door adversarial verdict + echo-chamber meta-check + the named independent-validation brief.
audience: Nick, PM, the Track-2 app-bootstrap charter session
state-type: audit (adversarial, one-shot)
status: COMPLETE 2026-06-15
review-baseline: core HEAD 1eddd9a (M6 COMPLETE 4-of-4, M6.3 committed-GREEN but INERT — main() is a stub); watermark AMD-93; invariants 163/47; projectionVersion 5; Doc 15 LOCKED. Static read-and-reason — Cowork cannot run Gradle; sandbox git quarantined; host Read/Grep authoritative.
inputs: 2026-06-15_Research_R-alpha_PM_Assessment.md (grade A) + the raw return (Prior-Art Survey, REC-216..235) · 2026-06-15_core-review_CONVERGE_synthesis.md · Doc 15 §3.3/§3.4/§4.1/§5/§6/§16 + the V005 migration + EncryptedPayload/PayloadCipher source · AMD-88/89/91/92/93 · OQ-15-2 disposition. External: NIST CSRC SP 800-38D Rev.1 second pre-draft (web-verified this session).
-->

# Track 3 — Red-Team & Reversibility Audit

**Stance: adversarial.** Every recent decision is treated as a *claim under test*. Success = the number of genuine one-way / costly-to-reverse risks surfaced before app-bootstrap locks them, not confirmation of the plan. "A" grades and "M7 READY" are hypotheses, not ground. The most valuable single output this session is catching **one** reverse-now-while-cheap decision — and there is one (Finding F1, the AEAD/envelope version discriminator), plus one pause (F2, encrypted-scope width).

**Freshness preflight (review lens): PASS-for-review.** Baseline `1eddd9a` matches the CONVERGE and R-α assessment baselines; the one known staleness (PROJECT_SNAPSHOT masthead M6.3-uncommitted) is framework-pre-cleared. This is a read-only review; drift is captured, nothing is mutated. Source round-trip spot-checks held: the envelope columns (`payload_iv` BLOB / `dek_ref` TEXT, V005), `EncryptedPayload(ciphertext, iv, keyVersion)`, the chain canonicalization field list (Doc 15 §3.3), AMD-92 FLATTEN, and the zero-production-publish attestation all resolve in source as cited.

---

## 0. Headline (stands alone)

**The plan is mostly sound and mostly two-way. The crypto envelope is the exception — and it locks at the same instant everything else does.**

Of ~19 consequential recent decisions, **most are two-way doors** and earn a quick "fine, reversible." The genuinely one-way, locks-soon cells cluster in exactly one place: the **at-rest encryption envelope**, which becomes permanent the moment app-bootstrap activates `payloadCipher` and the first sensitive-PII row is written. Three envelope-level decisions are cheap to set now (corpus empty) and expensive-to-awkward later (immutable log + hash chain):

1. **F1 — the AEAD/envelope has NO algorithm or version discriminator (flagship).** `payload` + `payload_iv` + `dek_ref` (`scope_id:key_version`). `dek_ref` carries a *key* version, never an *algorithm* version. AES-256-GCM is implicitly hardcoded. The R-α/Doc 15 deferral of GCM-SIV-the-algorithm to Tier-2 is correct and evidence-backed — **but it answered the wrong question.** Deferring the *algorithm* is fine; shipping with no *agility mechanism* is the one-way door. Verdict: **REVERSE-NOW-WHILE-CHEAP (narrow)** — reserve a 1-byte AEAD/version tag in the envelope before first write. Independent-validation brief authored (R-γ).
2. **F2 — `encrypted_scopes = [identity, presence_personal]` may be too NARROW.** Verdict: **PAUSE-FOR-EVIDENCE** (the energy/erasure interviews) — with a bias the disposition does not state: on a one-way door whose reverse-cost is *irreversible* (plaintext PII can never be retro-encrypted or shredded) and whose forward-cost is *measured-trivial* (≤0.12% of one core), the default under uncertainty should be to **over-encrypt**, not under-encrypt.
3. **F3 — C6 (per-scope nonce-construction is unbound) rides the same lock.** Random-IV `encrypt()` and counter-nonce `encryptPayload()` resolve the *same* per-scope DEK (NIST SP 800-38D §8.3 anti-pattern). Which construction a scope used is implicit in its ciphertext forever. Bind each scope to exactly one construction **before first write**. The CONVERGE already flagged this MED (C6); this audit re-ranks it to *app-bootstrap-gating* because it shares F1's lock-time.

**These three are not independent items to schedule whenever — they are a single forcing function on the Track-2 app-bootstrap charter: the envelope's self-describing bytes must be finalized before the cipher is switched on, because that switch is the one-way door.** Everything else (the whole M7 AMD block, AMD-92 FLATTEN, RunCausalChain, rotate-DEK-on-restore, the NEW-1 read contract) is either two-way now or has a designed zero-migration escape — verdicts below.

**One cross-cutting correctness flag (F4, not a reversibility item but load-bearing for two of the verdicts):** `chain_hash` is **all-ZERO / not yet computed** at HEAD (CONVERGE reserved register; Doc 01 §14 "not implemented"). The NEW-1 cause-discrimination safety argument — and the R-α "tombstone un-forgeability reduces to breaking the chain" defense — **assume a live, verified chain that does not exist yet.** The brief, the return, and the grade-A assessment all reason as if it were live. This is the echo chamber's shared blind spot (§4).

---

## 1. The reversibility ledger

Every consequential decision made or queued in roughly the last two weeks. **Door** = one-way (hard/impossible to reverse) vs two-way (cheaply reversible). **Cost-to-reverse** with the *why*. **Locks** = when the door actually shuts. Rows are ordered by scrutiny priority (one-way + locks-soon first). Two-way rows get a one-line clear.

| # | Decision | Door | Cost-to-reverse (why) | Locks when | Verdict |
|---|---|---|---|---|---|
| **F1** | **AEAD = AES-256-GCM, envelope carries NO algorithm/version tag** (`payload_iv`/`dek_ref`; `dek_ref`=`scope_id:key_version`, a KEY not an ALGORITHM version) | **one-way (cleanly); two-way only via an awkward implicit-v1 retrofit** | **Costly.** Re-encrypting the corpus to change AEAD is impossible once the chain is live (it mutates `stored_payload_bytes` → breaks `chain_hash[n]`+all successors, Doc 15 §5). The only forward path is "tag new rows, treat tagless as GCM-v1" — which works but is a discipline-dependent landmine and overloads the already-fragile `:`-split `dek_ref`. Adding the tag **now** is ~1 byte/row, free. | **at-first-corpus-write = app-bootstrap** | **REVERSE-NOW-WHILE-CHEAP (narrow): add a discriminator before app-bootstrap.** §3.1 |
| **F2** | `encrypted_scopes = [identity, presence_personal]`; everything else plaintext-at-rest | **one-way per scope** | **Effectively irreversible.** A row written plaintext can never be retro-encrypted (immutable log) nor crypto-shredded (no per-scope key) — confidentiality + erasure are foreclosed for that corpus. A row written encrypted costs only perf to "undo" and you keep the key. **Asymmetric.** | **at-first-corpus-write = app-bootstrap** | **PAUSE-FOR-EVIDENCE (interviews) + over-encrypt bias.** §3.2 |
| **F3** | C6: per-scope nonce construction unbound — random-IV `encrypt()` + counter-nonce `encryptPayload()` share one DEK | **one-way once a scope has written under a construction** | **Costly.** NIST SP 800-38D §8.3 forbids both constructions under one key; which a scope used is implicit in its ciphertext permanently. Binding now = a guard/namespace, cheap. | **at-first-corpus-write = app-bootstrap** | **RESOLVE-NOW-WHILE-CHEAP (bundle with F1).** §3.3 |
| **F5** | NEW-1 cause-discriminated read contract — CASE-b fail-closed (app-bootstrap), CASE-a degrade+tombstone (crypto-shred WU, post-MVP) | **two-way (the regret-prone half is deferred & revisable)** | **Cheap.** The MVP footprint ≈ flat fail-closed (which is the prompt's proposed safe alternative). No per-row tombstone wire format is written at MVP; the cause-carrying `DegradedEvent` + tombstone ship with the (post-MVP) shred op and are design intent, not code. | fail-closed at app-bootstrap; tombstone wire-format at crypto-shred WU | **PROCEED** — with a sequencing gate (depends on F4 live chain) + a tombstone-granularity note. §3.4 |
| **F6** | rotate-DEK-on-restore = BINDING; carry-high-water-mark demoted to cross-check (Doc 15 §6 currency amendment — **escalated, NOT yet ratified**) | **two-way (design only; backup/restore unbuilt — F3 foundation-readiness)** | **Cheap.** No code exists; the backup/restore WU is unscoped. | at the backup/restore WU | **PROCEED** — with a REQUIRED clarification (rotate = additive new DEK version, retain priors; NOT re-encrypt/replace). §3.5 |
| **F7** | AMD-92 **FLATTEN** type-residency (`RunId`→`Ulid`, `RunStatus`→`String` in event payloads) | **two-way now (zero persisted); one-way at first automation publish** | **Cheap→near-zero.** FLATTEN-vs-typed barely changes the wire — typed ULID/enum wrappers serialize to the identical bytes — so relocation later is a zero-log-migration *code* change (the DOCS review confirmed this). The genuinely-foreclosed thing (richer `RunCausalChain` *in the payload*) is recoverable from the correlation-id trace graph. | at M7.1 first automation-event publish | **PROCEED** — the real one-way item is the per-event field SET (already CONVERGE C4), not FLATTEN. §3.6 |
| **F8** | AMD-88 new permits (Calendar/Reachability/Manual) + `triggerId` on every Tier-1 permit | **two-way (no evaluator exists; permits frozen pre-producer)** | **Cheap.** Breaking ctor change, but the construction-site sweep is "tests + the unbuilt M7.1 evaluator." `triggerId` *values* reach persisted `automation_triggered.matched_triggers` at M7.1 → the id *scheme* (ULID, unique-in-automation) semi-locks then. | shapes: first user YAML (post-launch); id scheme: M7.1 publish | **PROCEED.** §3.7 |
| **F9** | AMD-89 `SemanticTagSelector` + `includedRoles` PRIMARY-only default on group selectors (BREAKING) | **two-way** | **Cheap.** Selectors are YAML re-parsed every load — *zero* persisted serialized instances; sweep is Phase-2 tests/fixtures. PRIMARY-default behavioral contract locks only when users author definitions. | first user YAML (post-launch) | **PROCEED.** §3.7 |
| **F10** | AMD-91 `RunCausalChain` replaces `cascadeDepth:int` on `RunContext` (supersedes AMD-04) | **two-way** | **Cheap.** `RunContext` is in-memory, NEVER persisted; no production Run has executed. The supersession ledger was audited element-by-element (6/6). It *improves* determinism (chain-membership replaces windowed/evictable suppression) — a correctness win, not debt. | never (internal runtime type) | **PROCEED.** §3.7 |
| **F11** | D2: encrypt sensitive-PII on write from MVP (vs the research's defer-all-to-Tier-2) | **one-way** | **Irreversible by design** (Doc 15 §5 "the irreversible contract"). But this is the core privacy invariant (INV-PD-03) + future-shreddability rationale, and the now-or-never logic is correct. | at-first-corpus-write | **PROCEED** (the *width* is the live question — F2; the *principle* is sound). |
| **F12** | Counter-based deterministic 96-bit nonces, never random (Doc 15 §3.4) | **one-way (nonce discipline baked per scope)** | Irreversible per corpus, but NIST §8.2.1-correct; random would hit the birthday bound. | at-first-corpus-write | **PROCEED.** |
| **F13** | C8 write-path hardening: ctor fail-closed guard + treat nonce dir-fsync `IOException` as FATAL (today swallowed at DEBUG) | **two-way (code), but guards a one-way hazard** | **Cheap.** A swallowed dir-fsync failure on the nonce path can leave the high-water rename non-durable → post-crash nonce repeat → AES-GCM break. | behaviorally at first corpus write | **PROCEED — do before app-bootstrap** (cheap; bundle with F1/F3). |
| **F14** | Chain canonical-metadata format (13 fixed fields, length-prefixed BE binary; format version in genesis) | **one-way at chain activation** | Has an agility mechanism (genesis-recorded version + dual-format verify) — the *right* pattern, and notably the one F1 lacks. Note: `payload_iv`/`dek_ref` are **not** chain-covered (only the 13 fields + `payload`). | at chain activation | **PROCEED** (note the IV/dek_ref coverage gap → feeds R-γ). |
| **F15** | `chain_hash` left all-ZERO / uncomputed at HEAD | n/a (a *state*, not a decision) | — | — | **FLAG (F4):** NEW-1 + tombstone safety assume this is live. §3.4/§4. |
| **F16** | Machine-local root key at MVP (passphrase/TPM = Tier-2) | **two-way** | **Cheap.** Schema + key hierarchy identical across MVP/Tier-2; only root-key *acquisition* changes — non-breaking upgrade (OQ-15-1/3). | never | **PROCEED.** |
| **F17** | `projectionVersion` stays 5 across M6.3 (additive columns) | **two-way** | Additive `ALTER TABLE ADD COLUMN`, backfill-free. | — | **PROCEED.** |
| **F18** | "M7 READY" + app-bootstrap as a combined gate carrying C1(auth)+C2(read-contract)+C9(lifecycle) | **two-way (process/sequencing)** | Re-reviewable; nothing built. | — | **PROCEED** — but app-bootstrap is *also* where F1/F2/F3 lock, so the charter must carry them too (§5). |
| **F19** | Pipeline self-grading (same authors briefed, ran, graded R-α "A"; adopted frictionlessly) | n/a (meta) | — | — | **See §4 echo-chamber check.** |

**Read of the ledger:** the scrutiny budget belongs to **F1, F2, F3** (one-way, lock at app-bootstrap) and the **F4 chain-liveness** cross-dependency. F5–F19 are either two-way or have designed escapes; the verdicts below show the work for each one-way door and for the two highest-value two-way doors the prompt named.

---

## 2. Ranked "re-examine before it propagates" list

1. **F1 — AEAD/envelope version discriminator.** Reserve a 1-byte algorithm/version tag in the envelope before app-bootstrap. **Gates the Track-2 app-bootstrap charter.** Dispatch the R-γ challenge brief (§6) to independently pressure-test the "implicit-v1 is a safe escape" claim before committing.
2. **F2 — encrypted-scope width.** The energy/erasure interviews (entry-gate row 3) must explicitly resolve scope WIDTH, not just energy, *before* the cipher activates. Default-to-encrypt under uncertainty. **Gates the charter** (shares the lock).
3. **F3 — bind per-scope nonce construction (C6).** Re-ranked from CONVERGE-MED to charter-gating because it locks at first write. Bundle with F1/F13 as "finalize the envelope bytes."
4. **F4 — chain liveness vs NEW-1.** Do not enable the CASE-a degrade path (or the tombstone) until `chain_hash` computation + mandatory startup verification are live and tested. Add as an explicit ordering invariant on the crypto-shred WU.
5. **F6 — rotate-DEK-on-restore semantics.** Before the Doc 15 §6 amendment is ratified, pin "rotate = additive new DEK version, priors retained" in the amendment text — the current wording is mis-implementable into either a chain break or silent data loss.

Everything below #5 is a confirmed two-way door; the honest, expected outcome is that the bulk of the plan proceeds.

---

## 3. Per-decision adversarial verdicts (one-way doors + the named suspects)

Discipline: steelman the *opposite* choice; name the failure mode advocates under-weight; state the disconfirming evidence sought; verdict. For a one-way door, PROCEED must cite what was tried to disprove it.

### 3.1 F1 — Crypto-agility / AES-256-GCM vs the missing version tag (FLAGSHIP)

**The decision under test.** Doc 15 + R-α encrypt sensitive-PII under AES-256-GCM and park GCM-SIV / committing-AEAD as "Tier-2." The envelope is `payload` (ciphertext+tag), `payload_iv` BLOB(12), `dek_ref` TEXT = `scope_id:key_version`. **Source-confirmed: there is no algorithm or envelope-version field anywhere — not in the payload columns, not in `scope_keys` (whose `encrypted_dek` wrap is itself hardcoded AES-256-GCM).** The AEAD is implicit.

**Steelman of the opposite (ship an explicit discriminator now).** Every serious at-rest AEAD format carries an algorithm/version identifier precisely so the algorithm can change without re-encrypting the corpus: JWE `alg`/`enc`, COSE, Tink keysets, the AWS Encryption SDK message-format version, age, GPG packet version, Fernet's leading `0x80` version byte. The reason is universal: **ciphertext outlives algorithms.** HomeSynapse's corpus is an *immutable, hash-chained* log — the most extreme version of "ciphertext you can never rewrite." The cost of a discriminator now is ~1 byte/row on an empty corpus; the cost later is that re-encryption is *impossible* (it mutates `stored_payload_bytes` → breaks `chain_hash`, Doc 15 §5), so agility must be retrofitted by convention onto a live chain.

**The failure mode the current choice under-weights.** The R-α pipeline conflated two different questions and only answered one:
- *"Should we adopt GCM-SIV now?"* → No (correct: RFC 8452 is Informational, two-pass, **not FIPS-validatable** — web-confirmed current as of Nov 2025).
- *"Should we be able to adopt a different AEAD later without rewriting the corpus?"* → **never asked.** The agility *mechanism* (a version tag) is orthogonal to the algorithm *choice*. You defer the algorithm precisely *because* the landscape is unsettled — which is exactly the condition under which you want the mechanism. And the landscape is provably unsettled: **NIST issued a second pre-draft for SP 800-38D Rev.1 in June 2026 proposing `wGCM` (Rijndael-256, 256-bit block) plus nonce-derivation modes (AES-XGCM, DNDK-GCM, XAES-256-GCM), comment period open through 31 Jul 2026** (web-verified — this also *discharges* the assessment's flagged-unverified "wGCM" item: it is real). A successor mode landing in the corpus's multi-year lifetime is not speculative.

**The specific evidence that would change the call (and what I found when I sought it).** I tried to disprove "this is a one-way door" by finding a cheap later-retrofit:
- *Disconfirming evidence found (partial):* the chain does **not** cover `payload_iv`/`dek_ref` (only the 13 metadata fields + `payload`, Doc 15 §3.3). And SQLite `ALTER TABLE ADD COLUMN` is additive/backfill-free (V005 proves it). So you *can* add a `payload_alg` column later and adopt the convention "NULL ⇒ AES-256-GCM v1, present ⇒ named." Old rows stay readable; chain unbroken. **This means the door is two-way, not impossible — I will not overclaim it as irreversible.**
- *Why the hedge still wins despite that:* the implicit-v1 escape is (a) discipline-dependent (it silently fails if anyone ever writes a second algorithm *without* a tag), (b) forces a future migration of an immutable log under the worst conditions (corpus large, chain live), and (c) overloads the `dek_ref` `:`-split that the CONVERGE *already* flagged as fragile (colon-in-scope-id `NumberFormatException`). A 1-byte tag now removes all three for ~nothing.

**Verdict: REVERSE-NOW-WHILE-CHEAP (narrow).** Add an explicit AEAD/version discriminator to the envelope (a `payload_alg`/`envelope_version` column, or a 1-byte prefix on the ciphertext/IV) **before app-bootstrap activates `payloadCipher`.** This is *not* a five-alarm "the door is irreversible" claim — it is the calibrated one: the underlying door is two-way, but the asymmetry (free now vs. immutable-log migration later) and the live NIST flux make the cheap hedge the right call, and it should be **decided explicitly rather than defaulted-by-omission.** The broader encrypt-on-write decision (F11) is PROCEED. Because internal red-teaming is structurally insufficient here (we designed this envelope), this warrants the independent-validation brief (§6, R-γ).

### 3.2 F2 — The `encrypted_scopes` set `[identity, presence_personal]`

**The decision under test.** OQ-15-2 fixed the MVP encrypted set to `[identity, presence_personal]`; energy and all other categories stay plaintext-at-rest. The disposition is evidence-backed *for what it measured*: the Pi-4 microbench shows 13–37× gate margins, and energy was kept plaintext on **PII-classification** grounds (INV-PD-03), explicitly *not* perf (perf would not have forced it out — 3.5–19 µs/event is trivial).

**Steelman of the opposite (encrypt a wider set at MVP).** The one-way door here is per-scope and asymmetric. A row written **plaintext** can never be retro-encrypted (immutable log) and can never be crypto-shredded (no per-scope key exists for it) — so confidentiality *and* the GDPR-aligned erasure story are permanently foreclosed for every plaintext row. A row written **encrypted** that "didn't need it" costs only a measured ≤0.12% of one core, and you retain the key so it stays readable. When a one-way door has an *irreversible* downside on one side and a *trivial, measured* cost on the other, the rational default under uncertainty is the reversible side: **encrypt.**

**The failure mode the current choice under-weights.** Classifying "what is PII" is a *judgment made before the user research that bears on it has returned.* Energy/occupancy patterns are a well-known re-identification and presence-inference vector; the energy/erasure interviews (entry-gate row 3) exist precisely to resolve this — yet the scope set was fixed ahead of them. If the interviews reveal energy (or another category) *is* erasure-sensitive, every plaintext row written between app-bootstrap and that finding is permanently un-shreddable. The disposition treats `[identity, presence_personal]` as "the expected-case outcome, Doc 15 needs no edit" — a momentum framing for a one-way door.

**The specific evidence that would change the call.** The energy/erasure interview returns (do users expect to be able to *erase* energy/occupancy history? is it experienced as sensitive?). The note in the prompt is correct that these interviews "bear on widening" — so this is a flag, not a pre-emption.

**Verdict: PAUSE-FOR-EVIDENCE.** Hold the width question open until the interviews return, and **make scope-WIDTH (not just energy) an explicit interview output that gates app-bootstrap.** Register the asymmetry as the decision rule: *on this one-way door, the default under uncertainty is to encrypt* — so the burden is on keeping a plausibly-PII category plaintext, not on adding it. `[identity, presence_personal]` is defensible as a floor; it is **not** safe as a ceiling decided before the evidence.

### 3.3 F3 — C6: per-scope nonce construction is unbound (re-ranked to charter-gating)

**The decision under test.** `StandardScopeKeyManager.encrypt()` (random 96-bit IV) and `encryptPayload()` (deterministic counter nonce) resolve the **same** per-scope DEK; nothing binds a scope to one construction. The CONVERGE flagged this MED (C6), citing NIST SP 800-38D §8.3: the deterministic and RBG-based constructions **shall not both be used** under one key.

**Why it belongs in this audit (not just the CONVERGE backlog).** It is a one-way door with the *same lock-time as F1*: which construction a scope used is implicit in its ciphertext, permanently, from the first encrypted write. Fixing it after rows exist means you can never be sure a given scope didn't mix constructions. Fixing it now is a guard or a namespace — cheap.

**Steelman of "leave it, it's safe by disjointness."** In production today the scopes that use `encryptPayload` (`identity`, `presence_personal`) are disjoint from any `encrypt` caller, so no single DEK actually sees both. **Disconfirming evidence:** that disjointness is *unenforced* — a future identity-bearing secret or a config change could route an `encrypt` call to a scope already using counter nonces, and nothing stops it. The `fence_randomIvPathUnchanged` test even exercises *both* on scope `identity`. Unenforced safety on a catastrophic crypto invariant, locking at first write, is exactly the momentum pattern this audit hunts.

**Verdict: RESOLVE-NOW-WHILE-CHEAP.** Bind each scope to exactly one nonce strategy (namespace the scope-id, or guard `encrypt`/`encryptPayload` to reject a scope that has issued the other), encode it as an enforced invariant + the NIST citation in Doc 15 §3.4, before app-bootstrap. **Bundle F1 + F3 + F13 into one "finalize the envelope" beat on the app-bootstrap charter** — they share a lock-time and all three are cheap-now/irreversible-later.

### 3.4 F5 — NEW-1 cause-discriminated read contract + shred tombstone

**The prompt's attack:** is NEW-1 solving a post-MVP problem prematurely and committing us to a contract (degrade-on-shred + tombstone event type + cause-carrying `DegradedEvent`) we might regret? Would flat fail-closed at MVP be lower-regret?

**What is actually locked at MVP (the disconfirming evidence).** The R-α disposition **splits** the contract: CASE-b (unintended unreadability) → **fail-closed**, routed to app-bootstrap; CASE-a (intended shred) → **degrade + tombstone**, routed to the crypto-shred WU which is **post-MVP**. So the MVP footprint is *fail-closed on any decrypt failure* — which **is** the prompt's proposed "flat fail-closed at MVP." No per-row tombstone wire format and no cause-carrying `DegradedEvent` are written at MVP; those are design *intent* for a future WU, not code, and are cheaply revisable. The prompt's regret concern is therefore largely **already addressed by the split** — the regret-prone machinery is deferred, and the thing locked now is the conservative option.

**Attacking the tombstone un-forgeability claim harder than the return did.** R-α (REC-232) argues forging an "intended" signal reduces to breaking the chain. Two cracks I pushed on:
- **Granularity.** The proposed tombstone records `(scope, timestamp, reason)` — **no `key_version`.** Scopes are versioned (`scope_id:key_version`); a scope-level tombstone could wrongly degrade rows written under a *still-valid* later version (e.g., post-rotation, post-restore per F6). The decision rule and the tombstone must key on `(scope, key_version)`, not scope alone. Hand this to the crypto-shred WU.
- **The load-bearing dependency is not live (F4).** The entire argument rests on `chain_hash` being computed and startup-verified. **It is all-ZERO at HEAD.** Until chain computation + mandatory verification ship, "decrypt-impossible while chain validates" is vacuous — there is no real chain to break, so the un-forgeability defense is not yet operational. The MVP *fail-closed* half is safe without the chain (it just fails closed on any decrypt failure); the *degrade* half is **not** — it must not be enabled until the chain is live. The return's own caveat says exactly this ("the design is only as strong as the chain_hash's independence... if violated, flat fail-closed becomes mandatory") but neither it nor the assessment noticed the chain isn't computed yet.

**Verdict: PROCEED** on the MVP fail-closed half (it equals the safe alternative; low lock risk). For the deferred half, attach two gates to the crypto-shred WU: **(a) sequencing — degrade/tombstone must not ship before `chain_hash` is live + startup-verified (F4); (b) granularity — tombstone and the read-side decision rule key on `(scope, key_version)`.** These cost nothing now and prevent a real future foot-gun.

### 3.5 F6 — rotate-DEK-on-restore as binding

**The prompt's attack:** does re-wrapping or re-encrypting old ciphertext on restore touch stored bytes and break `chain_hash` (§5)? If rotate-on-restore implies re-encryption, "chain stays valid through key change" may not hold.

**What "rotate" actually means (disconfirming the chain-break worry).** The raw return is explicit (REC-220 / Stage-1.1): *"mint a fresh per-scope DEK (re-wrapped under the scope KEK) before resuming any encryption in that scope... makes the restored counter value irrelevant."* This is **mint-a-new-DEK-for-future-writes**, not re-encrypt-existing-payloads. Existing ciphertext stays under its old DEK/`key_version`; only *new* post-restore writes use the new version (fresh counter from 0, no collision possible with the old version's used nonces). Therefore:
- It does **not** touch any event `stored_payload_bytes` → `chain_hash` is unaffected. The prompt's worry is based on the re-encryption reading, which is **not** what is meant.
- Even *re-wrapping the DEK* (changing `scope_keys.encrypted_dek`) touches only the `scope_keys` table, which is **not chain-covered** at all — so re-wrap is also chain-safe. Only re-encrypting *payloads* would break the chain, and nobody proposes that.

**The failure mode that IS real (and under-specified).** "Rotate" = **additive** new `key_version`. The old version's row **must be retained** so pre-restore ciphertext stays decryptable. If a Coder implements "rotate" as *replace/overwrite the scope's DEK*, every pre-restore encrypted row becomes permanently unreadable — silent data loss dressed as a key rotation. The return and assessment never state "retain priors" explicitly; the ambiguity is exactly the failure the prompt smelled, just on the *opposite* axis from the one it guessed (data loss, not chain break).

**Verdict: PROCEED** (the binding call is sound and chain-safe). **REQUIRED before the Doc 15 §6 amendment ratifies:** the amendment text must pin "rotate-on-restore = mint an *additive* new DEK version (new `scope_keys` row), retaining all prior versions; it does NOT re-encrypt payloads and does NOT replace prior versions." This closes both mis-implementations (chain break from re-encrypt; data loss from replace) at zero cost while the feature is still on paper.

### 3.6 F7 — AMD-92 FLATTEN type-residency

**The prompt's attack:** once events persist flattened (`RunId`→`Ulid`, `RunStatus`→`String`), the wire format is permanent. Is FLATTEN right, or does it foreclose a future need (e.g., richer run lineage in payloads)?

**Steelman of the opposite (keep typed `RunId`/`RunStatus`; relocate them to a shared module).** Typed payload fields preserve compile-time safety and let a future "richer lineage" need embed structured types directly.

**Why FLATTEN survives the attack (disconfirming evidence).**
- **The wire is nearly identical either way.** A typed `RunId` wraps a `Ulid` and serializes to the same ULID string; a `RunStatus` enum serializes to its `name()`. FLATTEN-vs-typed is therefore a *code-level* distinction that does **not** change the on-disk bytes. The DOCS review states this directly: *"relocation stays available later with zero log migration."* So the feared permanence is real for the *bytes* but the FLATTEN choice barely touches the bytes — relocating to typed later is a code change, not a log migration.
- **The one genuinely-foreclosed thing is recoverable elsewhere.** Richer `RunCausalChain` structure in the payload is flattened to `int cascadeDepth` + `List<AutomationId> chain`. But the full lineage (per-hop EventIds, timestamps, the causal structure) is **query-assembled from `correlation_id`** (AMD-92 §2.4; trace is never materialized) — a *richer* form than any payload denormalization, always available. So FLATTEN does not actually lose lineage; it declines to denormalize it.
- **The architectural reason is sound.** Typed `RunId`/`RunStatus` in payloads forces `event → automation` — the exact AMD-52/E70-1 JPMS cycle that already forced the value-model relocation. Relocating `RunId` to `platform` to dodge that was correctly rejected (it is automation-internal by design). FLATTEN is the lower-coupling choice.

**Verdict: PROCEED.** The reversibility risk the prompt points at is real but **mis-located**: it is not "FLATTEN vs typed" (near-zero-migration) — it is the **specific flattened field SET of each automation event record, frozen at first publish.** That is the actual one-way door, and the CONVERGE already named it (C4: widen the placeholder records before any production publish; settle the design at M7.1 scoping). The standing carry: treat the M7.1 run-initiation payload field lists as the irreversible commitment and get them complete before the first publish.

### 3.7 F8/F9/F10 — The M7 breaking changes (AMD-88 `triggerId`, AMD-89 `includedRoles`, AMD-91 `RunCausalChain`)

**The prompt's attack:** any of these premature or irreversible *before M7.1 has even run*? Is "the construction-site sweep is empty" a reason they're safe, or a reason we're under-testing them?

**The honest answer: it's both, but the door is two-way, so "safe" dominates.**
- **Empty sweep = genuinely two-way.** All three are Phase-2 type/contract changes to **unbuilt** modules (the entire automation engine is in the reserved-but-unbuilt register). AMD-91's `RunContext` is **in-memory, never persisted** ("no production Run has ever executed") — purely internal, locks *never*. AMD-89's Selectors are **YAML re-parsed every load** — *zero* persisted serialized instances. AMD-88's permits freeze shapes before their producers exist. Reshaping any of them again before M7.1 costs "update the type + its tests."
- **The "under-testing" worry is legitimate but bounded.** Empty construction sites mean the new fields have no behavioral tests — we won't *know* the shapes are right until M7.1 builds against them, and a shape flaw could force a re-amendment. But because they're two-way (no persisted form, no users), a re-amendment at M7.1 is cheap. This is just normal Phase-2-then-Phase-3 discipline (freeze the interface, then let implementation test it).
- **The one place a breaking change reaches a persisted wire format:** AMD-88's `triggerId` flows into `automation_triggered.matched_triggers[]` (AMD-92 row 1), and AMD-89's role-filtering result flows into `resolved_targets`. So the *values* persist at M7.1 — but the persisted forms are a ULID string and a set of EntityIds, which are stable regardless of the surrounding type shapes. The id *scheme* (ULID, unique-within-automation) semi-locks at M7.1 publish, and it is reasonable.

**Verdict: PROCEED on all three** (two-way). AMD-91 is additionally a *correctness improvement* (deterministic chain-membership suppression replaces windowed/evictable state — INV-TO-02 alignment), not debt. The only carries: (i) the construction-site sweeps must actually run at M7.1/M7.2 issue (already on each AMD's checklist); (ii) settle the `triggerId` generation/stability contract before M7.1 publish since `matched_triggers` persists ids (folds into the F7/C4 "get the field set right before first publish" beat). The C3 doc-drift fix (RunContext Javadoc still cites superseded AMD-04) remains the cheap fix-first before M7.2 — already tracked by the CONVERGE.

---

## 4. Echo-chamber meta-check (is the pipeline rubber-stamping its own momentum?)

The same pipeline wrote the R-α brief, ran the survey, and graded it "A." Three tests: did the brief's framing steer the return? did "grade A" reward agreement? what load-bearing claim was adopted without independent verification?

**(a) The framing steered the question — and the steer is the flagship.** The brief framed the AEAD question as *"should we adopt GCM-SIV?"* (an algorithm choice). The return dutifully answered *"not yet, Tier-2"* (REC-222/223/230) and the assessment graded the reasoning highly. **Nobody asked the orthogonal, cheaper, more important question — "should the envelope be *agile*?"** The shared algorithm-choice frame is exactly the mechanism the prompt warns about: it produced confident closure on a question the pipeline never asked (F1). This is the clearest echo-chamber artifact in the set — not a wrong answer, a *missing* question, invisible from inside the frame.

**(b) "Grade A" measured research quality, not decision completeness.** The return genuinely steelmanned both extremes, used primary sources with verbatim quotes, and defeated the partitioning-oracle objection on HomeSynapse's own invariant — that is real quality, and I will not call the grade unearned. But the adoption was *frictionless*, and a high grade on a well-argued return created **false closure**: the one structural gap (envelope agility) went unnamed because the whole pipeline shared the frame, and the grade implicitly certified "this question is handled." Quality of argument ≠ completeness of the decision surface.

**(c) The load-bearing unverified assumption the echo chamber adopted: the chain is live.** The brief's QB-anchors, the return's REC-226/232 defense, and the assessment's "defeats the objection via the chain_hash invariant" **all reason as if `chain_hash` is computed and verified.** It is **all-ZERO / not implemented** at HEAD — `SqliteEventStore` binds the `ZERO_HASH` constant and its Javadoc states "actual hash computation is deferred to the crypto milestone" (CONVERGE reserved register confirms: "computation not built"). The blind spot is *systemic*, not just in the R-α artifacts: **Locked Doc 15 §4.1 itself asserts "for a fresh MVP install the chain is real from genesis"** — design intent written in the present tense — while the code binds the zero hash. So the obvious rebuttal ("but Doc 15 says the chain is real") is itself the echo: a governance doc reading as live what the code leaves inert. The return's own caveat even states the contract collapses if the chain invariant doesn't hold — yet none of the artifacts checked whether it holds *today*. Every layer assumed the load-bearing invariant is operational when it is unbuilt (F4).

**(d) The one item the assessment *did* flag as unverified — now resolved, and it cuts toward F1.** The assessment flagged the "June-2026 wGCM second-pre-draft" as past its knowledge horizon. **Web-verified this session: it is real** (NIST CSRC, second pre-draft for SP 800-38D Rev.1, wGCM/Rijndael-256 + nonce-derivation modes, comments through 31 Jul 2026). So: discharge the flag — and note that an *active NIST process toward a successor AEAD mode* is precisely the external condition that makes the F1 agility hedge worth its ~1 byte.

**Meta-conclusion.** The pipeline is high-quality and not cynically self-confirming — but it exhibits the predicted failure on two axes: a *framing* that foreclosed the cheaper question (F1), and a *shared assumption* (live chain) that no artifact verified (F4). Both are exactly what an internal, momentum-carrying review misses and an adversarial pass is for. That is the value this session adds; it is not manufactured.

---

## 5. What gates the Track-2 app-bootstrap charter

App-bootstrap is the convergence point: it activates `payloadCipher` (the one-way crypto doors F1/F2/F3/F11/F12 all lock here) **and** makes the CONVERGE HIGHs live (C1 auth, C2 read-contract) **and** reconciles lifecycle (C9). The charter must therefore carry, **as a first-class "finalize the envelope before the cipher switches on" gate:**

1. **F1 — decide the AEAD/envelope version discriminator** (add it, or record an explicit, written rationale for relying on implicit-v1). Do not let it be defaulted by omission. Pull the R-γ brief's return in before finalizing.
2. **F2 — the encrypted-scope WIDTH**, resolved by the energy/erasure interviews with a default-to-encrypt bias. The width must be set before first write, not after.
3. **F3 — bind each scope to one nonce construction** (C6); **F13 — the C8 write-path hardening** (fatal nonce dir-fsync + ctor guard). Both cheap, both lock at first write.
4. **F4 — chain liveness** ordering: the CASE-a degrade/tombstone path must not be wired until `chain_hash` computation + mandatory startup verification are live (the MVP fail-closed half does not need it).

The existing app-bootstrap load (C1+C2+C9) already makes it "a high-density latent-defect milestone" (CONVERGE Seam 1). This audit adds the envelope-finalization gate to that list. **None of F1–F4 is on the M7 critical path** — they sequence into app-bootstrap, which is independent of the M7.x build. M7.1 prep can proceed.

---

## 6. Independent-validation brief authored (deliverable 2)

**One brief warranted; named and authored.** Internal red-teaming is structurally insufficient for **F1** because *we designed the envelope* — the blind spot is endogenous (§4a). Authored and saved, dispatch-ready, framed adversarially (the reviewer is rewarded for finding the flaw, not confirming the deferral), with the standard quote-back/evidence discipline:

- **`context/instructions/2026-06-15_Research_R-gamma_Crypto-Agility_Envelope-Versioning_CHALLENGE_Brief.md`** — challenges F1: is shipping a non-self-describing AEAD envelope on an immutable hash-chained log defensible, or is a version/algorithm discriminator a now-or-never that must enter at app-bootstrap? It is told to *try to defeat* the "implicit-v1 is a safe escape" argument I built in §3.1, to survey how immutable/append-only encrypted stores version their envelopes, and to take a position against HomeSynapse's actual constraints.

**Why no second brief.** The other one-way doors do not warrant a fresh web brief: **F2 (scope width)** routes to Nick's energy/erasure *user interviews*, not web research — a DOCS brief is the wrong instrument. **F5 (cause-discrimination/tombstone)** was already the subject of R-α's deep primary-source survey; my additions (F4 chain-liveness, `(scope,key_version)` granularity) are *internal* sequencing/spec facts, not web-research questions — they route to the crypto-shred WU and the Doc 15 §6 amendment text, not a new survey. **F6** is a one-line amendment-text pin. Authoring more briefs would be motion, not validation.

---

## 7. Recommendation summary

- **REVERSE-NOW-WHILE-CHEAP:** F1 (envelope version discriminator) — narrow, before app-bootstrap; F3 (bind per-scope nonce construction). Bundle with F13 as "finalize the envelope bytes."
- **PAUSE-FOR-EVIDENCE:** F2 (encrypted-scope width) — gate on the interviews with a default-to-encrypt bias.
- **PROCEED with a required pin:** F5 (chain-liveness + `(scope,key_version)` gates on the crypto-shred WU); F6 (rotate = additive version, retain priors — pin in the §6 amendment text before ratification).
- **PROCEED, two-way, fine:** F7 FLATTEN, F8/F9/F10 the AMD-88/89/91 breaking changes, F11/F12/F14/F16/F17 the remaining crypto/schema decisions, F18 the M7-READY/app-bootstrap sequencing.
- **Dispatch:** the R-γ crypto-agility challenge brief (§6) to a fresh DOCS conversation; fold its return into the app-bootstrap charter's envelope-finalization gate.
- **Gates the Track-2 app-bootstrap charter:** F1, F2, F3, F4 (the "finalize the envelope before the cipher switches on" gate, §5).

**Net:** the plan is mostly two-way and proceeds. The session caught the one genuine reverse-now-while-cheap before app-bootstrap locks it (F1), re-ranked one CONVERGE-MED to charter-gating because it shares the lock (F3), surfaced one pause the disposition framed away (F2), and named the echo chamber's shared blind spot (F4 chain-liveness). We proceed knowing which doors are one-way, having tried to break the ones that don't reopen.

---

## Commit message (handed to Nick — `!`-free)

```
docs(audit): add Track-3 red-team reversibility audit

Adversarial reversibility audit of the recent decisions (R-alpha
dispositions, the M7 AMD-88..93 block incl. AMD-92 FLATTEN, the crypto
posture, the encrypted-scope set). Baseline core 1eddd9a (M6 4-of-4,
M6.3 committed but inert), watermark AMD-93. Read-only; no code, tests,
or governance files modified. Preflight PASS-for-review.

Ledger: ~19 consequential decisions classified by door-type, cost-to-
reverse, and lock-time. Most are two-way and proceed. The one-way,
locks-at-app-bootstrap cells cluster in the at-rest envelope:

- F1 (flagship, REVERSE-NOW-WHILE-CHEAP): the envelope carries no
  algorithm/version tag (payload_iv/dek_ref; dek_ref is a KEY not an
  ALGORITHM version) - AES-256-GCM is implicitly hardcoded. Deferring
  GCM-SIV the algorithm is correct (still not FIPS-approvable; NIST
  wGCM second pre-draft web-verified June 2026); shipping with no
  agility mechanism is the one-way door. Reserve a 1-byte discriminator
  before the cipher activates. Independent-validation brief authored
  (R-gamma, context/instructions/).
- F2 (PAUSE-FOR-EVIDENCE): encrypted_scopes [identity, presence_personal]
  may be too narrow; plaintext PII is irreversibly un-encryptable and
  un-shreddable while the encryption cost is measured-trivial - default
  to over-encrypt; gate width on the energy/erasure interviews.
- F3 (RESOLVE-NOW): C6 per-scope nonce construction unbound (NIST
  800-38D 8.3) re-ranked from CONVERGE-MED to charter-gating - shares
  F1's lock-time.
- F4 (FLAG): chain_hash is all-ZERO/uncomputed; the NEW-1 cause-
  discrimination + tombstone safety argument assumes a live chain the
  echo chamber (brief+return+grade-A assessment) never verified.

Two-way / PROCEED: AMD-92 FLATTEN (typed-vs-flat barely touches the
wire; lineage is correlation-assembled), AMD-88/89/91 breaking changes
(unbuilt modules, no persisted form), rotate-DEK-on-restore (additive
version, chain-safe - pin "retain priors" in the Doc 15 sec 6 amendment),
the NEW-1 MVP fail-closed half.

Gates the Track-2 app-bootstrap charter: F1/F2/F3/F4 as a "finalize the
envelope before payloadCipher switches on" gate. None on the M7 path.

File: context/audits/2026-06-15_redteam_reversibility-audit.md
```

---

*End of red-team reversibility audit. Companion deliverable: `context/instructions/2026-06-15_Research_R-gamma_Crypto-Agility_Envelope-Versioning_CHALLENGE_Brief.md`. No production code, tests, or governance files were modified.*

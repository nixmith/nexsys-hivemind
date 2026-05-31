<!--
file: context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md
purpose: P2 — the contiguous AMD allocation that unblocks authoring of the M4 critical-path amendments.
audience: Nick (ratify), PM, Coder
update-cadence: once (ratification), then reference
state-type: decision
status: RATIFIED (rev. 2) — ratified by Nick 2026-05-29; ratification cleanups applied
last-verified: 2026-05-29 against amendments/ on disk + the v2 plan §7 + the four research assessments
-->

# P2 — AMD Renumbering / Allocation Decision (RATIFIED — rev. 2)

**Decision owner:** Nick. **Author:** PM (Mode 3). **Status:** RATIFIED 2026-05-29. **Ratified scheme:** the 4-AMD device block (§5 recommended) — device 46–49, projection 50–52 fixed; integration assign-at-milestone.
**Gates (now cleared):** authoring of M4 amendment files is unblocked. Author only from §3; the first amendment to author is **AMD-50** (§9).
**Source evidence:** PLAN-M4-CONSOLIDATED-v2 §3 + §7 + §10.1; `2026-05-29_M4_Plan_Independent_Verification_Report.md` §H/§J/I-2/I-3; the four colliding research assessments (R4/R5/R6/R7) plus Research 8 (device-content source for REC-23–30); `design/amendments/` directory listing.

**Rev. 2 changelog (Nick review, 2026-05-29):** (1) M4.0b-2 re-scoped to backfill + version-bump on the existing string change-detect — typed work moved to a new WU; §9 corrected. (2) Withdrawn/reuse framing dropped — nothing ≥ 46 was ever authored, so there is no "reuse." (3) Only the content-stable device + projection blocks (46–52) are fixed; the integration block joins assign-at-milestone. (4) REC→AMD mappings PM-confirmed against source. (5) §6.2 collision fix.

**Ratification cleanups (Nick review, 2026-05-29):** (a) source-evidence citation fixed to R4/R5/R6/R7 (colliding) + R8 (device-content source); (b) §8.6 added — AMD-50 is authored as the general N→N+1 transition discipline, not hardcoded to 1→2; (c) §3.2 added — confirms the projection block (50–52, incl. AMD-52) is count-stable.

---

## 1. Why P2 exists

Four research assessments (R4 automation, R5 config, R6 integration, R7 API) each self-assigned AMD numbers **independently**, against a moving watermark, before any was ratified — R4 baked **AMD-48..50**, R6 baked **AMD-53..63** (11 candidate numbers; 10 accepted, AMD-61 withdrawn for the rejected REC-49), R5 baked **AMD-64..71**, R7 baked **AMD-72..85**. The v2 plan then needed two *new* M4 blocks that no assessment numbered: a device 4th slot for SemanticTag, and a Workstream-A projection block for Research 9/10. The result is a collision: the same integer lands on two different changes.

**None of those assessment numbers were ever authored as files** (see §2). P2 resolves the collision by fixing the two content-stable critical-path blocks contiguously now, and putting everything else on an assign-at-milestone rule so it cannot re-collide.

**The single most load-bearing consequence:** P2 frees **AMD-50** — the refinement of AMD-41 §3.2.4 that authorises the one-shot backfill, which **M4.0b-2 cannot be authored without**. Ratifying P2 is the gate that lets M4.0b-2 follow M4.0b-1.

---

## 2. Current state (source-verified 2026-05-29) — the clean model

- **On-disk authored amendments top out at AMD-45.** `design/amendments/` highest files: `AMD-44_Floor_Aggregate_and_EntityRole_Enum.md` (RATIFIED, pending implementation) and `AMD-45_Atomic_Subscriber_View_Checkpoint_Coupling.md` (RATIFIED 2026-05-29, M4.0a).
- **Every integer ≥ 46 is unallocated on disk — no file exists.** Gaps 28–30 are also unused; allocation proceeds forward, monotonic.
- **Every AMD number ≥ 46 appearing in any research assessment is a NON-BINDING provisional placeholder** that was never authored: R4's 48–50, R6's 53–63, R5's 64–71, R7's 72–85. This decision therefore allocates 46+ **freely** — there is **no "reuse"** of any number, because nothing ≥ 46 was ever written. The historical "withdrawals" (a provisional `EntityState.category` once sketched at AMD-47; R6's AMD-61 for rejected REC-49) are withdrawals of *placeholders*, not of files, and impose no constraint here.
- **P1 de-poison is done:** `AMD-45:75` was corrected from `MinimalDerivationRule` to the `MINIMAL_DERIVATION_RULE` constant before AMD-45 was ratified. No phantom remains in `design/amendments/`.

---

## 3. The ratified allocation — FIXED block 46–52 (device + projection only)

P2 fixes only the two **content-stable** critical-path blocks. The integration block (content is P3-gated) joins assign-at-milestone in §4/§6. RECOMMENDED scheme (device = 4 AMDs; the fork is §5):

| AMD | Change | RECs | Authoring WU | Block |
|---|---|---|---|---|
| **46** | `EntityCategory` on `Entity` (not `EntityState`) | REC-23 | M4.B1 | Device (Workstream B) |
| **47** | `AttributeValue` expansion — `QuantityValue`, `ArrayValue`, `DegradedAttributeValue` (public), `AttributeValueUpcaster` SPI, `QuantityValue` unit normalization | REC-24, REC-27, REC-29, REC-93 | M4.B3 | Device (Workstream B) |
| **48** | `Capability` batch expansion (8 permits) | REC-30 | M4.B5 | Device (Workstream B) |
| **49** | `SemanticTag` replaces `labels` on `Entity` | REC-26 | M4.B4 | Device (Workstream B) |
| **50** | **Projection rebuild / one-shot backfill / cursor-as-log-position — refines AMD-41 §3.2.4** | REC-76, REC-77, REC-79 | **M4.0b-2** | **Workstream-A projection** |
| **51** | Typed per-permit comparator + float-comparison policy | REC-90, REC-94 | **M4.0b-3** (post-M4.B3) | Workstream-A projection |
| **52** | Typed `StateChangedEvent` payload (`String`→`AttributeValue`) — **breaking** | REC-91 | **M4.0b-3** (post-M4.B3) | Workstream-A projection |

**M4 FIXED block = 46–52 (7 = 4 device + 3 projection). First unfixed integer = 53.**

> **Allocation note (2026-05-31):** **AMD-53 is allocated to the timestamp-model unifier** (`design/amendments/AMD-53_Timestamp_Model_Unifier_Event_Time_Activity_Timestamps.md`, PROPOSED — `EntityState.lastChanged`/`lastUpdated`/`lastReported` event-time sourcing; a Workstream-A projection follow-up authored ahead of Workstream C). Per §2 (forward/monotonic) and §6 (everything past the fixed bands is assign-at-milestone; all assessment numbers ≥ 46 are non-binding), the unifier correctly takes the next free integer at its milestone. **The integration block's indicative range therefore re-bases to 54+** (was "≈ 53–62"); it remains assign-at-milestone from the live watermark at Workstream-C briefing. No number is "reused"; nothing ≥ 53 was ever authored before AMD-53.

Amendments needing **no** AMD (confirmed): REC-28 (PM mods eliminated the subpackage AMD — this is why M4.0b-1 was amendment-free), REC-80/81/82, REC-92.

### 3.1 WU re-scope (Nick review #1 — the sequencing fix)

The v2 plan §3 scoped M4.0b-2 as *typed comparator + backfill + version bump*, which would gate it on M4.B3 (typed values) — making it half-implementable before those types exist. **Corrected per Nick's 2026-05-29 review:**

- **M4.0b-2** = the one-shot backfill **+ `projectionVersion` 1→2 bump on the existing string change-detect** (governed by **AMD-50 only**). It therefore depends only on **AMD-50 + M4.0b-1's green build** — nothing typed.
- **M4.0b-3 (NEW)** = typed per-permit comparator (**AMD-51**) + typed `StateChangedEvent` payload (**AMD-52**). Gated on **M4.B3** (AMD-47 delivers `QuantityValue`/`ArrayValue`/upcaster). The 2→3 derivation-version transition rides M4.0b-3 under AMD-50's already-authorised reconciliation discipline.

**This re-scopes v2 plan §3.** Propagate the corrected M4.0b-2 scope line and the new M4.0b-3 row into PLAN-M4-CONSOLIDATED-v2 §3 as a doc-currency follow-up (alongside P4).

### 3.2 Why the projection block (50–52) is count-stable (Nick review #3 — the AMD-52 check)

The fixed projection block is stable in *count* even though some of its content is still open (the R9/R10 Nick-calls in v2 §10). Each is one cohesive change that the open decisions can re-content but **not split**:

- **AMD-50** — the version-transition backfill / cursor-determinism / determinism-contract refinement. REC-76/77/79 are mutually dependent (backfill correctness needs cursor-as-log-position needs the determinism contract); they cannot meaningfully separate.
- **AMD-51** — the typed per-permit comparator. The open float policy (REC-94: `absEps`/`relEps`, abs vs rel vs hybrid vs ULP) changes its *content*, not whether it is one amendment.
- **AMD-52** — the typed `StateChangedEvent` representation change. The open R10 representation decision can change its *content* (fallback-parse behaviour, exact typing) but **cannot split it**: the payload-type change, the `applyToState` typed-store write, and the `CheckpointSerializer` `Map<String,String>`→typed evolution must land **atomically** (a partial change corrupts stored events), and the upcaster (REC-29) already lives in AMD-47. One cohesive breaking change.

This is the distinction from the integration block, where NQ-1..6 can genuinely **split** an amendment (e.g. AMD-53 → hooks + config-schema versioning, two distinct concerns) — which is why integration correctly stays assign-at-milestone (§4) while the projection block is fixed here.

---

## 4. Integration block (R6) — assigned at Workstream-C briefing, NOT fixed here (Nick review #3)

The integration freeze is **M4 Workstream C** but its content is **P3-gated** (Research 6 NQ-1..6 can still split AMD-53's config-schema versioning, fold REC-47's events, etc.). Fixing its integers now would force a `53b` sub-letter that violates §8.1's "one AMD = one cohesive change" and the contiguous-monotonic principle. So P2 **does not fix** these numbers: the block is assigned contiguous at Workstream-C briefing, from the live watermark at that time (indicatively 53–62), with any REC-41 split resolved as two full integers or deferred — never a sub-letter.

**Provisional per-REC map (planning aid only — non-binding):** 53 REC-41, 54 REC-42, 55 REC-43, 56 REC-44 (+REC-47 events per NQ-3/4), 57 REC-45, 58 REC-46, 59 REC-47, 60 REC-48, 61 REC-50, 62 REC-51. REC-49 rejected; REC-52 → M9. These ten map to the ten accepted R6 RECs (R6 assessment used 53–60, 62, 63 with AMD-61 withdrawn; the contiguous assignment closes that hole). No integer here is "reused" — none was ever authored.

---

## 5. The one ratification fork — device 3 vs 4 AMDs

Whether `EntityCategory` (REC-23) and `SemanticTag` (REC-26) get **separate** AMDs (46 and 49) or are **bundled** into one Entity-record AMD.

**PM recommendation: separate (the 4-AMD scheme above).** EntityCategory (M4.B1) is low-risk and has no upcaster dependency; SemanticTag (M4.B4) is HIGH-risk and gated on the AMD-47 upcaster. A bundle is half-implementable (EntityCategory ready while SemanticTag is blocked) — the exact hygiene §8.1 forbids. Cost of separating is one integer.

**If you bundle (3-AMD),** everything shifts down one: device = 46 (EntityCategory + SemanticTag), 47, 48; projection = 49, 50, 51; **the backfill amendment becomes AMD-49**; M4 ceiling = 51; first unfixed = 52. Flip at ratification and the PM re-stamps.

---

## 6. Non-fixed blocks — the assign-at-milestone rule

The integration (R6), automation (R4), config (R5), and API (R7) blocks all carry open NQs/DQs that can change their AMD counts. P2 does **not** bind their integers. Instead:

1. **Rule:** each is assigned a contiguous range **at the start of its implementing milestone** — Integration → Workstream-C briefing (post-P3); Config → M6; Automation → M7/M8; REST/WS API → M10/M11 — from the live watermark at that time.
2. **All assessment-embedded AMD numbers ≥ 46 for these blocks are PROVISIONAL — non-binding** (R4 48–50, R6 53–63, R5 64–71, R7 72–85).
3. **Indicative (non-binding) reservation** for planning: Integration ≈ 53–62, then Automation / Config / API contiguous after. Do not author from these.

**Only 46–52 are fixed by this decision.**

---

## 7. Supersession callouts (what becomes stale on ratification)

- **All assessment AMD numbers ≥ 46 are provisional placeholders, never authored** — R4 48–50, R6 53–63, R5 64–71, R7 72–85 are non-binding and are (re)assigned at their milestone (or, for R6, at Workstream-C briefing). There is no "withdrawn-integer reuse" to reconcile.
- The PM updates the "Global allocation" paragraph in `pm-handoff.md` and the watermark note in any KB state doc to point at this decision as the single source of AMD allocation truth, and verifies the **P1/P2/P3/P4 labels are used consistently** across `pm-handoff.md` and `PROJECT_SNAPSHOT.md` (Nick review #5) during WUCP Phase 2 closeout.

---

## 8. Authoring rules (post-ratification)

1. **One AMD = one cohesive, fully-ratifiable-and-implementable change.** No half-implementable bundles; no sub-letter splits (resolve at assignment as full integers).
2. **No amendment file is created at a number ≥ 46 until this decision is ratified.** After ratification, author **only** from §3; never from an assessment's self-assigned number.
3. **M4 amendments author in dependency order:** AMD-47 (types) before AMD-51/52 (M4.0b-3, which depend on the upcaster/typed values). **AMD-50 is independent** and is the M4.0b-2 unblock.
4. **Integration AMDs wait on P3** (Research 6 NQ-1..6) for both numbers and content (§4).
5. **P4 (Doc 02/05 currency)** must land before Workstream B/C *coding instructions* are authored — independent of this numbering decision, but flagged so the two prerequisites aren't conflated.
6. **AMD-50 is authored as the general N→N+1 version-transition discipline**, not hardcoded to 1→2. It authorises the reconciliation-scoped, non-emitting, cursor-deterministic backfill for *any* `projectionVersion` increment. This is what lets M4.0b-3's 2→3 transition ride AMD-50 without a fresh amendment (§3.1) — if AMD-50 were written 1→2-specific, M4.0b-3 would need its own §3.2.4 refinement.

---

## 9. What ratifying P2 unblocks (corrected — Nick review #1)

- **AMD-50** (projection rebuild/backfill/cursor, refining AMD-41 §3.2.4) can be authored → **M4.0b-2** (one-shot backfill + `projectionVersion` 1→2 bump **on the existing string change-detect**) is then gated **only on AMD-50 + M4.0b-1's green build**. No typed-value prerequisite.
- **AMD-46/47/48/49** (device types) → Workstream B (M4.B1/B3/B5/B4) unblocked, pending **P4** doc currency for the coding instructions.
- **M4.0b-3** (typed comparator AMD-51 + typed payload AMD-52) is **NOT** unblocked by P2 alone — it remains gated on **M4.B3** (AMD-47 types). Do not start it before M4.B3 lands.
- **Integration** numbers are assigned at Workstream-C briefing (post-P3), not by this decision.

**REC→change→AMD mappings (PM-confirmed against source, Nick review #4):** device REC-23/24/26/27/29/30 and projection REC-76/77/79/90/91/93/94 confirmed against PLAN-M4-CONSOLIDATED-v2 §7; integration REC-41–48/50/51 (REC-49 rejected, REC-52 → M9) confirmed against the R6 assessment. The R6 "53..63" is an 11-number candidate range with AMD-61 withdrawn → 10 accepted; **no hole at 59** (REC-47 → 59). The "ready / gated / HIGH-risk" annotations trace to the v2 plan §3 sequencing notes and §9 risk register.

**Recommended next step after ratification:** author **AMD-50** first — it is the critical-path unblock and has no type dependency — then M4.0b-2 is gated only on M4.0b-1's green build.

<!--
file: context/instructions/2026-06-28_AMD-CAND-2-3_doc02-08-color-currency_staged-fold.md
purpose: A STAGED currency fold for AMD-CAND-2 (color scope) + AMD-CAND-3 (color-temp canonical unit) — pre-drafted with verbatim before->after edits so it commits on Nick's word. These are internal-consistency corrections to Locked Doc 02/08 that conform to the already-canonical rule; NOT applied here (PROPOSED). The hub does not self-ratify a Locked-doc change.
audience: Nick (co-signs / rules the disposition); the v11 PM hub (applies the captured diffs on Nick's word + bumps the watermark + registers); the M9 + bench lanes (consume the conformed color contract).
state-type: governance fold (PROPOSED — staged, commit-on-word).
status: APPLIED 2026-07-01 — CONSUMED BY **AMD-96** at the v13 consolidated governance pass (Nick's word given): the v13 hub found proposed AMD-96 (2026-06-26) already carried this payload at direction level, so these verbatim diffs became AMD-96's §2.A/§2.B edit text (all three edits applied, incl. the optional Edit 3; all BEFORE anchors confirmed verbatim at docs 75d0345). Option A (White/CT) + Kelvin-canonical ruled as recommended. No separate AMD numbers consumed. PRIOR: STAGED 2026-06-28 by the v11 hub, from the Stream-B research return §6.
baseline: docs 75d0345 (Doc 02 + Doc 08 LOCKED; watermark AMD-95; invariants 170/50). Line numbers are at this HEAD — re-confirm the anchor text (not the line number) at apply time.
anchors: context/assessments/2026-06-28_device-model-and-corpus_research-return.md §6 (AMD-CAND-2/3) + §8 esc 2 · homesynapse-core-docs/design/02-device-model-and-capability-system.md §3.6/§3.7/§3.10 · design/08-zigbee-adapter.md §3.5 + the "Color modes beyond color temperature" note.
-->

# Staged currency fold — AMD-CAND-2 (color scope) + AMD-CAND-3 (color-temp canonical unit)

**Why staged, not applied.** These touch Locked docs; the hub does not self-ratify. They are **currency corrections** (conform existing text to the already-canonical rule + remove an internal inconsistency), lighter than AMD-CAND-1 (a new schema slot). **Two routes — Nick's call:** (a) **co-sign directly** — these are your scope call and they only conform/clarify, so your word + a watermark bump suffices; or (b) **bundle into the AMD-CAND-1 review pass** for a second opinion on the Locked-doc edits (same docs touched). Either way the exact edits are captured below so it commits the moment you say go. **Not pipeline-blocking** (the hero path is white/CT); fold before M9 builds color/CT handling on it.

**Hub recommendations (the disposition you flagged for your scope call):**
- **AMD-CAND-2 → Option A: scope to white/CT for V1.** Color (`color_hs`/`color_xy`) is post-MVP per Doc 02 §3.6; pulling it forward (option B) expands M9. Make Doc 02 §3.10 honest (color = reserved/post-MVP, not invited-optional) so it stops inviting a capability V1 cannot realize.
- **AMD-CAND-3 → Kelvin-canonical-at-ingestion (conform Doc 08 to Doc 02).** Doc 02 §3.7 is the Locked canonical-units moat rule (convert at ingestion); Doc 08 is the outlier (stores mireds, converts at query). Conform Doc 08.

---

## Edit 1 — AMD-CAND-3: Doc 08 §3.5 cluster→capability row (Kelvin-canonical-at-ingestion)

**File:** `homesynapse-core-docs/design/08-zigbee-adapter.md` §3.5 (the ZCL cluster→capability table; ~line 205).

**BEFORE (verbatim):**
```
| ColorControl (CT) | 0x0300 | `color_temperature` | `colorTemperatureMireds` (Uint16) → `color_temp_mireds` (IntValue); K = 1,000,000 / mireds computed at query time |
```
**AFTER:**
```
| ColorControl (CT) | 0x0300 | `color_temperature` | `colorTemperatureMireds` (Uint16) → **`color_temp_kelvin` (IntValue, K)**, converted `K = 1,000,000 / mireds` **at INGESTION** (Doc 02 §3.6 canonical `color_temp_kelvin` + §3.7 convert-to-canonical-at-ingestion); the original mireds value is retained for auditability per Doc 02 §3.7 (canonical + original protocol value). |
```
*Rationale:* eliminates the §3.7 moat-rule contradiction (no convert-at-query for a canonical attribute). The ZCL reporting config (line ~281, `colorTemperatureMireds` min/max) is unaffected — that is the wire attribute; the canonicalization happens at ingestion after the report arrives.

## Edit 2 — AMD-CAND-2: Doc 02 §3.10 light optional capabilities (honest color scope)

**File:** `homesynapse-core-docs/design/02-device-model-and-capability-system.md` §3.10 (entity-type composition table; ~line 413).

**BEFORE (verbatim):**
```
| `light` | `on_off` | `brightness`, `color_temperature`, `color_hs`, `color_xy` |
```
**AFTER:**
```
| `light` | `on_off` | `brightness`, `color_temperature` (V1); `color_hs`, `color_xy` (**post-MVP — reserved, not realized in V1**; see §3.6 post-MVP set) |
```
*Rationale:* §3.6 (~line 283) already lists `color_hs`/`color_xy` as post-MVP, but §3.10 listed them as V1 `light`-optional — so the doc both invited and could not realize color (and Doc 08 §3.5 has no full-color handler). This makes §3.10 consistent with §3.6 and with Doc 08's "Color modes beyond color temperature" reservation (~line 999), so the §3.10 "unexpected capability" validation does not warn on an intentionally-unbuilt capability.

## Edit 3 (optional clarity) — Doc 08 §3.5 Extended Color Light composition note

**File:** `homesynapse-core-docs/design/08-zigbee-adapter.md` §3.5 (device-type composition; ~line 224).

**BEFORE (verbatim):**
```
| Extended Color Light (0x010D) | OnOff + LevelControl + ColorControl(full) | `light` |
```
**AFTER:**
```
| Extended Color Light (0x010D) | OnOff + LevelControl + ColorControl(full) | `light` (V1 realizes `on_off`/`brightness`/`color_temperature` only; full color is post-MVP — see "Color modes beyond color temperature") |
```
*Rationale:* a small honesty note so the composition table doesn't imply full-color realization in V1. Optional — Doc 08 line ~999 already reserves full color; include if you want the table self-consistent.

---

## Register + watermark (on apply)

- Assign the next free AMD number(s) at ratification (do **not** pin while PROPOSED — INV-GA-02). One amendment covering both corrections is fine (a "Doc 02/08 color currency" amendment), or two — your call.
- Bump the watermark (AMD-95 → next) in `Architecture_Invariants_v1.md` / the amendments register; no new invariant required (these are currency conformances, not new contracts).
- No `projectionVersion` change, no code change in this fold (M9 will implement the conformed CT-at-ingestion when it builds the ColorControl handler; the corpus/IR already treats canonical units per Doc 02 §3.7).

## What this fold does NOT do

It does not add color support (that stays post-MVP); it does not touch the confirmation amendment (AMD-CAND-1, separate dispatch); it does not change the capability vocabulary beyond marking color reserved. Apply-time: re-confirm each BEFORE block against the live Locked text (anchor on the text, not the line number — the docs may have shifted), then apply host-side (the truncated-tail phantom is active — targeted edits, verify tails).

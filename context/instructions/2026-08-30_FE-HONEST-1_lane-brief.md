<!--
file: context/instructions/2026-08-30_FE-HONEST-1_lane-brief.md
purpose: FE-HONEST-1 — the chartered FE honesty row, now UNBLOCKED post-R-4: the explain surface must be LOUD about unresolvable refs (§10-J, HIGH) and the device/entity lists must read STORE TRUTH (§10-G/H/I, MED). Authored ahead at v59 beat 5; dispatch at will.
audience: a fresh FE lane (Cowork, nexsys-frontend skill) · Nick (dispatch + commit boundary) · the hub (audit)
status: ISSUE-READY. Write-set: web-ui/** ONLY (core = NICK'S HANDS at commit; the lane commits nothing). The brand/FE-flip is NOT this lane (Pelton-gated, its own instruction).
return: nexsys-hivemind/context/audits/<CT-filing-date>_FE-HONEST-1_return.md — ≤10 KB, §0-first (verdict · census · deviations · asks), instrument-limit disclosure line + CT-rederivation line required.
-->

# FE-HONEST-1 — loud unresolvable refs + store-truth read path (lane brief)

## §A The two defects (evidence of record — read these rows, then the primaries)
1. **§10-J (HIGH):** the explain surface CONCEALED a fault it could see — it said "it fires on state change" while the rule's `entity_ref` (`01KX1PB9AAB4VB3E10BD477TV3`) was dangling; one honest sentence would have surfaced it; instead it cost an hour of journal archaeology. Evidence: `context/audits/2026-08-30_R3a_hub-return_what-changed_card.md` :68 + the R-4 record (C4 section — bench-hero's refs belonged to the BENCH card's registry, F-R4-2).
2. **§10-G/H/I (MED):** `Available` with an empty `Last reported` while THE STORE HOLDS the rows (`availability_changed`, `state_reported`) — a READ-path gap, not a data gap; the Devices page shows an ENTITY ULID under a `DEVICE` column so a row cannot be correlated to a `device_adopted` log line; `Current` on the list vs "report time not recorded" on the detail. Evidence: the same card :74 + the R-4 record §6 (C2 was evidenced AT THE STORE because the list render could not carry it).

## §B The bar
The dashboard's honesty IS the product's honesty hero ("why did it fire? / why didn't it? / did it actually confirm?"). Deliverables: (1) an unresolvable `entity_ref` anywhere on the explain surface renders LOUD (named ULID, "not in this registry", visually failing — never a paraphrase that hides it); (2) Last-reported/Current derive from the store's own rows via the read API; (3) the device/entity column mislabel fixed. GROUND FIRST: read `web-ui/FRONTEND_DOCTRINE.md`, `web-ui/MODULE_CONTEXT.md`, the FROZEN v1.1 read-API contract, and the actual components before proposing the delta. **If the frozen contract does not expose a field the fix needs (e.g. report-time), file a CONTRACT-GAP PROPOSAL in the return and stop that item — the freeze is not yours to lift.**

## §C Fences
web-ui/** only · the frozen v1.1 contract untouched · no brand strings (G-2 fence) · frontend.yml CI gate must stay green in-lane · commit NOTHING · no public sentence anywhere.

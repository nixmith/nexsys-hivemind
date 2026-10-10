<!-- file: _scratch/v104/b3/AMD-103_independent-review_v3-addendum.md · a focused re-read of the hub's edits H1–H5 (v2r → v3) · v2r 32,916 B md5 97815379d6bc0ae78ee5fb2a65ed74ce · v3 33,809 B md5 e56640281e7c94518317d4fb44d9b2a7 · script v104b3_hub_edits_1.py md5 94e3f1f59526203d4b85aca191dfcc19 · core 409547c · docs 5e8eb8b -->

# AMD-103 v3 — addendum to the independent review

**Verdict: EDITS.** The v2r → v3 diff is exactly the hub's eight edits plus the status line, and every E1–E24 text is intact. Six exact edits make v3 safe to ratify: H1 ×2, H2, E16's dropped A4, R-F's comparison test, and R-H's balance. Two filing actions remain: bank D-v104-18/-20, and file the review at `:9`'s path.

## Findings

1. **The diff — HOLDS.** v3 = v2r + the script's eight replacements (H1, H2, H3a, H3b, H4a, H4b, H4c, H5a) + the status line (H5b, stamped `~15:10 CT`, matching the script's template). Rebuilt in memory, it is byte-identical to v3 (md5 `e5664028…`). The line diff touches exactly `:2`, `:4`, `:28`, `:29`, `:65`, `:76`. All 24 E texts are present: 19 verbatim, and 5 changed only by H edits (E2 by H1+H2, E8 by H4a, E13 by H4b, E16 by H3a+H3b+H4c, E20 by H5a). No other byte moved.

2. **H1 — the numbers are TRUE; the attribution is WRONG.** 1,644,011 → 1,654,229 is 10,218 in ≈ 2.45 h of Core time. But D-v104-20 R4 (working tree `:168`) says "store growth is a pilot gate … dry-run #1's `du` and retention row decide it", not "type counts measure the rate". And "this morning" is relative in a ratified record.
Old:
~~~~
Core time this morning (
~~~~
New:
~~~~
Core time on 2026-10-10 (
~~~~
Old:
~~~~
— dry-run #1's `du` and type counts measure the rate (D-v104-20 R4).
~~~~
New:
~~~~
— store growth is a pilot gate that dry-run #1's `du` and retention row decide (D-v104-20 R4).
~~~~

3. **H2 — the facts are TRUE; as a ratified sentence it is UNSOUND.** There is no hint at `:212–:214`, no `ANALYZE` anywhere, and IR-40 recorded the time-range read flipping to a rowid walk at bound LIMIT ≥ 500. I ran `EXPLAIN QUERY PLAN` (V001 DDL, in memory, SQLite 3.37.2 — not the shipped 3.51.3). It plans the type read and its `hasMore` probe on `idx_events_type` at LIMIT 1–1000, both empty and at 200 k rows, while reproducing IR-40's walk for the time-range read. So the pin is insurance, not a fix for a known defect. As written, the clause states an unwritten unit's guard as done, covers only the page query, and omits Nick's own word for the guard ("a rows-read guard in CI", D-v104-18 `:162`). Make it a requirement:
Old:
~~~~
the read's plan pinned to that index by REGISTRY-COLD-1's plan guard — `SELECT_BY_TYPE_SQL` carries no hint at `409547c`, `:212–:214`, and the shipped planner once chose a rowid walk for a sibling read, IR-40
~~~~
New:
~~~~
the type read and its `hasMore` probe (`:768–:779`) must stay on that index — `INDEXED BY` and an `EXPLAIN QUERY PLAN` test through the shipped driver, as IR-40 holds the time-range read, beside REGISTRY-COLD-1's rows-read guard (D-v104-18): `SELECT_BY_TYPE_SQL` carries no hint at `409547c` (`:212–:214`), no `ANALYZE` runs, and the shipped planner walked rowids for that sibling read at `LIMIT` ≥ 500
~~~~

4. **H3a, H3b — TRUE, and in register.** R2 matches `:168`. "One lane at a time" is D-v104-13 (a)'s "the free Java slot" (`:71`). D-v104-18 and D-v104-20 are still uncommitted (hivemind ` M` at `8ab4789`); bank them before AMD-103 files.

5. **H4a–c, H5 — HOLD.** The meanings are unchanged, and "earliest" now matches R-B (i)'s own word. The status line gives the review's md5 correctly; it lists H1–H4 only.

6. **Owed — my E16 is WRONG.** "for the fallback (a) and UPGRADE-1 only" drops A4. Nick's scan "stays for A4 and upgrade planning" (D-v104-18 `:163`), and R-H revisits the constant "by the filed rate".
Old:
~~~~
— for the fallback (a) and UPGRADE-1 only, off AVAIL-API-1's critical path.
~~~~
New:
~~~~
— for A4's derivation (R-H), UPGRADE-1 and the fallback (a), off AVAIL-API-1's critical path.
~~~~

7. **Owed — R-F (b) has no proof clause.** Nick's `COLD-BOOT: a` carries "a comparison test (the new rebuild equals the full replay)" (`:162`).
Old:
~~~~
before the cursor handoff (AMD-42 · AMD-101).
~~~~
New:
~~~~
before the cursor handoff (AMD-42 · AMD-101); AVAIL-API-1 carries REGISTRY-COLD-1's comparison test for the card — the catch-up's view equals a full replay's (D-v104-18).
~~~~

8. **Owed — a dangling citation.** `:9` says the review "is filed at" `nexsys-hivemind/context/audits/2026-10-10_v104-b3_AMD-103_independent-review.md`, and no such file exists. File the review and this addendum there before AMD-103 lands.

9. **R-A — FAIR.** It states the REC (`device_health`, the scope the stored bytes already carry), both alternatives with their cost (the split; the dual-scope set), and the move of the existing `availability_changed` row (R-A, §2, the Target line).

10. **R-H — ONE-SIDED.** It gives only the case against config. Add what config buys:
Old:
~~~~
left the schema for having no reader (IR-122) |
~~~~
New:
~~~~
left the schema for having no reader (IR-122); for config: the A4 revisit lands as a per-install edit, not a release, and under AMD-102 a misspelt key fails the boot loudly, not silently |
~~~~

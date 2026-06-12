<!--
file: context/handoff/2026-06-14_R16-returns_assessment_session_prompt.md
purpose: Next-PM-session brief — R16 RETURNS ASSESSMENT: both returns (R16-A logging/observability UX market+human factors, REC-186–200; R16-B LLM-legible output engineering, REC-201–215) → serialized assessment (B FIRST) → merged disposition → bucket routing (incl. the gate-free OUTPUT_CONVENTIONS.md draft). Authored 2026-06-12 at the Pi-evidence closeout, AHEAD of the returns landing.
audience: PM (next Cowork session), Nick (dispatches + lands the returns)
status: READY — runnable the moment BOTH returns are on disk. If either return is absent at Step-0: STOP per the 2026-06-14-brief fold-abort precedent (hygiene-only, nothing assessed).
-->

# Session Brief — R16 Returns: Serialized Assessment → Merged Disposition → Bucket Routing

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST**, then the freshness preflight vs the PINNED STATE below — one glance per check.

## MANDATORY-INPUT CHECK (Step-0, before anything)

**SATISFIED 2026-06-12 (intake done at the Pi-evidence conversation's tail):** both returns are ON DISK, renamed to convention —
`context/instructions/Research_16A_Logging_Observability_UX_Market_Human_Factors_RETURN.md` (292 lines, ~48K) and
`context/instructions/Research_16B_LLM_Legible_Output_Engineering_RETURN.md` (271 lines, ~41K).
Verify both exist at Step-0 anyway (one glance); if either vanished: STOP per the fold-abort precedent.

## INTAKE OBSERVATIONS (2026-06-12 — verify independently; these are intake-grade, NOT the assessment)

- **Quote-backs:** both returns' §0 blocks verified VERBATIM at intake against the in-session script reads (the §0.2(i)/(ii)/(iii) idiom blocks byte-match `pi-health.sh`/`pi4-validation.sh` at `01841ba`); §0.3's 14 names + §0.4 + Register-C present in both. Re-verify §0.3 against Doc 07 §11.2 and §0.4 against source — intake could not re-read Doc 07.
- **The seeded ground-precision hazard did NOT propagate:** neither return cites `automation.cascade.depth_exceeded` — both used the real 14. The §4-step adjudication rule below likely moot; keep it anyway.
- **16-B's headline defect claim (REC-204, diagnostics→stdout) is TRUE** — confirmed at intake directly against the shipped helpers (no `>&2` anywhere in pi-health.sh). The OQ-15-2 bench driver v2 (`assessments/oq-15-2-harness/`) shares the defect — fold it into the OUTPUT_CONVENTIONS retrofit list.
- **Both declare connector-blind** with explicit KB-verification gap lists (16-B §5: Doc 11 §3.5 metric prefixes, §11.2 `observability.*` names, manifest-pin currency; 16-A: §0.5-row anchors). THESE ARE THE ASSESSMENT'S PRIORITY VERIFICATION TARGETS.
- **External-claim spot-check list:** JEP 506/JDK 25 Scoped Values finalization (16-B leans on it for REC-211 — verify against OpenJDK record); OTel semconv v1.41.x; the Anthropic engineering-post quotes (Sep 2025); 16-A's HA thread IDs + the Hubitat ~1 MB buffer + SmartThings Dec-31-2022 sunset (the last is consistent with known history).
- **Cross-return coherence at intake:** A's REC-186/187 ⊂ B's REC-201–209 (the OUTPUT_CONVENTIONS core — a merge, not a conflict); REJECT sets complementary (A: emoji/lossy-surface/euphemism; B: collector/MESSAGE_ID/logfmt-wire/traceparent/SeverityNumber); register fences held in both directions (each routes the other's register out explicitly). 16-A's strongest finding for the dossier: the HA "Month of WTH" campaign evidence; its honest negative ("data-without-register" — B3 risk) deserves disposition prominence.

## PINNED STATE (verified 2026-06-12 at the Pi-evidence closeout)

- **SHAs:** hivemind `d70f8d1` (hygiene rotation) **+ ONE returns-intake commit expected on top** (the renamed returns + refreshed prompts + the rollover-synthesis prompt — reconcile the actual HEAD at Step-0; chain: `d70f8d1` ← `58794d7` Pi-evidence ← `723e0d9` R16) · core **`01841ba`** (scripts-only pair; substantive **`7c73c91`** — GREEN 147, pins 55/24/36, `projectionVersion` 5) · docs **`d7ea212`**. Check 9: the known one-file STALE acceptable. index.lock flag: GONE (deleted 2026-06-12 — if a NEW one appears, that is a fresh incident, not the old saga).
- **Hot-path posture (post-rotation 2026-06-12 evening):** snapshot ~59K · pm-handoff ~17K · cross-agent ~18K. Rotated content → `status/archive/PROJECT_SNAPSHOT-priors-rotated-2026-06-12.md` + `handoff/archive/pm-handoff-2026-06.md`, git-object-sourced from `58794d7`, host-verified.
- **Gate ground:** OQ-15-2 ✅ RESOLVED (encrypted set CONFIRMED `[identity, presence_personal]`); M6.3 1-of-3 (interviews = the sole open evidence gate); M7 rows 1–2+5 ✅, row 3 ⛔ (interview half), row 4 ⛔ (M5-C Increment 1 — its own prompt on disk, may run in parallel or already have run).
- **The briefs (committed `723e0d9`):** `context/instructions/Research_16A_Logging_Observability_UX_Market_Human_Factors_Brief.md` + `Research_16B_LLM_Legible_Output_Engineering_Brief.md`. Quote-back set: the verbatim pi-health idiom block + the Doc 07 §11.2 event-name list (all 14) + the DAS Register-C paragraph; 16-B adds `CausalContext` + the `com.homesynapse.event` module-info (source-verified at `7c73c91`).

## TASK (strict order)

1. **Step-0:** mandatory-input check (above) → preflight vs pinned → reconcile new HEADs into the snapshot masthead → archive this prompt when consumed.
2. **Intake:** returns saved verbatim in `context/instructions/` → copy/archive the raw returns to docs `research/returns/2026-06-DD_*` per the standing flow (Nick's commit carries them); never edit a return.
3. **Serialized assessment — B FIRST** (engineering constrains, human evidence prioritizes — the R16 record's stated fold order), then A. Per return, per the R13–R15 pattern: quote-back verification (every §0 quote-back honored verbatim — zero tolerance for adulterated embeds); source-verification of EVERY load-bearing claim against `7c73c91` / Doc 07 / Doc 11 / the DAS; fabrication scan (the R14 standard: a DOCS-connector-blind run must DECLARE it; fabricated identifiers = docked grade); grade + disagreement register + steelman.
4. **⚠ Ground-precision check (logged 2026-06-12 for THIS pass):** the R16 *session prompt's* `automation.cascade.depth_exceeded` exemplar is NOT a Doc 07 §11.2 table name — the briefs embed the real 14 (the `automation.run.started` class); the cascade diagnostic is the *event* `cascade_depth_exceeded` (§3.7.1/AMD-92 ground). If a return cites the prompt's wrong exemplar as ground, that is a brief-side seed, not a return fabrication — adjudicate accordingly (dock nothing for inheriting it; dock for failing to flag it if the return claims source verification of that name).
5. **Merged disposition** (one artifact): collision adjudication across A/B; REC-186–215 high-water; every REC → exactly one bucket: **SCRIPT-STANDARD** (feeds item 6) / **M12-INPUT** / **M10-M13-INPUT** (parking register) / **DOC-11-CURRENCY** (queue, Locked-doc fence respected) / **M5-C-COPY** (→ M5-C Increment 2; do NOT retro-inject into Increment 1 if it already ran) / **FUTURE** / **REJECT** (with reasons). Anti-requirements bind.
6. **The gate-free deliverable: `scripts/dev/OUTPUT_CONVENTIONS.md` DRAFT** from the SCRIPT-STANDARD bucket (the one artifact this cycle ships without waiting on any gate — the pi-health `READINESS:` machine-parseable line is the established seed pattern; the OQ-15-2 driver's `RESULT:`/`FLAG:`/`READINESS:` lines from `assessments/oq-15-2-harness/` are fresh in-house evidence to fold). Core repo file → hand Nick the commit separately from hivemind.
7. **Closeout:** research-agenda R16 rows → ASSESSED; consumed briefs → archive; snapshot/pm-handoff/cross-agent appends; commit messages handed over (`git commit -F` if any message contains `!`).

## TOKEN DISCIPLINE

The returns are the session's bulk — budget for two full reads + targeted source verification. Do NOT re-read the R13–R15 returns or disposition (the assessments carry them); Doc 07/Doc 11 only at cited anchors; the DAS only at Register C. The precision item is the per-REC bucket table — spend the care there.

## STANDING NICK-PACED ITEMS (surface, don't block on)

Energy/erasure interviews (the sole open M6.3/row-3 evidence gate) · M5-C Increment 1 (parallel; vetoes D-1..D-7 at its start) · the W25/W26 rollover + M6.3-vs-M7 ordering call (Sun Jun 14 boundary; needs the interviews) · pi4-validation.sh script fix (F1/F3) + optional Pi-4 confirmation run · spike-dir `git rm` + DOCS-connector deselection · backlog DONE-row compression (still queued — NOT taken at the 2026-06-12 rotation) · FUTURE-AMD queue.

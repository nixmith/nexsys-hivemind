<!--
file: context/handoff/2026-06-10_research13-return_M6.4-M6.2_session_prompt.md
purpose: Next-PM-session brief — process the Research 13 return → author M6.4 then M6.2. Carries a PINNED STATE block so the session spends its context window on assessment + instruction reasoning, not state re-derivation.
audience: PM (next Cowork session), Nick
status: READY — authored 2026-06-10 at the cleanup + research-scoping session closeout.
-->

# Session Brief — Research 13 Return Processing → M6.4 + M6.2 Instructions

PM session (nexsys-project-manager skill). Run the freshness preflight, but use the PINNED STATE below as the expected answer key — each check should take one verification glance, not a re-derivation. Divergence from a pinned line = real drift; investigate that line only.

## PINNED STATE (verified 2026-06-10 at the cleanup session — trust, then spot-verify)

- **homesynapse-core:** substantive HEAD = **`9035110`** (M6.1a, on `b7bc65c` M6.1b) + **one docs-only commit on top** (config `MODULE_CONTEXT.md` currency, committed by Nick 2026-06-10 — no code; treat like the `6c6dd33` typo-fix precedent; bump the snapshot Latest-commit field with its sha at next closeout, nothing else cites it). Build GREEN (147 tasks). `projectionVersion` 5. **No open deferred build gates.**
- **homesynapse-core-docs:** committed clean 2026-06-10 (the 4 docs-lane carries: Doc 06 §3.2 note + §3.7 AMD-67 banner, Doc 01 §4.4 +1 row, cloud-scalability §1.4 note). Watermark **AMD-87**; AMD-66/67/68/70/71 RATIFIED; AMD-69 DEFERRED (don't re-open). Doc 15 LOCKED + inviolate (§8.1 `ScopeKeyManager` nit stays parked for the next Doc-15-touching amendment).
- **nexsys-hivemind:** committed clean 2026-06-10 (sha-reconciliation + archival + Research 13 brief; the M6.1 instruction lives ONLY at `context/coding-instructions/archive/M6.1_Config_Pipeline.md`, with its EXECUTION RECORD).
- **Trackers are mutually consistent at the above** — snapshot/backlog/charter/W24/handoffs/pointer all cite `9035110`; cross-agent has ONE active entry (the 2026-06-10 CURRENT POINTER); pm-handoff's pre-M5-window records are rotated to `archive/pm-handoff-2026-05.md`/`-2026-06.md` (legacy M3-era tail is marked, rotation queued — not this session's job).
- **Check 9 caveat:** the 2026-06-10 sessions ran with the sandbox VM down → mirror diff was evidence-based. If the VM is up, run the real `diff -rq`; a STALE there is expected post-sync noise, CONFLICTED is not.
- **M6 state:** M6.1 ✅ COMPLETE (whole). **M6.2 gate fully satisfied** (AMD-68 ✓ + M6.1 landed). **M6.4 UNBLOCKED.** **M6.3 triple-gated — do NOT issue** (OQ-15-2 Pi-4 microbench + AMD-86 §3 interview signal + OR-M6-NONCE).
- **Research 13** (`context/instructions/Research_13_Config_System_Market_Superiority_Brief.md`): **AUTHORED, NOT YET DISPATCHED** — ⚠ corrected 2026-06-10: the original pinned line here said "dispatched by Nick," written presumptively before any dispatch occurred (PM defect, caught by the fresh session's preflight). **Dispatch is Nick's open action item.** REC-130+; disposition table mandatory. Research numbering is append-only — 12 = the consumed Zigbee return.

## TASK (in order — re-sequenced 2026-06-10 after the dispatch-state correction)

0. **Nick (not the PM session): dispatch Research 13 to the DOCS Project** (web search required; the brief masthead states the generic-deep-research evidence fallback). Until the return is captured verbatim to `homesynapse-core-docs/research/returns/`, Task 1 is BLOCKED — do not assess from summaries (the M5-window STOP rule).
1. **[BLOCKED on Task 0] Assess the Research 13 return** (6-step A–F; archive the raw return per research-agenda §2 Step 0). Enforce: quote-back gate honored; every REC has exactly one disposition bucket; ALREADY-COVERED rows carry real AMD/doc § citations (spot-verify a sample against the docs repo — do not trust the table blind); evidence meets the Mom-Test/primary-source bar. INCOMPLETE-EVIDENCE → trigger the brief's stated fallback rather than accepting thin findings. Then **lift the ⛔ gates on M6.4/M6.2** (fold any INSTRUCTION-OBLIGATION rows, or record confirmed-none) and issue.
2. **Author the M6.4 coding instruction ⛔ ISSUE-GATED** (the M4.C pattern — author now from the pinned obligations + ratified contracts; the top-of-file gate checklist requires "Research 13 disposition folded or confirmed-none" before issue; Nick ruling 2026-06-10: gated authoring converts the dispatch wait into ready work at zero sequencing risk) (hot-reload atomic swap). Pinned obligations (2026-06-10 rulings — non-negotiable): **R1** per-ERROR `config_error` startup publish (Doc 06 §3.6); **P2 consumer/pin survey re-run** for `config.section_reloaded`; **explicit `CoreSchema` on the reload re-parse** (config MODULE_CONTEXT gotcha). Plus: atomic `ConfigModel` swap (no torn read), AMD-66 listener invocation + classification-driven apply, `ConfigChangeSet` diffing, reload/write `ReentrantLock`, atomic file writes, §3.7 step-7 migration write-back + pre-migration backup (R2), `reload()`/`write()` un-staging — and any Research-13 INSTRUCTION-OBLIGATION rows. House mechanics: verbatim module-info embed (config gained 5 third-party non-transitive `requires` per the 2026-06-10 ruling — embed the CURRENT file, with the ruling note), §4c Clock reminder (config non-whitelisted), STOP-gates, P5 shift-left note.
3. **Author the M6.2 coding instruction ⛔ ISSUE-GATED** (same gate row) — secret store + per-scope key mgmt. Carries: the **E2 `com.homesynapse.app` bridge VERBATIM from the M6 charter CARRY 1** + re-verify zero-new-edge at issue (`persistence !requires config`, `config !requires persistence`, only `app` both) + embed both module-infos; AMD-68 `setAll` atomic durable write; `!secret`/`!env` stage-3 tag resolution (YamlLoader tag-constructor seam; LoadSettings must keep `CoreSchema`); machine-local root per Doc 15 §3.5/§7.3; `ScopedConfigurationAccess` exposure seam stays deferred to M9. **No M6.3 scope** (at-rest encryption, nonce machinery, encrypted-scope set all gated).
4. Standard closeout: WUCP drift check, handoffs, commit messages handed over.

## TOKEN DISCIPLINE (why this block exists)

Do not re-derive the sha chain, the gate history, or the archival state — it is pinned above and consistent on disk. Spend the window on: the return's evidence quality, the disposition-table fold, and the two instructions' contract precision (MODULE_CONTEXT gotchas → watch-outs; consumer/pin surveys; STOP-gates). Read targeted file sections, not whole trackers; the config `MODULE_CONTEXT.md` Gotchas + Phase-3 Notes and the M6 charter CARRY blocks are the high-value reads.

## STANDING NICK-PACED ITEMS (surface, don't block on)

Pi-4 microbench (OQ-15-2 — must not slip past M6.2) · energy/erasure interviews (AMD-86 §3 gate) · **M5-C website/docs floor (P6 — still not started)** · B2 C8/C9 ratification · GraalVM/GenZGC spikes → LTD-01.

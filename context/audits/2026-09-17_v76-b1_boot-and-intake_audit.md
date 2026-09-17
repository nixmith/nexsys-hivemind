<!--
file: context/audits/2026-09-17_v76-b1_boot-and-intake_audit.md
purpose: THE v76 BEAT-1 AUDIT — the boot at the instrument (the read budget with one trim disclosed, the five HEADs, the preflight one line per check); the v75 b8 packet's verdicts intaken at the bytes (both cards at diff-tree; CI #252 and install-smoke #60 on `3af6213` read from the GitHub API on the device; run #56's artifacts and their expiry; the repo's artifact count after the cleanup); one correction to the dispatch line (the uploads went THROUGH — CI-2's never-gate clause was not exercised); the closure counter's seventh sample; the window's ONE deliverable and the beat order re-cut (ENERGY-READ at b2, not inside b1); what the hub could not re-execute.
audience: the hub (the record; the next hub's boot) · Nick (§0 and §6)
state-type: intake audit + boot record
status: FILED v76 beat 1 (Thu 2026-09-17 ~18:0x CT; instrument 2026-09-17T23:02:39Z at boot)
-->

# v76 beat 1 — the boot at the instrument; the b8 packet's verdicts; the counter's seventh sample

## §0 Card
- **The window's ONE deliverable (plan §13):** the sitting's two records (H8-a, R-5B) intaken two-layer by Sunday night and ENERGY-READ DISPATCH-READY through THE PREMISE GATE — the corroboration leg's code on the Java slot before the plugs are in hand.
- **The boot:** `date -u` = 2026-09-17T23:02:39Z (CT = UTC−5 → ~18:02 CT). The read budget: 13,017 (the prompt) + 1,735 (the chain) + 2,468 (the newest beat) + 3,387 (the snapshot) + 10,151 (the brief) + 3,487 (the plan §2) + 2,424 (the plan §13) + ≈4,000 (the DR §3 at its decision headings — the section is 17,219 B whole; read whole it would have breached the 45 KB budget, so the three RESOLVED rows were read at their heading lines and the five OPEN rows (D-v75-2/3/6/7/8) only by name — their recommendations stand in the brief's §HELD and are the record's "silence = the recs") = **≈40.7 KB of 45.** pm-lessons: not read at boot (the dispatch line routes it to the ENERGY-READ block — b2 reads THE PREMISE GATE and THE CARD-GREP EXEMPTION there).
- **The five HEADs (one call, 23:0xZ):** core `3af6213` · hivemind `08b8474` · skills `180375f` · bench `f3631cb` · docs `7221ddc` — every porcelain 0, every push count 0, no `.git/*.lock` — **= Nick's STATE AT DISPATCH line, exactly.**
- **The preflight (§2): 12/12 PASS; Check 9 PASS 28/28 identical at the bytes.**
- **The intake at the bytes (§3):** the b8 hivemind card produced `08b8474` = 16 at diff-tree (11 M + 5 A — the order); the CI-2 card produced `3af6213` = 4 M (`.github/workflows/ci.yml`, `.github/workflows/install-smoke.yml`, `distribution/ci/install-smoke.yml`, `distribution/docs/architecture.md` — the order); neither message carries a trailer (grep 0, 0). **CI #252 on `3af6213` GREEN at the instrument, with every upload step THROUGH** — see the correction in §3.
- **The closure counter (§4): 7/20** — `3af6213`'s `Run the bus soak` step SUCCESS on run #252 (id 35279198978), the sample `bus-soak-252` stored (28,916 B, unexpired). Written on the step's conclusion at the instrument, as the dispatch line required.
- **Nick's dispatch text:** filed verbatim at `context/handoff/2026-09-17_v76_dispatch-text_verbatim.md`; the placeholder form `context/handoff/2026-09-17_v76_dispatch-text.md` set EXECUTED (its body untouched).
- **The beat order (§5):** ENERGY-READ is chartered at **b2**, not inside b1 as the plan's §13 bundles it — the b1 card reaches Nick's hands now instead of behind an hour of source reads (arc 52 (ii): a slot-releasing landing outranks a read-only dispatch). The window's deliverable is unchanged.
- **The ONE act handed (§7):** the b1 hivemind card → `HIVE: LANDED <sha>`.

## §1 The instrument readings (the GitHub API, unauthenticated, from the device VM — the repo `nexsys-io/homesynapse-core` is public; the container's egress proxy refuses the repo, the device's does not)
- `GET /actions/runs?head_sha=3af6213…` → 2 runs. **CI #252** (id 35279198978): created 2026-09-17T21:54:04Z, completed 21:57:13Z, conclusion **success**. Job `Build & Check` success — steps `Checkout` ✓ · `Run check` ✓ · `Upload test reports` ✓ · `Post Checkout` ✓. Job `Bus soak (non-gating sample)` success — `Checkout` ✓ · `Run the bus soak` ✓ · `Upload bus-soak reports` ✓. Artifacts: `test-reports-252` 1,926,573 B · `bus-soak-252` 28,916 B — both present, neither expired.
- **install-smoke #60** (id 35279198913): both jobs success (arm64 21:54:09Z → 21:56:27Z; amd64 → 21:56:53Z); every step ✓ including `Upload artifacts (image, .deb, logs)`; artifacts `distribution-artifacts-amd64` 130,318,825 B · `distribution-artifacts-arm64` 129,029,444 B, unexpired.
- **Run #56** (id 34840877827; the sitting's pin): `distribution-artifacts-amd64` 130,293,256 B (expires 2026-09-21T11:59:56Z) · `distribution-artifacts-arm64` 129,009,105 B (expires 2026-09-21T12:00:19Z) — **both present, expiring Monday ~07:00 CT; the sitting on Saturday is inside the window.**
- **The repo's artifact store after the cleanup:** `GET /actions/artifacts?per_page=100` → total_count 61 (the listing keeps expired records), 6 unexpired (#56's two, #60's two, #252's two), 6,021.2 MB listed. Nick's `ARTIFACTS: 62 deleted, 9,195 MB` was read from `gh` before the deletion; the two lists are not the same instrument and were not reconciled row by row (disclosed, §6).

## §2 The preflight, one line per check (the instrument, 2026-09-17T23:0xZ)
1. PROJECT_SNAPSHOT `last-verified: 2026-09-17 (v75 beat 8` = today and = the newest pm-handoff beat → PASS.
2. The plan of record resolves: the chain and the snapshot both name v75 beat 8; the snapshot names `context/planning/2026-09-15_v75_PROGRAM-PLAN_the-six-weeks-to-the-72-hour-run.md`; the file exists → PASS.
3. core `log -1` = `3af6213`; the snapshot's digest names `be4788a` "+ CI-2 on the close card" — one commit behind, the intermediate commit named → PASS.
4. `context/planning/phase-3-milestone-backlog.md` exists (29 DONE rows) → PASS (consistency read at the snapshot's digest, not re-derived row by row — disclosed §6).
5. pm-handoff `## Open Risks` present at line 80 (76 lines); its newest status line dated 2026-09-13 (4 days) → PASS.
6. coder-handoff line 21: `NEXT WU (refuse-to-close pointer): ENERGY-READ` = the brief's Java-slot row → PASS.
7. MODULE_CONTEXT.md: 21 tracked in core, 0 template-empty (every file > 800 B) → PASS.
8. cross-agent-notes: the file is the RETIRED CHANNEL stub (1,024 B), 0 active entries → PASS (nothing to be stale).
9. Check 9: 28 source files (nexsys-hivemind/project-manager, nexsys-hivemind/coder, nexsys-skills/orchestrators/nexsys-frontend) md5-listed on the device; 28 synced files md5-listed in the session; every path present on both sides with the same md5 → **PASS 28/28 identical at the bytes.**
10. strategic-context-map: 103 distinct `.md` cites; every `context/…` path cited resolves on disk (0 missing) → PASS (the cites outside `context/` were not resolved this boot — disclosed §6).
11. Source round-trip: the six ENERGY-READ sources the dispatch names resolve in core's `ls-files` (`ClusterHandlers.java` 1 · `EndpointClassifier.java` 1 · `ReportingConfigurator.java` 1; the other three are b2's greps); the `156/156` test count is the CI instrument's (run #251's `Run check` log, Nick's screenshot), not re-derived → PASS.
12. The archive convention: (1) LIVE/DISPATCH-READY instructions not dated today = the H8-a and R-5B navigator packets only (the sitting's lanes, recorded in §HELD); (2) exactly one LIVE orchestrator prompt (the v67 file); (3) `context/planning/weeks/*` tracked = 0 → PASS.

## §3 The intake at the bytes — the b8 packet's five blocks
| Block | Nick's line | At the instrument | Verdict |
|---|---|---|---|
| 1 the artifact cleanup | `ARTIFACTS: 62 deleted, 9,195 MB`; run #56's two kept | run #56's two artifacts present, unexpired (§1); the store shows 6 unexpired artifacts | BANKED; the kept pair confirmed |
| 2 the CI-2 landing | `CORE: CI2 3af6213`; "CI green with the quota still hit, so the fix is proven" | `3af6213` = 4 M at diff-tree, the order's files; CI #252 success; **every upload step ✓ and every artifact stored** | LANDED and GREEN. **Correction:** the quota was NOT still hit at 21:54Z — the uploads succeeded, so #252 proves the tree builds and the sample runs; it does not exercise CI-2's `continue-on-error`. That clause is proven the first time an upload fails under it and the verdict stays green. Until then CI-2 stands by construction (the yml diff), which is enough to ship on and not enough to call "proven". |
| 3 the hivemind card | `HIVE: LANDED 08b8474` | 16 = 11 M + 5 A at diff-tree; no trailer | LANDED as ordered |
| 4 the Activate email | `ACTIVATE: sent` 09-17 | not re-executable from here (a sent email) | BANKED on Nick's word; the Oct 9 rule stands |
| 5 the v76 dispatch | this session | the pasted text = the placeholder file with the two shas filled; filed verbatim | DONE |

## §4 The closure counter — the seventh sample
The dispatch line: "7/20 on the precedent … confirm the bus-soak step at the instrument before you write 7." Confirmed: run #252's job `Bus soak (non-gating sample)` conclusion success; step `Run the bus soak` conclusion success; the artifact `bus-soak-252` exists (28,916 B). The counter is written **7/20**: `a458a64` · `fed99e8` · `93390f0` · `6bd8508` · `e56f555` · `3d40b5f` · `3af6213`. The sample's XML was not read (the artifact download endpoint needs a token; the hub holds none — disclosed §6): the step's conclusion is the sample's colour of record, as the counter's prior samples were read when their step was green; a sample VETOES a green, never GRANTS one, and this sample did not veto.

## §5 The window's deliverable and the beat order
The plan's §13 bundles ENERGY-READ's charter into b1. This beat does not: the charter needs THE PREMISE GATE's greps at `3af6213` across six sources, the register's rows IR-15/24/25/26, DEVICE-SET's rows and ZIGBEE-GAPS rows 3 and 7, the module's `MODULE_CONTEXT.md` and `module-info.java` — an hour of reads that would have held the b1 card behind them. The b1 card goes to Nick now; b2 opens on ENERGY-READ with the whole window's context in front of it. The plan's §13 sequence otherwise stands (b2 ENERGY-READ · the knockout on a free slot after it · Saturday silent · b3 Sunday's intakes · b4 rehearsal 1's packet).

## §6 What the hub could not re-execute (disclosed)
- The bus-soak sample's XML (`bus-soak-252`) and the arm64 zip's sha256 `11f3a79e…` on run #56 — artifact downloads need a token; the step conclusions and the artifact records are the instrument today.
- The Activate email's sending (block 4) — Nick's word.
- The `gh` listing behind `ARTIFACTS: 62 deleted, 9,195 MB` — a different instrument (pre-deletion) from the API's post-deletion count (61 records, 6 unexpired); not reconciled row by row.
- The milestone backlog's 29 DONE rows and the strategic-context-map's non-`context/` cites — read at the digest, not row by row (as at v75 b1).
- The DR §3's five OPEN rows — read by heading only (the budget trim, §0); their recommendations are carried from §HELD.

## §7 The act handed
The b1 hivemind card (the census computed from porcelain inside the splice; the paths explicit) → `HIVE: LANDED <sha>`. Nothing else is asked; the words open stay open (silence = the recs); Saturday's packets untouched; no re-pin.

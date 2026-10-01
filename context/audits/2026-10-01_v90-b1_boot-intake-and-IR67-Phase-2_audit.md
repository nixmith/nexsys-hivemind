<!--
file: context/audits/2026-10-01_v90-b1_boot-intake-and-IR67-Phase-2_audit.md
purpose: v90 beat 1 — the boot at the byte budget, the preflight (12 checks, one line each), the five HEADs, the intake of the b4 card and the re-verification of IR-67's landing at the bytes, the paste's diff, WUCP Phase 2 for IR-67 (the MODULE_CONTEXT rows at source, the gate, the register row, the docs rows, Open Risks), the act handed.
audience: the v90 hub · the v91 boot (by §0) · DOCS-1's card (§6)
state-type: audit (one beat; WUCP Phase 2)
status: FILED — Thu 2026-10-01 ~12:5x CT (instrument 2026-10-01T17:52:24Z)
-->

# v90 beat 1 — BOOT, INTAKE and WUCP Phase 2 (IR-67) audit

## §0 Verdict
**BOOT PASS 12/12 at the first run; INTAKE BANKED; PHASE 2 CLOSED.** The boot read-set 41.3 KB of ordered ranges (+ ≈ 1.5 KB of locating greps). The five HEADs = the record plus the b4 card Nick ran (hivemind `0f0f2be`), verified at the bytes; core `5b0e20c` re-verified, not re-audited. The dispatch paste byte-identical to its file from line 8. Nick's words: `TIME: 1700` · `HOURS: 5` · `HIVE: LANDED 0f0f2be` · `PR8: closed` · `CREDITS: $409`. IR-67's Phase 2: five MODULE_CONTEXT rows hold at source, no deferred gate, the register's IR-67 row RETIRED, two docs rows carried to DOCS-1's card, OR-BENCH-FENCE-PJ2 stands with its close re-cut to BC7's card. ONE act handed: the b1 card.

## §1 The boot read-set (bytes at `wc -c`)
| Read | Bytes |
|---|---|
| the v67 prompt whole | 13,017 |
| `pm-handoff.md` line 8 · the newest beat (lines 15–20) | 1,320 · 1,295 |
| `PROJECT_SNAPSHOT.md` whole | 3,472 |
| `OPERATOR-BRIEF_for-Nick.md` whole | 12,142 |
| the v89 DR §3c + its Carried row (lines 42–47) | 3,312 |
| THE WEEKS AHEAD §10 (line 98 → end) | 6,759 |
| **the ordered ranges** | **41,317** |
| the locating greps: the DR's and the plan's headings; the lessons' eight heading lines; the preflight reference's Check 9 and Check 12 texts (in the container; not boot bytes) | ≈ 1.5 KB |
| read beyond §1, as blocks sent: the splice library (6,569) and the v89 b1 splice as the FORM; the v87 b3 Phase 2 audit (5,256) as the FORM of §5; the IR-67 return §0 and the intake audit §3; the register's IR-67/108..111 rows by grep | not boot bytes |

## §2 The preflight (one line per check)
- Check 1 PASS — the snapshot `last-verified: 2026-10-01 (v89 beat 4` = the newest beat; same day.
- Check 2 PASS — the plan of record resolves (`2026-09-27_v82_THE-WEEKS-AHEAD_program-and-company-plan.md` on disk); `context/planning/weeks/` untracked (0).
- Check 3 PASS — core HEAD `5b0e20c` = the snapshot's; hivemind `0f0f2be` = the snapshot's `a84dfb3` + the b4 card, as it said.
- Check 4 PASS — the milestone backlogs retired under `context/planning/archive/`; no milestone closed since the last PASS.
- Check 5 PASS — Open Risks: eleven `OR-` names (ADOPT-AWAKE · BENCH-FENCE-PJ2 · BUS-SILENT-DROP · FAILCHAN · HORIZON-UNPLANNED · JOURNALD-PRIO · M13-SDNOTIFY · METERING-VOLUME · NIGHTLY-0902-S31 · REHOMED-OQ · S31-INTERMITTENT) = the snapshot's eleven.
- Check 6 PASS — coder-handoff's newest entry (IR-67, line 17) names the next WU; re-cut this beat to LINK-READ-2 (§5).
- Check 7 PASS — 21 MODULE_CONTEXT.md tracked for 22 `include(` lines; the one without is `spike/wal-validation` (a spike, never a Phase 2 module).
- Check 8 PASS — `cross-agent-notes.md`: the one `active` token is the archived-section header's; nothing live.
- Check 9 PASS — 28/28 identical at the bytes (the three SOURCE trees on the device vs this session's synced trees, per-file md5; the diff empty).
- Check 10 PASS — `strategic-context-map.md`: every cited `.md` basename resolves against the five repos' `git ls-files`; the three unresolved are the map's own placeholders (`YYYY-MM-DD_topic.md` · `YYYY-MM_month.md` · `YYYY-WNN_monDD-monDD.md`).
- Check 11 PASS — `CapabilityPublisher` resolves (`integration-api/…/CapabilityPublisher.java`); the five IR-67 rows' claims spot-checked at source (§5); rest-api's count stays IR-103's open row.
- Check 12 PASS — grep 1 = 0 with the exclusions re-derived from the newest beat (`KREFRESH-1` DISPATCH-READY by the record; the `2026-10-01_` prefix; the IR-67 instruction and first message already terminal); grep 2 = 0 (the v67 prompt the one LIVE); grep 3 = 0.

## §3 The five HEADs (one call; `--no-optional-locks`)
core `5b0e20c` · hivemind `0f0f2be` · skills `e9a77a8` · bench `ede32c9` · docs `7221ddc` — porcelain 0, ahead 0, `main`, no `.git/*.lock`, in all five. Drift: hivemind moved by the b4 card since the record (§4); nothing else.

## §4 The intake (each line with its instrument)
- Core `5b0e20c` (IR-67) — RE-VERIFIED, not re-audited (v89 b4 banked it): `git show --stat`: 20 files = 5 A + 15 M (`diff-tree --name-status`); author Nick Smith, Thu 06:49:17 −0500; parent `8deef4b`; trailer grep 0; `docs/lane-returns` absent from the tree. `CI: 5b0e20c green` is Nick's word (v89 b4) — not re-executable from here.
- `HIVE: LANDED 0f0f2be` (b4) — `git show --stat`: 6 files = the b4 card's 6 (the v90 text · the brief · the chain archive · pm-handoff · the v89 DR · the snapshot); author Nick, Thu 07:00:09 −0500; parent `a84dfb3`; trailers 0. BANKED.
- `PR8: closed` — Nick's word; not verifiable from the container (no repository grant; `gh` absent). BANKED as said.
- `CREDITS: $409` — Nick's word at the paste (Monday's $208 + the top-up, less BH-3's and IR-67's spend); the first cloud dispatch of this window (DOCS-1) carries it; no further ask.
- `TIME: 1700` · `HOURS: 5` — read as the window's END at 17:00 CT (the instrument 12:33 CT at the boot; 12:00 + 5 h = 17:00, the hour the packet is owed by). Refutable by Nick's word; the 1b envelope does not move either way.
- The dispatch text — the paste (`_scratch/v90/2026-10-01_v90_dispatch-as-received.md`, 7,821 B, md5 `b981e0aa7f09…`) against `context/handoff/2026-10-01_v90_dispatch-text.md` from line 8 (7,821 B, the same md5); `diff` exit 0. IDENTICAL. The file flips to PASTED (D-v90-4).
- `PR1: closed` · `BENCH-PULL-5:` · `BASELINE:` · `NIGHTLY:` (Wed's and Thu's) — not said; asked only if they gate an act (none today before the sitting).

## §5 WUCP Phase 2 for IR-67 (`5b0e20c`; the protocol's Steps 0–12)
- **Step 0** the preflight: §2. **Step 1** Coder Phase 1: the five MODULE_CONTEXT rows landed by the lane (`git show --stat 5b0e20c -- '*MODULE_CONTEXT.md'`: `core/device-model` +2 · `integration/integration-api` 4 ± · `integration/integration-runtime` +2 · `integration/integration-zigbee` +2 · `lifecycle/lifecycle` +2; each `grep -c 'IR-67'` ≥ 1 — the api's second hit retires the M4.C round-trip GOTCHA by name). Spot-checks at source: device-model "63 public types; 65 `.java` incl. package-info + module-info" = `git ls-files … | grep -c '\.java$'` 65, `^public (class|interface|record|enum…)` 63 ✓; lifecycle's filter FOUR types — `EventTypes.CAPABILITY_ADDED` :80, `case CapabilityAdded added` :92, the orphan WARN :98 ✓; the runtime's `new DiscoveryServices(new SupervisorCapabilityPublisher(` at `StandardIntegrationSupervisor.java` :1095 ✓; the zigbee slice's `zigbee.capability_reconcile` tokens (:115 Javadoc; `_unbound` :673 DEBUG; `_ias_relearned` :715 WARN) and 4 `reconcileCapabilities(` sites ✓; `new CapabilityRemoved(` in `src/main` = 0 and `SupervisorCapabilityPublisher.publishRemoved` :112 throws — `removal=none` (D-v88-19) holds at source ✓. The coder-handoff entry (line 17, v89 b3) stands; its heading gains the landing and this close; the NEXT WU pointer → LINK-READ-2. No coder-lessons entry from the cloud lane (its return §6 says it writes nothing into the hivemind; the hub carried its entry at v89 b3).
- **Step 2a / Step 8** Deferred Build Gate: **none** — the return §0: `./gradlew check` `BUILD SUCCESSFUL in 1m 46s`, the six gate lines EXECUTED; CI green on `5b0e20c` (Nick's word, v89 b4). Nothing opens under Open Risks for it.
- **Steps 2, 3** the traceability index and `phase-3-milestone-backlog.md` carry no IR rows (the v87 b3 reading, as for PJ-2 and IR-61b); IR-class units live in the register and THE WEEKS AHEAD §2.
- **Step 4** Open Risks: OR-BENCH-FENCE-PJ2 STANDS; its Owner line gains the v90 b1 clause — BH-3 landed (`ede32c9`), IR-67 landed (`5b0e20c`), the Pi's clone stays at `40412f9`, the risk closes at BC7's card (Fri) which carries PJ-2 + IR-67 together, grades the first endpoint pairing (IR-102 a) and reads IR-67's attestation. No new OR: IR-110 (the third IAS arm) is fenced by the no-adoption rule until IR-15; IR-111's two rows are hardening, not risk. The count stays eleven.
- **Step 4 (the register)** IR-67's row → RETIRED v90 b1 at `5b0e20c`; the residue named in the row: IR-108/109 (the seam's documented gaps), IR-110, IR-111; the bench attestation rides BC7's card. The status line gains the segment. IR-108..111 stay OPEN as minted (v89 b2/b3).
- **Step 5** pm-lessons: no mint — the lane's nine deviations were all [INFO] and the intake's findings are register rows; the GRANT lesson (2026-09-30) stands OPEN as the carrier for the next cloud first message (DOCS-1's).
- **Step 6** the snapshot: rewritten this beat. **Step 9** drift: the five porcelains 0, ahead 0. **Step 10** Check 9: 28/28. **Step 11** the open-item sweep: `cross-agent-notes.md` nothing live. **Step 12** this file.
- **The docs rows → DOCS-1's card (§6).**

## §6 DOCS-1's list (the v87 b3 §4 eleven + IR-67's two = 13 rows)
1. IR-81 — Doc 03 §3.8's status line. 2. AMD-53 :78. 3. Doc 02 §3.5. 4. Doc 03 §9's `PT…` (D-v84-13). 5. IR-100's Doc 01 §4.4 row. 6. D4's fourth WARN token. 7. IR-95's §3.9 outcome vocabulary. 8. IR-97's `event_time` definition. 9. F3's payload-key row (`permit_join_opened/closed`). 10. F4's close-silence row (Doc 03 §9). 11. the `permit_join_duration` schema text (IGNORED since PJ-2; its removal is the `CONFIG-ERROR:` decision, IR-90). **12. AMD-59's status row → "implemented" at `5b0e20c` (the post-adoption capability path: the boot-time reconcile, the runtime's publisher, the projection's consumer; `capability.removed` typed, never published — D-v88-19).** **13. Doc 03's `capability.added` consumer row — `RegistryProjectionSubscriber`'s filter is four types; `RegistryProjection.applyCapabilityAdded` the fourth apply (REG-INV-1); the orphan and the already-carried arms NO-OP (AMD-59-INV-03).** IR-108 (rest-api renders no capability list) and IR-109 (the seam's two Javadoc gaps) are core-tree rows, not docs rows — they ride the removal unit.

## §7 Layer 2
Re-executed: the five HEADs, porcelains, push counts, branches and locks; `5b0e20c`'s stat, name-status, author, parent and trailer grep; `0f0f2be`'s stat, author, parent and trailer grep; the paste's md5 on both sides and the `diff`; Check 9's 28 md5s on both sides; Check 12's three greps with the exclusions; Check 5's eleven names; Check 10 at a basename index of the five repos; the five Phase 2 spot-checks at source. Not re-executed: PR #8's state and the CI run (Nick's words); the Pi (BENCH-PULL-5, the nightly, the baseline — Nick's hands); `./gradlew check` (the Gradle distribution is outside the container's allowlist — v89 b3's disclosure stands).

## §8 The act handed
1. The b1 card (`_scratch/v90/b1/card_b1.txt`; 10 paths; gated) → `HIVE: LANDED <sha>`. The 1b packet is beat 2's (by 17:00 CT); nothing at the rig before it is in Nick's hands.

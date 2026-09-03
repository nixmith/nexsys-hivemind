<!--
file: context/audits/2026-09-02_F-R4-1_intake_two-layer-audit_v61-beat-9.md
purpose: The hub's two-layer intake audit of the F-R4-1 Coder return (context/audits/2026-09-02_F-R4-1_return.md, 12,286 B; interview-on-rejoin, R-10 Row 10 RULED (a)). Layer 1: the return's §0 + §1–§5 read critically against the instruction. Layer 2: the hub's own re-execution at the bytes — the core porcelain, the 13-path diff, the source facts the return leans on (the exception hierarchy, the caller of openPermitJoinWindow, the codec idiom, the token census, the TCJ re-pin's assertion lines, line endings).
audience: Nick (the commit is his hands) · the Coder lane · the spine
state-type: intake audit (v61 beat 9, post-close)
status: FILED. VERDICT: ACCEPT (two [REVIEW] items ruled below; one cosmetic stamp defect). The commit msg file for Nick's hands: ../_scratch/2026-09-02_core_F-R4-1_commit-msg.txt (stages exactly 13 = 12 M + 1 A). Gate of record: CI on the push (law 16). R-4b criterion 0 = the 0x0061 hop's first silicon ⏺.
-->

# F-R4-1 intake — two layers (v61 beat 9)

## §0 Verdict
**ACCEPT.** The return is §0-first, within cap (12,286 B ≤ 12 KB by the instruction's own reading of "12 KB" as 12,288), census-exact, red-first staged, fence-attested, and honest about the one unmeasured surface. Every claim the hub re-executed held. The two `[REVIEW]` items are ruled in §3 (both ACCEPT-as-shipped; the T5b re-index charters as a follow-on row, not a change to this WU). One cosmetic defect: the return's filing stamp (23:30 CDT) runs ahead of the file's own mtime (04:17:16Z = 23:17 CDT) — the lane's mental clock; no content depends on it.

**What this WU buys.** The shipped pipeline started adoption only at a ZDP Device_annce; a mains router that rejoins on its own authority (R-3a: the whole mains fleet after the outage; R-4 D-g: the Hue-class device at nwk 0xf87d) reported forever as `ingestion_unknown_sender`. Now, inside an open permit-join window, that device is resolved (cache → coordinator address table over EZSP 0x0061) and admitted into the SAME interview → proposal → adopted path; an accepted 0x0024 rejoin admits the same way without a lookup. Outside a window nothing changes but one INFO per nwk per epoch. Relink ≠ adopt holds: an adopted device never re-enters. This is the WU that makes R-4b (four-of-four) reachable and C-002 mintable.

## §1 Layer 1 — the return read critically
- **Doctrine honored as ruled.** Two triggers (H-ii evidenced, H-i cheap) → one path (`cache.recordAnnounce` + `interviewQueue.schedule(…, REJOIN)`), never a bypass; adoption still requires the interview, the proposal, and the `adopt_devices` consent. The M9.4-TCJ §A.2 pin is amended for exactly one case and every other sentence survives — in the source Javadoc, in MODULE_CONTEXT, and in the TCJ test wording.
- **Red-first is real, not ceremonial.** HEAD compile-red on exactly the four missing seams; stage A (seams declared, hooks inert) turns compile-red into a 15-test behavior-red the hub can read scenario by scenario; stage B 581/581. The two green-by-construction rows (T6, the queue plumbing) are disclosed, not hidden.
- **The instruction's expectations met.** Census ≈6–8 M + N test A → 7 M inside (6 main + MODULE_CONTEXT) + 5 test M (each forced: two by the abstract listener methods, the TCJ re-pin, T8's home, the queue pins) + 1 A. Zero module-info / build / catalog / schema / event-mint / payload diffs — the frozen event-log contract is byte-untouched (`source` rides the log line only; the additive payload key is a proposal).
- **The one new silicon surface is named, isolated, and instrumented.** `FRAME_LOOKUP_EUI64_BY_NODE_ID = 0x0061` lives in a BENCH-VERIFY block binding code and tests (arc-convention 16); a miss logs the status byte so R-4b needs no second run to adjudicate criterion 0.
- **Deferred Build Gate: YES, disclosed correctly.** `./gradlew check` (ArchUnit, app + lifecycle suites) not run on the desk; owed against Nick's commit; CI on the push is the gate of record.
- **Stamp discipline.** The lane wrote "23:30 CDT"; the file landed 23:17 CDT. Cosmetic; the clock law (v61) applies to lanes too — the next Coder brief carries the `date -u`-first line for its filing stamp.

## §2 Layer 2 — the hub's re-execution at the bytes (instrument: device_bash on the mounted tree, 04:19–04:31Z)
| # | Claim | Re-executed | Result |
|---|---|---|---|
| 1 | Exactly 13 at porcelain, HEAD `f519f42`, nothing staged | `git --no-optional-locks status -sb` + `log -1` | **13 (12 M + 1 A)**, `main...origin/main` even, HEAD `f519f42`. Paths match the return's block. |
| 2 | 712 insertions / 33 deletions across 12 M; the new test class 1,118 lines | `git diff --stat` · `wc -l` | 712(+)/33(−) · 1,118 lines. |
| 3 | The command timeout PROPAGATES past the adapter's catch (watchdog arm), not swallowed as "unresolved" | `EzspCommandTimeoutException.java:15` | `extends RuntimeException` directly — NOT a subclass of `EzspCommandException`; the adapter's `catch (EzspCommandException \| EzspFormatException \| IllegalStateException)` cannot catch it. **Claim holds.** |
| 4 | The two `HashSet`s are run-thread confined (no lock, no `synchronized`) | callers of `openPermitJoinWindow()` in main code | ONE caller, `ZigbeeIntegrationAdapter.java:434`, on the production `run()` thread (the `permitJoinDeadline` Javadoc says the same); the hooks fire from the ingestion cycle on that thread. **Holds.** Corollary the hub notes: in main code the window opens once per run (no re-open path), so "per window epoch" = per run today; the T7 pin keeps the clearing correct if a re-open surface lands later. |
| 5 | `lookupIeee` uses the codec's status-width seam like `lookupNetworkAddress` | `EzspCodec.java:194/:208`; `EzspCoordinatorProtocol.java:658/:666` (the precedent) vs `:1640/:1647` (the new) | Same idiom, same offsets. **Holds.** |
| 6 | The TCJ re-pin changed wording only, assertions byte-unchanged | `git diff` on the TCJ test filtered to `assert` lines | **0** assertion lines in the diff. **Holds.** |
| 7 | Five new log tokens, test-asserted | grep per token, main vs test | `rejoin_candidate:` 1/13 · `rejoin_ignored_window_closed` 1/11 · `rejoin_candidate_unresolved` 2/5 · `lookup_eui64_failed` 2/5 · `rejoin_candidate_ignored` 2/6 (main/test occurrences). **Holds.** |
| 8 | LF-only | `grep -q $'\r'` on all 13 | all LF. **Holds.** |
| 9 | `adoption.deviceIdFor(IEEEAddress)` exists (the relink ≠ adopt gate) | `ZigbeeAdoptionSlice.java:519` | exists, `Optional<DeviceId>`. **Holds.** |
| 10 | 581/581 in-lane | not re-runnable at the bridge (no JDK/Gradle in the mount VM) | **DISCLOSED, not re-executed** — CI on the push adjudicates (law 16). |

Not re-executed, disclosed: the bellows source read (the lane fetched `dev`; the hub takes the constant on the lane's citation plus the 0x60/0x26/0x22 cross-check it re-derived; R-4b's first ⏺ is the only ground truth that matters).

## §3 Rulings on the return's §3
- **[REVIEW] T5b — the adopted-but-cache-unindexed corner.** RULED: ACCEPT AS SHIPPED (spec §5 "never re-enters" honored literally; the DEBUG note is the honest observable). The cache re-index (`recordAnnounce` only, no schedule) is CHARTERED AS A FOLLOW-ON ROW — F-R4-1b — dispatched only if R-4b observes the corner on hardware (a fresh cache file or an F-6 invalidation on an adopted device). Not a change to this commit.
- **[REVIEW] `CoordinatorProtocol` +1 public method.** RULED: ACCEPT — instruction-sanctioned (the M9.4-TCJ precedent); coordinator-neutral (INV-CE-04); a ZNP binding reads its own table.
- **[INFO] ×4** (the two extra tokens; the structural dedup via the IEEE-keyed map; no fake protocol in test-support; no reason slot on `InterviewAttempt`): all recorded; the follow-ons (1)–(5) of the return's §4 enter the docket as candidate rows, none chartered before R-4b.

## §4 What rides forward
1. **Nick's commit** (his hands): the msg file `../_scratch/2026-09-02_core_F-R4-1_commit-msg.txt`; stages exactly the 13; push; the CI verdict banks as one spine line.
2. **R-4b's packet** now has its criterion 0 (the 0x0061 hop's first ⏺, the log grammar in `integration/integration-zigbee/MODULE_CONTEXT.md §F-R4-1`) and its predictions (the return §4). O-2 is CLOSED (measured on the held card 2026-09-03 03:10Z — see the beat-9 spine line), so R-4b's step 0 is no longer owed.
3. **The next Coder brief** carries the lane clock law (`date -u` first for the filing stamp).

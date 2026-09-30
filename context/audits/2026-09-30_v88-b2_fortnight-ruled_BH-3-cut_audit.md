<!--
file: context/audits/2026-09-30_v88-b2_fortnight-ruled_BH-3-cut_audit.md
purpose: v88 beat 2 — `HIVE: LANDED 5351870` at the bytes; the v87 hub's read filed and its rows ruled on Nick's words (THE WEEKS AHEAD §0 + §10); BH-3 cut through the eleven greps, THE PRIOR-LEDGER GATE and the harvest dry-run's disclosure; IR-107; the acts handed.
audience: the v88 hub · the v89 boot (by §0) · the BH-3 intake (its §2 counts are the baseline the lane re-runs)
state-type: audit (one beat)
status: FILED — Wed 2026-09-30 ~08:2x CT (instrument 2026-09-30T13:28:39Z)
-->

# v88 beat 2 — the fortnight ruled; BH-3 cut

## §0 Verdict
**INTAKE BANKED; THE FORTNIGHT RULED; BH-3 DISPATCH-READY.** `5351870` = HEAD, 8 files, trailers 0, porcelain 0 (before W-SKILLS-10's launch). The read filed verbatim (11,433 B with its frontmatter; the body's md5 as received `2c2700d18244`); six words ruled at the recs by Nick's framing, plus his three edits to the frame (D-v88-7..14). BH-3's charter (18,327 B) and first message (5,287 B) cut on eleven greps run in the hub's container; one premise corrected (the ULID route). IR-107 opened. W-SKILLS-10 launched (slot 1). The next act: the b2 card, then BH-3's paste.

## §1 The intake
- `HIVE: LANDED 5351870` — `git show --stat`: 8 files (the b1 card's 8); the message's trailer grep 0; HEAD; porcelain 0; ahead 0. BANKED.
- The read — the upload copied byte-for-byte under a 7-line frontmatter into `context/strategy/2026-09-30_TWO-WEEKS_strategic-read_for-v88.md`; its §5 banks `TR3:` and `HIVE: LANDED 92f7fb6` (already banked b1) and names `NIGHTLY:` and `BASELINE:` open (still open).
- Nick's edits to the read's frame (his words outrank the read's): the rig sitting ≤ 4 h and never past 21:30 CT (the read: ≤ 2 h, never started past 20:15); the close window at 21:30 (the read: 20:30); +$250 credits in about a week (the read: $208 only). Recorded D-v88-9/10/12.

## §2 BH-3's eleven greps, run in the container (core `8deef4b` at `/home/claude/nexsys-io/homesynapse-core`; bench `d093a95` at `/home/claude/nixmith/nexsys-bench`; both public, shallow clones)
| Row | The grep | Count | Note |
|---|---|---|---|
| 1 | `integrations/{integrationId}/permit-join` in `api/rest-api/src/main` | 5 | `RestFilters.java:520` the route; `:492` its Javadoc; `PermitJoinEndpoint.java:28`; `ProblemType.java:166`; `PairingWindowPort.java:15` |
| 2 | `IntegrationId.parse(ctx.pathParam` in `PermitJoinEndpoint.java` | 1 | :119; a malformed id → 400 (:122) |
| 3 | `6V1CMGY2HKF4H1FGZ4H7F257FS` in `*.java` | 1 | `IntegrationIdsPinTest.java:36` (`PINNED_INPUT_HEX db0b290f0a33792217c3e489de229df9`); the hub's Python re-derivation from `IntegrationIds.java:58`'s documented hash → the same 26 characters and hex |
| 4 | `integration.launched: integration_id=` in `StandardIntegrationSupervisor.java` | 1 | :563 — `integration_id={} integration_type={} io_type={}` |
| 5 | `"durationSeconds"\|"reason"` in `PermitJoinEndpoint.java` | 5 | the hub's first guess was 4 — corrected by the run (:31 Javadoc · :138 · :152 · :220 · :221) |
| 6 | `data.put("` in `PermitJoinEndpoint.java` | 6 | the six response keys (:219–:224) |
| 7 | `zigbee.permit_join_` in `ZigbeeIntegrationAdapter.java` | 5 | :99 (Javadoc) · :915 key_ignored · :958 opened · :1039 close_failed · :1060 event_conflict — the hub's first guess was "≥ 4"; pinned at 5 |
| 8 | `"permit_join_opened"\|"permit_join_closed"` in `core/event-model/…/EventTypes.java` | 2 | :306 · :312 |
| 9 | `Authorization: Bearer $(api_token)` in `tools/bench.sh` | 3 | :74 · :75 · :77; `api_token()` :18 |
| 10 | `zigbee.permit_join_opened` in `scenarios/boot-health.yaml` | 3 | the hub's first guess was 2 — :20 (the citation comment) · :21 · :67 (the forbidden entry) |
| 11 | `permit\|pairing` in `tools/nightly.sh` (`-i`) | 0 | no pairing step to re-point |
Also read at source for the charter: the request bounds (`PairingWindowRequest` 1–254 s, reason ≤ 120), the 401 (`WWW-Authenticate: Bearer`, `RestFilters.java:819`), the 409/503 (PJ-2's T6 in the return :93), `bench.sh`'s `do_start`/`do_health`/usage (:1–:30, :83–:120), the BENCH-PULL-4 block's form (`…CORPUS-1_…operator-card.md:27`), the bench selftests in the container: `selftest: 42 check(s), 0 failure(s)` · `verify72h selftest: 26 check(s), 0 failure(s)`.

## §3 The gates on the cut
- **THE PRIOR-LEDGER GATE (law 15; #31).** Twelve strings BH-3's exit and landing reuse, grepped across `2026-09-28_PJ2_return.md` · `2026-09-28_v86-b3_PJ2_intake_audit.md` · `2026-09-28_v86_POST-CLOSE_landing-note.md`: `git switch -c` 0/0/0 · `push -u origin` 0/0/0 · `commit -F` 0/1/0 · the trailer sentence 0/0/1 · `diff --stat` 2/0/0 · `restore --staged` 0/0/1 · `docs/lane-returns` 0/3/2 · `user.name` 0/0/0 · `RETURNED` 1/2/0 · `shallow` 0/0/0 · `checkout --detach` 0/0/1 · `stop-hook` 0/0/0. Every hit is a CARRIED FIX (IR-101's `restore --staged` then `rm` for the return directory; the trailer grep before `commit -F`; the return on the branch under `docs/lane-returns/`) or the unchanged census read (`diff --stat`); the defective string of record — the `;` before `git commit` — is absent from BH-3's exit and from the gated landing card it will get.
- **THE HARVEST DRY-RUN (pm-lessons 2026-09-28).** The charter's harvest is the lane's own greps (§2, all eleven run here) and the verb's log read (`integration.launched` · `zigbee.permit_join_opened`). The corpus in git (`corpus/runs/2026-09-28_rehearsal-1/`: MANIFEST · report · verdict · window; 220 K) carries NO `app-log.jsonl`, so neither token was dry-run against a real bench log from here — DISCLOSED in D-v88-15 and in the charter's §0 (NOT-OBSERVED-HERE names BC7). The selftest builds its fixture log from the source form (:563, :958). BC7's Block 0 prints the live `integration.launched` line; a shape difference there is a result for the hub.
- **THE PREMISE GATE.** The plan's `/integrations/zigbee/permit-join` was an unmeasured hop; the route's path parameter is parsed as a ULID (row 2). Corrected in THE WEEKS AHEAD (both occurrences) and named in the charter (§2 row 3).
- **THE ONE-WAY-DOOR REVIEW (D-v82-10).** BH-3 opens no door: no event type, no schema, no migration byte, no public API (a bash verb, a selftest, a forbidden token, a README section, a status line). No independent review is owed for a bench tools lane; the hub's own second read of the charter against the source stands as §2.

## §4 The rulings (the DR §3b, D-v88-7..16)
The frame; `CAP: three`; the rig envelope (≤ 4 h by 21:30 CT); the three windows (07:00 · 13:00 · 21:30); `RUN: oct30-two-dry`; `JAVA-ROUTE: split` with the credits; `RESEARCH-LH: now` · `OUTREACH: this-week` · `LOADS: declared`; the pace's fence; BH-3 cut; the acts. THE WEEKS AHEAD: §0's hours line re-cut; §2 row 8 and §9 row 1's route corrected; §10 appended (6,760 B); the status line.

## §5 IR-107 (opened)
verify72h's attestation A1 reads `zigbee.permit_join_opened` as "a key at boot → red" (`tools/verify72h/README.md:72`; `grader.py:193`). Since PJ-2 the key never opens a window (`permit_join_key_ignored`), so `permit_join_opened` in a graded span now means an ENDPOINT window (red for THE RUN by design; expected in a rehearsal that pairs). VERIFY-72H-B re-cuts A1 into the two reads; until then a rehearsal's grade carries an A1 red its packet declares. → the register row.

## §6 Layer 2
Re-executed: the b1 commit's stat and trailer grep; the read's md5 before and after the copy; the eleven greps (each once, the counts above); the ULID derivation in Python against the pin test; the prior-ledger greps; the bench selftests in the container; every anchor of THE WEEKS AHEAD asserted once by the splice; the caps probed in one block. Not re-executed: any bench read (no Pi from here); the corpus boot-log tokens (absent from git — disclosed); W-SKILLS-10's boot (Nick's `LAUNCHED` word is the instrument; its porcelain check is its own).

## §7 The acts handed
1. The b2 card (`_scratch/v88/card_b2.txt`; 11 paths; gated; the lane's files fenced) → `HIVE: LANDED <sha>`.
2. BH-3's first message (slot 2) → `BH3: dispatched <HH:MM CT> cloud · CREDITS: $<n>`.
3. Then `BASELINE:` · `NIGHTLY:` in the gaps; IR-67 at beats 3–4; OUTREACH-1's first call today.

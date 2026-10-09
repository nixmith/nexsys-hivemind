<!--
file: context/audits/2026-10-09_v102-b3_HERO-U2a_intake_two-layer_audit.md
purpose: The hub's two-layer intake of HERO-U2a's return (`context/audits/2026-10-09_HERO-U2a_return.md`, 7,189 B; RETURNED Fri 2026-10-09 17:57 CT, 24 minutes after dispatch): the return read critically, then the hub's own reads at `da9ca3d` of the cites the design stands on, the mock's fifth state beside "Not responding" (the review's refutable-by), FIELDS.md's NOT-ON-WIRE rows against the wire's eight keys and the mirror's four; the verdict; the two notes; THE "QUIET" CARRIER framed as an H10 for Nick's word (the question AVAIL-API-1 must rule before it is cut). Filed v102 beat 3 (Fri 2026-10-09 ~18:1x CT; instrument 2026-10-09T23:19:44Z; D-v102-13/14).
audience: the hub (this close; v103's mock-review beat — Nick's Q1–Q8 and `CARRIER:` words; AVAIL-API-1's cut) · Nick (the verdict; the H10)
state-type: intake audit (two-layer)
status: FILED v102 beat 3 — VERDICT ACCEPT-WITH-NOTES; the design folder's card DISPATCH-READY (`_scratch/v102/b3/card_core_design.txt`); AVAIL-API-1 waits for `CARRIER:`
-->

# HERO-U2a — intake, two layers (v102 b3)

## §0 Verdict
**ACCEPT-WITH-NOTES.** Four files under `web-ui/dashboard/design/recovery-card-v1/` (SPEC.md 43,228 B · FIELDS.md 4,039 B · states.html 69,788 B · README.md 1,234 B); `web-ui/dashboard/src` untouched (porcelain 0); no name but `{{NAME}}` (0 files; `{{NAME}}` ×3 in the mock's header); no script and no external resource in the mock; P1–P5 HOLD at the hub's bytes; the review's refutable-by held — the fifth state "Not heard from since startup (not asked)" (×8) stands beside "Not responding since … (asked twice, no answer)" (×16) with a different verb, glyph and hue; the state table 6 rows × 3 stages, 18/18 cells, three honest "not sayable" cells named. FIELDS.md is the row of record: IN-MIRROR 5 (+ two joins) · ON-WIRE-NOT-IN-MIRROR 3 · NOT-ON-WIRE 10, every row cited at `da9ca3d`; the hub's six gaps 1–4 and 6 CONFIRMED, 5 CONFIRMED as a gap and REFUTED as a key (re-sourced to `lastProbeAt` null ∧ UNAVAILABLE). Two notes (§4). The design folder lands by Nick's card; SPEC §12's eight questions are his, in one batch at v103's mock-review beat; **AVAIL-API-1 is cut only after `CARRIER:` (§5).**

## §1 Layer 1 — the return read critically
- The form holds: §0 the card (the instrument limit; the census; P1–P5 adjudicated with cites; the defaults; the NOT-ON-WIRE list; the questions), §1–§4; `RETURNED … 7189` the last line; 7,189 B under the 10 KB cap; 0 trailer strings.
- P4's three findings are corrections of the CHARTER's table (the hub's premises), each with a cite — the prediction did what it was pre-registered for.
- §4 refuses to close: HERO-U2b (the mirror bump + the card on mocked fields; rows 1–2) named; row 3 waits on Q3/Q6; row 4 on AVAIL-API-1. One observation outside the lane (Q5 (c): one probe at boot for a seeded-dark mains device) — read in §4 below.

## §2 Layer 2 — the hub's own reads (Fri 2026-10-09 ~18:0x CT; `git show da9ca3d:` on the device)
| Claim (the return / FIELDS.md) | The hub's read at `da9ca3d` | Holds |
|---|---|---|
| the wire's `availabilityReason` is the reason name LOWER-CASED (`A:2080–:2081`) | `String reasonToken = reason == null ? null : reason.name().toLowerCase(Locale.ROOT);` | ✓ — the charter's "the NAME" was wrong; IR-134's own exhibit (`reason=ping_timeout`) had said so |
| a sixth value `LEAVE` (`AvailabilityReason.java:48–:49`) | `/** Device sent a ZDO Leave notification … */ LEAVE` | ✓ |
| a reply to a device that stays AVAILABLE publishes nothing (`T:599–:600`) | `state.probeMisses = 0; if (state.state == target) { changed = false; }` | ✓ — steady-state "Quiet (asked, answered)" has NO wire signature today |
| the sweep skips UNAVAILABLE (`T:465–:467`) | `if (state.state == State.UNAVAILABLE) { continue; }` | ✓ — a device seeded dark is never asked |
| the seed (`T:284–:291`) | `available != null` → AVAILABLE/UNAVAILABLE with reason FRAME_RECEIVED / SILENCE_TIMEOUT; `available == null` → UNKNOWN (probed) | ✓ — and see note N1: the seeded-dark device carries `silence_timeout`, not null |
| `PROBE_MISSES_TO_DARK = 2` (`T:110`) | as cited | ✓ |
| NOT-ON-WIRE rows absent from the wire and the mirror | the eight `summary.put` keys at `ListEntitiesEndpoint.java:194–:216` (`entityId · availability · stale · deviceId · lastReported · availabilityReason · lastSeenAt · link`) and `contract.ts:239–:275` (`availability · stale · deviceId? · lastReported?`; `EntityState` adds `lastChanged · lastUpdated · staleAfter`) | ✓ — none of `reportIntervalSeconds · silenceLimitSeconds · lastProbeOutcome · lastProbeAt · probeMisses · availabilityClass · integrationId · ieeeAddress` is on either |
| the mock: the fifth state beside R3; no script; no external | `grep -c '<script'` 0 · `https?://` 0 · "Not heard from since startup (not asked)." ×8 · "Not responding since 6:52 am (asked twice, no answer)." ×16 · "Quiet since 6:48 am (asked, answered)." ×6 · `{{NAME}}` ×3 | ✓ |
| `src/` untouched; no other name | `git status --porcelain -- web-ui/dashboard/src` → 0 · `grep -ril` for the candidate names → 0 files | ✓ |
| the state table 6 × 3 | SPEC §3: the six rows (R1–R5 + the open-vocabulary arm) × S1/S2/S3; "18 filled (R2 S1, R4 S1, R4 S3's null-interval arm honest 'not sayable')" | ✓ |

## §3 Not re-executed; disclosed
The a11y contrast pairs (the lane computed them; the hub read the claim "all ≥ 4.5:1"); the copy table's 61 keys' reading grades; the headless render of the mock (the hub grepped its strings, did not view it). These are the mock-review beat's reads (v103) when Nick looks at the mock.

## §4 Notes (the record's, not defects)
- **N1 — the fifth state at S2.** A device seeded UNAVAILABLE carries `silence_timeout` as its reason (`T:289–:290`) and the store's last `lastSeenAt`, so on the wire today it is indistinguishable from "Not responding by silence"; the card's S1 form (`availability = UNKNOWN` → the fifth) catches only the `available == null` seeds — which the sweep DOES probe. The fifth state is reliably sayable at S3 (`lastProbeAt` null ∧ UNAVAILABLE — Q5 (a)) or after Q5 (c), one probe at boot for seeded-dark mains devices, which would retire the state on silicon. The SPEC says so (R5 · Q5); the mock's P5 is the S3 form. The hub's view: Q5 (c) is a tracker behavior change — the same family as IR-56's surviving half (the 90-s post-restart read at the class's naming time, already in dry-run #1's packet) — and belongs to AVAIL-API-1's review or a sibling unit, never to the FE. Nick's word.
- **N2 — Register C over the charter's "we"** (Q1): the lane's default reads better and keeps the name out of every card string; the charter's sample sentences were illustrative, not copy. No block.

## §5 THE "QUIET" CARRIER — the H10 for Nick's word (the question AVAIL-API-1 must rule before it is cut)
```
ESCALATION TO NICK
Task: AVAIL-API-1 — the fields the recovery card reads (FIELDS.md §3)
Question: how does a probe's OUTCOME reach the read-API, given that a probe answered by a device that stays AVAILABLE publishes nothing today (T:598–:600) — so "Quiet since <t> (asked, answered)" has no wire signature?
Options:
 (a) an event per probe outcome — every ping, answered or not, publishes (an AvailabilityChangedEvent v3 or a ProbeEvent). Cost: the store grows one row per probe per device — the floor class (the S31, the Hue) probes every ≈ 60 s of silence (up to ≈ 1,440/day/device while silent), the metering class every ≈ 660 s (≈ 130/day); the derived-write rate limit is in the path. Buys: every probe in the record (the run's dataset for "asked twice" sentences; the household-sentence test of D-v101-25 met from the files alone). Risk: volume on the floor class; the projection's write rate.
 (b) a read-side field — rest-api reads lastProbeOutcome/lastProbeAt/probeMisses/silenceLimitSeconds/availabilityClass from the tracker's memory through a NEW port the zigbee module exposes (a module edge rest-api does not have today — D-v101-32). Cost: a port + module-info edits; no store growth. Buys: live truth at read time. Risk: not in the record (fails the household-sentence test); lost at restart (the fifth state's own cause).
 (c) the last probe carried on AvailabilityChangedEvent v3 only on TRANSITIONS, plus the contract fields. Cost: smallest. Buys: lastProbeAt/outcome at the dark edge; the contract sentence. Risk: R2 stays "not sayable" at steady state — the lane's finding is not answered.
 (d) hybrid — the contract fields (class · reportIntervalSeconds · silenceLimitSeconds) in a v3 event emitted at interview/boot (static per device), AND one probe_answered event per SILENCE EPISODE (published only when the silence limit has passed and the probe is answered — the first answer of an episode, never every probe). Cost: bounded — at most one event per episode per device; the v3 schema + upcaster; the projection's three reads. Buys: R2's exact words ("asked at <t>; it answered" = the episode), lastProbeAt for the fifth state's S3 test, the record whole. Risk: a class that lives in permanent silent→probed→answered cycles (the Hue today) makes "per episode" = "per probe" for that class — the volume question returns for it.
PM recommendation: (d) — the episode is the unit VOCAB: a already names (asked, answered); the record stays whole; the volume is bounded by episodes, not probes.
Refutable-by: SOAK-NIGHT-2's P3′ tonight — if the floor-class probe lines show a device answering at every 60-s probe for hours (one episode = hundreds of probes), (d) degrades to (a) for that class and the ruling needs a per-class rate cap or (b) for the floor class.
Blocking: AVAIL-API-1's cut only — HERO-U2b rows 1–2 (the mirror bump; the card on mocked fields) proceed on any option; row 3 waits on Q3/Q6; the word by Saturday's mock-review beat: `CARRIER: a | b | c | d`.
```

## §6 The landing and the words
- The design folder lands by Nick's card `_scratch/v102/b3/card_core_design.txt` (core; `git add -A web-ui/dashboard/design/recovery-card-v1`; four files; the message `_scratch/v102/b3/2026-10-09_core_HERO-U2a_design_commit-msg.txt`; the frontend gate is not touched by design files — CI on the push is the gate of record) → `CORE: LANDED <sha>` · `CI: green | red <run>`. BC9a is unaffected (it pins `37f05a9` BY SHA).
- Nick's words at v103's mock-review beat: `U2A: adopt-all-recs | Q<n>: <letter> …` (SPEC §12 Q1–Q8; the lane's recs are the defaults) · `CARRIER: a | b | c | d` (§5). HERO-U2b's charter is cut after `U2A:`; AVAIL-API-1 after `CARRIER:` and the one-way-door review.

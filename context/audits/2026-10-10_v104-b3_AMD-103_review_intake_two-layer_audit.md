<!--
file: context/audits/2026-10-10_v104-b3_AMD-103_review_intake_two-layer_audit.md
purpose: The two-layer intake of AMD-103's independent review (v104 beat 3): the reviewer's verdict and findings (layer 1); the hub's own reads at the bytes of every BLOCKING citation, the scripted application of the edits, and the focused re-read (layer 2); the text handed to Nick.
state-type: audit (two-layer)
status: FILED v104 beat 3 (Sat 2026-10-10 ~15:4x CT; instrument 2026-10-10T20:42:02Z)
-->

# AMD-103's independent review — intaken two-layer (v104 beat 3)

## §0 The card
- **The reviewer:** a fresh agent that had not seen the drafting (D-v101-33's form). It was relaunched 14:25 CT on `REVIEW: relaunch` (D-v104-17) against DRAFT v2 (md5 `6b0ea845…`) and the brief `_scratch/v104/b3/AMD-103_review-brief_v2.md` (md5 `ad6db8a1…`; the plan §3 row 9's seven questions). Nick's `AMD-103-PATH: b` (D-v104-18) was relayed to it mid-review by message.
- **Its file, filed verbatim beside this audit:** `2026-10-10_v104-b3_AMD-103_independent-review.md` (89,696 B, md5 `2f3c43314435fd6c4d7a61f30360b063`).
- **Its verdict: READY-WITH-EDITS.**
  - Questions: Q1 IMPRECISE · Q2 WRONG · Q3 IMPRECISE · Q4 IMPRECISE · Q5 WRONG · Q6 IMPRECISE · Q7 WRONG.
  - Findings: 6 BLOCKING (F1–F6) and 6 NON-BLOCKING (F7–F12).
  - Edits: 24 (E1–E24), each with an OLD text that occurs once and no overlap between them.
  - Its §4 names five things it could not verify.
- **The texts handed:** v4 at 15:20 CT (34,642 B, md5 `b8509868…`) drew Nick's verdict (§5). **v6 is the text for `AMD-103: ratify`:** `_scratch/v104/b3/AMD-103_DRAFT_v6.md`, 37,951 B, md5 `664e25b281b8f335bc4dcc84cb8bd4b4`.

## §1 Layer 1 — what the review found (BLOCKING)
- **F1 · R-F:** the state projection's "no arm" was false. It ignores the two types only because they are DEVICE-subject. The fix binds the subject in R-A.
- **F2 · R-F:** path (a) was recommended against the draft's own evidence. Nick ruled (b), and the ruled shape holds at the bytes under five written conditions.
- **F3 · R-A/§5:** the category premise was false. Every persisted `availability_changed` is `DEVICE_HEALTH`, not Doc 01 §4.4's `device_state`.
- **F4 · R-B:** the link reading is J1's flat triple. A probe reply carries no reading.
- **F5 · R-D/§1/§2:** T1 widens in kind twice, and the governing Doc 01 text was unquoted.
- **F6 · R-E:** `@EventType` is 58 → 60, not 59 → 61. Three count pins were missed (one named by AMD-99 §7), and the list to edit is `CORE_PRODUCTION_EVENT_CLASSES`.

## §2 Layer 2 — the hub's reads (core `409547c`, docs `5e8eb8b`; `--no-optional-locks`)
| F | The bytes read | Holds |
|---|---|---|
| F1 | `StateProjection.java:971–:984`: the `else` arm builds `EntityState(… stateVersion() + 1 …)` for any entity-subject payload. `:1152–:1157` `subjectEntityIdOrNull`: null unless `SubjectType.ENTITY`. `ZigbeeIntegrationAdapter.java:2088–:2094`: `AVAILABILITY_CHANGED` under `SubjectRef.entity(entityId)` | YES |
| F2 | `v003_snapshots_design_note.md:21` "Pi 5 NVMe at roughly 50,000 events per second". No "120 s" replay ceiling in `design/` (the only "120 seconds" is Doc 05 `:246`, a streaming keepalive). The registry's whole-log walk: `HomeSynapseCore.java:622–:623`, `ReplayDriver.java:145`, IR-148 | YES |
| F3 | `EventCategoryMapping.java:103–:104` `AVAILABILITY_CHANGED → List.of(EventCategory.DEVICE_HEALTH)`; Doc 01 `:615` lists it under `device_state` | YES — a doc–code divergence, now recorded and closed by §2's row move |
| F4 | `StandardAvailabilityTracker.java:358–:362`: "A ping reply is consumed by its exchange and never reaches the ingestion seam — it is evidence without a link reading" | YES |
| F5 | Doc 01 `:41`, `:132`, `:140`, `:259`, `:261`, `:582`, `:86–:93`, `:885` | YES |
| F6 | `@EventType(` in `src/main`: 58 occurrences in 58 files. `EventTypeAnnotationTest:179` `isEqualTo(43L)`. `JacksonWarmupTest:43` `58`, `:112` `43`. `AllEventClasses.java:39–:40` `CORE_EVENTS = EventTypes.CORE_PRODUCTION_EVENT_CLASSES` | YES |
| R-F's new cites | `V001:29` `INTEGER PRIMARY KEY AUTOINCREMENT` · `HealthEndpoint.java:23` · `SqliteCheckpointStore.java:167` · `InProcessEventBus.java:651–:652` · `HomeSynapseCore.java:663` `SubscriptionFilter.all()` | YES |

## §3 The application (scripts in `_scratch/v104/b3/`; PROBE first, then the write)
1. **The review's edits.** `v104b3_apply_review_1.py` applied E1–E24 to v2: each OLD once, no overlap. The result, `AMD-103_DRAFT_v2r.md` (32,916 B, md5 `97815379d6bc0ae78ee5fb2a65ed74ce`), equals the reviewer's own in-memory check.
2. **The hub's edits.** `v104b3_hub_edits_1.py` made H1–H5 on v2r:
   - R-F's growth figure names its window;
   - R-F's type read is pinned to its index;
   - §4's cut also waits for REGISTRY-COLD-1's landing, and Oct 16 is the hard go/no-go (D-v104-20 R2);
   - three ordinals are reworded for the claim-word guard;
   - the header.

   The result is v3 (33,809 B, md5 `e56640281e7c94518317d4fb44d9b2a7`).
3. **The focused re-read.** The SAME reviewer re-read v3 by message (no new agent): **EDITS**. Its file is filed beside this audit: `2026-10-10_v104-b3_AMD-103_independent-review_v3-addendum.md` (5,313 B, md5 `293fbdefc8cba5ad7890eafec742abda`).
   - The diff was clean: exactly the hub's edits, and all of E1–E24 intact.
   - Six exact edits were owed:
     - H1's date and its attribution to D-v104-20 R4;
     - H2 restated as a requirement on the type read AND its `hasMore` probe, beside Nick's rows-read guard. The reviewer's note: on SQLite 3.37.2 — not the shipped 3.51.3 — both statements already plan on `idx_events_type`, so the pin is insurance;
     - its own E16, which had dropped A4 from the timed scan's uses;
     - R-F's comparison clause;
     - R-H's case for config.
   - Two filing actions were owed: banking D-v104-18/-20 (done: `883fdff`), and filing the review at AMD-103 `:9`'s path (this beat).
4. **The final text.** `v104b3_readd_edits_1.py` applied the six edits, then H6 (the addendum's filing named at `:9`) and the status line. The result is **v4**. The claim-word guard ("first", "superior") holds at zero.

## §4 What the review could not verify (its §4), carried
1. R-F's number under (b): the index-only `COUNT` of the three types on the Pi or on BACKUP-1's copy, read before AVAIL-API-1's cut.
2. The registry walk's warm duration (D2b's log is on the Pi).
3. The categories actually stored on the Pi (the `event_category` column).
4. REGISTRY-COLD-1's own design. The instruction was drafted tonight, and its own one-way-door review is asked of Nick (`REVIEW-RC1: launch`).
5. Whether an integration restart re-runs `initialize()` (F7's fresh-instance claim).

## §5 Nick's verdict on v4 and the two re-reads after it
- **15:32 CT, Nick:** "ratify in substance, with three blocking edits and three non-blocking ones". He accepted R-A `device_health` and R-H a code constant. His six edits:
  - NE1: §2's row names the last link reading, not the reply's.
  - NE2: R-B's bookkeeping is under the lock, and the publish is outside it.
  - NE3: R-C's class is derived from the tracker's three arms.
  - NE4: §3's null state, a second position in `meta`, and precedence.
  - NE5: R-F is durable and coupled by default.
  - NE6: R-G's N comes from the contract set.

  He also asked for two additions (R-F's number; HERO-U2c inherits NE4) and gave one sequencing note: the docs card files the ratified version's md5. His words are filed verbatim in the DR §3c.
- **v5** (`v104b3_nick_edits_1.py`; 37,309 B, md5 `3ec9a4059b96ec8ab7e7517e65d1648d`) carries the six edits.
  - One citation was corrected at the bytes: NE2's sink is `StandardAvailabilityTracker.java:575–:618`. The lock is taken at `:575` and released at `:612–:613`; the sink runs at `:618`. `:246` and `:254` are the two lookups' "applied OUTSIDE the lock".
  - R-F's number needs no separate card. SOAK-NIGHT-2's S0 already reads `avail-rows-total` (`SELECT COUNT(*) … WHERE event_type='availability_changed'`, read-only), and at the opening boot that IS the three types' count ≤ H.
- **The same reviewer's second re-read: EDITS, three exact** (`2026-10-10_v104-b3_AMD-103_independent-review_v5-addendum.md`, 3,737 B, md5 `1670e3891927f0f1076598bf38e8d75f`):
  - NE2's lock is the tracker's `ReentrantLock`, not the run thread's.
  - R-C also declares when the derived contract changes, and never from a cycle whose lookup threw (`:530–:536`). The tracker re-reads its lookups at every evaluation, so a contract declared only at boot can name an arm the tracker has left.
  - R-F: a failed catch-up does not fail the boot; the projection stays not LIVE and its keys null.

  They were applied by script (`v104b3_v5r_edits_1.py`). **v6** — 37,951 B, md5 `664e25b281b8f335bc4dcc84cb8bd4b4` — is THE TEXT FOR `AMD-103: ratify`. The claim-word guard holds at zero.

## §6 The verdict of this intake
**ACCEPT.** Every BLOCKING citation holds at the bytes. Every edit — the review's 24, the hub's, Nick's six and the two re-reads' — is applied by script with its md5 on file. v6 is in Nick's hands for `ratify`. The docs card files v6's md5, and its RATIFIED line quotes the word given on v6.

<!--
file: _scratch/2026-08-30_R3a_HUB-RETURN_what-changed_card.md
purpose: The R-3a return, written for the HUB and led by WHAT CHANGED IN ITS PICTURE OF THE WORLD — not by chronology. Self-contained: a fresh hub session can act on this file alone. Evidence pointers in §9 are optional to every ruling below.
audience: the hub (v58). Nick performed every act; the guide adjudicated each block against artifact-derived expectations.
status: R-3a COMPLETE. §0–§11 all run, every STOP-gate PASSED. Bench restored 15:06 ET with [PASS] boot-health 6/6 · 0 forbidden, nine hours inside the Mon 03:00 CT floor.
scorecard: 32 predictions EXACT · 1 half · 5 misses/refutations OWNED IN FULL.
-->

# R-3a — THE RETURN: what changed in the picture

## §1 THE HEADLINE — what R-3a proved

1. **OR-E3-PROBE IS CLOSED ON HARDWARE.** Same card, same probe binary, same 44-byte artifact absent, fourteen minutes apart: `7c9e4fa` took **90 s to fail** (`TIMEOUT`, `ExecMainStatus=143`, `Failed to start`, restart loop); `dec35be` (R-9) took **4 s to `active`** (`Result=success`, `NRestarts=0`, `ready (200) … /health`), then `200` on `/health` and `401` on the API. **The sole difference is `--health-path /health` on `ExecStartPost`** — the probe binary is comments-only different between the two commits, verified at source. A single-variable controlled experiment on real silicon. H8's bar is met.
2. **THE FIRST CI-BUILT `+git` ARTIFACT IS ON A CARD**, hash-identical across all three hops (`8156f4cb…`), `Version: 0.1.0+git20260823.231355.gdec35be` == image stamp, **zero event loss** (22 → 24), integrity `ok`, `home_id` unchanged, `--allow-downgrades` spent exactly once. H12 confirmed on a third independent surface.
3. **H13 SATISFIED — R-3b's spec is the §7 drop-in text, byte-for-byte, unmodified.** P-a fired on the first measurement; no second hypothesis was needed. **R-3b is unblocked and needs nothing further from R-3a.**
4. **THE DROP-IN COSTS NOTHING MEASURABLE.** `projection_live → network_resumed` took **8.219 s** packaged-and-sandboxed vs **8.235 s** native on the bench the same morning. Sixteen milliseconds.
5. **THE BENCH IS UNHARMED.** All six devices relinked with their ORIGINAL bench identities; `position=25065` unchanged. See §2.1's safety half.

---

## §2 WHAT CHANGED IN THE HUB'S PICTURE — three things

### 2.1 A CUSTODY CLONE CARRIES THE NETWORK, NOT THE ADOPTIONS, AND NOT WORKING AUTOMATIONS
**This is the day's most consequential result and it re-prices R-4.**

The rig resumed the bench's Zigbee network in ~8 s (`network_resumed: channel=20 panId=0x774c`) while its HomeSynapse registry stayed **completely empty** (`Available 0 of 0`). Rehydration keys off the **registry** — a projection of the **event store** — which was correctly not cloned and must never be (the rig carries its own `home_id`).

**Proven by three forecasts, each filed before its observation:**

| registry adoptions | cache loaded | rehydrated | relinks |
|---|---|---|---|
| **0** (post-clone) | 6 | **0** | **0** |
| **1** (after one re-adoption) | 1 | **1** | **1** |
| **2** (after the second) | — | **2** | **2** |

**And it extends one layer up.** `bench-hero` travelled in the cloned `homesynapse.yaml` and binds by entity ULID:
```yaml
triggers: [{type: state_change, entity_ref: 01KX1PB9AAB4VB3E10BD477TV3, attribute: occupied, to: "true"}]
actions:  [{type: command, target: {entity_ref: 01KX1PA4HSJ581GASYB7DHE40F}, …} × 5]
```
Both refs appear in the **bench's** live `/api/v1/entities` roster and were absent from the rig's. **Automations survive a clone as text, not as rules — every entity reference dangles.**

**The safety half, and it is the reassuring one:** the two devices re-adopted on the rig (new ULIDs `01M19XN7…`, `01M19RHW…`) relinked on the bench with their **original** IDs. A full day of card-swapping, cloning, two re-adoptions, a permit-join window and an uncontrolled power loss on the rig **left the production bench's application state untouched.** The one-direction fence now has evidence behind it, not just doctrine.

### 2.2 THE PACKAGED ARTIFACT SURVIVES AN UNCONTROLLED POWER LOSS, COLD AND UNATTENDED
Mains power failed mid-run. The Pi rebooted unattended with the coordinator live and the service auto-started. **`network_resumed` — no `network_formed`.** Custody intact, `integrity_check ok`, rows grew, artifact and drop-in both survived, coordinator re-enumerated with an identical by-id string. The packet never scripted this; **recommend R-4 adopt an uncontrolled-power-loss leg deliberately** — it is free (pull the plug) and exercises WAL recovery, custody survival and the resume-vs-form branch at once. It produced more evidence in four minutes than the scripted probe produced in thirty.

### 2.3 A RECURRING SHAPE: HEALTHY OUTCOMES REPORTED THROUGH FAILURE CHANNELS
Four instances in one day, all new:

| finding | the healthy event | the failure channel |
|---|---|---|
| **§6-B** | a graceful operator-requested shutdown | app exits **143**, systemd marks the unit **`failed`** |
| **§10-O** | an orderly stop closing the serial port | **`transport_failed`** carrying F-S16's "physical port loss" signature |
| **§10-M** | (probably) a transient key self-expiring as designed | **`key_establishment_failed`** for device `0xFFFFFFFFFFFFFFFF` |
| **§10-I** | a device with no recorded report time | the list renders **`Current`** — a freshness claim with no evidence |

Same family as the M9.4 §B `key_establishment_failed` misclassification the project already fixed as KEYb (**confirmed landed today** — §10-L). **Never-false-ALIVE currently guards against claiming health that is not there, but not against claiming failure that is not there.** The second error costs operator trust just as fast. **Recommend the hub treat this as a class and consider a sweep.**

---

## §3 THE FINDINGS LEDGER

| id | severity | finding |
|---|---|---|
| **§9-B / §10-F / §10-N** | **HIGH** | Custody clones carry the network, not adoptions, not working automations. Three confirmed forecasts + direct proof from both entity rosters. **Re-prices R-4.** |
| **§10-P** | **HIGH** | **journald priority is blind to every application warning.** 158–201 app WARN/ERROR lines; `journalctl -p warning` reports **2**, both systemd's own. Any monitor filtering by PRIORITY sees a healthy service while warnings accumulate. |
| **§10-J** | **HIGH (FE)** | The explain surface **concealed a fault it could see**. It said *"it fires on state change"* when the rule says *entity `01KX1PB9AAB4VB3E10BD477TV3`, occupied → true*. One honest sentence would have surfaced the dangling ref; instead it took an hour of journal archaeology. |
| **§6-B** | **MED-HIGH** | The service lies about its own exit. `ExecMainCode=1` (CLD_EXITED) + `ExecMainStatus=143` + no `SuccessExitStatus` ⇒ every clean stop leaves the unit `failed`. **Root-correct fix: exit 0 on graceful SIGTERM shutdown** (a unit-side `SuccessExitStatus=143` would mask a genuine kill). |
| **§10-Q** | **MED-HIGH** | **165 × `zigbee.ingestion_unknown_sender`** — the un-re-adopted fleet was transmitting throughout §10. **This refutes the guide's own finding §10-B** (see §8). The packet's §9/§10 greps omit the single most informative token on a cloned rig. |
| **§4-C** | **MED** | The installer's banner AND `homesynapse-token` both instruct *"then delete the token file"* — which under `7c9e4fa` is exactly the §3 failure. R-9 is what makes both honest. |
| **§4-B** | **MED** | The packet's §4 I-3 groups baseline and install un-chained, so **a failed `integrity_check` would not have stopped the install**. |
| **§10-O** | **MED** | F-S16's "physical port loss" signature (`retransmits=0 crcRejects=0 timeouts=0`) also fires on a clean service stop. **The packet would send an operator hunting a hardware fault that is a normal shutdown.** |
| **§10-G/H/I** | **MED (FE)** | `Available` with an empty `Last reported` (criterion 2 only PARTIAL) · the Devices page shows the **entity** ULID under a `DEVICE` column, so a row cannot be correlated to a `device_adopted` log line · the list says `Current` where the detail says the report time is not recorded. **§10-G's defect is in the READ path — the store holds both `availability_changed` and `state_reported`.** |
| **§3-A** | **MED** | `ExecMainStatus=143` re-states the E3 risk precisely: systemd **tears down a healthy process**; the app does not crash. Recommend the OR row adopt this wording. |
| **§10-L** | — | **M9.4-KEYb appears to have LANDED** — a clean `key_established`, zero spurious failures. Free regression confirmation; **verify at source and close the row if still open.** |
| **§2-A / §4-A / §8-A / §10-D / §11-A** | — | The rig sat in the P-d state pre-clone (the fence was load-bearing, not ceremonial) · the probe's 503 arm fired, full state model silicon-exercised · the dongle enumerated `Device 004` vs `011`, vindicating the class-rule choice over the source RAMP comment's node path **within the hour** · power-loss survival · the bench unharmed. |

---

## §4 R-4, RE-PRICED — the hub's decision

R-4's four lift criteria, as measured today on a cloned-custody rig:

| # | criterion | today | why |
|---|---|---|---|
| 1 | `network_resumed` | **MET** (twice) | resumes in ~8 s |
| 2 | ≥1 device Available **with a fresh `Last reported`** | **PARTIAL** | Available yes; `Last reported` empty (§10-G — a read-path gap, the data exists) |
| 3 | rows grew + discriminator 0 | **MET** | 27 → 53, discriminator 0 |
| 4 | one automation run with a rendered explanation | **STRUCTURALLY UNREACHABLE** | dangling `entity_ref`s (§10-N) |

**Ruling needed on criterion (4). Three options:**
- **(a) clone the event store too** — reject on its face: it carries the bench's `home_id` and destroys the rig's identity.
- **(b) rewrite `entity_ref`s after re-adoption**, as an explicit rehearsal step. **The only option that preserves the criterion's meaning.**
- **(c) drop (4) for cloned-rig runs** and prove the automation path on the bench instead.

**Criterion (2) also needs a word:** either fix the read path first, or restate the criterion as "Available" without the freshness clause.

**And R-4 must plan for re-adoption, not resumption.** The rig resumes the *network* in seconds; the *fleet* re-adopts device-by-device on each device's own schedule. Two useful mechanisms measured today: a `SECURED_REJOIN` needs **no permit-join window** (a battery device did it unprompted when its parent returned), and a full announce→adopt→`reporting_configured`→`ias_zone_enrolled` chain runs in **10 seconds** with `proposal_accepted: source=config` off the cloned `adopt_devices` list.

---

## §5 OPEN-RISK ROWS TO ACT ON

- **OR-E3-PROBE — CLOSE IT.** Its stated third leg ("the packaged unit restarts with the artifact absent") landed today. Adopt §3-A's wording (systemd tears down a *healthy* process) and §4-C (the installer instructed operators into the failure) into the closure note.
- **M9.4-KEYb — verify and close** if still open (§10-L).
- **NEW ROW recommended: the failure-channel class** (§2.3) — four instances, one shape.
- **NEW ROW recommended: journald priority blindness** (§10-P) — it undercuts the observability claim directly.
- **OR-TOKEN-MODE-644 — corroborated**: the held card's 644 pair (Aug-13 mint) against the bench's 600 pair (rotate path), both observed again today. No change; residue still PKG-SEC-1.

---

## §6 PACKET AMENDMENTS — ★ = adopt permanently

★ §2: check the **installed** unit's `ExecStartPost` before E3-RED (F-A4 — without it a green is unfalsifiable) · ★ §4 I-3: **split** baseline from install so `integrity_check` can gate · ★ §6: **guard** the lay-down on the service actually being stopped · ★ §1: **parse-check both JSONs inside the custody tarball** (the hazard was real — the cache mtime moved mid-capture) · ★ §1: capture the F-S20 by-id string from the **live bench** pre-swap · ★ §0: read the overnight nightly digest before taking the bench down · ★ §4 I-1: pull the artifact confirm forward while the bench is up · ★ §7: verify with `systemctl show` (effective config), not `cat` (file text) · ★ **`--no-pager` on every `systemctl`**, not only `journalctl` · ★ §9: `reset-failed` before `start` (needed because of §6-B) · ★ §9/§10: add **`ingestion_unknown_sender`**, `permit_join_opened`, `ncp_configured` to the greps · ★ §9: note `adopt_list_loaded` is **DEBUG** — absence is not failure · ★ §10: **rewrite the "5 Available + 1 Unavailable" expectation** — unreachable on a cloned rig · ★ §10: correct **F-S16's** guidance (§10-O) · ★ §10: the `curl … Bearer $(sudo homesynapse-token)` line is **broken** — the helper prints a labelled block, not a bare token · ★ §10: "exactly one `network_resumed`" should be "one per service start, zero `network_formed`" · §6: the aside dir was dated **2026-08-30**, the date of the act.

**F-A5 (R-3b rider):** the unit's in-source RAMP comment recommends `DeviceAllow=/dev/ttyUSB0 rw` — a node path. R-3b ships the **class** form, and finding §8-A measured the justification live (the device number changed across the replug). **R-3b must update that comment** or source carries a recommendation contradicting the shipped unit. Also note `DeviceAllow=char-rtc r` appears in the effective config from systemd's own clock protection — not ours.

---

## §7 WHAT THE HUB SHOULD DO NEXT

1. **Author R-3b now.** Its spec is the §7 text verbatim; nothing is pending.
2. **Rule criterion (4)** — (b) recommended. And rule criterion (2)'s wording.
3. **Close OR-E3-PROBE**; verify and close M9.4-KEYb; open the two new rows from §5.
4. **Fold the ★ amendments** into the packet as one pass.
5. **Commission three source reads** for the items in §8 — none should be characterised without them.
6. **Re-price the weekend:** R-4 slid to Monday against the audits, THE SEPTEMBER PLAN OF RECORD and the Pelton word.

---

## §8 NOT ESTABLISHED — do not treat these as characterised

- **§10-E** the trigger that destroys the cloned device cache (inferred from a 0600→0644 mode change and the load counts; the precise write path is unread).
- **§10-M** the cause of `key_establishment_failed` for `0xFFFFFFFFFFFFFFFF` (transient-key expiry is plausible; the timing does not line up exactly).
- **§10-Q** the composition of the `Configuration issue [WARNING] at 'integrations.zigbee'` ×3 against the cloned yaml — content not captured.
- **The guide's own refuted claims**, recorded rather than quietly dropped: the Δ+4 row model (observed Δ+2 on an upgrade restart); the §9 fleet-arm inference (the actual mechanism was neither P-g nor P-e as reasoned); the M9.4-KEYb false-failure prediction (refuted, in the good direction); `transport_failed = 0` (observed 2); and **finding §10-B, refuted by §10-Q** — the guide concluded "nothing transmitted" when 165 `ingestion_unknown_sender` warnings show the fleet was transmitting all along, invisible to both its greps and journald's priority filter.

---

## §9 POINTERS (optional to every ruling above)

- **Full operator record** — 1,665 lines, incl. **Appendix A, the complete verbatim transcript** (every command, every byte, with the stated rule that the transcript wins over the adjudication), Appendix B source verification, Appendix C the amendment ledger, and the closing state: `_scratch/2026-08-30_R3a_rehearsal_operator-record.md`
- **Saturday's deferral ruling + pre-run desk audit** (produced amendments F-A1…F-A5): `_scratch/2026-08-29_R3a_DEFERRED_desk-audit_operator-return.md`
- **The morning's escalation card** (the `RIG` ruling): `_scratch/2026-08-30_R3a_ESCALATION_fleet-repair-ruling_card.md`
- **The packet of record, unmodified:** `context/handoff/2026-08-26_R3a_rehearsal_operator-packet.md`
- **Bench evidence bundle:** `/home/homesynapse/hs-bench/bundles/boot-health-20260830T190604Z`

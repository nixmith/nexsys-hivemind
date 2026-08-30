<!--
file: _scratch/2026-08-29_R3a_DEFERRED_desk-audit_operator-return.md
purpose: R-3a did NOT run Sat 2026-08-29. This is (a) the deferral ruling + the clock arithmetic behind it, (b) the re-priced Sunday card, and (c) a READ-ONLY desk audit of the packet's derived expectations against the artifacts at dec35be / 7c9e4fa (H12: expectations derive from the ARTIFACT, never the intent). Five packet amendments recommended; ten expectations confirmed exact.
audience: the hub (v58) · Nick (operator)
status: OPERATOR RETURN — unfiled. Nothing committed; nothing staged; no hardware act occurred.
fences honoured: no hardware touched · no card swapped · the coordinator never unplugged · core checkout NOT touched (all reads are `git show`/`git grep` at a sha; porcelain verified EMPTY at 5051fa5 before and unchanged) · nothing written inside either repo (this file is in the sibling _scratch/) · no token value anywhere.
-->

# R-3a — DEFERRED to Sunday daylight + the pre-run desk audit

## §0 THE RULING (supersedes the snapshot's IN-FLIGHT line)

`context/status/PROJECT_SNAPSHOT.md` (v58 beat 4) reads **"IN FLIGHT: R-3a session LAUNCHED ~20:00 CT (⏺s → the hub; measured text → R-3b stamped same-beat)."** That line is now **STALE**. The session launched and immediately ran its own pre-flight; the operator ruled **DEFER WHOLE TO SUNDAY** at ~21:10 CT. **No block of the packet was executed. Zero ⏺s exist. R-3b has no measured text to be stamped from at this beat.**

## §1 The arithmetic that produced the ruling

- Pi clocks at the ruling: **22:05 ET / 21:05 CT, Sat 2026-08-29**.
- Packet header pins: DAYLIGHT, 4–6 h, **bench floor back `[PASS]` before 03:00 CT = 04:00 ET** (the 04:30 ET nightly oneshot must find the bench up).
- Window remaining at the ruling: **~5 h 50 m**. Summed per-block bounds: **~3 h 10 m** nominal → landing ~00:15 CT, ~2 h 45 m slack.
- So the clock was *workable*. It was **not** the binding reason. The binding reasons the operator weighed: the §9 **P-d** branch (`zigbee.network_formed` → POWER OFF AT ONCE) is a reflex requirement, not a considered one, and it lands past midnight after a full authoring day; and §10's evidence window requires a physical motion-sensor walk.
- **Cascade the hub must re-price:** Sunday's R-4 (the guarded LIFT + the claim register) now slides to **Monday**, colliding with the audits + THE SEPTEMBER PLAN OF RECORD + the Pelton word. The v57-beat-9 §5 weekend shape no longer holds as written.

## §2 The re-priced Sunday card

Unchanged packet, one addition: a **named abort seam**. Recommended dispatch shape —

> Start §1 at first daylight. Run §1 → §11 in packet order. **Pre-ruling: if STOP-GATE §9 is not cleared by [start + 4 h], STOP, run §11, and carry §9–§10 to the next window.** §11 is never the block that gets compressed — the bench floor is the day's exit criterion, not a courtesy.

Block bounds as written: §1 10m · §2 15m · §3 ≤3m+restore · §4 20m · §5 ≤2m · §6 15m · §7 2m · §8 2m · §9 5–30m · §10 ≥30m · §11 20m.

Pre-flight facts confirmed tonight, so Sunday does not re-derive them: `C:\Users\Nick\r3-artifact` **exists** (Block I's source is where §4 I-1 says it is). `~/r3-rehearsal` does **not** exist — correct, §1 creates it. No `2026-08-29_R3a_..._operator-record.md` exists in `context/audits/`. Core checkout porcelain **EMPTY** at `5051fa5`.

## §3 THE DESK AUDIT (read-only, at the artifacts)

Method: `git show <sha>:<path>` and `git grep <sha>` only — no checkout, no working-tree touch, core fence intact.

### §3.1 CONFIRMED EXACT — ten expectations that derive correctly from the artifact

1. **`homesynapse.service:53` @ `dec35be`** is byte-for-byte the packet's prediction:
   `ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health`
2. **`health-probe.sh` message strings** (both commits): `log "token not yet available at ${TOKEN_FILE}"` · `log "ready (200) at ${URL}"` · `log "TIMEOUT after ${TIMEOUT}s — service did not become ready"` → renders `TIMEOUT after 90s — …` exactly as §3 predicts.
3. **`TOKEN_FILE` default = `/var/lib/homesynapse/config/initial_api_token`** at BOTH `7c9e4fa` and `dec35be` — §3's expected RED path string is exact.
4. **The probe is COMMENTS-ONLY different between `7c9e4fa` and `dec35be`** (zero code-line deltas). Consequence, and it strengthens the experiment: **the entire E3 RED↔GREEN delta is the unit's `ExecStartPost` line** — `--wait --timeout 90` (authed default `/api/v1/entities`, reads the token) vs `+ --health-path /health` (unauthenticated, no token read). One variable, cleanly isolated.
5. **§6's mechanism claim is verbatim at source.** `ZigbeeIntegrationAdapter.resumeOrForm()`: `if (parameterStore.load().isPresent()) { protocol.resumeStored(); log.info("zigbee.network_resumed: …") } else { formNetwork(); log.info("zigbee.network_formed: …") }`. Javadoc: *"a mismatch or missing key custody propagates PERMANENT — never adopt a wrong network, never silently re-form over corrupt custody."* **The §6 gate is correctly placed and correctly justified.**
6. **PAN rendering:** `panId=0x{}` via `Integer.toHexString(...)` → lowercase, unpadded → `panId=0x774c`. Matches §9/§11.
7. **`zigbee.port_identity_captured: stableId={} vendorId={} productId={} pinnedOnly={}`** with `toHexString` on vendor/product → `vendorId=10c4 productId=ea60` lowercase. Matches §9's P-a string exactly.
8. **All 17 §9 discriminator tokens exist** in the sources at `dec35be`. The grep is not blind.
9. **`registry.projection_live`** is INFO, in `lifecycle/RegistryProjectionSubscriber.onCaughtUp()`, format `registry.projection_live: devices={} entities={} position={}` — the boot glance-point.
10. **H12's version scheme** confirmed at `distribution/common.sh:57 hs_version()` — bare id wrapped as `0.1.0+git<YYYYMMDD.HHMMSS>.g<id>`, committer date in UTC, with the ordering rationale in-comment. (Already banked empirically by the amd64 leg.)

### §3.2 FINDINGS — five packet amendments recommended

**F-A2 — HIGH. `permit_join_duration` travels in the clone, and the join window opens on BOTH arms.**
`openPermitJoinWindow()` is called unconditionally after `resumeOrForm()` → `awaitNetworkUp()` (adapter start sequence), and reads `permit_join_duration` from config. Its own Javadoc: *"A restart naturally re-opens the window while the key is present — the designed bench semantic (the operator removes the key to stop re-opening on boot)."*
§6 clones the bench's `integrations/zigbee.yaml` **verbatim** onto the held card. If that file carries the key — likely, it is the bench's operator pairing path — then on §9 the held card **opens a Trust-Center preconfigured-key join window on the live fleet's production network** (`protocol.enablePreconfiguredKeyJoins(); protocol.permitJoin(duration);`) and logs `zigbee.permit_join_opened: duration=Ns`.
**This also re-prices the P-d worst case the packet quotes.** `formNetwork()` honours `channel` from the same cloned yaml: a pinned, in-range value **forms directly on that channel and the energy scan never runs**. So a P-d accident does not land on a random channel — it lands on **channel 20, the bench's own channel, with a join window opening seconds later.** That is precisely the configuration in which the six orphaned devices could be *recruited* by the rogue coordinator, not merely orphaned. The packet's "new PAN, new key, six devices orphaned, hours of re-pairing" understates it.
**Fix (three one-line changes):** (a) add `permit_join` to §1's yaml-glance grep and to §6's gate grep; (b) if the key is present, comment it out in the held card's cloned `zigbee.yaml` before §8's plug — key-removal is the documented control; (c) add `zigbee.permit_join_opened` to §9's discriminator grep so it is observed either way.

**F-A1 — MEDIUM. `zigbee.adopt_list_loaded` is DEBUG — the only DEBUG token in §9's grep.**
`log.debug("zigbee.adopt_list_loaded: entries={}", accepted.size())`. At production INFO level it **will not appear in the journal**. §9's P-e arm cites it as evidence of the cloned adopt list. An operator who greps and finds nothing could read it as "the adopt list failed to load" — a false negative on a load-bearing arm.
**Fix:** one parenthetical in §9 — *`adopt_list_loaded` is DEBUG; expect ABSENT at INFO. Its absence is NOT evidence the list failed. The INFO-level proof is `proposal_accepted` → `device_adopted`.*

**F-A4 — MEDIUM. §2 never checks the installed unit before §3, so E3-RED is not yet falsifiable-for-the-right-reason.**
Because the probe binary is identical at both commits (§3.1 item 4), E3-RED's entire RED prediction rests on the **installed** unit lacking `--health-path`. §2's rig glance checks `dpkg` version and `/opt/homesynapse/VERSION` but never the unit's `ExecStartPost`.
**Fix:** add to §2 — `systemctl cat homesynapse.service | grep -E '^ExecStartPost'` → expect `--wait --timeout 90` with **NO** `--health-path`. Then a `ready (200)` in §3 is a true refutation rather than an unnoticed already-upgraded card.

**F-A3 — LOW/MEDIUM. §9's P-b/P-c arm ordering is inverted for this rig, and two tokens are exception codes, not log lines.**
`zigbee.transport_unbound` and `zigbee.transport_unsupported` are **`PermanentIntegrationException` codes**, not `log.*` calls — they surface as exception text, not as an `INFO zigbee.…:` line. Recognise the shape.
More usefully: the `transport_unbound` site fires when `integrations.zigbee.serial_port` **is unset** and no `10c4:ea60` bridge enumerates. The cloned yaml **pins** `serial_port: /dev/zigbee`, so `resolvePort()` takes the pinned path and the enumerator never runs. **A permissions failure on this rig therefore surfaces as P-c (EPERM / Permission denied at `portChannelOpener.open(port)`), not P-b.** §9 should expect P-c first; a P-b on a pinned-port rig means the symlink itself is absent.

**F-A5 — LOW (an R-3b rider, not a Sunday change). Comment/code unity.**
The unit's in-source RAMP block at `dec35be` recommends the node-path form:
`#   PrivateDevices=no` / `#   DeviceAllow=/dev/ttyUSB0 rw` / `#   SupplementaryGroups=dialout`
§7's drop-in deliberately uses **class names** (`char-ttyUSB` / `char-ttyACM`, majors 188/166) plus `DevicePolicy=closed`, and justifies it: class rules survive replug renumbering where a node path would not. R-3b ships whatever §9 measures — so **R-3b must also update that RAMP comment**, or source carries a recommendation contradicting the shipped unit. (`SystemCallFilter=@system-service` + `SystemCallErrorNumber=EPERM` are already present at both commits — that is the ground for §9's P-c EPERM diagnosis.)

## §4 What the hub should do with this

1. **Correct the snapshot's IN-FLIGHT line** — R-3a is DEFERRED, not running; zero ⏺s.
2. **Re-price the weekend:** R-4 → Monday, against the audits + the September plan of record + the Pelton word. Rule whether R-4 holds Monday or slides.
3. **Rule on F-A2** before Sunday's §8 — it is the only finding that changes what the operator physically does, and it touches the fleet.
4. **Fold F-A1 / F-A3 / F-A4** into the packet as one amendment pass (four one-line edits, no structural change).
5. **Carry F-A5** onto R-3b's rider list.
6. R-3b remains blocked on §9's measured drop-in text. Nothing about R-3b can be stamped this beat.

## §5 What did NOT happen (the negative record)

No hardware act. No card swap. The coordinator was never unplugged. No SSH session to either Pi. The bench is untouched and its 04:30 ET nightly will run normally. No file written inside `homesynapse-core` or `nexsys-hivemind`; core porcelain verified EMPTY at `5051fa5` before the audit and unchanged after (every read was `git show` / `git grep` at a sha). No token value read, pasted, or recorded.

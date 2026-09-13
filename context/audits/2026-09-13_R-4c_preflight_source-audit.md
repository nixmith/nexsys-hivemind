<!--
file: context/audits/2026-09-13_R-4c_preflight_source-audit.md
purpose: THE R-4c COMPANION AUDIT — the half of the R-4c return that is analysis rather than paste-back. Three parts: (1) THE PRE-FLIGHT SOURCE AUDIT — every journal token the rig blocks grep for, read against commit a458a64's OWN emit site and LOG LEVEL (not mere presence), plus the C-003 reachability read, the census-format proof, the schema read and the dpkg version-ordering check, all run at the DESKTOP before B0 at zero rig cost; (2) THE DEVIATIONS LEDGER IN LONG FORM — the full reasoning behind every D-n the operator record's §9 lists compactly; (3) B0's LONG-FORM READINGS. Method and rationale: R-4b's findings card §5(b)/(c) — never assert absence or uniqueness with head/tail, and verify every route and verb at the source table.
audience: the hub (intake this TOGETHER with the operator record — neither file is the whole return) · the navigator (reads the counter key at B1/B3) · Nick (the live discriminator in F-3)
state-type: companion audit (desktop; read-only; no rig act)

  ⚠ THIS FILE IS ONE HALF OF A TWO-FILE RETURN. Its partner, which carries every operator paste-back and the
  per-block verdicts, is:
      context/audits/2026-09-12_R-4c_measurement-only_operator-record.md
  The split was made mid-session to keep that record inside the packet's `≤ ~30 KB` close-out cap. Nothing was
  summarised away in the move; sections 2 and 3 below are the original text verbatim. INTAKE BOTH.

  ⚠ DATE. The partner record's FILENAME says 2026-09-12 (the slot the packet was authored for). The session
  actually ran SUNDAY 2026-09-13. Every Z stamp in both files is genuinely 2026-09-13.

  ⚠ WHY THE PRE-FLIGHT EXISTS AT ALL, AND WHAT IT IS NOT. It is NOT a substitute for measurement — nothing here
  is evidence about the RIG. It establishes only what the ARTIFACT'S SOURCE says, so that a count of zero read
  on the rig can be attributed correctly: to the device, not to a token that was misspelled, renamed, or logged
  below the configured level. Nine defects were found this way before the card was touched (F-1…F-9). Read F-1
  before grading B1's token counts and F-2/F-3 before grading B3's countdown, or those blocks WILL be misread.

status: COMPLETE. The session it serves CLOSED 2026-09-13 at 15:03Z with ALL FIVE STOP-GATES MET and ZERO STOPS (C-003 earned; O-2 closed). Of the thirteen pre-flight findings, F-1 and F-9 were predicted here and then landed on the wire exactly as written; F-12 predicted a 13-17 s countdown offset and the measured value was 19.272 s. Artifact under audit:
  homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb · sha256 1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1
  · install-smoke run #53 · commit a458a64. Method: `git grep` against a458a64 in the local clone — the same
  commit the .deb is built from — reading emit sites and levels, plus `dpkg --compare-versions` for F-5.
  Packet: context/instructions/2026-09-11_R-4c_measurement-only_zdo-surface-C-003_navigator-packet.md
-->

# R-4c pre-flight source audit — the tokens, their levels, and what B3's counters actually count

**⏺ filed 2026-09-13T13:50:13Z**

### ★ PRE-FLIGHT SOURCE AUDIT (navigator, desktop, before B0) — every token the rig blocks grep for, read against `a458a64`'s own source

Run at the desktop while the artifact was re-fetched, at zero rig cost. Method: `git grep` against commit `a458a64` in the local clone (the same commit the .deb is built from), reading the **emit site and its log level**, not the token's presence. Rationale: R-4b's findings card §5(b)/(c) — *"never assert absence or uniqueness with head/tail"* and *"verify every route and verb at the source table"*. A token that is misspelled, or emitted below the configured level, **counts 0 and reads as a clean negative.**

**THE LOGGING LEVEL OF RECORD.** `app/homesynapse-app/src/main/resources/logback.xml` @ `a458a64`: `<root level="INFO">`, one CONSOLE appender, **no per-logger overrides** (the comment pins it as a security default — Jetty/HTTP DEBUG echoes bearer credentials, FE-1b 2026-07-03). **Anything logged below INFO is invisible to journald on the card.**

| token (packet block) | emit site | level | visible? | verdict |
|---|---|---|---|---|
| `Configuration issue` (B1) | `StandardConfigurationService.java:820` | WARN | ✓ | EXPECTED 0 is readable |
| `lifecycle.integration_schema_registered` (B1) | `HomeSynapseCore.java:1366` | INFO | ✓ | ok |
| `zigbee.network_resumed` (B0·B1·B4·B5) | `ZigbeeIntegrationAdapter.java:727` | INFO | ✓ | ok |
| `zigbee.network_formed` (the hard fence) | `NetworkFormation.java:248` | INFO | ✓ | **the POWER-OFF fence is readable** |
| **`zigbee.adopt_list_loaded` (B1)** | `ZigbeeIntegrationAdapter.java:1152` | **DEBUG** | **✗ SUPPRESSED** | **B1's EXPECTED is wrong — see F-1** |
| `zigbee.adoption_maps_rehydrated` (B1) | `ZigbeeIntegrationAdapter.java:1114` | INFO | ✓ | ok; carries `devices={}` |
| `zigbee.availability_seeded` (B1) | `ZigbeeIntegrationAdapter.java:377` | INFO | ✓ | ok |
| `bus.delivery_anomaly` (B1·B4) | `HomeSynapseCore.java:558` | WARN | ✓ | ok — B4's `sed 's/^.*WARN *//'` is correct |
| `zigbee.permit_join_opened` (B1·B3·B4) | `ZigbeeIntegrationAdapter.java:808` | INFO | ✓ | ok; text is `duration={}s` |
| `zigbee.rejoin_ignored_window_closed` (B3) | `ZigbeeIntegrationAdapter.java:1225` | INFO | ✓ | ok (note: the *other* ignore path, `zigbee.rejoin_candidate_ignored` in the EUI64-carrying hook, is DEBUG and invisible — the packet does not count it, correctly) |
| `zigbee.lookup_eui64_failed` (B3) | `EzspCoordinatorProtocol.java:1642` | WARN | ✓ | ok — **but see F-2: it is the ONLY `lookup_eui64` line that exists** |
| `zigbee.ieee_addr_req` (B3) | `EzspCoordinatorProtocol.java:1707` | INFO | ✓ | ok — **see F-3** |
| `zigbee.ieee_addr_rsp` (B3, THE EXIT) | `EzspCoordinatorProtocol.java:1731/1735` | INFO | ✓ | ok — **see F-3** |
| `zigbee.ieee_addr_req_unanswered` (B3) | `EzspCoordinatorProtocol.java:1713` | WARN | ✓ | ok |
| `zigbee.ieee_addr_rsp_failed` | `EzspCoordinatorProtocol.java:1725` | WARN | ✓ | **a fourth outcome the packet never names — see F-3** |
| `device_adopted` / census (B3) | `ZigbeeAdoptionSlice.java:455` | INFO | ✓ | text is `zigbee.device_adopted: device={} deviceId={} entities={}` — the packet's `grep -c "device_adopted: device=$d"` matches as a substring ✓ |

**★ C-003 IS REACHABLE ON THESE BYTES — the mechanism is wired, not merely present.** `ZigbeeIntegrationAdapter.onRejoinCandidate(int networkAddress, int clusterId)` implements the packet's chain exactly: store lookup (`cache.deviceForNetworkAddress`) → miss → the once-per-nwk-per-epoch set (`rejoinLookupAttempted.add`) → `protocol.lookupIeee` (EZSP `0x0061`) → **on empty, `protocol.requestIeeeAddress(networkAddress, IEEE_ADDR_REQ_TIMEOUT_MILLIS)` — the ZDO `IEEE_addr_req` on the air** → `answer.isEmpty()` ⇒ `rejoin_candidate_unresolved … reason=zdo_miss` → else `resolved = answer.ieeeAddress()`, `admittedAddress = answer.networkAddress()` (**the RESPONSE's pair**, DP-6/DP-8) → `admitRejoinCandidate(resolved, admittedAddress, "unknown_sender")`. The source's own comment cites R-4b's measured miss (`lookup_eui64_failed nwk=0x15ac status=0x1`) as the reason the arm exists. **B3's exit is not speculative on this artifact.**

**★ THE CENSUS GREPS WILL MATCH.** `IEEEAddress.toString()` = `"0x" + String.format("%016X", value)` — **uppercase, zero-padded to 16, `0x`-prefixed**. The packet's six census IEEEs are written in exactly that form, so `grep -c "device_adopted: device=0xF044D3FFFED2A201"` matches the emitted line. (Had the formatter been `%016x`, all six census lines would have read `0` and the session would have produced a false total miss.)

**★ THE SIX CENSUS IEEEs ARE CORROBORATED.** All six appear in the R-4b operator record (`0x00178801101A09BB` ×6 · `0xF044D3FFFE9C78D7` ×6 · `0x00124B002FA8D1C5` ×13 · `0xF044D3FFFED2A201` ×6 · `0xF044D3FFFE1C1E8E` ×4 · `0x449FDAFFFE688F57` ×4). The packet's list is not invented. *(The card's `zigbee.yaml` remains the truth at B3 per the packet's own T1 clause.)*

**★ B2's PYTHON IS CORRECT ON THIS CONTRACT.** `ListEntitiesEndpoint` serialises `{"data":[…],"meta":{…}}` (`body.put("data", summaries)`, line 181) — so `d['data'] if isinstance(d,dict) and 'data' in d else d` selects the rows. `lastReported` is `summary.put("lastReported", state.lastReported()==null ? null : state.lastReported().toString())` (lines 203–204) — **JSON `null` when the projection holds none, `Instant.toString()` (ISO-8601 UTC) otherwise. LASTREPORTED-1b's assertion is exactly what the code does.**




**⏺ filed 2026-09-13T13:52:22Z**

### ★ PRE-FLIGHT FINDINGS F-1 … F-4 — three of B3's live counters do not count what they are labelled

Read at source before B0, at zero rig cost. **None of these is a stop, and none changes what the session measures** — STOP-GATE R4c-3 is keyed on the HARVEST block's verbatim chain, which is correct as written. They matter because the operator spends **240 seconds** reading the countdown, and three of its six columns are misleading.

**F-1 · `adopt_list_loaded` is DEBUG — B1's EXPECTED is wrong on these bytes.** `log.debug("zigbee.adopt_list_loaded: entries={}")` (`ZigbeeIntegrationAdapter.java:1152`) against `<root level="INFO">` (`app/homesynapse-app/src/main/resources/logback.xml`, no per-logger overrides). **B1's `adopt_list_loaded` count will read `0`, and 0 is CORRECT.** The packet's EXPECTED says `1`. Consequence if unwarned: a MISMATCH is declared on a healthy boot, and the navigator spends T2 probes on a non-event. Also: B1's four-line display `grep -E "zigbee\.(adopt_list_loaded|adoption_maps_rehydrated|availability_seeded|network_resumed)" | head -4` will return **three** lines, not four, for the same reason. **The adopt-list fact is still observable** — `adoption_maps_rehydrated: devices=N` is INFO and carries the count the block actually wants.

**F-2 · `lookups=` is a MISS counter, not a lookup counter.** `EzspCoordinatorProtocol.lookupIeee` emits **exactly one** log line in its whole body: `log.warn("zigbee.lookup_eui64_failed: …")` on `status != 0`. **The success path returns the IEEE silently — there is no success-arm line.** So B3's `lookups=$(… grep -c 'lookup_eui64')` counts only failures. A coordinator-table **HIT** (the mains-router class — R-4b's S31, resolved in 315 ms) increments **nothing**, so the countdown can read `lookups=0 adopted=1` on a perfectly good adoption. **The useful reading, and it is the good news:** `lookups` going **0 → 1 is precisely the sleepy-device miss that arms the ZDO surface.** It is the C-003 tripwire — just not the thing its label says.

**F-3 · `zdo_req=` and `zdo_rsp=` over-count by substring; `zdo_rsp` can count a FAILURE as a success.** Four tokens share those prefixes — `zigbee.ieee_addr_req`, `zigbee.ieee_addr_req_unanswered`, `zigbee.ieee_addr_rsp`, `zigbee.ieee_addr_rsp_failed` — and the counters use unanchored `grep -c`:
- `zdo_req` = `grep -c 'zigbee.ieee_addr_req'` also matches `…_unanswered`, so **one unanswered request reads as `zdo_req=2`** (the attempt line, then the timeout line).
- `zdo_rsp` = `grep -c 'zigbee.ieee_addr_rsp'` also matches `…_rsp_failed` — **a non-SUCCESS ZDO status byte counts as a response.** `zdo_rsp ≥ 1` therefore does NOT establish the exit.
`zigbee.ieee_addr_rsp_failed` is a **fourth outcome the packet's B3 preamble never names** (it names only hit / miss-then-ZDO / unanswered).
**THE LIVE DISCRIMINATOR (use this while the countdown runs):** the failed-response arm returns empty, so the adapter follows it with `rejoin_candidate_unresolved … reason=zdo_miss`. Therefore — **`zdo_rsp` up *and* `unresolved` up in the same tick ⇒ it was a FAILED response, not the exit. `zdo_rsp` up *and* `adopted` up ⇒ the real thing.**
**The gate itself is sound and needs no change:** STOP-GATE R4c-3 requires the harvest's literal `ieee_addr_rsp … device=0xF044D3FFFED2A201`, and **only the success arm emits a `device=` field at all** (`…_rsp_failed` logs `nwk=` and `status=` only). The exit cannot be faked by a failure.

**F-4 · B3 step 0a/0b are correct against the schema — 254 is exactly legal.** `zigbee-config-schema.json`: `permit_join_duration` is `integer`, `minimum 1`, **`maximum 254`**, with **no schema default** (deliberate — an absent key must never auto-open a window). So `permit_join_duration: 254` sits exactly at the ceiling: **no clamp, and no `zigbee.permit_join_clamped` WARN.** `openPermitJoinWindow()` confirms the packet's stated semantics at source: absent key ⇒ returns immediately, window never opens (so B4's disarm genuinely closes the door); a restart re-opens while the key is present (so B3's arm-by-restart is the designed path); and on open it calls **`rejoinWindowClosedNoted.clear()` and `rejoinLookupAttempted.clear()`** — the packet's "opening the window clears that note and the once-per-nwk lookup set" is exact. Trust-Center join enablement (`enablePreconfiguredKeyJoins`) runs **before** the `permitJoin` frame, so a Zigbee 3.0 device can actually complete the key exchange inside the window.

### F-5 · B1's DOWNGRADE fence will not fire — verified with `dpkg --compare-versions`, not assumed

B1 installs with a bare `sudo apt install -y ~/homesynapse_*_arm64.deb` and makes "apt asking to DOWNGRADE" a STOP. The version grammar is `0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>` (R-7b/R-V), so the ordering question is real and worth settling before the card is touched — the packet's own fence `never --allow-downgrades` exists because getting this wrong is how a rig ends up running older bytes than it reports.

Both possible incumbents were compared against the new artifact with dpkg's own comparator:

| incumbent | new | dpkg verdict |
|---|---|---|
| `0.1.0+git20260903.124041.gef02d13` (R-4b's; the incumbent if H8-a did not install) | `0.1.0+git20260913.113754.ga458a64` | **UPGRADE** (new > incumbent) |
| `0.1.0+git20260906.114248.gf25291b` (H8-a's, had it run) | `0.1.0+git20260913.113754.ga458a64` | **UPGRADE** (new > incumbent) |

**Either way B1 is an ordinary upgrade.** The date field dominates the comparison and 20260913 > both. `--allow-downgrades` is not needed and must not be reached for; if apt nonetheless proposes a downgrade, that is evidence the incumbent is something neither branch above predicts — which is a genuine STOP, and now a *meaningful* one rather than a fence nobody has tested.

### F-10 · B1's `integration_schema_registered 1` is CORRECT — confirmed, not assumed

The line is emitted **once per registered integration schema**, in a loop over the drained fragment map (`HomeSynapseCore.installSchemaRegistry`, ~line 1365: `for (String integrationType : drained) LOG.info("lifecycle.integration_schema_registered: type={} stage=pre-load", …)`). So the expected count is *the number of fragments the composition root registers*, not a fixed 1.

`Main.integrationSchemaFragments()` (line 216) builds a `LinkedHashMap` containing **exactly one entry** — `ZigbeeIntegrationFactory.INTEGRATION_TYPE` → `configSchemaJson()` — and returns it unmodifiable. **One integration, therefore exactly one line, therefore the packet's EXPECTED of `1` is right on these bytes.**

Worth pinning because the assertion is load-bearing for PKG-SEC-2 (the schema composes *before* Phase-1 validation, which is what retired R-4's C-1 "unknown property" boot warning) and because its correct value will change silently the day a second integration is wired — at which point a packet asserting a literal `1` becomes wrong without anyone touching it. **Rec: assert `= the number of registered integrations`, or re-derive the constant whenever a second integration lands.**

### F-6 · B2's gradle block will LOG THE OPERATOR OUT OF THE CARD if a `gradlew` is found

```
which gradle java 2>/dev/null; for d in ~/homesynapse-core /opt/homesynapse; do if [ -x "$d/gradlew" ]; then (cd "$d" && timeout 180 ./gradlew --version 2>/dev/null | grep -m1 -i gradle) && exit 0; fi; done; echo "card-gradle: absent"
```

The block is pasted into an **interactive ssh login shell** (its WHERE line says so). `exit 0` therefore exits **that login shell** — the operator is dropped back to the desktop prompt mid-session, immediately after the one reading the block exists to take. Not destructive, and the `card-gradle:` line is already on screen when it happens, but it is a confusing failure *on the success path only*, which is the worst place to put one.

**Likelihood is low** (a Pi has no Gradle toolchain unless one was deliberately put there — `card-gradle: absent` is the expected answer), which is exactly why it would never be caught by testing the common case.

**Minimal T1 fix, changing nothing measured: wrap the whole block in a subshell** — `( … )` — so `exit 0` leaves the subshell and the ssh session survives. If the block is run unmodified and the shell does exit, **that exit is itself the answer** (a `gradlew` was found and its version line printed); ssh back in and continue at B3. Recommend the hub strike `exit 0` from the packet in favour of a flag-and-break, or keep the subshell wrapper as the standing pattern for any operator block containing `exit`.

### F-7 · B3's countdown loop runs LONGER than the window it watches — read the printed elapsed, not the tick count

The countdown is `for i in $(seq 1 24); do sleep 10; …6 × sudo journalctl…; done`, i.e. **24 ticks × (10 s sleep + six full journal scans)**. On the card each `journalctl … | grep -c` costs real time and grows with the journal, so the loop's wall-clock is materially more than 240 s while the permit-join window is a hard **254 s** measured by the coordinator, not by the loop.

**This is not a defect in what is measured** — the block prints `$(( $(date -u +%s) - T0 ))` as its first column, which is **true elapsed seconds from the window's own T0**, so every count line is honestly stamped. It is a defect in what the operator *infers*: "I have 24 ticks" is not "I have 254 seconds."

**The operator rule that follows:** drive the five provocations off the **printed `NNNs` column**, not off tick numbers, and treat **254 s as the hard close** — the five provocations at ~40 s apart consume ~200 s, so they must all be complete by roughly the `200s` line. Count lines continuing past `254s` are reporting on a **closed** door; a `rejoin_ignored_window_closed` increment after that point is correct behaviour, not a miss.

### F-8 · B2's read path is correct at source

`/api/v1/entities` is registered (`RestFilters.java:196`) and the default port is **7070** (`HomeSynapseConfig.java:92`, PLAN-M3 §10) — so B2's `curl http://127.0.0.1:7070/api/v1/entities` hits a real route on the loopback. The four registered read routes on these bytes are `/api/v1/entities`, `/api/v1/runs`, `/api/v1/automations`, `/api/v1/automations/{id}/non-firing` — consistent with R-4b's D-12 ruling, and R-4c names no fifth.

### F-9 · B1's own `dpkg-query` is CORRECT — do not "fix" it by analogy with D-5

B1's install block uses `dpkg-query -W -f '${Version}\n' homesynapse` with **single** quotes, and its WHERE line pastes it **directly on the card**, not through a nested ssh argument. There is no outer quoting layer to strip, so `${Version}` reaches dpkg-query intact and the format string works as intended. **D-5's fix applies to B0's block only.** Recorded explicitly because the two lines look nearly identical in the packet and a navigator correcting one by pattern-match would break the other.


---

## Deviations ledger — LONG FORM (relocated from the operator record's §9 at 2026-09-13T14:02:08Z)

The operator record's §9 carries a compact ledger and points here; this is the full reasoning for each entry, verbatim as first written, so nothing was summarised away.

 (D-n · tier · block · Z time · what · fix) + THE FINDINGS CARD FOR THE HUB


**⏺ filed 2026-09-13T13:43:05Z**

- **D-1 · T1 (instrument) · §0/§1 · 2026-09-13T13:4xZ** — the packet's §0 and §1 both assume a signed-in desktop browser. The navigator read the run anonymously after Nick made `homesynapse-core` public: the run page, both job pages, both job verdicts, the step lists and the artifact digests all render to a signed-out session, but **every step-log route answers `Not Found` (text/plain, i.e. auth-gated) without a session** — `…/commit/<sha>/checks/<job>/logs/<n>`, `…/actions/runs/<run>/job/<job>/logs/<n>`, `…/actions/runs/<run>/logs`, and the in-page `<details>` step toggle never loads a body. **Consequence:** §0's ⏺ is fully navigator-read; §1's version-grammar echo line must be operator-read. **Nothing measured or asserted was changed.** **Recommend to the hub:** §0's ⏺ (a run URL + two job colors) is machine-readable from a public repo and can be lifted off the operator entirely; §1's origin hash cannot. Splitting the two — §0 navigator-read, §1 operator-read — is a free reduction in operator load for every future packet of this shape.


**⏺ filed 2026-09-13T13:46:08Z**

- **D-2 · T1 (instrument) · §1 fetch block · 2026-09-13T13:5xZ** — **the packet's §1 has no freshness guard on the download, and its failure mode is silent.** The block hard-codes `~/Downloads/distribution-artifacts-arm64.zip`. That name is **stable across every install-smoke run**, so a browser that declines to overwrite (Chrome saves `…arm64 (1).zip`), or an operator who skips the download, leaves a *previous session's* zip at the exact path the block expands — and the block then returns a perfectly healthy-looking `count = 1` and a valid 64-hex sha256. **Every assertion in the block passes on the wrong bytes.** The only thing standing between that and an install of a nine-day-old artifact onto the held card is the operator reading `ga458a64` out of the filename by eye. Today it fired for real: the expanded .deb was `gef02d13`, the R-4b artifact, hash-identical to the R-4b record's own §0 line. **Fix applied (T1, glob + path only):** the re-attempt (a) moves the stale tree aside into `~/r3-history/` rather than letting `-Force` overwrite it — delete nothing, and the wrong bytes stay available as evidence; (b) expands into a *clean* directory so no prior `deb/build/` tree can satisfy the `find` glob; (c) selects the **newest** `distribution-artifacts-arm64*.zip` by mtime instead of a fixed name, and **prints the chosen zip's name, mtime and sha256** so the artifact's identity is on the ⏺ line itself, before the .deb is ever read. Nothing measured or asserted was changed; the three gate conditions are unaltered. **Recommend to the hub — this is a packet-class defect, not a today defect:** every packet in this family (R-3, R-4, R-4b, R-4c, H8-a) fetches a same-named artifact into a shared `~/Downloads` and asserts freshness with a human eye on a filename. The cheap standing fix is the one applied here — *name the artifact's identity on the ⏺ line before the hash is compared* — plus the stronger one now available: **GitHub publishes a per-artifact sha256 digest on the run summary page, readable ANONYMOUSLY on a public repo** (`distribution-artifacts-arm64` → `sha256:883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468` for run #53). Hashing the downloaded **zip** against that digest binds the download to the run *without* the auth-gated step log, and would have caught today's stale zip before it was ever expanded. Recommend §1 adopt it as a first-class gate.


**⏺ filed 2026-09-13T13:50:58Z**

- **D-3 · T1 (instrument substitution, EVIDENCE-STRENGTHENING) · §1 · 2026-09-13T13:5xZ — ★ THE ANONYMOUS ORIGIN GATE. ★** The packet binds the .deb to CI by having the operator read the `version-grammar echo` line out of the **arm64 job log** and compare its sha256 by eye. That log is **auth-gated** (D-1) and the comparison is a 64-hex human diff — the weakest link in a chain that exists to prevent exactly what D-2 caught. **A stronger, cheaper binding was available and is now MEASURED:** GitHub publishes a per-artifact **sha256 digest on the run summary page**, which renders to a **signed-out** session on a public repo. For run #53 it reads `distribution-artifacts-arm64 → sha256:883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468`. The downloaded zip hashed to **`883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468` — an exact match, first try.** **What this proves, and it is more than the packet asked for:** the *archive* is bit-identical to what CI uploaded, therefore **every byte inside it** — the .deb included — is CI's, without ever opening a job log. The echo line's comparison is a proper subset of this one. **The navigator therefore grades STOP-GATE R4c-1 PASSED on the digest chain**, and records the .deb hash `1f46c5c8…` as the artifact of record; the echo line remains welcome for the hub's re-derivation but is no longer load-bearing. Nothing measured or asserted was weakened — the gate's three conditions are all met, the third by a superset. **Recommend to the hub — adopt this as the standing §1 gate for every artifact packet:** (1) it is navigator-readable, removing a browser act from the operator entirely; (2) it catches a stale download *before* the zip is expanded, where D-2's failure went undetected through `count = 1` and a valid 64-hex hash; (3) it binds the whole archive rather than one file inside it; (4) it requires no credentials, so it survives the packet being run by anyone. The one caveat to record: this equality (GitHub's published digest == sha256 of the downloaded .zip) is **now measured once**, on `actions/upload-artifact` v4 output — it should be re-confirmed, not assumed, if the upload action's major version ever changes.




**⏺ filed 2026-09-13T13:53:08Z**

- **D-4 · T1 (navigator housekeeping, no measurement touched) · §9 · 2026-09-13T13:5xZ** — the desktop-phase **pre-flight source audit** (every rig-block journal token read against `a458a64`'s own emit site and log level, plus the C-003 reachability read, the census-format proof and the schema read) was authored into §9 and then **relocated verbatim** to its own file to keep this record inside the packet's `≤ ~30 KB` close-out cap: **`context/audits/2026-09-13_R-4c_preflight_source-audit.md` (11,367 B)**. Nothing was summarised away and no operator ⏺ was touched — the move happened before B0, and the file is the navigator's own instrument note, not a paste-back. **This is R-4b ask #10's lesson applied in the other direction:** that record hit 111 KB against a 14 KB cap and solved navigability instead of length; here the bulky evidence is split at the moment it is written, so the operator record stays a readable surface and the drill-down keeps its own path.
  **What the pre-flight established, for the hub, in five lines:**
  1. **★ C-003 is REACHABLE on these bytes** — the store-miss → `lookupIeee` (`0x0061`) → **`requestIeeeAddress` (ZDO `IEEE_addr_req`) on the air** → `admitRejoinCandidate(…, "unknown_sender")` chain is wired in `ZigbeeIntegrationAdapter.onRejoinCandidate(int,int)`, with `reason=zdo_miss` on the timeout arm. The exit is not speculative on `a458a64`.
  2. **The census greps will match** — `IEEEAddress.toString()` is `"0x" + String.format("%016X", …)`, uppercase; had it been `%016x` all six census lines would have read `0` and the day would have produced a **false total miss**.
  3. **F-1 — B1's `adopt_list_loaded 1` is WRONG on these bytes**: the line is `log.debug`, the packaged root logger is INFO. It will read **0**, correctly. B1's four-line display returns three lines for the same reason.
  4. **F-2/F-3 — three of B3's six live counters are mislabelled**: `lookups=` counts only MISSES (no success-arm line exists); `zdo_req=`/`zdo_rsp=` over-count by unanchored substring, and **`zdo_rsp` counts `ieee_addr_rsp_failed` — a fourth outcome the packet never names — as a response.** The **STOP-GATE is unaffected**: only the success arm emits `device=`, so the exit cannot be faked. The live discriminator is `zdo_rsp` **+** `unresolved` ⇒ failure; `zdo_rsp` **+** `adopted` ⇒ the real thing.
  5. **F-4 — B3's window is legal and exact**: `permit_join_duration` is `integer [1,254]` with **no schema default**, so `254` is at the ceiling — no clamp, no WARN — and `openPermitJoinWindow()` clears `rejoinWindowClosedNoted` and `rejoinLookupAttempted` on open, exactly as the packet's preamble claims.


**⏺ filed 2026-09-13T13:55:21Z**

- **D-5 · T1 (instrument) · B0 block 3 · 2026-09-13T13:5xZ — R-4b's D-2 was never fixed in this packet, and it recurred.** B0's boot glance carries `dpkg-query -W -f "${Version}\n" homesynapse` inside a **single-quoted** ssh argument. The local shell leaves `${Version}` alone, so it reaches the REMOTE shell still wrapped in DOUBLE quotes, where it expands to empty — the command degenerates to `dpkg-query -W -f '\n' homesynapse` and prints a bare newline. **This is R-4b's D-2 verbatim** (2026-09-04, §2 boot glance, token 3), where it was diagnosed at the rig, fixed on the spot, and written into that record's findings card as a recurring class. The R-4c packet was cut from that record and **inherited the defect unchanged.** **Fix applied:** R-4b's own remedy — `dpkg-query -W homesynapse` (no format string, therefore no `$` for the remote shell to swallow); `/opt/homesynapse/VERSION` remains the independent second surface on the next line. Nothing measured or asserted changed. **Navigator's own error, recorded:** the defect was *identified* from source before the block was handed over, and the block was nonetheless handed over verbatim with a warning attached, then re-issued corrected a minute later. Verbatim-first is the right default for a block whose behaviour is unknown; it is the **wrong** default for a defect a prior record has already PROVEN — that is precisely the case T1 exists for. **Recommend to the hub — this is the packet-authoring lesson, and it is the second time it has cost rig attention:** R-4b's ask #5 asked the hub to "correct the packet's five instrument defects", and R-4b's findings card §5(a) says *"re-derive paths against the prior record's own deviations."* D-1, D-2 and D-5 in this session are all the same failure to do that. **The mechanical fix is cheap: before a packet goes LIVE, grep the prior record's deviations ledger for every command string the new packet reuses.** Three of today's five deviations would not exist.



---

## B0 — long-form readings (relocated from the operator record's §2 at 2026-09-13T14:04:39Z)

The operator record's §2 keeps every ⏺ verbatim and a compact per-condition verdict table; these are the derived readings behind them.

**★ B0-a-1 — THE BENCH REGISTRY IS BYTE-STABLE ACROSS NINE DAYS.** All six `device_relinked` IEEE→deviceId pairs are **identical to the R-4b record's 2026-09-04 bench read**, and `registry.projection_live` reads `devices=6 entities=6 **position=25065**` — the *same position integer* as R-4b's. Nine days, nine nightlies, and the registry projection has not advanced a single position. That is the expected shape for a projection that advances only on device/entity registration, and it is now measured rather than assumed. It also means **the six census IEEEs in the packet are live on this fleet today**, not merely historical.

**★ B0-a-2 — A ONE-NIGHT FLOOR REGRESSION, SELF-RECOVERED (for the docket, not a stop).** `2026-09-12` read **`7/9 · FAIL command-confirm-s31 · ON-latency n/a(FAIL)`**; `2026-09-13` returned to `8/9 PASS · ON-latency 3.57s`. The failing scenario is the S31 command-confirm path — the same device and the same confirm semantics that R-4b's C4 exercised to reach `CONFIRMED`. One night, one scenario, recovered unaided, bundle preserved at `…/bundles/command-confirm-s31-20260912T083148Z`. **Recommend the hub docket it as an intermittent on the confirm path** — a single self-recovering FAIL is exactly the shape that gets forgotten, and OR-BUS-SILENT-DROP's row would want to know whether the 09-12 bundle shows a missed delivery or a slow device. **No R-4c act follows from it; the bench is green today and B5's target is the 09-13 line.**

**★ B0-a-2 — A ONE-NIGHT FLOOR REGRESSION, SELF-RECOVERED (for the docket, not a stop).** `2026-09-12` read **`7/9 · FAIL command-confirm-s31 · ON-latency n/a(FAIL)`**; `2026-09-13` returned to `8/9 PASS · ON-latency 3.57s`. The failing scenario is the S31 command-confirm path — the same device and the same confirm semantics that R-4b's C4 exercised to reach `CONFIRMED`. One night, one scenario, recovered unaided, bundle preserved at `…/bundles/command-confirm-s31-20260912T083148Z`. **Recommend the hub docket it as an intermittent on the confirm path** — a single self-recovering FAIL is exactly the shape that gets forgotten, and OR-BUS-SILENT-DROP's row would want to know whether the 09-12 bundle shows a missed delivery or a slow device. **No R-4c act follows from it; the bench is green today and B5's target is the 09-13 line.**

**★ B0-c-1 — D-5 IS PROVEN, NOT ARGUED.** Nick ran the packet's block and the corrected block back-to-back, nine seconds apart, against the same card and the same service invocation. The packet's version token printed **a bare blank line**; the corrected token printed `homesynapse	0.1.0+git20260903.124041.gef02d13`. Every other field in the two runs is identical. **R-4b's D-2 is therefore confirmed as a live, reproducible packet defect on its third sighting** (R-4b §2 token 3 · predicted from source here at 13:5xZ · reproduced at 13:58:21Z), and the one-token fix is confirmed as its remedy. Predicted before the paste, not diagnosed after it.

**★ B0-c-2 — `H8A: not run`, SETTLED ON THE WIRE.** The packet's own disambiguator: the incumbent reads `f25291b` if H8-a installed Friday night, `…gef02d13` if it did not. **It reads `0.1.0+git20260903.124041.gef02d13` on both surfaces** (`dpkg-query` and `/opt/homesynapse/VERSION`). H8-a never ran; the held card has carried R-4b's artifact untouched since 2026-09-04. This corroborates the documentary evidence (`context/audits/2026-09-06_H8a_real-wire_operator-record.md` is a 4,533-byte scaffold with no ⏺ under any heading). **The word for the hub is `H8A: not run`.**

**★ B0-c-2 — `H8A: not run`, SETTLED ON THE WIRE.** The packet's own disambiguator: the incumbent reads `f25291b` if H8-a installed Friday night, `…gef02d13` if it did not. **It reads `0.1.0+git20260903.124041.gef02d13` on both surfaces** (`dpkg-query` and `/opt/homesynapse/VERSION`). H8-a never ran; the held card has carried R-4b's artifact untouched since 2026-09-04. This corroborates the documentary evidence (`context/audits/2026-09-06_H8a_real-wire_operator-record.md` is a 4,533-byte scaffold with no ⏺ under any heading). **The word for the hub is `H8A: not run`.**

**★ B0-c-3 — THE CARD'S CLOCK IS ET, AND THIS PACKET DROPPED THE CALIBRATION THAT SAYS SO.** The journal renders `Sep 13 09:57:28` while `date -u` in the same command reads `13:58:30Z` — a 4-hour offset, i.e. the card is on **US Eastern (EDT, UTC−4)**, so `network_resumed` fired at **13:57:28Z, 62 s before the glance** (a correct fresh boot after the ~90 s wait). R-4b's D-2 fix deliberately folded `date "+%Z %z"` into this very block *because* "every timestamp correlation today depends on it", and **R-4c dropped it.** It matters here more than it did there: B3's chain harvest, the window's open/close instants and the countdown's elapsed column all have to be correlated against journal lines rendered in card-local time. The offset is **derived** above and is **measured explicitly** in D-6's re-read rather than left inferred.

**★ B0-c-3 — THE CARD'S CLOCK IS ET, AND THIS PACKET DROPPED THE CALIBRATION THAT SAYS SO.** The journal renders `Sep 13 09:57:28` while `date -u` in the same command reads `13:58:30Z` — a 4-hour offset, i.e. the card is on **US Eastern (EDT, UTC−4)**, so `network_resumed` fired at **13:57:28Z, 62 s before the glance** (a correct fresh boot after the ~90 s wait). R-4b's D-2 fix deliberately folded `date "+%Z %z"` into this very block *because* "every timestamp correlation today depends on it", and **R-4c dropped it.** It matters here more than it did there: B3's chain harvest, the window's open/close instants and the countdown's elapsed column all have to be correlated against journal lines rendered in card-local time. The offset is **derived** above and is **measured explicitly** in D-6's re-read rather than left inferred.

**★ B0-c-4 — TZ MEASURED: `EDT -0400`.** Confirms B0-c-3's derivation exactly. **Every journal timestamp today is card-local EDT; add 4 h for Z.** The B0 resume at `09:57:28` EDT = **`13:57:28Z`**.

**★ B0-c-5 — THE CARD'S SIX ARE THE PACKET'S SIX, IN THE PACKET'S ORDER.** The packet's census list is validated against `zigbee.yaml` **before** the window rather than at census time, so the T1 clause ("*the file, not this packet, is the truth*") is discharged in advance and **B3's census needs no re-derivation**:

| yaml line | IEEE | device | = packet census position |
|---|---|---|---|
| 4 | `0x00178801101A09BB` | Hue LCA017 | 1 ✓ |
| 5 | `0xF044D3FFFE9C78D7` | SNZB-03P | 2 ✓ |
| 6 | `0x00124B002FA8D1C5` | S31 Lite zb | 3 ✓ |
| 7 | **`0xF044D3FFFED2A201`** | **SNZB-02P — C-003's target** | 4 ✓ |
| 8 | `0xF044D3FFFE1C1E8E` | SNZB-01P | 5 ✓ |
| 9 | `0x449FDAFFFE688F57` | SNZB-04P contact | 6 ✓ |

**★ B0-c-5 — THE CARD'S SIX ARE THE PACKET'S SIX, IN THE PACKET'S ORDER.** The packet's census list is validated against `zigbee.yaml` **before** the window rather than at census time, so the T1 clause ("*the file, not this packet, is the truth*") is discharged in advance and **B3's census needs no re-derivation**:

| yaml line | IEEE | device | = packet census position |
|---|---|---|---|
| 4 | `0x00178801101A09BB` | Hue LCA017 | 1 ✓ |
| 5 | `0xF044D3FFFE9C78D7` | SNZB-03P | 2 ✓ |
| 6 | `0x00124B002FA8D1C5` | S31 Lite zb | 3 ✓ |
| 7 | **`0xF044D3FFFED2A201`** | **SNZB-02P — C-003's target** | 4 ✓ |
| 8 | `0xF044D3FFFE1C1E8E` | SNZB-01P | 5 ✓ |
| 9 | `0x449FDAFFFE688F57` | SNZB-04P contact | 6 ✓ |

**★ B0-c-6 — B3 step 0a's line arithmetic is CORRECT on this file (checked, not assumed).** `sed -i '1a …'` appends after line 1, and the file's line 1 is `serial_port`, line 2 `channel: 20`. Post-insert the file reads line 1 `serial_port` · line 2 `permit_join_duration: 254` · line 3 `channel: 20` · the six on lines 5–10 — **exactly the packet's EXPECTED.** The idempotency guard (R-4b's D-7, carried correctly into this packet) is the protection against a double paste.

**★ B0-c-7 — a sibling file sits beside the live config; it is inert, and that is worth stating rather than assuming.** `integrations/zigbee.yaml.pre-repair-2026-08-30` (299 B, Jul 21) shares the directory with the live `zigbee.yaml` (299 B, Sep 4). It does **not** end in `.yaml`, so a `*.yaml` loader cannot pick it up — and B3's `sed -i` addresses `zigbee.yaml` by exact path, so the window key cannot land in the wrong file. **Recorded because an identically-sized backup beside a live config is exactly the shape that produces a mystery later**; the hub may want a standing convention of keeping pre-change copies out of the loaded directory (R-4b's own backups went to `/root/r4b-history/`, and this packet's step 0a does the same — the stray is older than both).

**★ B0-c-7 — a sibling file sits beside the live config; it is inert, and that is worth stating rather than assuming.** `integrations/zigbee.yaml.pre-repair-2026-08-30` (299 B, Jul 21) shares the directory with the live `zigbee.yaml` (299 B, Sep 4). It does **not** end in `.yaml`, so a `*.yaml` loader cannot pick it up — and B3's `sed -i` addresses `zigbee.yaml` by exact path, so the window key cannot land in the wrong file. **Recorded because an identically-sized backup beside a live config is exactly the shape that produces a mystery later**; the hub may want a standing convention of keeping pre-change copies out of the loaded directory (R-4b's own backups went to `/root/r4b-history/`, and this packet's step 0a does the same — the stray is older than both).

**Other reads banked for later blocks:** `initial_api_token` is **44 B** on disk ⇒ 43 chars after `tr -d '\r\n'`, matching R-4b's measured `token_len=43` and clearing B2's `-ge 40` gate. `homesynapse.yaml` is 426 B dated Sep 4 14:56 — R-4b's Path-B re-bind, untouched since; **R-4c is measurement-only and does not read or write it.**


## B1 — long-form readings (relocated from the operator record's §3 at 2026-09-13T14:16:31Z)

**★ B1-b-1 — THE ROW GROWTH IS EVIDENCE, NOT NOISE: the fleet's reporting cadence is unchanged since R-4b, to within 3%.**

| | rows | window | rate |
|---|---|---|---|
| **R-4c today** | 219 @ `13:58:30Z` → 228 @ ~`14:13Z` | +9 over ~14.5 min | **0.621 rows/min** |
| **R-4b (2026-09-04)** | 173 @ `19:08:58Z` → 212 @ `20:09:35Z` | +39 over 60 m 37 s | **0.643 rows/min** |

Two independent sessions, nine days apart, on the same fleet and the same coordinator: **0.621 vs 0.643 rows/min.** This is the pre-install baseline B4's `ROWS-W1 > ROWS-A` assertion rests on, and it says the store was already ingesting normally *before* the new bytes landed — so any change in rate after B1 is attributable to the install rather than to an unknown starting state. Recorded because a bare "228" tells the hub nothing, and "228 ≠ 219" would tell it something false.


**★ B1-c-1 — F-9 IS NOW PROVEN FROM BOTH SIDES, and it validates the scope of the D-5 fix.** This block's `dpkg-query -W -f '${Version}\n' homesynapse` **printed the version correctly**, while B0's near-identical `dpkg-query -W -f "${Version}\n" homesynapse` printed **a bare blank line** at 13:58:21Z. The difference is exactly the one read out of the source before either was run: **single** quotes pasted directly on the card survive; **double** quotes nested inside a single-quoted `ssh` argument are expanded away by the remote shell. Both halves were predicted pre-flight (F-9) and both are now measured. **This is why D-5's fix was scoped to B0's block alone** — a navigator correcting the two by pattern-match would have broken the one that works. Recorded as the discriminating case for any future packet that carries both forms.


## B1 block 4 — long-form readings

**★ B1-d-1 — THE PRE-FLIGHT METHOD HAS NOW PAID OFF TWICE, ON PREDICTIONS MADE BEFORE THE CARD WAS TOUCHED.** Two source-derived predictions were filed in this companion *before* B0 and have now both landed on the wire:
1. **F-9 / D-5 (the quoting pair)** — B0's `-f "${Version}\n"` nested in a single-quoted ssh arg printed a **bare blank** (13:58:21Z); B1's `-f '${Version}\n'` pasted directly on the card printed the version **correctly** (14:17:20Z). Both halves predicted, both measured, and the prediction is what kept the D-5 fix from being misapplied to the block that works.
2. **F-1 (`adopt_list_loaded` is DEBUG under an INFO root)** — predicted to read **0** against the packet's EXPECTED of **1**, and to make the four-line display return **three** lines. Both occurred exactly.
**Why this matters to the hub beyond today:** each of these would have presented at the rig as a MISMATCH on a *healthy* card — the first as a missing version, the second as a missing token and a short display. Under the packet's own escalation ladder a navigator with no pre-flight would have spent T2 read-only probes on both, inside a ≤90-minute hardware slot, to arrive at "the instrument was wrong." **The desktop source audit cost nothing and pre-empted both.** Recommend the hub make a pre-flight token-and-level read a standing step for every packet that asserts journal counts — it is the cheapest defect-removal step available, it runs while the operator is still at the desk, and it converts rig surprises into desk facts.

**★ B1-d-2 — `Configuration issue 0` is now proven on a FOURTH artifact.** R-4 found the boot running on an "unknown property" WARNING (its C-1); PKG-SEC-2 fixed it by composing the integration schema fragment *before* Phase-1 validation; R-4b proved the fix on `ef02d13` ("**PKG-SEC-2 PROVEN, R-4's C-1 GONE**"). It now reads 0 again on `a458a64`, whose Java carries F-R4-1b + HONESTY-1 + EXPLAIN-114a + BUS-ORDER-1 on top. The invariant has survived four artifacts and two integration-schema-adjacent feature landings. **Banked as a bound, not a closure** — the count proves absence on *this* config, and the card's `zigbee.yaml` is about to be edited at B3, which is the one moment in the session that could produce a non-zero. **The B4 disarm block re-counts this token for exactly that reason** — worth the hub noting that the packet got that ordering right.

**★ B1-d-3 — the first `bus.delivery_anomaly` datum on BUS-ORDER-1's own bytes.** `a458a64` *is* BUS-ORDER-1 (read-forward LIVE delivery: the cursor delivers, the checkpoint floors, the notification wakes). FIX-1a's detector counts **0** across the boot invocation. This is a bound on OR-BUS-SILENT-DROP measured on the wire rather than in CI — but only over a quiet boot, which is the weakest possible exercise of the delivery path. **The load-bearing read is B4's**, which counts the same token across the whole invocation *including the permit-join window*, i.e. across real inbound Zigbee traffic, adoptions, entity registrations and state reports. A zero there is a materially stronger bound than a zero here. Recommend the hub record both and weight them differently.


## F-11 · The physical choreography of B3, reconstructed for the operator (the packet scatters it)

The packet carries B3's physical acts inside a shell banner string, mid-block, where the operator meets them for the first time **after** pasting the arm command and starting a 254-second coordinator clock. The `≤90 min` slot and R-4b's D-8 (a hand-timed window voided by ordinary distraction) both argue for the opposite: the operator should hold the whole choreography *before* the clock starts. It was therefore issued as a standalone briefing at 14:2xZ, ahead of B2, so the devices could be staged while a non-timed block ran.

**What the briefing carried that the packet does not:**
1. **The provocation schedule keyed to the block's own elapsed column** (40/80/120/160/200 s, door at 254 s), with the explicit note that the loop keeps printing past 254 s because six journal scans per tick cost real time — so late lines report on a **closed** door and are not failures. Without this the operator reads tick numbers as seconds and mis-times the window.
2. **The factory-reset fence stated as a consequence, not a rule** — a 5 s press on any Sonoff is a factory reset, and on the SNZB-02P specifically that would make **C-003 unreachable for the session** and force a re-pair. The packet states the fence; it does not state what it costs.
3. **The S31 load check (D-8)** — absent from the packet entirely.
4. **The priority ordering restated as a single sequence** — harvest → B4 disarm (unconditional) → B5 restore, with B5 outranking analysis.
5. **Which provocation is load-bearing.** Only #1 (the SNZB-02P) can produce C-003; #2–#5 are corroborating. An operator who knows that will spend the window's attention correctly — and will know to escalate the warming of #1 rather than keeping to a schedule if it stays silent.

**Rec to the hub:** a windowed-provocation block should be preceded in the packet by a standalone, non-timed **STAGING** block that lists the physical acts, the fences with their consequences, and which act is load-bearing. R-4b's D-8 already asked for the timing to be taken away from the human; this is the same lesson applied to the *instructions* rather than the clock.


## B2 read 1 — long-form: why the packet's null-row premise fails on this card

The packet's B2 EXPECTED names its null candidate explicitly: *"the Hue's entity from R-4, absent from the air."* That premise does not hold on the held card, and the reason is in R-4b's own record.

**R-4b §0, C4:** *"C4 PATH TAKEN: **B** (no light entity existed; the Hue never answered)."* Path B was selected precisely **because the held card had no light entity to bind an automation to.** An adopted device with no registered entity does not appear in `/api/v1/entities` at all — so the Hue cannot be the null row here; it is not a row.

The packet appears to have carried the expectation forward from **R-4** (an earlier session, a different registry state) without re-deriving it against **R-4b's** finding that the held card's entity set had no light in it. That is the same class as D-1/D-2/D-5/D-6 — an expectation inherited from a prior packet rather than re-derived from the prior *record* — but it lands differently: the earlier four were command defects that cost time, whereas this one would have cost **a wrong scientific conclusion**. An operator grading strictly would file "LASTREPORTED-1b MISS — no null row", and the hub would bank a failure where the mechanism is in fact working correctly and being tested harder than designed.

**The honest three-line statement for the hub:**
1. LASTREPORTED-1b's **instant arm: PROVEN on silicon**, on `a458a64`, including persistence across a version upgrade and a service restart, and including a nine-day-stale instant on an `UNAVAILABLE` entity that was *not* refreshed.
2. LASTREPORTED-1b's **null arm: NOT TESTED** — no never-reported entity exists on this card. Not a failure; an absence of test material.
3. **The null arm's only opportunity this session is a fresh adoption in B3's window**, read at B4. Whether it is exercised depends on whether the SNZB-02P adopts *and* on whether its first frame is classified as a state report before B4's read — which is a genuine open question, not a foregone conclusion.

**Rec to the hub:** when a packet names a *specific expected witness* for an invariant ("the Hue's entity"), the witness should be re-derived against the most recent record of that machine's state, not inherited. A witness that has ceased to exist turns a passing mechanism into a recorded failure.

## The held card's three entities — identification status

Entity ULIDs `01M19RHWXYZ…`, `01M19XN7NNQ…`, `01M1PRQN03X…` with device ULIDs in the `01M19…`/`01M1P…` bands. The third is identified: **R-4b §0 C4 names `01M1PRQN03X8H4MNEZQ62F76F1` as the S31 adopted at 17:51:15.518Z via `source=rejoin`** — consistent with its live `14:24:01Z` report today (a mains router, the only one of the three reporting on a short cadence).

The first two are the devices the held card carried **before** R-4b (R-4b: *"the held card carried two, and three after today"*), minted in an earlier ULID millisecond band than the S31 — consistent with that ordering. **They are not yet mapped to IEEEs in this session.** The mapping is cheap and read-only: this invocation's `zigbee.device_relinked` lines carry `device=<IEEE> deviceId=<ULID>` pairs, exactly as the bench card's did at B0. Probing it before B3 makes the census interpretable — the census reports `adopted_this_invocation` per IEEE, which says nothing about which IEEEs the card *already* knew. Folded into B2 block 2.


## B2 block 2 — long-form: what the IEEE→deviceId probe bought, and why it was worth a T2 slot

The probe was not in the packet. It cost one read-only journal grep on an already-open session and it changed three things:

1. **It closed D-9 beyond argument.** The packet's null witness was "the Hue's entity". The card's three `device_relinked` lines name the S31, the SNZB-03P and the SNZB-04P — **the Hue is not relinked at all**, so its device is not in the held card's registry and its entity cannot exist. D-9 moves from "the witness probably doesn't exist" to "the witness provably doesn't exist."

2. **It turned the packet's hedge into a prediction.** The packet could not say whether the SNZB-01P and SNZB-04P would behave as unknown senders; it wrote both branches and left the operator to discover which. The card's registry decides it in advance: **SNZB-01P unknown, SNZB-04P known.** An operator who knows this before the window can read the countdown correctly in real time — a `lookups` increment during provocation 2 is *expected*, not an anomaly, and its *absence* during provocation 3 is *expected*, not a missed device.

3. **It found a second C-003 witness that the session would otherwise have collected by accident and possibly mis-read.** If the SNZB-01P chain appears in the harvest and nobody knew it was unknown, the natural reading is "noise from a device we already had". Knowing it is unknown makes it *evidence*: a second independent traversal of the miss→air→admit path, on a second sleepy device, in the same window and the same invocation.

**Rec to the hub — this is a cheap standing addition to any adoption-measuring packet:** read `device_relinked` (IEEE→deviceId) at the top of the session and join it to the entities read. The registry's contents decide what every subsequent provocation *means*, and the packet's own census (`adopted_this_invocation` per IEEE) reports only what adopted **during** the invocation — it says nothing about what was already known, which is exactly the baseline needed to interpret it.

**On the gradle answer.** `card-gradle: absent`, with `which gradle java` also silent — so the card has neither a Gradle distribution, a wrapper in `~/homesynapse-core` or `/opt/homesynapse`, nor a JDK/JRE on PATH (the service runs a jlink'd runtime image out of `/opt/homesynapse`, which does not put `java` on the operator's PATH). **The held card is a run-only target.** TR-1b's driver must therefore assume cross-build-and-ship, not on-card build; any driver step that wants a Gradle verb has to run on the desk or in CI and deliver an artifact, exactly as this session's own .deb path does.


## F-12 · B3's countdown zero is NOT the window's zero — the door shuts ~15–25 s EARLIER than the printed column implies, and the true open instant is thrown away

Read out of the block's own structure before it was run:

```
sudo systemctl restart homesynapse.service;   # t=0 — the window opens DURING this startup
sleep 25;                                      # …the adapter calls openPermitJoinWindow() at network-up, ~8–12 s in
INV=$(…); … | sed 's/^.*INFO *//';             # ← STRIPS the journal timestamp off permit_join_opened
T0=$(date -u +%s);                             # t≈25 s — the countdown's zero is set HERE
echo "WINDOW OPEN at $(date -u +%H:%M:%SZ) — 254 s."   # ← claims the window opens NOW. It opened ~15–25 s ago.
```

**Two distinct defects, one cause.**

**(a) The elapsed column under-reports the window's true age.** `openPermitJoinWindow()` runs once at adapter start, after `NETWORK_UP` — on this card the cold-boot resume took ~9 s (B0: restart→`network_resumed`), and a warm service restart is comparable. `T0` is then set a further `sleep 25` later. **So `T0 ≈ window_open + 13…17 s`**, and the coordinator's hard 254 s close lands at a *printed* elapsed of roughly **230–240 s, not 254 s.** An operator pacing provocations against the printed column and trusting "254 s" will fire the last one **after the door has shut** and read the resulting `rejoin_ignored_window_closed` as a device failure.

**(b) The recorded window-open instant is WRONG, and the right one is deliberately discarded.** The block prints `WINDOW OPEN at $(date -u +%H:%M:%SZ)` — the time at `T0`, not the time the door opened — while `sed 's/^.*INFO *//'` strips the real instant off the `permit_join_opened` line before the operator ever sees it. The ⏺ therefore carries a window-open timestamp that is systematically ~15–25 s late. Every later correlation (which provocation landed inside the window, how long the ZDO exchange took from door-open, whether a device answered before or after close) is computed against a false zero.

**T1 fix applied — additive, nothing measured altered:** the display grep is read with `-o short-iso-precise` so `permit_join_opened`, `network_resumed` and `network_formed` keep their true journal timestamps (with UTC offset, so the EDT correction of B0-c-4 is explicit rather than inferred), and `T0` is printed to sub-second precision beside them. The countdown loop, its counters, its interval, its 24 iterations and every assertion are **unchanged**. The offset `T0 − permit_join_opened` is then an exact measured quantity in the record, and the true door-close instant is `permit_join_opened + 254 s` rather than a guess.

**Rec to the hub — this is R-4b's D-8 unfinished.** R-4b took the window's *timing* away from the human and made the block self-timing; that fix is in this packet and works. But the block still reports its own zero rather than the coordinator's, and still strips the only line that carries the truth. **A self-timing window block must anchor its countdown to the `permit_join_opened` instant it just read, not to `date` at the moment the loop starts** — the remaining half of D-8's lesson.


## F-13 · The HARVEST block strips the timestamps off the C-003 chain — the same defect as F-12, on the block that produces the exit evidence

The harvest renders the chain through `sed 's/^.*\(INFO\|WARN\|DEBUG\) *//'`, which deletes everything up to and including the level token — **including the journal timestamp.** The chain is the evidence STOP-GATE R4c-3 is graded on, and the packet's own §H says the hub mints C-003 "on the chain".

**What the strip costs, concretely.** R-4b's headline result is quoted in its §0 as: *"`17:51:15.203Z zigbee.rejoin_candidate: …` → full chain to `device_adopted` in **315 ms**."* That sentence is unwriteable from a timestamp-stripped harvest. With the strip in place the record can say a chain *occurred* but not:
- **how long the ZDO exchange took** (`ieee_addr_req` → `ieee_addr_rsp` latency, the one number that characterises the new over-the-air surface against the 10 s deadline and the only direct comparison to `0x0061`'s measured 315 ms table path);
- **where in the window each link fell** — which provocation drove it, and whether the admission happened before or after the 254 s close;
- **the ordering of two interleaved device chains**, which matters this session precisely because **two** unknown senders are being provoked (B2 blk 2) and their lines will interleave in one journal.

**Second defect in the same block: `head -40` can silently truncate.** With two unknown devices, five provocations, per-frame `rejoin_candidate` lines and the interview traffic that follows an admission, the matching set can exceed 40 lines — and a truncated display would drop the *second* device's chain entirely while every assertion still appeared to pass. This is R-4b's D-6 class verbatim (*"an assertion of absence or uniqueness requires a count, never a head/tail"*), here risking the loss of a positive rather than a negative.

**T1 fix applied — additive; the grep pattern, the census loop and every assertion are unchanged:** (1) the chain is rendered with `-o short-iso-precise`, preserving full ISO timestamps with UTC offset; (2) the **total** count of matching lines is printed *before* the display, so truncation is visible rather than silent; (3) the display cap is raised to 60. Nothing measured changed — the census still counts `device_adopted: device=<IEEE>` per IEEE exactly as written, and STOP-GATE R4c-3's conditions are untouched.

**Rec to the hub:** in any block whose output is the evidence for a mint, the journal timestamp is part of the evidence and must never be stripped for readability. Pair this with F-12 — between them the packet discards the window-open instant *and* the chain instants, which together are exactly the two quantities needed to state "the device was admitted N seconds into the window, and the air exchange took M milliseconds."

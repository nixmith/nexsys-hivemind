<!--
file: context/audits/2026-08-16_G1_rehearsal_complete-record_and_gate-day-brief.md
purpose: THE COMPLETE G1 REHEARSAL RECORD + GATE-DAY DECISION BRIEF. The single artifact the v53 hub reads before THE READ. Contains: the full instrument record of the Sat-Aug-15 night G1 rehearsal (commissioned by G-8, left NOT-RUN by the bench-evening return); the four-link client-defect chain that killed Act 2, proven end-to-end; the SYSTEM-LIVENESS HONESTY GAP (the night's most consequential product finding); F-21 RESOLVED at the instrument (the app holds NO serial port — measured); the G-11 timing decision (TIME-CRITICAL, the 03:30 fire); the G1 read-order of record for the gate; one-word-rulable decision rows; and the post-gate program rows this rehearsal minted.
audience: the PM mission-control hub (v53) — intake per law 37. Nick (operator + gate authority).
state-type: operator/desk return, COMPLETE. Layer-1 evidence, NOT a gate. Refutation welcome in BOTH directions — every load-bearing claim below names the instrument that produced it and the file:line that can refute it.
filed: 2026-08-16 ~01:05 CT (Sun), remote Cowork session under /nexsys-project-manager, operator Nick at the hands. Uncommitted; the hub's next order stages it.
version: **v2 — SUPERSEDES-IN-PLACE the v1 filed ~01:05 CT.** v1's body is UNCHANGED below (§0–§14); **§15 is APPENDED** and carries this session's response to the v53 hub's layer-2 audit and rulings — four substantive additions the hub's beat 1 needs (a missing prediction branch · a banked-evidence item the matrix treats only as a precondition · an interpretive tension in the DX-B frozen-row reading that must be STATED, not slipped · a pre-order porcelain check) plus one §10 refinement and two accepted corrections. **Appended, never rewritten — the census the hub planned (2 A + 2 M = exactly 4) is UNCHANGED by this, because this is the same file at the same path.**
supersedes: NOTHING is deleted. `context/audits/2026-08-15_G1-runbook_desk-adjudication_and_exhibit-readiness.md` (filed 20:45 CT, pre-rehearsal) REMAINS ON DISK as the pre-rehearsal desk record; it contains rows DX-1..DX-11 and the DX-4 recommendation that the instrument later REFUTED. It is kept deliberately — a desk prediction that the bench killed is provenance, not garbage (arc-discipline: errors legible, never quietly corrected). THIS file is the record of account where the two differ.
laws honored: the FREEZE HELD — zero code, config, constants, YAML, scenario, retune, deploy, or git operation on any repo or host; every act was a browser read, a DevTools read, or a read-only `/proc` glance · L3 — no token material was requested, received, or appears here · findings-never-fixes · arc-discipline 1 (never author on an unmeasured hop) · 13 (deploy-state re-derived at the instrument) · 19 (vacuous-verify pairing — the `/proc` check printed its pid before reporting absence) · 21/28 (per-hypothesis predictions FILED BEFORE the discriminating read) · 34 (chat is not a storage tier — this is filed).
-->

# G1 Rehearsal — Complete Record + Gate-Day Decision Brief

**Gate:** Sun 2026-08-16, THE READ. **This document was filed at 01:05 CT that morning.**
**Rehearsal window:** Sat 2026-08-15 ~20:45 CT → Sun 2026-08-16 ~01:00 CT. Operator: Nick (all Pi and browser acts). Session: remote Cowork hub-role, desk analysis + operator support. **No act was performed by the session; every observation below is Nick's terminal output or his screenshot, transcribed.**

---

## ⚠ §0 — THE TIME-CRITICAL ITEM, FIRST

**F-21 is RESOLVED, and it is the adverse branch.** The running application **does not hold the Zigbee serial port**:

```
homesynapse@hs-dev-1:~ $ for p in $(pgrep java); do echo "== pid $p =="; ls -l /proc/$p/fd 2>/dev/null | grep -i ttyUSB || echo "  (no ttyUSB fd)"; done
== pid 9767 ==
  (no ttyUSB fd)
```

One Java process, alive, serving the dashboard — and **zero `ttyUSB` file descriptors**. The check is anti-vacuous by construction: a pid printed, so `pgrep` found the process; the absence is a measurement, not a silence.

**The chain of facts:** the coordinator is physically present at `3-2.4.2` with `/dev/ttyUSB0` and the `/dev/zigbee` symlink both present since **Sat 16:38:43**. The app was restarted by the Aug-15 nightly at **~03:32–03:33 CT Saturday** — *thirteen hours before the coordinator arrived* — so it booted radio-blind. **It has now had ~8.5 hours with the device present and has not acquired it.** The app does not hotplug-acquire its transport.

**Consequence:** the Sun 03:30 CT nightly — **~2.5 hours from this filing** — is the last pre-READ instrument, and the v53 falsifiable prediction (7–8/9 confirms coordinator-absence was the whole story) rides on the app acquiring the port. It will acquire it **only if the nightly's own restart happens before the radio-dependent scenarios**, which the digests suggest (`boot-health` runs first and implies a boot; the automation ULID was re-minted 74 s into the Aug-15 nightly) but which is an **inference, not a measurement**.

**PM RECOMMENDATION — reversed from four hours ago, and the reversal is owned:** **FIRE G-11 NOW** (`bench.sh restart` + one `boot-health`), before the 03:30 fire.

At 21:00 CT I recommended *"do not fire G-11 tonight"* on the reasoning that the nightly probably self-heals. That recommendation rested on F-21 being **unresolved** and on a battery-sensor's report time. It is now resolved by direct measurement, and the discriminating fact is new: **the app has demonstrably failed to self-heal across 8.5 hours with the device present.** A system that did not hotplug-acquire in 8.5 hours will not do so in the next 2.5. The prior recommendation was correct on its evidence and is wrong on this evidence.

**Why the act is lawful:** G-11 is **pre-ruled sanctioned** (v52 beat 7 / PROJECT_SNAPSHOT): *"`bench.sh restart` + one boot-health = SANCTIONED RIG RECOVERY (not a freeze exception — the freeze froze code and evidence claims, not peripheral recovery)."* The only variation is **timing** — the pre-ruling scheduled it for Sunday morning *after* a 3/9. Firing it before the fire is a variation the hub/Nick must rule; it is the same act on the same authority.

**The asymmetry:** a restart is routine and frequently exercised (it appears throughout the bench record; identity durability across restart is proven — NQ-6). Its downside is small and bounded. The downside of waiting is a **third consecutive dead nightly on gate morning**, which would leave the READ with a product-evidence record stopping at Aug-13 and three excluded nights — a materially weaker position than "we found it, we recovered it, here is the verified-good night."

**No exhibit is at risk.** The permanent activity log is never deleted (the product's own line, rendered on every run page); the Aug-11 no-change run and all Jul-25/27 runs survive a restart. The bench-hero automation re-mints its ULID, which changes nothing — it already reads "No runs yet."

**If Nick declines:** entirely legitimate, and G-11 stands as originally ruled for Sunday morning. The cost is one nightly and a weaker evidence line, not the gate.

---

## §1 — Executive summary

The rehearsal was commissioned by **G-8** (ruled RUN-TONIGHT-AS-COMMISSIONED) and had been left **NOT RUN** by the bench-evening return under an operator-directed hold. It ran tonight. **It was the right call, and it paid for itself several times over.**

**Headline outcomes, in order of consequence:**

1. **A system-liveness honesty gap.** The Health surface reports **"✓ Live — processing events in real time," "Behind by: nothing — fully caught up,"** and **"✓ All clear — Nothing needs your attention"** while the application is **completely blind** — no radio, event log frozen at position 91229 for 40+ minutes, last device report 12+ hours old, and the Devices tile reporting **"Stale readings: none."** Every individual statement is defensible about the subsystem it measures. **The composite is a false impression, on the one product whose entire thesis is that it never claims what it has not measured.** §7.
2. **Act 2 of the demo is dead — from a CLIENT defect, with the API blameless.** `GET /api/v1/automations/{id}/non-firing` returned **200 OK, 395 bytes, in 17 ms**, with a complete and correct explanation. The dashboard threw on one unguarded property access and rendered an eternal spinner. Four-link chain, each link proven. §6.
3. **The error-posture law is violated app-wide.** `ErrorBoundary` is documented as **LOAD-BEARING** and forbids *"a silent blank or an eternal spinner"* — and it is mounted in **exactly one view** in the entire application. The July-27 incident it was written to prevent reproduced tonight on a different surface. §6.3.
4. **F-21 resolved, adverse.** §0.
5. **Act 3 exhibits 2 and 3 are FOUND and are excellent.** The five-modes-distinct rendering works on real bench data; the deployed wire carries v1.1.2 `resultOutcome`. **DX-6, the demo's largest pre-rehearsal risk, is resolved in our favour.** §5 / §9.
6. **Act 3 exhibit 1 (CONFIRMED with latency) does not exist on the demo surface** — adjudicated across four sampled runs plus a corpus argument. It moves to the ledger. §5.
7. **The C1 one-way door is INTACT.** Nothing found tonight touches the false-CONFIRM clause. Every defect is in the **observability/reporting** layer; none is in the **verdict** layer. §9.

**The shape of the result:** the honesty architecture is **proven at the action-verdict layer** and **gapped at the system-liveness layer**. That is a bounded, nameable, non-thesis-breaking finding — and it was produced by the project's own process, under freeze, 14 hours before the gate, with zero lines of code changed.

---

## §2 — Execution adjudication: what "execute the runbook" could mean

The dispatch was *"Read `context/handoff/2026-08-14_G1_gate-day-demo_runbook.md` and execute it."*

**Runbook integrity:** the uploaded copy is byte-identical to the repo copy — `md5 81b43b07d0cda560b7d26523a4b850c4`, 5 637 B both. The file read is the file of record.

**The session cannot perform the demo.** Measured, not asserted (arc-discipline 1):

| Hop the demo needs | Instrument | Result |
|---|---|---|
| SSH tunnel from the Windows host | — | The device bridge exposes **mounted folders**, not a shell on that host. |
| A shell on the Pi | `device_bash` (operator's local Linux VM) | **No network access by construction.** |
| Network path from the cloud container | cloud `bash` | Allowlisted egress; **no route to the operator's LAN**. |
| A browser | `mcp__claude-in-chrome__list_connected_browsers` | Returned **`[]`** — no extension connected. Measured 20:45 CT. |
| The API token | — | **L3 forbids it structurally.** |

The runbook's own `audience:` line already assigns performance to Nick and stewardship to the hub. **Verdict: NOT-EXECUTABLE-BY-HUB-SESSION; the session executed the runbook's pre-flight and supported the operator through the rehearsal.**

---

## §3 — The ordering finding

At dispatch the session banner read *"Sunday, August 16."* **That was the UTC date.** The container clock read `2026-08-16 01:45 UTC`; in `America/Chicago` (UTC−5) that was **Sat 2026-08-15 20:45 CT**. Corroborated by the spine: the bench-evening return filed 18:19 CT that day, the v53 prompt banked 18:41 CT.

**Consequence:** G1 is the **gate-day** script and its own §4 protocol places it **LAST at the READ**. Performing it Saturday would have executed a gate artifact a day early and out of ruled order. **Tonight's commissioned act was the runbook's own `## Rehearsal` section — "Sat evening, once."** Nick ruled **REHEARSE** at the decision row; the rest of this document is that rehearsal.

**Standing hazard for future sessions:** a remote session's date banner is UTC-derived. Any act gated on the operator's local calendar day must re-derive from the operator's timezone, never from the banner. *(Candidate harvest row → W-SKILLS-3.)*

---

## §4 — The instrument record (⏺ sets, verbatim)

### ⏺ 4.1 Setup

Tunnel `ssh -N -L 7070:127.0.0.1:7070 pi` up; browser at `http://localhost:7070/`; token read on the Pi terminal and typed into the browser only (**L3 held — no token material entered the conversation at any point**). Dashboard rendered.

### ⏺ 4.2 Act 0 — the exhibit inventory (`#/explain`)

**"Your automations" contains exactly ONE row:**

```
bench-hero                                          ✓ On   No runs yet   Why didn't it?
state change trigger · command action · delay action · command action · delay action · command action · delay actio...
```

- **No "Why did it fire?" link** — the row reads **"No runs yet."**
- **DX-4 (the desk recommendation to enter Act 1 through a named automation) is REFUTED at the instrument.** The session proposed it from source; the live data killed it. Recorded, not quietly dropped.
- `bench-hero` has **no condition component** — `state change trigger` then command/delay actions only.

### ⏺ 4.3 The runs list (`#/explain/runs`)

**50+ rows, all reading `An earlier automation`**, spanning **4 days ago → 22 days ago and continuing below the fold** (Jul-24 → Aug-11). Every row `✓ Completed`. Header: `Updated 10 hr ago`.

### ⏺ 4.4 Act 1 / Act 3 — run detail, four runs sampled

**Run `01KYHPMP0MMNDHGJJ88D1NA9VD` (operator's random pick):**

```
01KX1PA4HSJ581GASYB7DHE40F turned on because
01KX1PB9AAB4VB3E10BD477TV3 changed at 6:51 AM.

This run happened under an earlier version of your automations, so its
name is no longer on record. The run itself is preserved.

● 01KX1PB9AAB4VB3E10BD477TV3 changed at 6:51 AM.        ▸ Trigger
→ Turned on 01KX1PA4HSJ581GASYB7DHE40F.                 [⏱ Sent — no reply]      ▸ Command ▸ Recorded reason
→ Ran set_brightness on 01KX1PA4HSJ581GASYB7DHE40F.     [⏱ Sent — no reply]      ▸ Command ▸ Recorded reason
→ Ran set_color_temperature on 01KX1PA4…                [⇄ Replaced]             ▸ Command ▸ Recorded outcome
     "A newer command took over before this one finished. That is a change of intent, not a failure."
→ Ran set_color_temperature on 01KX1PA4…                [⏱ Sent — no reply]      ▸ Command ▸ Recorded reason
→ Ran identify on 01KX1PA4HSJ581GASYB7DHE40F.           [✓⋯ Accepted, never confirmed]  ▸ Command ▸ Recorded reason ▸ Recorded outcome
     "The device accepted the command but never reported doing it. The recorded reason below is
      shown exactly as recorded — an acceptance is not proof."
     "This kind of command is acknowledged but never reported back, so it cannot be confirmed."
◆ Done in 34.1s.                                        [✓ Completed]

"This explanation is rebuilt from HomeSynapse's permanent activity log — it is never deleted,
 so the run you need is always here."
```

**Three further runs sampled at the 19/20/21-days-ago bands — ALL STRUCTURALLY IDENTICAL** (same five actions, same five verdicts, `Done in 34.0s`):

| Run ULID | Decoded (CT) | Trigger shown | Duration |
|---|---|---|---|
| `01KYHPMP0MMNDHGJJ88D1NA9VD` | **2026-07-27 06:51:23 Mon** | 6:51 AM | 34.1 s |
| `01KYHQ0HN7QCN7G8J9MQNSTHHQ` | **2026-07-27 06:57:52 Mon** | 6:57 AM | 34.0 s |
| `01KYJZKHJGJR8Y94W2D203SJH6` | **2026-07-27 18:47:17 Mon** | 6:47 PM | 34.0 s |
| `01KYDKXJ4TAPDSGB6EDEBS0G7E` | **2026-07-25 16:46:50 Sat** | 4:46 PM | 34.0 s |

### ⏺ 4.5 Act 2 — `#/explain/why-not/01M028WEHCN64AFM2K0ZBSD5Z3`

**Renders "Why this didn't happen", "← Pick another automation", then an INDEFINITE `Loading…` spinner. It never resolves.** DevTools error badge showed **2** errors.

**The network request (DevTools → Network → Headers):**

```
GET http://localhost:7070/api/v1/automations/01M028WEHCN64AFM2K0ZBSD5Z3/non-firing
Status:  200 OK
Version: HTTP/1.1
Transferred: 557 B (395 B size)          Time: 17 ms
Content-Type: application/json           Content-Length: 395
Date: Sun, 16 Aug 2026 05:22:35 GMT
ETag: W/"91229"
X-HomeSynapse-View-Position: 91229
```

**The response body, whole:**

```json
{
  "data": {
    "automationId": "01M028WEHCN64AFM2K0ZBSD5Z3",
    "automationName": "bench-hero",
    "enabled": true,
    "verdict": "NEVER_TRIGGERED",
    "lastRelevantRunId": null,
    "explanation": "Automation 'bench-hero' has not been triggered; it fires on state change.",
    "triggerSummary": "state change",
    "lastEvaluation": null,
    "noCommandsIssued": null
  },
  "meta": { "viewPosition": 91229, "timestamp": "2026-08-16T05:44:17.103484856Z" }
}
```

**The console error (head; full stack in the operator paste):**

```
Uncaught (in promise) TypeError: can't access property "at", n.lastEvaluation is null
    children  http://localhost:7070/dashboard/assets/index-B9CmxYDm.js:1
    ...
index-B9CmxYDm.js:1:99808
```

**The minified source at the throw site (DevTools → Debugger):**

```
…,o("dd",{class:x.left,children:n.triggerSummary})]}),n.lastEvaluation.at?o("div",{class:"kvRow",children:[o(…
```

**Note the console shows the RAW TypeError — NOT the `[render-error] contained by ErrorBoundary:` prefix.** The boundary did not engage. This is the load-bearing evidence for §6.3.

### ⏺ 4.6 Close — Overview (`#/overview`)

```
✓ All running    HomeSynapse is live and watching your home in real time.

Recent runs                          Devices
An earlier automation   4 days ago   Available            5 of 6
An earlier automation   6 days ago   Offline                  1
An earlier automation   8 days ago   Not determined yet    none
An earlier automation   9 days ago   Stale readings        none
An earlier automation   9 days ago
                                     "Counts reflect each device's last report — not a live
                                      connection test. Open a device to see when it was last
                                      heard from."
```

Header freshness observed **"Updated 12 hr ago"** at ~21:00 CT, then **"Updated 7 min ago"** at ~22:15 CT.

### ⏺ 4.7 Devices (`#/devices`) — "Updated just now"

| Device ULID | Created (decoded, CT) | Status | Reading |
|---|---|---|---|
| `01KX1PA4HSJ581GASYB7DHE40F` | 2026-07-08 15:22:05 | **✗ Offline** | Current |
| `01KX1PB9AAB4VB3E10BD477TV3` | 2026-07-08 15:22:42 | ✓ Available | Current |
| `01KXW0157SP56CCSGJCNDCSQNG` | 2026-07-18 20:32:11 | ✓ Available | Current |
| `01KXW13WF0D6TYGN13WXHTG87K` | 2026-07-18 20:51:09 | ✓ Available | Current |
| `01KXW1W1SBJZERC9MBAMV2DWKE` | 2026-07-18 21:04:21 | ✓ Available | Current |
| `01KY12MQW954E4XYNKH0Y5H8VX` | 2026-07-20 19:54:02 | ✓ Available | Current |

**Device detail cards:**

```
01KX1PA4HSJ581GASYB7DHE40F           ✗ Offline
"Offline — last heard from —. Devices are rechecked every few minutes."
Color Temp Kelvin —   Brightness —   On —   Brightness Percent —   Last changed —
Last reported                                                        9:40 AM

01KX1PB9AAB4VB3E10BD477TV3           ✓ Available
"Available — last heard from —."
Battery Pct —   Occupied —   Last changed —
Last reported                                                       10:16 AM
```

### ⏺ 4.8 Activity (`#/events`)

```
Activity — Recent things that happened in your home, newest first.

        Endpoint GET /api/v1/events not found
                    [ Try again ]
```

Rendered as a **correct, calm, honest error state with retry**. `/api/v1/events` is B1-class, declared FROZEN-UNBUILT in `endpoints.ts` — the endpoint is not deployed; the nav item ships.

### ⏺ 4.9 Health (`#/health`) — "Updated 33 min ago"

```
System health — A quick read on whether everything is working.

Live status
  ✓ Live      HomeSynapse is up to date and processing events in real time.
  Behind by                                        nothing — fully caught up
  Projection version                                                       5
  Activity position                                                    91229

Reliability
  ✓ All clear    No events are stuck. Nothing needs your attention.
```

**`Activity position 91229` is byte-identical to the `X-HomeSynapse-View-Position: 91229` returned ~40 minutes earlier at 05:22:35 GMT. The event log did not advance at all in that window.**

### ⏺ 4.10 The `/proc` serial-port check

See §0. `pid 9767`, **no `ttyUSB` fd**.

### ⏺ 4.11 Timing

**NOT TIMED.** The operator was multitasking; every surface loaded instantly. **Recorded honestly as a gap.** The ≤10-minute budget is **unvalidated by measurement** but is not the risk: with Act 2 down and exhibit 1 absent, the demo runs **short**, not long.

---

## §5 — Findings register

IDs continue the pre-rehearsal desk file's **DX-** series (its DX-1..DX-11 stand except where marked). Severity is triage for reading order only; **the hub adjudicates, this session rules nothing.**

### CRITICAL

**DX-12 — SYSTEM-LIVENESS HONESTY GAP.** The Health board reports Live / fully-caught-up / all-clear, and the Devices tile reports `Stale readings: none`, while the application holds no radio, the log is frozen, and the newest device report is 12+ hours old. **Full treatment: §7.** *Refutation path: if a liveness signal for the integration/adapter layer exists on a surface not visited tonight, this finding narrows to a navigation problem. The session did not find one in `HealthView.tsx`'s rendered fields.*

**DX-13 — THE APP DOES NOT HOTPLUG-ACQUIRE ITS TRANSPORT, AND DOES NOT REPORT THE LOSS.** Measured: device present since 16:38:43, app running since ~03:33, no `ttyUSB` fd at 00:55. **This is a real-household failure mode** (dongle bumped, re-seated, USB power-save, powered-hub reboot) with a **silent** signature — the user's home stops responding and the health board says all-clear. Sibling of DX-12; same root class. *Refutation path: a restart that acquires the port confirms boot-time acquisition works and isolates the gap to hotplug — which is the G-11 act's second yield.*

**DX-14 — ACT 2 IS DEAD FROM A CLIENT DEFECT; THE API IS BLAMELESS.** 200 OK / 395 B / 17 ms, complete correct payload; the client threw. **Full treatment: §6.** *This is the strongest possible framing for the READ and should not be softened: the frozen v1.1 read-API — the contract the demo exists to demonstrate — performed perfectly.*

### HIGH

**DX-15 — THE ERROR-POSTURE LAW IS UNENFORCED APP-WIDE.** `ErrorBoundary` is mounted at **`RunChainView.tsx:26` and nowhere else** (exhaustive grep, §6.3). Its own doc calls it LOAD-BEARING and forbids the eternal spinner. **The 2026-07-27 incident reproduced on a sibling surface.** Direct instance of arc-discipline 25 (fix-the-class, not the file).

**DX-16 — CONTRACT-VS-WIRE NULLABILITY DIVERGENCE.** `contract.ts:350` declares `lastEvaluation` non-nullable; the wire sends `null`. **The type system actively concealed the need for a guard.** Class-level: the corpus needs a sweep for every FE dereference of a contract-declared-non-nullable field the server can null.

**DX-17 — ACT 3 EXHIBIT 1 (CONFIRMED WITH LATENCY) DOES NOT EXIST ON THE DEMO SURFACE.** Four runs sampled across three dates, all five-identical, zero `Confirmed` pills. Corroborating argument: the corpus holds **19 `state_confirmed` events** against ~345 organic runs; the digest's measured ON-latencies (`3.65 · 0.30 · 0.17 · 0.36 · 0.16 · 0.30` s) come from **nightly scenario legs that do not reach the explain surface** (surface run times are 06:51, 06:57, 16:46, 18:47, 20:34 — organic, never 03:30). **The runbook's premise — "any confirmed action from a recent nightly" — is refuted.** Exhibit 1 moves to the ledger.

**DX-18 — EVERY DEMO EXHIBIT TARGETS A DEVICE THAT HAS BEEN OFFLINE FOR WEEKS.** All five actions in every sampled run target `01KX1PA4HSJ581GASYB7DHE40F`, which the Devices page reports **Offline** and whose capabilities (brightness, colour temperature) identify it as the Hue — matching `1 SKIP(hue-online)` on **all 15 logged nightlies**. **This is why nothing ever confirms.** It is simultaneously the demo's biggest narrative risk (five amber tiles + a red row reads as "nothing works") and its strongest honesty exhibit (fifty runs, zero false claims). **Framing is everything — §10.**

### MEDIUM

**DX-19 — AUTOMATION IDENTITY IS RE-MINTED ON EVERY NIGHTLY RE-PROVISION.** The live `bench-hero` ULID `01M028WEHCN64AFM2K0ZBSD5Z3` decodes to **2026-08-15 03:33:45 CT** — ~74 s into the Aug-15 nightly — while 50+ runs exist. **This is the precise, timestamped root cause of F-13.** *Fact: the timestamp and the orphaned history. Inference (strong, not measured): nightly re-provisioning (`bench-hero RESTORED ✓`, every night) is the mechanism.* **State the distinction carefully at the READ: DEVICE identity is durable and proven (NQ-6; all six device ULIDs date to Jul-08/18/20 and survive every restart). It is the bench AUTOMATION that is re-provisioned from config.** Adjacent to the identity claims, not contradicting them — own the distinction rather than be handed it.

**DX-20 — DEVICE-DETAIL SELF-CONTRADICTION.** Both cards render **"last heard from —"** in prose while the table directly below shows **"Last reported: 9:40 AM" / "10:16 AM."** The sentence claims ignorance the row disproves — **on the availability-honesty surface the Close act celebrates.**

**DX-21 — `Stale readings: none` IS STRUCTURALLY UNFALSIFIABLE HERE.** Five devices whose last report is 12+ hours old are reported non-stale, consistent with `staleAfter` being null (which `OverviewView.tsx:79-81` explicitly notes is lawful). **A staleness indicator that cannot go stale is worse than none** — it converts an absent measurement into a positive reassurance. Sibling of DX-12.

**DX-22 — THE `Updated X ago` STAMP IS INCONSISTENT ACROSS SURFACES AT ONE MOMENT.** Observed in a single session: Overview `12 hr ago` → later `7 min ago`; runs list `10 hr ago`; why-not `1 hr ago`; Devices and run detail `just now`; Health `33 min ago`. Source: `feedback.tsx:79-86` renders `Updated {timeAgo(meta.timestamp)}` from the **server response timestamp**; the non-firing response stamped `2026-08-16T05:44:17Z` — i.e. *current*. **The session could not discriminate server-side stale-stamping from client-side response caching and does not claim to have.** Named discriminator for later: capture two surfaces' `meta.timestamp` against their HTTP `Date` headers in one sitting. **READ posture: if asked, do not assert a mechanism — say it is a known open question filed for post-gate.** *(An attempt to capture `/api/v1/entities` failed because DevTools was opened after navigation; the request had already completed. Declared.)*

### LOW / PROCESS

**DX-23 — `Activity` ships a nav item to an unbuilt endpoint.** 404, rendered honestly. **Demo hazard only: do not click Activity during the READ** — or click it deliberately and narrate it, which is on-thesis. Nav-hygiene row, post-gate.

**DX-24 — ACT 1'S SCRIPTED MIDDLE HOP DOES NOT EXIST.** The runbook narrates *trigger → **condition evaluation** → actions*. `bench-hero` has no condition component. Drop the hop; if asked, the automation has no conditions by design.

**DX-25 — F-15 CONFIRMED AT SOURCE.** `AppShell.tsx:11-18` ships `Overview · Ask why · Devices · Activity · Automations · Health`. **There is no "Runs" nav item**; the runbook's *"Runs surface"* names a screen that does not exist by that name. The list is at `#/explain/runs`, under **Ask why**.

**DX-26 — THE REMOTE SESSION DATE-BANNER HAZARD.** §3. Harvest row.

### REFUTED / WITHDRAWN (declared, not deleted)

**DX-4 — REFUTED.** The pre-rehearsal desk file recommended entering Act 1 via the Ask-why hub's named-automation list, predicting it would dissolve F-13/F-14. **The instrument killed it**: the only automation reads "No runs yet" and offers no "Why did it fire?" link. The recommendation was sound from source and wrong against live data. *The desk had no way to know `lastRunId` was null without looking — which is the entire argument for having run the rehearsal.*

**DX-6 — RESOLVED IN OUR FAVOUR.** The pre-rehearsal file's largest flagged risk was that a pre-v1.1.2 wire would render the honest-UNCONFIRMED exhibit as a red generic `Failed`, contradicting Nick's narration. **It does not.** See §9.1 for the proof.

---

## §6 — The Act-2 defect chain, in full

### 6.1 Link 1 — contract-vs-wire divergence

`web-ui/dashboard/src/lib/api/contract.ts:350`

```ts
lastEvaluation: { at: string | null; conditionsResult: string | null };
```

A **non-nullable object**. The server sends `"lastEvaluation": null` (§4.5, proven at the body). TypeScript therefore told the author the object could not be null, and any mock that always populated it kept the divergence invisible to the test suite.

### 6.2 Link 2 — the unguarded dereference

`web-ui/dashboard/src/views/WhyNotView.tsx:88`

```tsx
{nf.lastEvaluation.at ? (
```

Compiled and observed in the operator's debugger as `…n.lastEvaluation.at?o("div",{class:"kvRow"…`, throwing `TypeError: can't access property "at", n.lastEvaluation is null`. **Prediction/verification note: this exact line and mechanism were FILED IN ADVANCE of the operator opening DevTools, and the read confirmed them — per-hypothesis prediction before the discriminating read (arc-discipline 21/28).**

Second latent site on the same object: `nf.lastEvaluation.conditionsResult` (line ~89) — unreached only because the first throws.

### 6.3 Link 3 — no containment (the class-level finding)

Exhaustive grep of `web-ui/dashboard/src/`:

```
src/components/ErrorBoundary.tsx      (definition)
src/lib/poll.survival.test.tsx        (tests ×5)
src/views/RunChainView.tsx:12         import
src/views/RunChainView.tsx:26         <ErrorBoundary resetKey={runId} onRetry={state.reload}>
```

**`ErrorBoundary` is mounted in exactly ONE view.** `app.tsx`'s `renderView()` switch wraps nothing — the file does not import it. So `OverviewView`, `DevicesView`, `EventsView`, `HealthView`, `AutomationsView`, `ExplainHubView`, `RunsView`, and **`WhyNotView`** all render unprotected.

Confirmation the boundary did not engage: `componentDidCatch` logs with the prefix `[render-error] contained by ErrorBoundary:` — **that string is absent from the operator's console paste**, which shows the raw TypeError.

### 6.4 Link 4 — the honesty law that was violated

`ErrorBoundary.tsx`, header comment, verbatim:

> *"FE-LIVE-V112 item 1, evidence-backed (the 2026-07-27 devtools-chain-glance return): an uncontained render throw in the causal-chain view killed the view's polling loop — the "Updated" stamp froze and the application read as hung, turning a cosmetic defect into an apparent outage. **This boundary is therefore LOAD-BEARING, not stylistic (the error-posture law).**"*
>
> *"Honesty rule: this card names WHAT failed — the display, not the request. A fetch failure renders the Resource/ErrorState card ("the request failed, retry"); a render failure renders THIS card. The two are never conflated, and **neither is ever a silent blank or an eternal spinner.**"*

**The July-27 failure mode reproduced verbatim on a sibling surface**, because the fix was applied to the surface where the bug was found and not to the class. That is the exact pattern arc-discipline 25 exists to prevent: *"fixing only the files already open is how occurrence six survives to the suite."*

**And on this product an eternal spinner is not cosmetic — it is a false claim.** "Still working" when nothing is coming.

### 6.5 The counter-exhibit that proves the product can do this right

**At the same moment, on the same build, `Activity`'s 404 rendered a calm, correct, honest error with a retry** (§4.8). The **fetch-failure** path is honest and works (`Resource.tsx` → `ErrorState`). The **render-throw** path is unprotected outside one view. That contrast is the finding in one sentence — and it is a *good* sentence at the READ.

### 6.6 The fix, correctly scoped

**NOT** "add a `?.`". Three rows, all post-freeze:

1. **Mount `ErrorBoundary` in `app.tsx`'s `renderView()`** (or in `AppShell`) so *any* view's render throw degrades to the honest card. Red-first test exists in shape at `poll.survival.test.tsx`.
2. **Correct `contract.ts:350`** to `lastEvaluation: { … } | null` and guard both dereferences in `WhyNotView`.
3. **Corpus sweep (arc-discipline 25):** every FE dereference of a contract-declared-non-nullable field the server can null. Pair each with a fixture proving the null case renders honestly.

---

## §7 — DX-12 in full: the system-liveness honesty gap

**The simultaneous facts, all measured tonight:**

| Surface says | Reality |
|---|---|
| Health: **✓ Live — processing events in real time** | The app holds **no serial port** (§0) |
| Health: **Behind by: nothing — fully caught up** | Log frozen at position **91229** for 40+ minutes |
| Health: **✓ All clear — Nothing needs your attention** | The home has been **unreachable for ~12 hours** |
| Overview: **✓ All running — live and watching your home in real time** | Not watching anything |
| Devices: **Available 5 of 6** | Last report **10:16 AM**, ~14.7 h before this filing |
| Devices: **Stale readings: none** | Every reading is ~14.7 h old |

**The fair reading — and it must be stated, because the hub should adjudicate the real finding, not an inflated one:**

- *"Live / fully caught up / no events stuck"* is **literally true about the projection subsystem.** The projection IS caught up with the log; nothing IS stuck in the DLQ. Those sentences accurately describe what they measure.
- *"Available"* is **defensible by its own published definition** — `OverviewView.tsx:79-81` says so explicitly: *"'Available' is what the system last CONCLUDED from reports, never a live-contact claim,"* and the tile prints *"not a live connection test."*

**The defect is scope, not truthfulness.** The page is titled **"System health — A quick read on whether everything is working."** It presents projection lag and DLQ depth as *system* health while carrying **no liveness signal for the integration/adapter layer** — the layer that actually touches devices. So a dead radio yields a perfect green board, and `Stale readings: none` (DX-21) removes the one indicator that might have leaked the truth.

**This is composed-behavior-under-state-history (arc-discipline 11): every component is correct and the composition misleads.** It is precisely the class the project already knows is a first-class defect class — *"correct components compose invisibly."*

**Why it matters more than any render bug:** the product's differentiator is that it does not claim what it has not measured. Here the system makes a **positive, confident, unprompted claim of wellbeing** while blind. A user reading this board would have no reason to investigate, and their home would be dead.

**What it is NOT:** it is not a false CONFIRM. **The C1 one-way door is untouched** — no action was claimed confirmed that was not (§9.3). This is an observability-layer gap, not a verdict-layer failure. That distinction is load-bearing and should be stated in the same breath as the finding.

---

## §8 — Cross-references to standing state

- **F-0 / G-6 / G-7** (coordinator absent Aug-13 08:17 → Aug-15 16:38; both 3/9 nightlies rig-invalid; excluded from the flake distribution; product record through Aug-13) — **untouched and unchallenged by tonight.** DX-13 is an *additional*, independent finding about hotplug behaviour, not a competing explanation for Aug-14/15.
- **The v53 falsifiable prediction** (Sunday 03:30 returns 7–8/9) — **now materially at risk** unless G-11 fires (§0). If G-11 fires and boot-health passes, the prediction's premise is restored on a *verified* rig rather than an assumed one.
- **C1 / the ~1,728-verdict corpus** — re-verified at the assessments this session: `19 state_confirmed + 1,024 command_confirmation_timed_out + 685 command_result ≈ 1,728, zero false CONFIRM`, counting basis RULED satisfying (Nick's word, v43 beat 3), **8.6× the N≥200 MUST**. The runbook's *"~1,700+"* is accurate and conservative.
  **Standing REC (unchanged from the pre-rehearsal file, DX-E):** only 19 are `state_confirmed`; *"zero false CONFIRMs across ~1,700+ recorded verdicts"* is true but can be misheard as *"1,700 confirmations."* One clause closes it — *"…verdicts of every class, of which the confirmations are one."* Touches D-1's hardened fence, so it is **Nick's call**.
- **F-3** (no `homesynapse` user unit) — corroborated: the app runs as a bare `java` process, `pid 9767`, no systemd unit involved.

---

## §9 — What is PROVEN GOOD (this section is not a courtesy)

### 9.1 The five-modes-distinct verdict rendering works on real bench data — DX-6 resolved

Observed live: **`Sent — no reply`** (mode 1, dispatched-and-timed-out), **`Replaced`** (mode 2, deliberately-superseded, rendered verdict-free with *"That is a change of intent, not a failure"*), **`Accepted, never confirmed`** (mode 3, acked-then-silent, with *"an acceptance is not proof"*). **Zero generic red `Failed` pills anywhere.**

**Proof that the deployed wire carries first-class v1.1.2 `resultOutcome`:** `verdicts.ts`'s `actionVerdict()` can only reach mode 3 (`Accepted, never confirmed`) when `outcome === 'UNCONFIRMED'` **and** `ro === 'unconfirmed'`; `ro` derives from `a.resultOutcome` only when the field is **present**, because the recovery path (`classifyRecordedReason`) fires only on `outcome === 'FAILED'`. An UNCONFIRMED action on a pre-v1.1.2 wire would have rendered `Sent — no reply`. **The label observed is therefore conclusive.** Corroborated by the `▸ Recorded outcome` disclosure rows appearing on exactly the tiles that carry a disposition.

**Consequence: Act 3's narration stands as written. The demo's largest pre-rehearsal risk is dead.**

### 9.2 The frozen v1.1 read-API is fast and correct

`200 OK`, 395 bytes, complete honest payload, **17 ms**, with `ETag` and `X-HomeSynapse-View-Position` present and consistent with the Health board's `Activity position`. **The contract the demo exists to demonstrate performed perfectly.** Every defect tonight is client-side or scope-of-measurement.

### 9.3 The C1 one-way door is INTACT

Nothing found tonight touches the false-CONFIRM clause. Every finding lives in the **observability/reporting** layer. Across fifty-plus runs against a device that has been offline for weeks, **the system has never once claimed that device acted.** The `Accepted, never confirmed` tile is the system explicitly refusing to treat a protocol ACK as proof — the sharpest available form of the thesis, and it is rendering live on real hardware.

### 9.4 Log-token ↔ tile continuity is provable on camera

Every run's ULID decodes to the exact wall-clock time its tile displays:

| Run ULID | Decodes to | Tile reads |
|---|---|---|
| `01KYHPMP0M…` | 2026-07-27 **06:51**:23 CT | *"changed at **6:51 AM**"* |
| `01KYHQ0HN7…` | 2026-07-27 **06:57**:52 CT | *"changed at **6:57 AM**"* |
| `01KYJZKHJG…` | 2026-07-27 **18:47**:17 CT | *"changed at **6:47 PM**"* |
| `01KYDKXJ4T…` | 2026-07-25 **16:46**:50 CT | *"changed at **4:46 PM**"* |
| `01KZSSQHB5…` | 2026-08-11 **20:34**:59 CT | *"changed at **8:34 PM**"* (A1, prior night) |

**The identifier in the URL *is* the timestamp on the tile.** This is a stronger, more falsifiable form of the runbook's continuity line than the scripted version, and it takes ten seconds.

### 9.5 The honest-error path works

The Activity 404 rendered calm, correct, actionable copy. The product refuses to fake data when a surface is unbuilt.

### 9.6 The do-nothing / commands-sent pair renders distinctly

The Aug-11 run (`01KZSSQHB5…`, 20:34 CT, seen at A1 the prior night) renders *"Finished in 34.1s, **but nothing was changed**"* + **⚠ Completed, nothing changed** + *"all 9 planned steps ended without sending a command… the devices this automation targets were unavailable, so each was skipped by design. The step-by-step record of these skips is not kept yet."* The Jul-27 runs render *"Done in 34.1s"* + **✓ Completed** with five per-action verdicts. **Same automation, two honest and visibly different treatments** — the `isDoNothingRun` path working as designed on live data.

---

## §10 — The G1 read-order of record for the gate

**PM proposal. The hub rules; §11 row DX-B.** The runbook's own fallback law governs throughout: *"a broken tile is a ⏺ FINDING narrated honestly, never a mid-demo fix,"* and *"three broken acts = the demo still completes as a FINDINGS record."*

**Pre-flight (before the clock):** tunnel up, token entered, dashboard on Overview. **Do not click Activity at any point** (DX-23).

**Act 1 — "Why did it fire?" (~3 min).** Sidebar **Ask why** → **See recent runs** → open **`01KYHPMP0MMNDHGJJ88D1NA9VD`** (Jul-27 06:51). Walk the chain one hop per sentence: trigger → each action with its verdict. **Skip the condition hop** (DX-24). **Own the naming up front, don't wait to be asked:** *"this run's automation reads 'an earlier automation' because the bench automation is re-provisioned nightly and gets a new identity; the run itself is preserved — the system says so rather than inventing a name. Device identity, by contrast, is durable and proven across restarts."* Then the continuity line, with the decode if you want it: *"the identifier in that URL is the timestamp on that tile — this is a projection of the log, not a story about it."*

**Act 2 — "Why didn't it?" (~3 min). THE SURFACE CHANGES; THE QUESTION DOES NOT.**
Use the **Aug-11 no-change run `01KZSSQHB5…`** (20:34 CT). It delivers a genuine, log-derived no-change explanation — *"all 9 planned steps ended without sending a command… the devices were unavailable, so each was skipped by design. The step-by-step record of these skips is not kept yet"* — which never upgrades or replaces a verdict, and which **is** the no-change class the frozen row names.
**Then narrate the why-not surface's failure as a finding, with the evidence in hand.** *"Our 'why didn't it' page is down. We found it last night. The API answered correctly in seventeen milliseconds with a complete explanation — our dashboard threw on one unguarded null and showed a spinner. We have the exact line. It's a post-freeze fix, and the reason we're telling you rather than routing around it is that this is the whole point of the read."*
**This is a stronger moment than a working page would have been. Do not soften it and do not skip it.**

**Act 3 — "Did it actually confirm?" (~3 min).** On the Act-1 run, walk the pills: **`Replaced`** (intent change, verdict-free), then **`Accepted, never confirmed`** — the centrepiece. *"The device accepted the command and never reported doing it. An acceptance is not proof. The system says so instead of lying. Across roughly 1,700 recorded verdicts of every class on this bench, zero false confirmations."*
**Exhibit 1 moves to the ledger.** State the reason plainly and first, so the amber wall is framed before it is seen: *"the light this automation targets has been offline for weeks — that's why there is nothing confirmed to show you here. It fired fifty times at a dead light and never once claimed it worked. The measured confirmation latencies — 0.16 to 3.65 seconds — are in the nightly record, not on this screen."*
**Disarm the green chip:** ✓ Completed is run-level (the run finished); it is not a claim the devices acted, and every tile below says so.

**Close (~1 min).** `#/overview` → the availability tile's four rows + *"Counts reflect each device's last report — not a live connection test."*
**Then the honest coda — say it yourself:** *"and here is the thing we found last night that we like least: this board will tell you everything is fine while the radio is unplugged. Available is a conclusion from the last report, and nothing marks it stale. That's a real gap between our thesis and our current observability, we found it ourselves under freeze, and it's the first thing in the post-gate program."*

**Elapsed:** comfortably under 10 minutes; the constraint is no longer time.

---

## §11 — Decision rows for the hub / Nick — one-word-rulable

| # | Question | Options | PM REC |
|---|---|---|---|
| **DX-A** | **TIME-CRITICAL (~2.5 h).** Fire G-11 (`bench.sh restart` + one `boot-health`) **before** the 03:30 fire? | **FIRE NOW** · **HOLD** (G-11 stands for Sunday morning as pre-ruled) | **FIRE NOW.** §0. The reversal from the 21:00 REC is owned and the reason is a new measurement, not a change of mind. |
| **DX-B** | Adopt the §10 read-order (Act 2 → the Aug-11 no-change run + narrated why-not failure; exhibit 1 → the ledger; the Close coda)? | **ADOPT** · **AMEND** · **DECLINE** | **ADOPT.** It satisfies the frozen row's three questions on real data, it converts every defect into an owned statement, and it is under budget. |
| **DX-C** | Does G1 still run at the READ at all, given three of four acts carry a defect? | **RUN AS §10** · **RUN AS A FINDINGS RECORD ONLY** · **PULL IT** | **RUN AS §10.** The runbook pre-ruled three-broken-acts as still-completing. Pulling it would remove the strongest available evidence that this operation finds and states its own problems. |
| **DX-D** | Does **DX-12 / DX-13** (the liveness gap) get stated at the READ, or filed silently for post-gate? | **STATE IT** (the §10 coda) · **FILE SILENTLY** | **STATE IT.** A gate that certifies honesty cannot withhold the honesty finding. Stated by us it is evidence of discipline; discovered later it is evidence of the opposite. **This is Nick's call and it interacts with D-1's fence.** |
| **DX-E** | Does the D-1 fence gain the clause distinguishing *verdicts of every class* from *confirmations*? | **ADOPT** · **DECLINE** | **ADOPT** if the fence is still editable. Three seconds against a real mishearing risk. Nick's call — it is his hardened language. |
| **DX-F** | Post-gate priority: does **DX-12/DX-13** enter the semester program at **Tier 1**, ahead of the currently-ranked R-1..R-4 integrity chain? | **TIER 1** · **TIER 2** · **AS-RANKED** | **TIER 1, as a new row.** §12 argues it. The integrity chain hardens what the system *claims about actions*; this gap is what the system *claims about itself*, and it is the one a real household meets first. |

---

## §12 — Post-gate program rows this rehearsal minted

Proposed, not ratified. The HOLD lifts only at the READ's own post-gate word.

| Row | Scope | Why here |
|---|---|---|
| **NEW-1 — Integration-liveness truth** | A liveness signal for the adapter/transport layer, surfaced on Health and Overview; transport loss detected and *reported*, not silent; hotplug re-acquisition of `/dev/ttyUSB0`; `staleAfter` given a real default so `Stale readings` can actually fire. | **DX-12 + DX-13 + DX-21.** The gap between the thesis and the observability layer. Highest-consequence finding of the night; a real-household failure mode with a silent signature. **PM REC: Tier 1.** |
| **NEW-2 — Error-posture enforcement, app-wide** | Mount `ErrorBoundary` above the view switch; red-first test per view; make the eternal-spinner state unreachable by construction. | **DX-15.** A law the codebase already wrote, enforced in one view of nine. Second occurrence of the same incident class. |
| **NEW-3 — Contract-vs-wire nullability sweep** | Correct `contract.ts:350`; guard both `lastEvaluation` sites; **corpus sweep** for every FE dereference of a contract-declared-non-nullable field the wire can null; fixture per site proving the null case renders honestly. | **DX-16**, and arc-discipline 25 by name. |
| **NEW-4 — Automation identity durability** | Decide whether a re-provisioned automation should retain identity across config reload, or whether run→automation association should survive re-minting. | **DX-19.** Today every restart orphans all history. Adjacent to identity claims the company makes; worth ruling deliberately rather than inheriting. |
| **NEW-5 — Nightly ↔ explain-surface coverage** | Determine why nightly scenario runs produce no explain-surface automation runs, and whether they should. | **DX-17 + F-8.** Today the richest evidence stream (the nightly) is invisible on the explainability surface — which is why the demo had no confirmed exhibit. |
| **NEW-6 — Device-detail copy + freshness semantics** | Fix *"last heard from —"* vs *"Last reported: HH:MM"*; add dates to clock-only stamps; settle and document `Updated X ago`. | **DX-20 + DX-22.** Small, cheap, and on the honesty surface. |
| **NEW-7 — Nav hygiene** | `Activity` nav item vs unbuilt `/api/v1/events`. | **DX-23.** |
| **NEW-8 — Harvest → W-SKILLS-3** | (a) A remote session's date banner is UTC; re-derive the operator's local day before any calendar-gated act. (b) A surface never exercised on live data is **unverified**, whatever its tests say — `getNonFiring` had passing tests and a green CI and was broken on the first real payload. | **DX-26 + the DX-14 lesson.** |

**The (b) harvest deserves its own sentence, because it is the most transferable thing tonight produced:** *the mock was the reason the bug existed.* A fixture that always populates a nullable field does not merely fail to catch the defect — it manufactures the false type that causes it. **"Green CI on a surface never touched by a real payload" is a specific, nameable false-confidence class**, and it is worth a rule.

---

## §13 — Limits of this return

1. **Nothing in any repo was written but this file and its pre-rehearsal predecessor.** The freeze held absolutely: no build, deploy, `git` operation, config/constants/YAML edit, scenario invocation, retune, or restart. Every act was a browser read, a DevTools read, or a read-only `/proc` glance.
2. **No token material was requested, received, or recorded.** L3 held end to end.
3. **The full 11-check freshness preflight was NOT run to PASS.** Checks 1/5/6/8/10 and the Check-3 `git log` comparison were not executed; **Check 9 records STALE (mirror unverified from remote)** per the standing caveat — Nick's `diff -rq` remains the instrument of record. **This return is an INPUT, not a gate**, and no forward authoring rides it.
4. **The rehearsal was NOT TIMED** (§4.11).
5. **Four runs were sampled, not fifty.** DX-17's "no CONFIRMED exhibit exists" is a strong inference from four identical samples plus the 19-`state_confirmed` corpus argument — **not an exhaustive proof.** A confirmed action could exist in an unsampled run. *Refutation is cheap and welcome.*
6. **DX-19's mechanism is an inference.** The 03:33:45 timestamp and the orphaned history are facts; nightly re-provisioning as the cause is a strong reading, not a measurement.
7. **DX-22 is unresolved and is declared so.** No mechanism is claimed.
8. **The `/api/v1/entities` capture failed** because DevTools was opened after navigation. Declared.
9. **This session ruled nothing.** Every DX row is a REC. The hub and Nick rule.

**Refutation welcome in both directions.** Load-bearing claims and their refutation paths: `AppShell.tsx:11-18` · `ExplainHubView.tsx` · `format.ts:268,274` · `contract.ts:350` · `WhyNotView.tsx:88` · `verdicts.ts` (`actionVerdict`, the mode-3 branch) · `ErrorBoundary.tsx` (whole) · `app.tsx` `renderView()` · `RunChainView.tsx:26` · `Resource.tsx` · `feedback.tsx:79-86` · `OverviewView.tsx:79-115` · `RunExplanation.java:159-177` · `StandardExplanationService.java:708-727,740-750`.

---

## §14 — Route-back

*Intakes as the next v53 hub beat, ahead of THE READ.*

**Order of business, by deadline:**

1. **DX-A — NOW.** ~2.5 hours to the 03:30 fire. Everything else can wait; this cannot.
2. **DX-B / DX-C / DX-D** — before the READ. They set the demo's shape and its most consequential sentence.
3. **DX-E** — before the READ if the D-1 fence is still open.
4. **The Sunday digest** — adjudicate the v53 falsifiable prediction on arrival, now with the G-11 act (fired or not) as a declared variable in the reading.
5. **DX-F + §12** — post-gate, at the program ratification.

**The bench-evening return supersedes-in-place with Block C now COMPLETE** — this document is that block's ⏺ set, its findings, and its adjudication.

**One closing observation for the record, offered as judgement and refutable as such.** The rehearsal was in doubt: it had been held, its value was questioned, and its own commissioning ruling described it as possibly *"a different act than commissioned."* It ran, and in roughly four hours it found a dead hero surface, a violated error-posture law, a contract-vs-wire divergence, a radio-blind runtime that no board was reporting, and a gap between the product's thesis and its observability layer — **every one of them before the gate rather than during it, and none of them requiring a single line of code to be changed.** Whatever the READ concludes about the product, that is a measurement of the process, and it is a good one.

---

## §15 — ADDENDUM v2: response to the v53 hub's layer-2 audit and rulings

*Filed ~01:20 CT Sun. The hub audited this return at the git objects and by independent decode, confirmed every layer-2-reachable claim, and ruled DX-B ADOPT (adjudicated inside G-9), DX-C RUN AS §10, DX-D REC STATE-IT with a fence analysis, DX-E REC ADOPT, DX-F and §12 held to post-gate ratification with a preliminary shape. **The audit is accepted in full and no ruling is contested.** What follows is what a concurring session owes: the things the rulings did not cover.*

### 15.1 — The prediction matrix is missing a branch, and it is the one that matters most

The matrix gives three branches: (1) G-11 ran / boot-health PASS / fd present, (2) G-11 ran / fd absent post-boot, (3) G-11 did not run. **There is a fourth: G-11 ran, the fd IS present, and `boot-health` comes back RED.**

That is not a variant of Branch 2 — Branch 2 is a *transport-acquisition* failure, which is the already-named class. Branch 4 is the app coming up **with its radio** and still failing its own boot floor: projection, rehydration, or relink. **That would be the first genuine platform alarm of the arc**, and it is the only branch tonight that reaches past the observability layer toward the verdict layer.

**Predicted disposition, filed before the instrument (arc-discipline 21/28):** Branch 4 buys an **evidence read before the READ**, not a retune and not a second restart (arc-discipline 28 — the same leg failing twice under two theories buys a bundle read, never a third theory). The READ still proceeds — honest-red never blocks it, pre-ruled — but D-1's caveat set and the §10 Act-3 framing would both need a same-morning amendment, and NEW-1's scope would no longer be the right home for it. **Probability: low.** The app is demonstrably healthy on every non-radio axis right now (Health `✓ Live`, `Behind by: nothing`, DLQ `All clear`, projection version 5, dashboard serving). But an unnamed branch is how a surprise becomes an improvisation, and this one has 2 hours of runway.

### 15.2 — The G-11 `boot-health` PASS is itself a READ evidence item, not merely a precondition

The matrix treats a passing `boot-health` as the gate on Branch 1's prediction. It is more than that: **a PASS at ~01:15 CT would be the first radio-present positive on the hop-verified documented topology since Aug-13** — banked hours before the digest, on an act the freeze explicitly sanctions, and independent of whether the 03:30 fire is later clean or ambiguous.

**Recommendation: bank it as a named D-2 evidence line in its own right**, not as a footnote to the digest. If the 03:30 fire is for any reason unreadable, the boot-health PASS is still a standing radio-present positive, and the READ should not have to discover that it had one.

### 15.3 — DX-B's frozen-row reading is an INTERPRETATION. It should be stated as one at the READ, not slipped past.

The hub adjudicated: *"(b) names the no-change class as an acceptable form, so the Aug-11 run satisfies it."* **I concur with the ruling and dispute the framing of it as a plain reading.** The row's letter is:

> *"(b) why didn't it — a real **non-firing explanation** including the no-change class (log-derived; the explanation NEVER upgrades or replaces a verdict)"*

Strictly parsed, *"including the no-change class"* qualifies *"non-firing explanation"* — and a **non-firing explanation** is the artifact the `/non-firing` endpoint produces, on the surface that is down. The Aug-11 exhibit is a **run** explanation of an automation that **did** fire and changed nothing. It satisfies (b)'s *substance* exactly — it is log-derived, it is the no-change class by name, it never upgrades a verdict, and it answers the user question (b) exists to serve — while arriving from a different surface than (b)'s canonical one.

**That is a defensible interpretation. It is not a plain reading, and the difference is exactly the kind of thing an adversarial listener finds.**

**Therefore: state it.** One sentence, in Act 2, before the exhibit rather than after the challenge:

> *"The row asks for a non-firing explanation including the no-change class. Our why-not surface is down — I'll show you exactly why in a moment. So here is the no-change class delivered from the run surface instead: same question, same log, same law that an explanation never upgrades a verdict. I'm telling you it's a substitution rather than letting it read as the original."*

**Owned, it is a strength and it costs eight seconds. Unowned, it is the one place in the demo where a sharp listener can say "that isn't what the row asked for" — and be technically right.** This is the single highest-leverage amendment in this addendum.

### 15.4 — §10 refinement: end the coda on the door, not on the gap

DX-D's coda is scripted last, which means the liveness gap would be the final thing the room hears. The admission belongs there — but the demo should not *end* on a defect, and it does not need to in order to stay honest. **Append one sentence to §10's Close, after the gap statement:**

> *"And the reason I can show you that gap without flinching is what sits underneath it: across roughly seventeen hundred recorded verdicts on this bench, this system has never once said a device acted when it hadn't. The layer that makes claims about actions is sound and measured. The layer that makes claims about itself claims more scope than it measures — we found that ourselves, under freeze, and it's now the first row in the post-gate program."*

This satisfies the hub's own stated condition (the coda rides with the C1-intact distinction **in the same breath**) and fixes the ordering so the last impression is the intact door. **No new claim is introduced; the C1 figure is the already-ratified one, and DX-E's clause — if Nick adopts it — lands naturally in this sentence rather than needing a second home.**

### 15.5 — Pre-order hygiene: verify the HIVEMIND porcelain before the beat-1 census issues

The audit reports *"core porcelain shows the freeze held."* **Core is not the repo the beat-1 census is counted in.** The beat-1 order stages 4 in **hivemind** (2 A: both rehearsal files · 2 M: pm-handoff + PROJECT_SNAPSHOT), and that census is only correct on a known baseline.

**The open question:** the v53 prompt lists *"the beat-7 commit transcript → verify at porcelain (law 5)"* as expected first intake **#1** — i.e. at banking, the beat-7 order (stages exactly 6: 2 A + 3 M + 1 R) had **not been run**. If it still has not, then `context/audits/2026-08-15_bench-evening_pre-READ_operator-return.md` is **also still untracked**, the beat-1 census of 4 is short by at least one, and the beat-7 order is a live candidate for either the ghost-commit class or the OVERTAKEN-ORDER form (arc-discipline 33 — one msg file per order, retire-on-overtake).

**Recommendation: run `git --no-optional-locks status --porcelain` in `nexsys-hivemind` and re-derive the census from it before the order issues.** If beat-7 is un-run, the correct shape is almost certainly **one COMBINED beats-7+1 order** with its own message file and the beat-7 message file retired with a stamp — the precedent is the v52 beats-4+5 combination. Cheap to check; expensive to get wrong on gate morning, and a wrong "stages exactly N" clause is the exact failure arc-discipline 29/31 exists to prevent.

### 15.6 — DX-17 is unaffected by tonight's outcome, in either direction

Worth stating so nobody hopes otherwise in the morning: **no branch of the 03:30 matrix puts a `Confirmed` pill on the explain surface.** Even a clean 7–8/9 with a fresh measured ON-latency produces that latency in a *nightly scenario leg*, and nightly legs do not surface as explain-surface automation runs (DX-17 / F-8 / NEW-5 — the surface's run times are 06:51, 06:57, 16:46, 18:47, 20:34, never 03:30). Separately, `bench-hero`'s own target is the offline device (DX-18), so a bench-hero run would not confirm regardless.

**Act 3 exhibit 1 stays on the ledger under every branch.** Its post-gate upgrade path — turning DX-17 from a four-sample inference into an exact answer — is a single query for `state_confirmed` positions against the event store; **fold it into NEW-5** rather than leaving it as a standing layer-1 caveat.

### 15.7 — Two corrections accepted, one of them this session's own

**Accepted: the naming harvest.** This session was dispatched with the hub skill and self-labelled hub-role while functioning as operator support. The hub is right that the **pattern of record for a multi-block operator evening is the H5 navigator packet**, and the dispatch line + role skill are what created the ambiguity. No action, W-SKILLS-3 row.

**And a deviation of this session's own, declared rather than left for someone else to find:** under the navigator pattern the hub is retro-fitting, the law is **read-only plus ONE return write**. This session wrote **two** files — the pre-rehearsal desk return (20:45 CT) and this complete record (01:05 CT), now v2. Both are returns, both are at declared `context/audits/` paths, neither touched any other file in any repo, and the supersession relationship between them is explicit in both frontmatters. **It is nonetheless two writes where the pattern names one**, and the honest form is to say so — the fix, if the pattern is adopted for this class going forward, is that a desk pre-flight and its rehearsal record are one artifact filed once at the end, not two filed as they mature. Small; declared because a return whose deviations are invisible is worth less than one whose deviations are legible.

### 15.8 — What is still owed, and by whom

**Nothing is owed by this session.** Three words are owed by **Nick**, in this order of deadline:

1. **The G-11 evidence** — did it run; `boot-health` verdict verbatim; and the `/proc` fd re-check after the restart *(that third item is what discriminates Branch 1 from Branch 2, and it costs one command)*.
2. **DX-D** — STATE IT / FILE SILENTLY. Hub REC and this session's REC both STATE IT, with §15.4's ordering fix.
3. **DX-E** — ADOPT / DECLINE the D-1 fence clause. If adopted, §15.4 gives it its home.

On those, the hub authors beat 1. **§15.5 should be checked before that order issues.**

---

*End of return. Layer-1 evidence, refutation welcome in both directions. Every capability claim names the instrument that measured it; every source claim names the file and line. The session's own refuted prediction (DX-4) is recorded rather than removed, and the session's own pattern deviation is declared at §15.7. No API token material appears anywhere in this file. Nothing here retro-fails a closed ledger row.*

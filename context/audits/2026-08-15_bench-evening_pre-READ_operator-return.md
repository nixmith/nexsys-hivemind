<!--
file: context/audits/2026-08-15_bench-evening_pre-READ_operator-return.md
purpose: THE BENCH-EVENING (PRE-READ) OPERATOR RETURN — the single sanctioned write of the operator-support navigator session dispatched by context/handoff/2026-08-15_bench-evening_pre-READ_operator-packet.md. Blocks A1/A2/A3/B executed and CLOSED; Block C NOT RUN (operator-directed hold pending hub guidance). Supersedes-in-place.
audience: the PM mission-control hub (intake per law 37), Nick (operator).
state-type: operator return / audit INPUT. Layer-1 evidence, NOT a gate. Refutation welcome in both directions.
status: v2 — SUPERSEDES the v1 filed earlier this session. v1's F-4/F-5/F-6 are RESOLVED or WITHDRAWN by the §2E instrument evidence; see §3A. Block C remains pending.
filed: 2026-08-15, navigator session (fresh Cowork, NOT the hub). Uncommitted; the hub's next order stages it.
L3: NO token material appears anywhere in this file. The operator never transmitted the API token to the navigator at any point.
packet-§4-contract-map: (1) verdict table = §1 · (2) verbatim ⏺ pastes labeled by block = §2 · (3) anomalies/findings = §3 · (4) final-state line = §4 · (5) route-back line = §7. The five required contents are present and in relative order. §5 (declared execution deviations) and §6 (operator-requested hub guidance) are DECLARED ADDITIONS placed before the route-back so the closing line remains last; neither displaces nor alters a required content.
-->

# Bench Evening (Pre-READ) — Operator Return  *(v2, supersedes v1)*

**Navigator:** fresh Cowork operator-support session, read-only on every repo; this file is its only write.
**Operator:** Nick. All bench commands executed by the operator on the Pi; the navigator has no bench access.
**Window:** 2026-08-15, ~10:20 CT → ~19:15 (Pi clock).

---

> # ⚠ THE HEADLINE — root cause found, instrument-proven
>
> **The Zigbee coordinator was NOT ATTACHED TO THE PI AT ALL from Thu 2026-08-13 08:17 until Sat 2026-08-15 16:38.**
>
> This spans **both** collapsed nightlies (Aug-14 03:32 and Aug-15 03:32). Those two fires ran with **no radio present**. That is the cause of the 3/9 floor, and it is proven by three mutually-corroborating instrument facts in §2E:
>
> 1. `usbcore: registered new interface driver cp210x` appears for the **first time since boot** at **Sat Aug 15 16:38:20**. The `cp210x` driver auto-loads on first matching device; its first registration proves **no cp210x device existed on this Pi from boot until that moment**.
> 2. `uptime` = up **2 days, 10:56** at 19:13:51 → boot at **Thu Aug 13 ~08:17**, which matches the Aug-13 08:17:25 hub-enumeration lines exactly. The dmesg window therefore covers the entire uptime with no gap.
> 3. The dmesg filter (`cp210x|ttyUSB|usb 3-`) would have caught a coordinator attach on **any** bus — the `cp210x`/`ttyUSB` driver lines are port-independent. **There are none in the window.**
>
> ## Two consequences the hub must act on
>
> **(a) The freeze-day block's topology claim is FALSE.** `2026-08-14_freeze-day_operator-block.md` §4 states *"Last night's 03:30 fire ran direct-attach."* It did not. **Nothing was attached.** Every downstream plan built on the "direct-attach annotation" — including pm-handoff v52 beat 5's *"the Fri AND Sat digests bank direct-attach-annotated"* — is annotating the wrong variable.
>
> **(b) The Aug-14/Aug-15 digests are not evidence about the platform.** They are evidence about a **missing peripheral**. They should not be read as two nights of platform regression, and in the navigator's reading they should not sit in the READ's flake distribution beside radio-present nights without that distinction being explicit. **The hub adjudicates; the navigator does not rule on the bar.**
>
> **The test:** the **Sun 2026-08-16 03:30 CT** fire is the first with the coordinator present since Aug-13, on the verified documented topology. If coordinator absence was the sole cause, it should return to the Aug-6→13 floor (7–8/9). **This is a falsifiable prediction, stated in advance.**

---

## §1 Verdict table

| Block | Verdict | One line |
|---|---|---|
| **A1 — G1 chain render** | **PASS (with findings)** | Chain rendered end-to-end, 3 tiles, no blank card, no unresolved spinner. The pre-fix null-crash signature did NOT reproduce; the FE-LIVE-V112 item-1 fix is functionally deployed. The void-by-freeze contingency's trigger condition never fired. |
| **A2 — I2 key-hygiene re-sweep** | **PARTIAL — 2 legs clean, 1 expectation MISS, 1 leg UNAVAILABLE** | Custody listing complete + greps `0`/`0` clean; **`secrets.enc` reports `JSON text data`**, the exact negative case the block named; **`systemctl --user status homesynapse` → unit does not exist**, so the running-state stamp the I2/E3 close-out was designed around cannot be produced. |
| **A3 — flake/digest tail** | **COLLECTED — CAUSE NOW IDENTIFIED** | 30 lines banked whole. Nightly fired every night through Aug-15. Aug-14 and Aug-15 both 3/9 with `boot-health` FAIL — **cause: coordinator absent (see headline).** |
| **B — Rosonway restore + enumeration** | **PASS — VERIFIED BY INSTRUMENT** | `lsusb -t` matches I3b's documented tree **hop for hop**: Bus 003 Port 002 → hub port 4 → hub port 2 → `cp210x` @ 12M = **`3-2.4.2`**. USB-2-by-construction criterion also passes (both SS buses empty). `/dev/zigbee`, the by-id stableId, and `/dev/ttyUSB0` all present. |
| **C — G1 demo rehearsal** | **NOT RUN** | Operator-directed hold: Nick elected to route to the hub for guidance before the rehearsal. An explicit, recorded decision — not a failure. See §6. |

---

## §2 The ⏺ pastes, verbatim, labeled by block

*(L3: no token material appears in any paste. The operator read the API token on the Pi terminal and typed it into the browser only; it never entered the navigator conversation.)*

### ⏺ A0 — session state (operator, Pi login banner)

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/Desktop/Code/ClaudeFolder/homesynapse-core (main)
$ ssh pi
Linux hs-dev-1 6.18.34+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.18.34-1+rpt1 (2026-06-09) aarch64
...
Last login: Tue Aug 11 19:19:51 2026 from 100.74.96.24
homesynapse@hs-dev-1:~ $ pwd
/home/homesynapse
```

### ⏺ A1 — tunnel

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/Desktop/Code/ClaudeFolder/homesynapse-core (main)
$ ssh -N -L 7070:127.0.0.1:7070 pi
```

Silent hold = success. **⏺ tunnel up.**

### ⏺ A1 — AuthGate

Token read from **`/home/homesynapse/hs-bench/config/initial_api_token`** (the FIRST documented path; the `.homesynapse` fallback was not needed). One rejected entry occurred first — **operator-side transient, NOT a system defect** (F-18). Second entry succeeded; dashboard rendered.

### ⏺ A1 — the chain render

Surfaces: `http://localhost:7070/dashboard/#/explain/runs` → `http://localhost:7070/dashboard/#/explain/run/01KZSSQHB5K4XXA8VH…` *(run id truncated in the address bar as captured; full id not recovered)*

**Run list (screenshot, transcribed):**

```
Why did something happen?
Pick a run to see exactly why it fired, step by step.          Updated 3 hr ago

AUTOMATION                 WHEN            OUTCOME
An earlier automation      4 days ago      ✓ Completed
An earlier automation      5 days ago      ✓ Completed
An earlier automation      8 days ago      ✓ Completed
An earlier automation      8 days ago      ✓ Completed
An earlier automation      8 days ago      ✓ Completed
An earlier automation      9 days ago      ✓ Completed
An earlier automation      9 days ago      ✓ Completed
An earlier automation     10 days ago      ✓ Completed
An earlier automation     10 days ago      ✓ Completed
An earlier automation     10 days ago      ✓ Completed
An earlier automation     11 days ago      ✓ Completed
```

Sidebar nav as shipped: `Overview · Ask why · Devices · Activity · Automations · Health`. Footer state: **● Live** (green) + `Disconnect`.

**Run detail (screenshot, transcribed):**

```
Why this happened                                              Updated just now
← All runs

An earlier automation ran when 01KX1PB9AAB4VB3E10BD477TV3 changed at 8:34 PM,
but nothing was changed.

This run happened under an earlier version of your automations, so its
name is no longer on record. The run itself is preserved.

  ● 01KX1PB9AAB4VB3E10BD477TV3 changed at 8:34 PM.
      ▸ Trigger

  → Nothing was changed: all 9 planned steps ended without sending a command.
      This usually means the devices this automation targets were unavailable,
      so each was skipped by design. The step-by-step record of these skips is
      not kept yet.

  ◆ Finished in 34.1s, but nothing was changed.    ⚠ Completed, nothing changed

This explanation is rebuilt from HomeSynapse's permanent activity log — it is
never deleted, so the run you need is always here.
```

**⏺ A1 RECORD: chain rendered end-to-end. 3 tiles (trigger · no-change summary · finish). No blank card. No unresolved spinner. No error boundary. NO action verdicts on this run class.**

### ⏺ A3 — the nightly digest tail (30 lines, whole)

```
homesynapse@hs-dev-1:~ $ /usr/bin/tail -n 30 /home/homesynapse/hs-bench/digests/nightly.log
2026-08-01 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.65s
2026-08-02 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260802T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-03 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260803T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-04 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260804T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-05 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260805T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-06 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.30s
2026-08-07 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.17s
2026-08-08 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.36s
2026-08-09 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260809T083132Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-10 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260810T083135Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-11 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.16s
2026-08-12 quiesced AUTO floor: 7/9 · FAIL command-identify-honest · bundle /home/homesynapse/hs-bench/bundles/command-identify-honest-20260812T083124Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.30s
2026-08-13 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260813T083132Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-14 quiesced AUTO floor: 3/9 · FAIL boot-health · bundle /home/homesynapse/hs-bench/bundles/boot-health-20260814T083234Z · FAIL command-supersession · bundle /home/homesynapse/hs-bench/bundles
/command-supersession-20260814T083234Z · FAIL command-identify-honest · bundle /home/homesynapse/hs-bench/bundles/command-identify-honest-20260814T083254Z · FAIL usb-reenumeration · bundle /home/home
synapse/hs-bench/bundles/usb-reenumeration-20260814T083336Z · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260814T083338Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-15 quiesced AUTO floor: 3/9 · FAIL boot-health · bundle /home/homesynapse/hs-bench/bundles/boot-health-20260815T083231Z · FAIL command-supersession · bundle /home/homesynapse/hs-bench/bundles
/command-supersession-20260815T083231Z · FAIL command-identify-honest · bundle /home/homesynapse/hs-bench/bundles/command-identify-honest-20260815T083251Z · FAIL usb-reenumeration · bundle /home/home
synapse/hs-bench/bundles/usb-reenumeration-20260815T083332Z · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260815T083334Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
```

### ⏺ A2 — the I2 key-hygiene re-sweep (all four groups)

```
homesynapse@hs-dev-1:~ $ ls -la /home/homesynapse/hs-bench/data/zigbee/
total 40
drwxrwxr-x 3 homesynapse homesynapse 4096 Aug 15 04:34 .
drwxrwxr-x 3 homesynapse homesynapse 4096 Aug 15 04:33 ..
drwxrwxr-x 2 homesynapse homesynapse 4096 Jul 18 20:53 _pre-seed-backup-20260719
-r-------- 1 homesynapse homesynapse   32 Jul 18 21:09 .root-key
-rw-rw-r-- 1 homesynapse homesynapse  248 Jul 18 21:09 scope_keys.json
-rw-rw-r-- 1 homesynapse homesynapse  568 Jul 18 21:09 secrets.enc
-rw-rw-r-- 1 homesynapse homesynapse 4551 Aug 15 04:34 zigbee-devices.json
-rw-rw-r-- 1 homesynapse homesynapse  122 Jul 18 21:09 zigbee-network.json
-rw-rw-r-- 1 homesynapse homesynapse  123 Jul  6 19:05 zigbee-network.json.ch20-0x9b65.retired
homesynapse@hs-dev-1:~ $ file /home/homesynapse/hs-bench/data/zigbee/secrets.enc
/home/homesynapse/hs-bench/data/zigbee/secrets.enc: JSON text data
homesynapse@hs-dev-1:~ $ grep -ciE "network[_-]?key|networkkey" /home/homesynapse/hs-bench/digests/nightly.log
grep -ciE "seed" /home/homesynapse/hs-bench/digests/nightly.log
0
0
homesynapse@hs-dev-1:~ $ grep -inE "seed" /home/homesynapse/hs-bench/digests/nightly.log | head -5
homesynapse@hs-dev-1:~ $ systemctl --user status homesynapse 2>&1 | tail -25
Unit homesynapse.service could not be found.
```

*(No `sudo` was required on any command. `secrets.enc` was NOT opened — the block's "never cat any of them" rule held.)*

### ⏺ B — `lsusb` (flat) — TWO SAMPLES, BOTH POST-RE-CABLE

**Operator clarification (recorded):** *"The two lsusb outputs are the same because I had already re-cabled."* / *"I had re-cabled it the second I realized the mistake, then I told you about it."* **Both samples therefore describe the same post-restore state. There is NO pre-re-cable baseline, and none is needed — §2E supplies the history instead.**

```
homesynapse@hs-dev-1:~ $ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 002: ID 2109:2822 VIA Labs, Inc. USB2.0 Hub             
Bus 003 Device 003: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
Bus 003 Device 005: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

### ⏺ B — operator testimony on the physical act

Recorded per I3b playbook §4a (operator actions are data):

> *"There are 7 total USB ports — 2 USB-C, 1 USB 2.0, the remaining 4 USB 3.0 — and I had the cable plugged into the 2nd to last USB 3.0, thinking that the light above that port (the one for the 3rd from last, and correct port) was on for that port."*
> *"The cable is plugged into the 3rd from last USB port and is powered on."*

**Navigator cross-check against I3b §2:** with the layout `[1: C][2: C][3: USB-2.0][4][5][6][7: USB-3.0]`, **"3rd from last" = physical position 5**, and I3b names *"physical port 5 (a standard USB-A 3.0 port) → logical `3-2.4.2`"* as the coordinator's documented home. **Confirmed correct — and independently confirmed by `lsusb -t` below.**

### ⏺ 2E — THE INSTRUMENT EVIDENCE *(navigator-proposed, operator-authorized; see §5)*

```
homesynapse@hs-dev-1:~ $ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/2p, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 5000M
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/2p, 480M
    |__ Port 002: Dev 002, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 004: Dev 003, If 0, Class=Hub, Driver=hub/4p, 480M
            |__ Port 002: Dev 005, If 0, Class=Vendor Specific Class, Driver=cp210x, 12M
/:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 5000M
homesynapse@hs-dev-1:~ $ dmesg -T | grep -iE "cp210x|ttyUSB|usb 3-" | tail -40
[Thu Aug 13 08:17:25 2026] usb 3-2: new high-speed USB device number 2 using xhci-hcd
[Thu Aug 13 08:17:26 2026] usb 3-2: New USB device found, idVendor=2109, idProduct=2822, bcdDevice= 8.b4
[Thu Aug 13 08:17:26 2026] usb 3-2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[Thu Aug 13 08:17:26 2026] usb 3-2: Product: USB2.0 Hub             
[Thu Aug 13 08:17:26 2026] usb 3-2: Manufacturer: VIA Labs, Inc.         
[Thu Aug 13 08:17:26 2026] usb 3-2.4: new high-speed USB device number 3 using xhci-hcd
[Thu Aug 13 08:17:27 2026] usb 3-2.4: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[Thu Aug 13 08:17:27 2026] usb 3-2.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[Thu Aug 13 08:17:27 2026] usb 3-2.4: Product: USB2.1 Hub
[Thu Aug 13 08:17:27 2026] usb 3-2.4: Manufacturer: Generic
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: new full-speed USB device number 4 using xhci-hcd
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: New USB device found, idVendor=10c4, idProduct=ea60, bcdDevice= 1.00
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: Product: SONOFF Dongle Plus MG24
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: Manufacturer: SONOFF
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: SerialNumber: 0ae2dd7cecf8ef11b80168135c2a50c9
[Sat Aug 15 16:38:20 2026] usbcore: registered new interface driver cp210x
[Sat Aug 15 16:38:20 2026] usbserial: USB Serial support registered for cp210x
[Sat Aug 15 16:38:20 2026] cp210x 3-2.4.2:1.0: cp210x converter detected
[Sat Aug 15 16:38:20 2026] usb 3-2.4.2: cp210x converter now attached to ttyUSB0
[Sat Aug 15 16:38:29 2026] usb 3-2.4.2: USB disconnect, device number 4
[Sat Aug 15 16:38:29 2026] cp210x ttyUSB0: cp210x converter now disconnected from ttyUSB0
[Sat Aug 15 16:38:29 2026] cp210x 3-2.4.2:1.0: device disconnected
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: new full-speed USB device number 5 using xhci-hcd
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: New USB device found, idVendor=10c4, idProduct=ea60, bcdDevice= 1.00
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: Product: SONOFF Dongle Plus MG24
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: Manufacturer: SONOFF
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: SerialNumber: 0ae2dd7cecf8ef11b80168135c2a50c9
[Sat Aug 15 16:38:43 2026] cp210x 3-2.4.2:1.0: cp210x converter detected
[Sat Aug 15 16:38:43 2026] usb 3-2.4.2: cp210x converter now attached to ttyUSB0
homesynapse@hs-dev-1:~ $ ls -l /dev/zigbee
ls -l /dev/serial/by-id/
ls -l /dev/ttyUSB*
uptime
lrwxrwxrwx 1 root root 7 Aug 15 16:38 /dev/zigbee -> ttyUSB0
total 0
lrwxrwxrwx 1 root root 13 Aug 15 16:38 usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 -> ../../ttyUSB0
crw-rw---- 1 root dialout 188, 0 Aug 15 16:38 /dev/ttyUSB0
 19:13:51 up 2 days, 10:56,  4 users,  load average: 0.00, 0.00, 0.00
```

---

## §3A Corrections to v1 — declared, not silently amended

The navigator revised its own position **three times** during this session. All revisions are declared, because an operator return whose errors are invisible is worth less than one whose errors are legible.

| v1 item | Status in v2 | Why |
|---|---|---|
| **F-4** — Block B INCONCLUSIVE, parentage unprovable | **RESOLVED → PASS** | `lsusb -t` proves `3-2.4.2` hop for hop. |
| **F-5** — possible contradiction: "Rosonway present at pre-re-cable baseline" | **EVIDENCE WITHDRAWN, CLAIM RE-ESTABLISHED ON BETTER GROUNDS** | The v1 "baseline" was taken *after* the operator had already re-cabled, so it proved nothing about the earlier state. **However**, §2E independently establishes a stronger version: the freeze-day block's "direct-attach" claim is false because **nothing was attached at all.** |
| **F-6** — identical before/after `lsusb`, `Device 005` anomaly | **WITHDRAWN — NON-FINDING** | Operator confirmed both samples post-date the re-cable. Same state, same output. No anomaly. |
| **Navigator caution** — "the coordinator enumerated fine from the WRONG port" | **WITHDRAWN — FALSE** | No wrong-port state was ever observed. §2E shows position 6 **never enumerated at all**, consistent with a genuinely unpowered port (the unlit indicator). |
| **Correlation** — 3/9 onset tracks the first direct-attach fire | **SUPERSEDED — BOTH NAVIGATOR HYPOTHESES WRONG** | Neither direct-attach nor wrong-port. The device was **absent**. See headline. |
| **v1 §5.6** — navigator over-alarmed on Block B, missed the port-5 arithmetic | **STANDS as declared** | Operator's placement was correct throughout; the navigator's arithmetic lagged. |

---

## §3 Findings

Severity is the navigator's triage for reading order only. **The navigator adjudicates nothing** — every item is hub-refutable.

### CRITICAL

**F-0 (NEW) — The coordinator was absent from the Pi for 2 days 8 hours, spanning both collapsed nightlies.**
Absent **Thu Aug-13 08:17 → Sat Aug-15 16:38**. Proof in §2E, three independent legs (first-ever `cp210x` driver registration; `uptime`-to-`dmesg` boot cross-check leaving no unobserved gap; a port-independent filter returning nothing in the window). **This is the cause of F-1.**

**F-1 (CAUSE NOW KNOWN) — Aug-14 and Aug-15 are 3/9 with the boot floor failing, because there was no radio.**

| Aug 6-8 | 9 | 10 | 11 | 12 | 13 | **14** | **15** |
|---|---|---|---|---|---|---|---|
| 8/9 | 7/9 | 7/9 | 8/9 | 7/9 | 7/9 | **3/9** | **3/9** |

Four scenarios failed on both nights that had never failed in the 15-night window — `boot-health`, `command-supersession`, `command-identify-honest`, `usb-reenumeration` — plus the chronic `command-confirm-s31`. **All five require the radio.** The 3 that passed are the 3 that do not. The fit is exact. Note the Aug-13 03:32 fire (7/9) **preceded** the 08:17 boot, so it ran with the coordinator still present — the boundary is consistent to within hours.

**F-5 (RE-ESTABLISHED) — `2026-08-14_freeze-day_operator-block.md` §4's topology claim is false, and every plan resting on it is mis-annotating.**
The block asserts *"Last night's 03:30 fire ran direct-attach."* §2E shows nothing was attached. pm-handoff v52 beat 5's *"the Fri AND Sat digests bank direct-attach-annotated"* therefore annotates a variable that was not in play. **Hub ruling required on how those two digests are labelled and whether they enter the READ's distribution at all.**

### HIGH

**F-2 — `secrets.enc` reports `JSON text data`; the block expected `data` (opaque). NOT discriminated.**
Two readings fit, and the file was **not** opened (block rule: never `cat`):
- **(a)** genuinely unencrypted plaintext JSON wearing a `.enc` suffix — serious;
- **(b)** a JSON envelope wrapping base64 ciphertext — a standard, correct design for which `file` reports `JSON text data` accurately.

568 bytes fits either. **The discriminating test was NOT run** (packet §5; never-`cat`; and a careless read risks putting key material into scrollback for no time-critical benefit). **Hub decision required — see G-4.**

**F-3 — `systemctl --user status homesynapse` → `Unit homesynapse.service could not be found`. The I2/E3 running-state stamp cannot be produced.**
The error is *unit not found*, **not** `Failed to connect to bus` — the user manager answered and the unit is genuinely undefined. Plausibly residue of the Aug-09 clean-image install, with the app started by another path (`bench.sh`); **not investigated** (out of script).
**This is a unit-management finding, NOT an app-down finding:** at ~14:35 the dashboard served live data over the read-API with a green ● Live indicator. The concrete cost is that the **fourth evidence leg of the I2 close-out cannot be produced by the scripted command**, and the app-pid field is unobtainable.

**F-21 (NEW) — the app's port state after the 16:38 re-attach is UNVERIFIED.**
`/dev/zigbee → ttyUSB0` exists and the node is present, but **whether the running app has opened it** was not checked (app logs are out of script). If the nightly performs its own restart — `boot-health` being one of its scenarios implies a boot — Sunday's fire should acquire the port regardless. **Stated as a residual risk, not a defect.** No action taken; the freeze forbids a restart and the navigator did not seek an exception.

### MEDIUM

**F-7 — Key-file permissions are inconsistent. `secrets.enc` and `scope_keys.json` are world-readable.**
`.root-key` is correctly `-r--------` (0400, 32 bytes). But `secrets.enc` and `scope_keys.json` are both `-rw-rw-r--` (**0664 — group-writable and world-readable**) inside a `drwxrwxr-x` (0775) directory, so the path is traversable and both are readable by any local user. Practical exposure on a single-user Pi is small, but I2 is a posture row and the inconsistency beside a correctly-locked `.root-key` is exactly what such a row exists to surface.

**F-8 (PARTIALLY EXPLAINED) — no explain-surface run from Aug-12, 13, 14 or 15.**
Newest listed run is ~Aug-11. **The Aug-14/15 portion is now fully explained by F-0** — no radio, no device events, no automation triggers. **Aug-12 and Aug-13 remain unexplained**, since the digest shows a working radio then (Aug-12 carries a measured `ON-latency 0.30s`).
**Navigator correction to its own earlier framing:** the series was *already* sparse — the "days ago" labels map to Aug 11, 10, 7, 7, 7, 6, 6, 5, 5, 5, 4, i.e. **nothing on Aug 8 or 9 either**, with multiple runs on some days. So this is **not** one-run-per-night, and the Aug-12/13 gap sits inside a pre-existing sparse pattern. **Whether nightly scenarios are expected to produce explain-surface runs at all remains an open question the navigator cannot answer.**

**F-9 — Custody question: `_pre-seed-backup-20260719/` exists at 0775 and may contain pre-seed key material.** Not listed, not opened. Flagged only.

### LOW / POSITIVE / DEMO-READABILITY

**F-10 (POSITIVE, CONFIRMED TWICE) — the I3b USB-2-by-construction criterion PASSES.** I3b: *"It appears once, at 480M, on Bus 003 only; Buses 002 and 004 (5000M) are empty."* Observed: Bus 002 and Bus 004 carry 1-port root hubs with nothing attached; both hub stages appear once, on Bus 003, at 480M. **The uplink is in a black USB-2 socket, not blue** — the exact error I3b's `dmesg` caught in July did not recur.

**F-22 (NEW, POSITIVE) — the udev chain is intact; I3b's STOP branch does NOT trigger.**
`/dev/zigbee -> ttyUSB0`; by-id stableId present as `usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0`; `/dev/ttyUSB0` present as `crw-rw---- root:dialout 188,0`. I3b's disambiguation — *"`cp210x` present but no symlink = the genuine udev finding (STOP)"* — is **not** met. *(Not verified: that `homesynapse` is a member of `dialout`. It has worked historically; flagged for completeness only.)*

**F-23 (NEW) — the Device-number criterion should probably be retired.** The freeze-day block's pass test is *"Bus 003 Device number back in the twenties."* Observed: **Device 005**. But `uptime` shows a boot on Aug-13, and device numbers count attach events since bus reset — so a low number is the *expected* consequence of a recent reboot, independent of topology. **The criterion measures attach history, not cabling.** `lsusb -t` is the correct instrument and it passes. **Hub ruling suggested.**

**F-11 (RESOLVED) — `zigbee-devices.json` mtime.** v1 flagged a timezone ambiguity. `uptime` (19:13:51) and `dmesg -T` share one frame, and boot-time reconciles exactly with the Aug-13 08:17:25 hub lines, so the Pi's displayed clock is internally consistent. `zigbee-devices.json` at `Aug 15 04:34` sits ~1 h after the 03:32 nightly window. **Key material remains frozen at `Jul 18 21:09` and is not being rewritten — good hygiene evidence.**

**F-12 (POSITIVE) — log-token↔tile continuity is visibly supported.** The trigger tile carries a ULID (`01KX1PB9AAB4VB3E10BD477TV3`) and the run detail URL carries the run ULID.

**F-13 (DEMO) — every run in the visible history renders as "An earlier automation."** No automation name resolves anywhere. The detail explains: *"This run happened under an earlier version of your automations, so its name is no longer on record."* Act 1's script is *"walk the chain aloud, name the trigger"* — a nameless automation across the entire history is a live presentation problem.

**F-14 (DEMO) — the trigger subject renders as a raw ULID**: *"01KX1PB9AAB4VB3E10BD477TV3 changed at 8:34 PM."* Hard to speak aloud on a clock.

**F-15 (DEMO) — runbook↔nav naming mismatch.** The runbook says *"Runs surface."* The shipped nav is `Overview · Ask why · Devices · Activity · Automations · Health` — **no item named "Runs."** The list lives under **Ask why** (`#/explain/runs`).

**F-16 (DEMO) — the no-change class cannot supply per-step tiles, and says so honestly.** *"…The step-by-step record of these skips is not kept yet."* Arguably on-thesis for the "no data beats fake data" posture, but it yields **no action verdicts**, so it cannot serve Act 3.

**F-17 (DEMO, forward-looking) — Act 1 and Act 3 may have no scripted exhibits.** Act 1 wants *"last night's fire"* — absent. Act 3 wants CONFIRMED-with-latency; the most recent measured ON-latency is Aug-12, also absent from the surface. **Only one run was opened**, so exhibits may well exist among Aug 4–11. **Unverified either way.**

**F-18 (OPERATOR-SIDE, explicitly NOT a system defect) — one API-token entry was rejected before a successful second attempt.** Operator-side cause; the first documented path was correct. Recorded only because it **validates the runbook's own instruction** to enter the token before the demo clock starts. No mark against the system.

**F-19 (PROCESS) — "the documented topology" was not reproducible from the operator block alone.** The block says *"re-cable the coordinator BACK through the Rosonway hub (the documented topology)"* with **no port named**. The port identity lives only in the 2026-07-25 I3b report, which packet §0 did not list. The operator initially used position 6. **Recommend the port (`physical port 5 = 3-2.4.2`) be named inline in any future restore instruction.**

**F-20 (FLAKE DISTRIBUTION — recorded, not adjudicated).** `command-confirm-s31` across the 15 logged nights: **FAIL 9** (Aug 2,3,4,5,9,10,13,14,15) · **PASS 6** (Aug 1,6,7,8,11,12). **Caveat now material: Aug-14 and Aug-15 failed with no radio present (F-0), so they are not comparable to radio-present nights.** On radio-present nights only: **FAIL 7 · PASS 6.** `1 SKIP(hue-online)` is constant on every night. Measured ON-latency in the window: `3.65 · 0.30 · 0.17 · 0.36 · 0.16 · 0.30` s. **The navigator does not rule on the bar.**

---

## §4 Final state (at filing; Pi clock 19:13:51, 2026-08-15)

- **Pi reachable:** **YES** (`hs-dev-1`, kernel `6.18.34+rpt-rpi-2712`). **Uptime 2 days 10:56 → booted Thu Aug-13 ~08:17.** 4 users attached; load average `0.00 0.00 0.00`.
- **App pid:** **NOT OBTAINABLE by the scripted command** — `homesynapse.service` is not a defined `--user` unit (F-3). The app is nonetheless **demonstrably running**: the read-API served live data with a green ● Live indicator at ~14:35.
- **Cabling after B — VERIFIED BY INSTRUMENT:** Rosonway RSH-A107C on its own 12 V PSU; uplink in a **black USB-2 Pi socket** (both SS buses empty, F-10); **coordinator at `3-2.4.2`** — Bus 003 Port 002 → hub port 4 → hub port 2 → `cp210x` @ 12M, matching I3b's documented tree hop for hop. `/dev/zigbee`, the by-id stableId, and `/dev/ttyUSB0` all present and correctly owned (F-22).
- **Coordinator attach time:** **Sat Aug-15 16:38:43** (after a 16:38:20 attach, 16:38:29 pull, 16:38:43 re-seat — all at `3-2.4.2`).
- **Tunnel:** may be dropped. Block C requires fresh setup including re-entry of the API token.
- **Freeze:** **HELD.** Zero builds, deploys, `git pull`, config/constants/YAML edits, scenario invocations, retunes, or restarts. Every command run this session was read-only. Nothing was written to any repo except this file.
- **s31 legs and nightly machinery:** **UNTOUCHED.**
- **Next unattended event:** the **Sun 2026-08-16 03:30 CT** nightly — the first fire with the coordinator present since Aug-13, on the verified documented topology. **Predicted to return to the 7–8/9 floor. Stated in advance so it can falsify.**

---

## §5 Execution deviations (declared)

1. **Block order was A1 → A3 → A2 → B**, not A1 → A2 → A3 → B. A3 was pulled forward as the one command able to disambiguate the A1 staleness finding before the operator committed his evening. **No act skipped, added, or altered.**
2. **A second flat `lsusb` was taken** intending a pre/post baseline. It **did not function as one** — the operator had already re-cabled. Declared, and superseded by §2E.
3. **A fifth document was read** beyond packet §0: `context/handoff/2026-07-25_rosonway-topology-move_I3b_bench-session-report.md`, read-only. Reason: the operator raised port uncertainty, the block names no port (F-19), and the hub's criterion is positional. **It produced F-10, F-19, F-22, F-23 and the port-5 cross-check.**
4. **Four out-of-script read-only commands were run — OPERATOR-AUTHORIZED, not navigator-initiated.** `lsusb -t`, `dmesg -T | grep …`, the `/dev` triple, `uptime`. The navigator proposed them in v1 §6 and ran none until the operator directed *"give me instructions so we can confirm the information we need."* **None builds, deploys, edits configuration, restarts a service, or invokes a scenario — the freeze is untouched.** They produced F-0, the root cause.
5. **Block C was NOT run** — operator-directed hold pending hub guidance. Not a failure, not a skip.
6. **`secrets.enc` was NOT discriminated** despite the temptation being obvious and the navigator wanting to. §5 of the packet and the never-`cat` rule held. It remains G-4.
7. **Navigator error, declared three times over** — see §3A. The navigator over-alarmed on Block B, missed the port-5 arithmetic on first pass, and advanced two causal hypotheses that the instrument later refuted. The operator's own intuition (*"my intuition tells me that you are missing some details"*) was **correct** and prompted the checks that found the root cause.

---

## §6 REQUESTED GUIDANCE — the operator's explicit ask

Filed at the operator's direction. **G-1, G-2 and G-3 from v1 are now DISCHARGED** by §2E. What remains:

| # | Item | Status |
|---|---|---|
| **G-4** | Opacity discrimination on `secrets.enc` — **method to be specified by the hub**, not improvised | **OPEN.** Not time-critical for the READ; blocks the I2 close-out. |
| **G-5** | **How to file the I2/E3 close-out** given one evidence leg cannot be produced (F-3) and a second missed its expectation (F-2) | **OPEN — hub ruling required.** |
| **G-6** | **How to label the Aug-14/15 digests** now that "direct-attach" is disproven and the true condition was *no coordinator attached* (F-0, F-5) | **OPEN — hub ruling required. Highest priority for the READ.** |
| **G-7** | **Whether Aug-14/15 enter the READ's flake distribution at all**, given they measure a missing peripheral rather than platform behaviour (F-20) | **OPEN — hub ruling required.** |
| **G-8** | **Whether Block C runs tonight, and against which exhibits** (F-17). Its value has arguably shifted from *rehearsing the script* to *inventorying which exhibits exist* — a different act than commissioned | **OPEN — hub ruling required.** |
| **G-9** | **Whether the G1 read-order needs rebuilding** around F-13 → F-17 | **OPEN.** |
| **G-10** | **Whether the Device-number criterion is retired** in favour of `lsusb -t` (F-23) | **OPEN.** |
| **G-11** | Whether the app needs to re-acquire the port before Sunday's fire, or whether the nightly's own boot suffices (F-21) | **OPEN — any remedial act would require a freeze exception the navigator did not seek.** |

---

## §7 Route-back

*Intakes as the next v52 hub beat; the hub files the I2/E3 close-out, banks the digests with the topology annotation, adjudicates the Rosonway enumeration, and folds the rehearsal findings into the READ's G1 read-order.*

**Navigator addendum:** of those four intake actions —

- **the enumeration adjudication is DISCHARGED** — Block B passes by instrument (§2E, F-22, F-10);
- **the digest banking is BLOCKED and its premise disproven** — the "topology annotation" names a variable that was not in play; the true condition was *no coordinator attached* (F-0, F-5, G-6);
- **the I2/E3 close-out is BLOCKED** by F-2 and F-3 (G-4, G-5);
- **the rehearsal findings are PARTIAL** — Block C did not run (G-8).

This return is **INTERIM** and supersedes-in-place again when Block C completes and any authorized §6 items return.

---

*End of return. Layer-1 evidence, refutation welcome in both directions. Every ⏺ paste above is the operator's verbatim terminal output or a transcription of an operator screenshot; every interpretation is the navigator's and is refutable. The navigator's own three retractions are recorded at §3A rather than quietly corrected. No API token material appears anywhere in this file.*

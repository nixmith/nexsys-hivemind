<!--
file: context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md
purpose: The H3 clean-image fresh-install rep — operator-support RETURN. Supersedes-in-place (law 37).
status: ✅ COMPLETE. Phases 0–6 executed. Bench restored and verified. 12 findings, two CRITICAL/HIGH
        that no prior gate could have surfaced. Filed 2026-08-13.
governing: 2026-08-09 operator packet + 2026-08-11 Stage-2 dispatch addendum (addendum wins).
companions: context/handoff/2026-08-13_H3-stage2_hub-decision-brief.md   (adjudication)
            context/handoff/2026-08-13_H3-stage2_fresh-session-context-pack.md (successor lane)
-->

# H3 Stage 2 — clean-image fresh-install rep · OPERATOR RETURN

## 0. Verdict

| | |
|---|---|
| **H3 MUST row** | **SATISFIED on real hardware.** Documented install ran as written → healthy boot → health probe green → RUNNING + token + auth enforced |
| **Bench** | **RESTORED and verified.** App running, radio up, 6 entities, nightly re-armed Fri 04:30 EDT |
| **Fences** | All held. Coordinator out for the whole rep; read-only throughout; no fix applied to anything |
| **Findings** | **12** (F-13 … F-24) + F-9 converted to a measurement |
| **Highest-severity** | **F-23 (CRITICAL)** — the packaged runtime cannot run *any* integration, and the gate's assert set structurally cannot see it |

**The rep did what a rep is for.** It passed its stated criterion *and* found a defect that CI, by
construction, could never have caught — because the defect lives precisely in the gap between
"the service is up and authenticated" and "the system does its job."

## 1. The criterion, measured

| Assert | Evidence |
|---|---|
| Install AS WRITTEN | `sudo apt install -y ./homesynapse_0.1.0+gd26777c_arm64.deb` → **exit 0**, **9 s** (07:35:32→07:35:41 EDT), `HomeSynapse Core is running.` |
| Health probe green | `ExecStartPost=…/health-probe.sh --wait --timeout 90` → `status=0/SUCCESS`; `[health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities` |
| Service RUNNING | `is-active=active` · `is-enabled=enabled` · `SubState=running` · `Result=success` · `NRestarts=0` · `ExecMainStatus=0` · MainPID 2542 |
| Token at printed path | `-rw-r--r-- homesynapse:homesynapse 44 B /var/lib/homesynapse/config/initial_api_token`; `/usr/bin/homesynapse-token` rc=0 |
| Auth enforced | unauthenticated **401** · valid token **200** · **deliberately wrong token 403** (negative control — correctly separates *no credential* from *bad credential*) |
| Loopback-only | `ss` → `[::ffff:127.0.0.1]:7070`, no `0.0.0.0` bind |
| **Cold-boot (extra)** | After `reboot`, nobody logged in: `active`/`enabled` at 07:47:12 EDT, health probe 0, 401/200 |
| **Least-privilege** | `homesynapse:x:102:105:HomeSynapse Core:/var/lib/homesynapse:/usr/sbin/nologin` — uid 102, nologin, home = data dir. `/var/lib` 0700 · `/var/log` 0750 · `/etc` 0750 root:homesynapse |
| Artifact traceability | sha256 `5b1382…c575` verified **three times** (desktop, on-Pi pre-install, build summary); commit `d26777c`, clean tree; `MANIFEST.sha256 -c` → all OK |

## 2. Timings

| Mark | Value |
|---|---|
| Flash end | 2026-08-12 21:12:34 CDT *(file mtimes **and** cloud-init instance id `rpi-imager-1786587154260`, two independent sources)* |
| Fresh-image first boot | 2026-08-13 ~07:13 EDT; boot 1.808 s kernel + 26.702 s userspace |
| **Install** | **9 s**, exit 0 |
| Health green | 2026-08-13 07:35:41 EDT ← **the H3 evidence moment** |
| Cold-boot service up | 07:47:12 EDT; boot 1.291 s + 18.336 s |
| Clean stop | 0 s (graceful shutdown complete, WAL checkpointed) |
| Warm restart | 2 s incl. the health gate |
| Bench restored | 06:58 CDT; radio up 16 s after `bench.sh start` |
| Margin at completion | ~20 h to the Fri 04:30 EDT nightly |

## 3. Findings

**Numbering is RECONCILED.** The Stage-1 register ends at **F-12**; Stage 2 therefore continues at
**F-13**. Cross-stage relationships are mapped in §9.

### 3.1 CRITICAL

**F-23 — the packaged runtime cannot run any integration, and the gate cannot see it.**

*Symptom (hs-fresh journal, 07:35:41):*
```
integration.launched: integration_type=zigbee io_type=SERIAL
integration.start_failed … boot continues (INV-RF-01)
java.lang.NoClassDefFoundError: jdk/jfr/Event
   at StandardIntegrationSupervisor.publishLifecycle(:1099)
   at StandardIntegrationSupervisor.publishStarted(:1065)      ← the SUCCESS path
Exception in thread "integration-zigbee-0" java.lang.NoClassDefFoundError: jdk/jfr/Event
   at publishLifecycle(:1099) at markFailed(:851)              ← the FAILURE path
Caused by: java.lang.ClassNotFoundException: jdk.jfr.Event
```
Six occurrences per boot.

*Proof at the artifact:* `/opt/homesynapse/runtime/release` lists **15** modules; `jdk.jfr` is not
among them. `runtime/bin/java --list-modules | grep jfr` → absent.

*Root cause — `distribution/image/build-image.sh`. **The code diverges from its own stated design.***

- **`:75-76` — the comment specifies the algorithm:** *"Determine the java.\* modules the app actually
  needs. **jdeps on the full jar set gives the closure**; we union with a known-good floor so the image
  never under-links (some modules are reached reflectively and jdeps cannot see them)."*
- **`:79-83` — the code does not implement it.** jdeps is handed **exactly one jar**
  (`$(find "${IMAGE}/lib" -name 'homesynapse-app*.jar' | head -1)`). `--class-path` tells jdeps where
  to *resolve* classes, not which to *analyse*. The app runs a classpath of ~18 first-party jars, so
  any JDK module used only by a non-app jar is invisible to the computation. `jdk.jfr.Event` is used by
  `integration-runtime` — a different jar. `--ignore-missing-deps` suppresses the complaint.
- **`:85` — the safety net was correctly conceived and incompletely enumerated.** `FLOOR` exists
  precisely to catch what jdeps misses; it does not list `jdk.jfr`.

**This is the sharpest available statement of the defect, and it is stronger than "the FLOOR was
incomplete."** Line 76 promises a full-jar-set closure. Line 82 computes a one-jar closure. The
`FLOOR` was the second line of defence for reflective use — it was never meant to be the *only*
defence against a whole category of first-party jars going unanalysed. Both layers had to fail, and
the first failed silently by not doing what its own comment says it does.

*(This framing is the hub's, arrived at independently on review, and it is better than the one this
return originally carried. Recorded as a correction rather than absorbed silently.)*

*Blast radius:* `publishLifecycle()` is the common path for **every** integration lifecycle event, on
both branches. No integration can publish one. On the failure branch the throw is **uncaught** and
kills the supervisor thread. **Attaching a coordinator would not help** — `publishStarted` throws
before any device work. Both distribution paths are affected (the .deb wraps `build-image.sh`'s
output). The bench escapes only because it runs full Corretto 21, not the jlinked runtime.

*Why CI cannot see it:* `distribution/ci/install-smoke.yml:5` states the assert set verbatim —
*"loopback health probe → assert RUNNING + token + auth enforced → uninstall."* No integration-health
assert. The probe targets `/api/v1/entities`, which returns **200 with an empty list**. `INV-RF-01`
("boot continues") works as designed and, combined with an assert set that stops at auth, **converts
a total integration outage into a green install.**

*What the operator sees:* `HomeSynapse Core is running.` · `active (running)` · `200 {"data":[]}`.
**Indistinguishable from a correct fresh install awaiting pairing.** Of 24 probed HTTP paths only
four respond — `/` (302), `/api/v1/entities`, `/api/v1/runs`, `/api/v1/automations` (all 200, all
empty). Every health/status/integration path 404s, including `/health`, `/api/v1/health`,
`/api/v1/integrations`, `/metrics`, `/internal/health`. The log's claim that *"the supervisor health
surface carries the failure"* **has no reachable HTTP surface on any path probed.**

### 3.2 HIGH

**F-15 — Imager pre-populates the customisation fields with the retained BENCH profile.** Hostname
arrived pre-filled `hs-dev-1`; the user password and Wi-Fi SSID+password were also retained. The
settings doc frames these as *values to choose*; they are *defaults to overwrite*, and the retained
defaults are exactly the two values it forbids. An operator who agrees with every word of the doc and
clicks NEXT through a screen that already looks filled in ships `hs-dev-1` + `homesynapse` and
detonates both documented hazards at once — including the `postinst:23-27` landmine, silently, with
the install still reporting success. **The doc's own warning is defeated by the tool's defaults.**

**F-19 — turning Wi-Fi off in Imager does not turn the radio off.** The card carries
`cfg80211.ieee80211_regdom=US` and `runcmd: [rfkill, unblock, wifi]` **unconditionally**, with Wi-Fi
entirely unconfigured. The doc's stated reason for leaving Wi-Fi off is that an unconfigured
interface can stall `network-online.target`, which the unit waits on — and the real unit does declare
`After=/Wants=network-online.target`. The bench's actual protection is `dtoverlay=disable-wifi`; the
fresh image has no such line. *Measured:* `NetworkManager-wait-online.service` was the slowest unit on
both boots — **11.555 s** (boot 1) and **9.776 s** (boot 2, ≈53 % of an 18.3 s userspace boot).
`wlan0` stayed `DOWN` and `rfkill` is **not installed on Lite**, so the unblock runcmd silently
failed. **Honest limit: consistent with the predicted cost, causation not isolated** — no control
boot with `disable-wifi` was taken, and taking one would have meant editing the card.

**F-21 — the bench application does not start at boot.** `bench.sh` starts it via `nohup … &`;
there is **no systemd unit at either scope**. **Validated in the field**: after the restore reboot the
S2-6 block reported *"app NOT running (expected after reboot)"* and had to run `~/bench.sh start`.
The packet's Phase-6 criterion is unreachable by rebooting alone, and neither the packet nor the
settings doc says so. *(The .deb path does not share this defect — see the cold-boot assert.)*

### 3.3 MEDIUM–HIGH

**F-24 — every clean stop leaves the unit in `failed` state.** Captured at the instant of the stop:
`Result=exit-code · ExecMainCode=1 · ExecMainStatus=143 · ActiveState=failed`. The shutdown itself was
textbook: Javalin stopped → Jetty connector stopped → **WAL checkpoint completed** → DatabaseExecutor
shutdown → *"HomeSynapseCore stopped … (SIGTERM)"*. Then systemd: *"Main process exited,
code=exited, status=143/n/a — Failed with result 'exit-code'."* 143 = 128+15: the JVM handles SIGTERM
and exits(143) itself, so systemd sees a non-zero **exit** rather than death-by-its-own-signal. The
unit declares no `SuccessExitStatus`. Consequences: the unit is `failed` after every normal stop and
every reboot; `systemctl --failed` reports a failure that did not occur; "did it stop cleanly?" is
unanswerable from systemd state alone; and `Restart=on-failure` classifies TERM-based termination as
restart-worthy. Data preserved across stop (token, `homesynapse-events.db`, `data/zigbee/`).

**F-17 — cleared Wi-Fi fields silently re-populate on every revisit.** Operator, verbatim: *"every
time I return to Wifi tab after deleting the fields, they repopulate and I have to remove them
again."* "Off" is not a stable state; it is re-armed by mere navigation. **The act of stepping back to
double-check re-introduces the defect.**

**F-22 — two identically-named, identically-sized (44 B) API token files; only one is authorized.**
`~/hs-bench/config/initial_api_token` works (`bench.sh:18`); `~/.homesynapse/config/initial_api_token`
returns **403 on every route**. The state-dir one — the intuitive place to look — is wrong. This
session walked into it before reading `bench.sh`.

### 3.4 MEDIUM and below

- **F-16** — the Imager review screen shows *no values*, only "…configured". An F-15
  contamination is invisible at the last gate before an irreversible write.
- **F-14** — the settings doc has no position on **Raspberry Pi Connect**, a step that did not exist
  in 1.x and establishes outbound connectivity to Raspberry Pi infrastructure. Ruled OFF this rep.
- **F-18** — the doc's SSH-key instruction yields `id_ed25519_pi`, a non-default filename whose
  `IdentityFile` applies only within `Host pi`. `hs-fresh` has no stanza, so OpenSSH never offers it.
  The doc's promise (*"ssh works with no password"*) does not hold as written. Remedy used:
  `ssh -i ~/.ssh/id_ed25519_pi`.
- **F-20** — *"the S2-1 read block"* is referenced by the physical sequence's **first** instruction
  and does not exist. Authored by this session as `s2-1-preswap.sh` (+ `s2-1b`, `s2-1c`).
- **F-13** — the settings doc describes Imager 1.x navigation; v2.0.10 replaced it with a six-step
  rail. **Amended down mid-rep**: the OS-selection path survives intact; drift is confined to the
  customisation dialog. *(Severity lowered on evidence — recorded because the correction matters.)*
- **F-9 (Stage-1) → converted to a measurement.** `health-probe.sh` requires **curl or wget**, and
  falls through to `printf '000'` (read as "not up yet") if neither exists — so the readiness gate
  times out at 90 s, `ExecStartPost` fails, and the unit fails, *while the apt output blames the
  application*. The package declares **`Depends: adduser`** and nothing else. **Measured on Lite:
  curl 8.14.1-2+deb13u3 and wget 1.25.0 are both present** → latent, not triggered. The undeclared
  dependency is real; this image happens to satisfy it.

## 4. AS-DOCUMENTED vs AS-RUN

| Step | Documented | Run | Why |
|---|---|---|---|
| Rep date | Tue 2026-08-11 | Wed 08-12 (Phases 0–1) + Thu 08-13 (1b–6) | operator availability |
| Card label | `— 2026-08-11` | `— 2026-08-13` | true date; the label's only job is identification |
| Imager nav | 1.x tabs | v2.0.10 rail | F-13 |
| Imager version | unspecified | **2.0.10, not downgraded** | a stranger today gets 2.x; downgrading would fake the measured thing |
| Wi-Fi off | leave blank | blank **+ re-verified at the artifact** | F-17 makes blank unstable |
| Wi-Fi radio | implied off | **left enabled; card NOT edited** | F-19 — editing would erase the drift the rep exists to surface |
| SSH reach | `ssh nick@hs-fresh.local` | `ssh -i ~/.ssh/id_ed25519_pi …` | F-18 |
| S2-1 block | "run it" | authored here | F-20 |
| Install cmd | `sudo apt install ./…deb` | `… -y …` | non-interactive over ssh; `-y` answers the same prompt an operator would. No other change |
| bootfs check | not specified | mounted read-write on Windows | deliberate; Windows created `System Volume Information` — predicted, pre-accepted, harmless |
| Phase 5 legs | optional | **clean stop + restart + data-preservation RUN**; uninstall/update **skipped** (CI-proven) | recorded, not silent |
| USB topology | Rosonway hub (I3b) | **coordinator direct to Pi USB3** | introduced by the restore — see §6 |

## 5. Bench restore — verified

`hostname hs-dev-1` · SD `SD128` serial **`0xb4c3895a`** · `/mnt/nvme` mounted · **C-1** coordinator
back (`/dev/zigbee → ttyUSB0`, `10c4:ea60`) · **C-4** `bench.sh start` run (app was not running, as
F-21 predicted) → *"RADIO UP after 16 s"* · `bench.sh status` → `[OK] running (pid 2185)` + health
tokens + **empty failure tokens** · `bench.sh entities` → 585 B, six entities, **5 AVAILABLE + 1
UNAVAILABLE** (exact baseline match), viewPosition 91127 · zigbee **channel 20, panId 0x774c**, 6
devices relinked, `EMBER_NETWORK_UP` · nightly re-armed **Fri 2026-08-14 04:30:00 EDT** ·
`throttled=0x0`, 49.4 °C.

## 6. ⚠️ One configuration delta introduced by the restore — needs a decision

The coordinator is now plugged **directly into a Pi USB3 port**; before the rep it ran through the
**Rosonway hub**. Corroborated by enumeration: `Bus 003 Device 020/023` behind two hubs
(`2109:2822` VIA Labs, `0bda:5411` Realtek) before → **`Bus 003 Device 002`** now.

It works — the udev rule matches on vendor/product/serial rather than port path, so `/dev/zigbee` and
the autosuspend pin resolve correctly, and the radio came up in 16 s. **But** there is a standing
documented topology decision (`2026-07-25_rosonway-topology-move_I3b_bench-session-report.md`), power
delivery and enumeration order differ between a powered hub and a root port, and the Friday nightly
plus the **open S31 evidence read** would otherwise run against an undocumented topology — confounding
their results with a variable this rep introduced.

**Recommendation: restore the Rosonway path before the Friday 04:30 fire.** "Restore the bench" means
the state we found it in, and topology is part of that state. That direct-attach *works* is useful
data and is recorded — but adopting it is a change, and changes belong to the hub.

## 7. Insight rider — PROPOSED ONLY (S-10 / W-2)

Sized S/M against the A-14 15 h/wk floor. **The charter adopts or declines. Nothing here is a work order.**

1. **(S) Assert integration health in install-smoke.** The single highest-leverage item. F-23
   proves the current assert set converts a total integration outage into a green install. One
   assertion — "every declared integration reached RUNNING, or the failure is exposed on a health
   endpoint" — closes the class, not just this instance.
2. **(S) Expose a health/status endpoint.** The log says *"the supervisor health surface carries the
   failure"*; 24 probed paths say otherwise. Either the surface does not exist or it is undiscoverable —
   both are fatal to operability, and both are cheap to fix.
3. **(S) Fix the jlink module computation** — run jdeps over the whole `lib/` set rather than one jar,
   and/or add `jdk.jfr` to `FLOOR`. Consider failing the build when a module in `FLOOR` is absent from
   the linked runtime.
4. **(S) `SuccessExitStatus=143` on the unit** (F-24) — one line; makes "stopped cleanly" legible.
5. **(S) Declare the real dependencies** — `Depends: adduser` omits curl|wget, which the install's own
   readiness gate requires (F-9).
6. **(S) Pin card provisioning to a checked-in file.** Imager 2.0 ships a CLI and `--log-file`. A
   committed customisation file makes provisioning a reviewable artifact and renders F-15, F-16
   and F-17 **structurally impossible**.
7. **(S) Give the bench app a systemd unit** (F-21) — makes "restore" mean "reboot", which is what
   every runbook already assumes.
8. **(S) De-duplicate the token trees** (F-22).
9. **(M) Install-rehearsal as a standing evidence class.** This rep produced 12 findings, one CRITICAL,
   against an artifact that had already passed CI. A recurring rehearsal against a clean image is cheap
   insurance for the W-2 claim surface.

**Named candidates for the post-gate queue (NOT work orders):** a first-boot assertion harness that
fails loudly when a customisation did not land; declarative unit/drop-in state for the bench.

## 8. Self-audit — what a hostile reviewer attacks, and five errors of mine

1. **A derived clock correction carried forward as constant.** My container ran ~24 h slow, then
   silently re-synced. I kept applying the old offset and concluded there had been a second overnight
   gap. There had not. Corrected against the operator's machine. *Lesson: re-verify a correction at
   the instrument; never carry it.*
2. **A token that did not mean what it said.** My Wi-Fi grep printed `NO WIFI TRACE — clean` *alongside*
   grep hits, because two probed files did not exist and GNU grep exits 2, firing the `||` branch. The
   conclusion holds on file contents and mtimes — **not** on that line.
3. **I probed the wrong token file** (F-22) and briefly recorded `AUTHENTICATED → 401` as if the app
   had failed. It had not: I wrote `sudo tr … < "$TP"`, and the *redirect* runs as the calling user.
   The app was right; my script was wrong.
4. **A sloppy glob.** My zigbee restore check globbed all `bench-*.log` and `tail -3`, printing
   `panId=0x9b65` from a historical file. The current boot's value is `0x774c`, printed twice in the
   same output by `bench.sh` itself. No anomaly existed.
5. **An expectation derived without accounting for reboot semantics.** I asserted the restored bench
   should read `degraded / 1 failed`. It read `running / 0 failed` — **which is correct**: `failed` is
   a runtime state from Thursday's suite run, and a reboot clears it. My baseline was post-nightly;
   the restored state is post-boot. Different by construction.

*Also:* I truncated the failed-unit name with `head -15` in S2-1 and needed a second block to recover
it; and I ran `sha256sum -c` from the wrong cwd, briefly appearing to show 118 integrity failures that
were purely my error (`MANIFEST.sha256 -c` → **all OK** when run correctly).

**Weakest evidence in this return:** F-19's causation. Two samples show `NetworkManager-wait-online`
dominating boot, but no control run with `dtoverlay=disable-wifi` was taken, so the attribution to
`wlan0` is inference, not measurement. A hostile reviewer should attack there first, and would be
right to.

**Second weakest:** the claim that no health surface exists. I probed 24 paths, including every
conventional one. That is strong, but a probe cannot prove non-existence — an unguessed path remains
possible. The claim is stated as "no health endpoint responded on any of 24 probed paths."

**Not evidenced:** the uninstall-data-preserved and update-smoke legs (deliberately skipped, CI-proven).
Nothing here tests the artifact under a real Zigbee load — F-23 makes that untestable on this build.

---

# 9. Cross-stage synthesis and late corrections

*Added on final review, after reading four sources the body of this return had not consulted:
`distribution/smoke/run-smoke.sh`, `distribution/README.md`, the Stage-1 return
(`_scratch/h3/2026-08-09_H3-return_ROOT-DUPLICATE-displaced-v50-beat-5.md`), and the hardening block of
`homesynapse.service`. Three of the four changed something material. They are recorded here rather
than silently folded in, so the correction itself is auditable.*

## 9.1 Register reconciliation — done

Stage 1 ends at **F-12**. Stage 2 is now **F-13 … F-24**, one continuous register:

| new | was | title (short) |
|---|---|---|
| F-13 | F-S2-1 | Imager 1.x navigation in the doc (amended down mid-rep) |
| F-14 | F-S2-2 | no position on Raspberry Pi Connect |
| F-15 | F-S2-3 | Imager pre-fills the **bench** profile |
| F-16 | F-S2-4 | review screen shows no values |
| F-17 | F-S2-5 | cleared Wi-Fi re-arms on revisit |
| F-18 | F-S2-6 | SSH key never offered to `hs-fresh` |
| F-19 | F-S2-7 | Wi-Fi "off" does not disable the radio |
| F-20 | F-S2-8 | the referenced S2-1 block does not exist |
| F-21 | F-S2-9 | bench app does not start at boot |
| F-22 | F-S2-10 | two identical-looking token files |
| F-23 | F-S2-11 | **packaged runtime lacks `jdk.jfr`** |
| F-24 | F-S2-12 | clean stop leaves the unit `failed` (exit 143) |

Stage 1's taxonomy codes (`DOC` / `LB` / `GI` / `CA` / `LAT`) were **not** applied to F-13…F-24 —
this lane read the codes in use but did not find their expansions defined, and declined to invent them.

## 9.2 Three Stage-2 findings are not independent discoveries

**F-15 is the delivery vector for Stage-1's F-12.** F-12 already states the landmine: `postinst:23-27`
skips creating the service account if a login user named `homesynapse` exists, silently voiding
`README.md:116`. What F-15 adds is *how it actually happens to a careful operator* — Imager retains the
bench profile and pre-fills `homesynapse` into the username field. **F-12 was a hazard; F-15 shows it
has a high-probability, near-invisible trigger.** Together they are stronger than either alone.

**F-24 is the first fruit of Stage-1's F-8.** F-8 predicted: *"the hardened systemd unit has never
executed outside GitHub's amd64 Ubuntu runner … Stage 2 is first contact."* This rep supplied that
first contact, and first contact immediately produced F-24 (exit 143 → `failed`). F-8's risk was real
and is now discharged into a concrete defect.

**F-9 is measured, as this return already states** — curl and wget are both present on Pi OS Lite, so
the undeclared dependency is latent here. Stage 1 already anticipated exactly this: *"Latent on
Raspberry Pi OS; **live on any trimmed Debian base, container or netinst.**"* This rep confirms the
Raspberry-Pi-OS half of that prediction and does not test the other half.

## 9.3 ⚠️ CORRECTION — **F-23 is not an arm64 problem, and CI has been green on it all along**

The body of this return implies F-23 was found because we ran on real arm64 hardware. **That framing
is wrong and the hub must not inherit it.**

The jlink module set is computed by `build-image.sh` identically on every architecture. An amd64 build
in CI produces a runtime that **also** lacks `jdk.jfr`. And the CI assert set — now read from the
actual script rather than its header comment — cannot see it:

`distribution/smoke/run-smoke.sh` asserts, in order: service active/RUNNING · loopback health probe
green · token minted **and owned by `homesynapse`** · unauthenticated request rejected 401/403 ·
`GET /` → 302 · `GET /dashboard/` → 200 · stop → uninstall → **data preserved**. There is **no
integration assert of any kind.**

**Therefore: every green install-smoke run to date has certified an artifact whose integration
subsystem cannot start.** This is not an architecture gap. It is an assert-coverage gap, and it has
been silently true for as long as `publishLifecycle` has touched `jdk.jfr.Event`.

This makes F-23 **more** serious than §3.1 states, not less — and it interacts with Stage-1's **F-6**
(*"the gate of record is architecture-blind"*) without being explained by it.

## 9.4 ⚠️ IMPORTANT NUANCE — `PrivateDevices=yes` is a second, *known* blocker

`homesynapse.service` sets `PrivateDevices=yes`, and its own comment says so explicitly:

> `# RAMP (post-M9): the Zigbee coordinator is a serial device. PrivateDevices=yes blocks /dev access,`
> `# so loosen it then and allowlist the coordinator, e.g. PrivateDevices=no / DeviceAllow=/dev/ttyUSB0 rw /`
> `# SupplementaryGroups=dialout`

So **even with `jdk.jfr` restored, the packaged service could not reach a Zigbee coordinator** — by
design, as a documented post-M9 deferral. Two consequences the hub needs:

1. **Do not read F-23 as "the artifact was supposed to run Zigbee and mysteriously doesn't."** For
   *serial* integrations the packaged path was knowingly not ready.
2. **F-23 is still independent and still CRITICAL**, because `publishLifecycle()` throws for **every**
   integration regardless of I/O type. A non-serial integration would fail identically, and
   `PrivateDevices` has nothing to do with it.

Also: because the coordinator was physically unplugged for the whole rep (SD-5 rail) *and*
`PrivateDevices=yes` would have hidden it anyway, **this rep could not have tested Zigbee end-to-end on
the packaged path under any circumstances.** That is a scope fact, not a shortfall.

## 9.5 🔴 The pattern worth more than any single finding

This project has now hit the **same failure class at least four times**:

| # | Instance | The assert that passed |
|---|---|---|
| 1 | iteration-3 | *"REPORTING-CLEAN was VACUOUS"* (named in the Stage-1 return) |
| 2 | B3.1 A-5 | the anti-vacuous line added in response |
| 3 | **F-10** (Stage 1) | `command-s31-settle` asserts `terminal == true` — and `CONFIRMATION_TIMED_OUT` satisfies it. 14/14 PASS establishes nothing |
| 4 | **F-23** (this rep) | install-smoke asserts *boot + health + auth* — all true while the integration subsystem is dead |

The runner README already carries the lesson in one line: *"pgrep is the survival gate — never
`status`-based."* **The recurrence is the finding.** Each instance was fixed individually; the class
was not. Every one of these asserts verified a *proxy* that is cheap to satisfy, rather than the
*property* the gate exists to establish.

**Proposed, S:** a standing review question applied to every gate assert — *"name an input under which
this assert passes and the property is false."* If the answer comes easily, the assert is a proxy.
F-10 and F-23 would both have been caught at authoring time by that one question.

## 9.6 Install-path fidelity — verified against the contract

`distribution/README.md:24` documents the headline path as:

```
sudo apt install ./homesynapse_<version>_<arch>.deb
```

**That is exactly what was run** (plus `-y`, recorded in §4). The README's stated outcomes — user +
dirs + perms, enable + start, print the token path — all occurred and are evidenced in §1. The
documented **no-dpkg fallback**, `sudo distribution/install/install.sh ./…tar.gz` (README:33), was
**not exercised**; it remains unevidenced on arm64 hardware. README:103-105 also matches observation:
`HOMESYNAPSE_HOME=/var/lib/homesynapse`, token at `/var/lib/homesynapse/config/initial_api_token`,
with the move to `/etc/homesynapse` deferred to M13.

## 9.7 Coverage gaps in this rep — stated so nobody assumes otherwise

- **`GET /dashboard/` was never probed.** CI asserts it returns 200; this rep did not check it. `GET /`
  → 302 was observed and matches CI's expectation, but the shell itself is unverified on arm64.
- **The `install.sh` tarball path** was not exercised (README:33).
- **`/etc/homesynapse/homesynapse.env`** (1572 B conffile) was confirmed present with correct
  ownership but its **contents were never read**; it may carry operator-relevant knobs.
- **No `dtoverlay=disable-wifi` control boot** for F-19 causation (would have required editing the card).
- **Uninstall and update-smoke legs** deliberately skipped (CI-proven).
- **No load, soak, or restart-storm testing.** The rep is a first-boot and first-install rep.
- **The fresh card still holds the completed install.** It can be re-inserted to close any of the above
  without re-flashing — roughly a 10-minute round trip. **Do not wipe it before deciding.**

## 9.8 One more measurement worth recording

The failing bench-suite test **differs night to night**: Wed 2026-08-12 `FAIL command-identify-honest`
(ON-latency 0.30 s); Thu 2026-08-13 `FAIL command-confirm-s31` (ON-latency `n/a(FAIL)`). Both nights:
AUTO floor 7/9, 1 SKIP (hue-online), `bench-hero RESTORED ✓`, exit 1. **A different test fails each
night, so the bench suite has a non-zero flake floor.** That is not this rep's lane, but it bounds the
confidence of *any* evidence drawn from a single nightly run — including evidence the gate may rely on.
Also relevant to F-10: `command-confirm-s31` is the very leg whose precondition F-10 says is not
actually established.

Bench uptime before this rep was **3 weeks 6 days** (since 2026-07-16). The restore reboot was the
first in a month and completed cleanly.

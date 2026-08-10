<!--
file: context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md
purpose: The H3 clean-image fresh-install rep — STAGE-1 RETURN (the artifact half). Filed against the dispatch packet context/handoff/2026-08-09_H3-clean-image_fresh-install_operator-packet.md. Stage 1 (build the arm64 artifact) RAN AND PASSED on 2026-08-09; Stage 2 (the clean-image install) is RE-SLOTTED to Mon/Tue 2026-08-10/11 on hardware Nick is acquiring. Carries 12 findings, an unplanned cross-lane return on the OPEN s31 evidence read, and the Section-2 insight rider.
audience: the hub (adjudicates); Nick (ran hands). Cross-lane §7 routes to context/audits/2026-08-09_s31-confirm-timeout_evidence-read_v50-beat-3.md and is TIME-CRITICAL against the Fri 2026-08-14 EOD freeze.
state-type: operator return (stage-1 interim; supersede-in-place when Stage 2 files)
status: STAGE-1 COMPLETE · H3 [MUST] NOT CLOSED · STAGE-2 PENDING (Mon/Tue 2026-08-10/11)
governing-fences-held: bench untouchable (MEASURED, §4) · SD-5 coordinator rail (no radio act of any kind) · nightly margin (all Pi activity ceased 5 h 29 m before the 03:30 CT fire) · read-only on every repo (this file is the session's only write) · evidence captured verbatim
-->

# H3 — Clean-Image Fresh-Install Rep · STAGE-1 RETURN (artifact half)

## §0 Decision summary — read this first

**H3 [MUST] is NOT closed.** The ledger row requires *"one documented fresh install onto a clean Pi image (install.sh or deb) reaching a healthy boot (health-probe green) with the runbook's steps as written."* No install was performed. The row stays **PENDING**.

**What Stage 1 did close:** the rep's blocking precondition. There was no installable arm64 artifact in existence — and CI cannot make one. One now exists, built from the gate-of-record commit, verified, and in hand on two machines. Stage 2 is now a ~40-minute install rep instead of an open-ended build-and-install session.

**What the hub must decide, and by when:**

| # | Decision | Deadline | Where |
|---|---|---|---|
| D-1 | Whether the H3 row's phrase *"install path **reproducible**"* is claimed in the procedural sense or the build sense. **In the build sense it is now MEASURED FALSE** (§6 F-7). | before the Sun 2026-08-16 read | §6 F-7 |
| D-2 | Whether gate #4's standing green — measured exclusively on amd64 — is stated as such on gate day. | before the read | §6 F-6 |
| D-3 | The s31 confirm-timeout adjudication: **H-I is REFUTED** on the bundle record (§7). H-D vs H-L remain live and **the current instrument cannot discriminate them**. | before the Fri 2026-08-14 EOD freeze | §7 |
| D-4 | Whether any of the 7 rider items (§8.3) are adopted pre-freeze. Recommended: **none** — all are post-gate. Two are one-line and launch-blocking-class. | charter | §8.3 |

**Nothing in this return moves code. Every improvement is PROPOSED-only, per the packet's fence 4.**

---

## §1 Scope — what ran, what did not, and why

The packet's Phase 0 STOP fired as written: **no spare SD card and no spare Pi existed on 2026-08-09.** Per the packet, improvising onto the bench card was refused. Nick ruled the hub amendment on the spot:

- **STAGE 1 (2026-08-09, this return):** build the arm64 artifact on the bench Pi per escalation E1 option (a), confined to a new subdirectory on the NVMe. No install, no card, no swap, no image.
- **STAGE 2 (re-slotted Mon/Tue 2026-08-10/11):** flash the clean image onto a newly acquired card, swap, install the prebuilt `.deb` exactly as documented, probe green, restore the bench.

Nick additionally ruled the NVMe **out as an install target** (its fstab/boot state is not mutated during freeze week) — it was used only as build scratch. Provenance is disclosed rather than laundered: **the artifact was built at `d26777c` on the bench card's OS and will be installed onto a separately flashed clean image.** That disclosure is stronger than CI's own topology, where the runner that builds is the runner that installs.

Phases 3–6 of the packet (documented install · probe set · optional legs · bench restore) are **not attempted in this return** and carry forward to Stage 2 unchanged.

---

## §2 Timings (UTC; America/Chicago in parentheses)

| Mark | UTC | CT | Note |
|---|---|---|---|
| Inventory + network prereqs (S1-0) | 01:51:54 | 20:51 | GitHub auth FAIL discovered here |
| Repo made public by Nick | ~02:10 | ~21:10 | operator act; see F-3 |
| Scratch dir created (S1-1) | 02:27:46 | 21:27 | the rep's first and only new directory |
| Anonymous clone + pin `d26777c` (S1-2P) | 02:27:47 | 21:27 | clean tree, 0 dirty files |
| **BUILD START** | 02:27:49 | 21:27 | |
| build-image.sh END rc=0 | 02:30:52 | 21:30 | **183 s** — Gradle wrapper download + installDist + npm ci + Vite + jdeps + jlink + tar |
| build-deb.sh END rc=0 | 02:31:08 | 21:31 | **16 s** |
| **BUILD DONE** | 02:31:10 | 21:31 | **201 s total, cold caches** |
| S31 evidence pull (S31-B) | 02:38:17 | 21:38 | zero-write streaming tar |
| Stage-2 preflight (S2-0) | 02:38:18 | 21:38 | |
| S31 state discriminator (S31-C) | 02:44:53 | 21:44 | |
| Fence audit (S1-10) | 02:53:53 | 21:53 | |
| Artifact verification (S1-11) | 02:54:07 | 21:54 | |
| Determinism test launched (S1-8) | 02:54:30 | 21:54 | |
| Artifact collected to desktop (S1-6) | 02:54:48 | 21:54 | sha256 match both ends |
| Determinism test DONE | 02:56:08 | 21:56 | **98 s**, warm caches, image only |
| Last Pi activity | 03:00:52 | 22:00 | **5 h 29 m before the 03:30 CT nightly** |

**Nightly-fence note.** The packet states the nightly fires at 04:30 America/Chicago (fence 3, Phase 6). **That is wrong.** `nexsys-bench/tools/scheduler/nexsys-bench-nightly.timer:9` reads `OnCalendar=*-*-* 03:30:00 America/Chicago`, and the instrument confirms it: `NEXT Mon 2026-08-10 04:30:00 EDT` — the Pi's system clock is `America/New_York`, so 04:30 *there* is 03:30 CT. The packet's own Phase 0 line says 03:30 CT, so the packet is internally inconsistent. **The unit file is the source of truth; the operating deadline is 03:30 CT.** Also banked: `Persistent=true` — a card swap spanning 03:30 will fire the missed suite immediately on the restore boot.

---

## §3 The artifact of record

```
file        homesynapse_0.1.0+gd26777c_arm64.deb
bytes       50,626,968
sha256      5b13820237d990eba5997179f67815986601f97b3085236f40c3269ccd18c575
Package     homesynapse      Version 0.1.0+gd26777c      Architecture arm64
Depends     adduser          Installed-Size 73,592 KB

tarball     homesynapse_0.1.0+gd26777c_arm64.tar.gz
bytes       54,330,398
sha256      3221b805ba05ec36580a31f1717783b51d6baf40cd4365a37ae4c9eafa92394a

source      d26777c601c5acd909d8b6bacd7cd71ccc8fd802   (working tree clean, 0 files)
            contains ca0f41d — the gate-of-record code commit (CI #208 + install-smoke #28)
built on    hs-dev-1 · Raspberry Pi 5 Model B Rev 1.1 · aarch64 · Debian GNU/Linux 13 (trixie)
toolchain   Amazon Corretto 21.0.11 (matches install-smoke.yml:44 `distribution: corretto`)
            Node v22.23.1 / npm 10.9.8 (matches install-smoke.yml:53 `node-version: '22'`)
locations   Pi:  /mnt/nvme/h3-build-scratch/homesynapse-core/distribution/deb/build/
            Desktop: ClaudeFolder\_scratch\h3\artifact\   (sha256 verified identical)
```

**Independent verification performed without installing (S1-11):**

- 205 payload entries · 55 jars · 129 runtime files · all 8 README-promised paths PRESENT
- `runtime/bin/java` → `ELF 64-bit LSB pie executable, ARM aarch64` — and it **executes**: `OpenJDK Runtime Environment Corretto-21.0.11.10.1 (build 21.0.11+10-LTS)`
- launcher carries all six LTD-01 flags: `Xms512m Xmx1536m UseG1GC MaxGCPauseMillis=100 Xss512k UseStringDeduplication`
- **`MANIFEST.sha256` VERIFIES — 118 entries.** Note: `install.sh:44` performs this check; **the `.deb` install path never does.**
- **Dashboard SPA present in the packaged jar** — `dashboard/index.html` + a 101,883 B bundle. `npm ci` and Vite genuinely ran inside the 183 s; the timing is not a skipped build.
- Version **CONSISTENT** across image `VERSION` and `.deb` `Version` — both `0.1.0+gd26777c`.

**Traceability.** The version string derives from `git describe --always` → `d26777c` → the non-digit branch at `common.sh:62-64` → `0.1.0+gd26777c`. The commit is legible in the filename, the package metadata and the on-disk `VERSION`.

---

## §4 Fence audit — the bench was not touched (measured, not asserted)

The build log raised `!! HOME/.gradle EXISTS: 899M` / `!! HOME/.npm EXISTS: 150M`. **That alarm was a defective check of mine** — it tested existence, not modification. Settled definitively with `find -newermt` against the exact build-start timestamp:

| Check | Result |
|---|---|
| `~/.gradle` files modified since 02:27:49Z | **0** (newest file inside: 2026-08-06 19:34 — three days pre-rep) |
| `~/.npm` files modified since 02:27:49Z | **0** (newest: 2026-08-06 19:33) |
| `~/homesynapse-core` (deployed tree) modified | **0** |
| anything under `$HOME` (depth ≤2) in the window | **nothing** |
| SD card used | 13,799,844 KB — unchanged at build start and build end |
| bench app | pid **100370** — identical before, during and after |
| Zigbee coordinator | never touched; no radio act of any kind |
| S31 | no command issued; §7 used reads only |

All build traffic went where directed: 867 M `gradle-home`, 97 M `npm-cache`, 455 M clone, 8.9 M tmp — all on `/mnt/nvme/h3-build-scratch`. Total NVMe footprint after both builds and the artifact inspection: **2.0 GB of 222 GB free.** Nothing was deleted. The scratch tree is left in place for Stage 2 and for the hub's disposal.

---

## §5 AS-DOCUMENTED vs AS-RUN

| Step | As documented | As run | Deviation? |
|---|---|---|---|
| Obtain source | *(not documented anywhere)* | anonymous `git clone` of the public origin, `checkout --detach d26777c` | **doc gap** — F-1/F-3/F-5 |
| Build image | `distribution/image/build-image.sh` | identical, invoked from the clone root as `install-smoke.yml:62` does | none |
| Assemble .deb | `distribution/deb/build-deb.sh` | identical, same CWD | none |
| Build host prereqs | *(not documented)* | JDK 21 Corretto + Node 22 + npm + git, all already present on the host | **doc gap** — F-5 |
| Exec bits | implied | `-rwxrwxr-x` on both scripts; direct invocation, no `bash` prefix needed | none |
| Cache locations | *(not documented)* | `GRADLE_USER_HOME` / `npm_config_cache` / `TMPDIR` redirected to scratch | **operator addition** — required by the fence, not by the docs |
| Install | `sudo apt install ./homesynapse_<version>_<arch>.deb` | **NOT RUN** — Stage 2 | deferred |

**Operator additions made for fence compliance, recorded so they are not mistaken for documented steps:** cache redirection; `oom_score_adj=1000` + `renice 19` on the build so the kernel would kill the build rather than the bench app; a 30-second app-liveness watchdog; `setsid` detachment so an ssh drop could not orphan a build.

---

## §6 Findings

Severity key — **LB** launch-blocking class · **GI** gate-integrity class · **CA** claim-accuracy class · **DOC** documentation · **LAT** latent/hygiene.

| # | Sev | Finding | Anchor |
|---|---|---|---|
| F-1 | DOC | **No distribution document names a target OS image or version.** Exhaustive grep of `distribution/**` finds only "Raspberry Pi (arm64)" inside E1's problem statement. The install contract never states what it installs onto, so "a clean Pi image" is operator choice, not spec. | `distribution/README.md` (whole) |
| F-2 | LB | **No arm64 artifact exists and CI cannot produce one.** Artifacts are arch-specific by construction; CI runs amd64 only; E1 is open and undecided. A Pi operator cannot obtain an installable package from the project. | `escalations.md:9-18`, `common.sh:74-75`, `install-smoke.yml:34` |
| F-3 | LB | **Source acquisition is unprovisioned.** At rep start the Pi could not fetch source: `Repository not found / Authentication failed`. The repo is normally private and the device holds no credentials — no deploy key, no token, no apt repository. Working practice is a **manual repository-visibility toggle per Pi update**: an undocumented operator step that briefly exposes the source publicly and cannot survive a real distribution channel. | S1-0 `NETWORK_PREREQS`; `README.md:21-38` |
| F-4 | LAT | **`hs_version()` is CWD-dependent.** It resolves `$0`-relative inside a `bash -c`, so the stamped version depends on the directory the operator invokes from. Two scripts invoked from different directories would stamp different versions into the image and the package. Did not bite here **only because operator discipline forced both from the clone root** — mitigated by procedure, not by code. | `common.sh:48-53` |
| F-5 | DOC | **No build-host prerequisites are stated anywhere.** The image build requires JDK 21, Node, npm, git and network access to three registries. The only mention is a comment in a Gradle file, not in any operator-facing document. | `README.md:21-38` vs `web-ui/dashboard/build.gradle.kts:38` |
| F-6 | **GI** | **The gate of record is architecture-blind.** install-smoke — *"gate #4: install path proven"* — runs exclusively on `ubuntu-latest` (amd64) while the product ships arm64. **No evidence exists in the repo or the bench docs of any prior arm64 run of the distribution path**; on the available record, `2026-08-10T02:27:49Z` is the first. The standing green certifies an architecture no customer will run. | `install-smoke.yml:34`; absence across `distribution/**`, `nexsys-bench/**` |
| F-7 | **CA** | **The reproducibility claim is MEASURED FALSE.** `README.md:117` claims *"pinned JDK 21 and tool versions; the image build is deterministic and self-checksumming."* Two independent clones of `d26777c`, same toolchain, build cache explicitly disabled: **`MANIFEST.sha256` differs; tarballs differ.** Drift is **exactly 19 of 118 entries, all first-party `lib/*.jar`**. The jlinked `runtime/` (129 files) and every third-party jar are **byte-identical**. Mechanism: no `isPreserveFileTimestamps=false` / `isReproducibleFileOrder=true` anywhere in `build-logic/` (and no `gradle.properties` at all), so Gradle's `Jar` task embeds per-entry timestamps. `build-image.sh:140` pins only *tar member* mtimes via `--mtime=@${SOURCE_DATE_EPOCH:-0}`, which cannot affect bytes inside jars. *Prediction filed before the test; confirmed including the confinement of drift.* | `README.md:117`; S1-8 verdict |
| F-8 | **GI** | **The hardened systemd unit has never executed outside GitHub's amd64 Ubuntu runner.** The bench runs `installDist` output as a user process with `HOMESYNAPSE_HOME=~/hs-bench` and no unit at all. Every hardening directive is unexercised on Debian 13 trixie / systemd 257 / arm64 / AppArmor. Stage 2 is first contact. | `homesynapse.service:68-93` vs `nexsys-bench/tools/bench.sh:8` |
| F-9 | **LB** | **The package under-declares its runtime dependencies.** `control.in:7` declares only `Depends: adduser` — **confirmed in the shipped artifact**. The unit's readiness gate runs `/opt/homesynapse/libexec/health-probe.sh`, which hard-requires `curl` or `wget`; with neither it logs *"neither curl nor wget available"*, returns `000` forever, times out at 90 s, fails the unit, and surfaces as `postinst:60`'s generic *"installed but did not start cleanly."* CI cannot catch this — GitHub runners ship curl. Latent on Raspberry Pi OS; **live on any trimmed Debian base, container or netinst.** | `control.in:7`, `health-probe.sh:60-82`, `homesynapse.service:50`, `postinst:60` |
| F-10 | **GI** | **`command-s31-settle` asserts a terminal phase, not a state change.** Its sole positive evidence is `data.terminal == true`, with its own comment: *"SOME terminal, either disposition — the relay is OFF after it regardless."* `CONFIRMATION_TIMED_OUT` satisfies `terminal: true`. Its **14/14 PASS record therefore cannot establish the physical precondition** the confirm leg depends on. See §7 for what the record actually shows. Second instance tonight of a lesson class this project has already named and fixed elsewhere (iteration-3 *"REPORTING-CLEAN was VACUOUS"*; B3.1 A-5 anti-vacuous line; the runner README's *"pgrep is the survival gate — never `status`-based"*). | `scenarios/command-s31-settle` evidence block |
| F-11 | **CA** | **E1's cost trade-off rests on an unmeasured assumption.** `escalations.md:12` prices on-Pi arm64 building as *"simple, **slow**, needs a Pi in the loop"* and recommends option (b) — qemu cross-build in CI — instead. **Measured on target hardware: 201 s cold, 98 s warm.** "Slow" is false. Options (a) and (c) are cheap and the recommendation should be re-derived from the measurement. | `escalations.md:9-18`; §2 timings |
| F-12 | **LB** | **The package silently forfeits its least-privilege claim if a login user named `homesynapse` already exists.** `postinst:23-27` creates the service account only `if ! getent passwd homesynapse`. Where a *login* account of that name exists, creation is skipped, `User=homesynapse` binds to it, and the service runs as a full interactive account with a shell and a `/home` — voiding `README.md:116`'s *"dedicated `homesynapse` user"*. The install reports success and says nothing. **Not hypothetical: the bench card's own uid 1000 is `homesynapse`.** | `postinst:23-27`, `README.md:116` |

---

## §7 Cross-lane return — the OPEN s31 confirm-timeout evidence read

**Unplanned.** The packet authorised a read-only bundle pull; the pulled record turned out to discriminate hypotheses filed in `context/audits/2026-08-09_s31-confirm-timeout_evidence-read_v50-beat-3.md`. Reported as data and source-reading. **This lane does not adjudicate.**

Method: zero-write streaming tar (`tar -czf - | ssh > local`) — 41,664 bytes, 230 entries, sha256 `cf442a698506d9fb0659d9314c1320a95c87742fc06166bed3d27ad014c8aae0`. Nothing written on the Pi; the S31 was never commanded.

### 7.1 H-I is REFUTED — and its premise was factually wrong

The evidence read's §1.3 states the preceding leg *"printed `captured command_id = '01KZJTBXKXW5FYE9D83EPZNAJX'`"*, and §1.4 builds H-I on a claimed 12-character byte-identity. The bundles show otherwise:

| Leg | Command ULID | Target entity | POST | Terminal |
|---|---|---|---|---|
| timeout-honesty-no-change `083126Z` | `01KZJTBQMR6KZHGYV1VD7092W6` | `01KX1PA4HSJ581GASYB7DHE40F` | 08:31:20 | CONFIRMATION_TIMED_OUT *(by design)* |
| **command-confirm-s31 `083132Z`** | `01KZJTBXKXW5FYE9D83EPZNAJX` | **`01KXW1W1SBJZERC9MBAMV2DWKE`** | 08:31:26 | CONFIRMATION_TIMED_OUT |

The two ULIDs share only **7** leading characters (`01KZJTB`), then diverge at position 8 (`Q` vs `X`) — exactly what two ULIDs minted 6 s apart should do. The claimed 12-character identity does not exist. The s31 leg **minted its own command, against the correct entity, and adjudicated that command's own terminal phase.** Its `resolved.json` binds `let.command_id` to its own ULID and its `api-captures.json` records the `202` stimulus.

**Refuted as a class, not just for one night.** Across all 13 confirm runs on record (2026-07-30 → 2026-08-09): **13 distinct ULIDs, zero duplicates, every one targeting the S31 entity.** The runner's capture hygiene is sound over the entire record. No bench-runner defect WU is indicated on this evidence.

### 7.2 The measured latency distribution (never previously measured)

| Terminal | n | ACCEPTED → terminal |
|---|---|---|
| CONFIRMED | 6 | 0.174 · 0.307 · 0.366 · 2.120 · 3.626 · 3.658 s |
| CONFIRMATION_TIMED_OUT | 7 | 5.079 – 5.915 s *(the window itself, never a distinct mode)* |

Post-split-settle record: **6 PASS / 5 FAIL over 11 runs.** The CONFIRMED population is bimodal — three at 0.17–0.37 s (consistent with the 2026-07-29 probe's 111 ms and the Hue's 0.33 s) and three at 2.1–3.7 s that passed only by beating an arbitrary cutoff; worst passing margin **1.42 s**. The leg is sampling a latency distribution that straddles the assertion window on a device the platform itself downgraded to `best_effort` (`reporting_configured verified=0 degraded=1`, 2026-07-19).

### 7.3 §1.6's inference needs qualifying — and the reason is in the core

The evidence read's §1.6 reads the settle PASS as *"the S31 relay was alive and confirming within ~1 s of the FAIL adjudication."* The settle command did reach a genuine `CONFIRMED`:

```
01KZJTC3JMR0MCM5XEJMBQPBZC   ACCEPTED 08:31:32.948644
                             DISPATCHED 08:31:32.953407
                             CONFIRMED  08:31:33.460949     (512 ms)
```

**But `lastChanged` never moved.** A state read at 2026-08-10T02:44:53Z — 18 h later — returns `on=false` with `lastChanged = 2026-08-08T08:31:27.978Z`, i.e. **the platform has observed no on/off transition since 08-08**, across the 08-09 `turn_on`, the 08-09 `turn_off`, and ~223 subsequent reports (stateVersion 6329 → 6552 ≈ one update per 4.9 min; that rate assumes stateVersion increments per state event).

So the settle was **CONFIRMED with no state change.** The mechanism is in the core:

```java
// core/device-model/.../ExactMatch.java:24-26
return expectedValue.equals(reportedValue)
        ? ConfirmationResult.CONFIRMED
        : ConfirmationResult.NOT_YET;
```

`EXACT_MATCH` confirms on **value equality alone — no transition required**. A `turn_off` against an already-off relay is confirmed by the first report carrying `on=false`, including a routine unsolicited report. The codebase *has* a transition-aware mode — `AnyChange.java:26-28` compares against `previousValue` — but on_off uses exact match (the S31 scenario records `match_type exact`).

**Precisely what this does and does not establish.** It establishes that the device was **alive and reporting**, and that its CONFIRMED does **not** establish that the relay *actuated*. It does **not** establish that `EXACT_MATCH` is the wrong semantic — a user commanding "off" on an already-off device is arguably satisfied. The point for the hub is narrower and sharper: **CONFIRMED currently means "the device reports the state you asked for," not "the device did what you asked"** — and the product's headline question is *"did it actually confirm?"*

### 7.4 What remains open, and why the instrument cannot close it

H-D (real timeout at the device) and H-L (late delivery) are both live. **The current bundle design cannot discriminate them:** the A-9 post-window read fires at the timeout (08:31:32Z), and the settle leg commands the device **0.7 s later**, destroying the state that would distinguish them. The 08-10 read arrived 18 h too late for the same reason — a fact this lane established by spending the read, and reports as a negative result.

One asymmetry is worth the hub's attention without being over-read: the device confirmed an off-command in **512 ms**, 0.7 s after a turn_on failed to confirm in 5.42 s. If `EXACT_MATCH` can be satisfied without a transition, that 512 ms may be a **no-op confirmation** rather than evidence of a healthy report path — in which case it says nothing about why the turn_on went unconfirmed.

**Candidates for the hub (PROPOSED only, no work order):** strengthen the settle assert to require an observed transition (`currentPhase == CONFIRMED` plus a state `field_equals`), or rename the leg to what it proves; defer the settle by ≥1 native report interval so the post-window read can discriminate; measure the S31's native reporting interval properly rather than inferring it from stateVersion.

---

## §8 The insight rider (Section 2 of the packet)

### 8.1 Friction log — every manual step, ambiguity and undocumented prerequisite

| # | Friction | Anchor |
|---|---|---|
| 1 | No target OS image is named; the operator must choose one and the choice is unrecorded by the docs | `distribution/README.md` |
| 2 | No build-host prerequisites listed; JDK 21 / Node / npm / git / three registries discovered by reading Gradle internals | `web-ui/dashboard/build.gradle.kts:38` |
| 3 | Source acquisition undocumented and unprovisioned; required an out-of-band repository-visibility change | `README.md:21-38` |
| 4 | Version stamping is CWD-sensitive with no documented invocation directory | `common.sh:48-53` |
| 5 | Cache locations undocumented; defaults write ~1 GB into `$HOME`, which silently violates a "do not write to this machine" constraint | `build-image.sh` (no `GRADLE_USER_HOME` guidance) |
| 6 | The `.deb` path never verifies `MANIFEST.sha256`; only the tarball path does — asymmetric integrity for two paths the README presents as equivalent | `install.sh:44` vs `postinst` |
| 7 | The service account name collides with a plausible human login name, with no guard | `postinst:23-27` |
| 8 | The readiness probe's dependency is undeclared, and its failure surfaces as a generic message | `control.in:7`, `postinst:60` |

### 8.2 Reproducibility verdict — one paragraph

**A competent stranger holding only the documentation cannot reach probe-green, and would fail before touching the installer.** `distribution/README.md` opens at `sudo apt install ./homesynapse_<version>_<arch>.deb` and never says where that file comes from; no arm64 package is published anywhere (F-2), the source repository is private with no provisioned device credential (F-3), and no document states that building requires JDK 21, Node and npm (F-5) or which OS image is the target (F-1). Assume they clear all of that: they would then build successfully — the scripts themselves are sound, ran **as written** with zero edits, and produced a correct, self-verifying, arch-correct artifact in **201 seconds** — and they would then install onto a base image whose package set determines whether the readiness probe can run at all (F-9), under a service account whose privilege posture depends on whether their login name happens to collide (F-12). **The installer is the strong part of this system; everything around it — the artifact channel, the source channel, and the environment contract — is undocumented or absent.** That is the reproducible-install claim surface in one sentence, and it is a better W-2 result than a clean pass would have been.

### 8.3 PROPOSED improvements for the S-10 charter's W-2 scope

Priced against the **A-14 floor: 15 h/week, weekend-anchored** (`2026-08-02_A14_attended-hours_charter-input.md:20`). **S ≈ ≤2 h · M ≈ 2–8 h.** All post-gate; the charter adopts or declines. **Nothing here is a work order.**

| # | Item | Closes | Size |
|---|---|---|---|
| W2-1 | **Publish an arm64 artifact channel** (release attachment or apt repo). Removes the need for an operator to obtain source at all, and dissolves the visibility-toggle practice. The single highest-leverage item in this return. | F-2, F-3 | **M** |
| W2-2 | Declare the readiness dependency: `Depends: adduser, curl \| wget` | F-9 | **S** |
| W2-3 | Reproducible jars — `isPreserveFileTimestamps = false` + `isReproducibleFileOrder = true` in `homesynapse.java-conventions.gradle.kts`. Verify by re-running S1-8 to a byte-identical `MANIFEST.sha256`. | F-7 | **S** |
| W2-4 | Guard the service account in `postinst`: assert the pre-existing `homesynapse` is a system account (uid < 1000 / nologin) and fail loudly otherwise | F-12 | **S** |
| W2-5 | Re-derive E1 from the measurement (201 s cold / 98 s warm) — a decision, not code. Option (c) native arm64 runner, or an on-Pi release step. | F-11, F-6 | **S** |
| W2-6 | State the target base image and the build-host prerequisites in `distribution/README.md` | F-1, F-5 | **S** |
| W2-7 | **Install-rehearsal as an evidence class**: a standing checklist that an install rep runs on a *minimal* image and records the base environment (`dpkg -l` for probe dependencies, login-user name, OS codename) as part of the evidence. This rep's value came almost entirely from recording the environment, not the install. | F-1, F-8, F-9, F-12 | **M** |

**Named candidates for the post-gate queue (not W-2, not work orders):** run install-smoke on arm64 in CI (E1 option (b) or (c)); strengthen the settle assert per §7.4; carry the "vacuous green" lesson into a cross-lane checklist rather than per-file comments — this rep produced two independent instances of that class in a single evening (§10).

---

## §9 Stage 2 — carried forward

Prepared and on disk at `_scratch/h3/STAGE-2-IMAGER-SETTINGS.md`, derived from the S2-0 instrument read:

- `BOOT_ORDER=0xf461` → **SD is tried first**; the NVMe is a single GPT `Linux filesystem` partition with **no boot partition**, so a failed flash cannot boot the live bench. **No NVMe disassembly required.**
- Target image: **Raspberry Pi OS Lite (64-bit), trixie** — matches the bench codename; Lite chosen deliberately as the *more adversarial* test (Desktop's package richness would mask F-9) and because it has no udisks session to auto-mount the attached NVMe.
- ⛔ **The fresh image's login user must be `nick`, never `homesynapse`** — see F-12.
- Card label: `hs-dev-1 BENCH SD128 0xb4c3895a`. Coordinator to unplug: SONOFF Dongle-Plus MG24, CP210x `10c4:ea60`, serial `0ae2dd7cecf8ef11b80168135c2a50c9`.
- Power is clean (`throttled=0x0`, 47.7 °C) — removes undervoltage as a confounder.
- **Record `dpkg -l | grep -E '^ii +(curl|wget)'` on the fresh image BEFORE installing** — converts F-9 from a reading into a measurement either way.

**Pre-stated Stage-2 failure mode, filed before the attempt (law 9 posture).** `ExecStartPost` gives the probe 90 s (`service:50`); `TimeoutStartSec=120`; `Restart=on-failure` with `StartLimitBurst=5`/`300 s`. A cold first start on a fresh microSD must mint the token *and* answer HTTP 200 inside 90 s, or the unit fails, restarts five times and gives up, surfacing as `postinst:60`. The probe's own four log strings are the decision tree: `token not yet available` (not minted / perms) · `no connection yet` (JVM still booting) · `up, not ready yet (503)` (projection not caught up) · `auth rejected` (token/config fault, exits 3 immediately). Separately, `After=network-online.target` (`service:16-17`) on a **loopback-only** service may stall first boot on a fresh headless image.

---

## §10 Self-audit

**What was skipped.** The entire install half (Phases 3–6) — by ruling, not by omission. `update-smoke` and the uninstall-data-preserved leg: CI-proven, optional per the packet, not attempted. AppArmor state on the bench: not captured (my flag error).

**My instrument errors — five, all mine, none affecting a result.**
1. Queried the nightly timer in **system** scope; it is a **user** unit — corrected by Nick, verified at `nexsys-bench-nightly.service:1-2`. Would have entered the record as a false finding.
2. `swapon` not on the login PATH (`/usr/sbin`) — `free -m` was authoritative.
3. `aa-status --summary` is not a valid flag on Debian.
4. The `HOME/.gradle EXISTS` check tested **existence, not modification** — a defective test that produced a false fence alarm, resolved in §4.
5. `dpkg-deb --contents | grep -q` produced `Broken pipe` diagnostics — **the exact bug `build-deb.sh:101-104` documents and guards against.** I reproduced in my own harness a defect the repo had already learned.

Errors 1 and 3 share a root cause: **flags authored from memory rather than verified at the instrument.** Errors 4 and 5, with F-10, are the evening's third and fourth instances of a *vacuous-check* class — which is why W2-7 and the cross-lane checklist candidate exist. **My 30–50 minute build estimate was wrong by an order of magnitude (actual: 201 s)**; that error became F-11, which is one of the more useful findings here.

**The weakest evidence in this return.** (a) The ~4.9 min S31 reporting interval is *inferred* from stateVersion deltas, assuming stateVersion increments per state event — unverified. (b) F-7's drift is attributed to jar timestamps by mechanism and by the confinement of drift to exactly the Gradle-`Jar`-produced set; a byte-level entry diff would prove it and was not run. (c) The 201 s build is a single cold measurement on one machine. (d) F-6's "first arm64 build in project history" is an argument from absence across the repo and bench docs — strong, but not a positive proof.

**What a hostile reviewer attacks, in the order they will attack it.**
1. *"H3 is not closed."* **Correct, and this return says so first.** The row is PENDING.
2. *"You built on the bench card's OS, so the artifact is not from a clean environment."* True and disclosed in §1. The artifact's provenance is fully specified and its integrity independently verified; Stage 2's install target is separately flashed. This is a stricter topology than CI's, where the builder and the installer are the same machine.
3. *"Your fence claim is self-reported."* Answered by measurement in §4, not assertion — including a false alarm my own tooling raised and then disproved.
4. *"The findings are code reading, not install evidence."* F-7, F-11, F-2 and F-9's `Depends` line are **measurements**. F-9's runtime consequence, F-8 and F-12 are readings pending Stage 2 — labelled as such.
5. *"§7 exceeds your lane."* Fair. It is reported as data, refutation and source-reading with adjudication explicitly reserved to the hub, and it was produced by a read the packet authorised.

---

## §11 Evidence index — raw outputs, verbatim

All block scripts, their `.out.txt` captures and the artifact live at `ClaudeFolder\_scratch\h3\` (outside every repo, so the read-only fence holds). All 11 blocks are `bash -n` parse-clean — the same lint `install-smoke.yml:55-59` applies to `distribution/`.

| Block | Capture | Contents |
|---|---|---|
| S1-0 | `s1-0.out.txt` | inventory + network prereqs (the GitHub auth failure) |
| S1-1 | `s1-1.out.txt` | scratch creation, pre/post state |
| S1-2P | `s1-2p.out.txt` | anonymous clone, pin, checkout verification |
| S1-4 / S1-5 | `s1-4.out.txt`, `s1-5*.out.txt`, `artifact/h3-stage1-build.log` | the full build log, verbatim |
| S1-6 | `s1-6.out.txt`, `artifact/` | transfer + dual-end sha256 + `BUILD-SUMMARY.txt` |
| S1-8 / S1-9 | `s1-8.out.txt`, `s1-9*.out.txt` | determinism test + per-file drift list |
| S1-10 | `s1-10.out.txt` | fence audit |
| S1-11 | `s1-11.out.txt` | artifact inspection |
| S2-0 | `s2-0.out.txt` | Stage-2 preflight |
| S31-A/B/C | `s31-*.out.txt`, `s31-evidence-20260810T023817Z.tgz` | the 230-entry evidence pull (sha256 `cf442a69…aae0`) and the state discriminator |

**Handoff to Stage 2:** the artifact and `STAGE-2-IMAGER-SETTINGS.md` are on the desktop; the Pi scratch (`/mnt/nvme/h3-build-scratch`, 2.0 GB) is left in place and nothing was deleted. This file supersedes in place when Stage 2 files.

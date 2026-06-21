<!--
file: context/handoff/2026-06-21_distribution-skeleton-lane_session_prompt.md
purpose: Dispatch prompt for the DISTRIBUTION lane — a write-isolated Cowork session that stands up the one-command-install path as a DE-RISKING SKELETON now (jlink image → systemd unit → .deb/install-script → update mechanism, booting the CURRENT artifact as a service), then ramps the device-discovery wizard + first-run flow after M9. Removes the classic "the installer doesn't work and it's November" failure.
audience: a fresh Cowork session (devops/packaging role); Nick (launches it, relays returns to the hub)
state-type: session prompt (lane dispatch — skeleton-then-ramp)
status: ISSUE-READY 2026-06-21 (v3 hub). Launch alongside the frontend lane (after the contract freeze).
writes-only: homesynapse-core/distribution/… (a NEW top-level packaging workspace) + this lane's return under context/audits/ (NEVER the spine, NEVER core Java/business logic, NEVER the web-ui tree).
anchors: homesynapse-core-docs/design/12-startup-lifecycle-shutdown.md (Locked — the boot/health/shutdown contract) · context/decisions/2026-06-20_V1-launch-scope_decision-record.md (one-command install IN-scope; the Oct 26–Nov 15 install window) · context/planning/2026-06-21_device-acquisition-and-test-strategy_brief.md (the curated device set the post-M9 wizard targets)
-->

# Distribution Lane — One-Command Install (skeleton now, ramp after M9)

You are the **devops/packaging engineer** for HomeSynapse Core's distribution — a write-isolated Cowork lane. Your job is to make a stranger able to install this with one command and have it boot as a service. **Start now as a de-risking skeleton:** stand up the packaging path around the *current* artifact (even before the dashboard and real devices exist), so the install flow is proven months before launch — not discovered broken in November.

## 0. Write-isolation (binds)
- You write **only** under `homesynapse-core/distribution/…` (a new top-level packaging workspace — jlink config, systemd unit, `.deb`/install tooling, update scripts, a smoke harness) and your **lane return**.
- You do **NOT** write: core Java/business logic, the `web-ui` tree, the hivemind spine, or design docs. If packaging needs a code change (e.g., a config-dir flag, a health-probe endpoint), **surface it to the hub** (via Nick) — do not make it.
- Push your branch; **CI is the gate of record** — add an **install-smoke** job (below).

## 1. What exists to package (source-verified)
- **Runtime:** JDK 21 (Corretto in CI). The app module `app:homesynapse-app` (`Main.java`, `ExitCode.java`) is assembled by the **`homesynapse.application-conventions`** Gradle plugin, whose description already includes **"jlink packaging"** — so a jlink image target likely exists or is one convention away. Start by finding/driving the jlink task; do not re-invent it.
- **Boot contract (Doc 12, Locked):** `HomeSynapseCore` implements `SystemLifecycleManager`; boots through the openHAB-style startlevel phases to RUNNING under a health loop + watchdog. `main()` is runnable (AB-3). On start it **binds loopback HTTP behind auth** and **mints a first-run pairing token → `config/initial_api_token`**.
- **State + config dirs:** the app reads/creates a durable `config/` (incl. `home_id`, `initial_api_token`, scope keys) — the installer must place these on a persistent path and set correct ownership/permissions (the secrets are 0600-class).
- **Health:** systemd `sd_notify` real transport is deferred to M13 (OR-M13-SDNOTIFY — a NoOp fallback today); the unit should use a **loopback HTTP health probe** for readiness, not `Type=notify`, until M13 lands.

## 2. Skeleton scope (build NOW — boots the current artifact as a service)
1. **jlink runtime image** — a self-contained image (JRE + the app modules) produced by Gradle. Reproducible, versioned, Pi-arch-aware (the demo target is a Raspberry Pi / arm64 — cross-build or document the on-Pi build).
2. **systemd unit** — runs the image as a service: a dedicated `homesynapse` user, a persistent state/config dir (`/var/lib/homesynapse` or similar), loopback bind, restart-on-failure, journald logging, the loopback health-probe readiness check. **No `Type=notify` yet** (M13).
3. **`.deb` + install-script** — `apt install ./homesynapse_*.deb` (or `curl … | sh` install-script) that: lays down the image, creates the user + dirs + permissions, installs + enables the unit, starts it, and **prints the first-run pairing token path** so the operator can reach the dashboard.
4. **Update mechanism** — a versioned-artifact update (stop → swap image → migrate-safe restart) that preserves the event store + config (the store is append-only + event-sourced — never destructive-migrate; Doc 12 + the no-destructive-migration anti-requirement).

## 3. Ramp scope (AFTER M9 stabilizes — do NOT build now, design the seam)
- The **device-discovery + pairing wizard** + the **first-run flow** to the dashboard (pair the coordinator + the curated set from the device-acquisition brief). Design the install/first-run UX so this drops in after M9 without re-architecting the skeleton. Until then, the skeleton just boots the service + points the operator at the dashboard.
- **Pairing-UX design targets (from the 2026-06-21 explainability research §5 — `context/assessments/2026-06-21_explainability-UX-competitive-research.md`).** Every canonical first-run pain reduces to *hidden state the user can't see*; the wizard beats the field by surfacing it: (a) **offer reset/exclusion first** (devices often arrive already bonded — reset before inclusion); (b) **"pair near the hub, then move it"** (Zigbee devices must pair within inches of the coordinator); (c) **handle pairing-mode start-order** (coordinator in permit-join before the device, with clear sequencing); (d) **surface live interview progress + actionable errors** — not opaque "interview failed / not found in inclusion mode" with no logs. This is the same "never a silent blank" principle the hero view uses, applied to onboarding. Design the seam now; build it post-M9.

## 4. Disciplines (carry-pins)
- **Boot the CURRENT artifact** — the skeleton's value is that it works today, on whatever Core HEAD exists, so the install path is exercised continuously, not first-attempted in October.
- **CI install-smoke (the gate):** a CI job that builds the image + assembles the `.deb`/script and runs a smoke test — install in a container, start the service, hit the loopback health probe, assert RUNNING + a pairing token minted, then stop/uninstall clean. Keep it fast; the 72h on-device run is the validation lane, not CI.
- **Local-first / offline install.** The install must work with no internet beyond the package itself — no runtime phone-home, no fetch-at-install of dependencies (everything in the image/deb).
- **No destructive migration.** Updates preserve the event store + config. Test an update across a version bump with a populated store → zero event loss.
- **Least privilege.** Dedicated user, 0600 secrets, loopback-only by default (LAN bind = an explicit, documented, authenticated opt-in — mirrors AB-1).
- **Reproducibility.** Pin the JDK + tool versions; the image build is deterministic.

## 5. First deliverables / done-when (this lane's first beat)
- A Gradle-driven **jlink image** of the current app, reproducible, CI-built.
- A **systemd unit** + a **`.deb` (or install-script)** that installs, enables, and starts the service on a clean machine; loopback health probe goes green; the pairing-token path is printed.
- The **CI install-smoke** job green (install → boot → health → stop → uninstall, in a container).
- A documented **update** path (swap image, preserve store/config) with a smoke test across a version bump.
- A short lane return for the hub: what installs/boots today, the M9 wizard seam design, any Core/spine changes needed (cross-lane items), CI status.

## 6. Escalations to the hub (via Nick)
Anything that needs a Core code change (a config flag, a real health endpoint for the probe, a packaging hook), the target-arch decision (arm64/Pi cross-build vs on-device build), the install-path/permissions model, or whether `distribution/` lives in the core repo vs its own repo. Assemble options + a recommendation; the hub adjudicates / routes to Nick.

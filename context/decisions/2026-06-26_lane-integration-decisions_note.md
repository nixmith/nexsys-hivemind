<!--
file: context/decisions/2026-06-26_lane-integration-decisions_note.md
purpose: The short lane-integration decisions note from the §3 consolidated decision pass (Group C) — the v1.1 contract name field, the Doc 13 WS→poll currency addendum, the two CI wirings, the distribution Core hooks (E1/E2/E3/E6), and the FRONTEND_DOCTRINE.md shared-home promotion. Captures Nick's co-sign (decisions C8–C12); routes each to its owner.
audience: Nick (the CI file drops + the public-API call), PM hub, the Web-UI lane, the Distribution lane, the Core lane (E2/E3/E6)
state-type: decision note
status: RATIFIED 2026-06-26 — Nick co-signed C8–C12 in the §3 consolidated decision pass (C8 via the question, C9–C12 via the Group-C "confirm all as recommended" ruling).
inputs: context/audits/2026-06-26_frontend-dev-lane_return.md + context/audits/2026-06-26_distribution-skeleton-lane_return.md.
-->

# Lane-Integration Decisions — Note (2026-06-26)

The Track-A fleet's first returns surfaced lane-integration items needing the hub/Nick. All ruled in the §3 pass (Group C). Each captured below with the ruling + the owner/route.

## C8 — Entity `name`/`label` field (the frontend friction) → **add it (additive)**
**Ruled (Nick, public-API call).** The A1/A2/A3 entity reads carry no human display name; the dashboard humanizes `entityId` via `labelFor`. Add an **optional, additive** `name` field to the v1.1 contract — **Core returns it when set, omits it when unset**; the UI defaults to a humanized slug only when absent and swaps to the real field when it lands. **Folded** into the contract-freeze doc (`2026-06-21_dashboard-read-API-contract-freeze.md`, A1 shape + the additive-field note). **Decide-the-shape-now, fill-it-when-natural:** the implementation sources `name` from config/pairing and sequences with the config/M9 work, **not M7.4**. Non-breaking.

## C9 — Doc 13 WS→poll currency → **a Doc 13 currency addendum** (the no-WS/poll ruling is FIRM)
**Ruled.** Doc 13 (Web UI Observability MVP, Locked 2026-03-10) is WebSocket-first; the V1 rulings (V1 record D-OPEN-3 + the contract freeze + the frontend dispatch) make **no-WebSocket / poll-1–2s FIRM**. Mark the superseded sections — **§1 (WS-first principle), §3.5 (WS integration), §3.8 (health-via-WS), §8.2 (WS protocol table), and the WS-specific parts of §4.1/§6/§11** — with a currency addendum pointing them at the poll model. **Route:** a Doc 13 currency amendment (the AMD-95/AMD-96 pattern — a Locked-doc currency reconciliation through a source-verifying review → Nick co-sign → fold). Off the M7.4 critical path; schedulable. (Not folded into a Locked body here; captured as the next currency-amendment item.)

## C10 — The two CI wirings → **Nick drops the files into `.github/workflows/`** (activates gate #4)
**Ruled.** GitHub only runs workflows under `.github/workflows/` (repo-root, spine-owned, outside each lane's write-isolation). The two lane-delivered, ready-to-use files:
- `web-ui/dashboard/ci/frontend.yml` → `.github/workflows/` (path-filters `web-ui/dashboard/**`; runs `npm ci && npm run verify`).
- `distribution/ci/install-smoke.yml` → `.github/workflows/` (the container install-smoke = the mid-August **gate #4 "install path proven"**).
**Owner: Nick — one copy/symlink each.** This is the one step between "smoke written" and the gate being live. (Spine-owned; the hub does not write `.github/workflows/`.)

## C11 — Distribution Core hooks → **E1 + E2 (prioritized) + E3 + E6; E4@M13, E5 non-blocking, E7 decided**
**Ruled (Nick co-sign).**
- **E2 — bind-host/port operator-configurable in Core (the headless-Pi + wizard prerequisite). PRIORITIZE: a small Core WU ahead of the M9 wizard.** The composition root reads `HOMESYNAPSE_BIND_HOST` / `HOMESYNAPSE_HTTP_PORT` (the env drop-in is already wired in the systemd unit); authenticated LAN opt-in. Without it the dashboard is unreachable on a headless Pi — the pairing-wizard prerequisite. **Slot it into the Core lane ahead of the M9 wizard** (a small WU; not on the M7.4a/b critical path, but before M9's wizard build).
- **E1 — target arch.** CI matrix: cross-build **arm64** (release) + **amd64** (smoke); emulated arm64 smoke on a schedule. Owner: whoever wires CI (with C10).
- **E3 — unauthenticated loopback `/health` in Core** (a small Core hook; the authed probe works today, so nice-to-have — bundle with E2).
- **E6 — write `initial_api_token` `0600` explicitly** (tiny Core hardening; the `0700` dir already closes exposure).
- **E4** (`LinuxSystemPaths` at the composition root) tracks with **M13**; **E5** (fold jlink into Gradle) **non-blocking** (the script is the fallback); **E7** (`distribution/` repo home) **decided — in-repo** through launch.
**Route:** E2/E3/E6 → small Core hooks (schedule E2 ahead of the M9 wizard; bundle E3/E6); E1 → CI; E4 → M13; E5/E7 → no action.

## C12 — Doctrine promotion → **a shared home now** (+ a future `nexsys-frontend` skill)
**Ruled.** `web-ui/dashboard/FRONTEND_DOCTRINE.md` (the lean, reusable frontend doctrine) is promoted to a **shared home now** (out of the single module), with a **future loadable `nexsys-frontend` skill** (analogous to nexsys-coder / nexsys-project-manager) as the later step. **Route:** the hub relocates the doctrine to a shared location; the skill is a future enabling-investment, not a V1 blocker. (Note: per the env-model, the live skill is a read-only cache; a future `nexsys-frontend` skill source would live in the hivemind and sync via Nick's mirror — Check 9 discipline.)

## Routing summary
- **Nick:** the two CI file drops (C10); the public-API `name` field is co-signed (C8, folded).
- **Core lane:** E2 (bind-host/port — ahead of the M9 wizard) + E3 + E6 (small hooks); the `name` field implementation rides the config/M9 work.
- **Hub:** the Doc 13 currency addendum (next currency-amendment item, C9); the doctrine shared-home relocation (C12).
- **CI:** the arch matrix (E1) with the C10 wiring.
- **Deferred:** E4→M13, E5/E7→no action.

<!--
file: context/instructions/2026-06-15_CC-1_bind-address_spike_spec.md
purpose: CC-1 empirical spike — does the composition-root HTTP server bind all-interfaces or loopback? Calibrates the urgency of the C1/B-H1 unauthenticated-surface HIGH (INV-SE-02 unenforced) so the app-bootstrap charter scopes auth correctly.
audience: Coder (CORE spike, throwaway — outside the production tree); PM on return
state-type: spike spec (READY TO DISPATCH)
status: AUTHORED 2026-06-15 (Track-3 follow-on). Cheap; dispatch now — independent of M7 and of the crypto lane.
routing: CORE / Coder. Empirical only; no production code, no design decision in this spike.
baseline: homesynapse-core HEAD 1eddd9a. Source-confirmed already (PM, converge): no `.host(` in lifecycle production code; `HomeSynapseCore.java:412` installs only `installReadinessGate`; `:434` calls `app.start(config.httpPort())` (no `.host()`, no auth filter).
-->

# CC-1 — Composition-root bind-address spike

## Why (one paragraph)

The converge's C1/B-H1 HIGH is that the composition root stands up an **unauthenticated** HTTP server (`installReadinessGate` only; `app.start(httpPort())` with no `.host()`; `AuthMiddleware`/`RateLimiter` unimplemented) — INV-SE-02 has no enforcing code, latent only because `main()` is a stub. **The urgency of the auth work depends on one empirical fact this spike settles:** does the server bind **all-interfaces** (internet-reachable on a misconfigured/forwarded LAN — urgent) or **loopback** (local-only — less urgent)? Pass (loopback) vs fail (all-interfaces) sets the auth-milestone priority on the app-bootstrap charter. This is the one CC-verification the converge ranked worth dispatching now.

## Scope fences

- **Throwaway spike, outside the production tree** (a spike that becomes production code is a governance failure). No production change. No auth implementation — this only *measures* the current bind posture.
- **No design decision here.** The spike returns a fact; the PM routes it into the charter.
- Cowork/sandbox cannot run Gradle — this is a CORE/Coder dispatch that CAN.

## Tasks

1. **Static confirm (re-run the PM's check, report verbatim):**
   - `grep -rn "\.host(" lifecycle api app` — expect **no** production matches (only the readiness gate is installed). Report any match with file:line.
   - Confirm `HomeSynapseCore` start path: the `app.start(...)` call site and whether any `.host(...)` / bind-address config is threaded. Quote the call site.

2. **Empirical bind test (the deliverable):**
   - In a spike test source set, construct/start `HomeSynapseCore` (the real composition root — note it is currently constructed only in tests) on an ephemeral port.
   - Assert what address the listening socket is actually bound to. Concretely: attempt to connect to the readiness endpoint via (a) `127.0.0.1` and (b) a **non-loopback** local address (the host's LAN IP, or bind-probe `0.0.0.0` reachability). Determine whether the server answers on the non-loopback address.
   - Record the framework default: if the HTTP layer (Javalin/Jetty per the stack) defaults to `0.0.0.0` when `.host()` is unset, state that and cite the framework version from the catalog.

3. **Report** (short return, route to PM):
   - `BIND POSTURE: loopback | all-interfaces` (the binary).
   - The static grep result (host-call sites: none / list).
   - The framework default-bind behavior + version.
   - One line: does this make the C1 auth work *urgent* (all-interfaces) or *standard-priority* (loopback) for the app-bootstrap charter.

## Done-when

A single `BIND POSTURE:` verdict backed by an executed test (not inference), the `.host(` grep result, and the framework default — handed to the PM to set C1's priority on the app-bootstrap charter. No production files touched.

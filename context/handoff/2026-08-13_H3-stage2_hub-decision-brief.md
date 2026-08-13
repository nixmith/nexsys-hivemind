<!--
file: context/handoff/2026-08-13_H3-stage2_hub-decision-brief.md
purpose: Adjudication-shaped companion to the H3 Stage-2 return. This file exists so the hub can
  think INDEPENDENTLY and CRITICALLY about the rep's output without re-reading a long operator
  transcript. It states what is decided, what is NOT, and the specific decisions only the hub can make.
audience: the hub / orchestration session; Nick
status: OPEN — five decisions pending. Freeze is Fri 2026-08-14 EOD.
source of record: context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md
-->

# H3 Stage 2 — hub decision brief

## 1. What is settled (no decision needed)

- **The H3 MUST row is satisfied on its own stated terms.** Documented install as written → healthy
  boot → health probe green → RUNNING + token + auth enforced, on a fresh-flashed clean Pi image.
  Install: exit 0 in 9 s. Auth: 401 / 200 / 403 negative control. Plus an un-asked-for cold-boot
  assert: the service comes up healthy after `reboot` with nobody logged in.
- **The bench is restored and verified** against a measured pre-swap baseline: six entities,
  5 AVAILABLE + 1 UNAVAILABLE, zigbee ch 20 panId 0x774c, nightly re-armed Fri 04:30 EDT.
- **Every hard fence held.** Coordinator physically out for the whole rep; read-only throughout;
  nothing was fixed, patched, or worked around.
- **The artifact is traceable**: `homesynapse_0.1.0+gd26777c_arm64.deb`, sha256 `5b1382…c575`
  verified three times, commit `d26777c`, clean tree, `MANIFEST.sha256 -c` all OK.

## 2. The decision the hub actually has to make

### ⚖️ DECISION 1 — does F-23 change what the gate means? (CRITICAL)

**⚠️ CORRECTED FRAMING (found on final review — see return §9.3): this is NOT an arm64 finding.**
The jlink module set is computed identically on every architecture, so the amd64 image CI builds
lacks `jdk.jfr` too. And `smoke/run-smoke.sh` — read from the script, not its header comment —
asserts only: service RUNNING · health probe green · token minted and owned · unauth rejected
401/403 · `GET /` 302 · `GET /dashboard/` 200 · stop → uninstall → data preserved. **No integration
assert of any kind.** Therefore **every green install-smoke run to date has certified an artifact
whose integration subsystem cannot start.** This is an assert-coverage gap, not an architecture gap,
and it makes the finding MORE serious than a first reading suggests.

**⚠️ COUNTER-NUANCE the hub must weigh (return §9.4):** `homesynapse.service` sets
`PrivateDevices=yes`, and its own comment states that this blocks `/dev` access and must be loosened
"post-M9" to reach the coordinator. So even with `jdk.jfr` restored, the packaged service could not
reach a *serial* device — **by documented design**. Do not read F-23 as "it was supposed to run Zigbee
and mysteriously doesn't." F-23 remains independent and CRITICAL because `publishLifecycle()` throws
for **every** integration regardless of I/O type.

**The fact:** the packaged runtime is missing `jdk.jfr`. `StandardIntegrationSupervisor.publishLifecycle`
touches `jdk.jfr.Event` on **both** the started and failed branches, so **no integration can publish a
lifecycle event on any build produced by `distribution/image/build-image.sh`.** On the failure branch
the throw is uncaught and kills the supervisor thread. Attaching a coordinator would not help.

**The tension the hub must resolve:**

- H3's assert set is *boot + health + auth*. Those pass, cleanly and repeatably. **By its own frozen
  wording, H3 is met.**
- And yet the artifact that passed **cannot run a single integration** — i.e. cannot do the thing the
  product is for. The install prints `HomeSynapse Core is running.`, systemd shows `active (running)`,
  and `/api/v1/entities` returns `200 {"data":[]}`. An operator cannot tell this apart from a correct
  fresh install awaiting pairing.

**This is not the operator lane's call.** Three defensible positions, stated without preference:

1. **H3 stands as written.** The criterion was frozen deliberately and narrowly; moving it after the
   evidence is in is exactly the anti-pattern a frozen gate exists to prevent. F-23 is logged
   against a different row.
2. **H3 stands, but a new blocking row opens** for "the shipped artifact runs its integrations",
   because the gate's *purpose* — evidencing a working local-first system — is not served by an
   artifact that cannot.
3. **H3 is contingent** — provisionally satisfied, confirmed once the module set is corrected and the
   rep re-run. Cheapest to re-verify (the whole hardware half is now ~45 min with the blocks on disk).

**What tips it:** the defect is a one-line build fix and a re-link. The *expensive* part is not the fix
but deciding whether an artifact that passes CI and fails in the field should ever have been able to.

### ⚖️ DECISION 2 — is the assert set itself a gate item? (recommend: yes)

`install-smoke.yml:5` states its asserts verbatim: *"loopback health probe → assert RUNNING + token +
auth enforced → uninstall."* Combined with `INV-RF-01` ("boot continues" on integration failure —
working as designed), **the assert set structurally converts a total integration outage into a green
install.** This is a finding about the *evidence standard*, not about one bug. Every future build has
the same blind spot until it is closed. One assertion closes the class.

### ⚖️ DECISION 3 — the USB topology delta (time-boxed: before Fri 04:30 EDT)

The restore left the coordinator plugged **directly into a Pi USB3 port** rather than through the
**Rosonway hub** (`Bus 003 Device 020/023` behind two hubs → `Bus 003 Device 002`). It works: udev
matches on vendor/product/serial, `/dev/zigbee` resolves, radio up in 16 s. But a documented topology
decision exists (`2026-07-25_rosonway-topology-move_I3b`), and the Friday nightly plus the **open S31
evidence read** would otherwise run against an undocumented topology, confounding their results with a
variable this rep introduced. **Operator lane's recommendation: restore the Rosonway path.** Adopting
direct-attach is a change, and changes are the hub's.

### ✅ DECISION 4 — finding-register reconciliation — **RESOLVED, no decision needed**

The Stage-1 register ends at **F-12**. Stage 2 has been renumbered to **F-13 … F-24** and is now a
continuous single register. Cross-stage relationships (three Stage-2 findings are *amplifications or
first-contact confirmations* of Stage-1 findings rather than independent discoveries) are mapped in
the return's §9. Stage 1's severity taxonomy (`DOC` / `LB` / `GI` / `CA` / `LAT`) should be applied to
F-13…F-24 by whoever owns the register — this lane did not invent expansions for those codes.

### ⚖️ DECISION 5 — which insight-rider items enter S-10 scope

Nine PROPOSED items, all S or M (return §7). The four with the highest leverage-to-cost ratio:
**(1)** assert integration health in install-smoke · **(2)** expose a health/status endpoint ·
**(3)** fix the jlink module computation · **(4)** `SuccessExitStatus=143`.

### ⚖️ DECISION 6 — the recurrence, not the instance (recommend: treat as its own item)

This project has hit the **same failure class at least four times**: iteration-3's *"REPORTING-CLEAN
was VACUOUS"*; the B3.1 A-5 anti-vacuous line added in response; **F-10** (`command-s31-settle`
asserts `terminal == true`, which `CONFIRMATION_TIMED_OUT` satisfies — so 14/14 PASS establishes
nothing); and now **F-23** (install-smoke asserts boot + health + auth, all true while the integration
subsystem is dead). The runner README already states the lesson: *"pgrep is the survival gate — never
`status`-based."*

**Each instance was fixed individually. The class was not.** Every one of those asserts verified a
cheap *proxy* instead of the *property*.

**Proposed (S):** one standing question applied to every gate assert — *"name an input under which
this assert passes and the property is false."* If the answer comes easily, it is a proxy. F-10 and
F-23 would both have been caught at authoring time.

## 3. Findings at a glance

| # | Sev | One line |
|---|---|---|
| **F-23** | **CRIT** | Packaged runtime lacks `jdk.jfr`; no integration can publish a lifecycle event; CI cannot see it |
| F-15 | HIGH | Imager pre-fills the **bench** profile; the doc's landmine warning is defeated by the tool's defaults |
| F-19 | HIGH | Wi-Fi "off" does not disable the radio; `wait-online` is the slowest boot unit (11.6 s / 9.8 s) |
| F-21 | HIGH | The bench app has no systemd unit — restore-by-reboot yields a dead bench |
| F-24 | MED-HIGH | Every clean stop leaves the unit `failed` (exit 143, no `SuccessExitStatus`) |
| F-17 | MED-HIGH | Cleared Wi-Fi fields silently re-arm on revisit — being careful re-introduces the defect |
| F-22 | MED-HIGH | Two identical-looking 44 B token files; the intuitive one returns 403 |
| F-16 | MED | Imager's review screen shows no values — contamination invisible at the last gate |
| F-14 | MED | Doc has no position on Raspberry Pi Connect (outbound connectivity) |
| F-18 | MED | The doc's SSH-key instruction yields a key OpenSSH never offers to `hs-fresh` |
| F-20 | LOW-MED | The physical sequence's first instruction references a block that does not exist |
| F-13 | LOW-MED | Imager 1.x navigation in the doc — **amended down mid-rep**; OS path survives |
| F-9 | — | **Converted to a measurement**: curl+wget both present on Lite → latent, not triggered. Stage 1 predicted exactly this: *"latent on Raspberry Pi OS; live on any trimmed Debian base"* |

**Cross-stage:** F-15 is the *delivery vector* for Stage-1's **F-12** (the landmine had no known
trigger; Imager's retained profile is one). F-24 is the *first fruit* of Stage-1's **F-8** (*"the
hardened unit has never executed outside GitHub's amd64 runner — Stage 2 is first contact"*). Neither
is an independent discovery, and both are stronger read together with their Stage-1 parent.

## 4. What this lane did NOT do, on purpose

No fix, patch, edit, or workaround of any kind — not to the card, not to the repo, not to the unit.
The Wi-Fi radio was **left enabled** although one `config.txt` line would have quieted F-19, because
editing it would have erased the drift the rep exists to surface. No uninstall or update-smoke leg
(CI-proven, deliberately skipped, recorded not silent). No control boot for F-19 causation, because
that too would have required editing the card.

## 5. Confidence and where to attack

**High confidence:** the H3 asserts (measured repeatedly, including cold boot); F-23 (proven at
three levels — journal stack trace, `--list-modules`, and root cause at file+line); F-24 (exit code
captured at the instant of the stop, with the full graceful-shutdown log); the restore (like-for-like
against a measured baseline).

**Attack here first:** F-19's causation — two samples show `wait-online` dominating boot, but with no
`disable-wifi` control the attribution to `wlan0` is inference. **Second:** "no health surface exists"
rests on 24 probed paths; a probe cannot prove non-existence.

**The operator lane logged five of its own errors** in the return's self-audit (§8), including two
where a bug of mine briefly looked like a product defect. Both were caught and corrected before
anything entered a finding. That list is deliberately in the record so the hub can calibrate how much
to trust the rest.

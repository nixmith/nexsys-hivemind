<!--
file: context/audits/2026-09-12_CI-1_intake_two-layer-audit_v70-b10.md
purpose: The hub's intake audit of CI-1's return (context/audits/2026-09-12_CI-1_return.md, 6,036 B): the soak off the gate, kept as a sample source.
audience: the hub · Nick
state-type: intake audit
status: FILED at v70 beat 10 (Sat 2026-09-12 ~10:2x CT; instrument 2026-09-12T15:17:47Z)
-->

# CI-1 intake (v70 beat 10)

## §0 Verdict
**ACCEPT.** 4 M + 0 A exactly; nothing staged. Re-executed at the bytes: the `bus-soak` job in `ci.yml` (`:61–:90`) carries the three setup steps identical to `check`'s, the run line verbatim, `continue-on-error: true`, the always-on upload of the two lifecycle paths; `check` untouched; the conventions' `useJUnitPlatform { if (!project.hasProperty("includeBusSoak")) excludeTags("bus-soak") }` (`:57–:60`); `@Tag("bus-soak")` with its import in both ITs (`BusSoakIT:39/:100`, `BusPositionCensusIT:32/:80`). The lane measured P1 both ways (81 / 83) and the job's exact run line (2 classes), and parsed the YAML.
**I1 applied by the hub:** `lifecycle/lifecycle/MODULE_CONTEXT.md:245` gains `-PincludeBusSoak` in its How-to-run line (a one-token doc edit the lane's census forbade) — the core card carries five files.
**Not re-run:** the four gradle runs (taken from the return's counts).

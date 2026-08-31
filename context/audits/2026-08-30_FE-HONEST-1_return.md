<!--
file: context/audits/2026-08-30_FE-HONEST-1_return.md
purpose: FE-HONEST-1 lane return — loud unresolvable refs (§10-J) + store-truth read path (§10-G/H/I).
audience: the hub (audit) · Nick (commit boundary)
status: FILED 2026-08-30 ~21:30 CT. Tree DIRTY by charter — nothing committed.
-->

# FE-HONEST-1 — lane return

## §0 FIRST

**VERDICT: DELIVERED — both §B rows repo-complete; gate GREEN (container instrument, disclosed below); THREE CONTRACT-GAP PROPOSALS filed; the frozen contract untouched; ZERO commits (tree left dirty for Nick).** Honest register per H8: **REPO-COMPLETE, LIVE-VERIFICATION PENDING** — no real-wire exercise ran from this instrument.

**CT-rederivation line:** filing date re-derived at the instrument: `TZ=America/Chicago date` → **2026-08-30, 21:29 CDT** (device clock, in-session).

**Census (git --no-optional-locks status --porcelain; GIT_OPTIONAL_LOCKS=0 held all session):** 11 paths, ALL under `web-ui/dashboard/src/` — 7 M (`components/CausalChain.tsx`, `lib/api/mock/scenarios.ts`, `lib/format.ts`, `lib/format.test.ts`, `lib/format.wire-nullability.test.ts`, `views/DevicesView.tsx`, `views/RunChainView.tsx`) + 4 ?? (`lib/registry.ts`, `lib/registry.test.ts`, `components/CausalChain.dangling.test.tsx`, `views/DevicesView.honesty.test.tsx`). +315/−33. No spine file, no core file, no contract file touched. One rider OUTSIDE the fence, disclosed under Deviations: a build tarball in `_scratch/`.

**Gates:** `npm run verify` GREEN end-to-end — tokens:check ✓ · lint ✓ · typecheck ✓ · **tests 18 files / 230 passed / 0 failed** ✓ · build ✓ · bundle 64.3 KB / 100 KB ✓ · contract-check ✓ (11 endpoints, v1.1.2-2026-07-26 unchanged).

**INSTRUMENT-LIMIT DISCLOSURE:** (1) The gate could NOT run on the mounted tree — `node_modules/` is Windows-installed and its native binaries (rollup/esbuild) don't load in the session's Linux VM. The gate ran in the session's cloud container on a **byte-identical copy of the working tree** (tarred from the mount post-edit, `npm ci` from the repo's own lockfile, then `npm run verify`). `frontend.yml` at Nick's keyboard / CI remains the gate of record. (2) The live Pi was not reachable from this instrument — no real-wire exercise (hence the H8 register above). (3) Preflight Check-7: the `$MNT/.claude/skills` local mirror sits outside the connected folders; the check ran instead against the account-synced skill copy this session loads — 8/8 files hash-identical to `nexsys-skills/orchestrators/nexsys-frontend`. PASS on that basis. Preflight aggregate: **PASS (all 8)**, 2026-08-31 ~02:1x UTC.

**Deviations:** (a) one pre-existing test assertion updated (`format.wire-nullability.test.ts`): it pinned the OLD unreadable-stamp copy "not recorded" — which §10-G shows is itself a false claim when the store holds the row; re-pinned to the store-truth register (in-lane, test file, the change is the WU's point). (b) `_scratch/fe-honest-1_dashboard_tree.tar.gz` (204 KB) — the gate-transport tarball; the VM cannot delete files; safe for Nick to delete. (c) Nothing else.

**Asks:** the three contract-gap proposals below (hub adjudication) + one Core-side observation (§4) + the MOCK-vs-deploy note (§5).

---

## §1 What shipped — §B(1), the loud unresolvable ref (§10-J, HIGH)

**New `lib/registry.ts`:** a registry-census resolver for explain surfaces. Walks A1 to completeness (opaque cursors echoed, never constructed; bounded 4×500 — past the bound it declares itself incomplete). Resolution: `named` (registry name, C8) · `known` · `dangling` (**claimed ONLY on a complete census**) · `unverified` (no claim). The honesty cuts both ways: a partial census never accuses.

**`CausalChain.tsx` + `format.ts`:** every entity ref the hero renders (trigger subject, action targets, condition observedState, AND the L1 headline) now resolves against the census. A dangling ref renders **LOUD**: the **named ULID verbatim** (never prettified — the raw id is what correlates with the log), the phrase **"not in this hub's registry"**, error tone + `!` marker + a failing **"Not in registry"** pill (color+shape+text, §3a/CVD), and a calm one-line explanation. Wired in `RunChainView`. Default resolver = no-claim, so every other call site renders exactly as before.

**Copy centralized + test-locked** (`format.ts` / `format.test.ts`): `UNRESOLVED_REF_PHRASE` / `_PILL` / `_HELP`, `danglingTriggerLine/TargetLine`, `refLabel`. Bonus in-contract fix: where a ref RESOLVES, the surface now prefers the registry display name (C8) over the humanized slug.

**Mock:** new `dangling-ref` scenario — the R-4 exhibit ULID `01KX1PB9AAB4VB3E10BD477TV3` verbatim as a trigger ref foreign to the fleet, plus a ghost target; contract-shaped, validated by `contract.test.ts` like every scenario. Tests: `registry.test.ts` (no-false-accusation laws, cursor echo, bounded walk) + `CausalChain.dangling.test.tsx` (loud render, verbatim ULIDs, neutral-without-census).

**Stopped item:** the EXACT §10-J exhibit surface — WhyNot/Automations (`triggerSummary`: "it fires on state change") — **cannot go loud in-lane**: the frozen non-firing and automations reads carry NO entity refs to check. Filed as CG-1 and stopped, per charter.

## §2 What shipped — §B(2), store-truth Last-reported/Current (§10-G/I)

**§10-I (list "Current"):** the frozen A1 row carries `stale` but NO report time, so "Current" was a freshness claim with zero evidence — and it contradicted the detail ("report time not recorded"). The list now claims **nothing** for `stale:false` (muted em-dash + test-locked title pointing at the device page); `stale:true` still renders the Stale pill (that IS store evidence). Evidence-based list freshness needs CG-3.

**§10-G (detail):** A3 `lastReported` was already consumed; the gap this lane CAN fix is the register. The unreadable-stamp class (the `/state` epoch-seconds dialect — the store HOLDS the row; the wire serves a form the contract says is ISO) no longer renders **"not recorded"** (a false claim): new `lastReportedCell()` + reworded `availabilityEvidence` say **"a report time is on record, but this dashboard cannot read it yet."** Three honest states, one parse (DX-20 held): readable/date-qualified · on-record-but-unreadable · no report at all. No epoch-seconds parsing (the NEW-6 law holds; the dialect fix stays FE-STATE-DIALECT + Core conformance).

## §3 What shipped — §B(3), the device/entity mislabel (§10-H)

`DevicesView`: the column is now **"Entity"** (the rows ARE entities), each row shows the **raw entityId verbatim** in monospace under the display name, and the detail drawer gains an **"Entity ID"** row — the token that greps against the hub's own log lines. What it still cannot do — correlate an entity row to a `device_adopted` line — needs CG-2. Locked by `DevicesView.honesty.test.tsx` ("Entity" header present, "Device" gone, ids verbatim, "Current" unreachable).

## §4 CONTRACT-GAP PROPOSALS (the freeze is not this lane's to lift — all additive, v1.1.2-pattern)

- **CG-1 (unblocks the full §10-J fix — HIGH):** additive optional entity refs on the ref-carrying B3 reads that lack them: `NonFiringExplanation.triggerRef?: SubjectRef | null` (+ optionally `AutomationSummary.components[].ref?: SubjectRef | null`). With it, WhyNot/Automations run the same census check and the exact R-4 concealment ("it fires on state change" over a dangling ref) renders loud. Until then that surface CANNOT verify what `triggerSummary` names. **Stopped in-lane.**
- **CG-2 (§10-H's second half — MED):** additive optional `deviceId?: string` on A1/A2/A3 entity reads (the registries are projections; `entity_registered` carries provenance). Enables entity-row → `device_adopted` correlation.
- **CG-3 (§10-I's second half — MED):** additive optional `lastReported?: string | null` on A1 rows, so the LIST can render evidence-based freshness ("Current · 2 min ago") instead of the no-claim em-dash now shipped.

**Core-side observation (not a contract gap — routed, not fixed here):** §10-G's rig evidence ("Available", empty Last reported, store holds `availability_changed` + `state_reported`) is a READ-path population/dialect gap on Core's side of A3; the FE renders whatever conformant value A3 serves. Rides the existing F-V2/state-dialect family.

## §5 Notes for the audit

- **Brand fence (G-2):** zero brand strings added; all new copy is product-name-free.
- **Mock-vs-deploy:** the census walk + loud render are live-code paths; the `dangling-ref` scenario exercises them mock-side. Real-wire exercise per H8 = open the run page on a rig with foreign refs (the R-4 clone rig is the natural instrument) and confirm the loud row; the WhyNot half stays structurally unexercisable until CG-1.
- **Cost:** one extra polled read family (A1 census on the run page only), coalesced on the existing single poll loop; bundle 64.3 KB (35.7 KB headroom).

## §6 Next recommended WU

**FE-STATE-DIALECT (charter item (h))** stays the highest-leverage FE row (it closes the §10-G unreadable class at the root once Core conforms), with the CG-1 fold as a fast-follow if ruled. The refuse-to-close rule is satisfied: next WU named.

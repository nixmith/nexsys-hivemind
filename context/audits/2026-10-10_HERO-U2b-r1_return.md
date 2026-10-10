## §0 HERO-U2b-r1 return — verify GREEN
`date -u` Sat Oct 10 12:37:05 UTC 2026 · HEAD `2b4be09` · start 25 = 18 M + 7 ??. Gate RAN on a /tmp copy (node 22.23.2). Limit: no screen, no wire, no git write.
```diff
--- a/scripts/contract-check.mjs
+++ b/scripts/contract-check.mjs
@@ -22 +22,5 @@
-const EXPECTED_VERSION = 'v1.1.5-2026-09-19';
+// v1.1.6 (LINK-READ-2; landed core-side 2026-10-03 J1 df2bc62; the FE mirror is HERO-U2b, 2026-10-09): THREE
+// ADDITIVE optional-nullable keys on ONE read — A1 entities[].availabilityReason · lastSeenAt · link. The literal
+// homes stay FIVE (contract.ts · contract.test.ts · v113-additive.test.ts · v114-additive.test.ts · this file);
+// v115-additive.test.ts and v116-additive.test.ts assert the pin by pattern. They move together (HERO-U2b-r1).
+const EXPECTED_VERSION = 'v1.1.6-2026-10-09';
--- a/eslint.config.js
+++ b/eslint.config.js
@@ -32 +32,3 @@
-     * src/lib/i18n.ts. Scoped to the six hero SOURCE files only — never the tests, never the catalog.
+     * src/lib/i18n.ts. Scoped to EIGHT SOURCE files only — the six hero files plus the recovery card's two
+     * (HERO-U2b-r1, 2026-10-10, widens the six below to eight per SPEC §11 row 2; both read 0 under the rule;
+     * DevicesView.tsx stays out until its 10 HEAD literals are keyed) — never the tests, never the catalog.
@@ -48,0 +51,2 @@
+      'src/components/RecoveryCard.tsx',
+      'src/lib/recovery.ts',
--- a/design/recovery-card-v1/SPEC.md
+++ b/design/recovery-card-v1/SPEC.md
@@ -142,0 +143,6 @@
+| `recovery.state.notResponding.noTime.label` | Not responding (asked twice, no answer) | L1 label (null arm) | 4.4 | 6 |
+| `recovery.state.notResponding.bare.noTime.label` | Not responding | L1 label (S1 degraded · R4 · reason `leave`; null arm) | frag. | 2 |
+| `recovery.state.notResponding.line.noTime` | Asked twice; nothing came back. | L1 line (null arm) | −0.5 | 3 |
+| `recovery.state.left.line.noTime` | This device left the network. | L1 line (reason `leave`; null arm) | 2.9 | 5 |
+
+Amended 2026-10-10 (HERO-U2b-r1; the v103 intake): the four null-arm keys §3 names in words; 63 rows.
```
- **Gates** (`npm run verify` exit 0): tokens:check OK · eslint 0 · tsc 0 · vitest 32 / 682 / 6 todo · build ✓ · bundle 77.2 / 100 KB · contract-check ✓ 11 endpoints, v1.1.6-2026-10-09 (✗ v1.1.5 before).
- **md5** equal both sides: `84320a7a021d` · `cfd85e01943a` · `753b13d3c557`; host sizes equal.
- **Census** `git status --porcelain -- web-ui/dashboard` (lock-free): 28 = 21 M + 7 ?? (the 25 + these 3).
- Lint: ON for both, OFF for DevicesView (10 hits if added); a stdin sentence → 1 error.
- §7 = catalog: 63 = 63, 0 mismatches. Level/Words by §7's method, reverse-derived (52/59 · 58/59 cells; `;` ends a sentence: row 3 = 3 words).
- REPO-COMPLETE, LIVE-VERIFICATION PENDING. Next: the landing card, then the S2 card on the wire.
RETURNED nexsys-hivemind/context/audits/2026-10-10_HERO-U2b-r1_return.md 2989

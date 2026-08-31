<!--
file: context/instructions/2026-08-30_PKG-SEC-2_zigbee-schema-admission_charter.md
purpose: PKG-SEC-2 CHARTER (not yet an instruction) — close R-4's C-1: the shipped config schema does not admit `integrations.zigbee`, so the service boots with "Configuration issue [WARNING] ... not defined in the schema and the schema does not allow additional properties" ON EVERY START and runs on a WARNING. Chartered v59 beat 5 from the R-4 record; the design ruling lands at R-10 (or earlier at Nick's word), then this becomes a coding instruction.
audience: the R-10 sitting · the hub
status: CHARTERED — NOT DISPATCHED. Evidence: context/audits/2026-08-30_R4_re-rep_operator-record.md (C-1; permit_join semantics confirmed at the instrument: key present ⇒ opened duration=254s; absent ⇒ never opens).
-->

# PKG-SEC-2 charter — admit the zigbee integration config into the schema

The question is NOT "silence the warning" — it is which contract is true: (a) the schema admits an `integrations.*` subtree (schema-per-integration files, Doc 06's shape to verify); (b) the zigbee block joins the core schema explicitly; (c) `additionalProperties` carve-out for `integrations` (weakest — validates nothing). A boot-time WARNING on every start trains operators to ignore warnings — the F-S19 cousin in config space. Grounding read-set for the ruling: Doc 06 (configuration system) §schemas · `core/configuration/MODULE_CONTEXT.md` · the shipped schema file + the loader's issue-reporting path · the real config root measured at R-4 (`/var/lib/homesynapse/config/` + `integrations/zigbee.yaml` via include — D-f: the packet-era `/etc/...` path DOES NOT EXIST). Size guess: one small coding WU once ruled; zero Java is NOT guaranteed (the schema may live in resources). The R-4 deviation D-f also owes the ops-docs a path correction sweep — fold it into this WU's census when ruled.

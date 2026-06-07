<!--
file: context/assessments/2026-06-07_M5-D_sd_notify_transport_decision_matrix_OR-M13-SDNOTIFY.md
purpose: M5-D evidence lane — decision matrix + PM recommendation for the real sd_notify AF_UNIX-datagram transport mechanism (deferred to M13 behind the NotifyTransport seam). Compares a JNR/JNA native binding vs a systemd-notify subprocess fallback (and the FFM/Panama JDK-native option), with the GraalVM native-image entanglement flagged explicitly. Informs M13 + the M5-D evidence call. No catalog dependency added now.
audience: Nick, PM, Coder (at M13)
update-cadence: once (matrix), revisited at M13 with the GraalVM spike result
state-type: decision-support
status: MATRIX + RECOMMENDATION READY — final mechanism committed at M13, gated on the M5-D GraalVM spike. Independently reviewed 2026-06-07 (separate agent, adversarial re-derivation vs source incl. the actual SystemdHealthReporter.java) → RATIFY-WITH-EDITS; the citation fix folded.
last-verified: 2026-06-07 against OR-M13-SDNOTIFY (pm-handoff), the M5-A coder pushback (coder-handoff / cross-agent-notes 2026-06-06), Doc 15 (zero-new-deps at MVP), and the language-replatform assessment §1.2/§3/§4.1 (GraalVM native-image / FFM).
guardrail: Decision-support only. No libs.versions.toml entry, no subprocess call, no code is added by this artifact. The NotifyTransport seam (shipped in M5-A) holds the choice open until M13.
-->

# M5-D — sd_notify Transport Mechanism: Decision Matrix + Recommendation (OR-M13-SDNOTIFY)

**Lane:** M5-D (evidence). **Author:** PM. **Decision point:** M13 (composition root constructs the reporter + resolves `$NOTIFY_SOCKET`). **Status:** matrix + recommendation ready; **final mechanism committed at M13, gated on the M5-D GraalVM native-image spike** (the entanglement, §4).

---

## 1. The problem (why there's a decision at all)

`SystemdHealthReporter` (shipped in M5-A, committed `8028337`) speaks the sd_notify protocol — `READY=1` / `WATCHDOG=1` / `STOPPING=1` / `STATUS=…` datagrams to the `$NOTIFY_SOCKET` AF_UNIX address (with `@`→NUL abstract-socket handling). The protocol semantics, READY-once, thread-safety, and send-and-forget WARN-on-fail are **fully implemented and unit-tested** behind a package-private `NotifyTransport` seam.

**But pure OpenJDK 21 cannot open the socket sd_notify needs.** sd_notify is an **AF_UNIX `SOCK_DGRAM`** protocol; JEP 380 (Unix-domain sockets, JDK 16) delivered Unix-domain **stream** sockets only — `DatagramChannel.open(StandardProtocolFamily.UNIX)` **compiles but throws `UnsupportedOperationException` at runtime** (verified by the M5-A Coder pushback; the real `UnixDatagramTransport` now throws a clear "deferred to M13" `IllegalStateException`). So the production transport is **non-functional on a stock-JDK Tier-1 host** — correct-shaped, never wired. This is **OR-M13-SDNOTIFY** (pm-handoff), severity LOW–MEDIUM: a *functional Tier-1 systemd health reporter* needs a real transport, but **no MVP consumer is blocked** until on-device Tier-1 deployment, and M5-A ships the contract correctly behind the seam (compile + unit tests GREEN).

**This artifact picks the mechanism that fills the seam at M13.** It does **not** add a dependency or write code now (out of scope; the brief is explicit).

---

## 2. What the transport must actually do (small surface — this matters for the recommendation)

The job is tiny: **send a short, fixed-format datagram to a known AF_UNIX address, fire-and-forget.** No receive, no streaming, no framing beyond the newline-joined `KEY=value` body. Concretely the real transport needs three libc operations (or their equivalent): `socket(AF_UNIX, SOCK_DGRAM, 0)`, address the `$NOTIFY_SOCKET` path (handling the `@`→`\0` abstract-namespace case), and `sendto()` / `connect()`+`send()`. That's it. **A heavyweight FFI library for three syscalls is a poor cost/benefit** — keep this in mind reading the matrix.

---

## 3. The decision matrix

Four options (the two the brief names, the FFM/Panama option due-diligence requires, and the do-nothing baseline M5-A already chose):

| Dimension | **(a) JNR/JNA native binding** | **(b) `systemd-notify` subprocess** | **(a′) FFM / Panama (JDK-native binding)** | **(0) Keep the seam, defer (M5-A status quo)** |
|---|---|---|---|---|
| **How it works** | A native-call library (JNR-FFI or JNA) binds libc `socket`/`sendto` to send the datagram in-process | `ProcessBuilder` forks `systemd-notify --ready/--status=…` (or `busctl`) per notification | JDK's Foreign Function & Memory API calls libc `socket`/`sendto` in-process — zero external lib | Real transport throws "deferred to M13"; reporter exercised only via the test seam |
| **New dependency?** | **YES** — a `libs.versions.toml` entry + **PM approval** (JNR-FFI or JNA + jnr-posix). Violates Doc 15's "zero new deps at MVP" spirit for a 3-syscall job | **No** Java dep — but a **runtime dependency on the `systemd` CLI** being installed + on `PATH` | **No external dep** — FFM is in the JDK (`java.lang.foreign`) | None |
| **GraalVM native-image (THE entanglement, §4)** | **Worst.** JNR/JNA are reflection- and dynamic-proxy-heavy; native-image needs reachability metadata, and JNA's bundled native stub is historically painful under closed-world. Adds config burden to the very C15 spike | **Cleanest.** `ProcessBuilder` is pure-Java, no reflection/JNI → **closed-world-safe** with no config | **Good.** FFM downcalls are supported under native-image with a small config; GraalVM's strategic interop direction | Trivially clean (no native path) |
| **JDK constraint** | Works on Java 21 | Works on Java 21 | **FFM is preview on Java 21 (`--enable-preview`)**; final in **Java 22** (LTD-01 is Java 21 — a version-trajectory question) | Works on Java 21 |
| **Pi-4 runtime cost** | In-process syscall — **negligible** | **fork+exec per notification.** Fine for one-shot `READY`/`STOPPING`; **poor if WATCHDOG keepalives are frequent** (§5) — process churn on a constrained Pi | In-process syscall — **negligible** | None (non-functional) |
| **Watchdog-PID correctness** | Sends from the main JVM PID → correct for `WATCHDOG`/`$MAINPID` | **Caveat:** the subprocess has its **own PID** → systemd may reject the message unless `NotifyAccess=all` (security-loosening) **and** `--pid=$MAINPID` is passed to attribute it to the service | Sends from the main JVM PID → correct | n/a |
| **Robustness / failure mode** | Library-version + platform-ABI risk; one more native surface to maintain | Fragile: depends on the CLI existing, `PATH`, exec permissions; failures are stringly-typed | Stable JDK API; ABI-correct via libc; small hand-written downcall stubs | Always "fails" closed (never sends) — only acceptable pre-Tier-1 |
| **Testability** | Hard to unit-test the real path (still needs the seam) | Can assert the exec invocation; real behavior needs an integration host | Real path testable on Linux CI; seam still used for unit isolation | Already done (seam captures bytes, asserts once-semantics + thread-safety) |
| **Maintenance burden** | A native-binding dependency for 3 syscalls — high relative to value | Low code, but operationally brittle | Low-moderate (hand-written FFM stubs), zero deps, JDK-blessed | Zero (until M13) |

---

## 4. The GraalVM native-image entanglement (the explicit flag the brief requires)

**The mechanism choice cannot be made independently of the GraalVM native-image decision** — that is the entanglement OR-M13-SDNOTIFY names, and it is live because the **M5-D GraalVM native-image spike (C15)** is running *in the same lane*.

From the language-replatform assessment (`context/assessments/2026-06-06_core-language-replatform-assessment.md`):

- GraalVM native-image is the **endorsed in-Java lever** for the <512 MB footprint (W3, INV-PR-02) and cold-start (W4) — Option A, the recommended path (§1.2, §3, §6). It is likely to be adopted.
- Its cost is **closed-world compilation**: "closed-world/reflection configuration … and the integration runtime's dynamic-loading ambitions (LTD-17) interact awkwardly with closed-world compilation — these must be **spiked, not assumed**" (§3, Option A). The C15 spike explicitly asks "does closed-world compilation survive the integration runtime's dynamic-loading needs?" (§6).
- **FFM/Panama is the assessment's named modern native-interop direction** (§1.2 "FFM/Panama … ~2× faster"; §2.3 "Rust behind FFM/Panama, or Java with a vetted library"), and it has **first-class native-image support** — a materially better closed-world story than JNR/JNA.

**Therefore:**

- If **GraalVM native-image is adopted** (likely): **JNR/JNA becomes the most expensive option** (reflection metadata + JNA's fiddly native-image story) for a 3-syscall job, while **the subprocess (b) is closed-world-clean** and **FFM (a′) is closed-world-friendly and strategically aligned**.
- If **GraalVM is *not* adopted**: the closed-world penalty on JNR/JNA disappears, but JNR/JNA still costs a dependency + approval for a tiny job, so it remains hard to justify versus FFM (zero-dep) or subprocess (zero-dep).

Either way, **JNR/JNA is dominated.** The live variable is **FFM vs subprocess**, and that turns on (1) the GraalVM decision, (2) the JDK-version trajectory (FFM preview on 21 / final on 22), and (3) whether systemd **WatchdogSec** keepalives are used (§5).

---

## 5. The refinement the matrix turns on — do we use the systemd watchdog?

The subprocess option's only real cost is **process-per-heartbeat**. That cost is **conditional on whether the service opts into the systemd watchdog**:

- **READY/STOPPING only** (one-shot lifecycle notifications, sent ~twice per service lifetime): subprocess fork cost is **negligible**, the watchdog-PID caveat largely doesn't apply (no `WATCHDOG`), and **(b) becomes very attractive** — zero deps, closed-world-clean, trivial.
- **WATCHDOG keepalives enabled** (periodic `WATCHDOG=1` at a `WatchdogSec`-derived interval — typically seconds to tens of seconds, occasionally sub-second): subprocess **fork+exec every interval** is real churn on a Pi-4 **and** trips the `--pid`/`NotifyAccess=all` caveat — **(b) becomes poor**, and an **in-process** transport (FFM, or JNR/JNA) is strongly preferred.

So **before M13, decide whether HomeSynapse uses the systemd hardware/software watchdog** (a Doc 12 lifecycle/deployment choice). That single decision largely settles FFM-vs-subprocess.

---

## 6. PM recommendation

**Primary: defer the final commit to M13, gated on the M5-D GraalVM spike result + the watchdog decision (§5) + the JDK-version trajectory. The `NotifyTransport` seam (already shipped) is the correct holding pattern — do not pre-commit a mechanism now, and do not add a catalog dependency now.**

**Provisional lean (to carry into the M13 instruction, re-confirmed against the spike):**

1. **Reject JNR/JNA** as the default. It is the only option that is *both* a new governed dependency (catalog entry + approval) *and* the worst GraalVM-native-image fit — for a 3-syscall fire-and-forget job. Reserve it only as a fallback if FFM is somehow unavailable and an in-process transport is required (i.e., watchdog keepalives + still on Java 21 + FFM-preview disallowed).
2. **If WATCHDOG keepalives are NOT used (READY/STOPPING only):** prefer the **`systemd-notify` subprocess (b)** — zero dependency, closed-world-clean (GraalVM-safe regardless of the spike), trivial. Lowest-risk path to a functional Tier-1 reporter.
3. **If WATCHDOG keepalives ARE used, or an in-process transport is wanted regardless:** prefer **FFM/Panama (a′)** — zero external dependency, in-process (no per-heartbeat fork, correct `$MAINPID`), native-image-friendly, and the strategically-aligned interop direction. Adopt it once the project is on **Java 22+** (FFM final) or is willing to run `--enable-preview` on Java 21 for this narrow surface (a small, contained use — three libc downcalls).
4. **No catalog dependency, no subprocess call, no code** is added in M5-D. The seam holds.

**Decision tree for M13:**

```
GraalVM native-image adopted?  ──┐
JDK ≥ 22 (FFM final) or --enable-preview acceptable?  ──┤
Systemd WATCHDOG keepalives used?  ──┘
                                   │
   WATCHDOG keepalives?  ── NO ───────────────────────────────►  (b) systemd-notify subprocess   [zero-dep, closed-world-clean]
                          └─ YES ─► in-process needed
                                     │
                                     ├─ FFM available (JDK 22+ or preview OK) ─►  (a′) FFM/Panama   [zero-dep, native-image-friendly, in-process]
                                     └─ FFM NOT available ───────────────────►  (a) JNR/JNA        [LAST RESORT: catalog entry + approval + native-image config]
```

---

## 7. What this informs / writes into (no Doc 15 / no code touched)

- **OR-M13-SDNOTIFY (pm-handoff):** updated resolution path — the mechanism is now matrixed and recommended; **closed when a working transport ships at M13 + a Tier-1 sd_notify integration test passes on-device** (unchanged closure condition). Carry this matrix's recommendation into the **M13 coding instruction**.
- **The M5-D evidence call (GraalVM spike, C15):** the spike should **explicitly report** whether JNR/JNA-class reflection/JNI bindings survive its closed-world config — that result confirms or revises the §4 entanglement and the §6 lean. The sd_notify mechanism is one concrete test case for the closed-world question the spike already asks.
- **A pre-M13 decision to surface to Nick:** **does HomeSynapse opt into the systemd watchdog (WatchdogSec)?** (§5) — a Doc 12 lifecycle/deployment choice that largely settles FFM-vs-subprocess. Flag it; it is not decided here.
- **No `libs.versions.toml` entry is proposed now.** If the M13 decision lands on JNR/JNA (the last-resort branch), *that* is when the catalog entry + approval are requested — not before.

---

## Appendix — source citations

- **The runtime gap:** M5-A Coder technical pushback (coder-handoff "DEFERRED/RESOLVED — M5-A" + cross-agent-notes 2026-06-06): JEP 380 = Unix-domain *stream* only; `DatagramChannel.open(UNIX)` throws `UnsupportedOperationException`; the `NotifyTransport` seam + the M13 deferral. PM ruling ACCEPTED (pm-handoff 2026-06-07): mechanism folds into M5-D, entangled with GraalVM; no non-catalog dep / subprocess added.
- **OR-M13-SDNOTIFY:** pm-handoff Open Risks (severity, owner PM/Coder, closure condition; "JNR/JNA native binding vs systemd-notify subprocess … resolved with the M5-D evidence (entangled with the native-image spike)").
- **GraalVM / FFM entanglement:** `context/assessments/2026-06-06_core-language-replatform-assessment.md` §1.2 (W3/W4; GraalVM footprint/cold-start; FFM ~2× faster), §3 Option A ("closed-world/reflection configuration … dynamic-loading … must be spiked, not assumed"), §4.1 (GraalVM native-image numbers), §6 (the C15 native-image spike question; Path-A recommendation).
- **Zero-new-deps-at-MVP value:** Doc 15 §3.8 / §16 ("Dependencies: Zero new at MVP").
- **Watchdog protocol facts:** sd_notify(3) — `WATCHDOG=1` keepalives, `$MAINPID` attribution, `NotifyAccess`, `--pid` (systemd `systemd-notify` man page).

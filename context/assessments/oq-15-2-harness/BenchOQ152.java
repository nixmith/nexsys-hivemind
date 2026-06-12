/*
 * BenchOQ152 — OQ-15-2 AES-256-GCM write-path microbench (SPIKE — lives on the
 * Pi only; archived in nexsys-hivemind/context/assessments/oq-15-2-harness/).
 *
 * Zero-dependency (java.base only: javax.crypto + java.security). Measures the
 * Doc 15 §3.2 write-path encrypt step as a pure function, per microbench spec
 * §3.A: per-event cipher.init(ENCRYPT, dek, GCMParameterSpec(128, nonce)) +
 * doFinal over the REAL codec-serialized payload bytes, with the §3.4
 * deterministic 96-bit counter nonce (NEVER random; no SecureRandom on the
 * hot path). AES-256 (32-byte DEK), 128-bit tag.
 *
 * JMH-deviation note (recorded in §8): protocol is SampleTime-equivalent —
 * per-op nanoTime samples into preallocated arrays, 5 warmup + 10 measurement
 * batches in-process, >=3 separate JVM forks via the driver script, blackhole
 * sink to defeat DCE. At 10–130 µs/op, nanoTime granularity (~tens of ns) is
 * <0.5% of the measurand.
 *
 * Modes:
 *   warm <opsPerBatch> <file>...  — steady-state percentiles per payload file
 *   cold <file>                   — first-100-ops latency from a fresh JVM (§3.A cold)
 *   sha  <opsPerBatch> <file>...  — SHA-256 chain-hash cost (§3.C context):
 *                                   digest over 32-byte prev-hash || payload
 *
 * Output: human table + machine-parseable lines:
 *   RESULT:<mode>:<file>:<sizeB>:mean_us=..:p50_us=..:p90_us=..:p99_us=..:p999_us=..:min_us=..:max_us=..
 */
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.MessageDigest;
import java.security.SecureRandom;
import java.util.Arrays;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public final class BenchOQ152 {

    private static final int WARMUP_BATCHES = 5;
    private static final int MEASURE_BATCHES = 10;
    private static final int COLD_OPS = 100;
    private static final int SCOPE_SALT = 0x4F513152; // "OQ1R" — fixed 4-byte scope salt

    /** Blackhole — volatile sink defeats dead-code elimination. */
    private static volatile long sink;

    private final SecretKey dek;
    private final Cipher cipher;          // one instance, re-init per op (production shape)
    private final byte[] nonce = new byte[12];
    private long counter;                 // §3.4 deterministic counter nonce

    private BenchOQ152() throws Exception {
        byte[] keyBytes = new byte[32];   // AES-256 — SecureRandom ONCE, off the hot path
        new SecureRandom().nextBytes(keyBytes);
        this.dek = new SecretKeySpec(keyBytes, "AES");
        this.cipher = Cipher.getInstance("AES/GCM/NoPadding");
        ByteBuffer.wrap(nonce).putInt(SCOPE_SALT);
    }

    /** The operation under test: assemble counter nonce, re-init, doFinal. */
    private byte[] encryptOnce(byte[] plaintext) throws Exception {
        ByteBuffer.wrap(nonce, 4, 8).putLong(counter++);
        cipher.init(Cipher.ENCRYPT_MODE, dek, new GCMParameterSpec(128, nonce));
        return cipher.doFinal(plaintext);
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.err.println("usage: BenchOQ152 warm|sha <opsPerBatch> <file>...  |  BenchOQ152 cold <file>");
            System.exit(2);
        }
        String mode = args[0];
        switch (mode) {
            case "warm" -> runBatched(false, Integer.parseInt(args[1]), Arrays.copyOfRange(args, 2, args.length));
            case "sha"  -> runBatched(true,  Integer.parseInt(args[1]), Arrays.copyOfRange(args, 2, args.length));
            case "cold" -> runCold(args[1]);
            default -> { System.err.println("unknown mode: " + mode); System.exit(2); }
        }
        System.out.println("sink=" + sink); // keep the blackhole observable
    }

    private static void runBatched(boolean sha, int opsPerBatch, String[] files) throws Exception {
        for (String f : files) {
            byte[] payload = Files.readAllBytes(Path.of(f));
            BenchOQ152 bench = new BenchOQ152();
            MessageDigest digest = sha ? MessageDigest.getInstance("SHA-256") : null;
            byte[] prevHash = new byte[32];
            long[] samples = new long[MEASURE_BATCHES * opsPerBatch];
            int idx = 0;
            for (int b = 0; b < WARMUP_BATCHES + MEASURE_BATCHES; b++) {
                boolean record = b >= WARMUP_BATCHES;
                for (int i = 0; i < opsPerBatch; i++) {
                    long t0 = System.nanoTime();
                    byte[] out;
                    if (sha) {
                        digest.update(prevHash);
                        digest.update(payload);
                        out = digest.digest();
                    } else {
                        out = bench.encryptOnce(payload);
                    }
                    long t1 = System.nanoTime();
                    consume(out);
                    if (sha) prevHash = out;
                    if (record) samples[idx++] = t1 - t0;
                }
            }
            report(sha ? "sha" : "warm", f, payload.length, Arrays.copyOf(samples, idx));
        }
    }

    private static void runCold(String file) throws Exception {
        byte[] payload = Files.readAllBytes(Path.of(file));
        BenchOQ152 bench = new BenchOQ152();
        long[] samples = new long[COLD_OPS];
        for (int i = 0; i < COLD_OPS; i++) {
            long t0 = System.nanoTime();
            byte[] out = bench.encryptOnce(payload);
            long t1 = System.nanoTime();
            consume(out);
            samples[i] = t1 - t0;
        }
        System.out.printf("cold first op: %.1f us; ops 2-10: ", samples[0] / 1000.0);
        for (int i = 1; i < 10; i++) System.out.printf("%.1f ", samples[i] / 1000.0);
        System.out.println();
        report("cold", file, payload.length, samples);
    }

    private static void consume(byte[] out) {
        long acc = sink;
        for (byte b : out) acc ^= b;
        sink = acc;
    }

    private static void report(String mode, String file, int size, long[] samples) {
        long[] sorted = samples.clone();
        Arrays.sort(sorted);
        double mean = Arrays.stream(samples).average().orElse(0) / 1000.0;
        double p50 = pct(sorted, 50.0), p90 = pct(sorted, 90.0), p99 = pct(sorted, 99.0), p999 = pct(sorted, 99.9);
        double min = sorted[0] / 1000.0, max = sorted[sorted.length - 1] / 1000.0;
        String name = Path.of(file).getFileName().toString();
        System.out.printf("%-6s %-30s %5d B  n=%-6d mean=%8.2f  p50=%8.2f  p90=%8.2f  p99=%8.2f  p99.9=%8.2f  min=%6.2f  max=%8.2f  (us)%n",
                mode, name, size, samples.length, mean, p50, p90, p99, p999, min, max);
        System.out.printf("RESULT:%s:%s:%d:mean_us=%.2f:p50_us=%.2f:p90_us=%.2f:p99_us=%.2f:p999_us=%.2f:min_us=%.2f:max_us=%.2f%n",
                mode, name, size, mean, p50, p90, p99, p999, min, max);
    }

    private static double pct(long[] sorted, double p) {
        int i = (int) Math.ceil(p / 100.0 * sorted.length) - 1;
        return sorted[Math.max(0, Math.min(i, sorted.length - 1))] / 1000.0;
    }
}

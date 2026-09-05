public class Probe {
    public static void main(String[] a) {
        System.out.println("availableProcessors=" + Runtime.getRuntime().availableProcessors()
            + " vtParallelism=" + System.getProperty("jdk.virtualThreadScheduler.parallelism", "(default)")
            + " os=" + System.getProperty("os.name"));
    }
}

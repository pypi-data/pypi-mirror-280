// Import benchmarks
mod bench_count;
use bench_count::count_benches;

// Run all benchmarks
use criterion::criterion_main;
criterion_main!(count_benches);

use criterion::{black_box, criterion_group, Criterion};
use czv;
use czv::Result;
use std::path::PathBuf;

// macro_rules! get_test_files {
//     ( $( $x:expr ),* ) => {
//         {
//             let test_dir = std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("tests/resources/");
//             let mut files = Vec::new();
//             $(
//                 files.push(test_dir.join($x));
//             )*
//             files
//         }
//     };
// }

fn bench_row_count(file_path: PathBuf) -> Result<()> {
    czv::count::row_count(Some(file_path), None, false)?;
    Ok(())
}

fn bench_row_count_group(c: &mut Criterion) {
    let mut group = c.benchmark_group("row_count");
    group.bench_function("fruits.csv", |b| {
        b.iter(|| bench_row_count(black_box("tests/resources/fruits.csv".into())))
    });
    group.bench_function("constituents_altnames.csv", |b| {
        b.iter(|| {
            bench_row_count(black_box(
                "tests/resources/constituents_altnames.csv".into(),
            ))
        })
    });
    group.finish();
}

fn bench_column_count(file_path: PathBuf) -> Result<()> {
    czv::count::column_count(Some(file_path), None)?;
    Ok(())
}

fn bench_column_count_group(c: &mut Criterion) {
    let mut group = c.benchmark_group("column_count");
    group.bench_function("fruits.csv", |b| {
        b.iter(|| bench_column_count(black_box("tests/resources/fruits.csv".into())))
    });
    group.bench_function("constituents_altnames.csv", |b| {
        b.iter(|| {
            bench_column_count(black_box(
                "tests/resources/constituents_altnames.csv".into(),
            ))
        })
    });
    group.finish();
}

criterion_group!(
    count_benches,
    bench_row_count_group,
    bench_column_count_group
);

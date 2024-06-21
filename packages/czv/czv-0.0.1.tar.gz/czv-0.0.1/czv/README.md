# czv

Rust library for [czv](https://github.com/rzmk/czv). czv is a library of CSV-related operations for data engineering and analysis tasks.

## Links

-   czv GitHub repository: <https://github.com/rzmk/czv>
-   Rust: [crates.io/crates/czv](https://crates.io/crates/czv) ([source code](https://github.com/rzmk/czv/tree/main/czv))
-   WebAssembly (JavaScript/TypeScript): [npmjs.com/package/czv-wasm](https://www.npmjs.com/package/czv-wasm) ([source code](https://github.com/rzmk/czv/tree/main/czv-wasm))
-   Python: [pypi.org/project/czv](https://pypi.org/project/czv/) ([source code](https://github.com/rzmk/czv/tree/main/czv-python))

## Usage

To install `czv`, run:

```bash
cargo install czv
```

Let's say we want to print the total number of rows in a 4x3 CSV file `fruits.csv` including the header row:

```rust
use czv::{RowCount, Result};

fn main() -> Result<()> {
    let data = "\
fruits,price
apple,2.50
banana,3.00
strawberry,1.50
";
    let output = RowCount::new()
        .file_data(data)
        .include_header_row(true)
        .execute()?;
    println!("{output}"); // 4
    Ok(())
}
```

When ran, this should be the standard output printed in the terminal:

```console
4
```

## Tests

To run the tests, run:

```bash
cargo test
```

## Benchmarks

To run the benchmarks, run:

```bash
cargo bench
```

For benchmarks we use [criterion.rs](https://github.com/bheisler/criterion.rs).

## License

Licensed under either of

-   Apache License, Version 2.0
    ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
-   MIT license
    ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.

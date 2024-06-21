//! # czv
//!
//! CSV operations library for data engineering/analysis tasks.
//!
//! # Example
//!
//! Let's say we want to print the total number of non-header rows in our data:
//!
//! ```rust
//! use czv::{RowCount, Result};
//!
//! fn main() -> Result<()> {
//!     let data = "\
//! fruits,price
//! apple,2.50
//! banana,3.00
//! strawberry,1.50
//! ";
//!     let output = RowCount::new().file_data(data).execute()?;
//!     println!("{output}"); // 3
//!     Ok(())
//! }
//! ```
//!
//! # Usage
//!
//! It is recommended to use the builder structs rather than functions though both are provided.
//!
//! The builder structs are provided at the top-level for ease of use.
//!
//! For example use the [czv::RowCount](crate::RowCount) struct rather than the [czv::count::row_count](crate::count::row_count) function.
//!
//! # Links
//!
//! - czv GitHub repository: <https://github.com/rzmk/czv>
//! - Rust: [crates.io/crates/czv](https://crates.io/crates/czv) ([source code](https://github.com/rzmk/czv/tree/main/czv))
//! - WebAssembly (JavaScript/TypeScript): [npmjs.com/package/czv-wasm](https://www.npmjs.com/package/czv-wasm) ([source code](https://github.com/rzmk/czv/tree/main/czv-wasm))
//! - Python: [pypi.org/project/czv](https://pypi.org/project/czv/) ([source code](https://github.com/rzmk/czv/tree/main/czv-python))

/// Counting operations including row count and column count.
pub mod count;
#[doc(inline)]
pub use count::{ColumnCount, RowCount};
/// Extract a section of rows.
// pub mod slice;
// #[doc(inline)]
// pub use slice::Slice;

// Error-handling helpers
#[allow(dead_code)]
#[derive(thiserror::Error, Debug)]
#[error("{0}")]
/// Common catch-all error type based on [anyhow::Error].
pub struct CzvError(pub anyhow::Error);

impl From<anyhow::Error> for CzvError {
    fn from(value: anyhow::Error) -> Self {
        value.into()
    }
}

impl From<csv::Error> for CzvError {
    fn from(value: csv::Error) -> Self {
        value.into()
    }
}

/// Common Result type based on [anyhow::Result] and [czv::CzvError](crate::CzvError).
pub type Result<T, E = CzvError> = anyhow::Result<T, E>;

#[macro_export]
#[allow(unused_macros)]
/// Function-like macro you may pass a `&str` to return a [czv::CzvError](crate::CzvError).
///
/// For example:
///
/// ```should_panic
/// use czv::{bail, CzvError, Result};
///
/// fn main() -> Result<()> {
///     bail!("This is an example of an error message using `bail!`.");
/// }
/// ```
#[allow(clippy::crate_in_macro_def)]
macro_rules! bail {
    ($err:expr $(,)?) => {
        return Err(crate::CzvError(anyhow::anyhow!($err)))
    };
}

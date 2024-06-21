use crate::{bail, Result};
use csv::ReaderBuilder;
use std::path::PathBuf;
use typed_builder::TypedBuilder;

/// Returns a count of the total number of rows. Recommended alternative: [`czv::count::RowCount`](crate::count::RowCount).
///
/// See [`czv::count::RowCount`](crate::count::RowCount) for a builder version (recommended) of this function.
///
/// ## Notes
///
/// - Specify whether to include the header row in the count with `include_header_row`.
/// - You may not use `file_path` and `file_data` together, only one may be specified.
///
/// ## Arguments
///
/// * `file_path` - CSV file path (alternative to `file_data`).
/// * `file_data` - CSV file data (alternative to `file_path`).
/// * `include_header_row` - Specify whether to include the header row (first row) in the row count.
pub fn row_count(
    file_path: Option<PathBuf>,
    file_data: Option<String>,
    include_header_row: bool,
) -> Result<usize> {
    let mut rdr = ReaderBuilder::new();

    // file_path
    if let Some(file_path) = file_path {
        rdr.has_headers(!include_header_row);
        return Ok(rdr.from_path(file_path)?.records().count());
    }
    // file_data
    else if let Some(file_data) = file_data {
        rdr.has_headers(!include_header_row);
        return Ok(rdr.from_reader(file_data.as_bytes()).records().count());
    }
    // file_path and file_data were not provided
    else {
        bail!("Could not determine a file path or file data for row_count_builder.");
    }
}

#[derive(TypedBuilder)]
#[builder(doc, builder_method(name=new, doc="Returns a `RowCountBuilder` to customize row count options by running other methods before getting the row count with the `execute` method."), build_method(vis="", name=__build))]
/// Returns a count of the total number of rows.
///
/// The entry point for setting up a [`czv::count::RowCountBuilder`](crate::count::RowCountBuilder) by running [`RowCount::new()`](crate::count::RowCount::new).
///
/// # Example
///
/// Let's say we want to print the total number of non-header rows in our data:
///
/// ```rust
/// use czv::{RowCount, Result};
///
/// fn main() -> Result<()> {
///     let data = "\
/// fruits,price
/// apple,2.50
/// banana,3.00
/// strawberry,1.50
/// ";
///     let output = RowCount::new().file_data(data).execute()?;
///     println!("{output}"); // 3
///     Ok(())
/// }
/// ```
pub struct RowCount {
    #[builder(
        default,
        setter(
            doc = "CSV file path (alternative to `file_data`).",
            strip_option,
            into
        )
    )]
    file_path: Option<PathBuf>,

    #[builder(
        default,
        setter(
            doc = "CSV file data (alternative to `file_path`).",
            strip_option,
            into
        )
    )]
    file_data: Option<String>,

    #[builder(
        default = false,
        setter(
            doc = "Specify whether to include the header row (first row) in the row count. Defaults to false."
        )
    )]
    include_header_row: bool,
}

#[allow(non_camel_case_types)]
impl<
        __include_header_row: typed_builder::Optional<bool>,
        __file_data: typed_builder::Optional<Option<String>>,
        __file_path: typed_builder::Optional<Option<PathBuf>>,
    > RowCountBuilder<(__file_path, __file_data, __include_header_row)>
{
    /// Returns the row count.
    pub fn execute(self) -> Result<usize> {
        let builder = self.__build();
        row_count(
            builder.file_path,
            builder.file_data,
            builder.include_header_row,
        )
    }
}

/// Returns a count of the total number of columns (fields). Recommended alternative: [`czv::count::ColumnCount`](crate::count::ColumnCount).
///
/// See [`czv::count::ColumnCount`](crate::count::ColumnCount) for a builder version (recommended) of this function.
///
/// # Example
///
/// Let's say we want to print the total number of columns in our data:
///
/// ```rust
/// use czv::{ColumnCount, Result};
///
/// fn main() -> Result<()> {
///     let data = "\
/// fruits,price
/// apple,2.50
/// banana,3.00
/// strawberry,1.50
/// ";
///     let output = ColumnCount::new().file_data(data).execute()?;
///     println!("{output}"); // 2
///     Ok(())
/// }
/// ```
///
/// ## Arguments
///
/// * `file_path` - CSV file path (alternative to `file_data`).
/// * `file_data` - CSV file data (alternative to `file_path`).
pub fn column_count(file_path: Option<PathBuf>, file_data: Option<String>) -> Result<usize> {
    let rdr = ReaderBuilder::new();

    // file_path
    if let Some(file_path) = file_path {
        Ok(rdr.from_path(file_path)?.headers()?.len())
    }
    // file_data
    else if let Some(file_data) = file_data {
        return Ok(rdr.from_reader(file_data.as_bytes()).headers()?.len());
    }
    // file_path and file_data were not provided
    else {
        bail!("Could not determine a file path or file data for column_count_builder.");
    }
}

#[derive(TypedBuilder)]
#[builder(doc, builder_method(name=new, doc="Returns a `ColumnCountBuilder` to customize column count options by running other methods before getting the column count with the `execute` method."), build_method(vis="", name=__build))]
/// Returns a count of the total number of columns (fields).
///
/// The entry point for setting up a [`czv::count::ColumnCountBuilder`](crate::count::ColumnCountBuilder) by running [`ColumnCount::new()`](crate::count::ColumnCount::new).
///
/// For example:
///
/// ```rust
/// use czv::{count::ColumnCount, Result};
///
/// fn main() -> Result<()> {
///     let data = r#"fruits,price
/// apple,2.50
/// banana,3.00
/// strawberry,1.50"#;
///     let output = ColumnCount::new().file_data(data).execute()?;
///     println!("{output}"); // 2
///     Ok(())
/// }
/// ```
pub struct ColumnCount {
    #[builder(
        default,
        setter(
            doc = "CSV file path (alternative to `file_data`).",
            strip_option,
            into
        )
    )]
    file_path: Option<PathBuf>,

    #[builder(
        default,
        setter(
            doc = "CSV file path (alternative to `file_path`).",
            strip_option,
            into
        )
    )]
    file_data: Option<String>,
}

#[allow(non_camel_case_types)]
impl<
        __file_data: typed_builder::Optional<Option<String>>,
        __file_path: typed_builder::Optional<Option<PathBuf>>,
    > ColumnCountBuilder<(__file_path, __file_data)>
{
    pub fn execute(self) -> Result<usize> {
        let builder = self.__build();
        column_count(builder.file_path, builder.file_data)
    }
}

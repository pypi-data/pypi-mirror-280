use crate::Result;
use pyo3::pyfunction;
use std::path::PathBuf;

#[pyfunction]
pub fn row_count(
    file_path: Option<PathBuf>,
    file_data: Option<String>,
    include_header_row: Option<bool>,
) -> Result<usize> {
    Ok(czv::count::row_count(
        file_path,
        file_data,
        include_header_row.unwrap_or(false),
    )?)
}

#[pyfunction]
pub fn column_count(file_path: Option<PathBuf>, file_data: Option<String>) -> Result<usize> {
    Ok(czv::count::column_count(file_path, file_data)?)
}

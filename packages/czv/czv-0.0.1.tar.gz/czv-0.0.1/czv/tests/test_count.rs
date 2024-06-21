use czv;
use czv::Result;

#[test]
fn test_row_count() -> Result<()> {
    let cases = vec![
        ("tests/resources/fruits.csv", 3),
        ("tests/resources/constituents_altnames.csv", 33971),
    ];
    for (file_name, expected) in cases {
        let got = czv::count::row_count(Some(file_name.into()), None, false)?;
        assert_eq!(expected, got);
    }
    Ok(())
}

#[test]
fn test_row_count_builder() -> Result<()> {
    let cases = vec![
        ("tests/resources/fruits.csv", 3),
        ("tests/resources/constituents_altnames.csv", 33971),
    ];
    for (file_name, expected) in cases {
        let got = czv::count::RowCount::new().file_path(file_name).execute()?;
        assert_eq!(expected, got);
    }
    Ok(())
}

#[test]
fn test_column_count() -> Result<()> {
    let cases = vec![
        ("tests/resources/fruits.csv", 2),
        ("tests/resources/constituents_altnames.csv", 6),
    ];
    for (file_name, expected) in cases {
        let got = czv::count::column_count(Some(file_name.into()), None)?;
        assert_eq!(expected, got);
    }
    Ok(())
}

#[test]
fn test_column_count_builder() -> Result<()> {
    let cases = vec![
        ("tests/resources/fruits.csv", 2),
        ("tests/resources/constituents_altnames.csv", 6),
    ];
    for (file_name, expected) in cases {
        let got = czv::count::ColumnCount::new()
            .file_path(file_name)
            .execute()?;
        assert_eq!(expected, got);
    }
    Ok(())
}

// use czv;
// use czv::Result;

// #[test]
// fn test_slice() -> Result<()> {
//     let got = czv::Slice::new()
//         .file_path("tests/resources/fruits.csv")
//         .execute()?;
//     let expected = "fruit,price\napple,2.50\nbanana,3.00\nstrawberry,1.50".to_string();
//     assert_eq!(expected, got);
//     Ok(())
// }

// #[test]
// fn test_slice_start_end() -> Result<()> {
//     let cases = vec![(
//         "tests/resources/fruits.csv",
//         1,
//         3,
//         "banana,3.00\nstrawberry,1.50".to_string(),
//     )];
//     for (file_name, start, end, expected) in cases {
//         let got = czv::slice::slice(
//             Some(file_name.into()),
//             None,
//             Some(start),
//             Some(end),
//             None,
//             None,
//             false,
//         )?;
//         assert_eq!(expected, got);
//     }
//     Ok(())
// }

// #[test]
// fn test_slice_start_end_data() -> Result<()> {
//     let cases = vec![(
//         "fruit,price\napple,2.50\nbanana,3.00\nstrawberry,1.50".to_string(),
//         1,
//         3,
//         "banana,3.00\nstrawberry,1.50".to_string(),
//     )];
//     for (file_data, start, end, expected) in cases {
//         let got = czv::slice::slice(
//             None,
//             Some(file_data),
//             Some(start),
//             Some(end),
//             None,
//             None,
//             false,
//         )?;
//         assert_eq!(expected, got);
//     }
//     Ok(())
// }

// #[test]
// fn test_slice_start_0_end_3() -> Result<()> {
//     let expected = "apple,2.50\nbanana,3.00".to_string();
//     let got: String = czv::slice::Slice::new()
//         .file_path("tests/resources/fruits.csv")
//         .start(0)
//         .end(2) // exclusive
//         .include_header_row(false)
//         .execute()?;

//     assert_eq!(expected, got);
//     Ok(())
// }

// #[test]
// fn test_slice_index_2() -> Result<()> {
//     let expected = "strawberry,1.50".to_string();
//     let got: String = czv::slice::Slice::new()
//         .file_path("tests/resources/fruits.csv")
//         .index(2)
//         .include_header_row(false)
//         .execute()?;

//     assert_eq!(expected, got);
//     Ok(())
// }

// #[test]
// fn test_slice_index_override() -> Result<()> {
//     let got = czv::slice::Slice::new()
//         .file_path("tests/resources/fruits.csv")
//         .start(1)
//         .end(3)
//         .index(2)
//         .include_header_row(false)
//         .execute();

//     // Error: CzvError(Cannot use index with start, end, or length.)
//     assert!(got.is_err());
//     Ok(())
// }

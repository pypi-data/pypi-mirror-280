use czv::{Result, RowCount};

fn main() -> Result<()> {
    let data: &str = "\
fruits,price
apple,2.50
banana,3.00
strawberry,1.50
";
    let output: usize = RowCount::new().file_data(data).execute()?;
    println!("{output}"); // 3
    Ok(())
}

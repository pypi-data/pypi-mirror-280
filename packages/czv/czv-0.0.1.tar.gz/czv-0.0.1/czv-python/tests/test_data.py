import pathlib

data_path = pathlib.Path(__file__).parent.resolve().joinpath("data")
test_data = {
    file_name: data_path.joinpath(file_name)
    for file_name in ["fruits.csv", "constituents_altnames.csv"]
}

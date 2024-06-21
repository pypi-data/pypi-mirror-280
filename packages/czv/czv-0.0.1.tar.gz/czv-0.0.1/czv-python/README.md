# czv-python

Python library for [czv](https://github.com/rzmk/czv). czv is a library of CSV-related operations for data engineering and analysis tasks.

## Links

-   czv GitHub repository: <https://github.com/rzmk/czv>
-   Rust: [crates.io/crates/czv](https://crates.io/crates/czv) ([source code](https://github.com/rzmk/czv/tree/main/czv))
-   WebAssembly (JavaScript/TypeScript): [npmjs.com/package/czv-wasm](https://www.npmjs.com/package/czv-wasm) ([source code](https://github.com/rzmk/czv/tree/main/czv-wasm))
-   Python: [pypi.org/project/czv](https://pypi.org/project/czv/) ([source code](https://github.com/rzmk/czv/tree/main/czv-python))

## Installation and example

To install `czv`, run:

```bash
pip install czv
```

Or use [`uv pip`](https://github.com/astral-sh/uv) instead of `pip`.

Let's say we want to print the total number of rows in a 4x3 CSV file `fruits.csv` including the header row:

```python
import czv

output = czv.row_count(file_path="fruits.csv", include_header_row=True)

print(output) # 4
```

## Development

You'll need to have [maturin](https://github.com/PyO3/maturin/) and [uv](https://github.com/astral-sh/uv) installed. Set up a local virtual environment in the `czv-python` folder by running:

```bash
uv venv
```

Make sure to activate the virtual environment (instructions should be provided in your terminal after running the previous command).

Once you've activated the virtual environment, install dependencies by running:

```bash
uv pip install -r requirements.txt
```

### Build package in local environment

```bash
maturin develop --uv --release
```

### Run tests

```bash
pytest
```

### Publishing

To publish to pypi.org run:

```bash
maturin publish
```

"""
# czv

Python library for [czv](https://github.com/rzmk/czv). CSV operations library for data engineering/analysis tasks.

## Install

```bash
pip install czv
```

## Example

```python
import czv

data: str = \"""fruits,price
apple,2.50
banana,3.00
strawberry,1.50\"""

output: int = czv.row_count(file_data=data, include_header_row=True)

print(output) # 4
```

## Links

- czv GitHub repository: <https://github.com/rzmk/czv>
- Rust: [crates.io/crates/czv](https://crates.io/crates/czv) ([source code](https://github.com/rzmk/czv/tree/main/czv))
- WebAssembly (JavaScript/TypeScript): [npmjs.com/package/czv-wasm](https://www.npmjs.com/package/czv-wasm) ([source code](https://github.com/rzmk/czv/tree/main/czv-wasm))
- Python: [pypi.org/project/czv](https://pypi.org/project/czv/) ([source code](https://github.com/rzmk/czv/tree/main/czv-python))

"""

from typing import Optional
from pathlib import Path

def row_count(file_path: Optional[Path], file_data: Optional[str], include_header_row: Optional[bool]) -> int:
    """Returns a count of the total number of rows.
    
    ## Arguments
     
    * `file_path` - CSV file path.
    * `file_data` - CSV file data.
    * `include_header_row` - Specify whether to include the header row (first row) in the row count. Default is false.
    """

def column_count(file_path: Optional[Path], file_data: Optional[str]) -> int:
    """Returns a count of the total number of columns (fields).
    
    ## Arguments
    
    * `file_path` - CSV file path.
    * `file_data` - CSV file data.
    """

import czv
import pytest
from .test_data import test_data

class TestCountFunc:
    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", 3), ("constituents_altnames.csv", 33971)],
    )
    def test_count(self, file_name, expected):
        """Count the total number of non-header rows."""

        result = czv.row_count(file_path=test_data[file_name])
        assert result == expected

    @pytest.mark.parametrize(
        "file_name,expected",
        [("fruits.csv", 4), ("constituents_altnames.csv", 33972)],
    )
    def test_include_header_row(self, file_name, expected):
        """Count the total number of rows including the header row."""

        result = czv.row_count(file_path=test_data[file_name], include_header_row=True)
        assert result == expected

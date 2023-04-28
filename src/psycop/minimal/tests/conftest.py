from pathlib import Path

import pandas
import pytest  # pants: no-infer-dep


@pytest.fixture()
def test_string():
    return "A new test_string!"


@pytest.fixture()
def test_string_from_file():
    # Load test_string from test_string_file.txt
    assert pandas.__version__ != 0

    file_path = Path(__file__).parent / "test_string_file.txt"

    return file_path.read_text()

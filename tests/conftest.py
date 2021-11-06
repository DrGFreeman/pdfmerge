import os
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def test_data():
    """Fixture providing the path to the test data."""
    yield Path("tests/test_data").resolve()


@pytest.fixture(scope="session")
def odd_1_7(test_data):
    """Fixture providing the path to a pdf file of pages 1, 3, 5 & 7."""
    yield test_data / "odd_1-7.pdf"


@pytest.fixture(scope="session")
def even_8_2(test_data):
    """Fixture providing the path to a pdf file of pages 8, 6, 4 & 2."""
    yield test_data / "even_8-2.pdf"


@pytest.fixture(scope="session")
def even_6_2(test_data):
    """Fixture providing the path to a pdf file of pages 6, 4 & 2."""
    yield test_data / "even_6-2.pdf"


@pytest.fixture()
def default_output(tmp_path):
    """Fixture providing the path to the expected default output file in tmp_path for
    each test."""
    yield tmp_path / "merged.pdf"


@pytest.fixture(autouse=True)
def work_in_tmp_path(tmp_path):
    """Autouse fixture to set the working directory to the value of tmp_path for each
    test."""
    os.chdir(tmp_path)

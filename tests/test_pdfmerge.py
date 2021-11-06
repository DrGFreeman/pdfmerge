from pathlib import Path

from pdfminer.high_level import extract_text
import pytest

from pdfmerge import pdfmerge


def text_in_page(text, file, page):
    """Determine if the specified text is in the specified page."""
    return text in extract_text(file, page_numbers=[page])


def test_merge_same_length(odd_1_7, even_8_2, default_output):
    """Test merging two files with same number of pages."""
    pdfmerge(odd_1_7, even_8_2)

    assert all(text_in_page(f"Page {i + 1}", default_output, i) for i in range(8))


def test_merge_different_length(odd_1_7, even_6_2, default_output):
    """Test merging two files with different number of pages."""
    pdfmerge(odd_1_7, even_6_2)

    assert all(text_in_page(f"Page {i + 1}", default_output, i) for i in range(7))


@pytest.mark.parametrize(
    "output_path", ("output.pdf", "dirname/output.pdf", Path("path_output.pdf"))
)
def test_specified_output(tmp_path, odd_1_7, even_8_2, output_path):
    """Test merging into a specificied output file."""
    pdfmerge(odd_1_7, even_8_2, output=output_path)

    out_path_full = tmp_path.joinpath(output_path)
    assert out_path_full.is_file()
    assert all(text_in_page(f"Page {i + 1}", out_path_full, i) for i in range(8))

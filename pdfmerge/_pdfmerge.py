from itertools import zip_longest
from pathlib import Path

from PyPDF3 import PdfFileReader
from PyPDF3 import PdfFileWriter


def pdfmerge(odd, even, output=None):

    odd_path = Path(odd)
    even_path = Path(even)

    if output:
        out_path = Path(output)
    else:
        out_path = Path("merged.pdf")

    out_pdf = PdfFileWriter()

    with odd_path.open("rb") as odd_file, even_path.open("rb") as even_file:

        for odd_page, even_page in zip_longest(
            PdfFileReader(odd_file).pages, reversed(PdfFileReader(even_file).pages)
        ):
            if odd_page:
                out_pdf.addPage(odd_page)

            if even_page:
                out_pdf.addPage(even_page)

        # Ensure the output folder exists
        out_path.parent.mkdir(parents=True, exist_ok=True)

        with out_path.open("wb") as out_file:

            out_pdf.write(out_file)

# pdfmerge
Merge scanned pdf documents of odd and even pages into a single pdf document.

This packages resolves the problem of merging documents of odd and even pages resulting from scanning documents to pdf with a scanner loader that does not support double sided scanning:

1. Scan odd pages into `odd.pdf` (e.g. pages 1, 3, 5 & 7).
1. Flip the document over and scan even pages into `even.pdf`. This will scan the even pages in reverse order (e.g. pages 8, 6, 4 & 2).
1. Combine the odd and even pages with `pdfmerge odd.pdf even.pdf [merged.pdf]`.

## Installation

This packages uses the `pdftk` linux tool. On Ubuntu >= 18.10, it can be installed with `sudo apt install pdftk`.

Install the package from git using pip:

```
python3 -m pip install git+https://github.com/DrGFreeman/pdfmerge.git
```

Python version 3.6 or greater is required.

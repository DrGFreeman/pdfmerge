import sys

from ._pdfmerge import pdfmerge


def run():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: pdfmerge odd.pdf even.pdf [merged.pdf]")
    else:
        pdfmerge(*sys.argv[1:])


if __name__ == "__main__":
    run()

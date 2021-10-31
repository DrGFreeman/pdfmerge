from setuptools import find_packages
from setuptools import setup

setup(
    name="pdfmerge",
    version="0.1.0.dev",
    packages=find_packages(),
    entry_points={"console_scripts": ["pdfmerge=pdfmerge.__main__:run"]},
    python_requires=">=3.6",
)

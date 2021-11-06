import nox

test_reqs = ["pytest", "pytest-cov", "pdfminer.six"]


@nox.session(python="3.10")
def lint(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=["3.6", "3.7", "3.8", "3.9", "3.10"])
def tests(session):
    session.install(".", *test_reqs)
    session.run("pytest", "-v", "--cov", "--cov-report", "term-missing")

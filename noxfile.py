import tempfile

import nox
from nox_poetry import session

nox.options.sessions = "lint", "safety", "tests"
locations = "src", "tests", "noxfile.py"


@session(python=["3.10", "3.8"])
def tests(session):
    session.install("pytest", "coverage[toml]", "pytest-cov", ".")
    session.run("pytest", "--cov")


@session(python=["3.10", "3.8"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8", "flake8-bandit", "flake8-black", "flake8-bugbear", "flake8-isort"
    )
    session.run("flake8", *args)


@session(python="3.10")
def black(session):
    args = session.posargs or locations
    args += ("--extend-exclude", "day_template")
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")

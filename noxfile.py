"""Nox sessions."""
import tempfile

import nox
from nox.sessions import Session
import nox_poetry

locations = "src", "tests", "noxfile.py"
nox.options.sessions = (
    "lint",
    "mypy",
    "safety",
    "tests",
)


@nox.session
def unit_tests(session: Session) -> None:
    """Run the unit test suite."""
    args = session.posargs
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(
        session,
        "pytest",
        "requests-mock",
        "pytest-mock",
    )
    session.run(
        "pytest",
        "-m unit",
        "-rA",
        *args,
        env={
            "ALTINN_URI": "altinn-uri",
            "MONGO_USERNAME": "admin",
            "MONGO_PASSWORD": "admin",
        },
    )


@nox.session
def integration_tests(session: Session) -> None:
    """Run the integration test suite."""
    args = session.posargs
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(
        session,
        "pytest",
        "pytest-docker",
        "requests-mock",
        "pytest-mock",
    )
    session.run(
        "pytest",
        "-m integration",
        "-rA",
        *args,
        env={
            "ALTINN_URI": "http://localhost:8000",
            "MONGO_USERNAME": "admin",
            "MONGO_PASSWORD": "admin",
        },
    )


@nox.session
def tests(session: Session) -> None:
    """Run the integration test suite."""
    args = session.posargs or ["--cov"]
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(
        session,
        "coverage[toml]",
        "pytest",
        "pytest-cov",
        "pytest-docker",
        "requests-mock",
        "pytest-mock",
    )
    session.run(
        "pytest",
        "-rA",
        *args,
        env={
            "ALTINN_URI": "http://localhost:8000",
            "ALTINN_MODEL_PUBLISHER_URI": "https://altinn.fellesdatakatalog.digdir.no",
            "ORGANIZATION_CATALOGUE_URI": "https://organization-catalogue.staging.fellesdatakatalog.digdir.no",
            "MONGO_USERNAME": "admin",
            "MONGO_PASSWORD": "admin",
        },
    )


@nox.session
def contract_tests(session: Session) -> None:
    """Run the contract test suite."""
    args = session.posargs
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(
        session, "pytest", "pytest-docker", "requests_mock", "pytest_mock"
    )
    session.run(
        "pytest",
        "-m contract",
        "-rA",
        *args,
        env={
            "ALTINN_URI": "http://wiremock:8080",
            "MONGO_USERNAME": "admin",
            "MONGO_PASSWORD": "admin",
        },
    )


@nox.session
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    nox_poetry.install(session, "black")
    session.run("black", *args)


@nox.session
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    nox_poetry.install(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "pep8-naming",
    )
    session.run("flake8", *args)


@nox.session
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
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
        nox_poetry.install(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    nox_poetry.install(session, "mypy")
    session.run("mypy", *args)


@nox.session
def coverage(session: Session) -> None:
    """Upload coverage data."""
    nox_poetry.install(session, "coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)

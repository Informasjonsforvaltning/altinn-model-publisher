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


@nox_poetry.session
def unit_tests(session: Session) -> None:
    """Run the unit test suite."""
    args = session.posargs
    session.install(
        ".",
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
            "IS_TEST": "is_test",
        },
    )


@nox_poetry.session
def integration_tests(session: Session) -> None:
    """Run the integration test suite."""
    args = session.posargs
    session.install(
        ".",
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
            "IS_TEST": "is_test",
        },
    )


@nox_poetry.session
def tests(session: Session) -> None:
    """Run the integration test suite."""
    args = session.posargs or ["--cov"]
    session.install(
        ".",
        "coverage[toml]",
        "pytest",
        "pytest-cov",
        "pytest-docker",
        "requests-mock",
        "pytest-mock",
        "pytest-aiohttp",
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
            "API_KEY": "api-test-secret",
            "IS_TEST": "is_test",
        },
    )


@nox_poetry.session
def contract_tests(session: Session) -> None:
    """Run the contract test suite."""
    args = session.posargs
    session.install(".", "pytest", "pytest-docker", "requests_mock", "pytest_mock")
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


@nox_poetry.session
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox_poetry.session
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
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


@nox_poetry.session
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
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox_poetry.session
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox_poetry.session
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)

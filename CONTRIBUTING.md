# Contributing to SpectralGuard

## How to Contribute
1. Fork the repo
2. Create a branch: `git checkout -b feat/your-feature`
3. Install dev deps: `pip install -e ".[dev]"`
4. Run tests: `pytest tests/ --cov=spectral_guard`
5. Submit a PR with a clear description

## Development Setup
Ensure you have Python 3.10+ installed. We recommend using a virtual environment.

## Running Tests
All pull requests must pass the core test suite. We use `pytest` for unit and integration testing.

## Code Style
We enforce strict formatting using `Black` and `Ruff`.

## Adding a New Domain Profile
To add a new domain profile (e.g., beyond Energy, Finance, Healthcare, Aerospace), implement the `DomainProfile` interface in the SG-BenchGen module.

## Reporting Issues
Please use the GitHub Issue tracker. Provide a minimal reproducible example if reporting a bug.
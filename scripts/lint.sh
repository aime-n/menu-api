#!/bin/bash
# Runs code quality checks (ruff, black, isort)
set -euxo pipefail

echo "Running type checking..."
poetry run mypy --ignore-missing-imports app/

echo "Running code formatting check..."
poetry run black --check app/ tests/

echo "Running import sorting check..."
poetry run isort --check-only app/ tests/

echo "Running Ruff linter..."
poetry run ruff check app/ tests/

echo "All linting checks passed!"
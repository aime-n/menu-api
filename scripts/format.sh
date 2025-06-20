#!/bin/bash
# Formats and fixes code
set -euxo pipefail

echo "Formatting code..."

echo "Sorting imports..."
poetry run isort app/ tests/

echo "Formatting with Black..."
poetry run black app/ tests/

echo "Running Ruff with auto-fix..."
poetry run ruff check --fix app/ tests/

echo "Code formatting completed!" 
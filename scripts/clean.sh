#!/bin/bash
# Removes temporary files and caches
set -euxo pipefail

echo "Cleaning temporary files and caches..."

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true

# Remove test coverage files
rm -rf htmlcov/ .coverage .pytest_cache/ 2>/dev/null || true

# Remove mypy cache
rm -rf .mypy_cache/ 2>/dev/null || true

# Remove ruff cache
rm -rf .ruff_cache/ 2>/dev/null || true

# Remove build artifacts
rm -rf build/ dist/ *.egg-info/ 2>/dev/null || true

echo "Cleanup completed!"

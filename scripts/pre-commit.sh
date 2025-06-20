#!/bin/bash
# Pre-commit hook script - STRICT gatekeeper that prevents commits if checks fail
set -euxo pipefail

echo "PRE-COMMIT CHECKS - This will STOP your commit if any check fails!"

# Check if poetry.lock is up to date
echo "Checking poetry.lock..."
if [ pyproject.toml -nt poetry.lock ]; then
    echo "ERROR: poetry.lock is older than pyproject.toml"
    echo "Run 'poetry lock' to update it"
    exit 1
fi

# Check code quality (strict - no auto-fix)
echo "Checking code quality..."
make lint

# Run tests
echo "Running tests..."
make test

echo "All pre-commit checks passed! You can now commit safely." 
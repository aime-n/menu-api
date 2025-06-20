#!/bin/bash
# Done script - cleanup and summary after development session (informational only)
set -euxo pipefail

echo "DONE SCRIPT - Cleanup and summary (warnings only, won't stop anything)"

# Check if poetry.lock is up to date (warning only)
echo "Checking poetry.lock..."
if [ pyproject.toml -nt poetry.lock ]; then
    echo "WARNING: poetry.lock is older than pyproject.toml"
    echo "Consider running 'poetry lock' to update it"
else
    echo "poetry.lock is up to date"
fi

# Update database if needed (optional - don't fail if it errors)
echo "Updating database..."
if [ -f "./scripts/update_db.sh" ]; then
    ./scripts/update_db.sh || echo "Database update had issues, but continuing..."
else
    echo "update_db.sh not found, skipping database update"
fi

# Clean up any temporary files
echo "Cleaning temporary files..."
make clean

# Format and fix code
echo "Formatting code..."
make format

# Check code quality (informational)
echo "Checking code quality..."
make lint || echo "Some linting issues found, but continuing..."

# Run tests (informational)
echo "Running tests..."
poetry run pytest || echo "Some tests failed, but continuing..."

echo "Done script completed! Your development session is wrapped up."
echo "Remember to run 'make pre-commit' before committing if you want strict checks."
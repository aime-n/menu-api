#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports menu-mvp-api/
poetry run isort --check --diff menu-mvp-api/ tests/
poetry run black --check menu-mvp-api/ tests/
poetry run flake8 menu-mvp-api/ tests/
poetry run safety check -i 39462 -i 40291
poetry run bandit -r menu-mvp-api/

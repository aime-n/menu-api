#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports app/

poetry run black --check app/ tests/
poetry run flake8 app/ tests/
poetry run safety check -i 39462 -i 40291
poetry run bandit -r app/
poetry run mypy app/
poetry run flake8 app/
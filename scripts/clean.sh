#!/bin/bash
set -euxo pipefail

poetry run isort .
poetry run ruff check --fix .

poetry run isort app/ tests/
poetry run black app/ tests/

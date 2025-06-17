#!/bin/bash
set -euxo pipefail

./scripts/lint.sh
poetry run pytest -s --cov=menu-mvp-api/ --cov=tests --cov-report=term-missing ${@-} --cov-report html

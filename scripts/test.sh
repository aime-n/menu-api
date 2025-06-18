#!/bin/bash
set -euxo pipefail

./scripts/lint.sh
poetry run pytest -s

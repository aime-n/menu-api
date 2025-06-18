#!/bin/bash
set -euxo pipefail

poetry run isort app/ tests/
poetry run black app/ tests/

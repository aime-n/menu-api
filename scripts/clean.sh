#!/bin/bash
set -euxo pipefail

poetry run isort menu-mvp-api/ tests/
poetry run black menu-mvp-api/ tests/

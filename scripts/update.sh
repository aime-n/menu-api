#!/bin/bash
set -euxo pipefail

# Atualiza dependências
poetry install

# Formata o código
poetry run isort tests/
poetry run black tests/

# Cria diretório de migrações Alembic se não existir
if [ ! -d "app/db/migrations/versions" ]; then
  poetry run alembic -c alembic.ini init app/db/migrations
fi

# Aplica as migrações pendentes antes de gerar nova revisão
poetry run alembic -c alembic.ini upgrade head

# Gera uma nova revisão Alembic com autogenerate
poetry run alembic -c alembic.ini revision --autogenerate -m "update"

# Aplica as migrações no banco de dados
poetry run alembic -c alembic.ini upgrade head

# Roda os testes automatizados
poetry run pytest
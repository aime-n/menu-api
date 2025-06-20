#!/bin/bash
set -euxo pipefail

# Verifica se há mudanças nos modelos comparando com o banco de dados
echo "Verificando mudanças nos modelos..."

# Gera uma revisão temporária para detectar mudanças
TEMP_REVISION=$(poetry run alembic -c alembic.ini revision --autogenerate -m "temp_check" 2>/dev/null | grep "Generating" | tail -1 | awk '{print $NF}')

if [ -n "$TEMP_REVISION" ]; then
    echo "Mudanças detectadas nos modelos. Atualizando banco de dados..."
    
    # Remove a revisão temporária
    rm -f "app/db/migrations/versions/${TEMP_REVISION}_temp_check.py"
    
    # Gera uma nova revisão com nome apropriado
    poetry run alembic -c alembic.ini revision --autogenerate -m "update"
    
    # Aplica as migrações
    poetry run alembic -c alembic.ini upgrade head
    
    echo "Banco de dados atualizado com sucesso!"
else
    echo "Nenhuma mudança detectada nos modelos. Pulando atualização do banco de dados."
fi


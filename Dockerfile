# filepath: Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Instale Poetry
RUN pip install poetry

# Copie os arquivos do projeto
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

# Exponha a porta padrão do FastAPI
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Estágio de construção
FROM python:3.12-slim as builder

# Instalação do Poetry
RUN pip install poetry

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./

# Instala as dependências do sistema para o psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev libffi-dev\
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências do Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# Estágio final
FROM python:3.12-slim

# Copia o ambiente virtual e o código da etapa de construção
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app /app

# Define o diretório de trabalho
WORKDIR /app

# Expõe a porta do serviço
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
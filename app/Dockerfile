# Imagem base
FROM python:3.12

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos de dependências e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app

EXPOSE ${PORT:-8000}

# Comando para executar a aplicação
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}

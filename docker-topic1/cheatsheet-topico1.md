# 🐳 Tópico 1 — Cheatsheet: Imagens e Build com Python

## Estrutura do Dockerfile usado nos estudos

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "app.py"]
```

```python
# app.py
import os
name = os.getenv("NAME", "Mundo")
greeting = os.getenv("GREETING", "Olá")
print(f"{greeting}, {name}! Aqui é o Docker Integrador.")
```

## Comandos de build

```bash
# Build básico
docker build -t topic1-app .

# Build com tag de versão
docker build -t topic1-app:v1 .
```

## Dockerfile boas práticas

### Ordem do Dockerfile (aproveitamento de cache)
```dockerfile
# 1. Imagem base (muda raramente)
FROM python:3.12-slim

# 2. WORKDIR primeiro
WORKDIR /app

# 3. Dependências ANTES do código (cache de camada)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Código por último (muda com frequência)
COPY . .

# 5. Comando final
ENTRYPOINT ["python", "app.py"]
```

### --no-cache-dir
```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
# → Evita acumular cache do pip na imagem (menor tamanho)
```

## Rodar com variáveis de ambiente

```bash
# Valores padrão (NAME=Mundo, GREETING=Olá)
docker run topic1-app
# → "Olá, Mundo! Aqui é o Docker Integrador."

# Customizando variáveis
docker run -e NAME=Lucas topic1-app
# → "Olá, Lucas! Aqui é o Docker Integrador."

docker run -e NAME=Lucas -e GREETING="Fala aí" topic1-app
# → "Fala aí, Lucas! Aqui é o Docker Integrador."

# Rodar em background
docker run -d --name app-v1 topic1-app
```

## Utilitários

```bash
# Ver camadas da imagem
docker history topic1-app

# Ver detalhes
docker inspect topic1-app

# Remover imagem
docker rmi topic1-app

# Ver logs do container
docker logs app-v1
```
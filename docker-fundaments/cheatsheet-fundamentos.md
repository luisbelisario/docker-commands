# 🐳 Fundamentos — Cheatsheet: Dockerfile Básico

## Estrutura do Dockerfile usado nos estudos

```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["Mundo"]
```

```bash
# entrypoint.sh
#!/bin/sh
echo "Oi, $1!"
```

## Comandos essenciais

### FROM — Imagem base
```dockerfile
FROM ubuntu:latest          # Ubuntu oficial
FROM python:3.12-slim       # Python oficial (versão slim)
FROM alpine:latest          # Alpine (leve)
FROM nginx:alpine           # Nginx leve
```

### RUN — Comandos durante o build
```dockerfile
RUN apt-get update && apt-get install -y curl
RUN chmod +x /script.sh
```

### COPY — Copiar arquivos para a imagem
```dockerfile
COPY entrypoint.sh /entrypoint.sh          # Arquivo único
COPY . /app                                # Pasta inteira
COPY requirements.txt .                    # Para o WORKDIR atual
```

### ENTRYPOINT vs CMD
```dockerfile
# ENTRYPOINT = comando fixo (sempre executa)
ENTRYPOINT ["/entrypoint.sh"]

# CMD = argumento padrão (pode ser sobrescrito ao rodar)
CMD ["Mundo"]

# Rodando:
docker run minha-imagem           # → "Oi, Mundo!"
docker run minha-imagem Lucas     # → "Oi, Lucas!"
```

### WORKDIR — Diretório de trabalho
```dockerfile
WORKDIR /app
# Todos os COPY, RUN, CMD seguintes partem daqui
```

## Build e run

```bash
# Build da imagem
docker build -t minha-imagem .

# Build com tag específica
docker build -t minha-imagem:v1 .

# Rodar com argumento sobrescrevendo CMD
docker run minha-imagem Maria
# → "Oi, Maria!"

# Rodar em background
docker run -d minha-imagem
```

## Utilitários

```bash
# Listar imagens
docker images

# Remover imagem
docker rmi minha-imagem

# Ver histórico de camadas
docker history minha-imagem

# Inspecionar imagem
docker inspect minha-imagem
```
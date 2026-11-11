# 🐳 Tópico 2 — Cheatsheet: Gerenciamento de Containers

## 1. Mapeamento de portas (`-p`)

```bash
# Mapear porta do host para o container
docker run -d -p 8080:80 --name meu-nginx nginx:alpine

# Vários containers em portas diferentes
docker run -d -p 8081:80 --name outro-nginx nginx:alpine

# Erro: porta já alocada
docker run -d -p 8080:80 --name conflito nginx:alpine
# → "port is already allocated"

# Container sem -p NÃO é acessível pelo host
docker run -d --name sem-porta nginx:alpine
curl localhost:80  # → "Couldn't connect to server"
```

## 2. Volumes e bind mounts (`-v`, `--mount`)

### Bind mount (caminho do host → container)
```bash
# Montar pasta local dentro do container (read-only)
docker run -d -p 8080:80 \
  -v /Users/luissantos/Projetos/docker-commands/docker-topic2/my-site:/usr/share/nginx/html:ro \
  --name site nginx:alpine

# Alterar arquivo local → container reflete sem rebuild!
echo '<h1>Editado sem rebuild!</h1>' > my-site/index.html
```

### Volume nomeado (gerenciado pelo Docker)
```bash
# Criar volume
docker volume create meus-dados

# Container escreve no volume
docker run -d --name escritor -v meus-dados:/data alpine sh -c "echo 'persistiu' > /data/arquivo.txt && sleep 30"

# Outro container LÊ o mesmo volume
docker run --rm -v meus-dados:/data alpine cat /data/arquivo.txt
# → persistiu

# Remover volume
docker volume rm meus-dados
```

### Volume para persistência de dados
```bash
docker volume create contador-data

docker run -d -p 8000:8000 -v contador-data:/data --name contador-v1 contador
curl localhost:8000  # Visita #1

docker stop contador-v1 && docker rm contador-v1

# Novo container, mesmo volume → contador continua!
docker run -d -p 8000:8000 -v contador-data:/data --name contador-v2 contador
curl localhost:8000  # Visita #2
```

## 3. Variáveis de ambiente (`-e`, `--env-file`)

```bash
# Variável única
docker run --rm -e DB_HOST=localhost alpine env | grep DB_HOST

# Arquivo .env
cat > db.env << 'EOF'
DB_HOST=localhost
DB_PORT=5432
DB_NAME=meubanco
EOF

# Carregar do arquivo
docker run --rm --env-file db.env alpine sh -c "echo \$DB_HOST"

# Sobrescrever uma variável
docker run --rm --env-file db.env -e DB_HOST=producao alpine sh -c "echo \$DB_HOST"
```

## 4. Logs e exec interativo

```bash
# Logs do container
docker logs debug-box

# Seguir logs em tempo real
docker logs -f debug-box

# Executar comando em container rodando
docker exec debug-box uname -a
docker exec debug-box cat /etc/os-release

# Shell interativo dentro do container
docker exec -it debug-box sh
# Dentro: ls, whoami, exit
```

## 5. Restart policies

```bash
# Sempre reiniciar
docker run -d --name always-up --restart always alpine sleep 5

# Padrão (não reinicia)
docker run -d --name one-shot alpine sleep 3

# Outras políticas
--restart on-failure    # reinicia se exit code != 0
--restart unless-stopped  # reinicia sempre, exceto se parado manualmente
```

## Utilitários

```bash
# Limpar tudo (containers, imagens, volumes, cache)
docker system prune -a --volumes

# Parar e remover todos os containers
docker rm -f $(docker ps -aq) 2>/dev/null

# Remover imagem
docker rmi nome-da-imagem

# Ver logs de erro
docker logs nome-do-container
```
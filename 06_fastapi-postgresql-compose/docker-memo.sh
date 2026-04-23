# Build and start all services in detached mode
docker compose up --build -d

# Check running containers
docker ps

# Check api container logs
docker logs 06_fastapi-postgresql-compose-api-1

# Call the health endpoint
curl http://localhost:8000/health

# 強制的に全コンテナ停止・削除
docker compose down

# コンテナが全て消えたか確認
docker ps -a

# ボリューム削除
docker volume rm 06_fastapi-postgresql-compose_postgres_data

# Build and start services
docker compose up --build -d

# Check container status
docker compose ps
docker ps

# Check app logs
docker compose logs app

# List all service names in this project
docker compose config --service

# Override APP_ENV at runtime
# 実行時に APP_ENV を上書きする
docker compose run --rm -e APP_ENV=staging app python -c "import os; print(os.getenv('APP_ENV'))"

# Stop and remove containers
docker compose down

# Remove unused images
docker image prune -f

# Verify
docker ps
docker images

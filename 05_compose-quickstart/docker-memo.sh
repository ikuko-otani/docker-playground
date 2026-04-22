# Validate the resolved compose config (variable interpolation check)
# 変数補完後の compose.yaml を確認（IaC の動作確認）
docker compose config

# Start all services in the foreground
# 全サービスをフォアグラウンドで起動
docker compose up

# In a separate terminal — verify the app responds
# 別ターミナルでアクセス確認
curl http://localhost:8000

# Check running containers
# 起動中のコンテナ一覧を確認
docker compose ps

# Start in detached mode
# バックグラウンドで起動
docker compose up -d

# Watch logs
# ログをリアルタイム確認（Ctrl+C で抜ける）
docker compose logs -f

# 停止→再起動後もカウントが引き継がれることを確認
docker compose down
docker compose up -d
curl http://localhost:8000

# Inspect the named volume
# Named Volume の一覧を確認
docker volume ls

# Confirm variable interpolation
# 変数が正しく展開されているか確認
docker compose config
docker compose config | Select-String -Pattern "ports" -Context 0,4

# Stop and remove containers (keep volumes)
# コンテナを停止・削除（ボリュームは保持）
docker compose down

# Stop and remove containers AND volumes
# コンテナとボリュームをまとめて削除（データもリセット）
docker compose down -v

# Remove dangling images
# タグのない不要イメージを削除
docker image prune -f

# Confirm no containers are running
# 起動中のコンテナがないことを確認
docker ps

# Check disk usage
# Docker が使用しているディスク容量を確認
docker system df

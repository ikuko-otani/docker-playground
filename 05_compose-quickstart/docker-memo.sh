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

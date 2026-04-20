# D-03: Build, Tag, and Run Images

## What you will learn / 学習内容

**English:**
In this unit, you will learn how to build a Docker image from a Dockerfile,
tag it with a meaningful name and version, and run it as a container.
You will also practice stopping, removing containers and cleaning up images.

**日本語：**
この単元では、Dockerfile からイメージをビルドし、意味のある名前とバージョンでタグ付けし、
コンテナとして実行する方法を学びます。
コンテナの停止・削除、イメージのクリーンアップも練習します。

## Key Commands / 主要コマンド

```bash
# Build an image with a tag
# イメージをタグ付きでビルドする
docker build -t <name>:<tag> .

# Add an additional tag to an existing image
# 既存イメージに別タグを付与する
docker tag <source> <target>

# Run a container in detached mode with port mapping
# ポートマッピング付きでコンテナをバックグラウンド起動する
docker run -dp <host_port>:<container_port> <image>

# List running containers
# 実行中のコンテナ一覧
docker ps

# Stop and remove a container
# コンテナを停止・削除する
docker stop <container_id>
docker rm <container_id>

# List images
# イメージ一覧
docker images

# Remove unused images
# 未使用イメージを削除する
docker image prune
```

## Reference / 参照

- [Docker Workshop – Updating the application](https://docs.docker.com/get-started/workshop/03_updating_app/)
- Flagship project: [payment-ledger-api](https://github.com/ikuko-otani/payment-ledger-api)

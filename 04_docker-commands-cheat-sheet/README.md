# D-04: Docker Commands Cheat Sheet

## What you learn / 何を学ぶか

**English:**
This unit focuses on daily-use Docker CLI commands through hands-on repetition.
You will practice `ps`, `logs`, `exec`, `stop`, `rm`, and `image prune`
until they feel natural — the same muscle-memory goal as touch-typing.

**日本語：**
この単元では、日常的に使う Docker CLI コマンドをハンズオンで反復練習します。
`ps`, `logs`, `exec`, `stop`, `rm`, `image prune` を体に染み込ませることが目標です。
タッチタイピングと同じ「筋肉記憶」を養います。

---

## DONE criteria / 完了基準（Week 1 終了時）

- [ ] `docker run python:3.12-slim python -c "print('hi')"` がすぐ打てる
- [ ] 自作 Dockerfile から FastAPI "hello world" コンテナが起動する
- [ ] `docker logs -f` でコンテナログがリアルタイムに見られる

---

## Files / ファイル構成

| File | Description |
|------|-------------|
| `Dockerfile` | FastAPI hello-world コンテナ定義（手順書で埋める） |
| `app.py` | FastAPI サンプルアプリ（手順書で埋める） |
| `README.md` | この説明ファイル |

---

## Key commands covered / カバーするコマンド

```
docker ps / docker ps -a
docker logs / docker logs -f
docker exec -it <container> sh
docker stop / docker kill
docker rm / docker rm -f
docker images / docker image ls
docker image prune / docker container prune
```

---

## Berlin interview relevance / ベルリン面接での重要度

⭐⭐⭐ These commands are asked in virtually every backend container interview.
コンテナ面接ではほぼ必ず問われる基本コマンドです。

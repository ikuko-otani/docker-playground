# DC-01: Compose Quickstart

<!-- English summary -->
## What you will learn

This exercise follows the official Docker Compose Quickstart tutorial.
You will build a minimal **Flask + Redis** hit-counter application and
orchestrate it with `docker compose`.

| Topic | Key concept |
|---|---|
| `compose.yaml` structure | `services`, `build`, `ports`, `environment` |
| Dockerfile basics | `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD` |
| Service networking | Containers reach each other by service name (DNS) |
| Health checks | `healthcheck` + `depends_on: condition: service_healthy` |
| Named volumes | Data persistence across `docker compose down` |
| `.dockerignore` | Keep secrets & cache out of image layers |
| Compose Watch | `--watch` flag for live reload during development |
| Environment variables | `.env` file + `${VAR}` interpolation in `compose.yaml` |

---

<!-- 日本語のまとめ -->
## この演習で学ぶこと

公式 Docker Compose クイックスタートチュートリアルに従い、
**Flask + Redis** のヒットカウンターアプリを作成し、
`docker compose` で複数コンテナをオーケストレーシングする経験を積みます。

### 学習目標

- `compose.yaml` の基本構文を理解し、自力で書ける
- `docker compose up / down` でスタック全体を起動・停止できる
- `healthcheck` と `depends_on` で起動順序を制御できる
- `.dockerignore` でシークレットをイメージに焦き込まない理由を説明できる
- Named Volume によるデータ永続化の仕組みを説明できる

---

## Reference

- 📖 [Official tutorial](https://docs.docker.com/compose/gettingstarted/)
- 📁 Learning repo: `docker-playground/05_compose-quickstart/`
- 🎯 Target role: Python Backend (FastAPI) — Berlin EU scale-up

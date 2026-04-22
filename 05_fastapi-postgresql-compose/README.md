# DC-02: FastAPI + PostgreSQL compose.yaml from scratch

## What you learn / 学習内容

**English**
Build a `compose.yaml` from scratch that starts two services:
- `api` – a FastAPI application container built from a local `Dockerfile`
- `postgres` – an official PostgreSQL container

Key Compose concepts covered:
`services`, `build`, `image`, `ports`, `environment`, `depends_on`, `volumes`, `networks`

DONE condition: `curl http://localhost:8000/health` returns HTTP 200 and the api container successfully connects to PostgreSQL via environment variables.

---

**日本語**
ゼロから `compose.yaml` を書いて、2つのサービスを起動します：
- `api` – ローカルの `Dockerfile` からビルドした FastAPI コンテナ
- `postgres` – 公式 PostgreSQL コンテナ

習得する Compose の概念：
`services` / `build` / `image` / `ports` / `environment` / `depends_on` / `volumes` / `networks`

完了条件：`curl http://localhost:8000/health` が HTTP 200 を返し、api コンテナが環境変数経由で PostgreSQL に接続できること。

## File structure / ファイル構成

```
05_fastapi-postgresql-compose/
├── compose.yaml        # Main Compose file (you write this)
├── Dockerfile          # FastAPI image definition (you write this)
├── app/
│   └── main.py         # FastAPI app with /health endpoint (you write this)
└── README.md           # This file
```

## References / 参照

- [Docker Compose Getting Started](https://docs.docker.com/compose/gettingstarted/)
- [Compose file reference – services](https://docs.docker.com/reference/compose-file/services/)
- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)

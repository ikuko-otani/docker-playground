# DC-03: `.env`, `env_file`, `healthcheck`, `networks`

## What You Will Learn / 学習内容

This exercise covers the essential Docker Compose patterns for managing environment
variables, health checks, and network isolation in a FastAPI + PostgreSQL stack.

この演習では、FastAPI + PostgreSQL 構成における環境変数管理・ヘルスチェック・
ネットワーク分離のパターンを実践します。

## Topics / トピック

| Topic | Description (EN) | 説明 (JA) |
|---|---|---|
| `.env` file | Default variable file for interpolation | 補間用デフォルト変数ファイル |
| `environment` attribute | Inline env vars in compose.yaml | compose.yaml への直接記述 |
| `env_file` attribute | Load vars from external file | 外部ファイルから変数を読み込む |
| Precedence | `run -e` > `environment` > `env_file` > `ENV` | 優先順位ルール |
| `healthcheck` | Wait until service is truly ready | サービスが準備完了になるまで待機 |
| `depends_on` + `condition` | Start order with health awareness | ヘルスチェック連携の起動順序制御 |
| `networks` | Isolate service communication | サービス間通信の分離 |

## Files / ファイル構成

```
06_environment-variables/
├── Dockerfile          # FastAPI app image
├── compose.yaml        # Multi-service definition
├── .env.example        # Template — copy to .env
├── .gitignore          # Excludes .env from Git
├── app/
│   └── main.py         # FastAPI minimal app
└── README.md           # This file
```

## 🔐 Security Note / セキュリティ注意

- **Never commit `.env`** to version control.
  `.env` は絶対に Git にコミットしないでください。
- Use `secrets` for production credentials.
  本番環境では Docker Secrets または外部シークレット管理を使用してください。
- `.env.example` (with dummy values) is safe to commit.
  ダミー値の `.env.example` はコミットしても安全です。

## Reference / 参照

- [Docker Compose Environment Variables](https://docs.docker.com/compose/environment-variables/)
- [Compose Healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)
- [Compose Networks](https://docs.docker.com/compose/compose-file/06-networks/)

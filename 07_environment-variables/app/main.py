# DC-03: FastAPI minimal app for environment variable exercise
# DC-03: 環境変数演習用 FastAPI 最小構成アプリ
# TODO: Fill in the implementation following the lesson guide.
# 手順書に従って実装を追加してください。

import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    # Return APP_ENV and DATABASE_URL from environment
    return {
        "app_env": os.getenv("APP_ENV", "not set"),
        "database_url": os.getenv("DATABASE_URL", "not set")
    }

@app.get("/health")
def health():
    # DB connectivity check
    return {"status": "OK"}

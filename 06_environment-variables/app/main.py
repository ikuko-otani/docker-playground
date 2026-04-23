# DC-03: FastAPI minimal app for environment variable exercise
# DC-03: 環境変数演習用 FastAPI 最小構成アプリ
# TODO: Fill in the implementation following the lesson guide.
# 手順書に従って実装を追加してください。

import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
 # TODO: Return APP_ENV and DATABASE_URL from environment
 # 環境変数 APP_ENV と DATABASE_URL を返すように実装する
 return {
 "message": "TODO: return env vars here",
 "app_env": os.getenv("APP_ENV", "not set"),
 }


@app.get("/health")
def health():
 # TODO: add DB connectivity check
 # TODO: データベース接続確認を追加する
 return {"status": "ok"}

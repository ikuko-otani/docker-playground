# DC-01: Compose Quickstart
# DC-01: Compose クイックスタート
# Ref: https://docs.docker.com/compose/gettingstarted/
# TODO: Fill this file following the lesson guide.

# ベースイメージを指定（alpine = 軽量 Linux）
FROM python:3.12-alpine

# コンテナ内の作業ディレクトリを /code に設定
WORKDIR /code

# Flask の環境変数を設定（外部からアクセス可能にする）
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# C コンパイラなど Alpine 用のビルド依存を追加
RUN apk add --no-cache gcc musl-dev linux-headers

# 依存ファイルを先にコピー（レイヤーキャッシュ最適化）
COPY requirements.txt requirements.txt

# 依存ライブラリをインストール
RUN pip install -r requirements.txt

# 残りのアプリコードをコピー
COPY . .

# コンテナがリッスンするポートをドキュメント化
EXPOSE 5000

# コンテナ起動時に flask を実行
CMD ["flask", "run", "--debug"]

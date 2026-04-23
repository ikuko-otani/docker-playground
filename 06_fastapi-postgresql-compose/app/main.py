# DC-02: FastAPI application entry point
# TODO: Implement /health endpoint that connects to PostgreSQL

import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    # Read DB connection params from environment variables
    db_host = os.getenv("DB_HOST", "postgres")
    db_user = os.getenv("BD_USER", "user")
    db_pass = os.getenv("BD_PASSWORD", "password")
    db_name = os.getenv("BD_NAME", "appdb")

    try:
        conn = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            dbname=db_name,
            connect_timeout=3
        )
        conn.close()
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

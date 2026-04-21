# D-04: Docker Commands Cheat Sheet — sample FastAPI app
# TODO: Uncomment and fill in following the lesson guide.

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from D-04"}

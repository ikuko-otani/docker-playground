# DC-01: Compose Quickstart -- Flask + Redis hit counter
# 日本語訳：DC-01: Compose クイックスタート — Flask + Redis ヒットカウンター
# Ref: https://docs.docker.com/compose/gettingstarted/
# TODO: Fill in the blanks following the lesson guide.

import time
import redis
from flask import Flask

app = Flask(__name__)

# TODO: Connect to Redis using the service name as hostname
cache = redis.Redis(host="redis", port=6379)

def get_hit_count():
    # TODO: Implement retry logic with retries=5, delay=0.5s
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route("/")
def hello():
    # TODO: Return a greeting string with the hit count
    count = get_hit_count()
    return f"Hello World! I have been seen {count} times.\n"

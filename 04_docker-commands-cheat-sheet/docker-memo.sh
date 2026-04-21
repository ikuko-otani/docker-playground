docker run python:3.12-slim python -c "print(hi)"
docker run --name mytest -d python:3.12-slim python -c "import time; time.sleep(60)"

docker ps
docker ps -a

docker run --name logtest -d python:3.12-slim python -c "import time; [print(f'log {i}') or time.sleep(1) for i in range(30)]"

docker logs logtest
docker logs -f logtest

docker exec -it logtest sh

ls /
python --version
exit

docker build -t d04-fastapi .
docker run --name d04app -d -p 8000:8000 d04-fastapi

curl http://localhost:8000/

docker stop d04app logtest mytest
docker rm d04app logtest mytest
docker image prune -f
docker container prune -f

docker ps -a
docker images

docker rmi d04-fastapi:latest

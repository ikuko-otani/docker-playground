# D-03: Build, Tag, and Run Images

## What you will learn

**English:**
In this unit, you will learn how to build a Docker image from a Dockerfile,
tag it with a meaningful name and version, and run it as a container.
You will also practice stopping, removing containers and cleaning up images.

## Key Commands

```bash
# Build an image with a tag
docker build -t <name>:<tag> .

# Add an additional tag to an existing image
docker tag <source> <target>

# Run a container in detached mode with port mapping
docker run -dp <host_port>:<container_port> <image>

# List running containers
docker ps

# Stop and remove a container
docker stop <container_id>
docker rm <container_id>

# List images
docker images

# Remove unused images
docker image prune
```

## Reference

- [Docker Workshop – Updating the application](https://docs.docker.com/get-started/workshop/03_updating_app/)
- Flagship project: [payment-ledger-api](https://github.com/ikuko-otani/payment-ledger-api)

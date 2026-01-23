# dezc-docker-workshop
# Docker Codespaces

## Run Container and Map Volume
```bash
docker run -it --rm -v "$(pwd)":/app -w /app python:3.9.16
```
* `-v "$(pwd)":/app` This "mounts" your current directory ($(pwd)) to a folder named /app inside the container.
* `-w /app` This sets the "working directory" inside the container to /app, so you don't have to cd into it manually.
* `--rm` Remove the container after exiting.

```bash
docker run -it \
    --rm \
    -v $(pwd)/test:/app/test \
    --entrypoint=bash \
    python:3.9.16-slim
```
* `--entrypoint` is useful.

## Docker Commands

* `docker ps -a` Lists all containers including stopped ones.
* `docker ps -aq` Only display container IDs
* `docker rm $(docker ps -aq)` Remove all containers. 
* `docker stop $() and docker kill $()` can be used to stop or kill.


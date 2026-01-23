# dezc-docker-workshop
## Bash Commands
* `pwd` Prints the present working directory.
* `which python` Prints python version in the Codespace.


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

## Using `uv` in CodeSpace Container
* `pip install uv` Installs uv.
* `uv run which python` Python path in virtual environment.
* `uv run python -V` Python version from venv.  
**_uv run uses the isolated environment._**
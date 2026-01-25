# dezc-docker-workshop
## Bash Commands
* `pwd` Prints the present working directory.
* `cat ~/.bashrc` Prints the content of `.bashrc` file
* `which python` Prints python version in the Codespace.


## Run Container and Map Volume
`docker run -it --rm --entrypoint=bash python:3.13` Run python:3.13 image.
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
* `docker ps` Lists running containers.
* `docker ps -a` Lists all containers including stopped ones.
* `docker ps -aq` Only display container IDs
* `docker rm $(docker ps -aq)` Remove all containers. 
* `docker stop $() and docker kill $()` can be used to stop or kill.
* `docker volume ls` Lists the volumes.

### Docker Images
* `docker build -t test:pandas` Build the image as `<name>:<tag>`.
* `docker images` Lists the images.
* `docker ps` See the running container.

## Using `uv` in CodeSpace Container
* `pip install uv` Installs uv.
* `uv add pandas pyarrow` Adds packages to venv and updates `pyproject.toml`.
* `uv run <>` Run the command in the isolated environment.
* `uv run which python` Python path in virtual environment.
* `uv run python -V` Python version from venv.  

## Running PostGres
mkdir ny_taxi_postgres_data
```bash
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
  ```
  * Runs PostGres in Interactive Mode.
  * Use `-d` to run in detached mode and access using the URL.

  * `uv add --dev pgcli` to add pgcli
  * `uv run pgcli -h localhost -p 5432 -u root -d ny_taxi`

  ### PostGres Commands
  * `\dt` Lists tables.
  * `\q` Exit.

  ### Jupyter Notebook
  * `uv add --dev jupyter` Install Jupyter
  * `uv run jupyter notebook` Run Jupyter Notebook

  
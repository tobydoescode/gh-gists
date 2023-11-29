# GitHub Gist API

The GitHub Gist API server contained within this repository can be used to
retrieve the public gists for a given user.

## Getting Started

In order to build, deploy, test and use this project the following must be
preinstalled:

- Docker
- Python 3 (tests only)

### Build

To build this project run the following from the root of the repository -
replacing the preferred repostory and tag names as appropriate:

```sh
docker build -t <repository-name>:<tag-name> .
```

For example:

```sh
docker build -t gh-gist-api:v1.0.0 .
```

### Run

To run the server after building it, run the following command - replacing
the repository and tag names as used previously:

```sh
docker run -it --rm -p 8080:8080 --name gh-gist-api <repository-name>:<tag-name>
```

For example:

```sh
docker run -it --rm -p 8080:8080 --name gh-gist-api gh-gist-api:v1.0.0
```

> Note: this is running interactively, meaning the shell remains connected to
the container. Containers can also be run in "detached mode" by replacing "-it"
with "-d".

### Query

> Note: if running in "interactive mode" (using `-i`) you will need to open a
new terminal to execute the below commands.

To query the API execute the following - replacing the desired username as
appropriate:

```sh
curl http://localhost:8080/<username>
```

For example:

```sh
curl http://localhost:8080/octocat
```

### Test

>  Note: the app must be running before you attempt to execute the tests.

To run the tests execute the following commands:

```sh
python3 -m venv ./venv
python3 -m pip install -r requirements-dev.txt
python3 tests/main.py
```

### Cleanup

If running the container in "interactive mode" (using `-i`), press `Ctrl+C` to
stop the container.

If running the container in "detached mode" (using `-d`), execute the following:

```sh
docker rm -f gh-gist-api
```

To remove the image execute the following - replacing the repository and tag
names with the values entered above:

```sh
docker image rm <repository-name>:<tag-name>
```

For example:

```sh
docker image rm gh-gist-api:v1.0.0
```
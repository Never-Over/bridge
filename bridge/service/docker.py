# Responsible for docker initialization, entrypoint
import sys

import docker
from service import postgres


def get_docker_client() -> docker.DockerClient:
    try:
        client = docker.from_env()
    except docker.errors.DockerException:
        print("❌ Bridge Error: Make sure docker is installed and running.")
        sys.exit(1)

    return client


def build_environment(): ...


def get_config(postgres=True):
    client = get_docker_client()
    config = {}  # TODO make this a pydantic model
    if postgres:
        config["postgres"] = postgres.get_config(client)
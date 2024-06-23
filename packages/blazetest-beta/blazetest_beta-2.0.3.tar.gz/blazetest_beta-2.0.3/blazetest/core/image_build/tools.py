import os
from abc import ABC

import docker

from blazetest.core.utils.command_executor import CommandExecutor
from blazetest.core.utils.exceptions import DepotTokenNotProvided


class BuildTool(ABC):
    def __init__(
        self,
        project_context: str,
        docker_file_path: str,
        image_uri: str,
        build_platform: str,
        *args,
        **kwargs,
    ):
        self.project_context = project_context
        self.docker_file_path = docker_file_path
        self.image_uri = image_uri
        self.build_platform = build_platform

    def login(self, username: str, password: str, registry: str):
        pass

    def build(self):
        pass

    def push(self):
        pass

    def build_and_push(self):
        pass


class DepotBuildTool(BuildTool):
    """
    Uses depot.dev to build and push images to a remote repository.
    """

    EXECUTABLE = "depot"  # TODO: would executable work correctly?
    BUILD_COMMAND = "build"

    def __init__(
        self,
        project_context: str,
        docker_file_path: str,
        image_uri: str,
        build_platform: str,
        depot_token: str = None,
        depot_project_id: str = None,
    ):
        super().__init__(
            project_context=project_context,
            docker_file_path=docker_file_path,
            image_uri=image_uri,
            build_platform=build_platform,
        )
        self.depot_token = depot_token
        if self.depot_token is None:
            self.depot_token = os.getenv("DEPOT_TOKEN")
            if self.depot_token is None:
                raise DepotTokenNotProvided(
                    "Depot token not provided. "
                    "Please provide it using --depot-token CLI argument or DEPOT_TOKEN environment variable."
                )
        self.depot_project_id = depot_project_id

    def build_and_push(self):
        args = {
            "--tag": self.image_uri,
            "--file": self.docker_file_path,
            "--platform": self.build_platform,
            "--token": self.depot_token,
            "--push": None,
            "--provenance": "false",
            self.project_context: None,
        }

        if self.depot_project_id:
            args["--project"] = self.depot_project_id

        return self.__execute(
            command=self.BUILD_COMMAND,
            arguments=args,
        )

    def login(self, username: str, password: str, registry: str = None):
        client = docker.from_env()
        client.login(username=username, password=password, registry=registry)

    def __execute(
        self, command: str, arguments: dict, allowed_return_codes=None
    ) -> int:
        if allowed_return_codes is None:
            allowed_return_codes = [0]

        command_executor = CommandExecutor(
            executable=self.EXECUTABLE,
            command=command,
            arguments=arguments,
        )
        command_result = command_executor.execute_command(
            allowed_return_codes=allowed_return_codes
        )
        return command_result


class DockerBuildTool(BuildTool):
    """
    This class will be used to build and push images from local Docker.
    """

    def __init__(self):
        raise NotImplementedError("DockerBuildTool is not implemented yet.")

    def build(self):
        pass

    def push(self):
        pass


class RemoteBuildTool(BuildTool):
    """
    This class will be used to build and push images from AWS CodeBuild, Google Cloud Build, etc.
    """

    def __init__(self):
        raise NotImplementedError("RemoteBuildTool is not implemented yet.")

    def build(self):
        pass

    def push(self):
        pass

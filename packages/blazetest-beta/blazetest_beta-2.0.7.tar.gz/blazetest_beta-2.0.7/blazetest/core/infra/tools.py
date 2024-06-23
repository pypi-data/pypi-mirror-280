import base64
from abc import ABC, abstractmethod
import logging
from typing import Tuple

import boto3
from pulumi import automation as auto
from pulumi.automation import LocalWorkspaceOptions, ProjectBackend, ProjectSettings

from blazetest.core.config import CWD, LOKI_HOST, LOKI_USER, DOCKER_FILE_PATH
from blazetest.core.deployment.aws import AWSWorkflow
from blazetest.core.image_build.image_build import ImageBuildPush

logger = logging.getLogger(__name__)


class InfraSetupTool(ABC):
    def __init__(
        self,
        aws_region: str,
        resource_prefix: str,
        s3_bucket_name: str,
        ecr_repository_prefix: str,
        lambda_function_timeout: int,
        lambda_function_memory_size: int,
        loki_api_key: str,
        build_backend: str,
        depot_token: str,
        depot_project_id: str,
        tags: dict,
        debug: bool,
    ):
        self.aws_region = aws_region
        self.resource_prefix = resource_prefix
        self.s3_bucket_name = s3_bucket_name
        self.ecr_repository_prefix = ecr_repository_prefix
        self.lambda_function_timeout = lambda_function_timeout
        self.lambda_function_memory_size = lambda_function_memory_size
        self.loki_api_key = loki_api_key
        self.depot_token = depot_token
        self.depot_project_id = depot_project_id
        self.tags = tags
        self.debug = debug
        self.build_backend = build_backend

    @abstractmethod
    def deploy(self) -> None:
        pass


def log_pulumi_event(event: str):
    logger.info(event)


class PulumiInfraSetup(InfraSetupTool):
    """
    Uses Pulumi (https://www.pulumi.com/docs/) Automation API to build and deploy artifacts to the cloud.
    """

    PROJECT_NAME = "blazetest"
    PROJECT_BACKEND_URL = "file:\\/\\/~"
    PROJECT_RUNTIME = "python"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def deploy(self) -> None:
        env_vars = {}

        repo_info = self.create_ecr_repository()
        image_uri = self.build_and_push_image(
            repo_info=repo_info, build_backend=self.build_backend
        )

        workflow = AWSWorkflow(
            resource_prefix=self.resource_prefix,
            s3_bucket_name=self.s3_bucket_name,
            image_uri=image_uri,
            lambda_function_timeout=self.lambda_function_timeout,
            lambda_function_memory_size=self.lambda_function_memory_size,
            loki_host=LOKI_HOST,
            loki_user=LOKI_USER,
            loki_api_key=self.loki_api_key,
            env_vars=env_vars,
            tags=self.tags,
        )

        stack = auto.create_stack(
            stack_name=self.resource_prefix,
            project_name="blazetest",
            program=workflow.deploy,
            opts=self.get_project_settings(),
        )

        logger.info("Installing plugins")

        # TODO: updated automatically to the stable version
        stack.workspace.install_plugin("aws", "v5.42.0")
        stack.workspace.install_plugin("docker", "v4.3.1")

        stack.set_config("aws:region", auto.ConfigValue(value=self.aws_region))
        stack.refresh(on_output=log_pulumi_event, show_secrets=False)

        logger.info("Deploying..")
        workflow_result = stack.up(  # noqa
            show_secrets=False, on_output=log_pulumi_event, debug=self.debug
        )

        logger.info(
            "Deploying has finished.",
        )

    def __get_ecr_login_token(self) -> Tuple[str, str]:
        ecr = boto3.client("ecr", region_name=self.aws_region)

        response = ecr.get_authorization_token()

        auth_data = response["authorizationData"][0]
        token = auth_data["authorizationToken"]
        decoded_token = base64.b64decode(token).decode("utf-8")
        username, password = decoded_token.split(":")

        return username, password

    def create_ecr_repository(self):
        ecr = boto3.client("ecr", region_name=self.aws_region)

        ecr_tags = []
        for tag in self.tags:
            ecr_tags.append({"Key": tag, "Value": self.tags[tag]})

        try:
            response = ecr.create_repository(
                repositoryName=self.ecr_repository_prefix, tags=ecr_tags
            )
            repository = response["repository"]
            logger.info(
                f"Repository '{self.ecr_repository_prefix}' created successfully."
            )
            return repository
        except ecr.exceptions.RepositoryAlreadyExistsException:
            logger.warning(f"Repository '{self.ecr_repository_prefix}' already exists.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

    def build_and_push_image(self, repo_info: dict, build_backend: str = "depot"):
        image_uri = f"{repo_info['repositoryUri']}:{self.resource_prefix}"

        image_build_push = ImageBuildPush(
            backend=build_backend,
            project_context=CWD,
            docker_file_path=DOCKER_FILE_PATH,
            image_uri=image_uri,
            build_platform="linux/amd64",
        )

        # TODO: check if it works in the CI/CD pipeline
        username, password = self.__get_ecr_login_token()
        image_build_push.login(
            username=username,
            password=password,
            registry=repo_info["repositoryUri"],
        )

        image_build_push.build_and_push()
        return image_uri

    def get_project_settings(self):
        return LocalWorkspaceOptions(
            project_settings=ProjectSettings(
                name=self.PROJECT_NAME,
                backend=ProjectBackend(url=self.PROJECT_BACKEND_URL),
                runtime=self.PROJECT_RUNTIME,
            ),
        )

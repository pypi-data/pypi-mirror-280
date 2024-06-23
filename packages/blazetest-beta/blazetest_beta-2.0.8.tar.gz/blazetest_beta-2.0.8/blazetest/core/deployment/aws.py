import json
import logging
from typing import Dict

import pulumi
import pulumi_aws as aws
from pulumi_docker import Image


logger = logging.getLogger(__name__)


class AWSWorkflow:
    """
    The Workflow class is used to deploy an image to Amazon Elastic Container Registry (ECR)
    and an AWS Lambda function to an AWS CloudFormation stack.

    Attributes:
        s3_bucket_name (str): The name of the S3 bucket to use.
        resource_prefix (str): The name of the CloudFormation stack to deploy the Lambda function to.
        loki_user (str): Loki username
        loki_host (str): Loki host address name
        loki_api_key (str): Loki API Key
        tags (str): Tags to pass to the lambda

    Properties:
        lambda_function (aws.lambda_.Function): The Lambda function object.
        image (Image): The image object.
        s3_bucket_prefix (aws.s3.Bucket): The S3 bucket object.
        env_vars (Dict): A dictionary of environment variables to set for the Lambda function.

    Methods:
        deploy(): Initializes the ECR repository, S3 bucket, image, and Lambda function, and deploys them.

        create_s3_bucket(): Creates the S3 bucket.
        create_lambda_function(): Creates the Lambda function.

        get_lambda_iam_policy(): Retrieves IAM Policy for attaching to IAM Role
        get_lambda_iam_role(): Retrieves IAM Role for attaching to Lambda
        get_policy_attachment(): Attaches IAM Policy to IAM Role
    """

    lambda_function: aws.lambda_.Function
    image: Image

    def __init__(
        self,
        resource_prefix: str,
        s3_bucket_name: str,
        image_uri: str,
        lambda_function_memory_size: int,
        lambda_function_timeout: int,
        loki_user: str,
        loki_host: str,
        loki_api_key: str,
        tags: dict,
        env_vars: Dict[str, str],
    ):
        # The name of already created s3 bucket
        self.s3_bucket_name = s3_bucket_name
        self.resource_prefix = resource_prefix
        self.image_uri = image_uri

        # Logging related
        self.loki_user = loki_user
        self.loki_host = loki_host
        self.loki_api_key = loki_api_key

        if not tags:
            tags = {}

        self.tags = tags
        self.env_vars = env_vars

        self.lambda_function_memory_size = lambda_function_memory_size
        self.lambda_function_timeout = lambda_function_timeout

    def deploy(self):
        self.create_lambda_function()

    def create_lambda_function(self):
        iam_role = self.get_lambda_iam_role()
        iam_policy = self.get_lambda_iam_policy()

        role_policy_attachment = aws.iam.RolePolicyAttachment(
            f"{self.resource_prefix[:15]}-policy-attachment",
            role=iam_role.name,
            policy_arn=iam_policy.arn,
        )

        # TODO: use lambda extension or other way to paste the environment variables into AWS Lambda
        self.lambda_function = aws.lambda_.Function(
            self.resource_prefix,
            description="Lambda function for execution of PyTest tests in parallel",
            package_type="Image",
            image_uri=self.image_uri,
            role=iam_role.arn,
            memory_size=self.lambda_function_memory_size,
            timeout=self.lambda_function_timeout,
            environment=aws.lambda_.FunctionEnvironmentArgs(
                variables={
                    "S3_BUCKET": self.s3_bucket_name,
                    "LOKI_USER": self.loki_user,
                    "LOKI_HOST": self.loki_host,
                    "LOKI_API_KEY": self.loki_api_key,
                    **self.env_vars,
                },
            ),
            tags=self.tags,
            opts=pulumi.ResourceOptions(
                depends_on=[
                    role_policy_attachment,
                ],
            ),
        )

    def get_lambda_iam_policy(self) -> aws.iam.Policy:
        return aws.iam.Policy(
            resource_name=f"{self.resource_prefix[:15]}-policy",
            policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "s3:PutObject",
                            ],
                            "Resource": f"arn:aws:s3:::{self.s3_bucket_name}/*",
                        },
                        {
                            "Effect": "Allow",
                            "Action": [
                                "logs:CreateLogGroup",
                                "logs:CreateLogStream",
                                "logs:PutLogEvents",
                                "logs:PutRetentionPolicy",
                                "logs:DescribeLogStreams",
                            ],
                            "Resource": [
                                "arn:aws:logs:*:*:*",
                            ],
                        },
                    ],
                }
            ),
        )

    def get_lambda_iam_role(self) -> aws.iam.Role:
        return aws.iam.Role(
            resource_name=f"{self.resource_prefix[:15]}-role",
            assume_role_policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": "sts:AssumeRole",
                        }
                    ],
                }
            ),
        )

from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_ecr_assets as ecr,
    Stack,
    CfnOutput,
    Tags,
    App
)

from parameters.global_args import GlobalArgs

class LambdaStack(Stack):

       def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CmsCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
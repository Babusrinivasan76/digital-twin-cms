from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_lambda as _lambda,
    Stack,
    CfnOutput,
    Tags,
    App,
    aws_secretsmanager as secretsmanager,
    SecretValue as SecretValue
)

from parameters.global_args import GlobalArgs

env_name = "dev"
secretname = "CMS_ATLAS_URL"




# Create a new lambda function pull_from_mdb
class LambdaStack(Stack):

       def __init__(self, scope: Construct, construct_id: str, atlas_uri : str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a new secret in Secrets Manager and fetch the ARN

        mySecret = secretsmanager.Secret(self, "Secret", secret_name = secretname, secret_string_value = SecretValue.unsafe_plain_text(atlas_uri))

        secretarn = mySecret.secret_arn
        
        generated_name = mySecret.secret_name

        # Create a new lambda function to pull data from MongoDB
        lambda_function_pull_from_mdb = _lambda.Function(
            self, "pull_from_mdb",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_pull_from_mdb.handler",
            code=_lambda.Code.from_asset("AWS_Lambda_Stack"),
            environment={
                "PYTHONPATH" : "dependencies",
                "LOG_LEVEL": "INFO",
                "APP_ENV": "dev",
                "REGION_NAME":"us-east-1",  # Update your region
                "EVENTBUS_NAME":"XXXXX",  # Update the event-bus created 
                "MODEL_ENDPOINT":"sagemaker-soln-XXXX"  # Update your sagemaker model endpoint
            }
        )

        secret = secretsmanager.Secret.from_secret_attributes(self, secretname, 
        secret_complete_arn=secretarn)
        
        secret.grant_read(grantee=lambda_function_pull_from_mdb)


        # Create a new lambda function to push data to MongoDB
        lambda_function_push_to_mdb = _lambda.Function(
            self, "push_to_mdb",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_push_to_mdb.handler",
            code=_lambda.Code.from_asset("AWS_Lambda_Stack"),
            environment={
                "PYTHONPATH" : "dependencies",
                "LOG_LEVEL": "INFO",
                "APP_ENV": "dev",
                "region_name":"us-east-1",
                "evnetbus_name":"default",
                "model_endpoint":"sagemaker-soln-XXXX"
            }
        )
        
        secret.grant_read(grantee=lambda_function_push_to_mdb)

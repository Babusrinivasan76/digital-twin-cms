from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_events as events,
    aws_lambda as _lambda,
    aws_events_targets as events_targets,
    Stack,
    CfnOutput,
    Tags,
    App
)
from parameters.global_args import GlobalArgs

class EventbridgeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, lambda_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Reference an existing Lambda function
        my_function = _lambda.Function.from_function_arn(self, "lambda_pull_from_mdb", lambda_arn)

        # Define a new EventBridge rule
        rule = events.Rule(
            self, 
            'Rule', 
            event_pattern={
                "source": ["user-event"]
                        }
        )

        # Add the Lambda function as a target
        rule.add_target(events_targets.LambdaFunction(my_function))


        
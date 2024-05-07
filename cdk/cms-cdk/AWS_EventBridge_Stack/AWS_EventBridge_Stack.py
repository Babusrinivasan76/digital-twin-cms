from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_events as event,
    aws_lambda as _lambda,
    aws_events_targets as targets,
    Stack,
    CfnOutput,
    Tags,
    App
)
from parameters.global_args import GlobalArgs

class EventBridgeStack(Stack):

       def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

 # Define a new Lambda resource
        my_lambda = _lambda.Function(
            self, "MyLambda",
            code=_lambda.Code.from_inline("exports.handler = function(event, ctx, cb) { return cb(null, \"hi\"); }"),
            handler="index.handler",
            runtime=_lambda.Runtime.NODEJS_10_X,
        )

        # Define a new EventBridge rule
        rule = events.Rule(
            self, "Rule",
            event_pattern=events.EventPattern(
                source=["aws.ec2"]
            )
        )

        # Add Lambda as a target to the EventBridge rule
        rule.add_target(targets.LambdaFunction(my_lambda))
from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_events as events,
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
        events.CfnEventBus(self, 'PartnerEventBus',
        name='partner_event_bus_name',
        event_source_name='partner_name'
        )


        
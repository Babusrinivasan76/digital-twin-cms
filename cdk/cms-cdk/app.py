#!/usr/bin/env python3

import aws_cdk as cdk
from Amazon_ECR_Stack.Amazon_ECR_Stack import ECRStack
from AWS_EventBridge_Stack.AWS_EventBridge_Stack import EventBridgeStack
from AWS_Lambda_Stack.AWS_Lambda_Stack import LambdaStack
from AWS_S3_Stack.AWS_S3_Stack import S3Stack
from AWS_SageMaker_Stack.AWS_SageMaker_Stack import SageMakerStack
from MongoDB_Atlas_Stack.MongoDB_Atlas_Stack import MongoDBAtlasStack


from parameters.global_args import GlobalArgs


app = cdk.App()

# MongoDB AtlasBasic stack
cms_mongo_atlas_stack = MongoDBAtlasStack(
    app, 
    f"{app.node.try_get_context('project')}-mongo-atlas-stack"
)


# S3 Bucket to hold our datasources
cms_bkt_stack = S3Stack(
    app,
    f"{app.node.try_get_context('project')}-bucket-stack",
    stack_log_level = "INFO",
    custom_bkt_name = GlobalArgs.S3_BUCKET_NAME,
    description = "Data Integration Demo: S3 Bucket to hold our datasources"
)

app.synth()
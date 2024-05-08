#!/usr/bin/env python3

import aws_cdk as cdk
import os

from MongoDB_Atlas_Stack.MongoDB_Atlas_Stack import MongoDBAtlasStack
from AWS_S3_Stack.AWS_S3_Stack import S3Stack
from AWS_Lambda_Stack.AWS_Lambda_Stack import LambdaStack
from Amazon_ECR_Stack.Amazon_ECR_Stack import ECRStack
from AWS_EventBridge_Stack.AWS_EventBridge_Stack import EventbridgeStack
from AWS_SageMaker_Stack.AWS_SageMaker_Stack import SageMakerStack

from parameters.global_args import GlobalArgs



app = cdk.App()

# MongoDB AtlasBasic stack

cms_mongo_atlas_stack = MongoDBAtlasStack(
    app, 
    f"{app.node.try_get_context('project')}-mongo-atlas-stack",
    description = "MongoDB Atlas for CMS Digital Twin Solution"
)
atlasuri = cms_mongo_atlas_stack.Atlas_URI
project_ID = cms_mongo_atlas_stack.atlas_basic_l3.m_project.attr_id


# AWS S3 Bucket Stack to hold our datasources

cms_bkt_stack = S3Stack(
    app,
    f"{app.node.try_get_context('project')}-bucket-stack",
    stack_log_level = "INFO",
    custom_bkt_name = GlobalArgs.S3_BUCKET_NAME,
    description = "S3 bucket and roles and permission for CMS Digital Twin Solution"
)

# AWS Lambda stack to pull data from EventBridge to SageMaker & push data to MongoDB

cms_lambda_stack = LambdaStack(
    app,
    f"{app.node.try_get_context('project')}-lambda-stack",
    atlas_uri = atlasuri,
    description = "Lambdas for CMS Digital Twin Solution"
)

# Get the ARNs of the Lambda functions
arn_lambda_function_push_to_mdb = cms_lambda_stack.lambda_function_push_to_mdb.function_arn
arn_lambda_function_pull_from_mdb = cms_lambda_stack.lambda_function_pull_from_mdb.function_arn


# Amazon EventBridge Stack to trigger Lambda functions

cms_eventbridge_stack = EventbridgeStack(
    app,
    f"{app.node.try_get_context('project')}-eventbridge-stack",
    lambda_arn = arn_lambda_function_pull_from_mdb,
    description = "EventBridge to capture CDC and trigger Lambda for CMS Digital Twin Solution"
)




app.synth()
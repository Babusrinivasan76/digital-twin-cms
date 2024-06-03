#!/usr/bin/env python3

import aws_cdk as cdk
import os

from MongoDB_Atlas_Stack.MongoDB_Atlas_Stack import MongoDBAtlasStack
from AWS_S3_Stack.AWS_S3_Stack import S3Stack
from AWS_Lambda_Stack.AWS_Lambda_Stack import LambdaStack

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

app.synth()
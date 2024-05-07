from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_s3 as _s3,
    aws_s3_deployment as s3deploy,
    aws_mwaa as mwaa,
    aws_kms as kms,
    Stack,
    CfnOutput,
    Tags,
    App
)
from parameters.global_args import GlobalArgs

class S3Stack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        stack_log_level: str,
        custom_bkt_name: str = None,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.data_bkt = _s3.Bucket(
            self,
            "dataBucket",
            auto_delete_objects=True,
            removal_policy = RemovalPolicy.DESTROY,
            bucket_name = custom_bkt_name,
        )

        # Lets set custom bucket name if it is set
        if custom_bkt_name:
            cfn_data_bkt = self.data_bkt.node.default_child
            cfn_data_bkt.add_override("Properties.BucketName", custom_bkt_name)

        ###########################################
        ################# OUTPUTS #################
        ###########################################
        output_0 = CfnOutput(
            self,
            "S3SourceBucket",
            value=f"{self.data_bkt.bucket_name}",
            description=f"The datasource bucket name"
        )
        output_1 = CfnOutput(
            self,
            "dataSourceBucketUrl",
            value=f"https://console.aws.amazon.com/s3/buckets/{self.data_bkt.bucket_name}",
            description=f"The datasource bucket name"
        )
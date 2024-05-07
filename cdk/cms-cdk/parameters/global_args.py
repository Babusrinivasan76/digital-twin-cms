class GlobalArgs():
    """
    Helper to define global statics
    """

    OWNER = "AWS_CMS_MongoDB_Integration_Digital_Twin"
    ENVIRONMENT = "production"
    REPO_NAME = "AWS_CMS_MongoDB_Integration_Digital_Twin"
    SOURCE_INFO = f"https://"
    VERSION = "2023_07_11"
    SUPPORT_EMAIL = ["partners@mongodb.com", ]
    
    
    DATABASE_NAME = "Connected-Vehicle-DB"
    COLLECTION_NAME = "cms-connected-vehicle"
    S3_BUCKET_NAME = "cms-bucket-demo"
    AUTH_DATABASE_NAME = "admin"
    REGION_NAME = "US_EAST_1"
    IP_ADDRESS = "0.0.0.0/0" # Use for development or testing purposes only
    IP_COMMENT = "AWS CMS MongoDB Digital Twin CDK Test"
    PROFILE = "default"

    INSTANCE_SIZE = "M0"
    EBS_VOLUME_TYPE = "STANDARD"
    BACKING_PROVIDER_NAME = "AWS"

      # Tag details
    TAG_OWNER = "owner"
    TAG_PURPOSE = "partners"
    TAG_EXPIRE_ON = "2026-01-01"
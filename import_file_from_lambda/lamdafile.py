# import json
# import boto3
# from botocore.exceptions import ClientError


#LAB1

# def lambda_handler(file_name, bucket, object_name=None):
    
#     file_name= "test"
#     bucket= "targetbucketmadsabri"

#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = file_name

#     # Upload the file
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#         print(' upload done')
#     except ClientError as e:
#         logging.error(e)
#         return False


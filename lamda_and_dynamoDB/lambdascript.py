
# import boto3
# import json
# import time, urllib


# s3 = boto3.resource('s3')
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('day4lab3')

# def lambda_handler(event, context):
    
#     #specify source bucket
#     source_bucket_name=event['Records'][0]['s3']['bucket']['name']
    
#     #get object that has been uploaded
#     file_name=event['Records'][0]['s3']['object']['key']
#     print('file_name')
    
#     #specify destination bucket
#     destination_bucket_name='targetbucketmadsabi'
    
#     #specify from where file needs to be copied
#     copy_object={'Bucket':source_bucket_name,'Key':file_name}
    
#     #write copy statement 
#     s3.meta.client.copy(copy_object,destination_bucket_name,file_name)
    
#     #to get items of the table > get id and appned them into array >
# 		#sort array > get last id and increment it by 1
#     arr=[]
    
#     response = table.scan()
#     data = response['Items']
    
#     if not data :
#         i = 0
#     else:
#         for d in data:
#             arr.append(d['id'])
#         arr.sort()
#         i = arr[-1] + 1
    
    
    #add file name in dynamodb table
    # response = table.put_item(
    #     Item = {
    #         'id': i ,
    #         'file-name': file_name })


`

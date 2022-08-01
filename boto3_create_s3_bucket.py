from boto3 import resource

#this creates a bucket called "thisisanewbucketbucket" in the US-EAST-2 region
aws_resource = resource("s3") 
bucket = aws_resource.Bucket("thisisanewbucketbucket")

response = bucket.create(
    ACL ='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },  
)
print(response)
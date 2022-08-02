#from boto3 import resource
# boto3 import client
import boto3

#this creates a bucket called "thisisanewbucketbucket" in the US-EAST-2 region
aws_resource = boto3.resource("s3") 
bucket = aws_resource.Bucket("thisisanewbucketbucket")

response = bucket.create(
    ACL ='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },  
)
print(response)


print('----------------------------')
#List all bucket names
for b in aws_resource.buckets.all():
    print(b.name)

print('----------------------------')
#List bucket names and creation dates
s3 = boto3.client("s3").list_buckets()["Buckets"]
for b in s3:
    print(b['Name'])
    print(b['CreationDate'])

#Test Again
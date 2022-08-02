from boto3 import client

#Create a file for uploading
#test_file = open("test_file.txt", "a")
#test_file.write("This file is being created to test this upload script")
#test_file.close()


#Upload a single file
s3 = client("s3")
#s3.upload_file(
#    Filename="test_file.txt",
#    Bucket="thisisanewbucketbucket",
#    Key="uploaded_test_file.txt"
#    )

#List of objects in our created bucket
objects=s3.list_objects(Bucket="thisisanewbucketbucket")["Contents"]
for object in objects:
    print(object['Key'])
    
    
#Delete the object we created
s3.delete_object(
    Bucket = "thisisanewbucketbucket",
    Key = "uploaded_test_file.txt"
    )
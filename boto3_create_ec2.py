import boto3

ec2_resource = boto3.resource("ec2")

#Create EC2 Instance
ec2_resource.create_instances(
    ImageId='ami-090fa75af13c156b4',
    InstanceType='t2.micro',
    MaxCount= 1,
    MinCount=1
    )

#Print Instance IDs
li = []
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()['Reservations']
for i in range(len(instances)):
    li.append(instances[i]["Instances"][0]["InstanceId"])


#Delete Specific EC2 Instance
templist = []
templist.append(li[1])
#print(templist)
ec2.terminate_instances(InstanceIds=templist)
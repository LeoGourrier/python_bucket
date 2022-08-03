import boto3

#Create a VPC with the NetworkID of 10.0.0.0/16
client = boto3.client('ec2')
resource = client.create_vpc(CidrBlock='10.0.0.1/16')
print(resource)

#Describe VPCs
vpcs = client.describe_vpcs()['Vpcs']
for vpc in vpcs:
    print(vpc['CidrBlock'] + " - " + vpc['VpcId'])
    
    
#Delete VPC
response = client.delete_vpc(
    VpcId = "vpc-02a80d1e9f6873ac0"
    )
print(response)
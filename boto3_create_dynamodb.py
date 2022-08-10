import boto3
from boto3.dynamodb.conditions import Key, Attr

# replace the keys below


#Create a table named Vegetables
'''
dynamodb = boto3.client('dynamodb')
response = dynamodb.create_table(
    TableName='Vegetables',
    KeySchema=[
        {
            'AttributeName': 'Id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    AttributeDefinitions=[
        {
            'AttributeName': 'Id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        }
    ],
    Tags=[
        {
            'Key': 'Project',
            'Value': 'TestPy'
        },
    ],
)
'''

#Scan the Vegetables table
'''
response = dynamodb.scan(
    TableName='Vegetables'
)
'''

#Write 10+ items to the Vegetables table
'''
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vegetables')
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'Id' : 1,
            'Name': 'Artichoke',
            'Count': 6
        }
    )
    batch.put_item(
        Item={
            'Id' : 2,
            'Name': 'Asparagus',
            'Count': 10
        }
    )
    batch.put_item(
        Item={
            'Id' : 3,
            'Name': 'Beets',
            'Count': 1,
        }
    )
    batch.put_item(
        Item={
            'Id' : 4,
            'Name': 'Broccoli',
            'Count': 3
        }
    )
    batch.put_item(
        Item={
            'Id' : 5,
            'Name': 'Brussel Sprouts',
            'Count': 5
        }
    )
    batch.put_item(
        Item={
            'Id' : 6,
            'Name': 'Carrots',
            'Count': 4
        }
    )
    batch.put_item(
        Item={
            'Id' : 7,
            'Name': 'Cabbage',
            'Count': 1
        }
    )
    batch.put_item(
        Item={
            'Id' : 8,
            'Name': 'Celery',
            'Count': 2,
        }
    )
    batch.put_item(
        Item={
            'Id' : 9,
            'Name': 'Corn',
            'Count': 7
        }
    )
    batch.put_item(
        Item={
            'Id' : 10,
            'Name': 'Kale',
            'Count': 2
        }
    )
'''


#Query an item Named Cucumber from Vegetables
'''
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vegetables')
response = table.query(
    KeyConditionExpression=Key('Name').eq('Broccoli')
)
print(response['Items'][0])
'''

#Delete a table named Vegetables
'''
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vegetables')
table.delete()
'''

#Delete item in the table Vegetables
'''
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vegetables')
table.delete_item(
    Key={
        'Name': 'Artichoke',
        'Count' : 6
    }
)
'''
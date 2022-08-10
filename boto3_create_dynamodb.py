import boto3
from boto3.dynamodb.conditions import Key, Attr

# replace the keys below


#Create a table named Vegetables
'''
dynamodb = boto3.client('dynamodb')
response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Count',
            'AttributeType': 'N'
        }
    ],
    TableName='Vegetables',
    KeySchema=[
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Count',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
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
            'Name': 'Artichoke',
            'Count': 6
        }
    )
    batch.put_item(
        Item={
            'Name': 'Asparagus',
            'Count': 10
        }
    )
    batch.put_item(
        Item={
            'Name': 'Beets',
            'Count': 1,
        }
    )
    batch.put_item(
        Item={
            'Name': 'Broccoli',
            'Count': 3
        }
    )
    batch.put_item(
        Item={
            'Name': 'Brussel Sprouts',
            'Count': 5
        }
    )
    batch.put_item(
        Item={
            'Name': 'Carrots',
            'Count': 4
        }
    )
    batch.put_item(
        Item={
            'Name': 'Cabbage',
            'Count': 1
        }
    )
    batch.put_item(
        Item={
            'Name': 'Celery',
            'Count': 2,
        }
    )
    batch.put_item(
        Item={
            'Name': 'Corn',
            'Count': 7
        }
    )
    batch.put_item(
        Item={
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
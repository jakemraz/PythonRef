import boto3
import time
import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('mon')

month = 5
day = 27

KST = datetime.timezone(datetime.timedelta(hours=9))
sec = int(datetime.datetime(2020,month,day,0,0,0,tzinfo=KST).timestamp())

try:
  response = table.get_item(Key={'deviceName': 'mon1', 'timestamp': sec})
except ClientError as e:
  print(e.response)
else:
  print(response['Item']['payload'])



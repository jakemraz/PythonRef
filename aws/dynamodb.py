import boto3
import time
import datetime
from botocore.exceptions import ClientError
import json
from boto3.dynamodb.conditions import Key, Attr
from aws.decimal_encoder import DecimalEncoder

def get_item():
  dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
  table = dynamodb.Table('usages')

  KST = datetime.timezone(datetime.timedelta(hours=9))
  sec = int(datetime.datetime(2020,5,4,0,0,0,tzinfo=KST).timestamp())

  
  try:
    response = table.get_item(Key={'deviceId': 'client-id-1', 'date': '2020-05-27'})
  except ClientError as e:
    print(e.response)
  else:
    print(response['Item'])
    pass

  item = response['Item']['events']
  if len(item) == 144:
    table.delete_item(Key={'deviceId': 'client-id-1', 'date': '2020-05-27'})


def put_item():
  dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
  table = dynamodb.Table('timeseries')

  item = {'deviceId': 'a', 'timestamp': 1, 'tmp': 2}
  response = table.put_item(Item=item)
  print(response)


def upsert_item():
  dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
  table = dynamodb.Table('usages')

  try:
    response = table.get_item(Key={'deviceId': 'client-id-1', 'date': '2020-05-27'})
  except ClientError as e:
    print(e.response)
  else:
    item = response.get('Item', None)

    events = item.get('events', []) if item is not None else []

  print(response)
  print(events)
  # events = response['Item']['events']

  item1 = {
    "EVENT_TIME": "2020-05-27 00:00:00.000",
    "deviceId": "client-id-1",
    "status": "PUTOFF",
    "SUM_AMOUNT": 0
  }
  item2 = {
    "EVENT_TIME": "2020-05-27 00:10:00.000",
    "deviceId": "client-id-1",
    "status": "PUTOFF",
    "SUM_AMOUNT": 0
  }

  payloads = []
  #events = []
  payloads.append(item1)
  payloads.append(item2)


  events = events + payloads

  item = {
    "date": "2020-05-27",
    "deviceId" : "client-id-1",
    "events" : events
  }

  print(item)

  response = table.put_item(Item=item)
  print(response)


  #json.dumps(val, cls=decimal_encoder.DecimalEncoder)


def query_item():

  deviceId = 'client-id-1'
  month = 5
  day = 27

  dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

  KST = datetime.timezone(datetime.timedelta(hours=9))
  start_timestamp = int(datetime.datetime(2020,month,day,0,0,0,tzinfo=KST).timestamp())
  end_timestamp = int(datetime.datetime(2020,month,day+1,0,0,0,tzinfo=KST).timestamp()) - 1

  table = dynamodb.Table('timeseries')

  response = table.query(
      KeyConditionExpression=Key('deviceId').eq(deviceId) & Key('timestamp').between(start_timestamp, end_timestamp)
  )

  items = response['Items']

  print(json.dumps(items, cls=DecimalEncoder))
  

query_item()
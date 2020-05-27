import boto3
import json


def sendpush():

  title = "foo"
  body = "bar"
  client = boto3.client('sns')

  notification = {
    'notification': {
      'title': title,
      'body': body
    }
  }
  message = {
    'GCM': json.dumps(notification)
  }

  #json.dumps({"GCM":"{ \"notification\": { \"body\": \"bar\", \"title\":\"foo\" } }" })
  #client.publish(TargetArn=ARN, MessageStructure='json', Message=json.dumps({'GCM': json.dumps('bar')}))

  response = client.list_endpoints_by_platform_application(
    PlatformApplicationArn='arn:aws:sns:ap-northeast-2:411392496548:app/GCM/projectA'
  )
  endpoints = response['Endpoints']
  for endpoint in endpoints:
    client.publish(TargetArn=endpoint['EndpointArn'], MessageStructure='json', Message=json.dumps(message))

  #response = client.publish(TargetArn="arn:aws:sns:ap-northeast-2:411392496548:endpoint/GCM/projectA/5ddf14f6-039a-33db-a605-e7a10d70a443", MessageStructure='json', Message=json.dumps(message))
  #print(response)


sendpush()
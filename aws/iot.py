import boto3
import json

client = boto3.client('iot-data')
response = client.get_thing_shadow(
    thingName='mon1'
)

# prase botocore.response.StreamingBody
response_payload = json.loads(response['payload'].read().decode("utf-8"))
battery = response_payload['state']['reported']['battery_remain']
print(battery)

print(response_payload)

import boto3


def detect_label():
  client = boto3.client('rekognition', 'ap-northeast-1')
  response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'rekognition-bucket-jh',
            'Name': 'test.png'
        }
    },
    MaxLabels=10
  )
  print(response)

detect_label()
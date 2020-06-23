import boto3



pinpoint = boto3.client('pinpoint')
def error():

  del pinpoint

  try:
    pinpoint.get_good()
  except Exception as e:
    print(e)


error()
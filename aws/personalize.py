import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_recommendations(
    campaignArn = 'arn:aws:personalize:ap-northeast-2:411392496548:campaign/wproject-campaign',
    userId = '702',
    context = {
      'top1': "20",
      'top2': "22",
      'top3': "21"
    })

print("Recommended items")
print(response)
# for item in response['itemList']:
#     print (item['itemId'])
import requests
import json


def post():
  url = "https://baba.execute-api.ap-northeast-2.amazonaws.com/prod/alert"
  data = {
    "title":"hi",
    "body":"test"
  }
  
  response = requests.post(url=url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
  print(response.status_code)
  print(response.text)

post()
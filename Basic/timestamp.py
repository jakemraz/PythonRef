import dateutil.parser
import datetime
import time


#date = "2020-{:02d}-{:02d}".format(month, day)

def iso_to_sec():



  iso_string = "2020-05-27 00:00:00.000"
  iso_string = iso_string[:19]
  date=dateutil.parser.parse(iso_string)
  
  timestamp = int(time.mktime(datetime.strptime(iso_string, '%Y-%m-%d %H:%M:%S').timetuple()))
  print(timestamp)
  

def datetime_to_sec():
  KST = datetime.timezone(datetime.timedelta(hours=9))
  sec = int(datetime.datetime(2020,5,4,0,0,0,tzinfo=KST).timestamp())
  print(sec)

def get_time():
  KST = datetime.timezone(datetime.timedelta(hours=9))
  now = datetime.datetime.now(KST)
  print(now.hour)
  print(now.minute)
  print(now.second)

get_time()
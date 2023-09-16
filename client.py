import requests
from datetime import datetime
import numbers
import base64


def en(input):
  return base64.urlsafe_b64encode(bytes(input, "utf-8")).replace(b'=', b'~')


def time2string(time):
  return datetime.strftime(time, timestd)


def ltime(time):
  dif = get_time() - string2time(time)
  newtime = string2time(time) + dif
  return time2string(newtime)


def get_time():
  return datetime.now()


def clean_time(time):
  return time[9:17:]


def string2time(string):
  return datetime.strptime(string, timestd)


# requests routines
def connect(*args):
  username = args[0][0]
  if username == "local":
    return "This username is reserved"
  r = requests.get("http://glitchtech.top:8/connect",
                   params={"username": en(username)})
  result = r.json()
  if result["result"] == 1:
    global localusername
    localusername = username
    return "Connected as %s" % localusername
  else:
    return [
      "This username is already in use",
      "Please wait a few seconds before trying again"
    ]


def join(*args):
  if localusername == "local":
    return "Connect to the server first"
  room = args[0][0]
  r = requests.get("http://glitchtech.top:8/join",
                   params={
                     "username": en(localusername),
                     "room": en(room)
                   })
  result = r.json()
  if result["result"] == 1:
    global localroom
    localroom = room
    return "Connected to %s" % room
  elif result["result"] == 0:
    return "User/Room not found"


def message(msg):
  #cl_write(en(msg))
  r = requests.get("http://glitchtech.top:8/message",
                   params={
                     "username": en(localusername),
                     "message": en(msg)
                   })
  result = r.json()
  if result["result"] == 1:
    return msg
  else:
    return "User/Room not found"


def users(*args):
  r = requests.get("http://glitchtech.top:8/users")
  res = r.json()
  usercount = len(res)
  userlist = [
    "There are %s users online" % usercount,
    "Username        Last Updated        Activity"
  ]
  for user in list(res):
    if isinstance(res[user]["activity"], numbers.Number):
      activity = activitychart[res[user]["activity"]]
    else:
      activity = res[user]["activity"]
    time = clean_time(res[user]["keepalive"])
    userlist.append("%s%s%s" % (user.ljust(16), time.ljust(20), activity))
  return userlist


def keepalive(userid):
  r = requests.get("http://glitchtech.top:8/keepalive",
                   params={"username": en(userid)})
  result = r.json()
  #{'timestamp': '09:10:23:00:12:02:049792', 'author': 'a', 'message': 'ok'}
  #for i in result:
  #  write(i["author"], clean_time(ltime(i["timestamp"])), i["message"])
  return result

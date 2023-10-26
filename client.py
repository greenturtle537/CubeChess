import requests
from datetime import datetime
import numbers
import base64

userheader = "test"


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
def connect(username):
  r = requests.get("http://glitchtech.top:8/connect",
                   params={"username": en(username)})
  result = r.json()
  return result["result"]


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


def keepalive(username):
  r = requests.get("http://glitchtech.top:8/keepalive",
                   params={"username": en(username)})
  result = r.json()
  #{'timestamp': '09:10:23:00:12:02:049792', 'author': 'a', 'message': 'ok'}
  return result


def rooms():
  def rooms(*args):
  r = requests.get("http://glitchtech.top:8/rooms")
  res = r.json()
  roomcount = len(res)
  r = requests.get("http://glitchtech.top:8/users")
  userlist = r.json()
  roomlist = [
      "There are %s rooms open" % roomcount,
      "Room        Last Updated        Users"
  ]
  for room in list(res):
    presentusers = 0
    for user in list(userlist):
      numbercheck = isinstance(userlist[user]["activity"], numbers.Number)
      if not numbercheck and userlist[user]["activity"] == room:
        presentusers += 1
    #time = clean_time(res[room]["lifetime"])
    #Properly store lifetimes serverside first
    time = clean_time(time2string(get_time()))
    roomlist.append("%s%s%s" % (room.ljust(16), time.ljust(20), presentusers))
  return roomlist


def superconnect():
  print("hi")
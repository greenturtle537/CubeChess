import requests


def trycommand(commandtext):
  if commandtext in list(functionmap):
    #functionmap[commandtext]()
    return True
  else:
    return False


def docommand(commandtext, *args):
  return functionmap[commandtext](*args)


#def connect(*args):
#  return "Turn on the WiFi"

functionmap = {
  "connect": connect,
}


# requests routines
def connect(*args):
  username = args[0]
  r = requests.get("http://glitchtech.top:8/connect",
                   params={"username": username})
  result = r.json()
  return result


def users():
  r = requests.get("http://glitchtech.top:8/users")
  req = r.json()
  return req


def keepalive(userid):
  r = requests.get("http://glitchtech.top:8/keepalive",
                   params={"username": userid})
  result = r.json()

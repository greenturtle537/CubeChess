import requests
import base62
from time import sleep


def en(input):
  return base62.encodebytes(bytes(input, "utf-8"))


print("You have connected to GlitchChat")
username = input("Please enter your username: ")


def users():
  r = requests.get("http://glitchtech.top:8/users")
  req = r.json()
  return req


def keepalive(userid):
  r = requests.get("http://glitchtech.top:8/keepalive",
                   params={"username": userid})
  req = r.json()
  return req
r = requests.get("http://glitchtech.top:8/connect",
                 params={"username": username})
req = r.json()
print(req)
#Frameloop sequence ahead, todo error handling
while req["result"]:
  print(keepalive(username))
  sleep(0.5)

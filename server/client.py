import requests
import base62
from time import sleep


def en(input):
  return base62.encodebytes(bytes(input, "utf-8"))


def users():
  r = requests.get("http://glitchtech.top:8/users")
  req = r.json()
  return req


print("You have connected to GlitchChat")
username = input("Please enter your username: ")

r = requests.get("http://glitchtech.top:8/connect",
                 params={"username": username})
req = r.json()
print(req)
#Frameloop sequence ahead, todo error handling
while req["result"]:
  print(users())
  sleep(0.1)

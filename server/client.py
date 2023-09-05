import requests
import base62
from time import sleep
from kbhit import KBHit
from timer import RepeatedTimer
import os
from cursor import show_cursor
from cursor import hide_cursor

print("You have connected to GlitchChat")
username = input("Please enter your username: ")

rows = 30
command = ""

r = requests.get("http://glitchtech.top:8/connect",
                 params={"username": username})
result = r.json()
print(result)


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


def en(input):
  return base62.encodebytes(bytes(input, "utf-8"))


def users():
  r = requests.get("http://glitchtech.top:8/users")
  req = r.json()
  return req


def keepalive(userid):
  r = requests.get("http://glitchtech.top:8/keepalive",
                   params={"username": userid})
  result = r.json()


#Frameloop sequence ahead, todo error handling
buffer = []


def write(message):
  buffer.append(message)
  cleaner()


def cleaner():
  hide_cursor()
  cls()
  print("Command entry with keyboard & return, or ESC to exit")
  for i in range(rows):
    if i < len(buffer):
      print(buffer[i])
    else:
      print("")
  print("$:%s" % command, end="")
  show_cursor()
  if len(buffer) > rows:
    buffer.pop(0)


kb = KBHit()
while True:
  if kb.kbhit():
    c = kb.getch()
    if ord(c) == 27:  # ESC
      break
    if ord(c) == 8:  #Backspace
      command = command[0:len(command) - 2:]
    else:
      command = command + c
  write(keepalive(username))
  sleep(0.5)

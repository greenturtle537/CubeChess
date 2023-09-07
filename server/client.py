import requests
import base62
from time import sleep
from kbhit import KBHit
from timer import RepeatedTimer
import os
from cursor import show_cursor
from cursor import hide_cursor
import time
import sched
import curses
import curses.textpad


#curses routines
def start_curses(instance):
  curses.noecho()
  curses.cbreak()
  stdscr.keypad(True)


def stop_curses(instance):
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()


# requests routines
def connect(username):
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


# misc routines
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


def en(input):
  return base62.encodebytes(bytes(input, "utf-8"))


def center_text(text, y, pad="", attr=curses.A_NORMAL):
  length = len(text)
  stdscr.addstr(y, 0, pad * curses.COLS, attr)
  num = round((curses.COLS / 2) - (length / 2))
  stdscr.addstr(y, num, text, attr)


def write(message):
  buffer.append(message)
  refresh()


def refresh():
  while len(buffer) > curses.LINES - 6:
    buffer.pop(0)
  for i in buffer:
    stdscr.addstr(buffer.index(i) + 3, 0, i)
  stdscr.refresh()


def newmsg(username):
  write(keepalive(username))


def ping(method, args):
  if scheduler.empty():
    scheduler.enter(0.5, 1, method, (args, ))
    scheduler.run()


def counter(placeholder=""):
  global count
  count = count + 1
  write(str(count))


#Code entry

#curses setup
stdscr = curses.initscr()
win = curses.newwin(1, curses.COLS - 10, curses.LINES - 2, 4)
count = 2
stdscr.nodelay(True)

scheduler = sched.scheduler(time.time, time.sleep)
start_curses(stdscr)
buffer = []

center_text("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁", 0, "▓", curses.A_REVERSE)
center_text("| GlitchChat v1.0 |", 1, "▓", curses.A_STANDOUT)
center_text("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔", 2, "▓", curses.A_REVERSE)

center_text("", curses.LINES - 3, "▓")
stdscr.addstr(curses.LINES - 2, 0, "[$]: ")

tb = curses.textpad.Textbox(win, insert_mode=True)

stdscr.refresh()
command = ""
start = time.time()

while True:
  c = stdscr.getch()
  #6text = tb.edit()
  #ping(counter, count)
  if c == 27:  # Codes to escape(esc)
    break  # Exit the while loop
  elif c == curses.KEY_BACKSPACE or c == 127:  #Backspace is encoded as 127/DEL on chromebooks
    command = command[0:len(command) - 1]
    stdscr.addstr(curses.LINES - 2, 5, command + " ")
    stdscr.addstr(curses.LINES - 2, 5,
                  command)  #Wastefully corrects cursor position
  elif c == curses.KEY_ENTER or c == 13 or c == 10:  # Accept carriage return and line feed
    stdscr.addstr(curses.LINES - 2, 5, " " * len(command))
    stdscr.addstr(curses.LINES - 2, 5, "")  #cursor correction
    write(command)
    command = ""
  elif c > 31 and c <= 126:
    command = command + chr(c)
    stdscr.addstr(curses.LINES - 2, 5, command)
  if time.time() - start > 1:
    #write(str(count))
    count = count + 1
    start = time.time()
  stdscr.refresh()
stop_curses(stdscr)

#Frameloop sequence ahead, todo error handling
'''
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
  
'''

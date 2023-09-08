import requests
import base62
from time import sleep
import os
import time
import curses
import curses.textpad
import cmds


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

start_curses(stdscr)
buffer = []

center_text("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁", 0, "▓", curses.A_REVERSE)
center_text("| GlitchChat v1.0 |", 1, "▓", curses.A_STANDOUT)
center_text("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔", 2, "▓", curses.A_REVERSE)

center_text("", curses.LINES - 3, "▓")
stdscr.addstr(curses.LINES - 2, 0, "[$]: ")

stdscr.refresh()
command = ""
start = time.time()
flag = 0

while True:
  # ----- Key Input handlers -----
  c = stdscr.getch()
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
    if len(command) > 0 and command[0] == "/":
      commandls = command.split("/")
      commandls = commandls[1].split(" ")
      if cmds.trycommand(commandls[0]):
        commandout = cmds.docommand(commandls[0], commandls[1::])
        write(commandout)

    command = ""
  elif c > 31 and c <= 126:
    command = command + chr(c)
    stdscr.addstr(curses.LINES - 2, 5, command)
  # ----- Repeated routine handlers -----
  if time.time() - start > 1:
    #write(str(count))
    count = count + 1
    start = time.time()
  # ----- Single routine handlers -----

  stdscr.refresh()
stop_curses(stdscr)

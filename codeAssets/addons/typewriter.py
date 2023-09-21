from time import sleep
from os import system, name

from blessed import Terminal
t = Terminal()


# redefine names
t.rgb = t.color_rgb
t.on_rgb = t.on_color_rgb


# functions

def format(format: str) -> None: print(format, end='')


# def clear() -> None: system('cls' if name == 'nt' else 'clear')
def clear() -> None: print(t.clear)
  
def clearline(y: int) -> None: 
  with t.location(0, y): print(' '*t.width, end='')



def xyprint(string: str, x: int, y: int) -> None:
  with t.location(x, y): print(string, end='')

def xyinput(prompt: str, x: int, y: int) -> str:
  with t.location(x, y): return input(prompt)



def Inkey(timeout: float = 0) -> str:
  with t.cbreak(): 
    if timeout: return t.inkey(timeout=timeout)
    else: return t.inkey()

def RestrictedInkey(AllowedKeys: list, timeout: float = 0.00) -> str:
  with t.cbreak():
    key = ''
    while key not in AllowedKeys: 
      if timeout: key = t.inkey(timeout)
      else: key = t.inkey()
      if key == '': return ''
  return key


# doesn't work with formating
def dprint(string: str, x: int, y: int, delay: float = .00, dx: int = 1, dy: int = 0):
  if delay: 
    for char in string:
      with t.location(x, y): print(char, end='')
      x += dx; y+= dy; sleep(delay)
  else: 
    for char in string:
      with t.location(x, y): print(char, end='')
      x += dx; y+= dy



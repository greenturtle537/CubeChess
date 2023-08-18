_rgb = _rgba = ''

# random color
from random import randint as ri
def rand(minr: int = 0, ming: int = 0, minb: int = 0, maxr: int = 255, maxg: int = 255, maxb: int = 255) -> list: return [ri(minr, maxr), ri(ming, maxg), ri(minb, maxb)]

# basic four opperaters for rgb colors
def add_rgb(mod1: _rgb, mod2: _rgb): return [mod1[0]+mod2[0], mod1[1]+mod2[1], mod1[2]+mod2[2]]

def sub_rgb(mod1: _rgb, mod2: _rgb): return [mod1[0]-mod2[0], mod1[1]-mod2[1], mod1[2]-mod2[2]]

def mul_rgb(mod1: _rgb, mod2: _rgb): return [mod1[0]*mod2[0], mod1[1]*mod2[1], mod1[2]*mod2[2]]

def div_rgb(mod1: _rgb, mod2: _rgb): return [mod1[0]+mod2[0], mod1[1]+mod2[1], mod1[2]+mod2[2]]

# RGB class
class RGB:
  def __init__(self, r: int, g: int, b: int):
    self.value = [r, g, b]

  def __str__(self): return f'[{self.value[0]}, {self.value[1]}, {self.value[2]}]'

  def __add__(self, mod: _rgb or int): 
    if type(mod) == RGB: return [self.value[i]+mod.value[i] for i in range(3)]
    elif type(mod) == int: return [self.value[i]+mod for i in range(3)]

  def __sub__(self, mod: _rgb or int): 
    if type(mod) == RGB: return [self.value[i]-mod.value[i] for i in range(3)]
    elif type(mod) == int: return [self.value[i]-mod for i in range(3)]

  def __mul__(self, mod: _rgb or int): 
    if type(mod) == RGB: return [self.value[i]*mod.value[i] for i in range(3)]
    elif type(mod) == int: return [self.value[i]*mod for i in range(3)]

  def __truediv__(self, mod: _rgb or int):
    if type(mod) == RGB: return [self.value[i]/mod.value[i] for i in range(3)]
    elif type(mod) == int: return [self.value[i]/mod for i in range(3)]

  def __pow__(self, mod: _rgb or int): 
    if type(mod) == RGB: return [self.value[i]**mod.value[i] for i in range(3)]
    elif type(mod) == int: return [self.value[i]**mod for i in range(3)]

# complex rgb functions
def BiGradient_rgb(colorA: _rgb, colorB: _rgb, steps: int) -> list:
  d = [(colorB[i]-colorA[i])/(steps-1) for i in range(3)]
  return [[round(colorA[o]+d[o]*i) for o in range(3)] for i in range(steps)]
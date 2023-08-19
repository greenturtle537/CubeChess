import codeAssets.addons.typewriter as type
import codeAssets.addons.easyjson as json
import codeAssets.addons.colorcalc as colorcalc


# global main game vars
Pieces = []

class Board:
  def __init__(self, array):
    self.validlocations = []
    for y in range(len(array)):
      for x in range(len(array[y])):
        if array[y][x] == 1: self.validlocations.append((x,y))



Pieces = []
class piece:
  def __init__(self, movePaths: tuple[tuple[2]], attackPaths: tuple[tuple[2]], id: str):
    Pieces.append(self)
    self.movePath = ()
    self.attackPath = ()
    self.id = ()
    self.coords = ()

  def remove(self): Pieces.remove(self)

  def getattacked(self, attackedfrom: tuple[2]): pass
  def attackAction(self): pass
  def specialAction(self, tile: tuple[2]): pass



def ReadMods():
  global dmLines
  with open('game/mods','r') as dotmods: 
    dmLines = [line.replace('\n','') for line in dotmods.readlines()]; dotmods.close()
  for i in range(len(dmLines)):
    if dmLines[i][0] == 'p': dmLines[i] = 'game/modData/' + dmLines[i] + '.piece'; continue
    if dmLines[i][0] == 'b': dmLines[i] = 'game/modData/' + dmLines[i] + '.board'; continue
    if dmLines[i][0] == 'c': pass #needs work hard coded classes


def LoadMods():
  print(type.t.mediumseagreen)
  for line in dmLines:
    try:
      if line[0] == 'c': pass #hard coded classes
      else:
        with open(line,'r') as modfile:
          pass
      print(f"successfully loaded mod file {line}")
    except: print(f"{type.t.red}error loading mod file '{line}'{type.t.white}"); input(type.t.white + 'all mods loaded\n\n\n')


def LoadSettings(): 
  data = json.GetDict('game/settings')
  global board
  b = json.GetDict(f"game/modData/boards/{data['board']}.board")
  board = Board(b['array'])
  for y in range(len(b['array'][data['setup']])):
    for x in range(len(b['array'][data['setup']][y])):
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
      pass # interpret pieces
  
  


def StartGame(): 
  type.clear()

def GetPlayer1Action(): pass

def GetPlayer2Action(): pass

def ServerProcess1(): pass
def ServerProcess2(): pass

# ReadMods()
# LoadMods()
# LoadSettings()


def PrintBoard():
  board = type.t.bold + type.t.rgb(220,220,220) + """
   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   │         │         │         │         │         │         │         │         │
   ╰─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────╯
""" + type.t.normal


  type.xyprint(board, 0, 0)

  # for i in range(8):
  #   type.xyprint(type.t.mediumseagreen + 'RNBQKBNR'[i], 8+10*i, 3)
  #   type.xyprint(type.t.mediumseagreen + 'P', 8+10*i, 7)
  #   type.xyprint(type.t.indianred + 'RNBQKBNR'[i], 8+10*i, 31)
  #   type.xyprint(type.t.indianred + 'P', 8+10*i, 27)
  # with type.t.hidden_cursor(): type.xyinput('',0,0)


def DrawPieces():
  for piece in Pieces:
    type.xyprint(piece.char, 8+10*piece.pos[0], 3+4*piece.pos[1])







# gameplay

LoadSettings()

StartGame()
PrintBoard()
DrawPieces()


# while True:
#   GetPlayer1Action()
#   ServerProcess1()
  



# class pawn(piece):
#   def __init__(self):
#     self.movePath = ((0,1))
#     self.attackPath = ((-1,1),(1,1))
#   def onAttacked(self): pass
#   def Attack(self, tile): pass






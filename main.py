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
  for y in range(len(b['setup'][data['setup']])):
    for x in range(len(b['setup'][data['setup']][y])):
      piq = b['setup'][data['setup']][y][x]
  
  


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
  TeamColor1 = type.t.rgb(220,50,50)
  TeamColor2 = type.t.rgb(50,220,50)
  BoardColor1 = type.t.rgb(155, 130, 0)
  BoardColor2 = type.t.rgb(155, 130, 0)
  board = type.t.rgb(200,200,200) + """
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

  
  # prints the board multi-line string
  type.xyprint(board, 0, 0)


  # # prints the square character at each valid piece location
  # for x in range(8):
  #   for y in range(8):
  #     type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}⬞', 8+10*x, 3+4*y)

  # for i in range(8):
  #   type.xyprint(TeamColor1 + 'RNBQKBNR'[i], 8+10*i, 3)
  #   type.xyprint(TeamColor1 + 'P', 8+10*i, 7)
  #   type.xyprint(TeamColor2 + 'RNBQKBNR'[i], 8+10*i, 31)
  #   type.xyprint(TeamColor2 + 'P', 8+10*i, 27)
  # with type.t.hidden_cursor(): type.xyinput('',0,0)



# a function to draw pieces
def DrawPieces():
  for piece in Pieces:
    type.xyprint(piece.char, 8+10*piece.pos[0], 3+4*piece.pos[1])




board = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 0, 0, 1],
  [1, 1, 0, 1, 1, 0, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1]
]









##### gameplay

LoadSettings()

StartGame()
PrintBoard()
DrawPieces()




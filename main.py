import codeAssets.addons.typewriter as ttype
import codeAssets.addons.easyjson as json
import codeAssets.addons.colorcalc as colorcalc
from time import sleep



def ReadMods():
  global dmLines
  with open('game/mods','r') as dotmods: 
    dmLines = [line.replace('\n','') for line in dotmods.readlines()]; dotmods.close()
  for i in range(len(dmLines)):
    if dmLines[i][0] == 'p': dmLines[i] = 'game.modData.' + dmLines[i].replace('/','.'); continue
    if dmLines[i][0] == 'b': dmLines[i] = 'game/modData/' + dmLines[i] + '.board'; continue
    if dmLines[i][0] == 'c': pass #needs work hard coded classes


def LoadMods():
  global PieceById; PieceById = {}
  global PieceIds; PieceIds = []
  # check if debugOnBoot is on
  debugOnBoot = json.GetDict('game/settings')['debugOnBoot']
  if debugOnBoot: print(ttype.t.mediumseagreen)
  for line in dmLines:
    try:
      if '/' in line:
        with open(line,'r') as modfile: pass
        if debugOnBoot: print(f"successfully loaded mod file {line}")
      elif '.' in line: 
        name = line[line.find('.',line.find('.',line.find('.')+1)+1)+1:]
        exec(f"import {line} as {name}"); exec(f"PieceIds.append('{eval(name).char}')"); exec("PieceById.update({'char': 1})".replace('1',name). replace('char',eval(name).char))
    except: print(f"{ttype.t.red}error loading mod file '{line}'{ttype.t.white}")




def LoadSettings(): 
  data = json.GetDict('game/settings') # gets the settings file
  if data['debugOnBoot']: print(ttype.t.rgb(0,100,0))
  global board, cornerBoard # global some variables for later use in other functions
  b = json.GetDict(f"game/modData/boards/{data['board']}.board") # loads the board file
  board = b['array'] # loads the array from the .board file
  for y in range(len(b['setup'][data['setup']])):
    for x in range(len(b['setup'][data['setup']][y])):
      piq = b['setup'][data['setup']][y][x]
      # check if piece id/char is in list of loaded ones
      if piq[1] in PieceIds: 
        piece(x, y, PieceById[piq[1]], int(piq[0]))
        if data['debugOnBoot']: print(f'successfully placed piece id {piq[1]} at position ({x},{y})')
      elif piq[1] == ' ': continue
      elif data['debugOnBoot']: print(f'{ttype.t.red}could not place piece id {piq[1]} at position ({x},{y}){ttype.t.rgb(0,100,0)}')
      
  # make the cornerboard - 1 larger in width and height than board cause corner-count math
  cornerBoard = [[0b0000 for x in range(len(board[y])+1)] for y in range(len(board))]
  cornerBoard.append(cornerBoard[-1].copy())

  # fill the cornerboards data with 4bit numbers corresponding to adjacent tile existences
  for y in range(len(cornerBoard)):
    for x in range(len(cornerBoard[y])):
      if y-1 in range(len(board)) and x-1 in range(len(board[y-1])):
        if board[y-1][x-1] in [1,2,3]: cornerBoard[y][x] += 0b1000
      if y in range(len(board)) and x-1 in range(len(board[y])):
        if board[y][x-1] in [1,2,3]: cornerBoard[y][x] += 0b0100
      if y in range(len(board)) and x in range(len(board[y])):
        if board[y][x] in [1,2,3]: cornerBoard[y][x] += 0b0010
      if y-1 in range(len(board)) and x in range(len(board[y-1])):
        if board[y-1][x] in [1,2,3]: cornerBoard[y][x] += 0b0001





# a function to draw pieces
def DrawPieces():
  for piece in Pieces:
    ttype.xyprint(piece.char, 7+10*piece.pos[0], 3+4*piece.pos[1])




def PrintBoard():
 with ttype.t.hidden_cursor():
  corners = ' ╰╭├╮┼┬┼╯┴┼┼┤┼┼┼'
  # print cell func to print single cell at a time, just for testing getting stuff in correct positions
  def PrintCell(x, y):
    ttype.xyprint(' ───────── ',x,y)
    for i in range(1,4): ttype.xyprint('│         │',x,y+i)
    ttype.xyprint(' ───────── ',x,y+4)

  # sets the printing format to the board grayish color
  print(ttype.t.rgb(180,180,180))
   
  # prints the lines
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] in [1,2,3]: PrintCell(2+10*x, 1+4*y)
  # prints the corners
  for y in range(len(cornerBoard)):
    for x in range(len(cornerBoard[y])): 
      if cornerBoard[y][x] > 0: ttype.xyprint(corners[cornerBoard[y][x]], 2+10*x, 1+4*y)
  # returns printing format to normal
  print(ttype.t.normal)


  # board styling for showing what's available space and what's a gap
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] in [1,2,3]: ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*x, 4+4*y)








def SelectBoardSpace():
  selected1 = None
  with ttype.t.hidden_cursor():
   while True:
    x, y = boardSelection[0], boardSelection[1]
     # draw where the cursor is
     
    ttype.xyprint(f'{ttype.t.rgb(0,255,255)}╭ ╮', 6+10*x, 2+4*y); ttype.xyprint(f'{ttype.t.rgb(0,255,255)}╰ ╯', 6+10*x, 4+4*y)

    # get a keypress
    inkey = ttype.RestrictedInkey(['w', 'a', 's', 'd', 'e', ' ','\n', 'r', 'W', 'A', 'S', 'D'])
     
    # draw over where the cursor was
    try: 
      if board[y][x] in [1,2,3]: ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*x, 4+4*y)
      else: ttype.xyprint(f'   ', 6+10*x, 2+4*y); ttype.xyprint(f'   ', 6+10*x, 4+4*y)
    except: ttype.xyprint(f'   ', 6+10*x, 2+4*y); ttype.xyprint(f'   ', 6+10*x, 4+4*y)

    # draw where selected1 is (if it isn't None)
    if selected1 != None: ttype.xyprint(f'{ttype.t.rgb(0,180,255)}╭ ╮', 6+10*selected1[0], 2+4*selected1[1]); ttype.xyprint(f'{ttype.t.rgb(0,180,255)}╰ ╯', 6+10*selected1[0], 4+4*selected1[1])

    # interact based on keypress
    if inkey == 'W': boardSelection[1] = 0
    elif inkey == 'A': boardSelection[1] = len(board)-1
    elif inkey == 'S': boardSelection[0] = 0
    elif inkey == 'D': boardSelection[0] = len(board[boardSelection[1]])-1
    elif inkey == 'w' and y > 0: boardSelection[1] -= 1
    elif inkey == 's' and y < len(board)-1: boardSelection[1] += 1
    elif inkey == 'a' and x > 0: boardSelection[0] -= 1
    elif inkey == 'd' and x < 7: boardSelection[0] += 1
    elif inkey == 'r': ttype.clear(); PrintBoard(); DrawPieces()

    if inkey in ['e',' ','\n']: 
      if selected1 == None: 
        if board[y][x] in [1,2,3]: selected1 = (x,y)
      elif board[y][x] in [1,2,3]: 
        ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*selected1[0], 2+4*selected1[1]); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*selected1[0], 4+4*selected1[1])
        return [selected1, (x,y)]
        
        
    






def InitFunctionRecallVars():
  global TeamColor1, TeamColor2, BoardColor1, BoardColor2
  TeamColor1 = ttype.t.rgb(220,50,50)
  TeamColor2 = ttype.t.rgb(50,220,50)
  BoardColor1 = ttype.t.bold+ttype.t.rgb(125, 110, 0)
  BoardColor2 = ttype.t.rgb(185, 160, 0)

def InitSelector():
  global boardSelection
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] in [1,2,3]: boardSelection = [x,y]; break
    else: break








def PieceAt(x, y):
  for piece in Pieces:
    if piece.pos == (x,y) or piece.pos == [x,y]: return True, piece
  else: return False, dummypiece()


def CheckDirection(pOld, pNew):
  # straight detection
  if pOld[0] < pNew[0] and pOld[1] == pNew[1]: return 'right'
  if pOld[0] > pNew[0] and pOld[1] == pNew[1]: return 'left'
  if pOld[0] == pNew[0] and pOld[1] < pNew[1]: return 'down'
  if pOld[0] == pNew[0] and pOld[1] > pNew[1]: return 'up'
  # diagonal detection
  diag = abs(pNew[0]-pOld[0]) == abs(pNew[1]-pOld[1])
  if diag and pNew[0] > pOld[0] and pNew[1] < pOld[1]: return 'up-right'
  if diag and pNew[0] < pOld[0] and pNew[1] < pOld[1]: return 'up-left'
  if diag and pNew[0] < pOld[0] and pNew[1] > pOld[1]: return 'down-left'
  if diag and pNew[0] > pOld[0] and pNew[1] > pOld[1]: return 'down-right'
  # raw vector
  return (pNew[0]-pOld[0], pNew[1]-pOld[1])



def GetPieceMove():
  while True:
    selection = SelectBoardSpace()

    # if you select 2 different squares and the first one is a piece
    if selection[0] != selection[1] and PieceAt(selection[0][0], selection[0][1])[0]:
      piece = PieceAt(selection[0][0], selection[0][1])[1]
      direction = CheckDirection(selection[0], selection[1])
      vector = (selection[1][0]-selection[0][0], selection[1][1]-selection[0][1])
      # moving code
      if ((direction in piece.movePath) or (vector in piece.movePath) or (direction in CheckConditionals('move', piece)) or (vector in CheckConditionals('move', piece))) and (not PieceAt(selection[1][0], selection[1][1])[0]): 
        piece.erase(); piece.move(selection[1]); piece.draw(); return
      # attacking code
      elif ((direction in piece.attackPath) or (vector in piece.attackPath) or (direction in CheckConditionals('attk', piece)) or (vector in CheckConditionals('attk', piece))) and (PieceAt(selection[1][0], selection[1][1])[0]):
        # if piece.color == 2: PieceAt(selection[1][0], selection[1][1])[1].remove()
        # piece.erase(); piece.move(selection[1]); piece.draw()
        # if piece.color == 1: PieceAt(selection[1][0], selection[1][1])[1].remove()
        for p in Pieces:
          if tuple(p.pos) == tuple(selection[1]) and p != piece: piece.erase(); piece.move(selection[1]); piece.draw(); p.remove(); return



def ReversePieceDirection(dir):
  # string-based directions
  if type(dir) == str: 
    oDir = dir
    if 'up' in oDir: dir = dir.replace('up','down')
    if 'down' in oDir: dir = dir.replace('down','up')
    if 'left' in oDir: dir = dir.replace('left','right')
    if 'right' in oDir: dir = dir.replace('right','left')
    return dir
  # vector-based directions
  if type(dir) == tuple: return (dir[0], -dir[1])


# condition move list resulter
def CheckConditionals(type, piece): return [i[0] if i[1](piece, Board, Game) else None for i in (piece.conditionalMovePath if type == 'move' else piece.conditionalAttackPath)]



# predefine the piece class so when the Board class refrences a piece object it doesn't say the piece is undefined
class piece: pass
  
# board class stores functions for writing custom pieces
class Board:
  def _defvars(self): self.array = board
  def PieceAt(self, x: int, y: int) -> tuple[bool, piece]: return PieceAt(x,y)
  def TileAt(self, x: int, y: int) -> int: return board[y][x]
  def IsTileAT(self, x: int, y: int) -> bool: return board[y][x] > 0
Board = Board()

# game class stores generic game data for custom pieces
class Game:
  def __init__(self): self.turn = 0
Game = Game()

# global main game vars
Pieces = []
class piece:
  def __init__(self, x, y, data, color):
    Pieces.append(self)
    self.attackPath = data.attackPath
    self.movePath = data.movePath
    self.pawnPromote = data.pawnPromote
    self.canJumpPieces = data.canJumpPieces
    self.canJumpEmpty = data.canJumpEmpty
    self.char = (TeamColor1 if color-1 else TeamColor2) + data.char + ttype.t.normal
    self.id = data.char
    self.pos = [x, y]
    self.color = color
    self.conditionalMovePath = data.conditionalMovePath
    self.conditionalAttackPath = data.conditionalAttackPath
    self.pastMoves = [self.pos]
    self.onMove = data.onMove


    if self.color == 2: 
      newAtkPath = []; newMovePath = []; newConditionalMovePath = []; newConditionalAttackPath = []
      for i in range(len(self.attackPath)): newAtkPath.append(ReversePieceDirection(self.attackPath[i]))
      for i in range(len(self.movePath)): newMovePath.append(ReversePieceDirection(self.movePath[i]))
      for i in range(len(self.conditionalMovePath)): newConditionalMovePath.append((ReversePieceDirection(self.conditionalMovePath[i][0]), self.conditionalMovePath[i][1]))
      for i in range(len(self.conditionalAttackPath)): newConditionalAttackPath.append((ReversePieceDirection(self.conditionalAttackPath[i][0]), self.conditionalAttackPath[i][1]))
      self.attackPath = newAtkPath; self.movePath = newMovePath; self.conditionalMovePath = newAtkPath; self.conditionalMovePath = newConditionalMovePath
      
  def erase(self): ttype.xyprint(' ', 7+10*self.pos[0], 3+4*self.pos[1])
  def draw(self): ttype.xyprint(self.char, 7+10*self.pos[0], 3+4*self.pos[1])
  def remove(self): self.erase(); Pieces.remove(self)
  def move(self, newPos):
    oldPos = self.pos
    self.pos = newPos
    self.pastMoves.append((self.pos,Game.turn,(newPos[0]-oldPos[0], newPos[1]-oldPos[1])))
    self.onMove(self, Game, Board, Pieces, oldPos, newPos)



class dummypiece:
  def __init__(self):
    self.attackPath = self.movePath = []
    self.conditionalAttackPath = self.conditionalMovePath = []
    self.pawnPromote = False
    self.canJumpPieces = self.canJumpEmpty = True
    self.char = self.id = '⚠'
    self.pastMoves = [((63,63),-1,(63,63))]

  def __bool__(self): return False





def Run():
  with ttype.t.hidden_cursor(), ttype.t.cbreak():
    InitFunctionRecallVars()
    ReadMods()
    LoadMods()
    LoadSettings(); sleep(1)
    InitSelector()

    Board._defvars()
    
    ttype.clear()
    
    
    PrintBoard()
    DrawPieces()
    while True:
      Game.turn += 1
      ttype.xyprint(f'{ttype.t.rgb(160,160,160)}Turn: {Game.turn}', 0, 0)
      GetPieceMove()
      DrawPieces()
    


if __name__ == '__main__': Run()


ttype.xyinput('>>> ', 0, ttype.t.height-1)
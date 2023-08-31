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
  from types import ModuleType as module
  global PieceById; PieceById = {}
  global PieceIds; PieceIds = []
  print(ttype.t.mediumseagreen)
  for line in dmLines:
    # try:
      if line[0] == 'c': pass #hard coded classes
      elif '/' in line:
        with open(line,'r') as modfile: pass
        print(f"successfully loaded mod file {line}")
      elif '.' in line: 
        name = line[line.find('.',line.find('.',line.find('.')+1)+1)+1:]
        exec(f"import {line} as {name}")
        exec(f"PieceIds.append('{eval(name).char}')")
        exec("PieceById.update({'char': 1})".replace('1',name). replace('char',eval(name).char))

    # except: print(f"{ttype.t.red}error loading mod file '{line}'{ttype.t.white}")


def LoadSettings(): 
  print(ttype.t.rgb(0,100,0))
  data = json.GetDict('game/settings') # gets the settings file
  global board, cornerBoard # global some variables for later use in other functions
  b = json.GetDict(f"game/modData/boards/{data['board']}.board") # loads the board file
  board = b['array'] # loads the array from the .board file
  for y in range(len(b['setup'][data['setup']])):
    for x in range(len(b['setup'][data['setup']][y])):
      piq = b['setup'][data['setup']][y][x]
      if piq[1] in PieceIds: piece(x, y, PieceById[piq[1]], int(piq[0])); print(f'successfully placed piece id {piq[1]} at position ({x},{y})')
      elif piq[1] == ' ': continue
      else: print(f'could not place piece id {piq[1]} at position ({x},{y})')
      


  # make the cornerboard - 1 larger in width and height than board cause corner-count math
  cornerBoard = [[0b0000 for x in range(len(board[y])+1)] for y in range(len(board))]
  cornerBoard.append(cornerBoard[-1].copy())

  # fill the cornerboards data with 4bit numbers corresponding to adjacent tile existences
  for y in range(len(cornerBoard)):
    for x in range(len(cornerBoard[y])):
      if y-1 in range(len(board)) and x-1 in range(len(board[y-1])):
        if board[y-1][x-1] == 1: cornerBoard[y][x] += 0b1000
      if y in range(len(board)) and x-1 in range(len(board[y])):
        if board[y][x-1] == 1: cornerBoard[y][x] += 0b0100
      if y in range(len(board)) and x in range(len(board[y])):
        if board[y][x] == 1: cornerBoard[y][x] += 0b0010
      if y-1 in range(len(board)) and x in range(len(board[y-1])):
        if board[y-1][x] == 1: cornerBoard[y][x] += 0b0001





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
      if board[y][x] == 1: PrintCell(2+10*x, 1+4*y)
  # prints the corners
  for y in range(len(cornerBoard)):
    for x in range(len(cornerBoard[y])): 
      if cornerBoard[y][x] > 0: ttype.xyprint(corners[cornerBoard[y][x]], 2+10*x, 1+4*y)
  # returns printing format to normal
  print(ttype.t.normal)


  # board styling for showing what's available space and what's a gap
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] == 1: 
        # # style 1
        # ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭   ╮', 5+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰   ╯', 5+10*x, 4+4*y)
        # # style 2
        # ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭     ╮', 4+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰     ╯', 4+10*x, 4+4*y)
        # # style 3
        # ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◜   ◝', 5+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◟   ◞', 5+10*x, 4+4*y)
        # style 4
        # ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◜     ◝', 4+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◟     ◞', 4+10*x, 4+4*y)
        # # style 5
        ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*x, 4+4*y)








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
      if board[y][x] == 1: ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*x, 2+4*y); ttype.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*x, 4+4*y)
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
        if board[y][x] == 1: selected1 = (x,y)
      elif board[y][x] == 1: 
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
      if board[y][x] == 1: boardSelection = [x,y]; break
    else: break









def PieceAt(x, y):
  for piece in Pieces:
    if piece.pos == [x,y]: return True, piece
  else: return False, False


def CheckDirection(pOld, pNew):
  if pOld[0] < pNew[0] and pOld[1] == pNew[1]: return 'right'
  if pOld[0] > pNew[0] and pOld[1] == pNew[1]: return 'left'
  if pOld[0] == pNew[0] and pOld[1] < pNew[1]: return 'down'
  if pOld[0] == pNew[0] and pOld[1] > pNew[1]: return 'up'
  return (pNew[0]-pOld[0], pNew[1]-pOld[1])



def GetPieceMove():
  while True: 
    selection = SelectBoardSpace()
    ttype.xyprint('              ', 0, 35)

    if selection[0] != selection[1]:
      if PieceAt(selection[0][0], selection[0][1])[0]:
        piece = PieceAt(selection[0][0], selection[0][1])[1]
        
        if PieceAt(selection[1][0], selection[1][1])[0] and CheckDirection(selection[0], selection[1]) in piece.attackPath: PieceAt(selection[1][0], selection[1][1])[1].remove(); piece.eraseSelf(); piece.pos = list(selection[1]); piece.drawSelf()
          
        elif (CheckDirection(selection[0], selection[1]) in piece.movePath or (selection[1][0]-selection[0][0], selection[1][1]-selection[0][1]) in piece.movePath) and (not PieceAt(selection[1][0], selection[1][1])[0]): piece.eraseSelf(); piece.pos = list(selection[1]); piece.drawSelf()








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
    self.pos = [x, y]
    self.color = color
    if color == 2:
      for i in range(len(self.attackPath)): 
        if type(self.attackPath[i][1]) == int: self.attackPath[i] = (self.attackPath[i][0], -self.attackPath[i][1])
        elif self.attackPath[i] in ['up','down','left','right']: self.attackPath[i] = ['right','left','down','up'][['up','down','left','right'].index(self.attackPath[i])]
      
      for i in range(len(self.movePath)): 
        if type(self.movePath[i][1]) == int: self.movePath[i] = (self.movePath[i][0], -self.movePath[i][1])
        elif self.movePath[i] in ['up','down','left','right']: self.movePath[i] = ['right','left','down','up'][['up','down','left','right'].index(self.movePath[i])]

  def eraseSelf(self): ttype.xyprint(' ', 7+10*self.pos[0], 3+4*self.pos[1])
  def drawSelf(self): ttype.xyprint(self.char, 7+10*self.pos[0], 3+4*self.pos[1])
  def remove(self): Pieces.remove(self)







# ##### gameplay
InitFunctionRecallVars()
ReadMods()
LoadMods()
LoadSettings(); sleep(1)
InitSelector()

ttype.clear()

with ttype.t.hidden_cursor(), ttype.t.cbreak():
  PrintBoard()
  DrawPieces()
  while True:
    GetPieceMove()
    DrawPieces()


ttype.xyinput('>>> ', 0, ttype.t.height-1)
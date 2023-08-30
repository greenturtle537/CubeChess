import codeAssets.addons.typewriter as type
import codeAssets.addons.easyjson as json
import codeAssets.addons.colorcalc as colorcalc


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
    self.pos = [x, y]
    self.color = 0 or 1



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
  data = json.GetDict('game/settings') # gets the settings file
  global board, cornerBoard # global some variables for later use in other functions
  b = json.GetDict(f"game/modData/boards/{data['board']}.board") # loads the board file
  board = b['array'] # loads the array from the .board file
  for y in range(len(b['setup'][data['setup']])):
    for x in range(len(b['setup'][data['setup']][y])):
      piq = b['setup'][data['setup']][y][x]

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
    type.xyprint(piece.char, 8+10*piece.pos[0], 3+4*piece.pos[1])







def PrintBoard():
 with type.t.hidden_cursor():
  corners = ' ╰╭├╮┼┬┼╯┴┼┼┤┼┼┼'
  # print cell func to print single cell at a time, just for testing getting stuff in correct positions
  def PrintCell(x, y):
    type.xyprint(' ───────── ',x,y)
    for i in range(1,4): type.xyprint('│         │',x,y+i)
    type.xyprint(' ───────── ',x,y+4)

  # sets the printing format to the board grayish color
  print(type.t.rgb(180,180,180))
   
  # prints the lines
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] == 1: PrintCell(2+10*x, 1+4*y)
  # prints the corners
  for y in range(len(cornerBoard)):
    for x in range(len(cornerBoard[y])): 
      if cornerBoard[y][x] > 0: type.xyprint(corners[cornerBoard[y][x]], 2+10*x, 1+4*y)
  # returns printing format to normal
  print(type.t.normal)


  # board styling for showing what's available space and what's a gap
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] == 1: 
        # # style 1
        # type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭   ╮', 5+10*x, 2+4*y); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰   ╯', 5+10*x, 4+4*y)
        # # style 2
        # type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭     ╮', 4+10*x, 2+4*y); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰     ╯', 4+10*x, 4+4*y)
        # # style 3
        # type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◜   ◝', 5+10*x, 2+4*y); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◟   ◞', 5+10*x, 4+4*y)
        # style 4
        # type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◜     ◝', 4+10*x, 2+4*y); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}◟     ◞', 4+10*x, 4+4*y)
        # # style 5
        type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*x, 2+4*y); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*x, 4+4*y)








def SelectBoardSpace():
  selected1 = None
  with type.t.hidden_cursor():
   while True:
    x, y = boardSelection[0], boardSelection[1]
     # draw where the cursor is
     
    type.xyprint(f'{type.t.rgb(0,255,255)}╭ ╮', 6+10*x, 2+4*y); type.xyprint(f'{type.t.rgb(0,255,255)}╰ ╯', 6+10*x, 4+4*y)

    # get a keypress
    inkey = type.RestrictedInkey(['w', 'a', 's', 'd', 'e', ' ','\n'])
     
    # draw over where the cursor was
    try: 
      if board[y][x] == 1: type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*x, 2+4*y); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*x, 4+4*y)
      else: type.xyprint(f'   ', 6+10*x, 2+4*y); type.xyprint(f'   ', 6+10*x, 4+4*y)
    except: type.xyprint(f'   ', 6+10*x, 2+4*y); type.xyprint(f'   ', 6+10*x, 4+4*y)

    # draw where selected1 is (if it isn't None)
    if selected1 != None: type.xyprint(f'{type.t.rgb(0,180,255)}╭ ╮', 6+10*selected1[0], 2+4*selected1[1]); type.xyprint(f'{type.t.rgb(0,180,255)}╰ ╯', 6+10*selected1[0], 4+4*selected1[1])

    # interact based on keypress
    if inkey == 'w' and y > 0: boardSelection[1] -= 1
    if inkey == 's' and y < len(board)-1: boardSelection[1] += 1
    if inkey == 'a' and x > 0: boardSelection[0] -= 1
    if inkey == 'd' and x < 7: boardSelection[0] += 1

    if inkey in ['e',' ','\n']: 
      if selected1 == None: 
        if board[y][x] == 1: selected1 = (x,y)
      elif board[y][x] == 1: 
        type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╭ ╮', 6+10*selected1[0], 2+4*selected1[1]); type.xyprint(f'{BoardColor1 if ((x%2)+(y%2))%2 else BoardColor2}╰ ╯', 6+10*selected1[0], 4+4*selected1[1])
        return [selected1, (x,y)]
        
        
    






def InitFunctionRecallVars():
  global boardSelection
  for y in range(len(board)):
    for x in range(len(board[y])):
      if board[y][x] == 1: boardSelection = [x,y]; break
    else: break
  

  global TeamColor1, TeamColor2, BoardColor1, BoardColor2
  TeamColor1 = type.t.rgb(220,50,50)
  TeamColor2 = type.t.rgb(50,220,50)
  BoardColor1 = type.t.bold+type.t.rgb(125, 110, 0)
  BoardColor2 = type.t.rgb(185, 160, 0)



# ##### gameplay

LoadSettings()
InitFunctionRecallVars()

with type.t.hidden_cursor(), type.t.cbreak():
 PrintBoard()
 while True: type.xyprint(SelectBoardSpace(), 0, 40)


type.xyinput('>>> ', 0, type.t.height-1)
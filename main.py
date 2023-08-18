import codeAssets.addons.typewriter as type
import codeAssets.addons.easyjson as json
import codeAssets.addons.colorcalc as colorcalc


# global main game vars
Pieces = []

class Board:
  def __init__(self, validlocations: tuple[tuple]):
    self.validlocations = validlocations
    



Pieces = []
class piece:
  def __init__(self, movePaths: tuple[tuple[2]], attackPaths: tuple[tuple[2]], id: str):
    Pieces.append(self)
    self.movePath = ()
    self.attackPath = ()
    self.id = ()
    self.coords = ()

  def remove(self): Pieces.remove(self)





def ReadMods():
  global dmLines
  with open('game/.mods','r') as dotmods: 
    dmLines = [line.replace('\n','') for line in dotmods.readlines()]; dotmods.close()
  for i in range(len(dmLines)):
    if dmLines[i][0] == 'p': dmLines[i] = 'game/modData/' + dmLines[i] + '.piece'; continue
    if dmLines[i][0] == 'b': dmLines[i] = 'game/modData/' + dmLines[i] + '.board'; continue
      

def LoadMods():
  with open('game/.settings','r') as dotsettings:
    dmLines = [line.replace('\n','') for line in dotsettings.readlines()]; dotsettings.close()

ReadMods()








# class pawn(piece):
#   def __init__(self):
#     self.movePath = ((0,1))
#     self.attackPath = ((-1,1),(1,1))
#   def onAttacked(self): pass
#   def Attack(self, tile): pass






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






# class pawn(piece):
#   def __init__(self):
#     self.movePath = ((0,1))
#     self.attackPath = ((-1,1),(1,1))
#   def onAttacked(self): pass
#   def Attack(self, tile): pass






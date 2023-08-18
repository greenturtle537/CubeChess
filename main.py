import codeAssets.addons.typewriter as type
import codeAssets.addons.easyjson as json
import codeAssets.addons.colorcalc as colorcalc


# global main game vars
Pieces = []
Board = []





Pieces = []
class piece:
  def __init__(self, place: tuple[2]):
    self.movePath = ((0,0))
    self.attackPath = ((0,0))
    self.coords = []

  def remove(self): Pieces.remove(self)



class pawn(piece):
  def __init__(self):
    self.movePath = ((0,1))
    self.attackPath = ((-1,1),(1,1))

  def onAttacked(self): pass

  def Attack(self, tile): pass






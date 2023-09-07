attackPath = []
movePath = [(1,-1),(-1,-1)]
canPromote = True
canJumpPieces = True
canJumpEmpties = True
char = 'c'
promotesTo = ['C']

conditionalMovePath = [
  ((-2,-2), lambda p, b, g: b.PieceAt(p.pos[0]-1, p.pos[1]-1)[1]),
  ((-2,-2), lambda p, b, g: b.PieceAt(p.pos[0]+1, p.pos[1]+1)[1])
]
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): 
  if self.pastMoves[-1][2] == (-2,-2*(-1 if self.color-1 else 1)): p = board.PieceAt(newPos[0]+1, newPos[1]+1)[1]; p.erase(); p.remove()
  elif self.pastMoves[-1][2] == (2,-2*(-1 if self.color-1 else 1)): p = board.PieceAt(newPos[0]-1, newPos[1]+1)[1]; p.erase(); p.remove()
  if board.TileAt(newPos[0], newPos[1]) == (3 if self.color-1 else 2): self.promote() 
def onAttacked(self): self.remove(); return 'move'
  
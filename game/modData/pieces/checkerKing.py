attackPath = []
movePath = [(1,-1),(-1,-1)]
canPromote = False
canJumpPieces = True
canJumpEmpties = True
char = 'C'
promotesTo = []

conditionalMovePath = [
  ((-2,-2), lambda p, b, g: b.PieceAt(p.pos[0]-1, p.pos[1]-1)[1])
  ((-2,-2), lambda p, b, g: b.PieceAt(p.pos[0]+1, p.pos[1]+1)[1])
]
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): 
  if self.pastMoves[-1][2] == (-2,-2*(-1 if self.color-1 else 1)): p = board.PieceAt(newPos[0]+1, newPos[1]+1)[1]; p.erase(); p.remove()
  elif self.pastMoves[-1][2] == (2,-2*(-1 if self.color-1 else 1)): p = board.PieceAt(newPos[0]-1, newPos[1]+1)[1]; p.erase(); p.remove()
def onAttacked(self): self.remove(); return 'move'
  
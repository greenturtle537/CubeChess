def EnPassantRight(p, b, g):
  if b.PieceAt(p.pos[0]+1, p.pos[1])[1].id == 'p' and len(b.PieceAt(p.pos[0]+1, p.pos[1])[1].pastMoves) > 1 and b.PieceAt(p.pos[0]+1, p.pos[1])[-1].pastMoves[-1][2][1] in [-2,2]: return True
  return False
  
def EnPassantLeft(p, b, g):
  if b.PieceAt(p.pos[0]-1, p.pos[1])[1].id == 'p' and len(b.PieceAt(p.pos[0]-1, p.pos[1])[1].pastMoves) > 1 and b.PieceAt(p.pos[0]-1, p.pos[1])[-1].pastMoves[-1][2][1] in [-2,2]: return True
  return False
  
attackPath = [(1,-1),(-1,-1)]
movePath = [(0,-1),]
canPromote = True
canJumpPieces = False
canJumpEmpties = True
char = 'p'
promotesTo = ['r','n','b']

conditionalMovePath = [
  ((0,-2), lambda p, b, g: len(p.pastMoves) == 1), # initial 2 spaces if at start line

  ((1,-1), EnPassantRight),   # en passant right side
  
  ((-1,-1), EnPassantLeft)   # en passant left side
]
conditionalAttackPath = []

def onMove(self, game, board, pieces, oldPos, newPos): 
  # en passant
  if (abs(self.pastMoves[-1][2][0]) + abs(self.pastMoves[-1][2][1])) > 1 and abs(self.pastMoves[-1][2][1]) < 2 and board.PieceAt(newPos[0], newPos[1]+(-1 if self.color-1 else 1))[1].pastMoves[-1][1] and len(board.PieceAt(newPos[0], newPos[1]+(-1 if self.color-1 else 1))[1].pastMoves) == 2:  p = board.PieceAt(self.pos[0], self.pos[1]+(-1 if self.color-1 else 1))[1]; p.erase(); p.remove()
  # promotion
  if board.TileAt(newPos[0], newPos[1]) == (3 if self.color-1 else 2): self.promote() 

def onAttacked(self): self.remove(); return 'move'
    
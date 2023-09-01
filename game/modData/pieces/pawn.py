attackPath = [(1,-1),(-1,-1)]
movePath = [(0,-1),]
pawnPromote = True
canJumpPieces = True
canJumpEmpty = True
char = 'p'

conditionalMovePath = [
  ((0,-2), lambda p, b, g: len(p.pastMoves) == 1), # initial 2 spaces if at start line

  ((1,-1), lambda p, b, g: (b.PieceAt(p.pos[0]+1, p.pos[1])[1].id == 'p') and (b.PieceAt(p.pos[0]+1, p.pos[1])[1].pastMoves[-1][1] == g.turn-1) and (abs(b.PieceAt(p.pos[0]+1, p.pos[1])[1].pastMoves[-1][2][1]) == 2)),   # en passant right side
  
  ((-1,-1), eval("lambda p, b, g: (b.PieceAt(p.pos[0]-1, p.pos[1])[1].id == 'p') and (b.PieceAt(p.pos[0]-1, p.pos[1])[1].pastMoves[-1][1] == g.turn-1) and (abs(b.PieceAt(p.pos[0]-1, p.pos[1])[1].pastMoves[-1][2][1]) == 2))   # en passant left side
]
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): 
  p = board.PieceAt(newPos[0], newPos[1]-(1 if self.color-1 else -1))
  if p[0]:  # en passant removal of other pawn
      if p[1].id == 'p' and p[1].pastMoves[-1][1] == game.turn-1: p[1].remove(); return
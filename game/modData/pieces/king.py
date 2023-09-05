def castleLeft(p, b, g):
  if len(p.pastMoves) > 1: return False
  pi = b.PieceAt(p.pos[0]-4, p.pos[1])[1]
  if pi.id == 'r' and len(pi.pastMoves) == 1:
    if any([b.PieceAt(p.pos[0]-1, p.pos[1])[0], b.PieceAt(p.pos[0]-2, p.pos[1])[0], b.PieceAt(p.pos[0]-3, p.pos[1])[0]]): return False
    else: return True

def castleRight(p, b, g):
  if len(p.pastMoves) > 1: return False
  pi = b.PieceAt(p.pos[0]-4, p.pos[1])[1]
  if pi.id == 'r' and len(pi.pastMoves) == 1:
    if any([b.PieceAt(p.pos[0]+1, p.pos[1])[0], b.PieceAt(p.pos[0]+2, p.pos[1])[0]]): return False
    else: return True

attackPath = [(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,0),(1,1)]
movePath = attackPath
canPromote = False
canJumpPieces = True
canJumpEmpties = True
char = 'k'
promotesTo = []

conditionalMovePath = [((-2,0), castleLeft),  ((2,0), castleRight)]
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): 
  if oldPos[0]-2 == newPos[0]: p = board.PieceAt(oldPos[0]-4, oldPos[1])[1]; p.erase(); p.move((oldPos[0]-1, oldPos[1])); p.draw()
  if oldPos[0]+2 == newPos[0]: p = board.PieceAt(oldPos[0]+3, oldPos[1])[1]; p.erase(); p.move((oldPos[0]+1, oldPos[1])); p.draw()
def onAttacked(self): self.remove(); return 'move'
  
attackPath = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,-2),(-1,2),(1,-2),(1,2)]
movePath = attackPath
pawnPromote = False
canJumpPieces = True
canJumpEmpties = True
char = 'n'

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'
  
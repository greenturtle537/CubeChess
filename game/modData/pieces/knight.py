attackPath = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,-2),(-1,2),(1,-2),(1,2)]
movePath = attackPath
canPromote = False
canJumpPieces = True
canJumpEmpties = True
char = 'n'
promotesTo = []

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'
  
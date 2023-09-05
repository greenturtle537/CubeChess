attackPath = [(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,0),(1,1)]
movePath = attackPath
canPromote = False
canJumpPieces = True
canJumpEmpties = True
char = 'k'
promotesTo = []

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'
  
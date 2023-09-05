attackPath = ['up-left','up-right','down-left','down-right']
movePath = attackPath
canPromote = False
canJumpPieces = False
canJumpEmpties = True
char = 'b'
promotesTo = []

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'
  
attackPath = ['up-right','up-left','down-left','down-right','up','down','left','right']
movePath = attackPath
canPromote = False
canJumpPieces = False
canJumpEmpties = True
char = 'q'
promotesTo = []

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'
  
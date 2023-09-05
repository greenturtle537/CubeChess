attackPath = ['up','down','left','right']
movePath = attackPath
canPromote = False
canJumpPieces = False
canJumpEmpties = True
char = 'r'
promotesTo = []

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'

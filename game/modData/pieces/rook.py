attackPath = ['up','down','left','right']
movePath = attackPath
pawnPromote = False
canJumpPieces = False
canJumpEmpties = True
char = 'r'

conditionalMovePath = []
conditionalAttackPath = []
def onMove(self, game, board, pieces, oldPos, newPos): pass
def onAttacked(self): self.remove(); return 'move'

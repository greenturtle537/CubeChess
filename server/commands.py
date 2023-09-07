def trycommand(commandtext):
  if commandtext in list(functionmap):
    #functionmap[commandtext]()
    return True
  else:
    return False


def docommand(commandtext):
  return functionmap[commandtext]()


def connect():
  return "Turn on the WiFi"


functionmap = {
  "connect": connect,
}

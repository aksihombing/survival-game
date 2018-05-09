# I plan on putting each different aspect (if possible) in different files once done
#----- BOARD (below)-----#

class Game:
  
  
  def __init__(self):
    self.state = ["[]" for n in range(16)]
    self.game_over = False
    self.playerplace = "3,3"
  
  def __repr__(self):
    return "Game({})".format(self.state)
  
  def __str__(self):
    return "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(*self.state)

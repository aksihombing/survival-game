#If all my code works, I'll probably just put it all in individual files.

#----------BOARD----------#
class Game:
  
  
  def __init__(self):
    self.state = ["[]" for n in range(16)]
    self.game_over = False
  
  def __repr__(self):
    return "Game({})".format(self.state)
  
  def __str__(self):
    return "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(*self.state)





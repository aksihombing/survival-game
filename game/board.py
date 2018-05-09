# I plan on putting each different aspect (if possible) in different files once done
#----- BOARD (below)-----#

class Game:
  
  
  def __init__(self):
    self.state = ["[]" for n in range(16)]
    self.game_over = False
    self.playerplace = self.state[3][3]
  
  def __repr__(self):
    return "Game({})".format(self.state)
  
  def __str__(self):
    return "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(*self.state)
  
  # TEMPORARY CODE (UNTESTED)
  # The code below is for the start of the game
  def threethree(self):
    while True:
      try:
        xchoice = int(input("Which way do you want to go? (2,3), (2,2), or (3,2)?\n row:"))
        ychoice = int(input("\n column:"))
        if int(xchoice) is not 2 or 3:
          raise ValueError
        if int(ychoice) is not 2 or 3:
          raise ValueError
        # *While trying to look for the symbol for "Not equal to" in python through Google, I saw that "is not" is similar, so i tried it. 
        # *If it works, I'll add it to my sources.
        break
      except ValueError:
        print("Please choose from given.")
        break

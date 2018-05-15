# I plan on putting each different aspect (if possible) in different files once done
# Helper Functions---------------
from random import choice 
from random import randint

def pause():
  input()  
  return

#----- BOARD (below)-----#
class Game:
  
  
  def __init__(self):
    self.state = [['[]','[]','[]'] for n in range(3)]
    self.playerplace = self.state[2][2]
    self.game_over = False
  def __repr__(self):
    return "Game({})".format(self.state)
  
  def __str__(self):
    return "{} {} {}\n{} {} {}\n{} {} {}\n".format(*self.state)
  
  def story(self):
    print("It's been months since a virus spread. People who were infected died within hours, or at most, a few days, later. People's greed turned nearly everyone against each other.")
    pause()
    print("The group that you were once with has recently turned against you in order to maintain more supplies. Your two good friends decide to join you, staying loyal to you. The group sent the three of you off with minimal supplies to survive about five days, yet no map.")
    pause()
    print("One of your friends point out that they know of another base from radio transmissions. However, since there is no map, you and your friends must blindly travel together, hoping to come across the base. Also, the base, according to the radio transmissions, will also close under two months.")
    pause()
    playername = str(input("What is your name?:\n"))
    friend1 = str(input("What is the name of your first friend?\n"))
    friend2 = str(input("What is the name of your second friend?\n"))
    supplies = {"food" : str(randint(10,30)), "water" : str(randint(15,30)), "money" : "${}".format(str(randint(10,30)))}
    print("You have....\n {} food\n {} water\n {} left.".format(supplies['food'],supplies['water'],supplies['money']))
  
  
  # TEMPORARY CODE (UNTESTED)
  # The code below is for the start of the game
  def twotwo(self):
    while True:
      try:
        xchoice = int(input("Which way do you want to go? (1,2), (1,1), or (2,1)?\n row:"))
        ychoice = int(input("\n column:"))
        if int(xchoice) == 2 or 1:
          if int(ychoice) == 2 or 1:
            if int(xchoice)+int(ychoice) == 3:
              return self.playerplace == self.state[int(xchoice)][int(ychoice)]
        else:
          raise IndexError
      except IndexError:
        print("Please choose from the given")

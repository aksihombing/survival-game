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
    self.playername = str(input("What is your name?:\n"))
    self.friend1 = str(input("What is the name of your first friend?\n"))
    self.friend2 = str(input("What is the name of your second friend?\n"))
    self.supplies = {"food" : str(randint(10,30)), "water" : str(randint(15,30)), "money" : "${}".format(str(randint(10,30)))}
    print("You have....\n {} food cans, {} water bottles, {} left.".format(self.supplies['food'],self.supplies['water'],self.supplies['money']))
    return self.story()

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
    return self.twotwo()
  
  
  # TEMPORARY CODE (UNTESTED)
  # The code below is for the start of the game
  def twotwo(self):
    while True:
      try:
        xchoice = int(input("Which way do you want to go? (1,2), (1,1), or (2,1)?\n row:"))
        ychoice = int(input("\n column:"))
        if int(xchoice) == 2:
          if int(ychoice) == 1:
            return self.twoone()
        elif int(xchoice) == 1:
          if int(ychoice) == 1:
            return self.oneone()
          if int(ychoice) == 2:
            return self.onetwo()
        else:
          raise IndexError
      except IndexError:
        print("Please choose from the given")
  
  def twoone(self):
    while True:
      try:
        print("There is a large city ahead of your group. Do you wish to continue?\n Enter 1 to continue or 2 to travel east instead\n")
        continuechoice = int(input())
        if int(continuechoice) == int(1):
          print("Your group follows you deep into the city.")
          pause()
          print("Oh no! The city is infested, and unfortunately your group has been slowed down and infected.")
          pause()
          print("'Help...' you hear {} groan. You and {} hear {}'s groaning when it's too late!").format(self.friend1, self.friend2, self.friend1)
          pause()
          print("{} grabbed their shoulders and shook them, in disbelief of a lost friend. {}'s head looked up and before you knew it, {} was also infected.").format(self.friend2, self.friend1, self.friend2)
          pause()
          print("'{}! Run far away! Please!' {} shouts.").format(self.playername, self.friend2)
          pause()
          print("Sucks to be you, huh? It gets worse, too. In an attempt to flee, you hadn't been paying attention to where you ran. You turn around and see a horde of infected people chasing after you, the only healthy person around.")
          pause()
          print("G A M E  O V E R")
          self.game_over == True
        elif int(continuechoice) == 2:
          return self.oneone()
      except:
        return
 
 
  def oneone(self):
    while True:
      try:
        print("'There seems to be many ways to go from here!' {} cheerfully says.").format(self.friend2)
        pause()
        print("{} goes on and on and ON, describing the surroundings, other than the boring trees.").format(self.friend2)
        pause()
        print("Cutting you some slack, here's what they said, in a simpler and easy way.\n NORTHWEST - A strange building\n NORTH - A huge river\n NORTHEAST - A small town\n EAST - A city\n SOUTH - A small and thin river\n SOUTHWEST - There seems to be a light somewhere behind the trees\n WEST - Another small town.")
        
      except:
        return "ok"
  def onetwo(self):
    while True:
      try:
        print("There's a river ahead of your group. Do you cross the river to go east, or go north?\n Enter 1 to cross, or 2 to go north.\n")
        crossornot = int(input())
        if int(crossornot) == int(1):
          print("The water is really quick! Your group holds hands and tries to cross together.")
          pause()
          print("After some more shouting, you and your friends finally make it across, but at the cost of some supplies.")
          return self.playerplace[0][2], supplies[water]-4, supplies[food]-6, supplies[money]-10
        elif int(crossornot) == int(2):
          print("Your group heads north instead")
          return self.playerplace[1][1]
      except:
        return "ok"

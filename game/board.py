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
    self.supplies = {"food" : 32, "water" : 50}


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
  
  
  # NOT YET "DEBUGGED" ----------------------------

  def twotwo(self):
    while True:
      try:
        firstchoice = int(input("Which way do you wish to go?\n 1.)North: a city\n 2.)East: a river\n 3.)Northeast: nothing but trees!\n"))
        if int(firstchoice) == 1:
          pause()
          return self.twoone()
        elif int(firstchoice) == 2:
          pause()
          return self.onetwo()
        elif int(firstchoice) == 3:
          pause()
          return self.oneone()
        else:
          raise IndexError
      except:
        print("Please choose from the given")
  
  def twoone(self):
    while True:
      try:
        print("There is a large city ahead of your group. Do you wish to continue?\n Enter 1 to continue or 2 to travel east instead\n")
        continuechoice = int(input())
        if int(continuechoice) == int(1):
          pause()
          print("Your group follows you deep into the city.")
          pause()
          print("Oh no! The city is infested, and unfortunately your group has been slowed down and infected.")
          pause()
          print("'Help...' you hear one friend groan. You and your other friend hears their groaning when it's too late!")
          pause()
          print("Your other friend grabbed their shoulders and shook them, in disbelief of a lost friend. Your sick friend's head looked up and before you knew it, your other friend was also infected.")
          pause()
          print("Run far away! Please!' your conscious, sick friend shouts.")
          pause()
          print("Sucks to be you, huh? It gets worse, too. In an attempt to flee, you hadn't been paying attention to where you ran. You turn around and see a horde of infected people chasing after you, the only healthy person around.")
          pause()
          print("G A M E  O V E R")
          self.game_over == True
        elif int(continuechoice) == 2:
          pause()
          return self.oneone()
          
      except:
        return "Error. Please try again."
 
 
  def oneone(self):
    while True:
      try:
        print("'There seems to be many ways to go from here!' your friend cheerfully says.")
        pause()
        print("They go on and on and ON, describing the surroundings, other than the boring trees.")
        pause()
        print("Cutting you some slack, here's what they said, in a simpler and easy way.\n NORTHWEST - A strange building\n NORTH - A huge river\n NORTHEAST - A small town\n EAST - A city\n SOUTH - A small and thin river\n SOUTHWEST - There seems to be a light somewhere behind the trees\n WEST - Another small town.")
        pause()
        print("Where do you want to go?")
        direction = int(input("1.)Northwest\n 2.)North\n 3.)Northeast\n 4.)East\n 5.)South\n 6.)Southwest\n 7.)West\n"))
        if int(direction) == 1 :
          pause()
          return self.zerozero()
        elif int(direction) == 2 :
          pause()
          return self.onezero()
        elif int(direction) == 3 :
          pause()
          return self.twozero()
        elif int(direction) == 4 :
          pause()
          return self.twoone()
        elif int(direction) == 5 :
          pause()
          return self.onetwo()
        elif int(direction) == 6 :
          pause()
          return self.zerotwo()
        elif int(direction) == 7 :
          pause()
          return self.zeroone()
        else:
          raise ValueError
        
      except:
        return "Error. Please try again."

  def onezero(self):
    pass
  
  def twozero(self):
    pass
  
  def zerotwo(self):
    pass
  
  def zeroone(self):
    pass



  def onetwo(self):
    while True:
      try:
        print("There's a river ahead of your group. Do you cross the river to go east, or go north?\n Enter 1 to cross, or 2 to go north.\n")
        crossornot = int(input())
        if int(crossornot) == int(1):
          print("The water is really quick! Your group holds hands and tries to cross together.")
          pause()
          print("After some more shouting, you and your friends finally make it across, but at the cost of some supplies.")
          pause()
 
        elif int(crossornot) == int(2):
          print("Your group heads north instead")
          pause()
          return self.playerplace[1][1]
      except:
        return "Error. Please try again."






  # ------------- W I N ----------------
  def zerozero(self):
    print("After countless hours of losing sleep, having to ration whatever was left of your supplies, you have finally reached a less horrifying building.")
    pause()
    print("'Hey! Are you survivors? Are any of you infected?' someone shouts at the top of the wall in front of you. You and your friends nod very quickly.")
    pause()
    print("The man at the top seems to just stand and stare at you all. After about a few seconds, he says....")
    pause()
    print("'Well, come on in!'")
    pause()
    print("The gates slowly open and the three of you ran with all your energy to get inside.")
    pause()
    print("You have successfully arrived at the base!\n CONGRATULATIONS!\n YOU WIN")
    return self.game_over == True

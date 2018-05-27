# Helper Functions---------------
def pause():
  input()  
  return

#----- BOARD (below)-----#
class Game:
  
  
  def __init__(self):
    self.state = [['[]','[]','[]'] for n in range(3)]
    self.game_over = False
    self.party = {"Baton": True, "Roblox poster" :False }

  def __repr__(self):
    return "Game({})".format(self.state)
  
  def __str__(self):
    return "{} {} {}\n{} {} {}\n{} {} {}\n".format(*self.state)

  def story(self):
    print("It's been months since a virus spread. People who were infected died within hours, or at most, a few days, later. People's greed turned nearly everyone against each other.")
    pause()
    print("The group that you were once with has recently turned against you in order to maintain more supplies. Your two good friends decide to join you, staying loyal to you. Upon your departure, they sent the three of you off with minimal supplies to survive about one month, yet no map. However, they DID give you a baton... for the three of you to share. Nice.")
    pause()
    print("One of your friends point out that they know of another base from radio transmissions. However, since there is no map, you and your friends must blindly travel together, hoping to come across the base.")
    pause()
    return self.twotwo()
  
  
  # NOT YET "DEBUGGED" ----------------------------

  def twotwo(self):
    while True:
      try:
        firstchoice = int(input("Which way do you wish to go?\n 1.)North: a city\n 2.)East: a river\n 3.)Northeast: nothing but trees!\n"))
        if int(firstchoice) == 1:
          return self.twoone()
        elif int(firstchoice) == 2:
          return self.onetwo()
        elif int(firstchoice) == 3:
          return self.poster()
        else:
          raise ValueError
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
          if self.party["Baton"] == True:
            print("Wait! You have a baton! That's good...Right?")
            pause()
            print("Well, congrats! You've fled from the city and your dead friends! How loyal!")
            pause()
            print("It seems you're on your own.. That's unfortunate. On the bright side, you seem to do so well on your own! You live!.... for a month, until you find yourself at the wrong place in the wrong time...")
            pause()
            print("Congrats! You get the Not-So-Bad ending!")
            pause()
            print("It's an easy ending, but nonetheless, the goal was to get to a base, so...")
            pause()
            print("YOU LOSE")
            return self.game_over == False
            break
          else:
            print("Sucks to be you, huh? It gets worse, too. In an attempt to flee, you hadn't been paying attention to where you ran. You turn around and see a horde of infected people chasing after you, the only healthy person around.")
            pause()
            print("G A M E  O V E R")
            self.game_over == True
            break
        if int(continuechoice) == 2:
          return self.poster()
        else:
          raise ValueError
      except:
        return "Error. Please try again."
 
 
  def poster(self):
    while True:
      try:
        print("You all unanimously decide to set up camp in this area for the night. The three of you drew straws to see who's on watch, and luckily it wasn't you. You got pretty decent sleep that night.")
        pause()
        print("'Hey! Look what I got!' your friend who was on watch says. They hold up a Roblox poster.")
        robloxposter = int(input("Do you:\n 1.)Keep it\n 2.)Throw it out?\n"))
        if int(robloxposter) == 1:
          print("Nice choice! What will this do, though?")
          pause()
          return self.party["Roblox poster"] == True, self.oneone()
        elif int(robloxposter) == 2:
          print("Well, okay then. Rude.")
          pause()
          return self.party["Roblox poster"] == False, self.oneone()
        else:
          raise ValueError
      except:
        return "Error. Please try again."
  
  
  def oneone(self):
    while True:
      try:
        print("'There seems to be many ways to go from here!' your friend cheerfully says.")
        pause()
        print("They go on and on and ON, describing the surroundings, other than the boring trees.")
        pause()
        print("Cutting you some slack, here's what they said, in a simpler and easy way.\n 1.)NORTHWEST - A strange building\n 2.)NORTH - A huge river\n 3.)NORTHEAST - A small town\n 4.)EAST - A city\n 5.)SOUTH - A small and thin river\n 6.)SOUTHWEST - There seems to be a light somewhere behind the trees\n 7.)WEST - Another small town.\n")
        direction = int(input("Enter the number of the direction you wish to travel to:\n"))
        if int(direction) == 1 :
          return self.zerozero()
        elif int(direction) == 2 :
          return self.onezero()
        elif int(direction) == 3 :
          return self.twozero()
        elif int(direction) == 4 :
          return self.twoone()
        elif int(direction) == 5 :
          return self.onetwo()
        elif int(direction) == 6 :
          return self.zerotwo()
        elif int(direction) == 7 :
          return self.zeroone()
        else:
          raise ValueError
      except:
        return "Error. Please try again."

  def onezero(self):
    while True:
      try:
        print("To the west, there seems to be a river.")
        direction1 = int(input("Do you want to\n 1.)Cross the river to the west 2.)Travel east instead\n 3.)Travel south"))
        if int(direction1) == 1 :
          print("\n The river appears to be stronger than you thought! The current is too strong and fast, and before you realize it's nearly impossible to cross...")
          pause()
          print("You and your friends get taken by the    current! Oh no!")
          pause()
          print("By the time you get to land, you get separated from your friends. And what's worse?")
          pause()
          print("You have no food or clean water.")
          pause()
          print("After a few weeks of trying to survive in the barren area you found yourself in, you find a city. Sadly, finding food didn't do too well for you.")
          pause()
          print(".... You end up getting infected. Well, on the bright side, you make friends with other infected people. That's good...right?")
          pause()
          print("Y O U  L O S E :) ")
          self.game_over = True
        elif int(direction1) == 2 :
          return self.twozero()
        elif int(direction1) == 3 :
          return self.poster()
        else:
          raise ValueError
      except:
        return "Error. Please try again."

    
  
  def twozero(self):
    while True:
      try:
        print("You approach a building ahead of you, curious and afraid of what's to come.")
        pause()
        print("An old lady appears in front of you, with armed people behind her. She gives you one look and decides to run at you with her cane.")
        runorstay = int(input("What do you do? Do you\n 1.)run west\n 2.)Wait and see what happens\n"))
        if int(runorstay) == 1:
          pause()
          return self.onezero()
        elif int(runorstay) == 2:
          print("W-wow, that was unexpected. She swung at you and knocked your whole group out!")
          pause()
          print("Looks like you made the wrong choice...\n When you wake up, you're being... SACRIFICED? Well, uh, you're involved with a cult now-- actually, not really 'involved'-- more like being sacrificed by them. Niiiiiiiiice...")
          pause()
          print("YOU L O S E")
          return self.game_over == True
          
      except:
        return "Error. Please try again."
  
  def zerotwo(self):
    while True:
      try:
        print("There's a mysterious light somewhere in the trees. What could it be?")
        pause()
        approach = int(input("Do you\n 1.)Approach the light\n 2.)Go north instead, where there seems to be a building.\n"))
        if int(approach) == 1:
          print("When you approach the light source, you realize it's a campfire. You were trying to get a better look from behind a tree when you stepped on a twig. Rookie mistake. You were too outnumbered to even dare to pull out your party's only weapon-- the baton.")
          pause()
          print("'Who's there?' one of the mysterious men with a mouth mask shouted. The other around him held their weapons ready.")
          speakordie = int(input("This seems like a tight situation. They don't seem too friendly. Do you\n 1.)Wait until they find you\n 2.)Reveal yourself and try to join their group\n"))
          if int(speakordie) == 1:
            pause()
            print("It wasn't long until they spotted you all creeping on them. They didn't seem to enjoy being spied on, like many people. They were very 'defensive' and attacked. Let's spare you the details--")
            pause()
            print("YOU L O S E")
            return self.game_over == True
            break
          elif int(speakordie) == 2:
            pause()
            print("You first walked out from behind the trees. Your friends were quick to follow you, though reluctant to throw down their weapons just as you did.")
            pause()
            print("'We mean no harm! We were looking for a new place to stay!' you tried to explain with your hands up. The group before you gave each other looks. They all lifted up their masks and nodded, smiling.")
            pause()
            print("'Welcome to the club!' they all said in unison. Turns out they were a group of really nice vegans who decided to look more aggressive to avoid hurting anyone.")
            pause()
            print("Um-- Oh! It looks like you're a vegan now! Erm...Congrats?")
            pause()
            print("Well, that didn't last long, either. After about three weeks with them, you drank some nasty water from the nasty, polluted river. They were pretty strict on leaving the fish in the clean water alone, so you all didn't have much of a choice.")
            pause()
            print("After getting sick from the polluted water, it's safe to say that you, and a few others, died. Maybe you shouldn't go vegan next time-- but that's just me.")
            pause()
            print("YOU....LOSE?")
            return self.game_over == True
          else:
            raise ValueError
        elif int(approach) == 2:
          return self.zeroone()
        else:
          raise ValueError
      except:
        return "Error. Please try again."
  
  def zeroone(self):
    while True:
      try:
        print("There's a small building in front of you. One of your friends drag you inside. The further you walk into it, the colder it feels. You get chills down your spine and goosebumps.")
        pause()
        leftright=int(input("You get to a hallway with two doors. Where do you go?\n 1.)Left\n 2.)Right"))
        if int(leftright) == 1:
          pause()
          print("After walking through the left door, you walk into another hallway, which leads you.. outside?")
          pause()
          print("Before you have time to react, the front door is slammed shut, sending you bad vibes. Your friends quickly drag you east with them.")
          pause()
          return self.poster()
        elif int(leftright) == 2:
          pause()
          print("Oh? There's a staircase leading down into a basement!")
          pause()
          print("When you get to the bottom, there's a phone on the table...and.. what's this?")
          pause()
          print("Is that..? It's a roblox character...? Before you have time to process why there's a working smartphone and why the image is of a Roblox character, you turn around to see...")
          pause()
          if self.party["Roblox poster"] == True:
            print("You quickly pull out your handy Roblox poster. He seems pretty happy! He grabs the poster from you and you come out of the house alive!")
            pause()
            print("He's kind enough to write a note, saying that going north from there will lead to a safe place! You follow his directions and go north.")
            return self.zerozero()
          else:
            print("a guy wearing colored cardboard boxes like the Roblox character in the picture..? W-what is going on?")
            pause()
            print("O-Oh..It seems that you and your friends were taken by the Roblox man, never to return.")
            pause()
            print("Well sucks to be you, huh?")
            pause()
            print("YOU LOSE")
            return self.game_over==True
            break
        else:
          raise ValueError
      except:
        return "Error. Please try again."



  def onetwo(self):
    while True:
      try:
        print("There's a river ahead of your group. Do you cross the river to go east, or go north?\n Enter 1 to cross, or 2 to go north.\n")
        crossornot = int(input())
        if int(crossornot) == int(1):
          print("The water is really quick! Your group holds hands and tries to cross together.")
          pause()
          print("After some more shouting, you and your friends finally make it across! Sadly, you have lost your only weapon!")
          pause()
          self.party["Baton"] = False
          return self.zerotwo()
        elif int(crossornot) == int(2):
          print("Your group heads north instead")
          pause()
          return self.poster()
        else:
          raise ValueError
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

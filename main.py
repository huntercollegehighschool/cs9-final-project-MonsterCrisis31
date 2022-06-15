"""
Name(s): Kiren Nasta
Name of Project: Choose your own adventure
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
def doorB():
  print("You open the door only to realize to your horror that you are midair and falling at a rapid pace. All of a sudden, without even time to brace for impact, you land in some sort of lake. It's terribly painful but what really strikes you is the fact that the water is red. You can either continue to explore the lake or swim out and onto land.")
  choice = input("Enter E to explore the lake and enter L to swim out onto land: ")
  while choice != "E" and choice != "L":
    print("You must choose either 'E' or 'L'")
    choice = input("Enter E to explore the lake and enter L to swim out onto land: ")
  if choice == "E":
    explore()
  elif choice == "L":
    shore()
def explore():
  print("You swim towards the bottom of the lake and see a green glow coming from the bottom as well as a small opening. You swim up to get some air. You can either enter the opening with a green glow, or leave the lake and go to the shore")
  choice = input("Enter O to explore the lake and enter L to swim out onto land back to shore: ")
  while choice != "O" and choice != "L":
    print("You must choose either 'O' or 'L'")
    choice = input("Enter O to explore the lake and enter L to swim out onto land back to shore: ")
  if choice == "O":
    opening()
  elif choice == "L":
    shore()

def opening():
  print("You go through the opening and are transported through a portal back to your house. However, all of a sudden you realize it's not your house because everything is made of gold. You hear a noise and look up in terror as tons of gold fall from the sky, crushing you to death.")
  
def shore():
  print("You climb on to the shore. Suddenly, a group of zombies starts walking towards you. They have no visible weapons but a menacing look in their eyes. You realize you are cornered. Behind you is an opening but you have no idea what lies below. You can either risk it and jump into the opening, or you can attempt to fight the zombies.")
  choice = input("Enter J to jump into the opening and enter F to fight the zombies: ")
  while choice != "J" and choice != "F":
    print("You must choose either 'J' or 'F'")
    choice = input("Enter J to jump into the opening and enter F to fight the zombies: ")
  if choice == "J":
    backaway()
  elif choice == "F":
    fight()

def backaway():
  print("You jump through the opening and end up in a room full of lava. As you burn to death, you see another person that looks like yourself on top of a trash can. Before you can call out for help you have burned to death.")

def fight():
  print("You stand your ground and get ready to face the zombies. You can either charge blindly into battle with all the courage in the world, or you can search your backpack for tools.")
  choice = input("Enter C to charge at the zombies and enter S to search your backpack: ")
  while choice != "C" and choice != "S":
    print("You must choose either 'C' or 'S'")
    choice = input("Enter C to charge at the zombies and enter S to search your backpack: ")
  if choice == "C":
    charge()
  elif choice == "S":
    search()        

def search():
  print("You do not find any tools, but as you are deciding what to do next, a dagger flies up from below. Out of sheer luck, you catch it. You then attack the zombies and kill them easily. You don't know what this strange place is, but at least you're alive.")

def charge():
  print("Your courage amounts to nothing as the zombies rip your brains out and eat them.")
    
def doorA():
  print("It's your lucky day! By entering this room you now have the opportunity to win 1 million dollars. However there will be a consequence!!")
  choice = input("Enter B to press a button to claim the money, Enter N to decline the money and go to a different room, Enter S to start over: ")
  while choice != "B" and choice != "N" and choice != "S":
    print("You must choose either 'B', 'N', or 'S'")
    choice = input("Enter B to press a button to claim the money, Enter N to decline the money and go to a different room, Enter S to start over: ")
  if choice == "B":
    consequence()
  elif choice == "N":
    morals()
  elif choice == "S":
      start()
def morals():
  print("inside this room there is a giant pit of lava. You realize the door locks behind you and the lava is rapidly expanding. You can either climb on a trash can or search your backpack for tools that might help you inhibit the flow of lava.")
  choice = input("Enter I to search for tools that may inhibit the flow of lava and enter C to climb onto the trash can: ")
  while choice != "I" and choice != "C":
    print("You must choose either 'I' or 'C'")
    choice = input("Enter I to search for tools that may inhibit the flow of lava and enter C to climb onto the trash can: ")
  if choice == "I":
    inhibit()
  elif choice == "C":
    climb()
def inhibit():
  print("You find a dagger but a dagger won't do anything against lava. You throw your dagger upwards in frustration. Suprisingly, it doesn't come back down. Before you can ponder why this may have happened, the lava converges on you and you burn to death. You should have gone with the free money.")
def climb():
  print("You climb on a trash can, but realize that you have nowhere to go. As you are standing on the trash can in terror, someone falls from above and lands in the lava. They look at you before they promptly die. The trash can eventually melts and you fall into the lava to your death. You should have gone with the free money. ")
def consequence():
  print("Congratulations. You have won 1 million dollars. But the consequence is that one of your closest friends will die. You can either choose to burn the money and save your friend or to claim the money. ")
  choice = input("Enter B to burn the money and save your friend and enter C to claim the money: ")
  while choice != "B" and choice != "C":
    print("You must choose either 'B' or 'C'")
    choice = input("Enter B to burn the money and save your friend and enter C to claim the money: ")
  if choice == "B":
    burn()
  elif choice == "C":
    claim()
def claim():
  print("The person who died was your best friend. However, it turns out he was planning to murder you tomorrow, so you got lucky. Now you're 1 million dollars richer, and one fake friend less!")
def burn():
  print("You throw the wad of cash into the fireplace. However, to your horror, the fire starts to expand, and there's no way of stopping it. You burn to death. You should have gone with the money. ")
def start():
  print("There are two doors. Choose either door A or door B. ")
  choice = input("Enter A for door A or B for door B: ")
  while choice != "A" and choice != "B":
    print("You must choose either 'A' or 'B'")
    choice = input("Enter A for door A or B for door B: ")
  if choice == "A":
    doorA()
  elif choice == "B":
    doorB()
start()



  
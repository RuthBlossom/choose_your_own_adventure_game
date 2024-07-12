print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Dungeon Adventure!")
print("Your quest is to find the legendary treasure in the mystical dungeon.")


choice1 = input(
  "As you stand at the entrance, you see two paths: a dark corridor on the left and a mysterious staircase on the right. Which path do you choose? Type \"left\" or \"right\" \n").lower()

if choice1 == "left":
  print("You venture into the dark corridor, feeling a chill down your spine.")

  choice2 = input(
    "You come across a fork in the path. To the left, you hear growls and see a faint glow. To the right, you sense a draft. Which way do you go? Type \"left\" or \"right\" \n").lower()

  if choice2 == "left":
    print("You encounter a pack of hungry wolves guarding a chest. They are not pleased with your presence. Game Over.")
  elif choice2 == "right":
    print("You find a secret room with a healing potion and a map to the treasure room. You continue your journey.")

    choice3 = input(
      "You reach a room with three doors: one marked with a dragon symbol, one with a wizard symbol, and one with a rogue symbol. Which door do you choose? \n").lower()

    if choice3 == "dragon":
      print("You enter a room with a sleeping dragon guarding the treasure. You must carefully sneak past it.")

      choice4 = input("Do you want to \"sneak\" or \"attack\" the dragon? \n").lower()

      if choice4 == "sneak":
        print("You successfully sneak past the dragon and grab the treasure! Congratulations, you win!")
      else:
        print("The dragon wakes up and breathes fire. Game Over.")

    elif choice3 == "wizard":
      print("You encounter a wise old wizard who challenges you to a riddle. Solve it to proceed.")

      riddle_answer = input("What has keys but can't open locks? \n").lower()

      if riddle_answer == "piano":
        print("The wizard is impressed. He opens a secret passage to the treasure room. Congratulations, you win!")
      else:
        print("The wizard shakes his head. You failed the riddle. Game Over.")

    elif choice3 == "rogue":
      print("You enter a room filled with traps. Use your agility to navigate through.")

      agility_choice = input("Do you want to \"jump\" over the traps or \"crawl\" under them? \n").lower()

      if agility_choice == "jump":
        print("You skillfully jump over the traps and reach the treasure room. Congratulations, you win!")
      else:
        print("You trigger a trap and fall into a pit. Game Over.")

    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You hesitated too long, and a mysterious force transports you back to the dungeon entrance. Try again.")
else:
  print(
    "You climb the mysterious staircase, and it leads you to a magical portal. You step through and find yourself in the treasure room. Congratulations, you win!")

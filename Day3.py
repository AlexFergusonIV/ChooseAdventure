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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
choice1 = input("You're at a cross road.  Where do you want to go? Type \"left\" or \"right\"    ").lower()

if choice1 == "right" or choice1 == "Right":
    print("You chose", choice1)
    print("You run into a forest.  It is thick and full of foliage.  You lose your way over the course of hours.  You succomb to hunger and die.  GAME OVER.")
elif choice1 == "left" or choice1 == "Left":
    print("You chose", choice1)
    choiceleft  =   input("You come to a lake.  There is an island in the middle of the lake.  Type \"wait\" to wait for the boat.  Type \"swim\" to swim across.  ").lower()
    if choiceleft == "wait" or choiceleft == "Wait":
        choiceleftwait = input("You arrive to the island unharmed.  There is a house with 3 doors.  One red, one yellow, and one blue.  Which color do you choose?  ").lower()
        if choiceleftwait == "red" or choiceleftwait == "Red":
            print("There is a room with fire.  You die.  Game Over.")
        elif choiceleftwait == "yellow" or choiceleftwait == "Yellow":
            print("You see a golden shrine.  The treasure is yours.  You win! ")
        elif choiceleftwait == "blue" or choiceleftwait == "Blue":
            print("You return to the lake.  The waves are too much to bear.  You become exhausted in the water and drown.  GAME OVER. ")
        else:
            print("That's an invalid input!") 
    elif choiceleft == "swim" or choiceleft == "Swim":
        print("You become exhausted and drown.  GAME OVER. ")
    else:
        print("That's an invalid input!") 
else:
    print("That's an invalid input!")
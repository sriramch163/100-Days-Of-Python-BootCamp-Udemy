

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('Your\'re at a crossroad, where do you want to go? \nType '
                '"left" or "right".').lower()

if choice1 == "left":
    print("Congrats on level - 1")
    choice2  = input('You\'ve come to a lake. There is an island in the '
                     'middle of the lake. Type "wait" to wait for a boat. '
                     'Type "swim" to swim across the river').lower()
    if choice2 == "wait":
        print("Congrats on level - 2")
        choice3 = input("You have arrive at the island unharmed. There is house"
              "with 3 doors. One red, One Yellow, One blue. What would"
              "you choose?").lower()
        if choice3 == "red":
            print("Its a full of fire")
            print("GAME OVER")
        elif choice3 == "blue":
            print("You enter into the ocean")
            print("GAME OVER")
        elif choice3 == "yellow":
            print("Congratulations on your adventure, You won treasure")
        else:
            print("GAME OVER")
    else:
        print("You got attacked by the crocodiles")
        print("GAME OVER")
else:
    print("You fell into a hole. GAME OVER")

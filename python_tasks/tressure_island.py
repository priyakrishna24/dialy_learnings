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

print("********Welcome to the tressure island******")
print("Your mission is to find the tressure")
choice1=input("You are at a cross road ,where do you want to go? Type 'left' or 'right' :" )

if choice1=='left':
    choice2=input('You\'ve come to the lake. There is an island in the middle of the lake.\n\tType "wait" to wait for a boat. Type "swim" to swim accross')

    if choice2=='wait':
        choice3=input('You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, One yellow and one Blue. Which colour do you choose? ')
        if choice3=='red':
            print('Burned by fire.\n\tGame Over.')
        elif choice3=='blue':
            print('Eaten by beasts.\n\tGame Over.')
        elif choice3=='yellow':
            print('You win!')
        else:
            print('Game Over')

    else:
        print('Attacked by trout.\n\tGame Over.')
else:
    print('Fall into a river.\nGame Over')



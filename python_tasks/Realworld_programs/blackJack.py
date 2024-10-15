import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

# player1= random.sample(cards,2)
# dealer1 = random.sample(cards,2)

# print(player1)
# print(dealer1)

player=[]
dealer=[]

choice1=input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
rep=True
while  rep:
    if choice1=='y':
        player=[random.sample(cards,2)]
        dealer=[random.sample(cards,2)]
        print(player)
        print(dealer)
        choice2=input("Type 'y' to get another card, type 'n' to pass: ")
        if choice2=='y':
            player.append(random.sample(cards,1))
            print(f"your total is {sum(player)}")
        elif choice2=='n':
            break
        else:
            input("Type 'y' to get another card, type 'n' to pass: ")
    else:
        pass

        





    print(player)
    print(dealer)
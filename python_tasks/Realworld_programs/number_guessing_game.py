import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
computer_choosen_number=random.randint(1,101)

if level=='easy':
    attempts=10
elif level=='hard':
    attempts=5
else:
    print("please select the correct level")



while(attempts):
    guess=int(input("Make a guess:"))

    if guess<computer_choosen_number:
        print("Too low")
        if attempts-1 == 0:
            print(f"SORRY")
        else:

            print(f"guess again.You have {attempts-1} remaining:")
    elif guess>computer_choosen_number:
        print("Too high")
        if attempts-1 == 0:
            print(f"SORRY")
        else:
            print(f"guess again.You have {attempts-1} remaining:")
    elif guess==computer_choosen_number:
        print("Your guess is correct")
        break
    attempts-=1



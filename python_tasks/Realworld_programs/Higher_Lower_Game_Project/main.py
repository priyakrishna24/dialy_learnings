from game_data import data
from logo import logo,vs
import random

print(logo)
score=0
def check(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
          
game_should_continue=True
b =random.choice(data)
while game_should_continue:
    a =b
    b =random.choice(data)

    if a ==b :
        b =random.choice(data)


    
    print(f"compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    guess=input(f"Who has more followers? Type 'A' or 'B' : ").lower()

    print("\n"*20)
    print(logo)

    a_followers=a['follower_count']
    b_followers=b['follower_count']

    is_correct=check(guess,a_followers,b_followers)
    if is_correct:
        score+=1
        print(f"you are right! Current score: {score}")
    else:
        print(f"sorry that's wrong!. Your final score: {score}")
        game_should_continue=False
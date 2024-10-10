
# max=0
# winner=""
def greatest_bid(dict):
    max=0
    winner=""
    for key in dict:
        if dict[key]>=max:
            max=dict[key]
            winner=key
    print(f"The winner is {winner} with a bid of {max}")


dict={}

rep=False
while not rep:
    name=input("What is your name?")
    bid=int(input("What's your bid? : $"))

    dict[name]=bid

    repetition=input("Are there any other bidders? Type 'yes' or 'no'")
    

    if repetition=='no':
        rep=True
        greatest_bid(dict)
    # elif repetition=='yes':
    #     print("\n"*50)
    # else:
    #     print("Please enter either 'yes' or 'no' ")
        

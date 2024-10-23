MENU = { 
    "espresso": {
         "ingredients": { 
             "water": 50, 
             "coffee": 18, 
             }, 
             "cost": 1.5, }, 
    "latte": { 
        "ingredients": {
             "water": 200, 
             "milk": 150, 
             "coffee": 24, 
        },
         "cost": 2.5,
    }, 
    "cappuccino": { 
        "ingredients": { 
            "water": 250, 
            "milk": 100, 
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
"water": 300,
"milk": 200,
"coffee": 100
}

def check_resources(drink,MENU,resources):
    ingredients=MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry, there is not enough {item}.")
    return True





is_continue=True
while(is_continue):
    choice=input("What would you like? (espresso/latte/cappuccino) or 'report' to see the resources or 'off' the program: ")

    if choice =='off':
        print("Thanks for visiting")
        is_continue=False
    elif choice=="report":
        print(f"Water:{resources['water']}")
        print(f"Milk:{resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money:")
    elif choice in MENU:
        if check_resources(choice,MENU,resources):
            cost = MENU[choice]["cost"]
            print(f"The cost of {choice} is ${cost}")
    else:
        print("Invalid choice")

MENU = { 
    "espresso": {
         "ingredients": { 
             "water": 50, 
             "coffee": 18, 
             }, 
             "cost": 1.5, 
    }, 
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

money = 0.0  # Initialize money to track sales

def check_resources(drink, MENU, resources):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False  # Return False if resources are not enough
    return True  # Return True if resources are sufficient

def deduct_resources(drink, MENU, resources):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

is_continue = True
while is_continue:
    choice = input("What would you like? (espresso/latte/cappuccino) or 'report' to see the resources or 'off' the program: ")

    if choice == 'off':
        print("Thanks for visiting")
        is_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice in MENU:
        if check_resources(choice, MENU, resources):
            cost = MENU[choice]["cost"]
            print(f"The cost of {choice} is ${cost}")
            payment = float(input("Please insert money: "))
            if payment >= cost:
                change = payment - cost
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                money += cost
                deduct_resources(choice, MENU, resources)  # Deduct resources after drink is made
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Unable to make your drink due to insufficient resources.")
    else:
        print("Invalid choice")

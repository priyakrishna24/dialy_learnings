

print('Welcome to the tip calculator!')

# Getting inputs from the user
bill = float(input('What was the total bill? '))
tip = float(input('How much tip would you like to give? 10, 12, or 15? '))
people = float(input('How many people to split the bill? '))

# Calculate the total amount each person needs to pay
amount = (bill + (bill * (tip / 100))) / people

# Display the result, rounded to 2 decimal places
print(f'Each person should pay: ${round(amount, 2)}')

print('welcome to the roller coaster\n')
 
#Getting the inputs from user

height=int(input('Enter your height:'))
bill=0


if height>=120:

    age=int(input('Enter your age:'))

    if age<=12:
        bill=5
        print('your ticket cost is 5')
    elif age<=18:
        bill=7
        print('your ticket cost is 7')
    else:
        bill=12
        print('your ticket cost is 12')

    want_photos=input("if you want photo? Type y for'yes' or n for 'no':")

    if want_photos=='y':
        bill+=3

    print(f'The total bill for riding rollercoaster including photo is {bill}')
    
else:
    print('sorry you have to grow taller')
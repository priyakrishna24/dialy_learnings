print('welcome to the roller coaster\n')
 
#Getting the inputs from user

height=int(input('Enter your height:'))


if height>=120:
    age=int(input('Enter your age:'))
    if age>18:
        print('your ticket cost is 12')
    else:
        print('your ticket cost is 7')
else:
    print('sorry you have to grow taller')
# def greet():
#     print('Hii')
#     print('This is priya')
#     print('Is everything okay right.')


# greet()

#Functions with names or values

def greet_with_name(name):          #Here name is an parameter, It is like an variable or else it is like a placeholder.
    print(f'Hii {name}')
    print(f'How are you, {name}')

greet_with_name('priya')            #   Here priya is an argument, It is the actual valve passed to the function.


#Functions with multiple names or values
def greet_with_multiple(name,location):         
    print(f'Hii {name}')
    print(f'How are you, {name}')
    print(f'What is the weather update in {location}')
greet_with_multiple('priya','Nellore')                      #This the positional arguments
greet_with_multiple(location='Nellore',name='priya')        #These are the keyword arguments

def life_in_weeks(age):
    
    x=(90-age)*52
    print(f'You have {x} weeks left.')
    
life_in_weeks(56)
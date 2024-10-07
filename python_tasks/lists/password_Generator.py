import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['%', '#', '$', '%', '&', '*', '(', ')', '+']

print('Welcome to pypassword Generator')
no_letters=int(input('How many letters would you like in your password?\n'))
no_numbers=int(input('How many numbers would you like in your password?\n'))
no_symbols=int(input('How many symbols would you like in your password?\n'))


# password_letters=random.choices(letters,k=no_letters)
# password_numbers=random.choices(numbers,k=no_numbers)
# password_symbols=random.choices(symbols,k=no_symbols)

# password_list=password_letters+password_numbers+password_symbols
# password = ''.join(map(str, password_list))
# print(password)


#Easyyyyyy levelllll

# password=''

# for char in range(1,no_letters+1):
#     random_char=random.choice(letters)
#     password+=random_char

# for char in range(1,no_symbols+1):
#     password+=random.choice(symbols)

# for char in range(1,no_numbers+1):
#     password+=str(random.choice(numbers))

# print(password)

# hardddd levelllll


password_list=[]

for char in range(1,no_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,no_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1,no_numbers+1):
    password_list.append(str(random.choice(numbers)))

#print(password_list)
random.shuffle(password_list)
password = ''.join(password_list)
print(password)
#Create anew list that contains names larger than 5 characters and all in CAPS

names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

new_list=[name.upper() for name in names if len(name)>5]
print(new_list)
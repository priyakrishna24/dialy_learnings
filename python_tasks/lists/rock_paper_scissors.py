import random

rock='''        _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
'''

paper='''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissors='''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''


choice=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 forScissors.\n'))

images=[rock,paper,scissors]

print(images[choice])


computer_choice=random.randint(0,2)

print('computer chose:')
if computer_choice==0:
   print(rock)
elif computer_choice==1:
    print(paper)
elif computer_choice==2:
    print(scissors)
else:
    print('Invalid choice. Choose from 0, 1 or 2')

if choice==computer_choice:
    print('You win')
else:
    print('You lose')

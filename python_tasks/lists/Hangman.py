import random

word_list=['priya','krishna','gayi','vishnu']

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=[''] * len(chosen_word)
print('current state : '+ ''.join(placeholder))
# placeholder=[]
# for position in range(1,len(chosen_word)+1):
#     placeholder+='_'
# print(placeholder)

while(1):
    guess=input('Guess a letter:\n').lower()

    # word1=''
    # for i in range(len(chosen_word)):
    #     if guess == chosen_word[i]:
    #         word1+=guess
    #     else:
    #         word1+='_'
    # print(word1)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                placeholder[i]=guess
    else:
        print(f'The guessed latter {guess} is not in chosen word')

    print("Current state: " + ' '.join(placeholder))

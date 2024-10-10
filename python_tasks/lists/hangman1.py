import random

word_list=['priya','krishna','gayi','vishnu']

chosen_word=random.choice(word_list)
print(chosen_word)

blanks=['_'] * len(chosen_word)
print(''.join(blanks))
#print('current state :' + ''.join(blanks))

gameover=False
lives=len(chosen_word)
while not gameover:

    guess=input('Guess a letter :\n')
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                blanks[i]=guess
        print('current state :' + ''.join(blanks))
    else:
        print(f'You guessed {guess}, that is not in the word.You lose a life')
        lives-=1
        print(f'********************{lives}/{len(chosen_word)}*****************')
        
        if lives==0:
            gameover=True
            print('gameover')

    if '_' not in blanks:
        gameover=True
        print('you win')

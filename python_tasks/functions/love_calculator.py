def calculate_love_score(name1,name2):
    name=(name1+name2).lower()

    true_letters='true'
    love_letters='love'

    true_count=0
    love_count=0

    true_counts = {}

    for letter in true_letters:
        if letter in true_letters:
            true_counts[letter]+=1


    for letter in name:
        true_count+=true_letters.count(letter)
        print(true_count)

    for letter in name:
        love_count+=love_letters.count(letter)
        print(love_count)

calculate_love_score('priya','krishna')
import pandas as pd

df=pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

file={row["letter"]:row["code"] for (index, row) in df.iterrows()}

# rep=True
# while(rep):
#     word=input("Enter a word: ").upper()
#     try:
#         output=[file[letter] for letter in word ]
#     except KeyError:
#         print("Sorry' Only letters in word please")
#     else:
#         print(output)
#         rep=False


def phonetic():
    word=input("Enter a word: ").upper()
    try:
        output=[file[letter] for letter in word ]
    except KeyError:
        print("Sorry' Only letters in word please")
        phonetic()
    else:
        print(output)

phonetic()
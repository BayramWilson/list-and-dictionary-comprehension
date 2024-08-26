import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter : row.code for (index, row) in df.iterrows()}
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list = [dict[letter] for letter in word]
    except KeyError:
        print("there are illegal values inside")
        generate_phonetic()
    else:
        print(list)
generate_phonetic()
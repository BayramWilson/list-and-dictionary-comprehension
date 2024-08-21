import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {new_key:new_value for (index, row) in df.iterrows()}
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter : row.code for (index, row) in df.iterrows()}
# print(dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
list = [dict[letter] for letter in word if letter in dict]
print(list)

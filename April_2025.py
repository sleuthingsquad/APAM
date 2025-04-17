import pandas


df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = (input("Enter a word:")).upper()
output = [nato_dict[character] for character in word]
print(output)

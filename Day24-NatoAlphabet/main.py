import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter : row.code for (index , row) in data.iterrows()}

input_name = input("Enter a word: ").upper()


new_list = [letter for letter in input_name]
print(new_list)

phonetic_list = [dic[letter] for letter in input_name]
print(phonetic_list)
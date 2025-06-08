import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter : row.code for (index , row) in data.iterrows()}


def gen_phenetic():
    input_name = input("Enter a word: ").upper()
    try:
        phonetic_list = [dic[letter] for letter in input_name]
    except KeyError:
        print(f"Sorry, only letters in the input please")
        gen_phenetic()
    else:
        print(phonetic_list)

gen_phenetic()



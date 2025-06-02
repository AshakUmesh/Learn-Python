PLACEHOLDER = "[name]"


with open("names", "r") as names_file:
    names_list = names_file.readlines()

with open("letter", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"./LetterFolder/letter_for_{stripped_name}.txt",mode="w") as final_letter:
            final_letter.write(new_letter)





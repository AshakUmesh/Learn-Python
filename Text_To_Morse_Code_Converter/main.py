MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ' ': '/'
}

def main():
    input_string = input("Enter the string you want to convert: ").upper()
    string_to_morse(input_string)

def string_to_morse(input_string):
    try:
        for char in input_string:
            if char not in MORSE:
                raise ValueError(char)
    except ValueError as e:
        print(f"Invalid Character --> {e}")
        return
    else:
        char_list = [char for char in input_string]
        morse_list=[]
        for char in char_list:
            morse_list.append(MORSE[char])
        morse_string = " ".join(morse_list)
        with open("Morse.txt", "a") as file:
            file.write(f"{morse_string}\n")
        print(morse_string)


if __name__ == '__main__':
    main()








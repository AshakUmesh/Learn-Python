import random

hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list=["apple","rhythms", "gypsy", "pharaoh", "crypts", "oxymoron", "jinx", "zephyr", "brouhaha", "psoriasis", "queue", "memento", "sphinx", "quorum", "fluffiness", "jigsaw", "whiskey", "quizzes", "lynx" ]

chosen_word=random.choice(word_list)
life=0
n=7
placeholder = ""
word_lenght = len(chosen_word)

print("Guess the word\t",end="")

for i in range(0,word_lenght):
    placeholder+="_"

print(placeholder)

game_over=False
correct_letter=[]

while(game_over==False):
    guess = input("Guess the Letter:    ").lower()
    display="";
    if guess in correct_letter:
        print(f"You have already Guessed :{guess}   ")
    if guess not in chosen_word:
        print(f"You guessed {guess} you loose a life    ")
        print(hangman[life])
        life = life + 1
        n=n-1;
        print(f"        ******************** {n} LIVES LEFT ************************        ")
        if life > 6:
            print(" You Loose ")
            break;


    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"


    print(display)


    if "_" not in display:
        game_over=True
        print("         You Win        ")
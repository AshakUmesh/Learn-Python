import random

print("Welcome to number guessing game! ")
print("I am thinking of a number between 1 and 100")
guess = -1
value = random.randint(1,101)

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choice == "easy":
    guess=10
    print("You have 10 attempts to guess the guess")

if choice == "hard":
    guess=5
    print("You have 5 attempts to guess the guess")

while guess != 0:
    num=int(input("Make a guess: "))
    guess -= 1
    if num < value:
        print("Too Low")
        print("Guess again")
        print(f"You have {guess} attempts remaining to guess the number")
    elif num > value:
        print("Too High")
        print("Guess again")
        print(f"You have {guess} attempts remaining to guess the number")
    elif num == value:
        print("You Guessed Correctly, You Win!")
        break
    if guess == 0:
        print("You have run out of guesses, You Loose.")
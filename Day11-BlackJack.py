import random  #start
def deal_card():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)


def calculate_score(lists):
    if sum(lists) == 21 and len(lists) == 2:
        return 0
    if 11 in lists and sum(lists) > 21:
        lists.remove(11)
        lists.append(1)
    return sum(lists)

def compare(user_score,computer_score):
    if user_score==computer_score:
        print("Draw")
    elif computer_score==0:
        print("BlackJack You Loose")
    elif user_score==0:
        print("BlackJack You Win ")
    elif user_score>21:
        print("You went Over ,You Loose")
    elif computer_score>21:
        print("Computer went over, You Win")
    elif computer_score > user_score:
        print("You Loose")
    elif computer_score < user_score:
        print("You Win ")



def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(0, 2):
        user_cards.append(deal_card())
    computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        print(f"Your cards {user_cards} , Your Score {user_score}")
        computer_score=calculate_score(computer_cards)
        print(f"Compters cards {computer_cards} , Compters Score {computer_score}")

        if user_score==0 or computer_score==0 or user_score>21:
                is_game_over = True
        else:
            user_choice=input("Type 'y' to get another card , type 'n' to pass: ")
            if user_choice=="y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and computers final hand is {computer_cards}")
    compare(user_score,computer_score)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n'") == "y":
     play_game()
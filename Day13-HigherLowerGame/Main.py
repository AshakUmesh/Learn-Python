import random
import game_data
def higher_lower_game():
    print("""                 
               / / / (_)___ _/ /_  ___  _____
              / /_/ / / __ '/ __ \/ _ \/ ___/
             / __  / / /_/ / / / /  __/ /
            /_/ ///_/\__, /_/ /_/\___/_/
               / /  /____/_      _____  _____
              / /   / __ \ | /| / / _ \/ ___/
             / /___/ /_/ / |/ |/ /  __/ /
            /_____/\____/|__/|__/\___/_/  """)
    point=0
    game_over = False
    n =random.randint(0, 49)
    entry1 = game_data.data[n]

    while game_over is False:
        print(f"\nCompare A: {entry1['name']}, {entry1['description']}, {entry1['country']}")

        print("""\t\t\t| |  / /____
            | | / / ___/
            | |/ (__  ) 
            |___/____(_) """)
        m=random.randint(0,49)

        while m==n:
            m=random.randint(0,49)

        entry2 = game_data.data[m]
        print(f"Compare B: {entry2['name']}, {entry2['description']}, {entry2['country']}\n")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice not in ['A','B']:
            print(f"\nEntered invalid code You have won {point} points")

            break

        if choice == "B":
            if entry2['follower_count'] > entry1['follower_count']:
                entry1 = entry2
                point+=1
            else:
                print(f"\nGame Over! You have won {point} points ")
                print(f"\n{entry1['name']}: {entry1['follower_count']} million followers\n")
                print(f"{entry2['name']}: {entry2['follower_count']} million followers\n")
                game_over = True

        if choice == "A":
            if entry1['follower_count'] > entry2['follower_count']:
                point+=1
            else:
                print(f"\nGame Over! You have won {point} points")
                print(f"\n{entry1['name']}: {entry1['follower_count']} million followers\n")
                print(f"{entry2['name']}:{entry2['follower_count']} million followers\n")
                game_over = True

while True:
    play = input("Do you want to play? (y/n): ").strip().lower()
    if play == 'y':
        higher_lower_game()
        retry = input("Do you want to retry? (y/n): ").strip().lower()
        if retry == 'y':
            higher_lower_game()
        elif retry == "n":
            print("Thanks for playing!\n")
            break
    elif play == 'n':
        print("Goodbye!\n")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")



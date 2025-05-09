import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

item = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock ,1 for Paper or 2 for Scissors "))

if user_choice>2:
    print("Invalid Entry")
else:
    print(f"User choose {item[user_choice]}")

system_choice = random.randint(0,2)


if (system_choice==user_choice):
    print(f"\nSystem Choose {item[system_choice]}\n DRAW")
elif (user_choice==0):
    if(system_choice==1):
        print(f"\nSystem Choose {item[system_choice]}\nYou Lost ")
    elif(system_choice==2):
        print(f"\nSystem Choose {item[system_choice]}\n You Win ")
elif (user_choice==1):
    if(system_choice==2):
        print(f"\nSystem Choose {item[system_choice]}\n You Lost")
    elif(system_choice==0):
        print(f"\nSystem Choose {item[system_choice]} \n You Win")
elif (user_choice==2):
    if(system_choice==0):
        print(f"\nSystem Choose {item[system_choice]}\n You Lost")
    elif(system_choice==1):
        print(f"\nSystem Choose {item[system_choice]}\n You Win")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
direction = str(input("Type left or right "))
if direction=="left":
    direction1=str(input("do you want to swim or wait "));
    if direction1=="swim":
        print("Game Over Better Luck Next Time ")
    if direction1=="wait":
        direction2=str(input("Which door? red or blue or yellow "));
        if direction2=="blue":
            print("Game Over Better Luck Next Time ")
        elif direction2=="red":
            print("Game Over Better Luck Next Time ")
        else:
            print("You Win! Congrats")

if direction=="right":
    print("Game Over Better Luck Next Time ")
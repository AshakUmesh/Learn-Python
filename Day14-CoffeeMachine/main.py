import coffee_machine_menu
import ingredients_remaining
def calculate_money():
    """It is a funtion that calculate the total money added by user"""
    print("Please insert coin. ")
    quaters = int(input("How many quarters: "))
    dime = int(input("How many dime: "))
    nickle = int(input("How many nickle: "))
    pennies = int(input("How many pennies: "))
    total = 0.01 * pennies + 0.10 * dime + 0.05 * nickle + 0.25 * quaters
    return total

machine = "on"
total = 0

while machine == "on":
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # type report to know about ingredients remaining
    if choice == "latte":
        total=calculate_money()
        if ingredients_remaining.water < coffee_machine_menu.menu["latte"]["water"] :
            print("Sorry, there is not enough water")
        elif ingredients_remaining.coffee < coffee_machine_menu.menu["latte"]["coffee"] :
            print("Sorry, there is not enough coffee")
        elif ingredients_remaining.milk < coffee_machine_menu.menu["latte"]["milk"] :
            print("Sorry, there is not enough milk")
        else:
             if total >= coffee_machine_menu.menu["latte"]["money"]:
                print(f"Here is ${total - coffee_machine_menu.menu['latte']['money']} in change")
                ingredients_remaining.water -= coffee_machine_menu.menu["latte"]["water"]
                ingredients_remaining.coffee -= coffee_machine_menu.menu["latte"]["coffee"]
                ingredients_remaining.milk -= coffee_machine_menu.menu["latte"]["milk"]
                ingredients_remaining.money += coffee_machine_menu.menu["latte"]["money"]
                print("Enjoy your latte ☕")
             else:
                 print("That is not enough money. Money refunded")

    elif choice == "espresso":
        total = calculate_money()
        if ingredients_remaining.water < coffee_machine_menu.menu["espresso"]["water"] :
            print("Sorry, there is not enough water")
        elif ingredients_remaining.coffee < coffee_machine_menu.menu["espresso"]["coffee"] :
            print("Sorry, there is not enough coffee")
        elif ingredients_remaining.milk < coffee_machine_menu.menu["espresso"]["milk"] :
            print("Sorry, there is not enough milk")
        else:
            if total >= coffee_machine_menu.menu["espresso"]["money"]:
                print(f"Here is ${total - coffee_machine_menu.menu['espresso']['money']} in change")
                ingredients_remaining.water -= coffee_machine_menu.menu["espresso"]["water"]
                ingredients_remaining.coffee -= coffee_machine_menu.menu["espresso"]["coffee"]
                ingredients_remaining.milk -= coffee_machine_menu.menu["espresso"]["milk"]
                ingredients_remaining.money += coffee_machine_menu.menu["espresso"]["money"]
                print("Enjoy your espresso ☕")
            else:
                print("That is not enough money. Money refunded")


    elif choice == "cappuccino":
        total = calculate_money()

        if ingredients_remaining.water < coffee_machine_menu.menu["cappuccino"]["water"] :
            print("Sorry, there is not enough water")
        elif ingredients_remaining.coffee < coffee_machine_menu.menu["cappuccino"]["coffee"] :
            print("Sorry, there is not enough coffee")
        elif ingredients_remaining.milk < coffee_machine_menu.menu["cappuccino"]["milk"] :
            print("Sorry, there is not enough milk")
        else:
            if total >= coffee_machine_menu.menu["cappuccino"]["money"]:
                print(f"Here is ${total - coffee_machine_menu.menu['cappuccino']['money']} in change")
                ingredients_remaining.water -= coffee_machine_menu.menu["cappuccino"]["water"]
                ingredients_remaining.coffee -= coffee_machine_menu.menu["cappuccino"]["coffee"]
                ingredients_remaining.milk -= coffee_machine_menu.menu["cappuccino"]["milk"]
                ingredients_remaining.money += coffee_machine_menu.menu["cappucino"]["money"]
                print("Enjoy your cappuccino ☕")
            else:
                print("That is not enough money. Money refunded")

    elif choice == "off":
        machine = "off"

    elif choice == "report":
        print(f"water = {ingredients_remaining.water}")
        print(f"coffee = {ingredients_remaining.coffee}")
        print(f"milk = {ingredients_remaining.milk}")
        print(f"money = {ingredients_remaining.money}")

    else :
        print("Enter a valid input. ")


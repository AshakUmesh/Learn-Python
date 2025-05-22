from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = "on"
money_machine = MoneyMachine()
machine_menu = Menu()
order = CoffeeMaker()

while machine == "on":
    options = machine_menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()

    if choice == "report":
        order.report()
        money_machine.report()
    elif choice == "off":
        machine = "off"
    else:
        drink = machine_menu.find_drink(choice)
        if order.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                order.make_coffee(drink)

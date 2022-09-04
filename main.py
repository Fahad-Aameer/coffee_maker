from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_menu = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()

machine_on = True
while machine_on:
    order_name = input("What would you like? (espresso/latte/cappuccino/):")
    if order_name == 'off':
        machine_on = False
    elif order_name == 'report':
        item_report = make_coffee.report()
        money_report = money.report()
        print(f"{item_report}\n{money_report}")
    else:
        choice = coffee_menu.find_drink(order_name)
        enough_resources = make_coffee.is_resource_sufficient(choice)
        if enough_resources:
            enough_money = money.make_payment(choice.cost)
            if enough_money:
                make_coffee.make_coffee(choice)

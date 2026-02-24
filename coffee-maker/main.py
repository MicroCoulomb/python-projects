from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

shop_open = True
my_coffee = CoffeeMaker()
my_money = MoneyMachine()
my_menu = Menu()

while shop_open:
    order = str(input(f"What would you like to order? [{my_menu.get_items()}]: ")).lower()
    if order == "off":
        print("Shop closed.")
        shop_open = False
    elif order == "report":
        my_coffee.report()
        my_money.report()
    else:
        user_order = my_menu.find_drink(order)
        if order in my_menu.get_items():
            if my_coffee.is_resource_sufficient(user_order):
                if my_money.make_payment(user_order.cost):
                    my_coffee.make_coffee(user_order)
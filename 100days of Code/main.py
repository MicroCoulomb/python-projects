MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_enough(o_ingredients):
    lack_ingredient = []
    for ingredient in o_ingredients:
        if o_ingredients[ingredient] > resources[ingredient]:
            lack_ingredient.append(ingredient)
    if not lack_ingredient:
        return True
    else:
        print("Sorry there is not enough " + " & ".join(lack_ingredient))
        return False

def use_resources(o_ingredients):
    for ingredient in o_ingredients:
        resources[ingredient] -= o_ingredients[ingredient]

profit = 0
shop_open = True

while shop_open:
    order = str(input("What would you like to order? (espresso/latte/cappuccino): ")).lower()

    if order == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    elif order == "off":
        print("Machine Turn off. Maintenance")
        shop_open = False
        break
    elif check_enough(MENU[order]["ingredients"]):
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        order_price = MENU[order]["cost"]
        user_payment = 0.01 * pennies + 0.05 * nickles + 0.10 * dimes + 0.25 * quarter
        order_change = user_payment - order_price

        if user_payment < order_price:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${order_change:.2f} in change.")
            profit += order_price
            use_resources(MENU[order]["ingredients"])
            print(f"Here is your {order}. Enjoy!")
from data import MENU, profit, resources

def check_resources(chosen_drink_ingredient):
    """Check the inventory to confirm the ingredients return booleans in case resources aren't sufficient"""
    for item in chosen_drink_ingredient:
        if chosen_drink_ingredient[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.​")
            return False
    return True

def process_coins():
    """Receives money prompt and returns total"""
    total = int(input("How many quarters:  ")) * 0.25
    total += int(input("How many dimes:  ")) * 0.10
    total += int(input("How many nickles:  ")) * 0.05
    total += int(input("How many pennies:  ")) * 0.01
    return total

def is_transaction_successful(received_payment, drink_cost):
    """checks if received payment is enough for the coffee and returns boolean"""
    if received_payment >= drink_cost:
        change = round(received_payment - drink_cost, 2)
        print(f"Here is $2.45 dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
                
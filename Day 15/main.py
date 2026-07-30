# Coffee Machine project
no_more_coffee = False

def check_resources(resources):

def make_coffee():
    resources = {'water' : 300, 'milk' : 200, 'coffee' : 100, 'money' : 0,}
    

    choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if choice == 'off':
        no_more_coffee = True
    elif choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        


while not no_more_coffee:
    make_coffee()
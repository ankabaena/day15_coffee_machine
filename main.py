# This is a coffee machine script, day 15 from Angela Yu's Udemy Python course

from data import MENU, resources


def report():
    '''print the current resources of the machine'''
    # for key in resources:
    #   print(f"{key.title()}: {resources[key]}ml")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def calculate_resources(coffee):
    """calculates if enough resources for coffee ordered, returns True or False"""
    for key in MENU[coffee]['ingredients']:
        if MENU[coffee]['ingredients'][key] > resources[key]:
            print(f'Sorry, there is not enough {key}.')
            return False
        else:
            return True


def pay(coffee):
    '''asks for coins to pay for the coffee'''
    print("Please insert coins: ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    change = paid - MENU[coffee]['cost']
    if change >= 0:
        print(f"Here is ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def reduce_resources(coffee):
    '''reduces the resources by the amount that was used '''
    resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']


more_coffee = True
money = 0
while more_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        more_coffee = False
    elif choice == "report":
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if calculate_resources(choice):
            if pay(choice):
                money += MENU[choice]['cost']
                print(f"Here is your {choice}. Enjoy!")
                reduce_resources(choice)

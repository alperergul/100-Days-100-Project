from regex import P
from sqlalchemy import true
from dataset import menu, resources


def throw_prompt():
    print("""
1. espresso
2. latte
3. cappuccino
4. report
5. exit
    """)
    return input("What do you want? : ")


def check_resources(choice):
    if(choice != 'espresso'):
        milk = menu[choice]['ingredients']['milk']
        water = menu[choice]['ingredients']['water']
        coffee = menu[choice]['ingredients']['coffee']

        if resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= coffee:
            return True
        else:
            return False
    else:
        water = menu[choice]['ingredients']['water']
        coffee = menu[choice]['ingredients']['coffee']
        if resources['water'] >= water and resources['coffee'] >= coffee:
            return True
        else:
            return False


def total_coins():

    quarter = int(input("How many quarters do you want to put in? : "))
    dimes = int(input("How many dimes do you want to put in? : "))
    nickels = int(input("How many nickels do you want to put in? : "))
    pennies = int(input("How many pennies do you want to put in? : "))

    return quarter * .25 + dimes * .10 + nickels * .05 + pennies * .01


def check_user_money(money, choice):
    if money < menu[choice]['cost']:
        return False
    else:
        return True


def coffee_machine():
    resources['money'] = 0
    while True:
        choice = throw_prompt()
        if choice == "1":
            print("espresso")
            if(not check_resources('espresso')):
                print("Sorry, not enough resources!")
                continue
            else:
                user_money = total_coins()
                change = user_money - menu['espresso']['cost']
                if(check_user_money(user_money, 'espresso')):
                    resources['money'] += menu['espresso']['cost']
                    resources['water'] -= menu['espresso']['ingredients']['water']
                    resources['coffee'] -= menu['espresso']['ingredients']['coffee']
                    print(f"Here is your change: ${change.__round__(2)}")

                    print("Here's your espresso!")
        elif choice == "2":
            if(not check_resources('latte')):
                print("Sorry, not enough resources!")
                continue
            else:
                user_money = total_coins()
                change = user_money - menu['latte']['cost']
                if(check_user_money(user_money, 'latte')):
                    resources['money'] += menu['latte']['cost']
                    resources['water'] -= menu['latte']['ingredients']['water']
                    resources['milk'] -= menu['latte']['ingredients']['milk']
                    resources['coffee'] -= menu['latte']['ingredients']['coffee']
                    print(f"Here is your change: ${change.__round__(2)}")
                    print("Here's your latte!")

        elif choice == "3":
            print("cappuccino")
            if(not check_resources('cappuccino')):
                print("Sorry, not enough resources!")
                continue
            else:
                user_money = total_coins()
                change = user_money - menu['cappuccino']['cost']
                if(check_user_money(user_money, 'cappuccino')):
                    resources['money'] += menu['cappuccino']['cost']
                    resources['water'] -= menu['cappuccino']['ingredients']['water']
                    resources['milk'] -= menu['cappuccino']['ingredients']['milk']
                    resources['coffee'] -= menu['cappuccino']['ingredients']['coffee']
                    print(f"Here is your change: ${change.__round__(2)}")

                    print("Here's your cappuccino!")
        elif choice == "4":

            print(f"""
    water: {resources["water"]}
    milk: {resources["milk"]}
    coffee: {resources["coffee"]}
    money: ${resources["money"]}
            """)

            print("report")
        elif choice == "5":
            print('Bye!')
            break
        else:
            print("Invalid choice")


coffee_machine()

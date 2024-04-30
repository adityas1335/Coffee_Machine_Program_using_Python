# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}


def is_res_sufficient(items):
    for item in items:
        if items[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def payment_processing():
    opt = int(input("Select 1 for coins or 2 for QR Scan: "))
    if opt == 1:
        one = int(input("Enter ₹1 coins: "))
        two = int(input("Enter ₹2 coins: ")) * 2
        five = int(input("Enter ₹5 coins: ")) * 5
        ten = int(input("Enter ₹10 coins: ")) * 10

        total = one + two + five + ten
        return total
    else:
        total = int(input("Enter Amount Scan and Pay: "))
        return total


def return_change(change):
    print("")
    print(f"collect your ₹{change} change")


def is_payment_done(payments, drinks):
    if drinks['cost'] > payments:
        print("")
        print("Sorry that's not enough money")
        return False
    else:
        if payments > drinks['cost']:
            changes = payments - drinks['cost']
            return_change(changes)
        print("")
        print("Payment Successful✅")
        return True


def resources_updated(items):
    for item in items:
        resources[item] -= items[item]


def profit_update(profits, money):
    profits += money["cost"]
    return profits


profit = 0

is_on = True

while is_on:
    print("")
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice.lower() == 'off':
        is_on = False
    elif choice.lower() == 'report':
        print("")
        print(f'Milk: {resources["milk"]}')
        print(f'Water: {resources["water"]}')
        print(f'Coffee: {resources["coffee"]}')
    elif choice.lower() == 'profit':
        print(f'Money: ₹{profit}')
    else:
        drink = MENU[choice]
        if is_res_sufficient(drink['ingredients']):
            print("")
            print(f'Pay: ₹{drink["cost"]}')
            print("")
            payment = payment_processing()
            if is_payment_done(payment, drink):
                resources_updated(drink['ingredients'])
                profit = profit_update(profit, drink)
                print("")
                print(f"Here is your {choice} ☕. Enjoy!")
                print("Have a nice day!🙂")

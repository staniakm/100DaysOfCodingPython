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
    "coffee": 100
}

total_money = 0.0

COINS = [
    {"name": "penny", "value": 0.01},
    {"name": "nickel", "value": 0.05},
    {"name": "dime", "value": 0.10},
    {"name": "quarter", "value": 0.25},
]


def print_menu():
    for key in MENU:
        coffee = MENU[key]
        print(f"""{key}: cost: ${coffee['cost']}
        ingredients: {coffee['ingredients']}
""")


def decrease_resource(coffe):
    ingredients = coffe['ingredients']
    for key in ingredients:
        resources[key] -= ingredients[key]


def check_resources(coffe):
    required_ingredients = coffe['ingredients']
    is_enough = True
    for key in required_ingredients:
        if required_ingredients[key] > resources[key]:
            is_enough = False
            print(f"Sorry. not enough {key}")

    return is_enough


def calculate_total_payed(payed):
    total_payed = 0.0
    for coin in COINS:
        total_payed += coin['value'] * payed[coin['name']]
    return total_payed


def accept_coins_and_prepare_coffe():
    global total_money
    coffee = input("What type of coffe do you want (espresso/latte/cappuccino)?")
    selected_coffee = MENU[coffee]
    if check_resources(selected_coffee):
        cost = selected_coffee['cost']
        print(f"Coffee wil cost {cost}")
        print("How do you want to pay??")
        waiting_for_payment = True
        while waiting_for_payment:
            payment = {}
            for elem in COINS:
                coins = int(input(f"How many {elem['name']}"))
                payment[elem['name']] = coins
            total_money_payed = calculate_total_payed(payment)

            if total_money_payed >= cost:
                waiting_for_payment = False
                print(f"Start to prepare {coffee}")
                total_money += cost
                decrease_resource(selected_coffee)
                if total_money_payed > cost:
                    print(f"Here is your change {round(total_money_payed - cost, 2)}")
                print_report()
                print("Here is your coffe")
            else:
                waiting_for_payment = False
                print("Not enough money, returning money")


def calculate_coins():
    total_sum = 0.0
    for entry in COINS:
        total_sum += entry["value"]
    return round(total_sum, 2)


def print_report():
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${total_money}
    """)


running = True
while running:
    answer = input("What would you like to do (menu/coffe/report/off)?")

    if answer == "off":
        running = False
    elif answer == "report":
        print_report()
    elif answer == "coffee":
        accept_coins_and_prepare_coffe()
    elif answer == "menu":
        print_menu()
    else:
        print("Unknown command")

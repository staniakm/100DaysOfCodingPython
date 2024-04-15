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

COINS = [
    {"name": "penny", "value": 0.01},
    {"name": "nickel", "value": 0.05},
    {"name": "dime", "value": 0.10},
    {"name": "quarter", "value": 0.25},
]


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
    Money: ${calculate_coins()}
    """)


running = True
while running:
    answer = input("What would you like to do (report/coffe/off)?")
    if answer == "off":
        running = False
    elif answer == "report":
        print_report()

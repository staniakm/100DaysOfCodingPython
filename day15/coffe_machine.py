class MoneyMachine:
    total_money = 0.0
    COINS = [
        {"name": "penny", "value": 0.01},
        {"name": "nickel", "value": 0.05},
        {"name": "dime", "value": 0.10},
        {"name": "quarter", "value": 0.25},
    ]

    def calculate_total_payed(self, payed):
        total_payed = 0.0
        for coin in self.COINS:
            total_payed += coin['value'] * payed[coin['name']]
        return total_payed

    def calculate_coins(self):
        total_sum = 0.0
        for entry in self.COINS:
            total_sum += entry["value"]
        return round(total_sum, 2)

    def print_total_money(self):
        print(f"Money: ${self.total_money}")

    def calculate_coins_value(self):
        payment = {}
        for elem in self.COINS:
            coins = int(input(f"How many {elem['name']}"))
            payment[elem['name']] = coins
        return self.calculate_total_payed(payment)

    def accept_payment(self, cost):
        self.total_money += cost


class MenuModule:
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

    def print_menu(self):
        for key in self.MENU:
            coffee = self.MENU[key]
            print(f"""{key}: cost: ${coffee['cost']}
            ingredients: {coffee['ingredients']}
    """)

    def get_coffee(self):
        coffee = input("What type of coffe do you want (espresso/latte/cappuccino)?")
        return {"name": coffee, "attributes": self.MENU[coffee]}


class ResourcesModule:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }

    def decrease_resource(self, coffe):
        ingredients = coffe['ingredients']
        for key in ingredients:
            self.resources[key] -= ingredients[key]

    def check_resources(self, coffe):
        required_ingredients = coffe['ingredients']
        is_enough = True
        for key in required_ingredients:
            if required_ingredients[key] > self.resources[key]:
                is_enough = False
                print(f"Sorry. not enough {key}")

        return is_enough

    def print_resources(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")


class CoffeMachine:
    money_module = MoneyMachine()
    menu_module = MenuModule()
    resources_module = ResourcesModule()

    def accept_coins_and_prepare_coffe(self):
        selected_coffee = self.menu_module.get_coffee()
        if self.resources_module.check_resources(selected_coffee['attributes']):
            cost = selected_coffee['attributes']['cost']
            print(f"Coffee wil cost {cost}")
            print("How do you want to pay??")
            waiting_for_payment = True
            while waiting_for_payment:

                total_money_payed = self.money_module.calculate_coins_value()

                if total_money_payed >= cost:
                    waiting_for_payment = False
                    print(f"Start to prepare {selected_coffee['name']}")
                    self.money_module.accept_payment(cost)
                    self.resources_module.decrease_resource(selected_coffee['attributes'])
                    if total_money_payed > cost:
                        print(f"Here is your change {round(total_money_payed - cost, 2)}")
                    self.print_report()
                    print("Here is your coffe")
                else:
                    waiting_for_payment = False
                    print("Not enough money, returning money")

    def print_report(self):
        self.resources_module.print_resources()
        self.money_module.print_total_money()

    def start(self):
        print("Starting coffe machine")
        running = True
        while running:
            answer = input("What would you like to do (menu/coffe/report/off)?")

            if answer == "off":
                running = False
            elif answer == "report":
                self.print_report()
            elif answer == "coffee":
                self.accept_coins_and_prepare_coffe()
            elif answer == "menu":
                self.menu_module.print_menu()
            else:
                print("Unknown command")

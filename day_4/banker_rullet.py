import random

names = ["Joe", "Paul", "Emily", "Aleksandra"]

name = names[random.randint(0, len(names) - 1)]

print(f"{name} will pay the bill")

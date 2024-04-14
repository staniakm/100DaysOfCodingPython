import random

from art import logo, vs
from gme_data import data


def pick_second(first_selection):
    second_pick = random.choice(data)
    while first_selection == second_pick:
        second_pick = random.choice(data)
    return second_pick


print(logo)

running = True
correct_count = 0
while running:
    print("Who has more followers?")
    first = random.choice(data)
    second = pick_second(first)
    print(f"1. {first['name']} - {first['description']}")
    print(vs)
    print(f"2. {second['name']} - {second['description']}")
    answer = input()
    if answer == "1" and first['follower_count'] > second['follower_count']:
        correct_count += 1
        print("Correct")
    elif answer == '2' and first['follower_count'] < second['follower_count']:
        correct_count += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"You get {correct_count} points")
        running = False

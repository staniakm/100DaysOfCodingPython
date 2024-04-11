print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

decision = input("You are standing on a crossroad. You can go 'left' or 'right'")
if decision.lower() == 'right':
    print("You have been attacked by bandits and killed")
    print("Game Over")
else:
    print("After short time you have reached a lake")
    print("You see an island in the middle of lake")
    decision = input("You can try to 'swim' or 'wait' for boat")
    if decision.lower() == "swim":
        print("You are out of stamina and drowned")
        print("Game Over")
    else:
        print("You have reached an island")
        print("You see the house with 3 doors. 'red', 'blue', 'yellow'")
        decision = input("Which one fo you want to open")
        if decision.lower() == "yellow":
            print("You have found great treasure")
            print("Game Over")
        elif decision.lower() == "red":
            print("When you have opened the door, fireball hits you")
            print("You died in flames")
            print("Game Over")
        else:
            print("When you opened the door")
            print("Frost bolt hits you")
            print("You have died frozen to death")

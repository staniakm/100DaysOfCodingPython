import random

values = ["ROCK", "SCISSORS", "PAPER"]
computer = values[random.randint(0, 2)]
computer_result = values.index(computer)

player = input("Choose rock, scissors, paper").upper()

player_result = values.index(player)

print(f"Player select {player}, computer select {computer}")
if (player_result == computer_result):
    print("Draw")
elif (player_result == 0 and computer_result == 1
      or player_result == 1 and computer_result == 2
      or player_result == 2 and computer_result == 0):
    print("Player won")
else:
    print("Computer won")

# Number Guessing Game Objectives:
import random


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def game():
    running = True
    while running:
        mode = input("Pick difficulty (easy, hard)")
        if mode == "easy":
            no_of_lives = 10
        else:
            no_of_lives = 5
        print("Gues the number")
        random_number = random.randint(0, 100)

        guessing = True
        while guessing and no_of_lives > 0:
            guess = int(input("What is your guess?"))
            if guess == random_number:
                print(f"Congrats, you guess it and still have {no_of_lives} lives")
                guessing = False
            else:
                print("Failed to guess")
                no_of_lives -= 1
                if guess > random_number:
                    print("Too high")
                else:
                    print("Too low")

        if no_of_lives == 0:
            print(f"Failed to guess the number: {random_number}")

        answer = input("Do you want to play again?")
        if answer == "no":
            running = False


game()

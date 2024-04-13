# Step 1
import random

no_of_tries = 6
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_to_guess = list(random.choice(word_list))

guessed_letters = []

for l in word_to_guess:
    guessed_letters.append("_")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
complete = False
print(guessed_letters)
while not complete and no_of_tries > 0:
    user_letter = input("Guess the letter")

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    if user_letter in word_to_guess:
        for l in range(0, len(word_to_guess)):
            if user_letter == word_to_guess[l]:
                guessed_letters[l] = user_letter

        if "_" not in guessed_letters:
            complete = True
            print("Congrats, You have won")
        print(guessed_letters)
    else:
        print(f"User letter {user_letter} is NOT in word")
        print("You have lost one chance")
        no_of_tries -= 1
        if no_of_tries == 0:
            print("You have lost :(")
            print(word_to_guess)

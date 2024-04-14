############### Blackjack Project #####################
import random

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def draw_card(player_cards, no_of_cards):
    for i in range(0, no_of_cards):
        player_cards.append(deal_card())


def calculate_score(user_list):
    cards_sum = sum(user_list)
    if cards_sum > 21:
        if user_list.count(11):
            user_list.remove(11)
            user_list.append(1)
        return sum(user_list)
    else:
        return cards_sum


def check_blackjack(user_cards, computer_cards):
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    if len(computer_cards) == 2 and len(user_cards) == 2 and (computer_score == 0 or user_score == 0):
        print("Black jack")
        print(len(computer_cards))
        if computer_score == 0:
            print(f"Computer won with score {calculate_score(computer_cards)}")
        else:
            print(f"Player won with score {calculate_score(user_cards)}")
        return True
    else:
        return False


def check_winning(user_cards, computer_cards):
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)

    if computer_score > user_score:
        print("Computer won")
        print(f"Player score: {user_score}\nComputer score: {computer_score}")
    elif computer_score < user_score:
        print("Player won")
        print(f"Player score: {user_score}\nComputer score: {computer_score}")
    else:
        print("Draw")
        print(f"Player score: {user_score}\nComputer score: {computer_score}")


def check_overlap(total_cards):
    return calculate_score(total_cards) > 21


def reset_new_game(user_cards, computer_cards):
    print("""############################ PREPARING TABLE ##################################""")
    draw_card(user_cards, 2)
    draw_card(computer_cards, 2)


def start_game(new_game):

    while new_game:
        user_cards = []
        computer_cards = []
        reset_new_game(user_cards, computer_cards)
        print("""############################ START NEW GAME ##################################""")

        if check_blackjack(user_cards, computer_cards):
            answer = input("Do you want to play again?")
            if answer == "no":
                break
        else:
            next_card = True
            while next_card and not check_blackjack(user_cards, computer_cards):
                user_score = calculate_score(user_cards)
                print(f"You have already: {user_score} points")
                print(user_cards)
                answer = input("Do you want to draw another card (yes/no)?")
                if answer == "no":
                    next_card = False
                else:
                    draw_card(user_cards, 1)

            if check_overlap(user_cards):
                print(f"Player lost with total {calculate_score(user_cards)}")
            else:

                while not check_blackjack(user_cards, computer_cards) and calculate_score(computer_cards) < 17:
                    print("Computer draw another card")
                    draw_card(computer_cards, 1)

                print(f"Computer cards: {computer_cards}")
                if check_overlap(computer_cards):
                    print(f"Computer lost with score: {calculate_score(computer_cards)}")
                else:
                    check_winning(user_cards, computer_cards)

            answer = input("Do you want to start again?")
            if answer == "yes":
                new_game = True
            else:
                new_game = False


start_game(True)

print("Game over")

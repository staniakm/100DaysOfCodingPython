from os import system

bids = []


def calculate_winner(bids):
    winner = ""
    price = 0
    for bidder in bids:
        if bidder["value"] > price:
            winner = bidder["name"]
            price = bidder["value"]
    print(f"Winner is {winner} with price {price}")


finish = False
while not finish:
    name = input("What is your name")
    bid = int(input("What is  your bid"))
    bids.append({
        "name": name,
        "value": bid
    })
    others = input("Are there any other bidders (yes/no) ?")

    if others == 'no':
        finish = True
    system('cls') # not working

calculate_winner(bids)

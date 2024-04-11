# to ride a rollecoster one have to be at least 120 cm
# additional requirement, if age < 12 then one pay 7$ else 12$
# new requirement when age < 12 than cost is 5, between 12 and 18 7$ else 12$
# midlife crisis - ppl 45-55 ride for free

min_allowed_height = 120
height = int(input("What is your height (in cm)?"))

if height >= min_allowed_height:
    print("You can buy a ticket")
    ticket_price = 0
    age = int(input("What is your age?"))
    if age < 12:
        ticket_price = 5
    elif 12 <= age <= 18:
        ticket_price = 7
    elif age >= 45 and age <= 55:
        ticket_price = 0
    else:
        ticket_price = 7
    photo = bool(input("Do you want photo?"))
    if photo:
        ticket_price += 3
    print(f"Ticket will cost {ticket_price}")

else:
    print("Your height is not enough")

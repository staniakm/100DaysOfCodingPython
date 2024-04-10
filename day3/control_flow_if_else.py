# to ride a rollecoster one have to be at least 120 cm
# additional requirement, if age < 12 then one pay 7$ else 12$
# new requirement when age < 12 than cost is 5, between 12 and 18 7$ else 12$

min_allowed_height = 120
height = int(input("What is your height (in cm)?"))

if height >= min_allowed_height:
    print("You can buy a ticket")
    age = int(input("What is your age?"))
    if age < 12:
        print("Ticket cost is 5$")
    elif 12 <= age <= 18:
        print("Ticket cost 7$")
    else:
        print("Ticket cost full price 12$")
else:
    print("Your height is not enough")

# to ride a rollecoster one have to be at least 120 cm
# additional requirement, if age < 12 then one pay 7$ else 12$


min_allowed_height = 120
lower_cost_age = 12
height = int(input("What is your height (in cm)?"))

if height >= min_allowed_height:
    print("You can buy a ticket")
    age = int(input("What is your age?"))
    if age >= lower_cost_age:
        print("Ticket cost is 12$")
    else:
        print("Ticket cost 7$")
else:
    print("Your height is not enough")

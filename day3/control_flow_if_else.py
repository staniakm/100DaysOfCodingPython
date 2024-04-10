# to ride a rollecoster one have to be at least 120 cm

min_allowed_height = 120
height = int(input("What is your height (in cm)?"))

if (height >= min_allowed_height):
    print("You can buy a ticket")
else:
    print("Your height is not enough")

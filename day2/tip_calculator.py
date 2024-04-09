# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

bill = float(input("What is the bill value?"))
tip = int(input("What is the tip percentage value (5,10,15,20..)"))
no_of_ppl = int(input("For how many ppl split the bill?"))

print(round(((bill / no_of_ppl) * (100 + tip) / 100), 2))

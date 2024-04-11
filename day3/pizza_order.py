### pizza order processor
# pizza size:
# Small (s) 15$
# medium (m) 20$
# large (l) 25$
# pepperoni on small (Y or N) +2$
# peperoni on large/medium +3$
# extra cheese +1$

print("Thank you for choosing Pizza Automate")
size = input("What size of pizza do you want to order (S,M,L) ?")
add_pepperoni = input("Do you want pepperoni (Y,N)?")
extra_cheese = input("Do you want extra cheese (Y,N) ?")

bill = 0

if extra_cheese == 'Y':
    bill += 1

if size == 'S':
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
print(f"Your order is ready, it cost {bill}")

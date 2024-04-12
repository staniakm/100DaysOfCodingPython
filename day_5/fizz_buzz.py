# Fizz if / 3
# Buzz if /5
# FizzBuzz if /3 and /5

for i in range(0, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
